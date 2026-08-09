---
name: formulas-reference
description: Beam bending formulas, Eurocode load combinations, Eurocode material design values, TEK17 load tables, and deflection limits. Load only when performing structural calculations — beam sizing, deflection checks, load takedowns, or material capacity verification. Do NOT load for regulatory or permit questions.
license: Proprietary
metadata:
  triggers: calculate, beam sizing, deflection, moment, shear, load combination, ULS, SLS, formula, kN, kN/m, section properties, capacity check, utilization, span calculation, load takedown, design value, f_yk, f_ck, f_d, E modulus, Ixx, W_pl
  load_with: structural-engineering
  safety_level: medium
  load_priority: on-demand
---

# Formulas Reference — Authoritative Sources

**All formulas cite their source standard. No custom interpretations. Working memory. Includes modern (TEK17/Eurocode) and historical (1920s–1960s) Norwegian standards.**

---

> For historical materials (1920s-1960s concrete, steel, timber grades and load standards), see [references/historical-materials.md](references/historical-materials.md)

### 1.1 Simply Supported Beam — Uniformly Distributed Load (q)

**Source: Roark & Young, Table 8, Case 1a**

**Max Bending Moment (center):**
```
M = (q × L²) / 8
```
- Reference: Roark Table 8.1, verified EN 1993-1-1 Annex B
- Applicable for linear elastic analysis

**Max Deflection (center):**
```
δ = (5 × q × L⁴) / (384 × E × I)
```
- Reference: Roark Table 8.1
- Valid for linear elastic behavior

**Max Shear Force (at support):**
```
V = (q × L) / 2
```
- Reference: Roark, basic equilibrium

**Slope at Support:**
```
θ = (q × L³) / (24 × E × I)
```
- Reference: Roark Table 8.1

**Variables:**
- q = distributed load [kN/m]
- L = span [m]
- E = modulus of elasticity [MPa or N/mm²]
- I = second moment of inertia [mm⁴]
- δ = deflection [mm]
- θ = slope/rotation [radians]
- V = shear force [kN]

### 1.2 Simply Supported Beam — Central Point Load (P)

**Source: Roark & Young, Table 8, Case 5**

**Max Bending Moment (center):**
```
M = (P × L) / 4
```
- Reference: Roark Table 8.5

**Max Deflection (center):**
```
δ = (P × L³) / (48 × E × I)
```
- Reference: Roark Table 8.5

**Max Shear Force:**
```
V = P / 2
```
- Reference: Equilibrium

**Variables:**
- P = point load [kN]
- L = span [m]
- E = modulus of elasticity [MPa]
- I = second moment of inertia [mm⁴]

### 1.3 Cantilever Beam — Distributed Load (fixed end to free end)

**Source: Roark & Young, Table 9, Case 1**

**Max Bending Moment (at fixed support):**
```
M = (q × L²) / 2
```
- Reference: Roark Table 9.1

**Max Deflection (at free end):**
```
δ = (q × L⁴) / (8 × E × I)
```
- Reference: Roark Table 9.1

**Max Shear Force:**
```
V = q × L
```
- Reference: Equilibrium

**Variables:**
- q = distributed load [kN/m]
- L = span [m]
- E = modulus of elasticity [MPa]
- I = second moment of inertia [mm⁴]

### 1.4 Cantilever Beam — End Load (at free end)

**Source: Roark & Young, Table 9, Case 5**

**Max Bending Moment (at fixed support):**
```
M = P × L
```
- Reference: Roark Table 9.5

**Max Deflection (at free end):**
```
δ = (P × L³) / (3 × E × I)
```
- Reference: Roark Table 9.5

**Variables:**
- P = point load [kN]
- L = span [m]
- E = modulus of elasticity [MPa]
- I = second moment of inertia [mm⁴]

---

## 2. MATERIAL PROPERTIES & DESIGN VALUES

### 2.1 Steel (EN 1993-1-1, Section 3.2)

**Modulus of Elasticity:**
- $E = 210,000$ MPa (all grades)
- $G = 81,000$ MPa (shear modulus)

**Source: EN 1993-1-1:2005, Table 3.1**

**Yield Strength (examples):**
- S235: $f_y = 235$ MPa
- S275: $f_y = 275$ MPa
- S355: $f_y = 355$ MPa

**Source: EN 1993-1-1, Table 3.1 & NS 3940**

### 2.2 Concrete (EN 1992-1-1, Section 3.1)

