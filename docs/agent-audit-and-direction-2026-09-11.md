# BTBA Agent Audit and Brainstorming

**Date:** 2026-09-11

**Scope:** Repository-mode audit; public industry research; no property assessment.

**Basis:** Local working tree on develop, based on Git HEAD
`d42417cf26abe8e71cea7dcb0d189f18331dc7e8`, including existing uncommitted work.

**Status:** Findings and proposals, not a completed remediation or engineering approval.

**Historical baseline:** This document preserves findings from before the reliability
implementation. See [the implementation status](reliability-implementation-2026-09-11.md)
for repairs and remaining gaps. Source files have changed; quoted observations below
describe the audited versions, not a claim that every defect still exists.

## Executive Conclusion

**BTBA has a strong evidence-and-review design, but it is not yet a dependable
construction-detailing system.** Its best work is keeping project scope, evidence,
assumptions, decisions and release status separate. Its most important weaknesses
are contradictory technical source content, unreliable extraction semantics and
the absence of behavioral/geometry checks behind many written safeguards.

The next investment should not be more topic skills or a large multi-agent team.
It should be a narrow, demonstrable workflow:

**source drawing → identified wall/opening → sourced detail → checked dimensions
and interfaces → review package → controlled revision.**

That is the practical bridge from a helpful conversation to the user's goal of
knowing how each wall and window well will be built.

## Audit Method and Limits

Reused the shared system/startup/routing instructions already loaded. Inspected
the current documentation, lifecycle/tender/detail workflows, representative
technical skills, all local utility source files, validator, tests and repository
metadata. The audit combines:

- source inspection and cross-document consistency review;
- four targeted in-memory Python probes using synthetic inputs;
- current DiBK spot-checks for room requirements and energy minimum levels;
- reruns of existing static contracts, skill lint and beam tests;
- [research of 12 industry agents/assistants](industry-agent-research-2026-09-11.md),
  including selected code from six public projects.

This is not a complete audit of every engineering claim, standard, template,
third-party dependency, host permission or runtime route. No real drawing was
processed, external agent installed, model evaluated or project directory opened.
The system Python used for probes/lint is not evidence of the editor's selected
interpreter. No claim of measured token savings, user time savings or competitor
superiority is made.

## What BTBA Is Doing Well

| Strength | Concrete evidence | Preserve / extend |
|---|---|---|
| **Clear separation of evidence and authority** | [System prompt](../system_prompt.md) distinguishes observations, user reports, assumptions, reviews and authority decisions; avoids equating missing paperwork with illegality | Make the same distinctions explicit in typed records and user-facing detail fields |
| **Useful Norway-first scope** | [Shared constraints](../.instructions.md), [BIM guidance](../skills/bim-ifc/SKILL.md) and [routing](../skills/routing/SKILL.md) distinguish Norwegian law, project requirements and foreign examples | Focus the product on residential renovation/extension detail coordination before broad civil automation |
| **Practical project/document control** | [Lifecycle](../skills/project-lifecycle/SKILL.md) separates recency from authority, draft from sent, and release purpose from general readiness | Keep an enquiry to appoint a designer possible even while construction holds remain open |
| **Scoped loading and privacy intent** | Startup selects repository/general/project mode; lifecycle and lessons are on-demand; private project directories are ignored | Retain the simple workflow; add actual scoped tool boundaries rather than mandatory whole-folder retrieval |
| **One well-bounded deterministic calculation tool** | [Beam engine](../skills/structural-engineering/scripts/beam_calculator.py) validates units/fields, rejects invalid inputs, preserves provenance and returns design compliance unassessed; 27 tests pass | Use this as the pattern for every new arithmetic tool, including detail quantities |
| **Strong commercial-document hygiene** | [Tender workflow](../skills/residential-tender-writing/SKILL.md) separates outcome from design responsibility; estimate and contract workflows require explicit bases | Connect detail IDs to pricing and variation records without inventing cost data |
| **Lessons tied to actual prevention checks** | [Lessons](../skills/lessons-learned/SKILL.md) distinguish implemented guard text from behaviorally tested prevention | Turn the eight known failure patterns into executable scenario evaluations |
| **More honest product documentation** | [README](../README.md), [claim audit](readme-audit-2026-09-11.md) and [detail template](../templates/construction-detail-package.md) distinguish tools, prototypes, instructions and future work | Continue reporting maturity by capability; do not use skill count or disclaimers as a quality score |

