---
name: sintef-byggforsk
description: Technical execution for Norwegian construction — moisture physics, vapour barriers, insulation, airtightness, wall/roof assemblies, frost-safe foundations. Based on SINTEF Byggforskserien.
triggers: [moisture, fukt, vapour, damp, insulation, isolasjon, airtight, tett, thermal bridge, kuldebre, condensation, kondensasjon, mould, mugg, rot, råte, wall assembly, veggoppbygging, roof assembly, takoppbygging, PE-folie, mineral wool, steinull, EPS, XPS, PIR, drainage, drenering, ventilated cavity, luftet, blower door, tetthetsprøve, frost, tele, capillary, kapillær, sd-value, dampsperre, undertak, vindsperre]
load_with: []
safety_level: medium
license: Proprietary
---

# Skill: SINTEF Byggforsk

## Domain
Technical execution details for Norwegian construction, drawing on SINTEF Byggforsk Byggdetaljblad (construction detail sheets) and the Byggforskserien knowledge base. Covers moisture physics, insulation performance, airtightness, roofing, foundations, and material compatibility — with emphasis on how to actually build correctly, not just what the code requires.

---

## What SINTEF Byggforsk Is

**SINTEF Byggforsk** is Norway's independent building research institute. Their **Byggdetaljblad** (detail sheets, numbered in the 500-series) are the definitive technical reference for Norwegian construction practice. They are not law, but they represent accepted good practice (god byggeskikk) and are routinely cited by building authorities as the standard of care.

Key series:
- **520** — Foundations and ground works
- **523** — Basement and below-grade
- **524** — External walls
- **525** — Roofs
- **526** — Floors
- **527** — Windows and doors
- **571** — Moisture and vapour
- **700** — Building physics (heat, moisture, sound)