**Modulus of Elasticity (secant):**
```
E_cm = 22 × (f_cm / 10)^0.3  [GPa]

where f_cm = f_ck + 8 MPa (mean compressive strength)
```

**Source: EN 1992-1-1:2004, Section 3.1.3, Table 3.1**

**Example (C30/37):**
- $f_{ck} = 30$ MPa (characteristic)
- $f_{cm} = 38$ MPa (mean)
- $E_{cm} = 33,000$ MPa

### 2.3 Timber (EN 1995-1-1, Section 3.2)

**Modulus of Elasticity (parallel to grain):**
- Softwood (C24): $E_{0,m} = 11,000$ MPa
- Softwood (C30): $E_{0,m} = 12,000$ MPa
- Hardwood (D30): $E_{0,m} = 10,000$ MPa

**Source: EN 1995-1-1:2004, Table 3.3**

**Bending Strength (characteristic):**
- C24: $f_{m,k} = 24$ MPa
- C30: $f_{m,k} = 30$ MPa

**Source: EN 1995-1-1, Table 3.3**

---

## 2. LOAD DEFINITIONS (EN 1991 + TEK17 National Annex)

### 2.1 ULS Load Combinations

**Source: EN 1990:2002 + A1:2005 — Section 6.4.3 (Combination rules)**
**Norwegian implementation: TEK17 Section 7 + National annex to EN 1991**

```
Standard combination (Permanent + Variable):
E_d = 1.35 × G_k + 1.50 × (Q_k or S_k)

where:
  E_d = design effect (ULS)
  G_k = characteristic permanent action (dead load)
  Q_k = characteristic variable action (live load)
  S_k = characteristic snow load
  1.35 = partial safety factor for permanent actions (EN 1990)
  1.50 = partial safety factor for leading variable actions (EN 1990)
```

**Reference:** EN 1990:2002, Table 6.2a (STR/GEO combinations)

### 2.2 Snow Load (EN 1991-1-3 + TEK17 National Annex)

**Source: EN 1991-1-3 — Section 5 (Snow loads on roofs)**

**Norway divided into zones (TEK17 Table 7.1):**

| Zone | Characteristic Snow Load s_k | Region Examples | Reference |
|------|-------|---|---|
| 1 | 1.5–2.0 kN/m² | Coastal (Oslo, Bergen area) | TEK17 Table 7.1 |
| 2 | 2.5–3.0 kN/m² | Østlandet interior (Lilehammer, inland) | TEK17 Table 7.1 |
| 3 | 3.5–4.5 kN/m² | Mountains (>500m), north (>60°N) | TEK17 Table 7.1 |
| 4 | 5.0+ kN/m² | High mountains (>1000m) | TEK17 Table 7.1 |

**Design snow load (ULS):**
```
s_d = γ × s_k  (EN 1990, γ = 1.50)
```

**Roof shape coefficient ψ:**
```
Source: EN 1991-1-3, Section 5.3.3

Pitch 0°–30°: ψ = 0.8 (uniform)
Pitch 30°–60°: ψ = 0.8 × (60 − α) / 30  (linear)
Pitch >60°: ψ = 0  (snow slides off)
```

**Reference:** EN 1991-1-3:2003, Section 5.3

### 2.3 Live Load / Imposed Load (EN 1991-1-1)

**Source: EN 1991-1-1:2002 — Table 6.1 (Category A–D loads)**

| Occupancy | q_k | Load Category | Reference |
|-----------|-----|---|---|
| Residential (dwellings) | 1.5–2.0 kN/m² | A | EN 1991-1-1, Table 6.1 |
| Office / Commercial | 2.5–3.0 kN/m² | B | EN 1991-1-1, Table 6.1 |
| Accessible attic (storage) | 0.5–1.0 kN/m² | A | EN 1991-1-1, Table 6.1 |
| Roof (not accessible) | 0.4–0.6 kN/m² | H | EN 1991-1-1, Table 6.1 |

**Reference:** EN 1991-1-1:2002, Table 6.1 and National Annex

### 2.4 Dead Load Material Properties

**Source: EN 1991-1-1 — Annex A (Unit weights of materials)**

