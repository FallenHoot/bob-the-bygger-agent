---
name: sintef-byggforsk
description: Review Norwegian wall/roof/below-grade assemblies for moisture, insulation, airtightness, vapour control, drying, frost and junction continuity using scoped design/product evidence.
triggers: [moisture, fukt, vapour, insulation, airtightness, thermal bridge, condensation, wall assembly, veggoppbygging, roof assembly, drainage, frost, sd-value, dampsperre, vindsperre, lysgrav]
load_with: []
safety_level: high
status: draft
license: Proprietary
---

# Skill: Building Physics and SINTEF Detail Review

## Purpose

Develop and review source-linked construction assemblies and interfaces, not a
catalogue of supposedly compliant wall thicknesses. Use actual SINTEF guidance,
product documentation and design calculations when available. SINTEF guidance is
not law, and this skill is not an authorized copy of Byggforskserien.

## Trust Boundary

BTBA may organize layer schedules, identify continuity conflicts, explain moisture
mechanisms and draft alternatives. Existing hidden layers and numerical performance
remain unverified without evidence. A generic wall build-up, product name, photograph
or U-value alone cannot establish moisture safety, fire/acoustic performance or
construction release. Consequential choices need the appropriate building-physics,
structural or trade designer's review for the actual conditions.

The earlier contradictory cold/warm resistance ratio, Sd classifications,
regional frost depths, default wall thicknesses, thermal-bridge corrections and
universal material moisture thresholds are withdrawn. Do not reuse them from old
AI notes or adjacent templates. No guessed replacement rule is supplied.

## Inputs and Scope

- Selected wall/roof/floor/well IDs, location, exposure, use and intended decision.
- Relevant plan/section/detail revision; existing versus proposed dimensions.
- Known existing layers and condition, with observations separated from assumptions.
- Indoor/outdoor moisture/temperature exposure, terrain/groundwater, precipitation,
  occupancy and ventilation evidence as relevant.
- Exact products and versions: thermal properties, vapour resistance, compatibility,
  installation/fixing/joint instructions and tested assembly evidence.
- Applicable regulations, contract criteria and design methodology; unavailable
  sources remain unverified. No project selection means bounded general guidance.

## Assembly Review Procedure

1. Establish source identity, date/revision, evidence status, units and layer direction.
   Match relevant details to each instance; two walls of one type can have different
   exposure, supports, openings or junction requirements.
2. Inventory all layers, thicknesses and functions. Distinguish structural layer,
   insulation, air/vapour/water control, ventilation/drainage cavity and finish.
   Unknown layers are not zero thickness or an assumed modern construction.
3. Trace the water and air paths through bases, corners, openings, floors, roofs and
   penetrations. A continuous line on a diagram is not evidence of installed quality.
4. Establish drying paths and moisture sources: rain/snow, ground water/capillarity,
   construction moisture and indoor vapour. Below-grade assemblies and high-humidity
   uses cannot inherit above-grade timber-wall details without assessment.
5. Compare sourced thermal and moisture calculations/product limits with the
   applicable performance basis. Never infer U-value, fire resistance, acoustic
   performance or dew-point safety merely from total thickness or material labels.
6. Record incompatible products, unresolved interfaces and evidence required before
   covering. Ask only for inputs that change the current conclusion.
7. Return a draft detail or comparison with source-linked layers/junctions, open
   holds, review owner and next step. Use [construction-detail packages](../construction-execution/SKILL.md#construction-detail-packages)
   when the user requests a coordinated deliverable.

## Vapour, Air and Drying

Use [the checked §13-13 source summary](../building-code-tek17/references/verified-requirements.md#moisture)
for the limited distinction between regulation and preaccepted guidance. The
inspected guidance normally locates the air/vapour-tight layer on the warm side
and provides an outward drying route. It is not permission to add polyethylene
to every old or below-ground wall.

For the actual assembly, determine:
- vapour resistance of each layer and joints from exact product data;
- air-barrier continuity through service penetrations and transitions;
- whether internal insulation cools existing moisture-sensitive materials;
- whether an impermeable layer traps construction or ground moisture;
- whether a proposed service cavity/insulation distribution needs hygrothermal review;
- installation moisture limits and measurement methods from the actual products/design.

No universal cold-side insulation fraction, polyethylene thickness, drying time or
moisture percentage is an automatic pass. A steady-state illustrative calculation
is not a substitute for a suitable moisture analysis where transient effects matter.

## Insulation and Thermal Bridges

Record declared/design conductivity and applicability, thickness, framing fraction,
fixings, cavities, continuity and moisture/compression effects. Use the appropriate
calculation method; a sum of layer resistances alone may omit framing and junctions.
Keep area U-values, linear Ψ-values and normalized thermal-bridge contributions
in their correct units and scopes. Do not add generic correction factors twice.

Compare with the [actual energy pathway](../building-code-tek17/references/verified-requirements.md#energy),
not a supposed universal wall thickness. A product's fire reaction classification
is distinct from the wall's fire resistance and tested assembly configuration.

## Junction Checks

| Interface | Evidence and checks |
|---|---|
| Wall base/foundation | Capillary separation, support/fixing, insulation continuity, splash/terrain exposure and waterproofing termination |
| Window head/jamb/sill | Structural opening versus frame/clear opening, support, installation joint, flashings/drip paths, air seal and reveal insulation |
| Roof/wall and floor/wall | Structural movement, air/vapour transitions, ventilation routes, thermal bridges and fire separation |
| Old/new | Existing materials/condition, movement, compatibility and accessible joining method; no assumed hidden membrane |
| Services | Actual opening, sleeve/seal/fire-stop system, access and responsibility; no unreviewed cutting of structure |
| Below grade/window well | Groundwater and water pressure, waterproofing continuity, drainage outlet/invert/backwater, frost and retaining/foundation interaction |

## Ground Moisture, Drainage and Frost

[DiBK §13-10](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17/13/vi/13-10)
and the applicable design/product sources must be reviewed for below-grade work.
The page is a source starting point; no full below-grade rule pack is verified here.

Establish soil grading/permeability, groundwater, frost susceptibility, local climate,
loads, terrain and outlet evidence. Distinguish water shedding, drainage and waterproofing
against hydrostatic pressure; a drainage board is not automatically all three.
Do not prescribe a pipe diameter/fall, aggregate depth, regional frost depth or
infiltration solution from a generic table. Do not assume excavation can expose
or undermine a footing safely; route structural/ground review where implicated.

## Execution and Hold Points

Use project/product criteria for weather protection, substrate preparation,
moisture/strength checks, joint inspection and tests before concealment. Record
method, result, date, reviewer and release evidence. Elapsed time or visual appearance
alone does not release backfill, floor covering or structural loading.

On changed assembly/product/terrain evidence, use [project-lifecycle](../project-lifecycle/SKILL.md)
to flag affected details, quantities and procurement pending revalidation. Preserve
history and the intended scope; do not silently replace reviewed or issued details.

## Synthetic Cases and Review Status

- A fictional wall has an unknown existing lining: produce alternatives and an
  investigation question, not a verified complete layer stack.
- A proposed window moves outward: review support, flashing, air seal, thermal
  bridge and well projection; do not preserve the old junction by assumption.
- A well has no evidenced outlet: mark drainage unresolved; no default soakaway.

These are expected behaviors, not executed model evaluations. Reviewed 2026-09-11:
workflow and withdrawal of unsupported defaults; limited public §13-13 comparison
only. Authorized SINTEF detail editions, manufacturer assemblies and project
hygrothermal analyses remain unverified until supplied and assessed.
