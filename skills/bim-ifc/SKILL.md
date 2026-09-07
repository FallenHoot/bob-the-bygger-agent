---
name: bim-ifc
description: Norway-first BIM/IFC review, Statsbygg SIMBA, TFM, Archicad IFC translators, property mapping, IDS validation and BCF. Load for BIM models or Norwegian model-delivery requirements.
license: Proprietary
triggers: [IFC, BIM, ifc file, ifcopenshell, Revit, ArchiCAD, Bonsai, buildingSMART, IDS, clash detection, BCF, model coordination, BREEAM, Statsbygg, SIMBA, TFM, tverrfaglig merkesystem, IFC-oversetter, IFC translator, Nordic BIM, property mapping, egenskapskobling, BIM-manual, fagmodellansvarlig, openBIM, Navisworks, model check, IFC export, IFC import, digital twin, COBie, model federation, LOD, level of development, eByggesøknad, digital byggesøknad]
load_with: []
safety_level: low
---

# Skill: BIM / IFC

## Domain
Building Information Modelling (BIM) concepts, the IFC (Industry Foundation Classes) open standard, the IfcOpenShell toolchain, buildingSMART IDS (Information Delivery Specification), clash detection, BCF issue tracking, and Norwegian BIM policy requirements.

**Load proportionately:** for a SIMBA/TFM/export-settings question, use this skill
alone. Add `architectural-drawing-reading` when interpreting model geometry or
drawings; add `ifc-infrastructure` only for infrastructure content. Load
`building-code-tek17` for regulatory questions, not for every export task.

## Trust Boundary

Bob may inspect IFC data, compare it with supplied delivery requirements, and
report evidence-backed deviations. A missing value is unknown, not a passing
check. An export preset, valid IFC schema, or passing IDS report does not certify
engineering safety, TEK17 compliance, or contractual acceptance. The
fagmodellansvarlig owns the discipline export setup; BIM-koordinator coordinates
checks, and the client/responsible professionals retain their approval duties.

---

## What BIM Is (and Is Not)

**BIM** is not a single tool — it is a process for creating and managing information about a building across its entire lifecycle. A BIM model contains:
- **Geometry**: 3D representations of structural elements, walls, openings, MEP runs
- **Properties**: Material data, fire ratings, U-values, load-bearing status, manufacturer info
- **Relationships**: Which slab sits on which beam; which door belongs to which wall

A 2D PDF drawing is NOT BIM. A Revit or ArchiCAD model IS BIM (if it has properly authored element data). An IFC file is BIM exchanged in an open format.

**The practical distinction for BTBA:**
- When a user shares a PDF plan → use `architectural-drawing-reading`
- When a user shares an IFC file or mentions BIM coordination → use `bim-ifc`
- When questions involve Norwegian BIM mandates, IDS validation, or clash detection → use `bim-ifc`

---

## IFC — Industry Foundation Classes

**IFC** is an open, neutral file format maintained by buildingSMART International. It is the lingua franca of open BIM.

### Versions in Use (2026)
| Version | Status | Notes |
|---|---|---|
| **IFC2x3 TC1** | Widely deployed | Legacy; supported by virtually all tools; most existing models |
| **IFC4 Add2 TC1** | Current stable | Preferred for new projects; better geometry types, improved MEP |
| **IFC4x3 Add2** | Emerging | Adds infrastructure (roads, geotechnical strata, earthworks, alignments) — see `ifc-infrastructure` skill for these entities; not yet mainstream for building-only models |

Select the schema and exchange view required by the agreed delivery specification
and supported by the receiving tools, not simply the newest available version.

**Key IFC entity types:**
| Entity | What it represents |
|---|---|
| `IfcWall` | Wall element (can be load-bearing or not) |
| `IfcBeam` | Horizontal structural member |
| `IfcColumn` | Vertical structural member |
| `IfcSlab` | Floor or roof slab |
| `IfcDoor`, `IfcWindow` | Opening elements with operation type |
| `IfcSpace` | Room/zone with area and name |
| `IfcBuildingStorey` | Floor/level |
| `IfcBuilding` | The whole building |
| `IfcProject` | Top-level container (coordinate system, units) |
| `IfcPropertySet` | Attached property data (e.g., fire rating, U-value) |
| `IfcMaterial` | Material assignment |

### Reading an IFC File

When a user provides an IFC file or data extracted from one:

