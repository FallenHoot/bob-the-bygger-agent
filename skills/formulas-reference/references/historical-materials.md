# Historical Construction Materials — Norway (1920s–1960s)

**Part of the formulas-reference skill. Referenced from SKILL.md.**

## 0. HISTORICAL STANDARDS & MATERIALS (1920s–1960s Norway)

**Reference era:** NB 8 (older Oslo Building Code), DS 800 (Danish Standards adopted in Norway), DIN standards (German influence pre-WWII)

### 0.1 Historical Concrete Grades (1920s–1960s)

**Norwegian designation: B-grades**

| Grade | f_ck [MPa] | f_d [MPa] | E_mean [GPa] | Typical Use | Age | Notes |
|-------|-----------|----------|--------------|------------|-----|-------|
| **B150** | ~12 | 12/1.5 ≈ **8** | 26–28 | Very early (pre-1940) | 28 days | Rare; mostly laboratory |
| **B200** | ~16 | 16/1.5 ≈ **10.7** | 28–30 | Common (1940s–1970s) | 28 days | Standard post-war residential |
| **B250** | ~20 | 20/1.5 ≈ **13.3** | 30–32 | Mid-strength (1950s–1970s) | 28 days | Commercial/structural |
| **B300** | ~24 | 24/1.5 ≈ **16** | 32–34 | Demanding (1960s+) | 28 days | Equivalent modern C25/30 |

**Relationship to modern grades:**
- B200 ≈ C16/20
- B250 ≈ C20/25
- B300 ≈ C25/30

**Source:** NB 8 (Oslo Building Code), DS 800, SINTEF historical records

### 0.2 Historical Steel Grades (1920s–1960s)

**Norwegian/Scandinavian designation: E-grades (Engelsk = English/Bessemer)**

| Grade | f_y [MPa] | Design f_d [MPa] | E [MPa] | Typical Use | Notes |
|-------|-----------|-----------------|---------|------------|-------|
| **E200 (mild)** | 200 | 200/1.8 ≈ **111** | 200,000 | Early structures (pre-1930) | Very ductile; rare |
| **E235 (E-stål)** | 235 | 235/1.8 ≈ **131** | 210,000 | Standard (1930s–1960s) | Equivalent modern S235 |
| **E275** | 275 | 275/1.8 ≈ **153** | 210,000 | Higher strength (1950s+) | — |
| **H-40 (reinforcing)** | ~400 | 400/1.8 ≈ **222** | 200,000 | Rebar (1960s+) | Smooth or slightly deformed |

**Partial safety factors (old standards):**
- Allowable stress: γ ≈ 1.8–2.0 (vs. modern γ = 1.15 for ULS)
- Much more conservative than modern Eurocodes

**Source:** DS 800, NB 8, old DIN standards adopted post-WWII

### 0.3 Historical Timber Grades (1920s–1960s)

**Norwegian/Scandinavian timber classification: C-grades (softwood sawn, not glulam)**

| Grade | Bending f_m,k [MPa] | Compression f_c,0,k [MPa] | E_mean [MPa] | Typical Use | Source |
|-------|---|---|---|---|---|
| **C16 (Nordic)** | 16 | 12 | 8,000 | Common (1930s–1950s) | Old log-based standard |
| **C22** | 22 | 15 | 9,500 | Better material (1950s–1970s) | Sorted sawn timber |
| **C30** | 30 | 18 | 11,500 | Demanding (1960s+) | High-grade softwood |

**Glulam (introduced post-WWII):**
- GL16, GL20: rare in pre-1960s structures
- Most older beams are solid sawn timber
- Modern GL32h ≈ 2× strength of old C22

**Source:** NB 8, DS 800, early NS standards

### 0.4 Historical Load Standards (1920s–1960s)

**Reference: NB 8, old DIN standards, pragmatic practice**

**Dead load (egenvekt — unchanged):**
- Tile roof: 0.7–1.0 kN/m² (including structure)
- Wood floor (solid): 0.5–0.8 kN/m²
- Brick/masonry: 15–20 kN/m³ (unchanged)

