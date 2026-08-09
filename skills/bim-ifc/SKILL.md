---
name: bim-ifc
description: BIM/IFC awareness — reading IFC files, buildingSMART IDS validation, IfcOpenShell toolchain, clash detection, BCF issue tracking, and Norwegian BIM mandate requirements. Load whenever user mentions IFC, BIM, Revit, ArchiCAD, a .ifc file, model coordination, clash detection, or information delivery specifications.
license: Proprietary
metadata:
  triggers: IFC, BIM, ifc file, ifcopenshell, Revit, ArchiCAD, Bonsai, buildingSMART, IDS, clash detection, BCF, model coordination, BREEAM, Statsbygg, openBIM, Navisworks, model check, IFC export, IFC import, digital twin, COBie, model federation, LOD, level of development, eByggesøknad, digital byggesøknad
  load_with: architectural-drawing-reading
  safety_level: low
---

# Skill: BIM / IFC

## Domain
Building Information Modelling (BIM) concepts, the IFC (Industry Foundation Classes) open standard, the IfcOpenShell toolchain, buildingSMART IDS (Information Delivery Specification), clash detection, BCF issue tracking, and Norwegian BIM policy requirements.

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
| **IFC4x3 Add2** | Emerging | Adds infrastructure (bridges, roads, tunnels); not yet mainstream |

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
2. **Identify the coordinate system** — `IfcSite` and `IfcBuilding` set the world coordinate system. Check `RefLatitude`, `RefLongitude`, and `RefElevation` for georeferencing.
3. **Check spatial hierarchy** — valid hierarchy is: `IfcProject` → `IfcSite` → `IfcBuilding` → `IfcBuildingStorey` → elements. Models missing a storey level are poorly authored.
4. **Check structural elements** — look for `LoadBearing = True` on `IfcWall` instances. In poorly authored models, this property may be missing.
5. **Check property sets (Psets)** — Norwegian Statsbygg and NS 3451 use specific Psets (`Pset_WallCommon`, `Pset_BeamCommon`, custom Norwegian Psets). Missing Psets indicate incomplete authoring.

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

**IDS** (Information Delivery Specification) is a buildingSMART standard (v1.0 Final, 2022) for defining *machine-readable requirements* that an IFC model must satisfy.

### What IDS Solves

Without IDS, a contractor receives an IFC model and manually checks whether it contains the required information. With IDS, the checking is automated using tools like `ifctester`.

### IDS File Structure (XML)

An IDS file defines **specifications** — each specification contains:
- **Applicability**: Which IFC elements this rule applies to (by entity type, classification, property)
- **Requirements**: What data those elements must have (properties, materials, classifications, geometry)

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

### Statsbygg BIM Manual
Norway's state building client (Statsbygg) has published one of the world's most comprehensive BIM requirements. Key requirements:
- All new public buildings require IFC delivery at key milestones
- IFC4 preferred for new projects
- Georeferencing required (EPSG:25833 — ETRS89 / UTM zone 33N)
- LOD (Level of Development) requirements per phase:
  - Concept: LOD 100 (massing only)
  - Schematic: LOD 200 (approximate geometry + classification)
  - Design Development: LOD 300 (accurate geometry + full properties)
  - Construction: LOD 350 (connections, interfaces)
  - As-Built: LOD 400+ (actual as-built condition)

### Norwegian NS Standards for BIM
| Standard | Coverage |
|---|---|
| **NS 3451** | Table of building elements (classification system used in Psets) |
| **NS 3420** | Specification texts (used in model-to-specification linking) |
| **NS 8360** | BIM objects — requirements for building product objects |
| **NS-EN ISO 19650** | Organization and digitization of information about buildings (replaces BS 1192) |

### eByggesøknad / Digital Permit Applications
DiBK (Norwegian Building Authority) has been developing digital building permit submission. IFC models may be submitted directly or linked from digital søknad. The `buildingSMART/BIM-Validation-Tools` project validates IFC models for søknad compliance.

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
6. **Verify georeferencing** — confirm ETRS89 / UTM 33N for Norwegian projects

**Escalation:** IFC validation for permit submission requires a licensed responsible designer (ansvarlig prosjekterende). Bob can identify issues but cannot sign off on model compliance.