1. **Check units first** — IFC models can be in meters, millimeters, or feet. `IfcProject.UnitsInContext` defines the project unit. Norwegian projects should be millimeters or meters.
2. **Identify the coordinate system** — check placements, the declared horizontal CRS and vertical datum, units, and the local-to-map transformation (for IFC4, inspect `IfcProjectedCRS` / `IfcMapConversion` where supplied). `IfcSite.RefLatitude`, `RefLongitude`, and `RefElevation` alone do not verify the full transformation. Check against the project's survey basis; do not assume UTM zone 33 for all Norway.
3. **Check spatial hierarchy** — valid hierarchy is: `IfcProject` → `IfcSite` → `IfcBuilding` → `IfcBuildingStorey` → elements. Models missing a storey level are poorly authored.
4. **Check structural elements** — look for `LoadBearing = True` on `IfcWall` instances. In poorly authored models, this property may be missing.
5. **Check property sets and classifications** — `Pset_WallCommon` and `Pset_BeamCommon` are international IFC sets, not uniquely Norwegian requirements. Compare required values, classification references, and TFM mapping against the agreed project requirement set. NS 3451 classification alone does not prescribe a universal IFC Pset or prove TFM completeness.

### Common IFC Export Problems
| Problem | Symptom | Cause |
|---|---|---|
| Missing storeys | All elements at level 0 | Elements not assigned to IfcBuildingStorey |
| Wrong units | Geometry 1000× too large or small | Millimeter model opened as meter model |
| Missing properties | No load-bearing data | Author didn't fill Psets |
| Geometry errors | Invisible walls, clipping issues | Invalid geometry kernels; use IFC4 geometry |
| Duplicate GUIDs | Model merge problems | GUIDs regenerated during export |

---

## IfcOpenShell — Open Source IFC Toolchain

