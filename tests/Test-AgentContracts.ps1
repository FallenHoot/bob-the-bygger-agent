#requires -Version 7.0
<#
.SYNOPSIS
Read-only static regression checks for BTBA source contracts.
.DESCRIPTION
Run with & <script-path>, optionally -ProjectPath <folder>. The default does
not open projects. A supplied folder must use the current INDEX/project/decision
register and paired contractor-tender conventions tested below. No customer,
project location, release date, or engineering dimension is embedded here.

Exit 0 means all selected static checks passed; exit 1 means one or more failed.
This is not a model-behavior test, engineering verification, general Markdown or
YAML validator, or execution of the Python skill validator. It reads that
validator's STRING_FIELDS declaration only. No dependencies or writes are needed.

Keep this file in root tests/, not skills/tests/: the Python validator treats
each immediate skills/ directory as a skill requiring SKILL.md.
#>
[CmdletBinding()]
param([string] $ProjectPath)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$RepositoryRoot = Split-Path -Parent $PSScriptRoot
$Results = [System.Collections.Generic.List[object]]::new()
$SourceCache = @{}

function Assert-True {
    param([bool] $Condition, [string] $Message)
    if (-not $Condition) { throw $Message }
}

function Invoke-Check {
    param([string] $CheckLabel, [scriptblock] $Body)
    try {
        & $Body | Out-Null
        $Results.Add([pscustomobject]@{ Name = $CheckLabel; Passed = $true })
        Write-Output "PASS  $CheckLabel"
    }
    catch {
        $Results.Add([pscustomobject]@{ Name = $CheckLabel; Passed = $false })
        Write-Output "FAIL  $CheckLabel : $($_.Exception.Message)"
    }
}

function Read-Source {
    param([string] $Path)
    $full = [IO.Path]::GetFullPath($Path)
    if (-not $SourceCache.ContainsKey($full)) {
        Assert-True (Test-Path -LiteralPath $full -PathType Leaf) "Missing source: $full"
        $SourceCache[$full] = [IO.File]::ReadAllText($full)
    }
    return $SourceCache[$full]
}

function Read-Repo {
    param([string] $RelativePath)
    return Read-Source (Join-Path $RepositoryRoot $RelativePath)
}

function Get-SimbaRouteRow {
    param([string] $Text)
    # $ anchors before LF, not before CRLF; permit a CR without capturing it.
    return [regex]::Match($Text, '(?m)^(?<row>\|[^\r\n]*SIMBA[^\r\n]*)\r?$').Groups['row'].Value
}

function Remove-FencedCode {
    param([string] $Text)
    # CommonMark-style backtick/tilde fences, including quoted fences and
    # longer outer fences. Keep blank lines so headings retain boundaries.
    $output = [System.Collections.Generic.List[string]]::new()
    $marker = ''; $length = 0
    foreach ($line in ($Text -split '\r?\n')) {
        $candidate = $line -replace '^\s*(?:>\s*)+', ''
        if ($marker) {
            if ($candidate -match ('^ {0,3}' + [regex]::Escape($marker) + '{' + $length + ',}\s*$')) {
                $marker = ''; $length = 0
            }
            $output.Add('')
        }
        elseif ($candidate -match '^ {0,3}(`{3,}|~{3,})(.*)$') {
            $fence = $Matches[1]; $info = $Matches[2]
            if ($fence[0] -eq '`' -and $info.Contains('`')) { $output.Add($line); continue }
            $marker = [string]$fence[0]; $length = $fence.Length
            $output.Add('')
        }
        else { $output.Add($line) }
    }
    return $output -join "`n"
}

function Get-CurrentText {
    param([string] $Text)
    $visible = Remove-FencedCode $Text
    $boundary = [regex]::Match($visible, '(?im)^#{1,6}\s+Historical\s+Appendix\b')
    if ($boundary.Success) { return $visible.Substring(0, $boundary.Index) }
    return $visible
}

function Get-Section {
    param([string] $Text, [string] $Heading)
    $visible = Remove-FencedCode $Text
    $headings = [regex]::Matches($visible, '(?m)^(#{1,6})\s+(.+?)\s*#*\s*$')
    for ($i = 0; $i -lt $headings.Count; $i++) {
        $entry = $headings[$i]
        if ($entry.Groups[2].Value -notmatch $Heading) { continue }
        $end = $visible.Length
        for ($j = $i + 1; $j -lt $headings.Count; $j++) {
            if ($headings[$j].Groups[1].Length -le $entry.Groups[1].Length) {
                $end = $headings[$j].Index; break
            }
        }
        return $visible.Substring($entry.Index, $end - $entry.Index)
    }
    throw "Missing section matching '$Heading'"
}

function Assert-Patterns {
    param([string] $Text, [string[]] $Patterns)
    # Fold wrapping and emphasis, but never let fenced examples satisfy guards.
    $plain = ((Remove-FencedCode $Text) -replace '[*`]', '') -replace '\s+', ' '
    foreach ($pattern in $Patterns) {
        Assert-True ([regex]::IsMatch($plain, $pattern, 'IgnoreCase')) "Missing contract pattern: $pattern"
    }
}

function Get-Frontmatter {
    param([string] $Text)
    $match = [regex]::Match($Text, '\A\uFEFF?---\r?\n(?<body>[\s\S]*?)\r?\n---(?:\r?\n|$)')
    Assert-True $match.Success 'Missing delimited frontmatter'
    return $match.Groups['body'].Value
}

function Get-Field {
    param([string] $Frontmatter, [string] $Name)
    $entries = [regex]::Matches($Frontmatter, '(?m)^' + [regex]::Escape($Name) + ':[\t ]*([^\r\n]*)\r?$')
    Assert-True ($entries.Count -eq 1) "Expected exactly one flat '$Name' field"
    return $entries[0].Groups[1].Value.Trim()
}

function Test-IgnoredTarget {
    param([string] $Target)
    # Ignore ALL URI schemes (including mailto:, file:, vscode:), protocol-relative
    # URLs and explicit template tokens. Ordinary missing relative files fail.
    return ($Target -match '^[a-z][a-z0-9+.-]*:|^//' -or
        $Target -match '[{}<>\[\]]|\$\(|\*|(?:^|/)\.\.\.(?:/|$)' -or
        $Target -match '^(?:path/to|placeholder|TODO)(?:/|$)')
}

function Get-LinkTargets {
    param([string] $Text)
    $visible = Remove-FencedCode $Text
    # Markdown destinations allow balanced parentheses, escaped characters,
    # angle-wrapped paths with spaces, and an optional quoted title.
    $inline = '(?x) !?\[(?:[^\[\]\\]|\\.|\[[^\]]*\])*\]\(\s* (?<dest><[^>\r\n]+>|(?:[^\s()\\]|\\.|\((?<depth>)|\)(?<-depth>))+(?(depth)(?!))) (?:\s+(?:"[^"]*"|''[^'']*''))?\s*\)'
    foreach ($match in [regex]::Matches($visible, $inline)) {
        $match.Groups['dest'].Value.Trim('<', '>')
    }
    # Definitions themselves are checked, including unused reference definitions.
    foreach ($match in [regex]::Matches($visible, '(?m)^ {0,3}\[[^\]]+\]:\s*(?<dest><[^>\r\n]+>|\S+)')) {
        $match.Groups['dest'].Value.Trim('<', '>')
    }
    # Backticked qualified paths are source references; bare filenames in prose
    # may be naming conventions or examples, not file-relative destinations.
    foreach ($match in [regex]::Matches($visible, '`(?<dest>(?:\.{1,2}/)?(?:[\w.-]+/)+[\w.-]+\.(?:md|json|ya?ml|ps1|py)(?:#[\w-]+)?)`')) {
        $match.Groups['dest'].Value
    }
}

