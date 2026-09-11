# BTBA Agent — Change Log

**Publication privacy note:** Project identifiers and private inventory details
have been omitted from the public release notes. Historical review claims below
remain reported history, not independently verified project evidence.

---

## 2026-09-11 — Evidence and Evaluation Hardening

Continued the reliability work with reproduced failure cases, not additional
readiness claims. See [docs/reliability-hardening-2026-09-11.md](docs/reliability-hardening-2026-09-11.md).

- Detail reports no longer alias their input; layer unknowns are explicit.
  Project numeric values require source-matched evidence locators, and synthetic
  sources/quantities cannot become project evidence by relabeling the package.
  Numeric range and fixed arithmetic tolerance checks prevent floating-point
  collapse or scale-dependent comparisons from looking consistent.
- Revision reports include field-level before/after differences, absent-versus-null
  distinction, metadata changes and changed/removed holds. Hold removal triggers
  review/revalidation, not closure. No-change and deep reverse-order dependency
  regressions protect complete traversal. Well/opening alignment is explicitly
  unassessed because its geometry is not modeled.
- PDF extraction now includes rectangle edges, unrotated crop-relative coordinates,
  rotation/crop metadata, source-byte hashes and source-scoped candidate IDs.
  Hidden crop content, unsupported paths and truncated candidate samples are
  reported as omissions rather than implied complete wall geometry.
- Added a strict evaluation-run schema and local record checker. Pending templates
  remain not_run; complete case/attempt coverage, reviewer/configuration/timing,
  scoped artifact paths and hashes are checked. Fixtures never count as host
  performance. Timestamp validation is explicit rather than dependent on optional
  JSON Schema date-time packages. No model or transcript content is executed.
- SVG labels are bounded and invalid control text rejected; the saved synthetic
  preview matches the renderer. Updated and long-label renders were inspected.

**Observed validation:** 97 automated tests and 81 static checks passed; skill
lint found 0 errors and 19 existing review-status warnings. Dependency compatibility,
whitespace and relevant editor diagnostics passed. Tests initially reproduced the
old defects; an intermediate traversal return-placement defect and missing optional
date-time validation were fixed with dedicated regressions.

**Limits:** Live-host evaluations remain not run. Source locators/hashes do not
establish truthful provenance or professional approval. The tools do not establish
site conditions, full wall/room topology, native CAD/BIM authoring, general sandboxing
or licensing resolution. No private project was opened, no packages were added in
this batch, and no staging, commits, sends or publication were performed.

---

## 2026-09-11 — Reliability Repairs and Tested Detail Records

Implemented a bounded reliability upgrade after the audit. See
[docs/reliability-implementation-2026-09-11.md](docs/reliability-implementation-2026-09-11.md)
for the per-finding status and remaining work. No claim that the entire agent is
professionally verified or that every audit item is closed.

- Source-checked room, energy, escape, moisture and stormwater distinctions against
  current public DiBK pages; replaced broad regulatory, building-physics and
  electrical defaults with scoped evidence workflows. Removed relevant downstream
  room/height, curing, heritage, pricing and symptom-to-repair shortcuts.
- Reworked six shared templates to remove preset grades/loads/limits, invented
  inspection/approval schedules, generic costs and maintenance intervals. Preserved
  their purposes using source/applicability, review and release fields.
- Drawing schema v2 adds explicit page/view selection, retained sparse text,
  caller-supplied calibration rather than confirmed scale text, supported linear
  DXF unit conversion, angular separation, native DWG rejection, no implicit OCR
  and output overwrite protection. Optional external OCR still needs separate
  availability, privacy and backend-scope verification.
- Added strict detail records, root-scoped local reads, units/datums/source/dependency
  validation, rectangular quantities and conservative revision invalidation. The
  local tool cannot close holds or authorize construction. A synthetic wall/window/
  well fixture produces a dimension-labeled SVG schematic; the saved preview is
  checked against the renderer and was rendered for visual inspection.
