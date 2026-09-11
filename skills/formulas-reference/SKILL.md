---
name: formulas-reference
description: On-demand illustrative beam formulas and load-reference checks for structural calculations. Verify sources, units, Norwegian annexes, and applicability before design use; not a permit reference.
license: Proprietary
triggers: [calculate, beam sizing, deflection, moment, shear, load combination, ULS, SLS, formula, kN, kN/m, section properties, capacity check, utilization, span calculation, load takedown, design value, f_yk, f_ck, f_d, E modulus, Ixx, W_pl]
load_with: [structural-engineering]
safety_level: medium
load_priority: on-demand
status: unreviewed
---

# Formulas Reference: Illustrative, Source Verification Required

> **NOT A PROJECT DESIGN BASIS.** Remaining tables, examples, clause/table
> references, editions, historical grade equivalences, material factors, and
> deflection limits have **not been comprehensively verified**. Treat them as
> illustrative/unverified lookup prompts, not authoritative design values.
> Verify the applicable NS/NS-EN edition and Norwegian National Annex, actual
> material/product/condition, design situation, factors, and source clauses
> before use. If the source is unavailable, leave the value unverified rather
> than guess. A citation or arithmetic result is not professional verification.

## Trust Boundary

Use on demand for bounded explanations and source-checked calculations with
explicit inputs, units, assumptions, and limits. Follow the structural input
lock and [routing evidence gates](../routing/SKILL.md#evidence-and-bim-gates).
Missing safety-critical evidence blocks design/installed-member adequacy claims,
not a clearly labeled concept explanation. Qualified structural review of the
actual design basis is needed before relying on a solution; this reference
does not authorize construction or establish whole-member or building safety.

**Unit convention for the beam formulas below:** use one coherent system per
calculation. With force in N, length in mm, $E$ in N/mm² and $I$ in mm⁴, use
$q$ in N/mm and $P,V$ in N; results are $M$ in N·mm, $\delta$ in mm, and
$\theta$ in radians. Convert kN to N and m to mm before substitution in that
system. Alternatively, kN/m and m give moments in kN·m and shear in kN;
do not combine that system with unconverted N/mm² and mm⁴. Stress calculations
with section modulus in mm³ require moment in N·mm. These are idealized
linear-elastic beam models; verify supports, loading, stiffness assumptions,
and whether shear deformation or other effects need separate treatment.

**Optional web cross-check:** when using Beam Calculator, consult the
[resource review and unit cautions](../structural-engineering/references/beam-calculator.md).
The formula display omits conversion factors in its numeric substitutions;
rebuild them in coherent units. Its L/360 helper is not a Norwegian code limit,
and its indicative timber Fy/Fu labels are not verified design properties.
Use an independent calculation, not two pages sharing the same solver, as
the arithmetic cross-check. No calculator integration is installed by this link.

**Local numerical implementation:** use the
[tested beam calculator procedure](../structural-engineering/references/local-beam-calculator.md)
for the supported simple-span/cantilever point-load and UDL cases. It performs
unit conversion and returns response, not Norwegian design compliance. Read the
[Norwegian design-basis register](../structural-engineering/references/norwegian-design-basis.md)
for source-checked public requirements and numerical provisions still unverified.

---

> For historical materials (1920s-1960s concrete, steel, timber grades and load standards), see [references/historical-materials.md](references/historical-materials.md)

### 1.1 Simply Supported Beam — Uniformly Distributed Load (q)

**Source to verify:** Roark & Young, uniform-load simply supported case;
check the table/case in the actual edition rather than relying on legacy numbering.

| Response magnitude | Formula | Location |
|---|---|---|
| Maximum moment | $M = qL^2/8$ | Midspan |
| Maximum deflection | $\delta = 5qL^4/(384EI)$ | Midspan |
| Maximum shear | $V = qL/2$ | Support |
| Slope | $\theta = qL^3/(24EI)$ | Support |

**Variables for §§1.1–1.4:** $q$ = line load [N/mm], $P$ = point load [N],
$L$ = span [mm], $E$ = elastic modulus [N/mm²], $I$ = second moment of area
[mm⁴]. Results: $M$ [N·mm], $V$ [N], $\delta$ [mm], $\theta$ [radians].
Assume the stated ideal supports and constant $EI$; the unit/applicability
checks above apply to every case. Magnitudes do not specify a sign convention.

### 1.2 Simply Supported Beam — Central Point Load (P)

**Source to verify:** Roark & Young, central-point-load simply supported case.

| Response magnitude | Formula | Location |
|---|---|---|
| Maximum moment | $M = PL/4$ | Midspan |
| Maximum deflection | $\delta = PL^3/(48EI)$ | Midspan |
| Maximum shear | $V = P/2$ | Either half-span |

### 1.3 Cantilever Beam — Distributed Load (fixed end to free end)

**Source to verify:** Roark & Young, full-span uniform-load cantilever case.

| Response magnitude | Formula | Location |
|---|---|---|
| Maximum moment | $M = qL^2/2$ | Fixed support |
| Maximum deflection | $\delta = qL^4/(8EI)$ | Free end |
| Maximum shear | $V = qL$ | Fixed support |

### 1.4 Cantilever Beam — End Load (at free end)

**Source to verify:** Roark & Young, free-end-point-load cantilever case.

| Response magnitude | Formula | Location |
|---|---|---|
| Maximum moment | $M = PL$ | Fixed support |
| Maximum deflection | $\delta = PL^3/(3EI)$ | Free end |

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

**Source to verify:** Applicable NS-EN 1993-1-1 edition and product standard;
strength depends on product, grade, and thickness. The examples are not a
universal yield-strength assignment.

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

## 2. LOAD DEFINITIONS (NS-EN 1991 and Applicable Norwegian National Annexes)

### 2.1 ULS Load Combinations

**Source to verify:** NS-EN 1990 and its applicable Norwegian National Annex,
together with the relevant action and material standards. TEK17 is not a
National Annex or a substitute for the combination rules.

Identify the design situation and limit state, favorable/unfavorable permanent
actions, each relevant leading variable action, accompanying actions, and
compatible load arrangements. Source each partial factor $\gamma$ and
combination factor $\psi_0$, $\psi_1$, or $\psi_2$ from the applicable provisions.
Do not assume a universal permanent-plus-one-variable formula, omit snow merely
because imposed load leads, or multiply ground snow by one factor as the whole
roof design. $E_d$ is the resulting design **effect of actions**, not necessarily
an area load. Record the verified combination and analysis model used to obtain it.

### 2.2 Snow Load (NS-EN 1991-1-3 and Norwegian National Annex)

**Source-specific procedure:** verify the applicable NS-EN 1991-1-3 edition,
Norwegian National Annex, ground-load provisions, and roof load cases. The
former purported TEK17 zoning table is withdrawn; no replacement zones or
coefficient values are asserted here.

1. Establish site location/municipality and altitude from identified evidence.
  Source characteristic **ground** snow load $s_k$ [kN/m²] and any altitude
  adjustment or special local provisions from the applicable Norwegian NA.
  Record edition, clause/table, location, altitude, and derivation. A city
  example, roof pitch, or geographical guess does not establish $s_k$.
2. For roof cases to which the standard expression applies, derive the
  characteristic roof snow action, not the factored ULS design action:

  $$s = \mu_i C_e C_t s_k$$

  Here $s$ is roof snow load [kN/m²] on the horizontal projected-area basis
  specified by the standard; $\mu_i$ is the roof shape coefficient for case
  $i$, $C_e$ the exposure coefficient, and $C_t$ the thermal coefficient.
  These coefficients are dimensionless and must be sourced and justified.
  $\psi$ denotes a combination factor, **not** a roof shape coefficient.
3. Verify applicability to the actual roof geometry and design situation.
  Check relevant balanced/unbalanced arrangements, drift and accumulation,
  adjacent roofs, obstructions/parapets, snow retention/guards, sliding and
  local effects. Pitch alone does not justify zero load or full sliding.
  Where additional or exceptional cases apply, use their verified provisions
  rather than force them into the expression above.
4. Keep ground load, roof load, area basis, and tributary-area conversion
  distinct. Apply verified NS-EN 1990/NA combinations for ULS and the relevant
  SLS assessment after establishing the roof actions and load cases. Do not
  invent coefficients, combination factors, or unsupported omissions.

Unresolved location, altitude, coefficient applicability, or arrangement stays
explicitly unverified and prevents a project design snow-load claim.

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

**Source to verify:** Applicable NS-EN 1991-1-1 Annex A and actual product data.
The retained rows below are **illustrative/unverified**, not sourced project
inputs. Unit weight $\gamma_{\mathrm{mat}}$ [kN/m³] is not mass density
$\rho$ [kg/m³] or a dimensionless partial factor.

| Material | Unit weight γ_mat [kN/m³] | Area load per mm of uniform thickness | Reference to verify |
|----------|-----------|---|---|
| Concrete | 25 | 0.025 kN/m² per mm | EN 1991-1-1, A.1 |
| Timber (softwood) | 4–5 | — | EN 1991-1-1, A.1 |
| Steel | 78.5 | — | EN 1991-1-1, A.1 |
| Brick/Masonry | 18–20 | 0.018–0.020 kN/m² per mm | EN 1991-1-1, A.1 |

**Tiled roofs (L001):** The former ceramic-tile row mixed area-load units with
a volumetric heading and is removed, not corrected to a guessed value. Obtain
manufacturer mass per tile and installed coverage (tiles/m², including the
specified overlap), or a documented installed mass per area. Record product,
source/revision, coverage, and whether area means sloping roof or horizontal
projection. Do not model profiled/overlapping tiles as a solid uniform layer
without supporting product data.

**Conversions, not material assumptions:**

$$m_A\ [\mathrm{kg/m^2}] = m_{\mathrm{tile}}\ [\mathrm{kg/tile}]
× n\ [\mathrm{tiles/m^2}]$$

$$g_k\ [\mathrm{kN/m^2}] =
\frac{m_A\ [\mathrm{kg/m^2}]\,g\ [\mathrm{m/s^2}]}{1000}$$

Here $g = 9.80665\ \mathrm{m/s^2}$ is standard gravitational acceleration,
not a material load value. $g_k$ denotes characteristic permanent area load.
For a genuinely uniform layer of thickness $t$ in meters:

$$m_A = \rho t, \qquad
\gamma_{\mathrm{mat}} = \frac{\rho g}{1000}, \qquad
g_k = \gamma_{\mathrm{mat}}t$$

Do not multiply an already area-based mass/load by thickness. For a uniform
pitched plane and vertical dead load, $g_{k,\mathrm{horizontal}} =
g_{k,\mathrm{slope}}/\cos\alpha$, where $\alpha$ is pitch from horizontal;
do not reconvert loads already based on horizontal projection.

Record the full in-scope roof assembly, including covering, battens, structure,
insulation, ceilings, services, and other permanent components, in the locked
takeoff. Source each component and area basis, avoid double counting, and mark
missing components **unverified, not zero**. Neither age nor tile type supplies
a default roof total. Obtain the responsible structural designer's verification
of the assembly and takeoff before design use.

---

## 3. MATERIAL PROPERTIES & STRESS EXAMPLES (UNVERIFIED)

### 3.1 Steel (Norwegian/Eurocode Standards)

**Common beam profiles: HEB 180, HEA 180, IPE 200, etc.**

| Property | S235 (E235) | S355 (E355) | Unit | Note |
|----------|-------------|------------|------|------|
| **Yield strength f_y** | 235 | 355 | MPa | Characteristic |
| **Design resistance basis** | Verify applicable resistance expression | Verify applicable resistance expression | — | Source the relevant partial factor; no universal factor given |
| **Young's modulus E** | 210,000 | 210,000 | MPa | Both steel types |
| **Shear modulus G** | 81,000 | 81,000 | MPa | — |
| **Density ρ** | 7850 | 7850 | kg/m³ | For weight calc |

**Bending stress (beam):**
```
σ = M / W   [MPa]  where W = second moment / distance to extreme fiber [mm³]

Stress comparison η = σ / f_d (only for a verified applicable stress criterion)
```

Passing one stress comparison does not establish safety. Verify section class,
stability, interactions, restraints, connections, supports, and serviceability
as applicable, using the appropriate design resistance and factors.

**Shear stress:**
```
τ = V × S / (I × t_w)   [MPa]

where:
  V = shear force [N] for I, S, and t_w in mm-based units
  S = first moment of area above neutral axis [mm³]
  I = second moment [mm⁴]
  t_w = web thickness [mm]
  
Elastic stress comparison only: τ ≤ f_d / √3, where applicable and verified
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
  k_mod = sourced modification factor for service class and load duration
  γ_M = applicable sourced material partial factor
```

Verify the material/product standard, grade, applicable NS-EN 1995-1-1/NA
provisions, and any further factors/checks. No default factors are approved here.

**Deflection limit (SLS — Serviceability):**
```
Illustrative ratios only, not acceptance criteria:
L / 300
L / 200

For 3.5m span:
  L/300: δ_max = 3500 / 300 = 11.7 mm
  L/200: δ_max = 3500 / 200 = 17.5 mm
```

**Creep effect on timber deflection:** Verify the applicable timber serviceability
method, action-by-action contributions, service class, load duration, creep
factor $k_{\mathrm{def}}$, and relevant combination factors. Do not apply a
single assumed $\psi$ or blanket multiplier to all initial deflection. Distinguish
instantaneous, final, and net final deflection and any specified precamber.

### 3.3 Concrete — Norwegian Standards

| Strength | f_ck [MPa] | f_d [MPa] | E_mean [GPa] | Unit weight γ_mat [kN/m³] | Age |
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

## 4. LOAD COMBINATION VERIFICATION (NS-EN 1990 and Norwegian NA)

### 4.1 Ultimate Limit State (ULS — Bruddgrense)

Use the verified design situation, limit-state expressions, partial factors,
leading/accompanying variable actions, and arrangements described in §2.1.
Check each relevant leading action and governing arrangement. Snow, imposed
load, and wind are not automatically mutually exclusive. Do not eliminate an
accompanying action without a verified applicable rule. Convert area loads to
member loads with the actual load path/tributary area before member analysis.

### 4.2 Serviceability Limit State (SLS — Bruksgrensetilstand)

Characteristic (sometimes called rare), frequent, and quasi-permanent
combinations are distinct, not interchangeable names. Select the combination
appropriate to the response being assessed and source its coefficients from
the applicable NS-EN 1990/NA provisions. Include material-specific long-term
effects where relevant. Record the verified expression and acceptance criteria;
no universal SLS factors or deflection limits are supplied here.

---

> Historical worked example, not revalidated by this edit: [references/worked-examples.md](references/worked-examples.md).
> Do not reuse its project inputs, factors, or conclusions without independent source checks.

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

## 7. DEFLECTION RATIOS (ILLUSTRATIVE, NOT DESIGN LIMITS)

| Example ratio | Meaning only |
|---|---|
| L/200 | Span divided by 200 |
| L/300 | Span divided by 300 |
| L/150 | Span divided by 150 |
| L/500 | Span divided by 500 |

No structure-type assignment or acceptance limit is verified by this table.
Establish the applicable standard/NA and project performance criteria, response
definition (instantaneous/final/net), finishes/equipment sensitivity, vibration,
and load combination. A ULS partial factor is not an SLS deflection criterion.

---

## 8. QUICK CALC CHECKLIST FOR BEAM ASSESSMENT

**When evaluating an existing beam:**

1. **Identify:**
   - [ ] Material (steel: grade S235 or S355? timber: GL32h or GL28h? concrete: C16/20 or C25/30?)
   - [ ] Profile (HEB 180? IPE? GL 220×380?)
   - [ ] Second moment I (from tables or calc: I = b×d³/12 for rect.)

2. **Load:**
  - [ ] Sourced assembly dead-load takeoff, units, area basis, missing components
  - [ ] Site location/altitude and sourced NS-EN 1991-1-3 Norwegian NA ground load s_k
  - [ ] Roof snow s = μ_i C_e C_t s_k where applicable; sourced coefficients, drift/retention and relevant arrangements
  - [ ] Actual imposed-load category and applicable NS-EN 1991-1-1/NA values verified
  - [ ] Applicable ULS/SLS combinations and factors verified; area-to-line-load conversion and load path documented

3. **Moment & Shear:**
   - [ ] M_max = (q_d × L²) / 8  (simple span, uniform load)
   - [ ] V_max = (q_d × L) / 2

4. **Capacity Check (ULS):**
  - [ ] Applicable bending/shear resistance expressions, material factors, units, and section class verified
  - [ ] Stability, interactions, restraints, connections, and supports assessed; one stress ratio is not a safety finding

5. **Deflection (SLS):**
   - [ ] δ_SLS = (5 × q_SLS × L⁴) / (384 × E × I)
  - [ ] Applicable response definition, long-term effects, and sourced standard/project acceptance criteria verified

6. **Red Flags:**
   - [ ] Corrosion (steel) / moisture (timber)?
   - [ ] Cracks in concrete or distress?
   - [ ] Visible deflection (sagging)?
   - [ ] Missing bracing / lateral instability?
   - [ ] Connection details adequate?

---

**Load only when relevant. Verify original sources before reliance. This is not
complete or certified engineering knowledge.**

*Last reviewed: 2026-09-06. Scoped text corrections only; remaining references
and engineering tables are not comprehensively verified. Guard behavior unvalidated.*
