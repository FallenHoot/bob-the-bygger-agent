---
name: architectural-drawing-reading
description: Reading Norwegian architectural and structural drawings — plantegninger, snitt, fasader, detaljer, konstruksjonstegninger. Includes symbol libraries, hatching conventions, søknad drawing package completeness, and vision-based analysis protocol. Load whenever a drawing or image is shared.
triggers: [drawing, tegning, floor plan, plantegning, section, snitt, elevation, fasade, detail, detalj, blueprint, scale, målestokk, title block, tegningshode, hatch, skravur, symbol, IFC, BIM, dimension, mål, beam notation, bjelke notation, reading drawings, tolke tegninger, drawing package, tegningspakke, søknad drawings, situasjonsplan, image uploaded, photo of drawing, scan, PDF drawing]
load_with: []
safety_level: low
auto_load_on: [image_upload, drawing_reference]
license: Proprietary
---

# Skill: Architectural Drawing Reading

## Domain
Reading, interpreting, and extracting information from Norwegian architectural and structural drawings — including floor plans (plantegninger), sections (snitt), elevations (fasader), details (detaljer), site plans (situasjonsplaner), and structural drawings (konstruksjonstegninger). Handles both image uploads (multimodal) and text descriptions of drawings.

---

## Core Principle

**Never fabricate. Uncertainty is information.**

When reading a drawing, BTBA distinguishes between three states:
- ✅ **Confirmed**: Directly readable from the drawing
- ⚠️ **Inferred**: Reasonable interpretation, stated as such with reasoning
- ❓ **Unknown**: Cannot be determined from this drawing — flag it and ask

A flagged gap is better than a confident fabrication. Structural conclusions drawn from misread drawings have consequences that cannot be undone.

---

## Norwegian Drawing Types — Terminology

| Norwegian | English | Typical Scale | Content |
|---|---|---|---|
| Situasjonsplan | Site plan | 1:500, 1:1000 | Plot boundaries, building footprint, setbacks, access, terrain |
| Plantegning | Floor plan | 1:100, 1:50 | Room layout, walls, doors, windows, stairs, dimensions |
| Fasadetegning | Elevation | 1:100, 1:50 | External appearance, window/door positions, roof profile, materials |
| Snitt / Tverrsnitt | Section | 1:100, 1:50 | Vertical cut through the building — ceiling heights, construction layers |
| Detaljtegning | Detail | 1:20, 1:10, 1:5, 1:1 | Specific junctions, connections, material build-ups |
| Fundamentplan / Grunnmursplan | Foundation plan | 1:100, 1:50 | Footings, basement walls, drainage, bearing conditions |
| Bjelkeplan / Dekkeplan | Floor structure plan | 1:100, 1:50 | Joist direction, beam positions, structural grid |
| Armeringstegning | Reinforcement drawing | 1:50, 1:20 | Rebar layout in concrete elements |
| Konstruksjonstegning | Structural drawing | 1:100, 1:50 | Load-bearing system, connections, member sizes |
| Rørtegning / VVS-tegning | MEP plan (plumbing/HVAC) | 1:100, 1:50 | Pipe runs, ventilation ducts, drain locations |

---

## The Reading Sequence — Always Follow This Order

### Step 1: Title Block First (Tegningshode)
Before reading anything else, read the title block. It tells you what you are looking at and under what authority.

Find and record:
- **Tiltakshaver** (client/owner)
- **Tegningsnummer** (drawing number) — critical for referencing other sheets
- **Tegningens navn/innhold** (drawing title — what is this a drawing of)
- **Dato** (date) — and revision history (Rev A, B, C...)
- **Målestokk** (scale) — never assume scale without confirmation
- **Tegnet av / Kontrollert av** (drawn by / checked by)
- **Prosjektnummer** (project number)

If the title block is missing or illegible, flag this immediately. An undated, unscaled, unattributed drawing cannot be relied upon without independent verification.