function Get-Anchors {
    param([string] $Text)
    $visible = Remove-FencedCode $Text
    $used = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    $lines = $visible -split '\r?\n'
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $heading = $null
        if ($lines[$i] -match '^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$') { $heading = $Matches[1] }
        elseif ($i + 1 -lt $lines.Count -and $lines[$i].Trim() -and $lines[$i + 1] -match '^ {0,3}(?:=+|-+)\s*$') {
            $heading = $lines[$i]; $i++
        }
        if ($null -eq $heading) { continue }
        $heading = $heading -replace '!?(\[([^\]]+)\])\([^)]*\)', '$2'
        $heading = [Net.WebUtility]::HtmlDecode(($heading -replace '<[^>]*>', ''))
        $slug = ($heading.ToLowerInvariant() -replace '[^\p{L}\p{M}\p{N}\s_-]', '') -replace '\s', '-'
        $unique = $slug; $suffix = 0
        while (-not $used.Add($unique)) { $suffix++; $unique = "$slug-$suffix" }
        $unique
    }
    foreach ($match in [regex]::Matches($visible, '(?i)<[^>]+\b(?:id|name)\s*=\s*["'']([^"'']+)["''][^>]*>')) {
        $match.Groups[1].Value
    }
}

function Assert-LocalLinks {
    param([string] $Path, [string] $Text)
    $issues = [System.Collections.Generic.List[string]]::new()
    foreach ($target in @(Get-LinkTargets $Text | Select-Object -Unique)) {
        if (Test-IgnoredTarget $target) { continue }
        $parts = $target -split '#', 2
        $relative = [Uri]::UnescapeDataString(($parts[0] -split '\?', 2)[0]) -replace '\\([() ])', '$1'
        if (-not $relative) { $resolved = $Path }
        else { $resolved = [IO.Path]::GetFullPath((Join-Path (Split-Path -Parent $Path) $relative)) }
        if (-not (Test-Path -LiteralPath $resolved)) { $issues.Add("Missing local target: $target"); continue }
        if ($parts.Count -eq 2 -and $parts[1] -and [IO.Path]::GetExtension($resolved) -eq '.md') {
            $fragment = [Uri]::UnescapeDataString($parts[1])
            if ($fragment -cnotin @(Get-Anchors (Read-Source $resolved))) {
                $issues.Add("Missing local anchor: $target")
            }
        }
    }
    Assert-True ($issues.Count -eq 0) ($issues -join '; ')
}

Write-Output 'BTBA source contracts: STRUCTURAL/STATIC ONLY'
Write-Output 'Not model behavior, engineering verification, or a Python validator/test run.'