These are observed design/source strengths. Apart from the stated tests, they
are not claims that the host always follows the procedures in live project work.

## Priority Findings

Priority is about development order, not a finding that any building is unsafe.
**P0** means resolve before relying on the affected construction-detail output;
**P1** means foundational next work; **P2** means subsequent product hardening.

### F01 — P0: Some Central Technical Claims Are Demonstrably Wrong or Mis-scoped

[Building-code guidance](../skills/building-code-tek17/SKILL.md)
labels its U-value table as §14-3 minimum levels, but the current
[DiBK §14-3 first paragraph (a)](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17/14/14-3)
lists a different set for the stated non-log-wall category: wall 0.22, roof 0.18,
floor 0.18 and window/door 1.2 W/(m²K), plus leakage 1.5 h⁻¹. The skill instead
lists 0.18, 0.13, 0.10 and 0.80, with a thermal-bridge row. This is not a minor
wording problem: minimum levels and an energy-compliance pathway are different.
Those source values are an audit comparison, not a design prescription.

[Room guidance](../skills/building-code-tek17/SKILL.md) stated a generic
2.20 m habitable-room height and 7.0 m² minimum area. Current
[DiBK §12-7](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17/12/ii/12-7)
distinguishes the ordinary 2.4 m requirement for rooms for permanent occupancy
from other uses and existing-building exceptions. Its FAQ explicitly says there
is no fixed minimum room area; the earlier 7 m² was a recommendation, not a rule.

**Consequence:** a cautious system prompt cannot reliably neutralize specific
incorrect tables loaded for the task. The error may reach an otherwise polished
wall, window or room assessment.

**Next:** source-review the relevant room, energy, escape, moisture and structural
requirements. Replace blanket tables with narrowly scoped requirement records,
and mark unchecked material non-authoritative. Preserve corrections/provenance.
Do not call the entire technical library verified after these spot checks.

### F02 — P0: Building-Physics Advice Contains an Internal Contradiction

The former [vapour-control rule](../skills/sintef-byggforsk/SKILL.md) said the cold
side is at most one-fifth of total resistance, but simultaneously gives a
cold:warm ratio of at least 4:1. Those statements cannot both describe the same
positive resistances. This is an internal consistency finding, not an endorsed
replacement rule for membrane placement.

**Next:** verify against authorized current building-physics/product sources
before proposing assemblies. Record exposure, existing moisture conditions,
drying paths and applicability; no universal wall build-up. Nearby sd-value,
thermal-bridge and material tables also merit review, but were not independently
validated in this audit.

The audited [electrical skill](../skills/electrical-nek400/SKILL.md) also made
broad legal/insurance statements and uses uncertain authority terminology. These
remain **unverified findings for DSB/NEK/legal source review**, not conclusions
about the legality or insurance coverage of any installation.

### F03 — P0: Drawing Quantities Can Look Verified Without Being Verified

- [Scale detection](../skills/drawing-reader/scripts/extract_geometry.py)
  labels the first scale-like text `confirmed: true` without checking a dimension
  or a particular view. A synthetic page with a 1:100 plan and 1:5 detail returned
  one confirmed 1:100 scale.
- [DXF extraction](../skills/drawing-reader/scripts/extract_drawing.py)
  labels the raw dimension measurement `value_mm` without converting drawing
  units. A stub representing metre units and a raw measurement of 10 returned
  `value_mm: 10.0`, not a normalized 10,000 mm. This was an in-memory unit-path
  probe, not an end-to-end ezdxf-file test.
- [Geometry processing](../skills/drawing-reader/scripts/extract_geometry.py)
  takes the first page. Line candidates and text rows are not a semantic wall
  model, and the full sheet envelope is not the building envelope.
- The embedded Pipeline A example in the [drawing skill](../skills/drawing-reader/SKILL.md)
  fails Python parsing with `IndentationError`. This is example-code failure;
  it does not mean the separate extractor script has that syntax error.

**Next:** distinguish detected versus calibrated scale, normalize units before
assigning unit-specific fields, expose explicit page/view selection, preserve
uncertainty, and add fixtures before relying on quantities or generating details.

### F04 — P1: Good Guard Text Is Not Yet an Enforced Action Boundary

[Agent configuration](../.github/agents/btba-agent.agent.md) exposes broad read,
search, edit and execute tool categories. Privacy and release rules are primarily
instructions plus host permissions. Git ignore rules are not upload prevention.
No repository-level restricted executor or upload-policy test was found in the
tracked implementation; host controls were not evaluated.