### Step 2: Identify Drawing Type and Orientation
- What drawing type is this? (Plan, fasade, snitt, detalj)
- If plan: which floor? (Kjellerplan, 1. etasje, 2. etasje, loftplan)
- If fasade: which facade? (Nord, Syd, Øst, Vest)
- If snitt: which section cut, and in which direction? (Look for the section indicator on the plan)
- Where is north? (Look for nordpil on site plans and sometimes floor plans)

### Step 3: Establish Scale and Dimensions
- Confirm the stated scale against any dimensioned elements
- Identify the dimension string conventions: internal vs. external dimensions, wall face vs. wall centre
- Check for scale bars (målestokklinje) — these survive reproduction better than written scale

### Step 4: Read the Structural System
- Identify load-bearing walls (bærevegger): typically shown with heavier lines, different hatching, or explicit notation
- Identify columns (søyler): typically shown as solid black squares or circles in plan
- Identify beams (bjelker): shown as dashed rectangles in plan (hidden above the cut plane), with span direction noted
- Identify the floor and roof structure: joist direction, structural grid (aksegrid)
- Identify the foundation system: strip (stripsåle), pad (punktfundament), slab (plate), piles (peler)

### Step 5: Read the Building Envelope
- Exterior wall build-up (thickness, layers from outside to inside)
- Window and door openings — width × height
- Roof slope and orientation
- Overhangs (takutstikk)

### Step 6: Identify Special Conditions
- Fire separation walls (brannskillende konstruksjoner): typically shown with a double line or explicit notation (F60, F90, EI60, EI90)
- Stairwells (trapperom) — typically a fire cell
- Wet rooms (våtrom): bathroom, kitchen, laundry — marked on plan
- Underfloor heating (gulvvarme) zones
- Heritage features (antikvariske elementer) — sometimes noted on drawings for listed buildings

### Step 7: Cross-Reference Other Sheets
- Note all sheet references on this drawing (see Snitt A-A on sheet K.02, etc.)
- Identify details that are expanded on other sheets
- Do not draw conclusions about construction without checking referenced details

---

## Norwegian Drawing Conventions and Symbol Library

### Line Types
| Line type | Norwegian | Use |
|---|---|---|
| Solid heavy | Synlig kontur | Visible outlines — the main drawing line |
| Solid medium | Synlig linje | Secondary visible elements |
| Dashed | Skjult linje | Elements above the cut plane (beams, upper walls), or hidden elements |
| Dash-dot | Symmetrilinje / akselinje | Centrelines, grid axes |
| Dash-dot-dot | Seksjonslinje | Section cut indicators |
| Dotted | Hjelpelinje | Construction lines, reference lines |

### Hatching Conventions in Plan and Section

| Material | Norwegian | Hatch pattern |
|---|---|---|
| Concrete (in situ) | Betong | Diagonal lines at 45°, closely spaced |
| Reinforced concrete | Armert betong | Same + small reinforcement symbol |
| Masonry (brick) | Murstein | Brick bond pattern |
| Masonry (lightweight block) | Lettbetong / Leca | Rectangular grid |
| Timber in section | Tre | Diagonal lines with grain marks at varying angles |
| Timber (structural) | Konstruksjonstre | X-pattern or diagonal with heavier outline |
| Insulation (mineral wool) | Mineralull | Zigzag or wavy horizontal lines |
| Insulation (rigid) | Stivt isolasjonssjikt | Dotted or hatched rectangle |
| Sand/gravel fill | Pukk/sand | Irregular dots or stipple |
| Soil | Jord/terreng | Diagonal short strokes |
| Steel (in section) | Stål | Solid black fill (thin sections) or diagonal fine lines |
| Screed / levelling | Påstøp | Diagonal fine lines |
| Vapour barrier / membrane | Dampsperre / membran | Heavy single or double line |