When citing specific sheet numbers, BTBA will note that numbering may have been updated. Direct the user to [www.byggforsk.no](https://www.byggforsk.no) for the current edition.

---

## Moisture Physics — Fundamentals

### The Four Sources of Moisture
1. **Precipitation** (nedbør): Rain and snow driven against the envelope
2. **Ground moisture** (grunnfukt): Capillary rise and soil water vapor
3. **Construction moisture** (byggeinnfukt): Water in concrete, mortar, green timber
4. **Condensation** (kondensasjon): Water vapor in interior air condensing on cold surfaces

Every moisture problem in Norwegian construction traces to one or more of these sources not being adequately controlled.

### Vapour Drive Direction
In Norway's climate, the vapour pressure is nearly always higher inside a heated building than outside in winter. The vapour drive is **outward** for most of the year. This means:
- The **vapour retarder** goes on the **warm (interior) side** of insulation
- Cold side must be able to dry outward (breathable, permeable construction)
- Never trap moisture between two vapour barriers

### Critical Moisture Values
| Material condition | Risk |
|---|---|
| Wood at > 20% moisture content (MC) | Risk of mould (mugg) |
| Wood at > 28% MC | Risk of rot (råte) |
| Concrete with RH > 85% at bonding surface | Adhesive/coating failures |
| Concrete with RH > 90% before floor covering | Alkali emissions |

### Diffusion and the sd-value (Dampsperre)
- **sd-value**: equivalent air layer thickness for vapour diffusion (m)
- A vapour retarder has sd ≥ 1,500 m (Class I) per NS 1501
- A vapour barrier has sd ≥ 50,000 m (effectively impermeable)
- Common 0.15 mm polyethylene: sd ≈ 75 m (classified as a strong vapour retarder, not full barrier — but used as one in practice)

**Rule of 5:2**: The thermal resistance on the cold side of the vapour retarder should be no more than 1/5 of total (cold:warm ratio ≥ 4:1). If cold side is thicker, condensation risk inside the construction rises.

---

## Insulation Systems

### Mineral Wool (Steinull / Glassvatt)
- Lambda value (λ): typically 0.034–0.038 W/mK for standard products
- Stone wool preferred for fire separation (non-combustible, A1 classification)
- Glass wool acceptable for non-fire-rated cavity fill
- Compress mineral wool and it loses thermal performance — never compact to fit

### Rigid Foam Boards
| Product type | λ (W/mK) | Notes |
|---|---|---|
| EPS (Expanded polystyrene) | 0.036–0.040 | Ground contact OK. Not A-rated fire class. |
| XPS (Extruded polystyrene) | 0.030–0.036 | Excellent moisture resistance. Below slab, in drainage. |
| PIR (Polyisocyanurate) | 0.022–0.025 | Best R-value per mm. Roofs and wall interiors. |
| Phenolic foam | 0.020–0.022 | Highest performance, expensive, brittle |

### Thermal Bridge (Kuldebroer) — Correction Values
Every structural element that penetrates the insulation layer is a thermal bridge. Norwegian standard requires kuldebroverdi (Ψ-values) to be calculated or estimated from tables (SINTEF 700-series).

Typical correction values (normalized per m² envelope area):
- Stud frame wall with 600mm stud spacing: +0.03–0.05 W/m²K effective
- Window perimeter (per linear metre frame): Ψ ≈ 0.04–0.08 W/mK
- Balcony slab penetration (no thermal break): Ψ ≈ 0.5–0.8 W/mK

Eliminating balcony thermal bridges with structural thermal break elements (e.g., Schöck Isokorb) is required practice for TEK17 energy compliance in multi-storey construction.

---

## Airtightness

### Target Values
- TEK17 implies air leakage at 50 Pa (n50): ≤ 1.5 air changes/hour for residential, ≤ 1.5 h⁻¹ for other buildings
- Passive house standard (Passivhus, NS 3700): n50 ≤ 0.6 h⁻¹
- The air barrier must be continuous — every penetration (pipes, cables, rafters) must be sealed

### Air Barrier Materials and Details
| Location | Preferred material |
|---|---|
| Timber frame walls | 0.15 mm polyethylene membrane (PE-folie) |
| Concrete or masonry | Concrete itself (if cast-in-place and unpierced) |
| Roof / loft hatch | Pre-formed gasket or airtight hatch product |
| Window-to-wall junction | Compressible pre-compressed foam tapes (forkomprimerte lister) |

Critical sealing points:
1. Top of external wall to ceiling/roof structure (often unsealed in older buildings)
2. Around electrical boxes (use airtight electrical boxes or membrane collars)
3. Pipe and cable penetrations through the air barrier (use rubber grommets or membrane sealing sleeves)
4. Around roof windows (Velux or equivalent: use their own connecting membrane collars)

---

## Wall Assemblies — Common Norwegian Configurations

### Standard Timber Frame Wall (Bindingsverkvegg) — New Construction
```
Exterior cladding (trekledning / fasadeplater)
Ventilated cavity 25–50 mm (luftet kledning)
Wind barrier membrane (vindsperre) sd ≈ 0.1–0.3 m
Structural sheathing (vindsperreplate) OR open framing
Insulation in stud cavity — mineral wool (100–198 mm)
Vapour retarder PE-folie 0.15 mm
Optional service cavity with additional insulation (50–100 mm)
Interior gypsum board (gipsplate)
```
Typical total: 250–300 mm wall thickness for TEK17 compliance (U ≤ 0.18 W/m²K).

### Brick Veneer + Timber Frame (Murverk + Bindingsverk)
```
Half-brick (120 mm) masonry outer leaf
Cavity (30–50 mm) — cavity ties (murankre) at max 600 mm c/c horizontal, 450 mm vertical
Wind barrier
Timber frame with insulation (145–198 mm)
Vapour retarder
Interior finish
```
The cavity must be ventilated at base (weep holes) and top for moisture management.

### Log Wall (Laftekonstruksjon) — Historic and Modern
- Settling (setning): green log walls settle 20–40 mm per metre of height during drying. All openings need settling allowance (settling space above door/window frames filled with compressible material).
- Modern machined logs (rund- or kantet laft) have lower settling (10–20 mm/m) than hand-hewn.
- Log walls do not meet TEK17 U-value requirements without supplementary insulation — heritage buildings require dispensasjon.

---

## Roof Systems

### Pitched Roof — Cold Loft (Kald loft)
```
Roof tiles / metal roofing
Underroof (undertak) — membrane on battens
Counter batten (motlekte)
Rafter (sperr)
Ventilated cold loft space — min. 50 mm clear at ridge, 25 mm at eave
Insulation at ceiling level
Vapour retarder
Interior ceiling
```
Cold loft requires free ventilation from eave to ridge. Blocked soffits are the most common cause of moisture damage in Norwegian roofs.

### Warm Roof (Varm takkonstruksjon) — Flat / Low-Pitch
```
Waterproofing membrane (takbelegg)
Drainage layer (if inverted)
Thermal insulation — PIR or XPS minimum 200 mm for TEK17
Vapour barrier (essential on warm side of insulation)
Structural deck (betong or timber)
Interior finish
```
Critical: ensure no cold bridging at parapet edge. Detail the parapet-to-deck junction with a continuous insulation wrapping.

### Green Roof (Vegetasjonstak)
- Root-resistant membrane required (FPO, PVC, or modified bitumen with root barrier)
- Drainage layer ≥ 40 mm (Leca, drainage mat)
- Filter fabric
- Growing medium: 50–200 mm depending on plant type (sedum: 50–80 mm, perennials: 150–200 mm)
- Structural load: wet substrate 60–100 mm sedum = 0.8–1.5 kN/m²; check building structure

---

## Foundations and Below-Grade

### Kapillær Fukt (Capillary Moisture)
- Concrete and masonry wick water from the ground by capillary action
- Solution: capillary break (kapillærbrytende lag): ≥ 150 mm crushed stone (pukk) 8–16 mm under slab
- Additional: horizontal waterproofing membrane (horisontalt fuktsperre) at slab level or at sill plate level for timber frame

### Drainage (Drenering)
Correct drainage sequence from outside foundation wall:
1. Drainage membrane on foundation wall (drenerende plate)
2. Filter fabric (filterduk)
3. Drainage pipe (drensrør) Ø 100 mm at foundation base level, minimum 1:200 fall to daylight or sump
4. Crushed stone fill (pukk) 200–300 mm
5. Backfill

### Frost Depth (Telehiv)
| Region | Design frost depth (tele) |
|---|---|
| Oslo / coastal Østlandet | 1.0–1.5 m |
| Inland Østlandet / Hedmark | 1.5–2.0 m |
| Trondheim area | 1.2–1.8 m |
| Bergen / mild coast | 0.5–1.0 m |
| Northern Norway inland | 2.0–3.0 m+ |

All footings must bear below the frost depth (frostfri dybde) or be frost-protected with perimeter insulation (frostsikring med isolasjon) per SINTEF Byggdetaljblad 520-series.

---

## Interaction with Other Skills
- **Structural Engineering**: SINTEF details provide connection and construction details that structural drawings must coordinate with.
- **TEK17**: SINTEF Byggdetaljblad document the accepted methods of achieving TEK17 U-value, airtightness, fire, and moisture requirements.
- **Historic Preservation**: SINTEF publishes specific guidance for moisture management in old timber buildings (eldre trehus). Standard modern solutions often cause more damage on historic structures than they solve.
- **Construction Execution**: SINTEF details define the sequence-sensitive steps — vapour retarder installation timing, concrete curing before floor covering, moisture content checks on timber.

---

*Authority: SINTEF Byggforsk Byggdetaljblad (Byggforskserien), NS 3700 (Passivhus), NS 1501 (Vapour retarders)*
*Last reviewed: 2026-07-26*