[IfcOpenShell](https://ifcopenshell.org/) is the primary open-source library for working with IFC files. It provides Python bindings and a family of CLI tools.

### Key Tools

| Tool | Purpose | Use Case |
|---|---|---|
| **ifcopenshell-python** | Python API for reading/writing IFC | Scripted model interrogation, property extraction |
| **ifcconvert** | CLI converter: IFC → OBJ, DAE, SVG, PDF, GLB, IFC | Visualization, format conversion |
| **ifcclash** | Clash detection between IFC models | Identify MEP/structural conflicts |
| **ifctester** | IDS model validation (checks if model meets IDS requirements) | Quality control before delivery |
| **ifcdiff** | Compare two IFC models to find changes | Revision management |
| **ifcfm** | Extract FM handover data from IFC | Facility management deliverables |
| **ifcmcp** | MCP server for AI-based IFC querying | AI agents querying/editing IFC models |
| **ifcpatch** | Run pre-packaged IFC repair scripts | Fix common IFC export problems |
| **ifccsv** | Export IFC schedules to CSV/Excel | Quantity takeoffs, material lists |
| **Bonsai (Blender add-on)** | Full IFC authoring in Blender | Free alternative to Revit/ArchiCAD |

### Python Quick Reference (ifcopenshell)

```python
import ifcopenshell

# Open a file
model = ifcopenshell.open("building.ifc")

# Get all walls
walls = model.by_type("IfcWall")

# Get load-bearing walls
load_bearing = [w for w in walls 
                if ifcopenshell.util.element.get_pset(w, "Pset_WallCommon", "LoadBearing")]

# Get all spaces with their areas
spaces = model.by_type("IfcSpace")
for space in spaces:
    area = ifcopenshell.util.element.get_pset(space, "Qto_SpaceBaseQuantities", "NetFloorArea")
    print(f"{space.LongName}: {area} m²")

# Get material for an element
element = model.by_type("IfcBeam")[0]
material = ifcopenshell.util.element.get_material(element)
```

---

## buildingSMART IDS — Information Delivery Specification

**IDS** (Information Delivery Specification) is a buildingSMART standard for defining *machine-readable information requirements* that an IFC model must satisfy. Verify the version required by the project and supported by the validator.

### What IDS Solves

Without IDS, a contractor receives an IFC model and manually checks whether it contains the required information. With IDS, the checking is automated using tools like `ifctester`.

### IDS File Structure (XML)

An IDS file defines **specifications** — each specification contains:
- **Applicability**: Which IFC elements this rule applies to (by entity type, classification, property)
- **Requirements**: What information those elements must have (e.g., properties, materials, classifications). Geometry/clash checks and professional design review are separate; an IDS pass is not a complete model acceptance.

```xml
<ids:specification name="All load-bearing walls must have fire rating" 
                   minOccurs="1" maxOccurs="unbounded">
  <ids:applicability>
    <ids:entity>
      <ids:name><ids:simpleValue>IFCWALL</ids:simpleValue></ids:name>
    </ids:entity>
    <ids:property dataType="IfcBoolean" minOccurs="1">
      <ids:propertySet><ids:simpleValue>Pset_WallCommon</ids:simpleValue></ids:propertySet>
      <ids:baseName><ids:simpleValue>LoadBearing</ids:simpleValue></ids:baseName>
      <ids:value><ids:simpleValue>TRUE</ids:simpleValue></ids:value>
    </ids:property>
  </ids:applicability>
  <ids:requirements>
    <ids:property dataType="IfcLabel" minOccurs="1">
      <ids:propertySet><ids:simpleValue>Pset_WallCommon</ids:simpleValue></ids:propertySet>
      <ids:baseName><ids:simpleValue>FireRating</ids:simpleValue></ids:baseName>
    </ids:property>
  </ids:requirements>
</ids:specification>
```

### Validating with ifctester

```bash
ifctester your-model.ifc your-requirements.ids --report report.html
```

Output: Pass/fail per specification with element-level detail.

---

## BCF — BIM Collaboration Format

**BCF** (BIM Collaboration Format) is a buildingSMART standard for communicating issues found in a BIM model. It is tool-agnostic — issues created in Navisworks can be opened in Revit, BIMcollab, or IfcOpenShell.

### BCF Contains Per Issue
- **Title and description** of the problem
- **Viewpoint** (camera position pointing at the problem)
- **Snapshot** (screenshot of the viewpoint)
- **Status** (Open, In Progress, Closed, ReOpened)
- **Assigned to** / **Due date**
- **Related IFC elements** (GUIDs of elements involved)

### BCF Workflow for Norwegian Projects
1. Coordinator federates all discipline models (architectural, structural, MEP) in model-checking software
2. Clash detection run → issues created as BCF
3. BCF file shared with discipline authors
4. Authors fix clashes, update models, close BCF issues
5. New clash run confirms resolution

Tools: BIMcollab, Solibri, Navisworks, IfcOpenShell (`bcf` module)

---

## Norwegian BIM Requirements

### Applicability First: Norway Is Not Synonymous with Statsbygg

Distinguish four sources of authority in every recommendation:
1. Norwegian law, regulations, applicable local plans and permit conditions.
2. The agreed project BIM requirements (byggherrekrav), delivery milestone and
   approved deviations. These cannot override statutory obligations.
3. Referenced standards and Norwegian editions/national annexes where relevant.
4. Vendor presets and international examples, which are implementation guidance,
   not evidence of compliance with the first three.

For private residential work, do not impose Statsbygg/SIMBA or TFM unless the
client or contract requires it. If the requirement package is unavailable, mark
applicability unconfirmed and give conditional guidance, not a delivery pass.

### Statsbygg / SIMBA

**Source check: 2026-09-06.** Statsbygg's BIM page directs users to SIMBA. The
public requirements page identifies **SIMBA 2.1**, effective for new Statsbygg
projects from 2022-07-01 unless otherwise agreed, based on **IFC4 (4.0.2.1)**.
It also describes **SIMBA 2.1.1** as a minimum-requirements alternative for
small/simple projects. This is not permission for Bob to downgrade a contract.

- Read the project-adapted requirement set, version, discipline and milestone.
  SIMBA explicitly allows project tailoring; only accepted changes alter the
  delivery basis. Do not silently replace a contracted version with a newer web version.
- Distinguish current SIMBA from the historical **Statsbygg BIM Manual 1.2.1
  (December 2013)**. Do not call that manual current SIMBA.
- Check general requirements, machine-validatable requirements, geometry
  requirements and the agreed BIM requirement document/EIR. Use the supplied
  mvdXML and/or IDS files with compatible validators, not an invented rule set.
- Use the project's actual geometry/information requirements per milestone.
  Do not invent a universal Statsbygg LOD 100–400 ladder or treat LOD as proof of as-built status.
- Record the required horizontal CRS, vertical datum, origin, rotation and
  transformation. Do not apply a universal EPSG code or assume a height datum.

### Archicad IFC Translators and TFM (Tverrfaglig Merkesystem)

Nordic BIM's article (2026-06-03) describes TFM-ready translators in **Norsk
prosjekteringsmal for Archicad 27** and **Norsk avansert mal for Archicad 28**.
The translators depend on properties in those templates. The article explicitly
warns that a project's BIM manual can differ from the preset configuration.
Do not extrapolate that availability to other versions or templates unverified.

**Export review workflow:**
1. Record Archicad version, Norwegian template/version, translator/version, IFC
   schema/view, required discipline and milestone. Read available project files
   before asking for missing inputs.
2. Read the project's TFM convention and code source. Do not invent code syntax,
   values, property names, or treat a classification code as a complete TFM ID.
3. Trace each required value from the source property to its exported IFC
   attribute/Pset/property or classification location. Record type-versus-instance
   scope, data type, format, applicability, and permitted empty values.
4. Export a representative sample and reopen the IFC independently. Compare
   expected and actual locations/values, preserving leading zeros and separators
   where required. Check uniqueness at the scope specified by the requirement;
   shared system/type codes are not automatically duplicate instance IDs.
5. Run applicable machine checks on the full delivery and separate manual checks
   for geometry, georeferencing and interdisciplinary coordination. A sample
   confirms mapping behavior only, not the entire model.
6. Report requirement ID/source, model revision, GlobalId, expected/actual value,
   pass/fail/not-checked, and responsible discipline. Retest after export or
   mapping changes; never fix the exported file without reconciling the authoring source.

**Acceptance evidence:** retain the requirement version, export settings,
model revision, validator/version, report and outstanding manual checks.
The preset name "Statsbygg" or "TFM" is never sufficient evidence of acceptance.

### Norwegian NS Standards for BIM
| Standard | Coverage |
|---|---|
| **NS 3451** | Building-element classification; verify the project-required edition and IFC mapping |
| **NS 3420** | Specification texts (used in model-to-specification linking) |
| **NS 8360** | BIM objects — requirements for building product objects |
| **NS-EN ISO 19650** | Organization and digitization of information about buildings (replaces BS 1192) |

Verify the edition and relevant clauses in the project's cited standard before
applying numerical or coding requirements. A standard number or vendor template
does not supply its contents; flag inaccessible requirements rather than invent them.

### eByggesøknad / Digital Permit Applications
Check current DiBK guidance and the receiving application's/municipality's
accepted formats. Do not infer that an IFC or SIMBA pass replaces drawings,
application documents, responsible design, or municipal approval.

### Verified Source Entry Points

- [Statsbygg BIM](https://www.statsbygg.no/bim/) — client BIM policy, not a national law.
- [SIMBA requirements](https://simba.statsbygg.no/kravene) — versions and project tailoring.
- [About SIMBA](https://simba.statsbygg.no/om-simba) — IFC, IDS/mvdXML, BCF and historical manual distinction.
- [Fagmodellansvarlig](https://simba.statsbygg.no/rolle/fagmodellansvarlig) — export responsibility, self-checks, interdisciplinary checks and deviations.
- [Nordic BIM translator guidance](https://www.nordicbim.com/no-no/knowledge/no-no/ifc-oversetter-som-inkluderer-tfm-og-er-egnet-for-statsbygg-og-andre) — template-specific implementation guidance, not client acceptance.

Reuse this source summary for orientation. Recheck the relevant source and
contracted requirement revision before delivery decisions or version-specific
mapping advice; fetch only the applicable sections, not the entire SIMBA catalog.

---

## Clash Detection — Practical Guide

### Clash Types
| Type | Description | Example | Severity |
|---|---|---|---|
| **Hard clash** | Two elements physically occupy the same space | HVAC duct through a structural beam | Critical — must resolve |
| **Soft clash** | Insufficient clearance between elements | HVAC duct within 50 mm of beam flange | High — resolve or accept |
| **Workflow clash** | Sequential dependencies violated | Electrical conduit where plumber needs to run pipes | Medium — coordinate |

### Resolution Hierarchy
1. Reroute the MEP element (usually cheaper than structural modification)
2. Resize the MEP element (smaller duct or pipe)
3. Add structural opening (notch or sleeve — must be engineered)
4. Relocate the structural element (last resort; requires engineer sign-off)

### Clash Matrix for Norwegian Residential Projects
| Trade | Structural | MEP Mains | Electrical | Fire safety |
|---|---|---|---|---|
| **Structural** | — | Route MEP around structure | Route around structure | Maintain fire barriers |
| **MEP Mains** | Never penetrate bearing walls without engineering | — | Maintain min. clearance | Fire dampers at crossings |
| **Electrical** | Route around beams/columns | Separate cable trays from pipes | — | No cables in fire barriers |

---

## Guidance for Drawing Review with IFC Data

When a user has an IFC file and asks about structural or permit questions:

1. **Validate storey structure** — are all elements assigned to correct storeys?
2. **Check load-bearing flag** — are `Pset_WallCommon.LoadBearing` properties populated?
3. **Extract room schedule** — use `IfcSpace` to verify room areas against permit requirements
4. **Cross-reference with TEK17** — load `building-code-tek17` to check compliance of room sizes, ceiling heights, egress
5. **Check coordination** — are structural, architectural, and MEP models federated without hard clashes?
6. **Verify georeferencing** — compare the declared CRS, height datum and transformation with the project's survey and BIM requirements; missing information remains unverified.

**Escalation:** IFC validation for permit submission requires a licensed responsible designer (ansvarlig prosjekterende). Bob can identify issues but cannot sign off on model compliance.
