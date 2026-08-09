---
name: structural-engineering
description: Load paths, beam sizing, deflection, connections, foundation assessment, and structural failure diagnosis for Norwegian residential and light commercial construction (Eurocodes + Norwegian NA).
triggers: [beam, bjelke, load, last, load bearing, bærevegg, wall removal, vegg, column, søyle, foundation, fundament, deflection, nedbøyning, structural, konstruksjon, snow load, snølast, wind load, vindlast, moment, shear, capacity, kapasitet, glulam, limtre, timber, stål, reinforcement, armering, seismic, settlement, setning, rot, råte at bearing]
load_with: [building-code-tek17]
safety_level: high
license: Proprietary
---

# Skill: Structural Engineering

## Domain
Load path analysis, beam and column sizing, deflection limits, connection design, foundation assessment, and structural failure diagnosis — applied to Norwegian residential and light commercial construction.

---

## Drawing Freeze Gate ⛔

**This gate must pass before any detailed structural calculation is produced.**

Do not calculate moments, deflections, or member sizes until ALL of these are confirmed:

```
[ ] Drawing package reviewed using drawing-reader + architectural-drawing-reading
[ ] Drawing set is consistent with the owner’s stated design intent
[ ] Key spanning dimensions confirmed from drawings or site measurement (not inferred)
[ ] No unresolved contradictions between plan, section, and elevation
[ ] Architect has locked the layout — no open design questions that change structural geometry
```

**If the gate is closed:**
- Preliminary (rule-of-thumb) sizing with explicit LOW confidence is allowed
- Qualitative load path analysis (no numbers) is allowed
- State clearly: “Detailed structural calculations cannot be performed until [specific condition] is resolved”
- Never produce a structural calculation table or beam adequacy check before this gate passes

**Exceptions:** None. The gate exists because analysis built on incorrect drawings creates conflicting documents that persist and cause real errors.

---

## Calculation Input Lock Protocol 🔒

**Required before the first formula is written.** Every structural calculation session must open with a locked input table.

**Format — state this explicitly in the response:**

```
🔒 LOCKED INPUTS — [Project ID] — [Date]

| Input        | Locked value | Source                     | Method           | Confidence |
|---|---|---|---|---|
| Span         | [X] mm       | [Drawing ref / measurement] | [How confirmed]  | High/Med/Low |
| Dead load    | [X] kN/m²   | [Material list + EN 1991]  | [Calculated]     | High/Med/Low |
| Live load    | [X] kN/m²   | [EN 1991-1-1 Table X]      | [Code]           | High |
| Snow load    | [X] kN/m²   | [TEK17 Table 7.1, zone Z]  | [Code]           | High |
| Material     | [X]          | [Drawing / PE doc / test]  | [How confirmed]  | High/Med/Low |
| Section      | [X]          | [Drawing / PE doc / caliper]| [How confirmed] | High/Med/Low |

All calculations below use these locked values.
If any input changes, this entire calculation package is VOID.
```

**If a locked input changes later in the session:**
1. Immediately state: “⚠️ Input change detected: [old value] → [new value]. All calculations using the old value are VOID.”
2. Issue a new locked input table
3. Mark all prior calculations: “⚠️ SUPERSEDED by [new document / date] — do not use”
4. Rerun affected calculations from scratch

**Confidence rules:**
- Source is a PE drawing or direct measurement → High
- Source is the drawing under review, confirmed from title block / dimension string → High
- Source is user statement, not independently verified → Medium
- Source is assumed from era/location/practice → Low — must be stated explicitly in every conclusion that uses it

---

## Core Principles

### The Load Path Hierarchy
Every load must travel a continuous path from where it is applied to where it is resisted by the ground. There are no exceptions.

```
Snow + Live loads
       ↓
   Roof structure
       ↓
   Wall framing / columns
       ↓
   Floor structure / beams
       ↓
   Foundation / bearing walls
       ↓
   Ground (soil / rock)
```

When a wall is removed, a beam must replace the load path. When a floor is added, the columns and foundation must be checked for the additional load. Interrupting the load path without replacing it is the single most common cause of residential structural failure.

---

## Standard Load Values — Norway