| Material | ρ [kN/m³] | Per mm of thickness | Reference |
|----------|-----------|---|---|
| Ceramic roof tile | 15–20 kN/m² (per layer) | ~0.075 kN/m² per mm | EN 1991-1-1, A.1 |
| Concrete | 25 | 0.025 kN/m² per mm | EN 1991-1-1, A.1 |
| Timber (softwood) | 4–5 | — | EN 1991-1-1, A.1 |
| Steel | 78.5 | — | EN 1991-1-1, A.1 |
| Brick/Masonry | 18–20 | 0.018–0.020 kN/m² per mm | EN 1991-1-1, A.1 |

**Reference:** EN 1991-1-1:2002, Annex A

---

## 3. MATERIAL PROPERTIES & ALLOWABLE STRESSES

### 3.1 Steel (Norwegian/Eurocode Standards)

**Common beam profiles: HEB 180, HEA 180, IPE 200, etc.**

| Property | S235 (E235) | S355 (E355) | Unit | Note |
|----------|-------------|------------|------|------|
| **Yield strength f_y** | 235 | 355 | MPa | Characteristic |
| **Design yield f_d** | 235/1.15 ≈ **204** | 355/1.15 ≈ **309** | MPa | ULS partial safety 1.15 |
| **Young's modulus E** | 210,000 | 210,000 | MPa | Both steel types |
| **Shear modulus G** | 81,000 | 81,000 | MPa | — |
| **Density ρ** | 7850 | 7850 | kg/m³ | For weight calc |

**Bending stress (beam):**
```
σ = M / W   [MPa]  where W = second moment / distance to extreme fiber [mm³]

Utilization ratio η = σ / f_d  ≤ 1.0 (safe)
```

**Shear stress:**
```
τ = V × S / (I × t_w)   [MPa]

where:
  V = shear force [kN]
  S = first moment of area above neutral axis [mm³]
  I = second moment [mm⁴]
  t_w = web thickness [mm]
  
Allowable: τ ≤ f_d / √3  ≈ 0.577 × f_d
```

### 3.2 Timber (Glulam & Solid Sawn) — Norwegian/Eurocode

**Common glulam grades:**

| Grade | Bending f_m,k [MPa] | Compression f_c,0,k [MPa] | E_mean [MPa] | Density ρ [kg/m³] | Typical Use |
|-------|---|---|---|---|---|
| **GL32h** | 32 | 27 | 14,600 | 400–450 | Standard, good strength |
| **GL28h** | 28 | 24 | 13,700 | 380–420 | Economy grade |
| **GL36h** | 36 | 30 | 15,600 | 420–480 | Higher strength |

**Design bending stress (ULS):**
```
f_d = f_m,k × k_mod / γ_M

where:
  k_mod = modification factor (moisture + duration class, typically 0.8–1.0)
  γ_M = 1.35 (partial safety, glulam)
  
Example GL32h, load duration class Medium (k_mod = 0.9):
  f_d = 32 × 0.9 / 1.35 ≈ 21.3 MPa
```

**Deflection limit (SLS — Serviceability):**
```
δ_max ≤ L / 300  (typical residential)
δ_max ≤ L / 200  (can be used if approved)

For 3.5m span:
  L/300: δ_max = 3500 / 300 = 11.7 mm
  L/200: δ_max = 3500 / 200 = 17.5 mm
```

**Creep effect on timber deflection:**
```
δ_total = δ_initial + δ_creep

δ_creep = δ_initial × ψ × k_def

where:
  ψ = reduction factor for quasi-permanent load (~0.6)
  k_def = creep coefficient (glulam ≈ 0.6–0.8 depending on moisture class)
  
Typical: δ_final ≈ 1.5–1.8 × δ_initial (over time)
```

### 3.3 Concrete — Norwegian Standards

| Strength | f_ck [MPa] | f_d [MPa] | E_mean [GPa] | ρ [kN/m³] | Age |
|----------|-----------|----------|--------------|-----------|-----|
| **B200 (1960s Norwegian)** | ≈ 16 | 16/1.5 ≈ **10.7** | 28–30 | 24 | 28 days |
| **C16/20 (modern equiv.)** | 16 | 16/1.5 ≈ 10.7 | 28–30 | 24 | 28 days |
| **C25/30** | 25 | 25/1.5 ≈ 16.7 | 31 | 24 | 28 days |

**Reinforcement:**
- **H-40 (1960s Norway)** ≈ B400 (modern): f_y ≈ 400 MPa
- **Design yield (ULS):** f_d = 400 / 1.15 ≈ 348 MPa