**Snow load (snølast — older, often LIGHTER than modern):**
- Pre-1950s: mostly empirical, region-dependent
- Oslo/coastal: 1.0–1.5 kN/m² (modern ≈ 2.0–2.8)
- Mountains: 2.0–3.5 kN/m² (modern ≈ 3.5–5.0)
- **Impact:** Older structures often undersized by modern standards

**Live load (nyttelast — older values often HIGHER than modern):**

| Occupancy | Old value [kN/m²] | Modern (EN 1991) [kN/m²] | Note |
|-----------|---|---|---|
| Residential (dwelling) | 2.0–2.5 | 1.5–2.0 | Older more conservative |
| Office/Commercial | 3.0–3.5 | 2.5–3.0 | Older slightly higher |
| Accessible attic | 1.5 | 0.5–1.0 | Much higher old value |
| Roof (not accessible) | 1.0–1.5 | 0.4–0.6 | Old value 2–3× higher |

**Old load combination (roughly equivalent to modern ULS):**
```
Σ_E ≈ 1.3 × (g_k + q_k) + wind/snow   [pragmatic allowable stress]

or simply:
Σ_E ≈ 1.5 × (g_k + q_k)  [simpler old rule]
```

**No formal partial safety factors; designers used judgment and large safety margins.**

**Source:** NB 8, DS 800, SINTEF Byggforsk historical analysis

### 0.5 Historical Design Method (1920s–1960s)

**Allowable stress method (not limit state):**
```
Design approach: f_actual ≤ f_allowable / safety_factor

Example (steel):
σ = M / W  [actual stress]
σ ≤ f_y / 1.8  [allowable stress]

If σ > allowable → unsafe (by old standard)
If σ < allowable → safe (with margin)
```

**Deflection criteria (often LESS stringent than modern):**
- Roof: L/150 to L/200 (modern: L/200)
- Floor: L/250 to L/300 (modern: L/300)
- Cantilever: L/120 (modern: L/150)

**Creep in timber (recognized but not formally calculated):**
- Long-term deflection ≈ 1.3–1.5 × short-term (vs. modern 1.5–1.8)
- No systematic k_def factor; empirical observation

**Source:** NB 8, engineer practice notes, SINTEF historical records

### 0.6 Quick Era Assessment for Existing Structures

**If construction year is:**
- **1920–1940:** Expect B150–B200 concrete, E-stål steel, solid sawn timber C16–C22
  - Very light roof loads (old standard)
  - No formal seismic/wind design (rare in Norway)
  - Rebar likely smooth (no deformation)
  - Concrete carbonation ≈ 25–30 mm

- **1945–1960:** Expect B200 concrete, E235 steel, C22 timber (post-war standard rebuild)
  - Still light roof snow loads
  - Early glulam may appear (rare)
  - Mixed rebar quality (transition period)
  - Carbonation ≈ 20–25 mm (better post-war concrete)

- **1960–1975:** Expect B200–B250 concrete, E235–E275 steel, C22–C30 timber / early GL16–GL20 glulam
  - Modern load standards starting (DIN/DS 800 adopted)
  - H-40 rebar introduction
  - Better concrete strength consistency
  - Carbonation ≈ 15–20 mm (stricter QC)

**Red flags for old structures:**
- [ ] Visible cracks in concrete (deep carbonation risk if >cover depth)
- [ ] Severely corroded rebar (orange rust stains)
- [ ] Sag > L/150 (exceeds old deflection limit; check if still elastic)
- [ ] No stirrups in beams (pre-1950s concrete common)
- [ ] Mixed construction phases (wars, rebuilding)

---

**Primary References:**
- **Roark & Young (2012)**: "Formulas for Stress and Strain" — 8th ed., Table 8 (Bending of Beams)
- **Hibbeler (2017)**: "Structural Analysis" — 10th ed., Chapter 5 (Beams and Frames)
- **Timoshenko (1945)**: "Theory of Elasticity" — 2nd ed., Part 1 (Bending Theory)
- **EN 1993-1-1** (Steel): Section 5.3.2 — Linear elastic analysis formulas
- **EN 1995-1-1** (Timber): Section 3.2 — Elastic design
- **EN 1992-1-1** (Concrete): Section 3 — Linear elastic analysis

