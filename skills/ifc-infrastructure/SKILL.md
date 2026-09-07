---
name: ifc-infrastructure
description: IFC4.3 infrastructure schema — roads/driveways, retaining walls, earthworks, geotechnical strata, alignments. Load for site civil works beyond building-only IFC2x3/IFC4.
license: Proprietary
triggers: [IFC4.3, IFC4x3, IfcAlignment, IfcRoad, IfcRoadPart, IfcKerb, IfcBorehole, IfcGeotechnicalStratum, IfcEarthworksCut, IfcEarthworksFill, IfcReinforcedSoil, IfcPavement, access road, driveway, retaining wall model, site civil works, stationing, linear referencing, infrastructure BIM, buildingSMART IFC4.3]
load_with: [bim-ifc]
safety_level: low
---

# Skill: IFC4.3 Infrastructure Schema

## Domain

The IFC4.3 (IFC4x3) extension of the IFC schema, published by buildingSMART
International, adds entities for **infrastructure** that IFC2x3/IFC4 (building-only)
do not cover: roads, railways, bridges, ports/waterways, and — most relevant to
BTBA — **geotechnical strata, boreholes, earthworks, and pavements**.

**Authoritative sources** (read live rather than relying on memory — the full
spec has 800+ entities/property sets, far more than belongs in this file):
- Rendered docs: https://ifc43-docs.standards.buildingsmart.org/
- Schema source (EXPRESS/XMI + markdown definitions): https://github.com/buildingSMART/IFC4.x-development (branch `ifc4.3-main`)
- To look up any entity precisely: `https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/<EntityName>.htm`

## When to Load This vs. `bim-ifc`

- `bim-ifc` — building elements (`IfcWall`, `IfcBeam`, `IfcSpace`), clash detection, BCF, Norwegian BIM mandates. Load for any building-only IFC file or BIM coordination question.
- `ifc-infrastructure` (this skill) — load **in addition to `bim-ifc`** when the project or model includes site civil works: an access road or driveway, a retaining wall or earthworks cut/fill, geotechnical borehole/stratum data modeled in IFC, or pavement/course build-up.

For a Norwegian residential project, this mostly comes up on the **situasjonsplan** (access road, driveway paving, retaining walls on sloped sites) and when a geotechnical consultant delivers borehole/stratum data as IFC rather than a PDF report — cross-reference with `geotechnical` for the engineering interpretation of that data.

**Norwegian delivery scope:** use the client-required schema and project-adapted
BIM requirements, including CRS/height datum and TFM mapping where required.
IFC4.3 support does not imply acceptance for a Statsbygg IFC4 delivery. Apply the
Norway-first requirement workflow in `bim-ifc`; do not impose Statsbygg rules on
private site works without an applicable agreement. Load `geotechnical` only
when interpreting ground conditions or foundation/excavation implications.

## What's New in IFC4.3

IFC4.3 adds a **domain layer** (industry-specific entities) and extends the
**shared element layer** (entities usable across domains). The domain layer for
IFC4.3 is (chapter 7 of the spec):

| Schema | Covers | Relevant to BTBA? |
|---|---|---|
| `IfcArchitectureDomain` | Building-specific finalization | Already covered by `bim-ifc` |
| `IfcBuildingControlsDomain` | BMS/controls | Rarely, residential scope |
| `IfcConstructionMgmtDomain` | Construction sequencing entities | See `construction-execution` |
| `IfcElectricalDomain` | Electrical systems | See `electrical-nek400` |
| `IfcHvacDomain` | HVAC systems | See `hvac-mechanical` |
| `IfcPlumbingFireProtectionDomain` | Plumbing/fire suppression | See `plumbing-vs6050` |
| `IfcPortsAndWaterwaysDomain` | Ports, waterways, marine structures | Out of scope for residential |
| `IfcRailDomain` | Rail track, signaling, catenary | Out of scope for residential |
| `IfcRoadDomain` | Roads, kerbs, junctions, road furniture | **Yes — driveways/access roads** |
| `IfcStructuralAnalysisDomain` | FEA model entities (loads, analysis models) | Cross-check `formulas-reference` |
| `IfcStructuralElementsDomain` | Structural member finalization | Already covered by `structural-engineering` |

The shared element layer adds `IfcSharedInfrastructureElements` (chapter 6.6),
which is the **most relevant schema for BTBA**:

> Scope: Geotechnical & terrain (boreholes, geo models, geo slices, strata),
> aggregate courses, earthworks structures (cuts, fills, soil reinforcement),
> pavements, signs, signals. *(Source: IfcSharedInfrastructureElements schema
> definition, IFC4x3.)*

## Key Entities (Confirmed from the IFC4.3 Spec)

### `IfcSharedInfrastructureElements` — geotechnical, earthworks, pavement

| Entity | Represents |
|---|---|
| `IfcBorehole` | A geotechnical borehole/investigation point |
| `IfcGeomodel` | A 3D geological/geotechnical model |
| `IfcGeoslice` | A 2D cross-section cut through a geo model |
| `IfcGeotechnicalStratum` | A soil/rock layer (stratum) with material and extent |
| `IfcGeotechnicalAssembly`, `IfcGeotechnicalElement` | Groupings/base type for geotechnical objects |
| `IfcEarthworksCut`, `IfcEarthworksFill`, `IfcEarthworksElement` | Cut/fill earthworks operations |
| `IfcReinforcedSoil` | Soil reinforcement (e.g., geogrid-reinforced retaining fill) |
| `IfcCourse` | An aggregate/pavement course layer |
| `IfcPavement` | A paved surface (driveway, parking, path) |
| `IfcSign`, `IfcSignal` | Road/rail signage and signals |

Relevant property sets: `Pset_BoreholeCommon`, `Pset_GeotechnicalStratumCommon`,
`Pset_Stationing`, `Pset_LinearReferencingMethod`.

**Cross-reference with `geotechnical`**: if a user provides `IfcBorehole` /
`IfcGeotechnicalStratum` data, extract stratum boundaries, soil type, and any
`Pset_GeotechnicalStratumCommon` values, then hand off to `geotechnical` for
bearing capacity / quick clay risk interpretation — this skill only reads the
IFC structure, it does not replace geotechnical engineering judgment.

### `IfcRoadDomain` — driveways, access roads, kerbs

Confirmed in-scope per the spec: controlled access highways, dual/single
carriageway, street, bicycle path, footpath; junction types (interchange,
intersection, roundabout, pedestrian/bicycle crossing); road structure, guard
elements, signage, paving, and utilities (lighting, drainage) within the road
body. Explicitly **out of scope**: railway crossings, tramways, urban planning.

| Entity | Represents |
|---|---|
| `IfcRoad` | The road/driveway as a spatial element |
| `IfcRoadPart` | A functional part of the road (carriageway, footpath, etc.) |
| `IfcKerb`, `IfcKerbType` | Kerb/curb elements |

### Alignment & Stationing

IFC4.3's core innovation for infrastructure is **alignment-based linear
referencing** — a spine curve (`IfcAlignment`, defined in the geometric
constraint resource schema, chapter 8) that other elements reference by
**station** (distance along the alignment) rather than only by Cartesian
coordinates. `Pset_Stationing` and `Pset_LinearReferencingMethod` carry this
data. This matters when a civil/road model references positions as "station
120+50" instead of x/y — don't assume Cartesian-only coordinates when reading
an infrastructure-adjacent IFC file.

## Reading an IFC4.3 File with Infrastructure Content

1. Check the schema version (`FILE_SCHEMA` in the STEP header, or
   `IfcProject` in a JSON/XML export) — confirm it's `IFC4X3_ADD2` (or a `RC`/`ADD1`
   predecessor), not IFC2x3/IFC4, before expecting these entities to exist.
2. Identify which domain entities are present (`IfcRoad`, `IfcBorehole`,
   `IfcEarthworksCut`, etc.) using the same `ifcopenshell.open(...).by_type(...)`
   approach documented in `bim-ifc`.
3. For geotechnical entities, extract stratum/borehole data and hand off to
   `geotechnical` for engineering interpretation.
4. For road/pavement entities, check they connect correctly to the building's
   `IfcSite` and match the situasjonsplan's stated access/driveway geometry.
5. If precise attribute definitions are needed for an entity not covered
   above, fetch `https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/<EntityName>.htm`
   directly rather than guessing — the spec is versioned and authoritative.

**Escalation**: As with `bim-ifc`, IFC infrastructure data does not replace a
licensed geotechnical or civil engineer's sign-off. Bob can read and structure
the data; professional responsibility (ansvarlig prosjekterende) still applies
for permit-required site works.

Full domain/shared/resource schema index with links:
[references/ifc4x3-schema-map.md](references/ifc4x3-schema-map.md)