**Concrete carbonation (durability):**
```
Depth of carbonation over time:
  x_c = √(D_c × t)   [mm]

where:
  D_c = carbonation diffusion coefficient (typ. 1–5 mm²/year for outdoor concrete)
  t = time [years]
  
1964 construction (62 years in 2026):
  x_c ≈ √(3 × 62) ≈ 13.6 mm

B200 rebar cover (1960s std): typically 15 mm
→ Risk: marginal cover if D_c is high (outdoor exposure)
```

---

## 4. TEK17 LOAD COMBINATIONS (Simplified Reference)

### 4.1 Ultimate Limit State (ULS — Bruddgrense)

**Permanent + Snow (snow governs):**
```
E_d = 1.35 × G_k + 1.50 × S_k + (0.7 × Q_k,other)
```

**Permanent + Live (live governs):**
```
E_d = 1.35 × G_k + 1.50 × Q_k + (0 × S_k)  [snow eliminated]
```

**Permanent + Wind:**
```
E_d = 1.35 × G_k + 1.50 × W_k
```

### 4.2 Serviceability Limit State (SLS — Bruksgrensetilstand)

**Rare (quasi-permanent, long-term deflection):**
```
E_ser = G_k + ψ₂ × Q_k  [ψ₂ ≈ 0.3–0.6 depending on load]
```

---

> For a worked beam example (3.5 m kitchen beam, hip roof, Lørenskog), see [references/worked-examples.md](references/worked-examples.md)

## 6. NORWEGIAN BUILDING TERMINOLOGY (Quick Reference)

| Norwegian | English | Common Use |
|-----------|---------|-----------|
| **Egenvekt** | Dead load | g_k |
| **Nyttelast** | Live load, imposed load | q_k |
| **Snølast** | Snow load | S_k or s_k |
| **Vindlast** | Wind load | W_k |
| **Bruddgrense** | Ultimate limit state (ULS) | Design calculations |
| **Bruksgrensetilstand** | Serviceability limit state (SLS) | Deflection, cracking |
| **Senteravstand** | Spacing, center-to-center | c/c distance |
| **Opplagringstype** | Support type | Fixed, pinned, roller |
| **Kapasitetsutnyttelse** | Utilization ratio | η = demand / capacity |
| **Bærende** | Load-bearing | Structural member |
| **Ikke-bærende** | Non-load-bearing | Infill, partition |

---

## 7. DEFLECTION LIMIT QUICK REFERENCE

| Structure Type | SLS Limit | Note | ULS Safety Factor |
|---|---|---|---|
| **Roof (not human traffic)** | L/200 | Can deflect more | γ = 1.50 |
| **Floor (residential)** | L/300 | Stricter for comfort | γ = 1.50 |
| **Cantilever** | L/150 | More stringent | γ = 1.50 |
| **Beam under machinery** | L/500 | Precision required | γ = 1.50 |

---

## 8. QUICK CALC CHECKLIST FOR BEAM ASSESSMENT

**When evaluating an existing beam:**

1. **Identify:**
   - [ ] Material (steel: grade S235 or S355? timber: GL32h or GL28h? concrete: C16/20 or C25/30?)
   - [ ] Profile (HEB 180? IPE? GL 220×380?)
   - [ ] Second moment I (from tables or calc: I = b×d³/12 for rect.)

2. **Load:**
   - [ ] Dead load g_k (material weights, structure above)
   - [ ] Snow zone (1–4 Norway) → s_k
   - [ ] Live load q_k (attic: 0.5–1.5 kN/m²?)
   - [ ] Design load q_d = 1.35×g_k + 1.50×(s_k or q_k)

3. **Moment & Shear:**
   - [ ] M_max = (q_d × L²) / 8  (simple span, uniform load)
   - [ ] V_max = (q_d × L) / 2

4. **Capacity Check (ULS):**
   - [ ] Bending: σ = M / W ≤ f_d  (utilization η)
   - [ ] Shear: τ = V × S / (I × t_w) ≤ f_v,d

5. **Deflection (SLS):**
   - [ ] δ_SLS = (5 × q_SLS × L⁴) / (384 × E × I)
   - [ ] Limit: δ_SLS ≤ L/300 (or L/200 if approved)

6. **Red Flags:**
   - [ ] Corrosion (steel) / moisture (timber)?
   - [ ] Cracks in concrete or distress?
   - [ ] Visible deflection (sagging)?
   - [ ] Missing bracing / lateral instability?
   - [ ] Connection details adequate?

---

**This is complete embedded knowledge. Load on every session. Do not look up.**