### Dead Loads (Egenlast)
| Element | Characteristic load |
|---|---|
| Timber floor (120mm + flooring) | 1.0–1.5 kN/m² |
| Concrete slab 150mm | 3.6 kN/m² |
| Roof (pitched timber + tiles) | 0.8–1.2 kN/m² |
| Roof (flat, membrane + insulation) | 1.5–2.5 kN/m² |
| Brick masonry wall (per m²) | 1.8–4.0 kN/m² |
| Log wall (laft), ~200mm | 1.0–1.4 kN/m² |

### Imposed (Live) Loads — NS-EN 1991-1-1 (Eurocodes)
| Category | Use | q_k (kN/m²) |
|---|---|---|
| A | Domestic / residential floors | 2.0 |
| A | Stairs | 3.0 |
| B | Office | 3.0 |
| C1 | Areas with tables (cafés) | 3.0 |
| C3 | Crowded rooms | 5.0 |
| E1 | Storage | 7.5 |

### Snow Loads — NS-EN 1991-1-3 + Norwegian NA
Snow load on ground (s_k) varies by location:
- Oslo: ~2.5 kN/m²
- Bergen: ~3.5 kN/m²
- Trondheim: ~3.5–4.0 kN/m²
- Mountain regions: up to 9.0 kN/m²

Roof snow load: `s = µ_i × C_e × C_t × s_k`
- µ_i = shape coefficient (0.8 for flat/shallow pitch)
- C_e = exposure coefficient (typically 1.0)
- C_t = thermal coefficient (typically 1.0)

### Wind Loads — NS-EN 1991-1-4 + Norwegian NA
Reference wind speed (v_b,0) by zone. Oslo approx. 22 m/s. Apply terrain category corrections. For residential design, rely on the structural engineer's wind zone table rather than calculating from scratch without context.

---

## Load Combinations — Eurocode (NS-EN 1990)

### Ultimate Limit State (ULS) — Strength
The governing combination for most residential design:

**STR** (structural): `γ_G × G_k + γ_Q × Q_k,1 + Σ(γ_Q × ψ_0 × Q_k,i)`

Simplified for timber residential:
- Permanent load factor γ_G = 1.35 (unfavorable) / 1.0 (favorable)
- Variable load factor γ_Q = 1.5
- Common combination: **1.35 G + 1.5 Q** (or 1.0 G + 1.5 Q when permanent is favorable)

### Serviceability Limit State (SLS) — Deflection
Use characteristic combination: `G_k + Q_k,1 + Σ(ψ_0 × Q_k,i)`

---

## Timber Beam Sizing — Quick Reference

### Deflection Limits (NS-EN 1995-1-1, TEK17)
| Condition | Limit |
|---|---|
| Final deflection (w_net,fin) | L / 250 |
| Variable load deflection (w_2) | L / 300 |
| Appearance-sensitive spans | L / 400 |

### Span-to-Depth Rule of Thumb
For a simply supported timber floor joist at 600mm spacing, residential loading (2.0 kN/m² imposed + ~1.0 kN/m² dead):

**Depth (mm) ≈ Span (mm) / 20** as a starting estimate. Always verify with full calculation.

Example: 5.4m span → 270mm depth → try C24 45×270 or glulam GL30 90×270.

### Glulam (Limtre) Standard Sections
Common sections: 90×180, 90×225, 90×270, 90×315, 90×360, 140×180, 140×225, 140×270, 140×315, 140×360, 140×405, 140×450, 190×360, 190×405, 190×450, 215×450.

### Timber Strength Classes
| Class | f_m,k (bending) | f_t,0,k (tension) | E_mean |
|---|---|---|---|
| C16 | 16 MPa | 10 MPa | 8,000 MPa |
| C24 | 24 MPa | 14 MPa | 11,000 MPa |
| C30 | 30 MPa | 19 MPa | 12,000 MPa |
| GL24h | 24 MPa | 16.5 MPa | 11,600 MPa |
| GL30h | 30 MPa | 19.5 MPa | 13,600 MPa |

---

## Steel Beam Assessment

For residential lintels and replacement beams, HEB/HEA/IPE profiles are common. Quick check for ULS bending:

`M_Ed ≤ M_c,Rd = W_pl × f_y / γ_M0`

