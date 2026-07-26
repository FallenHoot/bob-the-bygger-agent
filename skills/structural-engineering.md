---
name: structural-engineering
description: Load paths, beam sizing, deflection, connections, foundation assessment, and structural failure diagnosis for Norwegian residential and light commercial construction (Eurocodes + Norwegian NA).
triggers: [beam, bjelke, load, last, load bearing, bærevegg, wall removal, vegg, column, søyle, foundation, fundament, deflection, nedbøyning, structural, konstruksjon, snow load, snølast, wind load, vindlast, moment, shear, capacity, kapasitet, glulam, limtre, timber, stål, reinforcement, armering, seismic, settlement, setning, rot, råte at bearing]
load_with: [building-code-tek17]
safety_level: high
---

# Skill: Structural Engineering

## Domain
Load path analysis, beam and column sizing, deflection limits, connection design, foundation assessment, and structural failure diagnosis — applied to Norwegian residential and light commercial construction.

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

## Interaction with Other Skills
- **TEK17**: All structural design must comply with §10 (Konstruksjonssikkerhet). Structural engineering calculations are required in the building permit application (søknad).
- **SINTEF Byggforsk**: Execution details for timber connections, moisture protection at foundations, and wood-concrete interfaces.
- **Historic Preservation**: Structural interventions on SEFRAK-registered buildings require antikvarisk assessment before introducing new loads or removing original structure.

---

*Authority: NS-EN 1990, NS-EN 1991 (Eurocodes), NS-EN 1993 (Steel), NS-EN 1995 (Timber), TEK17 §10*
*Last reviewed: 2026-07-26*
