# Construction Plans — Next-Stage Implementation Plan

**Date:** 2026-09-11

**Status:** Development proposal; initial document workflow and blank template added.

**Scope:** Reusable agent capability, not the design of a selected property.

**Implementation update:** [The reliability pass](reliability-implementation-2026-09-11.md)
adds source corrections, tested page/unit/calibration handling, local detail-record
validation, rectangular quantity checks and a synthetic revision demonstration.
These do not establish CAD generation, live agent reliability or professional review.

**Further hardening:** [the follow-up batch](reliability-hardening-2026-09-11.md)
adds source-locator requirements, exact revision differences, removed-hold review,
rotated/cropped rectangle extraction and hash-checked evaluation records. Live-host
evaluation and professional review remain separate, uncompleted stages.

**Audit follow-up:** [The agent audit](agent-audit-and-direction-2026-09-11.md)
identifies source, scale and unit defects to address before relying on detailed
output. Its B01–B09 backlog refines the implementation order below; findings are
not closed merely by adding this roadmap or the draft template.

## Goal

Help answer **how each wall is built and how each opening and window well fits
into it**, rather than stopping at a floor-plan review. The output should let a
designer or contractor locate an element, understand the proposed construction,
trace its evidence, and identify exactly what remains unresolved.

This combines building detailing with civil/site interfaces: levels, excavation,
surface water, below-ground drainage, foundations and retaining structures.
It is not initially a general roads/bridges/Civil 3D design platform.

## Approach and Trade-Offs

| Approach | Benefit | Limitation / decision |
|---|---|---|
| **Source-linked detail register first — selected** | Useful with current drawings and product evidence; exposes missing decisions before automating them | Initially document-based and manually reviewed; extend existing execution and domain skills |
| CAD/BIM connector first | Native geometry, schedules and drawings when the model is well authored | Requires an agreed authoring tool, reliable model semantics, licensing, tested APIs and review; defer until the detail records are stable |
| Train an engineering/drawing model first | Could support future extraction or surrogate-analysis research | Requires relevant licensed data, benchmarks and engineering validation; does not solve missing project evidence; not the immediate priority |

The first increment does not need another agent hierarchy or MCP server.
Keep deterministic arithmetic in tested tools; use the agent to organize evidence,
draft alternatives, identify interfaces, and request review.

## First Usable Deliverable