Where:
- `W_pl` = plastic section modulus (mm³) from profile tables
- `f_y` = yield strength = 355 MPa (S355) or 275 MPa (S275)
- `γ_M0` = 1.0 (partial factor)

Always check lateral-torsional buckling (LTB) for unrestrained beams with significant span. Provide lateral restraint at the compression flange where possible.

---

## Load-Bearing Wall Identification

**Signs a wall is structural:**
- Runs perpendicular to floor joists
- Located at mid-span of floor joists
- Sits above a beam, column, or another bearing wall on lower floors
- Made of full-height studs from foundation to roof ridge
- Has a doubled or tripled top plate
- Older masonry or log (laft) walls are almost always structural

**Definitive method:** Trace the load path from the roof down. Map joist direction (parallel to the long wall span) and look for mid-span supports.

---

## Foundation Assessment

### Bearing Capacity — Indicative Values
| Soil Type | q_a (kN/m²) |
|---|---|
| Soft clay / sensitive | 25–50 |
| Stiff clay | 75–150 |
| Dense sand/gravel | 100–300 |
| Rock (sound) | 1,000–3,000+ |

In Norway, always check for quick clay (kvikkleire) in areas with glaciomarine deposits (Østlandet, Trøndelag, coastal areas). If in doubt, require a geotechnical report (grunnundersøkelse) before any foundation modification.

### Strip Foundation Rule of Thumb
Width of strip footing = (Total wall load in kN/m) / (Allowable bearing pressure in kN/m²)

---

## Structural Failure Warning Signs

Treat these as red flags requiring immediate assessment:
- Diagonal cracking from window or door corners (differential settlement or racking)
- Horizontal cracks in masonry (overloading or foundation movement)
- Sagging ridge line or ceiling (inadequate roof structure or ridge beam failure)
- Out-of-plumb walls >L/200 in masonry
- Visible deflection in floors under load (check actual vs. permitted deflection)
- Rot at beam ends, sill plates, or at column bases (section loss = capacity loss)

---

## Structural Distress Patterns — Diagnosis Guide

### Crack Patterns in Masonry and Concrete

| Pattern | Likely cause | Urgency |
|---|---|---|
| **Diagonal crack from window/door corner** (45° stepped) | Differential settlement; foundation movement | High — monitor immediately, check soil |
| **Diagonal crack in wall panel** (shear crack) | Racking/lateral load; insufficient shear wall | High — structural assessment needed |
| **Horizontal crack** at mortar joint, mid-wall | Overloading; wall buckling; thermal/moisture | Medium — check load path above |
| **Vertical crack** at structural junction | Differential movement between two elements | Medium — could be shrinkage or movement |
| **Map/spider cracking** (all directions) | Plastic shrinkage (concrete); alkali-silica reaction | Low/Medium — depth matters; carbonation test |
| **Hairline cracks** in plaster | Normal thermal/moisture cycling | Low — cosmetic unless widening |
| **Wide crack > 3 mm, increasing** | Active movement — could be structural | Urgent — install tell-tales; get engineer |

**Tell-tale protocol**: If a crack is suspect, install a crack monitor (tell-tale or witness mark with date and crack width). Measure monthly. If crack grows > 1 mm/month or accelerates, escalate immediately.

### Timber Failure Patterns

| Sign | Likely cause | Action |
|---|---|---|
| **Sag in floor** — springy, deflects > L/250 | Overloaded joist, section loss from rot, inadequate size | Probe for rot; calculate actual deflection vs. limit |
| **Rot at beam end** | Moisture at bearing; end-grain exposure | Measure residual section; replace if > 25% cross-section lost |
| **Rot at sill plate** (under external wall) | Rising damp, failed DPC | Assess extent; replace sill before rebuilding above |
| **Split along grain** (horizontal crack) | Shear failure at bearing; over-notching | Check notch depth vs. EN 1995 limits (≤ h/4 at support) |
| **Crushing at bearing** | Perpendicular-to-grain stress exceeded | Assess bearing length; add spreader plate or post |
| **Insect damage** (powderpost beetle, woodworm)** | Boreholes + fine powder (frass) | Probe depth; treat with boron; assess section loss |
| **Creep deflection** (long-term sag, no load increase) | Sustained load + moisture cycling | Normal for spans > 4 m; check against L/250 final deflection limit |

### Concrete Failure Patterns