**Next:** separate read-only extraction/checking, local draft writes and external
actions. Give future tools explicit allowed roots, network policy, payload limits,
timeouts and result schemas. Require a reviewed `ChangeSet` before model/file
changes and exact authorization before external writes. Do not promise runtime
enforcement from a prose gate or an agent named “reviewer.”

### F05 — P1: The Test Suite Measures a Smaller Thing Than Users Need

All **60 static contracts and 27 beam tests pass**, while the probes above expose
unsupported scale confirmation, a unit-label defect and broken example code.
This is not a contradiction: the static suite correctly says it checks text,
metadata and paths, not drawing semantics or live behavior.

**Next:** keep the current suite, and add three layers:

1. extraction/geometry and document-parser fixtures;
2. fixed agent scenarios with observed tool calls and final artifacts;
3. qualified technical review of selected Norwegian requirement/detail cases.

Use the [industry research](industry-agent-research-2026-09-11.md) for inspiration:
action-sequence evaluation, typed validators and artifact checkers solve different
problems. Neither a model's self-grade nor an LLM second opinion is ground truth.

### F06 — P1: Detail and Revision Relationships Exist Mostly as Prose

The new [detail package](../templates/construction-detail-package.md) has the
right fields. [Lifecycle](../skills/project-lifecycle/SKILL.md) has sensible
invalidation rules. There is no machine-checked wall → opening → well → detail →
quantity → pricing dependency model yet.

**Next:** introduce a small versioned record schema and validator, not necessarily
a graph database. Changing a sash or terrain level should identify affected well
geometry, flashing, quantities and ordering records with exact old/new evidence.
Unknown dependencies must remain visible; no silent cross-document rewrite.

### F07 — P1: Reproducibility and Distribution Need Work

No tracked CI workflow or root developer-dependency manifest was found. The beam
tool has its own requirements, while full skill lint currently uses PyYAML from
the system environment. Twenty-three skills have no explicit review status.

[Root license](../LICENSE) says MIT, while all 25 skill headers say Proprietary.
This is an unresolved licensing inconsistency, not a decision this audit can make.
It affects contributions and reuse; maintainers must clarify intended scope and
rights rather than an agent silently changing licenses.

**Next:** document one reproducible validation environment, add CI with synthetic
fixtures, and publish a capability/source-review manifest. Distinguish a local
working-tree capability from a released version. Clarify licensing before reuse
or distribution; do not erase meaningful unreviewed warnings just to look finished.

### F08 — P2: Local Validator Has a Duplicate-Key Blind Spot

[Frontmatter loading](../skills/validate_skills.py) used PyYAML safe loading.
A synthetic frontmatter block with `status: unreviewed` followed by
`status: production` parses without error and keeps `production`.

**Next:** reject duplicate fields and add malformed-input tests. This is a
configuration ambiguity, not proof of malicious use or an exploitable application.
Actual checked skills were not found to contain this duplicate-status fixture.

### F09 — P2: Progressive Loading Is Good, but the Task Payload Is Still Large

Representative loaded bodies are 400+ lines: execution 411, drawing-reader 424,
building-code 415, and formulas 488. A load of several domains can still be large.
One declared companion cycle remains between building-code and structural skills.
The router explicitly treats these as hints and guards cycles; the metadata
cycle is **not evidence of a runtime loop**.

**Next:** split task procedure from detailed reference data, keep examples loaded
on demand and measure which sections each task really needs. Resolve contradictory
loading hints rather than introducing another orchestrator. Track latency/tool
count/context volume before claiming efficiency improvements.

### F10 — P2: The User Needs Inspectable Details, Not Only Longer Documents

BTBA can organize detail records, but no generated annotated plan, editable wall
section or source-linked visual review surface has been demonstrated here. More
Markdown sections alone will not prove that an opening fits a wall or that a well
allows the intended sash movement and access.

**Next:** produce one visual evidence-backed vertical slice before designing a
general interface. Drawings must identify units/datums, source basis, scope and
draft status. A schematic must not masquerade as a measured construction drawing.

## Observed Probes and Validation