### Door Symbols (Plan)
- Single door: arc showing swing radius from pivot
- Double door: two arcs
- Sliding door (skyvedør): double parallel lines with arrow
- Pocket door (innfellsdør): dashed lines within wall thickness
- Door opening dimensions given as width × height: e.g. D1 = 900×2100

### Window Symbols (Plan and Elevation)
- In plan: three lines within wall opening (representing frame, glass, frame)
- Window designation: e.g. V1 = 1200×1200 (width × height)
- Window schedule (vindusplan) lists all window types
- Roof window (takvindu/Velux): shown in plan as dashed rectangle within roof area

### Stair Symbols (Plan)
- Steps shown as parallel lines with direction arrow
- Up direction: arrow pointing toward the higher floor, labelled "opp"
- Down direction: cut line (break symbol) across the stair with "ned"
- Step count noted: e.g. "17 trinn"

### Room Designations
Norwegian buildings use a room numbering system. Common abbreviations:
- **Gang**: hallway / corridor
- **Entre / Vindfang**: entrance / vestibule
- **Stue**: living room
- **Soverom**: bedroom
- **Kjøkken**: kitchen
- **Bad**: bathroom
- **WC**: toilet room
- **Bod**: storage room
- **Teknisk rom**: plant room (mechanical room)
- **Trapperom**: stairwell

Room areas noted as **m² BRA** (bruksareal, per NS 3940).

### Grid Axes (Akselinjer)
Structural grids use:
- Numbers (1, 2, 3...) in one direction
- Letters (A, B, C...) in the perpendicular direction
- Grid intersection notation: A/1, B/3, etc.
- Grid spacing (akselavstand) is centre-to-centre

### Elevation Symbols
- **FFL**: Ferdig gulvlinje — finished floor level
- **RFL**: Råbygggulvlinje — structural floor level (before screed/flooring)
- **OK**: Overkant — top of element (OK bjelke = top of beam)
- **UK**: Underkant — underside of element (UK dekke = underside of slab)
- **TH**: Takhøyde — clear ceiling height
- **SOH**: Same as FFL in some conventions
- Levels given in metres above mean sea level (m.o.h.) on site plans

---

## Structural Drawing Reading — Specific Conventions

### Beam Notation in Plan
Beams shown as dashed rectangles (they are above the cut plane of a floor plan at ~1.0m):
- Annotation format: e.g. **GL30 90×315** = glulam GL30, 90mm wide × 315mm deep
- Or **HEB 200** = steel I-beam, 200mm serial
- Or **B1, B2, B3** with a separate beam schedule (bjelkeskjema)
- Span direction: always parallel to the beam's long axis

### Column Notation in Plan
Shown as solid or hatched square/rectangle:
- Timber column: hatched square, e.g. **KL90×90**
- Steel column: solid square, e.g. **HEA 160**
- Concrete column: hatched concrete, e.g. **S1 = 250×250**

### Load Arrows
- Downward arrows: applied loads (gravity)
- Upward arrows: reactions (support)
- Arrow annotated with load magnitude: e.g. **P = 45 kN** (point load) or **q = 12 kN/m** (distributed load)

### Concrete Reinforcement Notation
- Bars shown as lines with tick marks or dots (dots = bars perpendicular to drawing plane)
- Designation: **Ø12c200** = 12mm diameter bars at 200mm centres
- Or **4Ø16** = 4 bars of 16mm diameter
- Cover (overdekning) noted in mm: typically 25–50mm for internal, 35–75mm for external/exposed

### Foundation Plan Reading
- Centreline of strip footings (stripsåler) with width dimension
- Elevation of footing bottom (underkant fundament): must be below frost depth
- Steps in footing: used on sloping sites, maximum step height = 600mm, minimum step length = 600mm
- Pad footings (punktfundamenter): square or rectangular, with column position marked
- Drainage pipe (drensrør): shown as circle or oval, with fall direction arrow

---

## When Reading a Photograph or Scan of a Drawing

When an image is uploaded, work through this sequence before providing any analysis:

### Vision Self-Check Protocol
1. **Declare what you see**: "This appears to be a [drawing type] at scale [X], showing [brief description]."
2. **Read the title block**: State what you can and cannot read. Flag missing or illegible elements.
3. **Note image quality**: Is the drawing clear enough to read dimensions? Are any areas illegible? 
4. **Identify the drawing's coordinate system**: Which way is up? Where is the entrance?
5. **List confirmed structural elements** — only what is explicitly shown or annotated
6. **List inferred elements** — with explicit reasoning ("The walls are approximately 300mm thick, which is consistent with a 198mm stud + cladding assembly, but I cannot confirm without a detail drawing")
7. **List what cannot be determined from this drawing alone**

### What BTBA Will Not Infer Without Evidence
- Whether a wall is load-bearing, if the drawing does not indicate this
- Material specifications not shown by hatching or annotation
- Subsurface conditions not shown in a foundation or site plan
- Fire separation ratings unless annotated
- Sound insulation ratings unless annotated
- Actual dimensions if no scale bar or dimension strings are visible

### Common Drawing Quality Problems to Flag
- **Reproduced at unknown scale**: The stated scale does not match the actual printed size. Check with a scale ruler against known elements.
- **Missing title block**: Drawing cannot be authoritatively attributed or dated
- **Conflict between drawings**: Plan shows a wall that does not appear in the section — flag the conflict, do not resolve it by assumption
- **Revision without revision cloud**: A change may have been made without highlighting what changed
- **Hand-marked changes**: Pencil or pen additions to a printed drawing are modifications that may not be in the official file

---

## Drawing Package Structure — Norwegian Søknad

A complete building permit application (søknad) in Norway includes the following drawing set. BTBA can identify which drawings are present and which are missing:

| Drawing | Norwegian requirement | Governing reference |
|---|---|---|
| Situasjonsplan | Required — show building on plot with setbacks and neighbours | SAK10 §5-4 |
| Plan alle etasjer | Required — all floor plans | SAK10 §5-4 |
| Alle fasader | Required — all four elevations | SAK10 §5-4 |
| Minst ett snitt | Required — at least one section | SAK10 §5-4 |
| Konstruksjonstegninger | Required for structural review — signed by prosjekterende | TEK17 §10 |
| Energiberegning / U-verdi beregning | Required for new construction | TEK17 §14 |
| Branntegninger | Required for BKL2 and above | TEK17 §11 |
| VA-tegninger | Required if connecting to public water/sewer | Kommunale krav |

Missing drawings from a søknad package are grounds for the municipality to request supplementary documentation (tilleggsopplysninger), adding 4–8 weeks to the process.

---

## BIM and Digital Drawing Context

### IFC (Industry Foundation Classes)
IFC is the open standard for exchanging BIM (Building Information Modelling) data. In Norway, IFC delivery is required for public projects and increasingly expected for larger private projects.

- **IFC2x3** and **IFC4** are the current in-use versions
- Key entity types for BTBA: `IfcWall` (structural or non-structural flagged by `LoadBearing` attribute), `IfcBeam`, `IfcColumn`, `IfcSlab`, `IfcRoof`, `IfcWindow`, `IfcDoor`
- IFC models can be viewed in free tools: Autodesk Viewer, BIMvision, xBIM Xplorer

### When a BIM Model Is Referenced
If the user describes elements from a BIM model rather than a 2D drawing:
- Ask for the IFC export or specific model view
- Request confirmation of whether the `LoadBearing` attribute has been set correctly (it is often not set in early-stage models)
- Note that BIM models may differ from the approved permit drawings — the permit drawings govern legally

---

## Integration with Other BTBA Skills