- Added duplicate-YAML-key rejection, shared Python 3.12 test dependencies,
  Windows/Ubuntu CI definition and twelve live-host evaluation cases. CI is defined
  locally but not claimed executed remotely; live model evaluations remain not run.
- Removed ignored local configuration link prerequisites and rewrote the unbuilt
  geodata specification to reject guessed endpoints and map-to-safety shortcuts.
  No live geodata connector was implemented.

**Observed verification:** 60 deterministic tests and 79 static source contracts
passed. Skill lint: 25 skills, 0 errors, 19 existing unreviewed-status warnings.
Dependency compatibility and whitespace checks passed. Regression fixtures are
synthetic; no private project was read. The initial electrical description-colon
error, retained legacy extraction-reference body and static matcher mismatch were
corrected and rechecked rather than hidden.

**Remaining:** qualified technical/standards/product review, broader drawing and
CAD/BIM tests, live host behavior/permissions, hosted CI execution and maintainer
resolution of root MIT versus Proprietary skill licensing. Existing source/history
records remain; no license grants, private data, commits, sends or publication changed.

---

## 2026-09-11 — Agent Audit and Twelve-System Industry Research

Added [docs/agent-audit-and-direction-2026-09-11.md](docs/agent-audit-and-direction-2026-09-11.md)
and [docs/industry-agent-research-2026-09-11.md](docs/industry-agent-research-2026-09-11.md).
Reviewed 12 distinct industry agents/assistants: selected implementation files
from six public projects and first-party descriptions of six commercial systems.
Commercial claims, observed source mechanisms and BTBA recommendations are kept
separate. No external system was installed, run or integrated; licensing and
Norwegian applicability remain explicit adoption considerations.

The repository audit recognizes evidence/authority separation, scoped lifecycle
and tender workflows, and the tested local beam tool as strengths. It records
source-checked room/energy guidance mismatches, an internal vapour-rule conflict,
and synthetic observations of scale confirmation, DXF unit labeling, embedded
example syntax and duplicate YAML-key behavior. These are **open findings**, not
fixes or claims about a property's safety. Broader electrical/technical guidance,
licensing consistency, reproducible setup and host enforcement require follow-up.

Recommended direction: source and extractor reliability first, then a small
evidence/element/detail schema and one wall–opening–window-well demonstration.
An ordered B01–B09 backlog includes acceptance evidence rather than promising
autonomous CAD or a large agent hierarchy. Existing README and roadmap now link
to the audit; technical skills and implementation were not modified in this pass.

**Observed checks:** 60 static contracts and 27 beam tests passed again; skill
lint found 0 errors and the existing 23 unreviewed-status warnings. The targeted
probes exposed the documented gaps despite that passing baseline. Checked 60
local document links/ranges/anchors and exactly 12 research entries; no validation
failures. Edited-document diagnostics and tracked whitespace checks were clean.
No private project was opened, no packages installed, and nothing was staged,
committed, sent or published. Findings and proposals remain local documents.

---

## 2026-09-11 — README Reality Check and Construction-Detail Direction

Rewrote [README.md](README.md) around BTBA's purpose: a Norway-first assistant
connecting project evidence, design decisions and construction planning. Replaced
the stale 20-skill/version-2 completion list with the current 25-skill inventory,
separating instruction workflows, implemented local tools, prototypes and unbuilt
integrations. Removed blanket code-currency, professional-grade, mandatory-stamp,
automatic-memory and completed-template claims. Retained the existing local
beam-calculator work without changing its implementation.

- [docs/readme-audit-2026-09-11.md](docs/readme-audit-2026-09-11.md) records the
  evidence, corrections and unfinished extraction, source, template and connector
  work. This was not a full technical review of all domain guidance.
- [docs/construction-plans-roadmap.md](docs/construction-plans-roadmap.md) defines
  the next stage: wall instances/types, layers, openings, window wells, junctions,
  civil/site interfaces, quantities and review holds before CAD/BIM automation.