| Check | Observation on 2026-09-11 | Meaning / limit |
|---|---|---|
| Default source-contract suite | 60 passed, 0 failed; no project argument | Selected static text, link and metadata contracts hold |
| Existing beam numerical/CLI suite | 27 passed | Supported beam cases and input/error behavior; not whole-project design |
| Skill lint | 25 skills; 0 errors; 23 unreviewed-status warnings | Structural conventions only |
| Mixed-scale stub | First detected 1:100 returned as confirmed despite 1:5 detail | Scale detection is not calibration |
| Metre-unit DXF stub | Raw 10 reported in `value_mm` | Unit normalization absent in the exercised dimension path |
| Embedded extraction example | `IndentationError`, unexpected indent | Executable example needs repair/test |
| Duplicate YAML status | No parse error; later production value retained | Duplicate-key detection absent |

Probes used Python 3.12.10/PyYAML 6.0.3. Beam tests used the existing isolated
Python 3.12.10/Pint 0.25.3 environment. Synthetic stubs replaced input objects;
no real document, network-enabled OCR, package installation or outside code
execution was needed for these probes. Findings were not remediated in this
audit; passing baseline tests must not be presented as closing them.

## Brainstorming: Three Product Directions

| Direction | What it means | Trade-off |
|---|---|---|
| A. Better advisory skill pack | Source-clean the current material and improve document workflows | Lowest complexity; still weak on geometry, deterministic revision checks and visual inspection |
| **B. Evidence-backed detailing workbench — recommended** | Keep the current agent; add small local record/validation tools and reviewable wall/opening/well artifacts | Useful step toward construction plans without pretending to replace authoring software or engineers |
| C. Autonomous multi-agent BIM/engineering platform | Full authoring connectors, solvers, agent teams and project-system automation | High licensing, safety, versioning, evaluation and operational burden before the core evidence problem is solved |

Start with A's source corrections, then a narrow B increment. C is not a sensible
default next step. Add a specialist agent only where isolated context or restricted
tools measurably improve the task; do not add one merely for every trade title.

## Recommended Design for Direction B

### Seven Small Records, One Evidence Trail

These are proposed contracts, not implemented classes or a required database:

- `EvidenceRef`: source identity/content hash, page/view/bounding region, revision,
  date, units/datum, authority category, extraction method and inspected scope.
- `Claim`: field/value, evidence refs, observed/reported/proposed/derived state,
  uncertainty and conflicting alternatives. A source being available is not proof.
- `Element`: stable wall/opening/well ID, type, location and relationships;
  use IFC GUID or CAD handle only with source/revision context.
- `Detail`: layer/junction/product/geometry proposal and dependencies; no implied
  performance certification from an assembly label.
- `CheckResult`: rule/version, inputs, result, scope and not-assessed reason;
  arithmetic/geometry checks cannot set professional approval.
- `Issue`: affected records, missing decision/evidence, proposed resolver,
  response and actual closure evidence.
- `ChangeSet`: before/after records, impacted outputs, validation results,
  authorized purpose and applied-result record; preserve original source files.

Start with versioned JSON and a strict schema. Add SQLite/search/indexing only
when retrieval and concurrent editing justify it. Do not maintain a separate
unlinked truth store alongside project documents; generate summaries from the
same records and retain source links.

### The First Demonstration Should Be One Wall, One Opening and One Well

Use an original synthetic fixture or specifically authorized project evidence.
The demonstration should produce:

1. A scoped source sheet/section view with stable element IDs and evidence status.
2. One layer-by-layer wall type, applied to a located wall instance.
3. Window structural opening, frame and actual clear opening as separate fields.
4. A window-well plan/section showing finished datums, clear dimensions, sash
   envelope, obstructions and drainage/terrain interfaces; unresolved sizes remain
   unresolved instead of receiving plausible generic dimensions.
5. Detail quantity arithmetic with units, opening deductions and dependencies.
6. Review issues and construction holds linked to actual fields/details.
7. A second revision changing the window or terrain, with an explicit impact diff.

Start with deterministic, clearly labeled schematics or a controlled DXF output
if appropriate. Prefer native IFC semantics when supplied and verified rather
than flattening them into pixels. Do not require a commercial BIM license just
to use the basic evidence/detail register.

## Ordered Improvement Backlog

Effort bands are relative scope, not delivery commitments: **S** is a focused
change; **M** spans several modules/fixtures; **L** involves product integration
or substantial source review. Roles below are proposed, not assigned people.

