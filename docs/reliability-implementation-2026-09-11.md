# Reliability Implementation — 2026-09-11

**Status:** Local implementation and tests; not a release, professional review or
claim that every audit item is closed.

**Scope:** Repository only. No private project records, outbound sends, commits
or published artifacts. Existing local beam-calculator work retained.

## Implemented

**Later local hardening:** see [the follow-up report](reliability-hardening-2026-09-11.md)
for precise source locators, hold/field revision changes, report isolation,
rectangle/rotated/cropped PDF support and evaluation-record validation. Counts below
preserve this first batch's run history rather than describing the latest suite.

| Audit concern | Implemented change | Remaining boundary |
|---|---|---|
| F01 regulatory defaults | Reworked building-code workflow; checked room/energy/escape/moisture/stormwater register; removed blanket amendment, permit and class defaults | Limited public-source review, not full law/standards/local-plan verification |
| F02 contradictory technical guidance | Reworked building physics and electrical skills; withdrew unsupported ratios, numerical tables, credentials and insurance claims; corrected relevant GC/application references | Actual SINTEF/product/NEK/FEL/FEK rules need authorized source and appropriate professional review |
| F03 extraction | Schema v2: selected PDF pages, retained sparse text, no implicit OCR, detected versus caller-calibrated scale, explicit view clip, supported linear DXF units, native DWG rejection and angular separation | Heuristic line candidates; no general wall recognition or complete quantity takeoff; optional OCR not exercised |
| F04 action boundary | Detail tool reads explicit packages inside selected root, no network/writes; geometry output refuses overwrite; LLM OCR requires explicit authorization option | Not a general host sandbox; caller authorization flags are not proof of permission; external integrations remain unverified |
| F05 tests | Added synthetic real PDF/DXF fixtures, detail/schema/revision cases and malformed YAML tests; retained beam/static suites | Host model behavior and technical reviewer evaluations are separate and not performed |
| F06 typed records | Strict JSON schema, source/element references, unit/status/datum checks, rectangular arithmetic and conservative revision impact | No authoritative truth store, complete BIM topology, product-fit or design engine |
| F07 repeatability | Shared Python 3.12 dependencies, developer guide, Windows/Ubuntu CI definition; removed ignored-config link prerequisites | Hosted CI has not run; transitive dependencies are not fully locked; licensing conflict remains unresolved |
| F08 YAML ambiguity | Safe loader rejects duplicate keys; malformed shapes/types tested | Host-specific schema/export compatibility is not certified |
| F09 loading | Removed structural/building-code companion cycle; shortened key technical skills and replaced duplicated code examples with tested utility references | Context/latency savings not measured; other domain bodies still need review |
| F10 useful artifacts | Original synthetic wall/opening/well JSON, arithmetic/revision tests and generated SVG schematic; rendered for visual inspection | No native CAD drawing, real project design or qualified designer acceptance |

## Shared Template Corrections

Reworked structural memo, compliance-gap analysis, construction sequence, heritage
assessment, post-approval checklist and pre-application notes. Removed preset
grades/loads/limits, invented municipal inspection/sign-off schedules, fixed cure
times, SEFRAK grades, approval predictions and generic costs/maintenance periods.
Each now identifies AI draft status, source/applicability, review and release scope.
Blank fields are not evidence of completion or permission to build.

## Local Detail Tool

[tools/detail_package.py](../tools/detail_package.py) implements a deliberately
small contract using [schemas/detail-package.schema.json](../schemas/detail-package.schema.json).
It checks source IDs, unique records, dependency cycles, units, level datums and
unknowns; it computes layer totals, rectangular opening fit/net face area and
well depth/projection arithmetic. Overlapping or out-of-wall openings are not
silently double-deducted. Source revisions and changed elements propagate a
conservative revalidation set, using both old and new dependency graphs.

Output retains source/input records and a hash. Optional SVG output depicts the
single-wall/opening/well geometry, rejects unknown/conflicting geometry and escapes
input text. A saved synthetic SVG is checked against the generator; a temporary
raster rendering was visually inspected for label layout and clipping.
`design_compliance` always remains
`not_assessed`, and release remains `not_authorized`. The tool cannot close a hold,
read source URLs, verify professional review or modify drawings. A consistent
rectangle is not a safe retaining wall, drain, escape path or window installation.

See [the synthetic demonstration](../examples/detail-package/README.md) and
[developer guide](development.md) for inputs, expected outputs and execution.

## Verification Record

Final selected suites passed **60 deterministic tests** and **79 static source
contracts**; skill lint reported **0 errors and 19 unreviewed-status warnings**.
Dependency compatibility and whitespace checks passed. Tests used the shared
Python 3.12 environment on Windows. Results are also recorded in
[IMPROVEMENTS.md](../IMPROVEMENTS.md). Skill lint exposed
an unquoted description colon during development; it was corrected, not suppressed.
Existing unreviewed-status warnings remain meaningful review needs.

The [live-host case specification](evaluations/README.md) covers twelve expected
behaviors. Those cases were **not run against a separate model/host** in this pass.
Tool tests involving untrusted text establish only the deterministic tool behavior,
not prompt-injection immunity of the agent. CI configuration is not evidence of a
hosted Windows/Linux run.

## Still Open — Do Not Label These Complete

1. **Maintainer licensing decision:** root MIT and skill Proprietary labels conflict.
   No license was silently changed. Third-party dependencies have separate terms.
2. **Qualified source review:** licensed standards/NA, current SINTEF details,
   manufacturer assemblies, electrical/trade clauses and remaining legacy domain
   examples. Current source corrections are bounded, not a full-library certification.
3. **Live agent evaluation:** execute the synthetic scenarios in target hosts,
   inspect actual tool actions/artifacts and measure latency/context/cost.
4. **Wider extraction evidence:** diverse real/public drawings, rotated views,
   dimensional annotation overrides, curves/blocks/layouts and verified wall topology.
5. **CAD/BIM authoring and visualization:** select a toolchain, licensing and limited
   read-only scope before preview/apply or export workflows. No connector is installed.
6. **Runtime permissions:** host-level sandboxing, network policy and write approval
   enforcement across all tools; the new local CLI only bounds its own inputs.
7. **Live geodata:** the Norwegian-building-data specification now removes guessed
   endpoints and map-to-safety shortcuts, but is not a working source service or
   evidence of site clearance.

The completed work is a reliability foundation and a tested small detail-record
workflow. “Top tier” requires demonstrating these remaining behaviors and technical
reviews, not replacing an honest limitations list with a readiness badge.