- [templates/construction-detail-package.md](templates/construction-detail-package.md)
  provides an original blank, source-linked draft. Added an optional procedure to
  the existing execution skill and routing, not a new engineering engine. No
  project dimensions, compliant default well size or construction release supplied.
- Corrected the Quick Ask prompt's stale path/private-project fallback and aligned
  directly relevant contributor guidance with current loading/evidence boundaries.
- Reviewed the supplied public SmartPlansAI, civil-agent overview and SciML4StructEng
  pages. SmartPlansAI's inspected tree contains no implementation. No external code
  was adopted and no dataset or CAD/model accuracy was evaluated.

**Observed validation:** 60 default static source-contract checks passed with no
private-project argument; all 27 existing beam numerical/CLI tests passed in the
existing isolated environment. The isolated environment lacked PyYAML for skill
lint, so lint was rerun successfully with the existing system Python: 25 skills,
0 errors and 23 unreviewed-status warnings. No package installation was needed.
Edited-file diagnostics and tracked whitespace checks were clean.

**Limits:** Source assertions are not behavioral evaluations. New detail-package
examples are expected outcomes, not executed agent tests. Drawing extraction,
MCP services, CAD output, engineering applicability and project conditions were
not validated. All changes remain local; no private project files were opened,
staged or published, and no send, move, deletion, commit or push was performed.

---

## 2026-09-06 — Skill Authoring Primer Follow-Up