| Sign | Likely cause | Action |
|---|---|---|
| **Spalling + rust staining** | Rebar corrosion (carbonation or chloride) | Measure carbonation depth; cover depth; assess rebar section |
| **Delamination of cover** | Severe carbonation or chloride ingress | Expose rebar; assess structural section loss |
| **Map cracking in flat slab** | ASR (alkali-silica reaction) — rare in Norway | Core sample for analysis |
| **Punching failure at column** | Flat slab shear at column head | Structural emergency — prop immediately |
| **Honeycombing** | Poor compaction during pour | Assess depth; repair with structural epoxy if severe |

### Foundation Movement Indicators

| Sign | Likely cause | Action |
|---|---|---|
| **Diagonal cracking both sides of opening** | Differential settlement under wall ends | Check soil; monitor; geotechnical assessment |
| **Doors and windows sticking** | Frame racking from foundation movement | Check plumb; measure displacement; investigate soil |
| **Step cracks at corners** | Settlement of one corner of building | Most serious; likely soil compressibility or drainage issue |
| **Heave (floor rising)** | Frost heave or expansive clay | Check drainage; foundation depth; soil type |
| **Visible slope of floors** | Settlement or inadequate beam sizing | Level survey; trace cause before remediation |

**Response hierarchy for foundation distress:**
1. Prop any immediately unsafe elements
2. Install crack monitors; photograph with scale bar and date
3. Commission geotechnical investigation — `GEOTECHNICAL_REPORT_REQUIRED`
4. Commission structural assessment — `WET_STAMP_REQUIRED`
5. Do not dig near foundations without geotechnical guidance (can trigger progressive settlement)

---

## Interaction with Other Skills
- **TEK17**: All structural design must comply with §10 (Konstruksjonssikkerhet). Structural engineering calculations are required in the building permit application (søknad).
- **SINTEF Byggforsk**: Execution details for timber connections, moisture protection at foundations, and wood-concrete interfaces.
- **Historic Preservation**: Structural interventions on SEFRAK-registered buildings require antikvarisk assessment before introducing new loads or removing original structure.
- **BIM/IFC**: When structural analysis is based on an IFC model, cross-check `IfcWall.LoadBearing`, `IfcBeam`, and `IfcColumn` instances against Pset_WallCommon and Pset_BeamCommon property sets. Missing structural properties in the model are a red flag for incomplete BIM authoring.

---

## BIM Coordination Checklist (Structural)

When structural work is coordinated with architectural and MEP models:

```
Pre-design:
[ ] Structural model exported to IFC 4.x — all elements classified with correct IfcEntity
[ ] LoadBearing flag set to TRUE on all bearing walls, columns, and beams
[ ] Fire rating populated in Pset_WallCommon.FireRating for all fire-compartment walls
[ ] Storey assignment correct — no elements floating at Level 0
[ ] Coordinate system set to ETRS89 / UTM 33N (EPSG:25833) for Norwegian projects

Design coordination:
[ ] Clash detection run against MEP model — zero hard clashes at tender
[ ] All slab penetrations > 150 mm shown with trimmer bars or engineered opening
[ ] Steel connection zones clear of ductwork (min. 150 mm clearance to flanges)
[ ] Foundation depths coordinated with drainage, services, and piling platform level
[ ] Reinforcement cover zones not violated by embedded items

Fire stopping:
[ ] Fire stopping locations agreed at all structural penetrations
[ ] Intumescent collars specified at plastic pipe penetrations through fire-rated floors

Pre-construction:
[ ] Expansion joints aligned across all disciplines (structural, architectural, facade)
[ ] Temporary works propping scheme does not conflict with MEP rough-in sequence
[ ] Hold points for engineer inspection established: foundation before backfill, frame before cladding
```

**Clash resolution priority** (from `bim-ifc` skill):
1. Reroute MEP element (cheapest)
2. Resize MEP element (smaller duct/pipe)
3. Engineer a structural opening (notch or sleeve — requires calculation)
4. Relocate structural element (last resort; triggers re-calculation)

---

*Authority: NS-EN 1990, NS-EN 1991 (Eurocodes), NS-EN 1993 (Steel), NS-EN 1995 (Timber), TEK17 §10*
*Last reviewed: 2026-08-09*
