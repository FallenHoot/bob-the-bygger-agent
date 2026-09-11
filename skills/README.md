# Skill Authoring Standard

This document defines BTBA's **local authoring conventions** for skills in
`skills/`. The [Agent Skills specification](https://agentskills.io/specification)
is an external reference, not a claim that this local schema implements every
upstream requirement. BTBA's flat routing fields and 200-character description
recommendation are local choices. Check the target host's current schema before
exporting a skill; compatibility is not established by this validator.

When Python execution is permitted, run `python skills/validate_skills.py` after
editing a skill. If execution is declined, report static review only; do not
configure Python or claim a successful validator run.

## Directory Structure

```
skills/<skill-name>/
├── SKILL.md          # required — instructions + frontmatter
├── scripts/           # optional — executable code (Python/Node/Bash)
├── references/        # optional — detailed docs loaded on demand
└── assets/            # optional — templates, schemas, lookup tables
```

`<skill-name>` must exactly match the `name:` field in `SKILL.md` — lowercase
letters, numbers, and hyphens only, max 64 characters.

## Frontmatter Schema

```yaml
---
name: skill-name
description: What it does and when to use it. Prefer at most 200 characters locally.
license: Proprietary
triggers: [keyword1, keyword2, keyword3]
load_with: [other-skill-name]
safety_level: low
status: unreviewed                          # optional: unreviewed | draft | production
dependencies: python>=3.8, pymupdf>=1.24.0   # only if scripts/ exists
---
```

| Field | Required | Rules |
|---|---|---|
| `name` | Yes | Non-empty string; must match directory name exactly |
| `description` | Yes | Non-empty string. **Prefer ≤200 characters locally**, a style warning rather than a hard limit. Front-load the trigger scenario; no truncation or invisible invocation matching is established here. |
| `license` | No | Non-empty string, e.g. `Proprietary` |
| `triggers` | No | List of non-empty keyword/phrase strings. Keep in sync with the corresponding prose rule in `routing/SKILL.md`; the routing skill does not programmatically consume this field. |
| `load_with` | No | List of non-empty skill-name strings describing companion skills. Use `[]` if none, not null. Not an instruction to recursively reload skills. |
| `safety_level` | No | String: `low`, `medium`, `high`, or `critical`. High/critical marks potentially consequential errors, not certified safety. |
| `dependencies` | No | Non-empty string listing packages and versions when scripts need them. Presence does not verify installation or compatibility. |
| `run_before` | No | Non-empty string for orchestration order, e.g. `all_other_skills` or `none`. An ordering hint, not a dependency to load. |
| `auto_load_on` | No | List of non-empty event-name strings, e.g. `[image_upload]`. Local loading hints; runtime behavior is not tested here. |
| `load_priority` | No | Non-empty string, e.g. `on-demand`, describing the intended loading priority. |
| `status` | No | String: `unreviewed`, `draft`, or `production`. Absent means **unreviewed**, never implicit production. `draft` is work in progress. `production` is a self-declared review state requiring separate evidence, not validator certification. |

**Local schema only: do not use a nested `metadata:` block.** BTBA keeps its
fields at the top level. This is not an upstream prohibition of `metadata`.
Frontmatter must be a YAML mapping with string keys between standalone `---`
delimiter lines. Supplied fields must have the types above, including optional
fields; null values and lists containing non-strings are not accepted.

### Review status is not certification

One project use does not establish production readiness. Before declaring
`production`, record the reviewed scope, sources and revisions, reviewer/date,
representative success and failure cases, and unresolved limitations in the
skill or its existing references. A process guard implemented as instruction
text is distinct from a guard tested in use. Neither a status label nor a
clean structural lint result verifies engineering or legal conclusions.

### Loading ownership and cycles

Startup establishes mode and scope once. Lessons load only for matching failure
modes or an explicit retrospective; lifecycle loads for relevant updates.
Companion skills must not request startup again. Keep loading
idempotent with a loaded/visited set in any implementation; references back
to a caller are documentation, not new load edges. Lifecycle work at session
end must not restart initialization. Review such edges separately: this
validator does not traverse references or detect dependency cycles.

**Do not put free-text sentences containing an unquoted colon directly as a
frontmatter value** (e.g. `compatibility: Requires one of: X, Y`). YAML reads
the second colon as a new mapping key and fails to parse. If you need
prose like this, quote the whole value (`compatibility: "Requires one of: X, Y"`)
or — preferably — move it into the SKILL.md body under a `## Requirements`
heading instead of frontmatter.

## SKILL.md Body

- Keep the file under **500 lines**. If it's longer, move detailed reference
  material (symbol tables, extended examples, code samples) into
  `references/*.md` and link to them from the body.
- Structure: `## Purpose` or `## Domain` first, then the core procedure,
  then edge cases / integration points with other skills last.
- Reference files in `references/`, `assets/`, and `scripts/` explicitly by
  relative path so the agent knows when to load them.

### Workflow Contract

For new or materially revised workflows, check these six elements in existing
sections. Do not add duplicate headings merely to satisfy the checklist, or
bulk-rewrite unrelated skills. A skill should specify a reusable task procedure,
not just a topic description or a long one-off prompt.

| Element | Authoring check |
|---|---|
| Task | State the trigger, intended user/decision, boundaries and when not to use it. |
| Workflow | Define ordered actions, evidence checks, stop/continue conditions and review/release boundaries. |
| Inputs | Separate essential evidence from optional context. Missing input must produce a bounded result or a targeted request, never an invented fact. |
| Rules and assumptions | Distinguish statutory/project requirements, supplied client policy, assumptions and illustrative examples. Record source, revision and applicability; no client baseline means comparison unassessed. |
| Output | State the deliverable format, required fields, source/status/uncertainty fields, coverage limits and intended save location when persistence is requested. |
| Examples | Provide a small worked success case and a missing/conflicting-evidence case, with expected output and prohibited conclusions. Link larger examples for on-demand reading. |

#### Example Hygiene and Checks

Use synthetic examples by default. Do not copy private project records into
shared skills or test fixtures. An authorized, de-identified example still
needs a provenance and permission check. Mark example amounts, measurements,
dates, people and decisions as fictional; they are not defaults for other jobs.
Examples demonstrate output quality, not engineering, legal or client approval.

Keep a short input → expected output → forbidden inference case near the
workflow or in its existing references. Record actual observed output and test
status separately when run. A documented expectation or passing text assertion
is not a behavioral test, and repeated results do not guarantee correctness.

**Synthetic example: estimate arithmetic, not a market price.** Fictional line
E-01: 2 units × NOK 100/unit, reported amount NOK 250, VAT treatment unknown.
Expected: recomputed line NOK 200, variance −NOK 50 (recomputed minus reported),
with gross total unresolved. Forbidden: invent VAT, call the estimate complete,
or present NOK 200 as an agreed or reasonable price.

**Synthetic example: revision conflict.** Fictional sheet S-01 revision A has
documented approval for a defined scope; newer revision B is a draft with
changed geometry. Expected: retain both statuses, flag affected quantities
for review, and establish the applicable basis for the requested purpose.
Forbidden: call B approved merely because it is newer, or use A for the changed
scope without checking applicability.

These examples are local authoring checks, not additional default project facts
or a request to process every reference at startup. Register-driven context
and progressive reading remain owned by startup, routing and lifecycle.

### Trust Boundary section (required for `safety_level: high` or `critical`)

Any skill whose errors have physical, legal, or financial consequences must
include a `## Trust Boundary` section stating, in plain language:

1. What Bob may determine and state directly, on his own analysis.
2. What Bob may flag or estimate, but only as preliminary / low-confidence.
3. What needs an appropriate qualified designer, trade, survey professional,
  authorized decision maker or competent authority before consequential use,
  based on the actual task and applicable Norwegian requirements. Do not
  introduce a generic foreign PE licensing or wet-stamp requirement.

This consolidates escalation logic that would otherwise be scattered across
prose (see Lessons L003, L004, L006 in [lessons-learned](lessons-learned/SKILL.md) for
the failures this section exists to prevent). It is a required, single,
grep-able heading — not a rename of an existing "Disclaimer" or
"Escalation Flags" section, though it may reference or summarize one.
[The structural validator](validate_skills.py) warns (does not error) when this section is
missing on a high/critical skill, so adoption can be gradual.

## Why Recommend 200 Characters Locally?

Skills are read from disk per `system_prompt.md`. Concise descriptions help
readers identify the trigger without loading the whole skill. The local
200-character recommendation supports this style; it is **not an upstream
maximum, a portability guarantee, or a claim about host-side truncation**.
Keep descriptions and trigger lists aligned with the separate routing prose.

## Validation

Run [the PowerShell source-contract checks](../tests/Test-AgentContracts.ps1)
for repeatable static loading, link and evidence-guard regressions. Its optional
`-ProjectPath` checks only the explicitly supplied project's current registers;
the default run does not access private projects. This does not execute the
Python validator or test model behavior.

[The skill validator](validate_skills.py) is a **structural linter**. It checks frontmatter
parsing and mapping shape, string field names, required fields and field
types, name/directory match, local description-length and line-count
recommendations, locally disallowed `metadata`, unknown fields, status
declarations, a Trust Boundary heading for high/critical skills, and a
dependency declaration for non-empty script directories.

Malformed YAML and invalid field shapes are errors rather than reasons to
crash on string operations. Missing status warns that a skill is unreviewed;
declared production status warns to check its evidence separately. Warnings
are review prompts, not something to suppress merely to obtain a zero count.
The exit code is nonzero for errors, not for warnings.

**Not checked:** engineering/legal accuracy, applicability of citations,
guard execution, behavior on real projects, reference existence, dependency
cycles, package availability, upstream schema compliance, or production
readiness. A heading match does not verify the adequacy of its contents.
Static source inspection is not a substitute for running malformed-input
regression tests when execution is permitted.

Duplicate YAML keys are rejected rather than silently keeping the last value.
[Configuration regressions](../tests/test_skill_validator.py) exercise malformed
shapes, duplicate fields and invalid types. Use [the shared developer setup](../docs/development.md)
for the same environment across lint and tests. Passing these cases is not host
compatibility or technical certification.

```bash
python skills/validate_skills.py                 # check all skills
python skills/validate_skills.py --skill routing # check one skill
```

## Workflow Inspiration

The six-element authoring check was informed by the public
[Claude Skills for Construction primer](https://aiconstructionnews.com/blog/ai-primers/claude-skills-for-construction-what-they-are-and-how-to-use-them),
AI Construction News, May 19, 2026. The instructions and fictional examples here
are original adaptations. The article is not a host specification or Norwegian
technical/legal authority; its newest-revision advice does not establish approval.

*Last reviewed: 2026-09-06*