| ID / order | Deliverable | Effort / proposed owner | Dependencies | Acceptance evidence |
|---|---|---|---|---|
| B01 / first | Source correction pass for room/energy/escape and envelope claims; triage electrical/legal content | M–L / maintainer plus relevant Norwegian technical reviewers | Authorized current source access | Corrected claims have exact scope/source; contradictory examples removed or clearly held; selected reviewer cases recorded |
| B02 / first | Drawing unit, scale, page/view and example-code repairs | M / tool developer | Existing extractors and synthetic fixtures | Metre/mm/inch fixtures, mixed scales, missing scale, unsupported format and multi-page behavior tested; no unjustified confirmed flag |
| B03 / first | Reproducible development/test setup and CI; duplicate-key tests | S–M / maintainer | Dependency/license decisions | Fresh environment reproduces suites; CI does not read private projects; invalid frontmatter rejected |
| B04 / next | Versioned evidence/element/detail schema and validator | M / tool developer with designer input | B01 criteria and B02 provenance contract | Missing units/source/IDs and conflicting status transitions rejected or explicitly unresolved; synthetic fixtures validated |
| B05 / next | One-wall/opening/well detail demonstration | M / agent maintainer plus designer/trade reviewer | B04; selected source/product evidence | All declared elements accounted for; every consequential field sourced or unknown; visual/record consistency reviewed |
| B06 / next | Revision and quantity dependency checks | M / tool developer | B04–B05 | Window/terrain change flags affected details, quantities and pricing; unchanged records retained; stale reuse detected |
| B07 / alongside next | Behavioral evaluation suite and local run receipts | M / evaluation maintainer | Fixed synthetic cases and output contracts | Observed tool/action/artifact outcomes, failures, latency and model/config versions recorded; no self-grading-only pass |
| B08 / later | Read-only IFC or CAD connector, then preview/apply writing | L / integration developer | B04–B07 plus tool/license/privacy review | Bounded tool access, save-as, reviewed payload, failure handling and round-trip fixtures; no unapproved external send |
| B09 / later | Scoped authoritative-source lookup/cache | M–L / data/tool developer | Source terms, taxonomy and query scope | Source/version/coverage recorded; inaccessible or unmapped does not become safe/compliant |

Clarify the root/skill licensing conflict before code reuse/distribution; it is
a maintainer decision, not something B03 may silently resolve.

## How to Know We Are Improving

Define metrics before implementing the next stage. Proposed evaluation measures:

- **Evidence coverage:** fraction of consequential output fields with correct
  applicable sources; count unsourced assumptions separately, never as verified.
- **Extraction quality:** element precision/recall against curated fixtures,
  dimensional error in declared units and explicit uncertainty/calibration status.
- **Uncertainty handling:** missing critical input produces a useful bounded draft
  or question, not fabricated dimensions, approvals or categorical conclusions.
- **Revision completeness:** expected dependent records correctly invalidated,
  unrelated records preserved and revised outputs traced to the new basis.
- **Action safety:** zero unapproved external actions and zero original-file
  overwrites in the defined adversarial/permission scenarios.
- **Task usefulness:** reviewers can locate each wall, understand the build-up and
  identify the next decision without reconstructing the entire conversation.
- **Efficiency:** measured time to a useful draft, tool calls, retries, context
  size/cost and repeated questions; no token-savings claim before measurement.

Include success, ambiguous drawing, missing product data, changed revision,
conflicting approval, wrong-unit, untrusted-document and cross-project-leakage
cases. Require no unsupported approval claims in the defined release benchmark;
that is a test gate, not a universal reliability guarantee. Report repeated runs
with model/host/tool versions and qualified-review coverage separately.

## What Not to Build Yet

- A 25-agent hierarchy mirroring the 25 skills.
- A trained “Norwegian construction model” before source quality and benchmarks.
- Automatic code-compliance or construction-ready status from an LLM verdict.
- A generic wall/well dimension catalogue divorced from product and site evidence.
- A whole-project graph database or always-on monitoring without a measured need.
- Multiple CAD/platform integrations before one detail-package workflow works.
- More safety banners in place of correcting incorrect technical guidance.

## Recommended Next Action

**Authorize a focused reliability increment: B01–B03, followed by the B04–B05
single-wall demonstration.** That delivers a stronger basis for construction
plans than another broad expansion of skills. Keep the [existing roadmap](construction-plans-roadmap.md)
as the phase overview and this backlog as the audit-informed execution proposal.

This audit created findings and research documents only. It did not change
technical rules, repair extractors, close project holds or certify designs.