| Trigger from drawing | → Invoke this skill |
|---|---|
| Load-bearing wall to be removed | → `structural-engineering.md`: load path analysis |
| U-values or insulation layers visible | → `sintef-byggforsk.md`: moisture and thermal check |
| Søknad drawing package being reviewed | → `building-code-tek17.md`: completeness and compliance |
| Pre-1900 building or SEFRAK-registered | → `historic-preservation.md`: heritage drawing conventions |
| Classical proportions, façade composition | → `classical-architecture.md`: assess composition |
| Construction sequencing from drawings | → `construction-execution.md`: site sequence check |

---

## Asking the Right Questions — Drawing Review Checklist

When reviewing drawings on behalf of a client, BTBA asks:

**Structural**
- [ ] Is the load path continuous from roof to foundation on every drawing?
- [ ] Are all beam sizes specified, or left "by engineer"?
- [ ] Are connections shown at critical junctions (beam-to-column, beam-to-wall, roof-to-wall)?
- [ ] Is the foundation type shown, and is it appropriate for the noted soil conditions?

**Regulatory**
- [ ] Does the situasjonsplan show correct setbacks to all boundaries and roads?
- [ ] Is the building height within the allowed limit per reguleringsplanen?
- [ ] Are all required drawings present for the søknad package?
- [ ] Are wet rooms positioned above each other (minimizes pipe runs and leak exposure)?

**Buildability**
- [ ] Can a concrete pump reach the foundation pour?
- [ ] Is there a temporary prop plan for the construction sequence?
- [ ] Are door and window openings dimensioned correctly for off-the-shelf product sizes?
- [ ] Are headroom clearances confirmed at stairs and changes in ceiling height?

**Heritage (if applicable)**
- [ ] Does the façade drawing maintain the original window proportions?
- [ ] Are new openings aligned with the existing rhythm?
- [ ] Is the roof slope consistent with the original and neighbouring buildings?

---

## IFC / BIM File Reading

When the user provides an IFC file (or data extracted from one) instead of a 2D drawing:

**Before reading IFC data, check:**
1. **File version** — IFC2x3 TC1 (legacy, most common), IFC4 Add2 (current), IFC4x3 (infrastructure only)
2. **Units** — confirm meter or millimeter from `IfcProject.UnitsInContext`. Norwegian standard: millimeters.
3. **Storey structure** — `IfcBuildingStorey` names and elevations. Are all elements assigned to storeys?
4. **Coordinate system** — Norwegian projects use ETRS89 / UTM zone 33N (EPSG:25833). Check `IfcSite.RefLatitude / RefLongitude`.

**Extracting the same information as a 2D drawing:**

| 2D Drawing | IFC Equivalent |
|---|---|
| Floor plan (plantegning) | `IfcBuildingStorey` + all elements at that level |
| Room list | `IfcSpace` with `LongName` and area from `Qto_SpaceBaseQuantities.NetFloorArea` |
| Wall schedule | `IfcWall` + `Pset_WallCommon` (LoadBearing, IsExternal, FireRating) |
| Window schedule | `IfcWindow` + `Pset_WindowCommon` (OperationType, U-value) |
| Structural beams | `IfcBeam` + `Pset_BeamCommon` + `IfcMaterialProfileSet` (cross-section) |
| Door schedule | `IfcDoor` + `Pset_DoorCommon` (FireExit, SecurityRating) |

**Red flags in IFC models:**
- All elements at elevation 0.0 (missing storey assignment)
- `LoadBearing = False` on all walls (likely not filled in)
- No `IfcSpace` entities (rooms not modelled — can't extract areas)
- Duplicate GUIDs (model merge error — elements may be doubled)
- No materials assigned (can't extract U-values or structural properties)

**For full BIM/IFC guidance** (clash detection, IDS validation, IfcOpenShell tools), load the `bim-ifc` skill.

---

*Authority: NS-EN ISO 128 (Technical drawings), NS 3940 (Area measurements), SAK10 §5-4 (Drawing requirements for søknad), NS 3041 (Architectural symbols), NS-EN 81346 (Reference designation), IFC ISO 16739-1*
*Last reviewed: 2026-08-09*