Invoke-Check 'Harness: fences, current boundary, links and anchors' {
    $sample = @'
# Visible, Heading
[local](doc.md#visible-heading)
[balanced](folder/test(1).md)
[spaced](<folder/test file.md> "title")
[ref]: doc.md#visible-heading
````text
```
[hidden](missing.md)
# Hidden
```
````
~~~text
[also hidden](missing-too.md)
~~~
# Visible, Heading
## Historical Appendix: Retained history
[old](old.md)
'@
    $current = Get-CurrentText $sample
    $targets = @(Get-LinkTargets $current)
    Assert-True ($targets.Count -eq 4) 'Link parser/fence fixture failed'
    Assert-True ('folder/test(1).md' -in $targets -and 'folder/test file.md' -in $targets) 'Destination parser fixture failed'
    $anchors = @(Get-Anchors $current)
    Assert-True ('visible-heading-1' -in $anchors -and 'hidden' -notin $anchors) 'Anchor fixture failed'
    foreach ($target in @('https://example.org/a', 'mailto:a@example.org', 'vscode:test', '//example.org', '{project}/a.md', 'path/to/a.md')) {
        Assert-True (Test-IgnoredTarget $target) "Ignore fixture failed: $target"
    }
    Assert-True (-not (Test-IgnoredTarget 'missing-real-file.md')) 'Missing files must not be ignored'
}

Invoke-Check 'Agent: real entry point and ordered source references' {
    $agents = @(Get-ChildItem -LiteralPath (Join-Path $RepositoryRoot '.github/agents') -Filter '*.agent.md' -File)
    Assert-True ($agents.Count -gt 0) 'No actual agent entry points found'
    foreach ($agent in $agents) {
        $text = Read-Source $agent.FullName
        Assert-LocalLinks $agent.FullName $text
        Assert-Patterns $text @('system_prompt\.md.*session-initialization.*routing', 'once', 'relevant skills')
        $targets = @(Get-LinkTargets $text)
        foreach ($required in @('../../system_prompt.md', '../../skills/session-initialization/SKILL.md', '../../skills/routing/SKILL.md')) {
            Assert-True ($required -in $targets) "Agent lacks actual path reference: $required"
        }
    }
    Assert-Patterns (Read-Repo 'system_prompt.md') @('\.instructions\.md', 'session-initialization.*routing', 'in that order')
}

$sourceFiles = @(
    'README.md', 'CONTRIBUTING.md', '.github/prompts/btba.prompt.md',
    'docs/readme-audit-2026-09-11.md', 'docs/construction-plans-roadmap.md',
    'docs/reliability-implementation-2026-09-11.md', 'docs/development.md',
    'docs/reliability-hardening-2026-09-11.md',
    'docs/evaluations/README.md', 'examples/detail-package/README.md',
    'skills/building-code-tek17/SKILL.md', 'skills/building-code-tek17/references/verified-requirements.md',
    'skills/sintef-byggforsk/SKILL.md', 'skills/electrical-nek400/SKILL.md',
    'skills/drawing-reader/references/leveled-reading-model.md',
    'skills/drawing-reader/references/extraction-pipelines.md',
    'templates/structural-assessment-memo.md', 'templates/compliance-gap-analysis.md',
    'templates/construction-sequence.md', 'templates/heritage-assessment.md',
    'templates/post-approval-checklist.md', 'templates/pre-application-meeting-notes.md',
    'mcp/tools/norwegian-building-data.md',
    'templates/construction-detail-package.md',
    'system_prompt.md', '.instructions.md', 'skills/session-initialization/SKILL.md',
    'skills/routing/SKILL.md', 'skills/project-lifecycle/SKILL.md',
    'skills/lessons-learned/SKILL.md', 'skills/formulas-reference/SKILL.md',
    'skills/structural-engineering/SKILL.md', 'skills/bim-ifc/SKILL.md',
    'skills/structural-engineering/references/beam-calculator.md',
    'skills/structural-engineering/references/local-beam-calculator.md',
    'skills/structural-engineering/references/norwegian-design-basis.md',
    'mcp/tools/structural-analysis.md',
    'skills/construction-execution/SKILL.md', 'skills/residential-tender-writing/SKILL.md',
    'skills/general-contractor-review/SKILL.md', 'skills/drawing-reader/SKILL.md'
)
foreach ($relative in $sourceFiles) {
    Invoke-Check "Source links: $relative" {
        Assert-LocalLinks (Join-Path $RepositoryRoot $relative) (Read-Repo $relative)
    }
}

Invoke-Check 'README: inventory, guidance versus implementation and unfinished tools' {
    $text = Read-Repo 'README.md'
    $skillCount = @(Get-ChildItem -LiteralPath (Join-Path $RepositoryRoot 'skills') -Directory |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') -PathType Leaf }).Count
    Assert-Patterns $text @(
        "$skillCount modular skills", 'not a standalone CAD application',
        'Guidance.*means an agent procedure, not a tested software integration',
        'Server not implemented', 'No default well size|No universal window-well size',
        'not an implemented automatic construction-plan generator',
        'Git-ignored.*not distributed with a normal clone',
        'Numerical tests are not professional design certification',
        'no external connector is claimed tested or connected'
    )
    Assert-True ($text -notmatch 'WET_STAMP_REQUIRED|professional-grade|all 2026 amendments|All 6 output templates complete|agentskills\.io compliant') 'Outdated blanket readiness/authority claim returned'
    Assert-Patterns (Read-Repo 'docs/construction-plans-roadmap.md') @(
        'Source-linked detail register first', 'CAD/BIM detail output.*Not implemented',
        'expected and actual results separately', 'not a claim that an agent has passed',
        'No external code was installed', 'No individual dataset.*was evaluated'
    )
}

Invoke-Check 'Quick Ask: ordered loading and no hardcoded private fallback' {
    $text = Read-Repo '.github/prompts/btba.prompt.md'
    Assert-Patterns $text @(
        'system_prompt\.md.*session-initialization.*once.*routing',
        'explicitly selected project scope', 'No hardcoded project fallback',
        'no private-project lookup for repository maintenance',
        'Concise evidence summary', 'no private internal deliberation'
    )
    Assert-True ($text -notmatch 'projects/|skills/routing\.md|use ReAct sections') 'Legacy Quick Ask scope/path/instruction returned'
}

Invoke-Check 'Reliability: source corrections and no default construction release' {
    Assert-Patterns (Read-Repo 'skills/building-code-tek17/references/verified-requirements.md') @(
        'no fixed minimum room area', 'minimum levels.*complete applicable pathway',
        'preaccepted guidance', 'does not supply a universal lysgrav', 'not.*full.*review'
    )
    Assert-Patterns (Read-Repo 'skills/sintef-byggforsk/SKILL.md') @(
        'earlier contradictory cold/warm resistance ratio', 'withdrawn', 'No guessed replacement rule'
    )
    Assert-Patterns (Read-Repo 'skills/electrical-nek400/SKILL.md') @(
        'insurance-voiding claims.*withdrawn', 'specific FEL/FEK/NEK provisions.*not independently validated'
    )
    $fm = Get-Frontmatter (Read-Repo 'skills/building-code-tek17/SKILL.md')
    Assert-True ((Get-Field $fm 'load_with') -eq '[]') 'Structural/regulatory companion cycle returned'
    foreach ($template in @(Get-ChildItem -LiteralPath (Join-Path $RepositoryRoot 'templates') -Filter '*.md' -File)) {
        Assert-Patterns (Read-Source $template.FullName) @('Prepared by BTBA, AI advisory draft, not professional certification')
    }
}

Invoke-Check 'Reliability: local tools, evaluation distinction and fresh-clone paths' {
    Assert-Patterns (Read-Repo 'docs/development.md') @(
        'No private project or MCP configuration is needed', 'not a general sandbox',
        'transitive dependencies are not a complete lockfile', 'live-host runs|cases still to run'
    )
    Assert-Patterns (Read-Repo 'docs/evaluations/README.md') @(
        'live-host runs not performed', 'observed pass / observed failure / not run',
        'not a universal guarantee'
    )
    foreach ($path in @('system_prompt.md', 'skills/drawing-reader/SKILL.md')) {
        Assert-True ((Read-Repo $path) -notmatch '\]\([^)]*mcp-config\.json\)') 'Ignored config link is a clone prerequisite'
    }
    foreach ($path in @('skills/drawing-reader/references/extraction-pipelines.md', 'skills/drawing-reader/references/norwegian-extraction-prompt.txt')) {
        $text = Read-Repo $path
        Assert-True ($text -notmatch 'Confirmed scale from title block|mm assumed for Norway|YOUR_API_KEY') 'Unsafe legacy extraction prompt returned'
        Assert-Patterns $text @('untrusted', 'scope', 'calibration')
    }
    Assert-Patterns (Read-Repo 'mcp/tools/norwegian-building-data.md') @(
        'not implemented or connected', 'No features in query.*not.*no hazard',
        'failed request is not an empty result', 'No source text can execute commands'
    )
}

Invoke-Check 'Hardening: evidence and candidate identity remain scoped' {
    Assert-Patterns (Read-Repo 'docs/reliability-hardening-2026-09-11.md') @(
        'Removed holds', 'requiring review, not a closed issue',
        'not an independently verified document hash',
        'not persistent BIM wall IDs across revisions',
        'not an installation tolerance',
        'host benchmark itself remains not run'
    )
    Assert-Patterns (Read-Repo 'docs/evaluations/README.md') @(
        'validator_fixture cannot count as host passes',
        'every case/attempt', 'observed_failure, not blocked',
        'not independent correctness or certification'
    )
    Assert-Patterns (Read-Repo 'skills/drawing-reader/references/leveled-reading-model.md') @(
        'unrotated crop-relative', 'rotation and cropbox metadata',
        'sample_truncated', 'not persistent wall identities'
    )
}

Invoke-Check 'Construction details: scoped evidence, dimensions, holds and revision invalidation' {
    $section = Get-Section (Read-Repo 'skills/construction-execution/SKILL.md') '^Construction Detail Packages$'
    Assert-Patterns $section @(
        'Draft instruction workflow, not an automated CAD/BIM generator',
        'no property is selected.*do not retrieve another project',
        'Missing safety-critical inputs permit a bounded inventory/options draft',
        'Do not promote legacy generic assemblies',
        'reuse existing project IDs/registers',
        'a type schedule alone does not account for every wall',
        'structural opening, frame outer size, glazing area.*actual unobstructed clear opening',
        'clear internal width parallel to facade.*finished facade plane.*bottom/rim/terrain levels',
        'sash travel, steps/ladder, cover/grating',
        'no default compliant window-well size',
        'Do not assume infiltration or an existing drain connection is feasible',
        'missing quantities stay unknown, not zero',
        'technical review, authorized issue.*authority approval',
        'affected results not valid for reuse pending revalidation',
        'expected results, not observed behavioral test runs',
        'Forbidden: invent a compliant well size or release excavation'
    )
}

Invoke-Check 'Detail template: element coverage, well geometry, source and release fields' {
    $text = Read-Repo 'templates/construction-detail-package.md'
    Assert-Patterns $text @(
        'Prepared by BTBA, AI advisory draft, not professional certification',
        'Draft.*not issued for construction', 'Blank fields are unknown, not zero',
        'Source Manifest and Design Basis', 'Wall Register.*One Row per Instance',
        'Wall Type Detail', 'Junction and Detail Register', 'Window and Door Schedule',
        'Actual unobstructed clear opening', 'Window-Well Schedule.*Lysgraver',
        'External footprint and excavation are separate sizes',
        'Unknown outlet remains an open hold',
        'Quantities, Sequence and Inspection Holds',
        'Open Decisions and Revision Impacts',
        'not valid for reuse pending revalidation',
        'not an issued design, professional approval, permit or authorization to order/build'
    )
}

Invoke-Check 'Detail routing: companion domains and actual template destination' {
    $text = Read-Repo 'skills/routing/SKILL.md'
    $rows = [regex]::Matches($text, '(?m)^\| Construction detail packages[^\r\n]*')
    Assert-True ($rows.Count -eq 1) 'Expected one construction-detail route'
    Assert-Patterns $rows[0].Value @(
        'construction-execution/SKILL\.md#construction-detail-packages',
        'building physics', 'structural/ground', 'regulatory/trade',
        'No default well size or automatic CAD generation'
    )
    Assert-True ('../../templates/construction-detail-package.md' -in @(Get-LinkTargets $text)) 'Missing detail-package template link'
}

Invoke-Check 'Startup: repository/general/project routes and scoped intake' {
    $text = Read-Repo 'skills/session-initialization/SKILL.md'
    $modes = Get-Section $text '^Select Mode'
    foreach ($mode in @('Repository', 'General', 'Project')) {
        Assert-True ($modes -match "(?m)^\|\s*$mode\s*\|") "Missing mode row: $mode"
    }
    Assert-Patterns $modes @('No mandatory address', 'index/current summary', 'explicitly supplied.*sufficient', 'Do not ask.*again', 'editor context.*hint')
    Assert-Patterns (Get-Section $text '^Read in Scope') @('INDEX\.md first', 'fallback', 'lessons lazily', 'not as a startup scan')
    Assert-Patterns (Read-Repo 'system_prompt.md') @('Do not load every.*lesson at startup')
    Assert-Patterns (Read-Repo 'skills/routing/SKILL.md') @('no mandatory startup or per-response lesson scan')
}

Invoke-Check 'Lessons: lazy flat metadata, no startup subscription' {
    $text = Read-Repo 'skills/lessons-learned/SKILL.md'
    $fm = Get-Frontmatter $text
    Assert-True ((Get-Field $fm 'load_with') -eq '[]') 'Lessons load_with must be empty'
    Assert-True ((Get-Field $fm 'load_priority').Trim('"', "'") -eq 'on-demand') 'Lessons must be on-demand'
    Assert-Patterns (Get-Field $fm 'triggers') @('retrospective', 'matching known failure')
    Assert-True ($fm -notmatch '(?im)^\s*auto_load_on:|ALWAYS_CHECK_AT_SESSION_START|session start') 'Lessons have unconditional startup metadata'
    Assert-Patterns (Get-Section $text '^Purpose') @('Load only matching lessons', 'No unconditional startup', 'Do not reload startup')
}

Invoke-Check 'Orchestration: empty load_with and string run_before matches validator' {
    $validator = Read-Repo 'skills/validate_skills.py'
    $strings = [regex]::Match($validator, '(?s)\bSTRING_FIELDS\s*=\s*\((.*?)\)')
    Assert-True $strings.Success 'Cannot locate Python STRING_FIELDS declaration'
    Assert-True ($strings.Groups[1].Value -match '["'']run_before["'']') 'run_before missing from STRING_FIELDS'
    $lists = [regex]::Match($validator, '(?s)\bLIST_FIELDS\s*=\s*\((.*?)\)')
    Assert-True ($lists.Success -and $lists.Groups[1].Value -notmatch '["'']run_before["'']') 'run_before must not be a LIST_FIELDS member'
    foreach ($skill in @('session-initialization', 'routing', 'project-lifecycle')) {
        $fm = Get-Frontmatter (Read-Repo "skills/$skill/SKILL.md")
        Assert-True ((Get-Field $fm 'load_with') -eq '[]') "$skill load_with must be []"
        if ($skill -eq 'session-initialization') {
            $before = Get-Field $fm 'run_before'
            Assert-True ($before -match '^(?:routing|"routing"|''routing'')$') 'Startup run_before must be the scalar string routing'
        }
    }
    Assert-Patterns (Get-Section (Read-Repo 'skills/routing/SKILL.md') '^Dependency and Cycle Guard') @('one-way', 'visited set.*canonical', 'Ignore self-links and back-edges', 'Lifecycle never calls startup')
}

Invoke-Check 'Lifecycle: evidence states and transmission proof' {
    $section = Get-Section (Read-Repo 'skills/project-lifecycle/SKILL.md') '^Evidence and Release Status'
    foreach ($status in @('Reported', 'Observed/documented', 'Proposed/assumed', 'Derived', 'Reviewed', 'Submitted/issued', 'Approved', 'Disputed/unverified', 'Superseded')) {
        Assert-True ($section -match ('(?m)^\|\s*' + [regex]::Escape($status) + '\s*\|')) "Missing evidence state: $status"
    }
    Assert-Patterns $section @('Authority is not recency', 'transmission record.*destination.*date.*exact version', 'competent authority', 'Never promote a draft email.*sent')
}

Invoke-Check 'Lifecycle: dependency invalidation and safe archival' {
    $text = Read-Repo 'skills/project-lifecycle/SKILL.md'
    Assert-Patterns (Get-Section $text '^Drift and Dependency') @('old/new claim', 'direct and downstream dependencies', 'not valid for reuse pending revalidation', 'Preserve original calculations and issued records', 'release holds', 'left unchecked')
    Assert-Patterns (Get-Section $text '^Safe Archiving') @('in-place status', 'replacement.*content and scope', 'Preserve unique', 'inbound and outbound links', 'obtain authorization', 'Do not overwrite', 'verify they resolve', 'leave the source in place')
}

Invoke-Check 'SIMBA route matcher: identical LF and CRLF behavior' {
    $row = '| BIM, SIMBA | [bim-ifc](../bim-ifc/SKILL.md) |'
    Assert-True ((Get-SimbaRouteRow "intro`n$row`nnext") -ceq $row) 'LF row lookup failed'
    Assert-True ((Get-SimbaRouteRow "intro`r`n$row`r`nnext") -ceq $row) 'CRLF row lookup failed'
    Assert-True ((Get-SimbaRouteRow 'No matching row') -eq '') 'Absent row must not match'
}

Invoke-Check 'SIMBA: scoped routing and preset is not acceptance' {
    $route = Read-Repo 'skills/routing/SKILL.md'
    $row = Get-SimbaRouteRow $route
    Assert-Patterns $row @('bim-ifc/SKILL\.md', 'do not require drawing, permit, or infrastructure')
    Assert-Patterns (Get-Section $route '^Evidence and BIM Gates') @('client.*agreement.*revision.*purpose', 'not universal', 'preset.*not acceptance or professional approval')
    Assert-Patterns (Read-Repo 'system_prompt.md') @('SIMBA.*project/client requirements.*not universal', 'preset.*not professional approval')
    $bim = Read-Repo 'skills/bim-ifc/SKILL.md'
    Assert-Patterns (Get-Section $bim '^Norwegian BIM Requirements') @('do not impose.*SIMBA.*unless.*client or contract', 'project-adapted requirement set', 'preset.*never sufficient evidence of acceptance')
    Assert-Patterns (Get-Section $bim '^Trust Boundary') @('preset.*does not certify.*contractual acceptance')
}

Invoke-Check 'Review fallback: unmatched concern gets reviewer and evidence, no invented flag' {
    Assert-Patterns (Get-Section (Read-Repo 'system_prompt.md') '^Safety and Review Triggers') @('If no listed review trigger fits', 'appropriate reviewer', 'next evidence', 'plain language', 'Do not invent an official-looking flag')
    Assert-Patterns (Get-Section (Read-Repo 'skills/routing/SKILL.md') '^Trust Boundary') @('outside.*listed review triggers', 'appropriate reviewer.*next evidence.*plain language', 'Do not invent an official-looking flag')
}

Invoke-Check 'Formulas: fabricated snow table and malformed tile row absent' {
    $text = Remove-FencedCode (Read-Repo 'skills/formulas-reference/SKILL.md')
    Assert-True ($text -notmatch '(?i)TEK17\s+(?:Table|tabell)\s*7\.1') 'Fabricated TEK17 snow-table citation returned'
    $snow = Get-Section $text '^2\.2\s+Snow Load'
    Assert-True ($snow -notmatch '(?m)^\s*\|') 'Snow zoning/coefficient table returned to source-specific procedure'
    Assert-Patterns $snow @('NS-EN 1991-1-3', 'Norwegian National Annex', 'altitude', 'ground.*roof', 'unverified')
    $dead = Get-Section $text '^2\.4\s+Dead Load'
    Assert-True ($dead -notmatch '(?im)^\s*\|[^\r\n]*(?:ceramic|tile|takstein)[^\r\n]*\|') 'Removed tile material row returned'
    Assert-True ($dead -notmatch '\b0\.075\b|15\s*[-–]\s*20\s*kN/m[²2]') 'Former malformed tile value returned'
    Assert-Patterns $dead @('manufacturer mass per tile', 'installed coverage', 'source/revision', 'area.*sloping roof or horizontal', 'missing components.*unverified, not zero')
}

Invoke-Check 'Beam reference: optional cross-check, units, Norway applicability and evidence scope' {
    $reference = Read-Repo 'skills/structural-engineering/references/beam-calculator.md'
    $links = @(Get-LinkTargets (Get-Section $reference '^Resource Map$'))
    $paths = @('documentation', 'calculator/beam-deflection',
        'calculator/beam-deflection-formulas-shown', 'calculator/beam-deflection-unit-converter',
        'calculator/beam-deflection-limit-l-360', 'calculator/material-reference',
        'calculator/section-properties')
    foreach ($path in $paths) {
        $prefix = "https://beam-calculator.github.io/en/$path/"
        Assert-True (@($links | Where-Object { $_.StartsWith($prefix) }).Count -eq 1) "Missing or duplicate beam resource: $path"
    }
    Assert-Patterns (Get-Section $reference '^Evidence and Review Scope$') @(
        'browser UI was not run', 'no whole-site solver audit', 'not evidence about any property'
    )
    Assert-Patterns (Get-Section $reference '^Use Procedure$') @(
        'support conditions', 'self-weight', '1 cm⁴ = 10,000 mm⁴', '1 kN/m = 1 N/mm',
        'SLS combination', 'Norwegian National Annexes', 'criterion unverified',
        'lateral-torsional buckling', 'creep', 'not structural approval',
        'private project inputs.*without explicit authorization'
    )
    Assert-Patterns (Get-Section $reference '^Observed Cautions$') @(
        'substitution is not a unit-complete calculation', 'C16/C24 timber',
        'plastic section modulus', 'clamps.*positive minima'
    )
    Assert-Patterns (Get-Section $reference '^Supplied Link Interpretation$') @(
        'st=c.*Cantilever', 'lt=p.*Point load', 'w=12.*not 12 kN/m',
        'derived values, not observed browser outputs', 'Forbidden inference'
    )
    Assert-Patterns (Get-Section (Read-Repo 'skills/structural-engineering/SKILL.md') '^Optional Beam Calculator Reference$') @(
        'references/beam-calculator.md.*on demand', 'not a universal Norwegian limit'
    )
    Assert-Patterns (Read-Repo 'skills/formulas-reference/SKILL.md') @(
        'structural-engineering/references/beam-calculator.md', 'No calculator integration is installed'
    )
}

Invoke-Check 'Structural source: input/span invalidation outside examples' {
    $text = Read-Repo 'skills/structural-engineering/SKILL.md'
    Assert-Patterns (Get-Section $text '^Calculation Input Lock Protocol') @('before the first formula', 'locked input changes', 'old value.*VOID', 'new locked input table', 'prior calculations.*SUPERSEDED', 'Rerun affected calculations', 'drawing dimension.*not the installed geometry')
    Assert-Patterns (Get-Section (Read-Repo 'skills/lessons-learned/SKILL.md') '^Lesson L002') @('span', 'corrected', 'structural-engineering', 'not an automated consistency check')
}

Invoke-Check 'Local beam workflow: no automatic Norwegian design defaults or approval' {
    $skill = Read-Repo 'skills/structural-engineering/SKILL.md'
    Assert-Patterns (Get-Section $skill '^Local Tested Beam Analysis$') @(
        'Pint units', 'local JSON report', 'not an MCP server', 'numerical.*unverified',
        'No automatic load factors or deflection limits', 'not revalidated'
    )
    Assert-Patterns (Get-Section $skill '^Deflection Criteria') @(
        'withdrawn as design defaults', 'unavailable criterion stays unverified',
        'do not report pass/fail', 'norwegian-design-basis.md'
    )
    Assert-Patterns (Get-Section $skill '^Drawing Freeze Gate') @(
        'not a ban on conceptual arithmetic', 'not structural verification',
        'Bounded numerical comparisons.*allowed'
    )
    $register = Read-Repo 'skills/structural-engineering/references/norwegian-design-basis.md'
    Assert-Patterns $register @(
        'dibk.no/regelverk/byggteknisk-forskrift-tek17/10/10-2',
        'regulation.*guidance', 'No numerical NA rule pack is implemented',
        'not.*revalidated', 'exact standard/NA edition'
    )
    $guide = Read-Repo 'mcp/tools/structural-analysis.md'
    Assert-Patterns $guide @('Unverified Availability', 'configuration entry does not establish availability',
        'stated section and supplied inertia.*not a verified matched pair')
    Assert-True ($guide -notmatch 'WET_STAMP_REQUIRED|666450000') 'Obsolete MCP sizing/stamp defaults returned'
}

Invoke-Check 'Structural source: installed profile needs traceable evidence, not visual inference' {
    $section = Get-Section (Read-Repo 'skills/structural-engineering/SKILL.md') '^Steel Beam Assessment'
    Assert-Patterns $section @('Do not assess installed-beam adequacy until.*profile is confirmed', 'as-built documentation tied to that member', 'direct dimensions.*verified section table', 'Photographs.*crew size.*order timing.*do not confirm', 'Identification does not establish grade.*adequacy', 'hypothetical comparison.*assumed.*not for design')
}

# These are section-scoped source contracts, not execution of the workflows.
# Link/anchor validity is checked separately above, including routing destinations.
Invoke-Check 'Contracts: accepted baseline, missing evidence and no imported commercial defaults' {
    $section = Get-Section (Read-Repo 'skills/construction-execution/SKILL.md') '^Contract Departures Review$'
    Assert-Patterns $section @(
        'client-accepted comparison baseline.*revision.*evidence of who accepted it and when',
        'prior register, article example, tender draft, or AI suggestion is not an accepted baseline',
        'If it or the relevant clause is missing, record not assessed',
        'Source clause / revision.*exact relevant wording.*amendment and precedence evidence',
        'Decision owner / review.*authorized decision owner.*decision and evidence/date',
        'Acceptance requires a separate authorized decision.*not legal approval',
        'Do not import.*illustrative LD cap \(including 10%\), liability exclusions, warranty terms, or other commercial defaults'
    )
}

Invoke-Check 'Contracts: Norwegian consumer applicability and unavailable clauses remain unassessed' {
    $section = Get-Section (Read-Repo 'skills/construction-execution/SKILL.md') '^Contract Basis and Applicability$'
    Assert-Patterns $section @(
        'Determine the parties \(including consumer/professional status\), work type.*scope, and design responsibility first',
        'Establish whether bustadoppføringslova or håndverkertjenesteloven applies',
        'which contract/NS standard, if any, was actually agreed',
        'Do not prescribe NS 8405, NS 8415, or NS 8407 for every Norwegian contract',
        'or assume an agreed standard overrides mandatory consumer protections',
        'Verify exact clauses, edition, amendments, document precedence, and applicable law',
        'authorized Standard Norge material, current Lovdata text.*qualified Norwegian counsel',
        'Unavailable clauses or unresolved applicability mean not assessed, not a reconstructed rule from memory'
    )
}

Invoke-Check 'Tender packages: stable requirement-to-price IDs and explicit unpriced interfaces' {
    $section = Get-Section (Read-Repo 'skills/residential-tender-writing/SKILL.md') '^Optional Procurement Package Record$'
    Assert-Patterns $section @(
        'not a mandatory new file or prerequisite for a short enquiry',
        'Reuse existing IDs.*stable local IDs only where absent.*working identifiers, not issued references',
        'Package ID and scope.*linked requirement IDs.*included and excluded work explicitly',
        'Source basis.*date/revision.*conflicting or missing sources as unresolved',
        'Trade interfaces.*owner-direct supply, installation, testing, and handover',
        'Pricing lines.*Stable line IDs linked to requirements.*quantities, units, rates or lump sums, currency and VAT basis; unknown values stay unpriced',
        'Trace requirement\s*→\s*package\s*→\s*pricing line without silently expanding scope',
        'exclusion needs an explicit destination/owner or an unresolved gap',
        'general-contractor-review/SKILL\.md#estimate-reconciliation'
    )
}

Invoke-Check 'Estimates: coverage crosswalk, unpriced not zero and evidence-based overlaps' {
    $section = Get-Section (Read-Repo 'skills/general-contractor-review/SKILL.md') '^Estimate Reconciliation$'
    Assert-Patterns $section @(
        'Preserve original quantities, rates, amounts, subtotals and reported totals unchanged',
        'requirement\s*→\s*package\s*→\s*pricing-line crosswalk.*source revisions',
        'priced, allowance, excluded/owner-direct, alternative, or missing/unpriced',
        'List unmatched estimate lines and unexplained exclusions',
        'blank/missing price is unpriced, not zero; accept zero only when explicitly evidenced',
        'partial priced subtotal is not a complete project total',
        'If requirements are missing, report coverage as unknown, not complete',
        'owner-direct supply versus trade supply/install, GC versus subcontractor work',
        'Flag suspected overlap pending confirmation; do not delete apparently duplicate lines without evidence'
    )
}

Invoke-Check 'Estimates: separate alternatives, replacement deltas and allowance inclusions' {
    $section = Get-Section (Read-Repo 'skills/general-contractor-review/SKILL.md') '^Estimate Reconciliation$'
    Assert-Patterns $section @(
        'selected base, allowance inclusions, and mutually exclusive alternatives',
        'Never add competing systems together',
        'replacement option, remove the displaced base scope before adding its replacement',
        'incremental option, apply only the documented delta',
        'If selection or pricing basis is unknown, show separate scenarios or an unresolved total, not an assumed selection',
        'Prevent allowances being counted both within lines and again below the subtotal'
    )
}

Invoke-Check 'Estimates: explicit VAT arithmetic and variance do not establish price adequacy' {
    $section = Get-Section (Read-Repo 'skills/general-contractor-review/SKILL.md') '^Estimate Reconciliation$'
    Assert-Patterns $section @(
        'multiply quantity\s*×\s*rate with compatible units and disclosed conversions/rounding',
        'lump sums as supplied, marking their internal arithmetic unverifiable',
        'Independently sum line amounts into package subtotals and the selected base subtotal',
        'Retain signs for credits, discounts and other adjustments',
        "each adjustment's amount or rate, eligible base and application order",
        'Show contingency and VAT separately with sourced rates, explicit eligible bases, inclusions/exclusions and order',
        'do not assume it is VAT-taxable or untaxed',
        'Recompute net/gross totals only where treatment is established',
        'Unknown quantity/rate, percentage base or tax basis leaves affected results unresolved',
        'do not invent a rate, use a default contingency, or plug a gap',
        'signed variance \(recomputed minus reported\).*lines, subtotals, adjustments and totals',
        'three separate conclusions: scope coverage, arithmetic consistency, and price adequacy/uncertainty',
        'Correct arithmetic does not establish complete scope, market reasonableness, affordability, technical adequacy, or a binding price',
        'Price adequacy needs separately sourced, comparable market/quotation evidence.*otherwise mark it unassessed'
    )
}

Invoke-Check 'Bidder review: supplied criteria, evidence shortfall and no forced decision' {
    $section = Get-Section (Read-Repo 'skills/residential-tender-writing/SKILL.md') '^Optional Bidder Review Mode$'
    Assert-Patterns $section @(
        "client's tender request.*contractor's proposed offer",
        'contractor-supplied capacity.*competence evidence, and bid criteria',
        'Do not invent availability, margins, scores, thresholds, or company policy',
        'each supplied criterion with evidence and return met / unmet / unknown',
        'recommendation only where supplied evidence and criteria support it',
        'conditional bid, list conditions, responsible resolver and required evidence/timing',
        'no-bid, identify the specific failed criterion and evidence',
        'If decisive inputs are missing, return insufficient evidence to recommend.*not an invented decision',
        "Separate recommendation from the contractor's actual decision",
        'Record a decision/approval only if supplied, with its source and date',
        'Neither recommendation authorizes sending, contracting, ordering, or construction',
        'Incomplete design does not automatically mean no-bid'
    )
}

Invoke-Check 'Drawing summaries: per-sheet identity, provenance, quantity types and coverage' {
    $section = Get-Section (Read-Repo 'skills/drawing-reader/SKILL.md') '^Reusable Per-Sheet Summary$'
    Assert-Patterns $section @(
        'one traceable entry per relevant sheet.*No new parallel file is mandatory',
        "distinguish the file's 1-based page number from the printed sheet number",
        'never imply that reviewing one page covers the file',
        'Source identity:.*reviewed page number, sheet number/title, discipline, revision and drawing date, floor/zone',
        'Mark missing or conflicting fields rather than guess them',
        'Extraction provenance: extraction date and method/tool, source location for each fact',
        'Quantities: value, units, scope and source location.*annotated.*scaled.*recorded view calibration.*derived.*linked inputs and method',
        'record quality/uncertainty per quantity',
        'Coverage: reviewed, partial, unreadable, or not reviewed',
        'Reviewed means the declared scope only, not approval',
        'referenced sheets/details/specifications and whether checked, missing, or not reviewed'
    )
}

Invoke-Check 'Drawing summaries: revised sources invalidate affected entries before reuse' {
    $section = Get-Section (Read-Repo 'skills/drawing-reader/SKILL.md') '^Reusable Per-Sheet Summary$'
    Assert-Patterns $section @(
        'When the source is revised, mark only affected summary entries, quantities, and dependent conclusions not valid for reuse pending re-extraction/revalidation',
        'Re-extract the affected pages/zones only; retain prior revision provenance and unchanged entries',
        'If revision impact is uncertain, mark it needs review before reuse, not silently current',
        'Do not claim complete revision coverage without checking the relevant change scope',
        'not source authority, an issued drawing, design approval, or verification of as-built conditions',
        'Check the exact source revision before consequential reuse',
        'Untrusted-content rules also apply to stored extracts'
    )
}

Invoke-Check 'Drawing scale: metadata allowed, measured geometry requires view calibration' {
    $text = Read-Repo 'skills/drawing-reader/SKILL.md'
    Assert-Patterns (Get-Section $text '^Scoped Extraction$') @(
        'Metadata and readable annotated values can be extracted without confirmed scale',
        'Measured geometry requires verified scale/calibration for the particular view',
        'paper coordinates or a title-block scale alone do not establish real dimensions'
    )
    Assert-Patterns (Get-Section $text '^Scope-Specific Scale Gate$') @(
        'Metadata-only extraction may proceed with unknown scale.*coverage limits explicit',
        'Readable dimension annotations may be transcribed as annotated, not geometrically verified',
        "verify the actual view's scale against a known dimension or scale bar",
        'record calibration, units, and any resizing/distortion concerns',
        'Different views may use different scales',
        'If calibration is unresolved, withhold scaled quantities and their derivatives; retain usable metadata and annotations'
    )
}

Invoke-Check 'RFI records: response and receipt are not authorized closure' {
    $section = Get-Section (Read-Repo 'skills/project-lifecycle/SKILL.md') '^Scoped Correspondence and RFI Records$'
    Assert-Patterns $section @(
        'read only the relevant thread, attachments, and linked register entries',
        'preserve its IDs and conventions.*Do not require new parallel files',
        'marking missing evidence unknown, not inferred',
        'attachment manifest distinguishing referenced, actually received, missing, and unreadable attachments',
        'due date and its basis.*do not invent a deadline or contractual entitlement',
        'dispatch alone does not prove receipt',
        'Response: source/date, respondent, exact revision/scope addressed.*remaining questions',
        'Closure: open/pending/closed status, closure evidence, who confirmed it, when, and for which scope',
        'A reply is not design approval, variation authorization, or proof that an issue is closed',
        'scope-specific evidence and an appropriately authorized decision-maker',
        'Receipt acknowledgments and partial answers leave unresolved items open',
        'not automatic monitoring, reminders, sending, or escalation',
        'External actions still require explicit authorization'
    )
}

Invoke-Check 'Schedules: accepted baseline, calendars and dependencies cannot release holds' {
    $section = Get-Section (Read-Repo 'skills/construction-execution/SKILL.md') '^Package-Based Schedule \(Optional\)$'
    Assert-Patterns $section @(
        'Predecessor ID, dependency type and any lag.*evidence or explicitly proposed assumption',
        'Duration / calendar.*Working duration, calendar, availability/productivity or supplier evidence',
        'Constraints / holds.*source and release owner/evidence',
        'Proposed dates separately from accepted baseline dates, revision and acceptance evidence',
        'no accepted baseline\s*→\s*comparison not assessed',
        'planner and affected trades review logic, calendars, durations, and constraints before any baseline decision',
        'Preserve the old baseline and record authorized changes rather than silently replacing it',
        'Report gaps instead of manufacturing a critical path',
        'only label one as calculated with a complete validated dependency/calendar/duration model and traceable calculation',
        'No generic curing time, age, planned date, or reported completion releases a technical hold'
    )
}

Invoke-Check 'Progress: cutoff evidence and measured percentages are not payment certification' {
    $section = Get-Section (Read-Repo 'skills/construction-execution/SKILL.md') '^Site Progress Reporting$'
    Assert-Patterns $section @(
        'reporting cutoff.*accepted baseline revision',
        'If absent.*baseline variance is not assessed',
        'Keep later updates separate from evidence available at the cutoff',
        'dated measurement, units, method, reporter, and source',
        'observed, contractor-reported, measured, inspected, and accepted are different',
        'photo or reported finish does not prove concealed quality, inspection acceptance, or hold release',
        'Do not treat an undocumented inspection as passed',
        'measured quantity and baseline denominator/method for any calculated percentage',
        'Do not infer percentages from photos, narrative, elapsed time, or unsupported claims',
        'Keep claimed progress explicitly attributed and unverified',
        'Reported progress is not accepted work or payment certification.*neither entitlement nor an extension of time'
    )
}

Invoke-Check 'FDV: exact installed products and manuals, explicit missing evidence, no invented warranties' {
    $section = Get-Section (Read-Repo 'skills/construction-execution/SKILL.md') '^FDV Handover Records$'
    Assert-Patterns $section @(
        'draft evidence index for the installed assets, not a generic collection of product brochures',
        'Asset ID, actual room/system/location, manufacturer, exact model/variant and serial where applicable, installation evidence',
        'Exact matching manual title/revision/link and supplied warranty document, issuer, terms and start evidence',
        'distinguish warranty from statutory defect rights',
        'Test/commissioning result, date, responsible party and source; matching as-built drawing revision',
        'Source document/page for each task, interval and condition; applicability to installed model/configuration verified',
        'Missing, mismatched, superseded or unverified evidence; named collection/action owner',
        'Do not invent warranty periods, maintenance intervals, commissioning results, or installed-product matches',
        'Keep unknowns explicit and request exact supplier/manufacturer evidence',
        'Issue only a draft index with open-document actions until the designated reviewer verifies scope and delivery',
        'Document completeness is not technical acceptance, contractual handover, a ferdigattest, or permission to occupy'
    )
}

Invoke-Check 'Routing: scoped commercial, drawing, RFI and execution workflows' {
    $section = Get-Section (Read-Repo 'skills/routing/SKILL.md') '^Task Routes$'
    $routes = @(
        @{ Intent = 'Procurement packages'; Patterns = @('residential-tender-writing/SKILL\.md', "distinguish client tender preparation from the contractor's decision") },
        @{ Intent = 'Estimate audit'; Patterns = @('general-contractor-review/SKILL\.md#estimate-reconciliation', 'do not run the full drawing-review workflow for a pricing-only question') },
        @{ Intent = 'Contract departures'; Patterns = @('construction-execution/SKILL\.md#contract-departures-review', 'actual contract and Norwegian consumer-law applicability, not default foreign commercial positions') },
        @{ Intent = 'Package-based schedule'; Patterns = @('site progress report or FDV/O&M completeness', 'construction-execution/SKILL\.md', 'separate proposed, reported and accepted states', 'No mandatory whole-project sequence') },
        @{ Intent = 'Correspondence register'; Patterns = @('RFI tracking, unanswered queries or response closure', 'project-lifecycle/SKILL\.md', 'scoped local evidence updates, not automatic monitoring or external sends') },
        @{ Intent = 'Drawing-file extraction'; Patterns = @('drawing-reader/SKILL\.md', 'Inspect only relevant pages/revisions') }
    )
    foreach ($route in $routes) {
        $rows = [regex]::Matches($section, '(?m)^\|\s*' + [regex]::Escape($route.Intent) + '[^\r\n]*$')
        Assert-True ($rows.Count -eq 1) "Expected one scoped route for: $($route.Intent)"
        Assert-Patterns $rows[0].Value $route.Patterns
    }
}

Invoke-Check 'Authoring: workflow contract and synthetic example boundaries' {
    $text = Read-Repo 'skills/README.md'
    Assert-LocalLinks (Join-Path $RepositoryRoot 'skills/README.md') $text
    $section = Get-Section $text '^Workflow Contract$'
    foreach ($element in @('Task', 'Workflow', 'Inputs', 'Rules and assumptions', 'Output', 'Examples')) {
        Assert-True ($section -match ('(?m)^\|\s*' + [regex]::Escape($element) + '\s*\|')) "Missing authoring element: $element"
    }
    Assert-Patterns $section @(
        'Missing input.*bounded result.*never an invented fact',
        'Use synthetic examples by default',
        'Do not copy private project records',
        'not defaults for other jobs',
        'actual observed output and test status separately',
        'not a behavioral test',
        'gross total unresolved',
        'Forbidden: invent VAT',
        'Forbidden: call B approved merely because it is newer'
    )
}

Invoke-Check 'Lifecycle: output destinations and register applicability' {
    $section = Get-Section (Read-Repo 'skills/project-lifecycle/SKILL.md') '^Current-State Navigation$'
    Assert-Patterns $section @(
        'Output destination and convention',
        'within the active project',
        'do not overwrite source or issued records',
        'only files actually saved',
        'Do not create another context file',
        'existing drawing/document register',
        'applicability and approval separately',
        'older approval does not cover newly changed scope',
        'register and file disagree.*flag the conflict',
        'not.*whole-folder rescan'
    )
}

if (-not [string]::IsNullOrWhiteSpace($ProjectPath)) {
    $ProjectRoot = [IO.Path]::GetFullPath($ProjectPath)
    Write-Output 'Project checks enabled for the explicitly supplied folder; no other project is scanned.'
    foreach ($name in @('INDEX.md', 'project.md', 'decision-log.md')) {
        Invoke-Check "Project current links: $name" {
            $path = Join-Path $ProjectRoot $name
            Assert-LocalLinks $path (Get-CurrentText (Read-Source $path))
        }
    }

    Invoke-Check 'Project: historical appendices do not satisfy current assertions' {
        foreach ($name in @('project.md', 'decision-log.md')) {
            $text = Read-Source (Join-Path $ProjectRoot $name)
            Assert-True ($text -match '(?im)^##\s+Historical Appendix') "Missing historical boundary: $name"
            $current = Get-CurrentText $text
            Assert-True ($current -notmatch '(?im)^##\s+Historical Appendix|KNOWN FACTS \(Verified\)') "History leaked into current scope: $name"
            Assert-Patterns $current @('historical', 'withdrawn', 'not.*(?:approval|approved)|No engineering approval')
        }
    }

    Invoke-Check 'Project: eight stable open holds with closure evidence' {
        $index = Get-CurrentText (Read-Source (Join-Path $ProjectRoot 'INDEX.md'))
        $holds = Get-Section $index '^Open Decisions and Release Holds$'
        $rows = [regex]::Matches($holds, '(?m)^\|\s*\*{0,2}(RH-\d{2})\*{0,2}\s*\|')
        $ids = @($rows | ForEach-Object { $_.Groups[1].Value })
        Assert-True ($ids.Count -eq 8 -and @($ids | Select-Object -Unique).Count -eq 8) 'Expected exactly eight unique hold-definition rows'
        foreach ($id in 1..8) { Assert-True (('RH-{0:00}' -f $id) -in $ids) "Missing hold RH-$id" }
        Assert-Patterns $holds @('All holds.*OPEN', 'Closing a hold requires recorded evidence', 'not.*assigned tasks', 'Evidence required for closure')
        foreach ($name in @('project.md', 'decision-log.md')) {
            $current = Get-CurrentText (Read-Source (Join-Path $ProjectRoot $name))
            foreach ($id in $ids) { Assert-True ($current.Contains($id)) "Current $name omits $id" }
        }
    }

    foreach ($name in @('INDEX.md', 'project.md', 'decision-log.md')) {
        Invoke-Check "Project current evidence: $name" {
            $current = Get-CurrentText (Read-Source (Join-Path $ProjectRoot $name))
            Assert-Patterns $current @(
                '(?:A20-1.{0,60}(?:missing|absent)|(?:no|missing) A20-1)',
                'independent.*(?:extension|load path)', 'flush.*(?:upper|finished)',
                '(?:one|1)[ -](?:lower )?bedroom.*hobby.*(?:two|2)[ -](?:lower )?bedrooms?.*hobby',
                'upper.*(?:family.room|family room)', 'window', 'operable', 'triple.glazed',
                'azimuths?.*(?:conflict|unresolved)|conflict.*azimuths?', 'survey.*verif',
                'Lyssand.*default', 'free opening', 'sill', 'wall.*finished.floor.*datum'
            )
            $beam = [regex]::Match($current, '(?im)^(?:\|[^\r\n]*|-[^\r\n]*)\bspan\b[^\r\n]*$').Value
            Assert-Patterns $beam @('(?:owner.report|reported)', '(?:correct|old|earlier)', '(?:No adequacy|No verified.*adequacy|adequacy.*not.*established)')
            $spans = @([regex]::Matches($beam, '\b\d+[.,]\d+\s*m\b') | ForEach-Object { $_.Value -replace '\s', '' } | Select-Object -Unique)
            Assert-True ($spans.Count -ge 2) 'Current span record must distinguish corrected and earlier values'
        }
    }

    Invoke-Check 'Project: release anchor and purpose-limited versus execution release' {
        foreach ($name in @('project.md', 'decision-log.md')) {
            $current = Get-CurrentText (Read-Source (Join-Path $ProjectRoot $name))
            Assert-True ('INDEX.md#open-decisions-and-release-holds' -in @(Get-LinkTargets $current)) "Exact release anchor absent in $name"
            Assert-Patterns $current @('explicit user release.*exact.*text.*recipients.*purpose.*file/revision/date manifest', '(?:Construction|Construction, product ordering).*separate release', 'relevant.*(?:closure evidence|hold-closure evidence)', 'RIB.*(?:does not depend|does not require)')
        }
    }

    Invoke-Check 'Project: representative tender pairs retain current release gates and links' {
        $index = Get-CurrentText (Read-Source (Join-Path $ProjectRoot 'INDEX.md'))
        $pairs = @{}
        foreach ($target in @(Get-LinkTargets $index | Select-Object -Unique)) {
            if ($target -match '^contractor-tender-(email|english)-(\d{4}-\d{2}-\d{2})\.md$') {
                $language = $Matches[1]; $date = $Matches[2]
                if (-not $pairs.ContainsKey($date)) { $pairs[$date] = @{} }
                $pairs[$date][$language] = $target
            }
        }
        Assert-True ($pairs.Count -gt 0) 'No indexed representative contractor tender pair found'
        foreach ($date in @($pairs.Keys | Sort-Object)) {
            Assert-True ($pairs[$date].Count -eq 2) "Incomplete tender pair for $date"
            foreach ($language in @('email', 'english')) {
                $path = Join-Path $ProjectRoot $pairs[$date][$language]
                $current = Get-CurrentText (Read-Source $path)
                Assert-LocalLinks $path $current
                # Header notice only. Older body text cannot satisfy a release gate.
                $notice = ([regex]::Matches($current, '(?m)^>.*$') | ForEach-Object { $_.Value }) -join "`n"
                Assert-True ('INDEX.md#open-decisions-and-release-holds' -in @(Get-LinkTargets $notice)) "Tender notice lacks exact release anchor: $language"
                Assert-Patterns $notice @('DRAFT NOT ISSUED', 'RH-08', 'A20-1.*(?:missing|mangler)', '(?:independent|selvstendig)', '(?:Flush|Fluktende)', '(?:one bedroom|ett soverom).*(?:two bedrooms|to soverom)')
                if ($language -eq 'english') {
                    Assert-Patterns $notice @('Historical dispatch status is unknown', 'open holds ONLY after explicit user release', 'exact outgoing text.*recipients.*purpose.*file/revision/date manifest', 'missing documents.*unresolved assumptions', 'enquiry authorizes no site work', 'Completed RIB design is not required', 'Construction, product ordering and fixed-price scope.*separate release', 'closure evidence for relevant holds', 'no external release')
                }
                else {
                    Assert-Patterns $notice @('Historisk utsendelsesstatus er ukjent', 'åpne avklaringspunkter KUN etter uttrykkelig frigivelse', 'nøyaktig utgående tekst.*mottakere.*formål.*filnavn/revisjon/dato', 'manglende dokumenter.*uavklarte forutsetninger', 'forespørsel tillater ikke arbeid', 'Ferdig RIB-prosjektering er ikke et vilkår', 'Utførelse, produktbestilling og fastprisomfang.*separate frigivelse', 'lukking av relevante avklaringspunkter', 'ingen frigivelse for utsendelse')
                }
            }
        }
    }
}
else {
    Write-Output 'SKIP  Optional project checks: no -ProjectPath supplied; no private project opened.'
}

$failed = @($Results | Where-Object { -not $_.Passed }).Count
$passed = $Results.Count - $failed
Write-Output "SUMMARY  $passed passed; $failed failed; $($Results.Count) named static checks."
Write-Output 'LIMITS  Text/metadata/path assertions only; no model behavior, engineering, full YAML/Markdown validation, or Python tests. External links and fenced examples are not checked; project links are limited to current registers and indexed tender pairs. No source files are changed.'
if ($failed) { exit 1 }
exit 0