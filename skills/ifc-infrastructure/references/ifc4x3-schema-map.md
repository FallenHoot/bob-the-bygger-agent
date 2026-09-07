# IFC4.3 Schema Navigation Index

**Part of the `ifc-infrastructure` skill.** Full chapter index of the IFC4.3
(IFC4x3 Add2) specification, with links to the live rendered docs. Use this to
jump directly to a schema instead of searching — then fetch the linked page
for exact entity attributes, property sets, and examples rather than relying
on memory.

Source: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/toc.html
Schema source (EXPRESS/XMI + markdown): https://github.com/buildingSMART/IFC4.x-development (branch `ifc4.3-main`)

## Chapter 5 — Core Data Schemas

Kernel entities (`IfcRoot`, `IfcObject`, `IfcProduct`, `IfcSpatialElement`, etc.)
— unchanged in spirit from IFC2x3/IFC4. See `bim-ifc` for the practical subset
BTBA already uses (`IfcProject`, `IfcSite`, `IfcBuilding`, `IfcBuildingStorey`).

## Chapter 6 — Shared Element Data Schemas

| # | Schema | Covers |
|---|---|---|
| 6.1 | `IfcSharedBldgElements` | Walls, beams, columns, slabs, doors, windows — building elements shared across domains |
| 6.2 | `IfcSharedBldgServiceElements` | MEP: ducts, pipes, cable carriers |
| 6.3 | `IfcSharedComponentElements` | Fasteners, discrete accessories, mechanical fasteners |
| 6.4 | `IfcSharedFacilitiesElements` | Furniture, equipment for facility management |
| 6.5 | `IfcSharedMgmtElements` | Work plans, work schedules, control |
| **6.6** | **`IfcSharedInfrastructureElements`** | **Geotechnical (boreholes, strata), earthworks, pavements, signs/signals — see SKILL.md for entity table** |

Full page: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/chapter-6/

## Chapter 7 — Domain Specific Data Schemas

| # | Schema | Covers | BTBA relevance |
|---|---|---|---|
| 7.1 | `IfcArchitectureDomain` | Building-specific finalization | Covered by `bim-ifc` |
| 7.2 | `IfcBuildingControlsDomain` | BMS/controls | Low |
| 7.3 | `IfcConstructionMgmtDomain` | Construction sequencing | See `construction-execution` |
| 7.4 | `IfcElectricalDomain` | Electrical systems | See `electrical-nek400` |
| 7.5 | `IfcHvacDomain` | HVAC | See `hvac-mechanical` |
| 7.6 | `IfcPlumbingFireProtectionDomain` | Plumbing/fire suppression | See `plumbing-vs6050` |
| 7.7 | `IfcPortsAndWaterwaysDomain` | Ports, waterways, marine | Out of scope |
| 7.8 | `IfcRailDomain` | Rail track, signaling, catenary, telecom | Out of scope |
| **7.9** | **`IfcRoadDomain`** | **Roads, kerbs, junctions, road furniture** | **Driveways/access roads** |
| 7.10 | `IfcStructuralAnalysisDomain` | FEA model entities (loads, analysis models) | Cross-check `formulas-reference` |
| 7.11 | `IfcStructuralElementsDomain` | Structural member finalization | Covered by `structural-engineering` |

Full page: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/chapter-7/

## Chapter 8 — Resource Definition Data Schemas

Supporting data structures with no independent identity (referenced by entities
above, not standalone). `IfcAlignment` and the linear-referencing geometry that
makes IFC4.3 infrastructure work lives in `IfcGeometricConstraintResource`.

| # | Schema |
|---|---|
| 8.1 | `IfcActorResource` |
| 8.2 | `IfcApprovalResource` |
| 8.3 | `IfcConstraintResource` |
| 8.4 | `IfcCostResource` |
| 8.5 | `IfcDateTimeResource` |
| 8.6 | `IfcExternalReferenceResource` |
| **8.7** | **`IfcGeometricConstraintResource`** (includes `IfcAlignment`) |
| 8.8 | `IfcGeometricModelResource` |
| 8.9 | `IfcGeometryResource` |
| 8.10 | `IfcMaterialResource` |
| 8.11 | `IfcMeasureResource` |
| 8.12–8.14 | Presentation resources (appearance, definition, organization) |
| 8.15 | `IfcProfileResource` |
| 8.16 | `IfcPropertyResource` |
| 8.17 | `IfcQuantityResource` |
| 8.18 | `IfcRepresentationResource` |
| 8.19 | `IfcStructuralLoadResource` |
| 8.20 | `IfcTopologyResource` |
| 8.21 | `IfcUtilityResource` |

Full page: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/chapter-8/

## Looking Up a Specific Entity

Every entity, type, property set, and quantity set has its own page:

```
https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/<Name>.htm
```

Examples: `IfcBorehole.htm`, `IfcGeotechnicalStratum.htm`, `Pset_Stationing.htm`.
Fetch the page directly for the authoritative attribute list, inheritance, and
examples — do not guess attribute names from memory, they're versioned and the
spec is still under active development (`IFC4X3_ADD2`, in progress as of this
writing).

## Annexes (for deeper/edge-case lookups)

| Annex | Content |
|---|---|
| A | Computer-interpretable listings (EXPRESS/XSD schema files) |
| B | Alphabetical listing of every entity/type |
| C | Inheritance listings (class hierarchy) |
| D | Diagrams |
| E | Worked examples |
| F | Change logs between IFC4.3 sub-releases |

Full index: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/toc.html

*Last reviewed: 2026-09-06.*