Reviewed the public [Claude Skills for Construction primer](https://aiconstructionnews.com/blog/ai-primers/claude-skills-for-construction-what-they-are-and-how-to-use-them)
(May 19, 2026). Most context-navigation advice was already covered. Added a
six-element workflow contract to the existing authoring standard: task,
procedure, inputs, rules, output and examples. Original synthetic arithmetic
and revision-conflict examples demonstrate expected outputs and prohibited
inferences without copying private project data or creating new skills.

Lifecycle guidance now explicitly records requested output destinations and
uses document registers while separating revision recency from applicability
and approval. No extra project context file, mandatory whole-folder scan or
host-autoload assumption was introduced. Changes remain local; private project
records were not accessed or changed in this follow-up.

Validation: 42 default static source-contract checks passed, with no private
project accessed; whitespace checks and editor diagnostics were clean. Fixed
existing authoring references exposed by the added relative-link check. This
is not live agent behavior testing. Example expectations are not represented
as executed behavioral evaluations. Python execution remains untested.

---

## 2026-09-06 — Construction Workflow Connections

Reviewed the public [10 Plug-and-Play Claude Skills for Construction Professionals](https://aiconstructionnews.com/blog/ai-trends/ccc)
article (May 20, 2026). Subscriber-only skill files were not accessed or copied.
Its workflow descriptions informed original additions to existing skills, not
ten new skills or another mandatory project context file.

- Context builder and document control build on the existing lifecycle index.
  Added scoped correspondence/RFI records with response and closure evidence.
- Drawing summaries now identify each reviewed sheet/page, extraction method,
  source revision, quantity provenance, coverage and re-extraction needs.
- Tender modes connect procurement packages to pricing lines and distinguish
  client-side tender drafting from contractor bid/no-bid recommendations.
- Estimate review separately reconciles scope, arithmetic and price adequacy,
  including owner-direct overlaps, unpriced work, alternatives and VAT bases.
- Execution gains contract-departure, package-schedule, progress and FDV records.
  Contract comparisons require actual client terms and applicability checks;
  the article's example damages cap is not a Norwegian default.
- Optional routes retain scoped loading and existing authorization gates.
  No private project records were changed by this follow-up. No new database,
  background monitoring, mandatory whole-folder scan or external publication.

Validation: 40 default source-contract checks passed without accessing private
projects, edited-file whitespace checks passed, and editor diagnostics were
clear. Independent scoped static review found no actionable issues in these
additions. See [the regression script](tests/Test-AgentContracts.ps1).
These additions do not validate engineering, contract legality, extraction
accuracy or live agent behavior. Python execution remains unperformed.

---

## 2026-09-06 — Integrated Agent and Project Reconciliation

This entry supersedes the intermediate correction-status statements below,
not their historical evidence. Work remains local on the existing feature
branch. Private project records remain Git-ignored; no send, commit or push
was performed.

- Repaired actual agent paths and removed hardcoded project facts. Shared rules
  now distinguish Norwegian law, project requirements, advice and approvals.
- Replaced repeated intake and forced skill loading with repository/general/
  project modes, index-first retrieval, lazy lessons and guarded dependencies.
  The startup/lifecycle reciprocal load pair is removed. Token savings have
  not been measured.
- Added evidence-status, changed-input and purpose-specific release gates.
  Historical records are preserved and quarantined, not certified by recency.
- Private project reconciliation details are omitted from this public log;
  only reusable agent safeguards are included in the release.
- Corrected the specific L001–L008 target guards, the malformed roof-load row,
  unsupported snow-zone table and targeted professional/legal shortcuts.
  All eight lesson guards are implemented as instruction text, not proven
  model behavior. Other technical tables still require source verification.
- Added [repeatable static contract checks](tests/Test-AgentContracts.ps1).
  Runs passed 21 checks without project access and 31 with an explicitly supplied
  project path. Checks cover source contracts, paths/anchors, loading metadata,
  evidence safeguards and selected project regressions, not engineering approval.
- Independent static review found further context-loss and release-gate defects;
  those findings were corrected, including locally quarantining historical
  correspondence and protecting preliminary enquiries from circular design gates.

**Validation limits:** Python configuration was declined, so the modified
Python validator and malformed-YAML runtime cases were not executed. Static
checks and clean editor diagnostics do not establish runtime agent behavior,
complete regulatory correctness, structural safety or an approved project.

---

## 2026-09-06 — Focused Audit Corrections (Static Review Only)

**Scope:** `skills/validate_skills.py`, `skills/README.md`,
`skills/lessons-learned/SKILL.md`, and this change log only. Existing work in
other files is not part of this correction. No Python execution or environment
configuration was authorized for this pass. No runtime validator result is
claimed; editor diagnostics and read-only source checks are not runtime tests.

- **Validator hardening:** standalone frontmatter delimiters, parse-error
  handling, mapping/string-key validation, and field type checks before
  string operations. Empty/scalar/list frontmatter and malformed field shapes
  receive structural errors rather than reaching unsafe `.get`/`len` calls.
  These code paths require runtime regression tests when execution is allowed.
- **Local conventions, not upstream claims:** flat routing fields and the
  200-character description recommendation belong to BTBA. Removed the claim
  that longer text is invisible to invocation matching. No host portability
  or upstream conformance is certified by this linter.
- **Status honesty:** absent status means unreviewed. A `production` label
  requires separate scope/review/test evidence; one project use is insufficient.
  Meaningful warnings should not be suppressed to obtain a zero count.
- **Eight lesson guards reviewed against current target text:** L002/L007
  have implemented instruction guards; L003/L004/L006/L008 have partial
  coverage; L001/L005 lack the specific claimed target guard. All eight remain
  behaviorally unvalidated. Replaced the blanket promotion claims with evidence
  locations and limitations, without modifying those target skills.
- **Unsafe lesson shortcuts removed:** no universal accepted tile-roof dead
  load and no permit-exemption route to structural/geotechnical safety. Load
  inputs require assembly-specific provenance and appropriate engineering
  review. This correction does not validate previous project calculations.
- **Lesson maintenance:** reversible, in-scope lesson corrections do not
  require a new approval each time. Engineering decisions, outbound actions,
  destructive changes, and professional approvals retain their own gates.
- **Loading ownership:** removed the lessons-to-startup `load_with` back-edge
  and documented once-per-session ownership. The separately owned
  `project-lifecycle` still declares `load_with: [session-initialization]`,
  while startup declares lifecycle as a companion. That remaining reciprocal
  pair needs owner correction; a prose rule is not a tested cycle guard.

**Open limitations:** runtime malformed-YAML/type regression tests, behavioral
guard tests, and domain-source validation were not performed. The validator
does not check reference existence or dependency cycles. Target-skill issues
include the roof-table unit inconsistency, exemption-to-GREEN shortcut,
missing boundary survey labels, incomplete correspondence checklist, and
missing unmatched-flag fallback. These are not closed by editing the lesson
record. Legacy repository memory contains the prior 200-character/upstream,
promotion, and zero-warning claims; it is outside this four-file ownership
scope and must not be used as verification of the corrected claims.

### Correction to the Earlier v3.0 Audit Narrative

The entry below records earlier work and reported counts, not proof that all
findings were fixed. A Trust Boundary heading only establishes text presence;
it does not establish sound engineering guidance. Likewise, reported zero
warnings do not establish correctness, safe behavior, complete remediation,
or production readiness. Historical archive actions and project classifications
are not independently revalidated by this pass. Absence of references alone
does not prove a document is obsolete or safe to archive.

---

## v3.0 (2026-09-06) — Full Agent Audit: Lifecycle, Trust Boundaries, Token Discipline

A full self-audit of the agent — architecture, token efficiency, self-correction,
and document lifecycle — was reported alongside a learnings review of two
external agent-operating-system repos (`chrstian6/contractor`,
`cmaurer/claude-general-contractor`).

### Audit findings

1. **No project document lifecycle.** The earlier pass reported inconsistent
  document naming and unclear current-versus-superseded status. The reusable
  issue is dependency drift across documents (Lesson L002), not a requirement
  to move every superseded file. Private inventories are omitted.
2. **Token cost paid on every session regardless of relevance.**
   `system_prompt.md` (loaded in full, every session) duplicated the entire
   `technical-education-support` skill's simplification method as a ~55-line
   "Educational Communication" section, including a table of illustrative
   `example.com` placeholder links.
3. **11 of 24 skill descriptions reportedly exceeded the local 200-character
  style recommendation** (up to 496 chars). This was a concision finding,
  not evidence of truncated descriptions or invisible invocation matching.
4. **`drawing-reader/SKILL.md` was 539 lines**, over the 500-line guideline,
   with four full pipeline code blocks (Marker, ocr-skill, ezdxf, vision-model
   prompt) loaded in full even when only one pipeline applies to a given file.
5. **Escalation/trust-boundary logic existed but was inconsistent** — some
   skills had a `## ⚠️ DISCLAIMER` or `## Escalation Flags` section, others had
   none, using different headings and none machine-checkable. (Partially
  addressed in the prior session's skill-structure audit; headings were
  added, but their content and behavior were not thereby validated.)
6. **`residential-tender-writing` had no `triggers:` field**, inconsistent
   with every other skill's frontmatter.
7. The reusable response is a scoped *lifecycle convention*, not mandatory
  bulk cleanup. Private folder assessments are omitted from the public log.

### Changes Reported in the Earlier Pass (Not Complete Remediation)

- **New skill: `skills/project-lifecycle/SKILL.md`** — defines the `INDEX.md`
  convention (current phase / active documents / needs-verification / archived),
  the `archive/` convention, consistent versioned-naming guidance,
  and a session-end check that proactively does what Lesson L002 only catches
  reactively. Wired into `session-initialization` (Step 3b/3c) and
  `system_prompt.md`'s skill table and Success Metrics.
- **Earlier archival work was reported**, but private paths and inventory
  details are omitted. "OUTDATED" labels or zero remaining references do not
  establish that a move preserves required evidence. This correction does
  not independently verify those archival actions.
- **Trimmed `system_prompt.md`'s "Educational Communication" section** from
  ~55 duplicated lines to a 6-line pointer at `technical-education-support`,
  plus a standalone rule (now stated once, cross-cutting): never fabricate a
  placeholder link and present it as a real resource.
- **Trimmed all 11 over-length skill descriptions** to ≤200 chars and added
  the missing `triggers:` field to `residential-tender-writing`.
- **Split `drawing-reader/SKILL.md`** — Pipelines B–E's full code moved to
  `skills/drawing-reader/references/extraction-pipelines.md`; SKILL.md now
  carries only Pipeline A in full plus a routing table pointing to the rest.
  539 → under 500 lines.
- **Added Trust Boundary headings** — the earlier pass reported every
  `safety_level: high|critical` skill (22 of 25) had a section stating what Bob
  decides alone, what's preliminary-only, and what always needs a named
  licensed professional or authority. The 3 process/meta skills (`routing`,
  `session-initialization`, `lessons-learned`) got a lighter version
  clarifying their `critical` rating is about process integrity, not
  professional licensing.
- **Previously reported structural lint result:** 25 skills, **0 errors, 0
  warnings** (25 warnings mid-audit, 12 pre-existing). Not rerun in this
  correction; the validator has since changed. This count is not a quality,
  engineering, behavioral, or production-readiness finding.
- Bumped `system_prompt.md` to **Agent version 3.0 — 25-skill architecture**
  and updated its Success Metrics with the project-coherence/lifecycle rule.

### Learnings applied from external repos (this session + prior session)

- `chrstian6/contractor`: LEARNINGS.md `Trigger/Lesson/Guard/Promoted` schema
  (adopted into `lessons-learned` in the prior session) and its general
  "short main file, detail loaded per-role" discipline (applied here by
  trimming `system_prompt.md`).
- `cmaurer/claude-general-contractor`: per-skill `## Trust Boundary` section
  and `status: draft|production` frontmatter (adopted in the prior session;
  this session reportedly added sections to the remaining 13 skills. Their
  presence did not validate their contents or establish review status).
- Not adopted: the multi-agent delegation org, git-branch-per-task, and
  adversarial-reviewer-swarm pattern from `contractor` — Bob is a single
  advisory agent producing documents for a human to act on, not a coding
  swarm; that machinery doesn't map onto this problem.

---

## v2.0 (2026-08-09) — Architecture Overhaul

Major release. See README.md for the full feature list.

**Key changes:**
- **20-skill modular architecture** — all skills restructured to `skills/<name>/SKILL.md` directory format per agentskills.io spec
- **3 new domain skills**: `geotechnical`, `soknad-package`, `bim-ifc`
- **2 new utility skills**: `drawing-reader` (with OCR pipeline + security fencing), `drawing-investigation-protocol` (now separate from reading)
- **`formulas-reference` split** into core SKILL.md + `references/` for historical materials and worked examples
- **DOK arealanalyse** section added to `building-code-tek17`
- **Structural failure modes** diagnosis guide added to `structural-engineering`
- **Decision log persistence** — session facts can be written back to `project.md`
- **MCP config** expanded: Marker, ocr-skill, ezdxf, ifcmcp, Geonorge added
- **README** completely rewritten to match actual architecture
- All `license: Proprietary` fields added to every skill (agentskills.io spec compliance)
- All stale file paths removed from system_prompt.md, README, routing

---

## v1.3 (2026-07-27) — Session Initialization Fix

> **Historical note:** Skill paths in this section (e.g., `skills/session-initialization.md`) use the old flat-file format. The current system uses `skills/<name>/SKILL.md`. All functionality described below is still present — only the paths changed.

You were right: BTBA was asking questions in circles and not reading from its own documentation. This fixes it.

---

### The Core Problems (Identified)

1. **No forced documentation reading** — Skills existed but BTBA would skip them.
2. **No image/attachment checking** — If you uploaded photos, BTBA might not ask to see them.
3. **No decision logging** — Questions got asked multiple times in the same session.
4. **No session context** — Every response started from scratch instead of building on what was already discussed.
5. **No structured questioning** — BTBA would ask 15 questions at once instead of the 3-4 that actually matter.

---

### The Fixes (v1.3)

### 1. **Mandatory Session Initialization** (`skills/session-initialization.md`)

Before answering ANY question, BTBA now:

```
✓ Detects your language (Norwegian/English)
✓ Checks for attachments or images
✓ Loads project context if one exists
✓ Reads foundational skills (routing, structure, code)
✓ Creates a Decision Log to track what's been asked
✓ Orients you with one clear question
```

**Result**: No more starting from zero. No more "what's the material?" after you already said it.

### 2. **Non-Repetition Rule** (Part of Session Init)

Every question is checked against the Decision Log first:

```
IF question already answered this session:
  → Skip it, reference the prior answer
  → Move to the NEXT logical question

IF question is similar but different:
  → Acknowledge the context
  → Ask only what's new
```

**Result**: Focused conversations. One answer per question per session.

### 3. **Structured Drawing Protocol** (`drawing-investigation-protocol.md` + Session Init)

If you provide photos or drawings:

```
1. Ask you to upload them (if you haven't)
2. Load them immediately
3. Describe what's visible
4. Ask systematic gaps (dimensions, materials, loads, conditions)
5. Document in Decision Log: "Drawing shown: [description]"
```

**Result**: Drawings get examined before structural claims are made.

### 4. **Decision Log** (Updated Core Framework)

Every session now has a running log:

```
# Decision Log
- Question 1: Is the beam load-bearing?
  Answer: Yes, supports floor above
  Source: User + drawing inspection
  Confidence: High

- Question 2: What material?
  Answer: Timber, ~200×100mm (observed)
  Source: Drawing measurement
  Confidence: Medium

- Assumption 1: C24 grade (not specified)
  Impact: Load-bearing capacity
  Can override: Yes
```

You can always see what's been established and what's still open.

### 5. **Documentation-First Workflow**

The updated `system_prompt.md` now requires:

```
Step 1: Check Decision Log (don't repeat)
Step 2: Load relevant skills (routing.md applies)
Step 3: Read the drawings (if present)
Step 4: Do the analysis
Step 5: Document it in Decision Log
```

**Result**: Every answer is grounded in documentation, not improvisation.

---

## How It Works in Practice

### Old Flow (Broken)
```
User: "Is my kitchen beam adequate?"
BTBA: "What's the span? What material? What loads? When was it built?"
      [15 questions at once — feels circular]
```

### New Flow (Fixed)
The project reference in this historical dialogue is a placeholder, not a
published client identity.

```
[Session Init runs]
BTBA: "I'm ready. What's the project address or name?"

User: "Kitchen at [selected project], beam was installed 12 months ago."
[Decision Log creates entry for project + prior knowledge]

BTBA: "Got it. Can you share a photo of the beam?"
[Waits for image, then loads drawing-investigation-protocol]

User: [Uploads photo]
BTBA: "I see a concrete tile roof, ~3m span. I need:
      - Exact beam dimensions (take a tape measure?)
      - Support type at each end
      - Any visible distress?"
[Each question MATTERS; none repeated]
```

---

## Files Changed

| File | What Changed |
|---|---|
| `system_prompt.md` | Added Session Initialization requirement + updated Core Decision Framework to include Decision Log steps |
| `skills/session-initialization.md` | NEW — Defines the startup checklist, non-repetition rule, and Decision Log structure |
| (All other skills) | No changes — they're loaded on-demand as before |

---

## What You'll Notice

✅ **First message is always an orientation**, not a flood of questions  
✅ **Second message asks only what you haven't answered yet**  
✅ **Photos/drawings are requested explicitly** and examined before analysis  
✅ **Assumptions are documented** — you can challenge them  
✅ **Conversations don't loop** — each new question moves forward  

❌ **Less freestyle**, more structured  
❌ **Requires you to provide data** (won't pretend to know things)  
❌ **More reliance on drawings** — "show me" before "tell me"  

That's intentional. Circles happen when there's no structure.

---

## Next Steps for You

1. **Try it on your kitchen beam question** — see if the flow feels different
2. **Upload that photo or drawing** when prompted — BTBA will wait
3. **Let me know if the questions make more sense now** — they should be focused, not circular

This fix is about discipline: reading docs first, checking what's been said, asking only what matters, documenting everything. That's how a real contractor works.

---