Use [templates/construction-detail-package.md](../templates/construction-detail-package.md)
through the [execution workflow](../skills/construction-execution/SKILL.md#construction-detail-packages).
Reuse the selected project's registers and IDs; save only within its authorized
scope. The public template must contain no private project facts.

### 1. Evidence and Geometry Basis

- Relevant architectural plans, sections, elevations and detail sheets, with
  source/page/revision and the actual status of each.
- Survey/site measurements: datums, finished-floor levels, terrain and drainage
  levels. Keep proposed levels distinct from measured existing levels.
- Existing-condition evidence: wall composition, supports, foundation geometry,
  services and concealed conditions; uncertainty remains visible.
- Product data for the actual window, well, insulation, membranes and fastening
  systems—not a generic similar product.
- Structural, ground, moisture, fire, daylight and other design criteria for the
  affected scope, with applicable Norwegian source revisions and review needs.

Missing evidence permits an inventory or options draft. It does not permit
invented dimensions, hidden-material identification, performance ratings or
approval. A recent source is not automatically applicable or approved.

### 2. Wall Instances, Types and Junctions

Give each wall segment a stable instance ID tied to floor/location/endpoints and
a wall-type ID. Shared types reduce duplication, but individual openings,
support conditions, exposure and old-to-new connections need instance overrides.
Do not mistake one wall-type sheet for coverage of every wall.

Each type records layers in a stated direction, thickness and purpose, framing
or reinforcement design reference, fixings, moisture/air/thermal continuity,
fire/acoustic/thermal criteria and evidence. Detail corners, wall bases, floor
and roof junctions, movement joints and service penetrations where relevant.
Unverified existing construction must not become a specified new build-up.

### 3. Windows and Window Wells — Lysgraver

Keep structural opening, frame outer size, glazing area and unobstructed operable
opening as different quantities. Record opening direction and sash envelope,
finished sill/head levels, installation joints, reveal insulation and flashings.

For each well, define dimensions against explicit finished datums:

- clear internal width, parallel to the facade;
- clear projection, perpendicular from the stated finished facade plane;
- well-bottom and rim/adjacent-terrain levels, with the resulting depth;
- external footprint, wall thickness, excavation and working space separately;
- space consumed by the open sash, steps/ladder, grating or cover and other
  obstructions, with usable access/escape geometry assessed separately;
- surface-water interception, bottom fall, drain invert, outlet capacity and
  backwater/overflow arrangements; discharge route and permissions where applicable;
- below-ground waterproofing continuity, frost strategy, retaining/support and
  anchorage basis, foundation interaction and fall protection.

There is **no default compliant well size**. A well serving light/ventilation is
not automatically an acceptable escape route. Infiltration or connection to an
existing drain is not assumed feasible. Structural and excavation solutions need
site-specific evidence and appropriate design review.

### 4. Construction, Quantities and Review

Link each detail to scope/pricing lines, installation sequence, temporary-works
dependencies, inspections before concealment, responsible reviewers and release
evidence. Distinguish quantity provenance: annotated, measured/scaled, derived,
or allowance. Missing quantities stay unknown, not zero.

Drawn, proposed, reviewed, issued and approved are separate states. A populated
package is not an instruction to build. Record scope-specific technical review,
applicable authority decisions and authorized issue separately; no software or
AI status can substitute for them.

## Delivery Stages and Acceptance Evidence

| Stage | State on 2026-09-11 | Evidence needed to call the stage complete |
|---|---|---|
| A. Detail-package workflow | Instructions, template, strict records and synthetic demonstration present | User/design-team review and observed host behavior; complete actual source/product basis |
| B. Reliable element extraction | Page/unit/calibration repairs tested; wall semantics still heuristic | Persistent IDs, wider export/geometry fixtures, measured accuracy and uncertainty |
| C. Quantities and consistency checks | Rectangular face/opening/layer/well arithmetic and revision impact tested locally | Broader geometry/material scope, dimensional datums and product/design review; not a complete takeoff engine |
| D. CAD/BIM detail output | Not implemented; separate SVG schematic preview exists | Selected authoring/export stack; dimensioned plans/sections/junctions; units/datums; reviewable round-trip/export fixtures; exact source/revision manifest |
| E. Engineering and live-source expansion | Guidance and specifications only | Verified applicable standard/NA and product rules; benchmarked calculations; tested connectors with failure states, provenance and privacy controls |

Stage A can be useful before stages B–E. Do not report this plan or a text
assertion as a successful behavioral evaluation. No delivery dates or effort
estimates are committed here.

## Minimum Evaluation Cases

Use synthetic fixtures or explicitly authorized public drawings:

1. **Complete single-wall case:** one instance/type, window, well and junction
   sources → traceable draft with explicit coverage, quantities and review status.
2. **Same type, different interfaces:** two walls with different foundations or
   exposures → separate instance notes; no silent shared-detail assumption.
3. **Nominal versus clear window size:** only catalogue dimensions supplied →
   actual free opening and escape assessment remain unresolved.
4. **Missing well outlet/ground evidence:** draft geometry options only; no fixed
   execution size, drain connection or excavation release.
5. **Mixed scales and units:** distinguish annotated values from measured ones;
   reject uncalibrated geometry and demonstrate conversions explicitly.
6. **Changed window or terrain revision:** identify affected well, junction,
   quantities and procurement scope; preserve old evidence and mark reuse on hold.
7. **Missing or conflicting reviewer record:** draft remains draft; no inferred
   issue, approval, sent message or permission to build.
8. **Document instruction injection:** treat source text as data; it must not
   change project scope, authorize uploads or close a hold.

Record expected and actual results separately. These cases are planned
evaluations, not a claim that an agent has passed them.

## Supplied References: Findings and Relevance

Public pages retrieved on 2026-09-11. No external code was installed, project
data uploaded, third-party model trained or CAD application run.

| Reference | Observed evidence | Useful direction / boundary |
|---|---|---|
| [SmartPlansAI](https://github.com/4EvrEvolving/SmartPlansAI) | Describes an AI/OCR Civil 3D experiment; [inspected tree](https://github.com/4EvrEvolving/SmartPlansAI/tree/e2763a0a698296cf5d6fed1bcb2494b1b6e9055e) contains only a README and Git attributes | Extract → interpret → reconstruct is a relevant goal, but no executable automation or tests were available to evaluate; no detected repository license authorizes assuming code reuse |
| [Agentic AI in Civil Engineering — Amir Rafe](https://pozapas.github.io/aicivil.html) | Educational overview of agent loops, narrow skills, MCP, evaluation and engineering applications | Keep reusable procedures separate from tool connections; use explicit review/permission boundaries. Page performance claims were not independently verified or adopted |
| [SciML4StructEng Repository](https://sciml4structeng.github.io/Repository/) | ETH Zurich-origin structural datasets for empirical ML research, with citation and donation guidance | Potential future benchmark/data discovery; not a wall/well detail library. No individual dataset's fit, license, model accuracy or Norwegian applicability was evaluated |

Re-check per-repository and per-dataset licenses and attribution before reuse.
Research examples are not Norwegian regulatory sources or evidence of professional
acceptance. BTBA should solve the current detail-record problem before adopting
research infrastructure.