---
name: geotechnical
description: Soil investigation, bearing capacity, settlement, quick clay risk, and foundation type selection per Norwegian geotechnical standards. Load for soil, foundation, or ground-condition questions.
license: Proprietary
triggers: [soil, grunn, kvikkleire, quick clay, borehole, boring, grunnundersøkelse, CPT, CPTU, SPT, bearing capacity, bæreevne, settlement, setning, foundation, fundament, pile, pæl, ground investigation, geotechnical report, NGU, NVE, landslide, skred, radon, slope stability, skråningsstabilitet, fill, fyllmasse, peat, torv, rock, fjell, soft clay, bløt leire, frost depth, frostdybde, drainage, drenering, excavation, graving]
load_with: [building-code-tek17]
safety_level: critical
---

# Skill: Geotechnical Engineering

## ⚠️ DISCLAIMER

Geotechnical design needs adequate site-specific evidence. Bob can interpret evidence and identify risk flags, not authorize foundations or excavation. A qualified geotechnical professional determines whether existing evidence suffices or additional investigation is needed. Verify the applicable Norwegian design, responsibility, and documentation requirements rather than imposing a universal license or report format.

**Review trigger:** use `GROUND_HAZARD_REVIEW` whenever:
- Mapping indicates possible quick clay or an area-stability concern
- Soil conditions are unknown before any excavation or foundation work
- Significant fill (fyllmasse) is suspected
- Settlement-sensitive structures are proposed on soft clay

---

## Trust Boundary

**Bob may, on his own analysis:**
- Interpret provided ground investigation data (CPT/CPTU/SPT/borehole logs) and identify risk flags
- Read public map layers (NGU kart, NVE aktsomhetskart) and state what they show for a given plot
- Explain which foundation types are typically appropriate for a described soil profile, in general terms

**Bob may flag only as preliminary / low-confidence:**
- Any bearing capacity or settlement estimate made without a site-specific ground investigation report
- Foundation type suitability when soil data is inferred from nearby boreholes or regional maps rather than the subject plot

**Seek qualified geotechnical review before relying on:** foundation design or bearing values, excavation near foundations/slopes/waterways, quick-clay screening, or settlement-sensitive work on soft clay/fill. Identify the responsible designer and the investigation/review scope appropriate to the measure and hazard. This is a safety-review gate, not a claim that every such case has the same statutory investigation program.

**Ground evidence gate (L004):** Label evidence as owner-reported, photograph/visible outcrop, map screening, site investigation, or professional assessment, with location, date, coverage, and limitations. A bedrock photograph establishes at most a visible surface observation, not rock continuity beneath all supports, rock quality, bearing capacity, settlement performance, or local/area slope stability. Map absence of a hazard is not site clearance either. Keep **UNKNOWN: ground safety not established** until scope-specific professional evidence resolves it. A permit/responsibility exemption cannot establish technical safety or turn this status GREEN. Missing documentation alone is not proof of illegality or unsafe ground.

---

## Norwegian Geotechnical Framework

### Governing Standards
| Standard | Coverage | Authority |
|---|---|---|
| **NS-EN 1997-1** (Eurocode 7, Part 1) | Geotechnical design — general rules | CEN / Standard Norge |
| **NS-EN 1997-2** (Eurocode 7, Part 2) | Ground investigation and testing | CEN / Standard Norge |
| **NS-EN ISO 22476** | Field testing standards (CPT, SPT, borehole) | CEN / ISO |
| **NGF Melding Nr. 2** | Norwegian Geotechnical Society guidelines for site investigation | NGF |
| **NVE Veileder 7/2014** | Geotechnical assessments in areas with quick clay | NVE |
| **NVE Veileder 1/2019** | Flood hazard mapping | NVE |
| **TEK17 §7** | Natural hazard safety requirements | DiBK |

### Data Sources for Site Assessment
| Source | What it gives | URL |
|---|---|---|
| **NGU kart** | Quick clay sensitivity map, soil type (løsmassekart), rock depth | geo.ngu.no |
| **NVE Atlas** | Flood zones (Q200), landslide zones, avalanche zones | atlas.nve.no |
| **Geonorge** | DOK datasets, municipal plans, property data | geonorge.no |
| **DSA radonkart** | Radon ground risk classification | nrpa.no/radon |
| **Kartverket Høydedata** | LiDAR terrain model (1 m grid) — terrain analysis | hoydedata.no |

---

## Norwegian Soil Classification

### Soil Types in Norway — Common Conditions
| Type (Norwegian) | Type (English) | Typical Location | Key Properties |
|---|---|---|---|
| **Fjell** | Bedrock (granite/gneiss/schist) | Outcrops or at variable depth | Bearing/deformation depend on continuity, weathering, fractures, support geometry, and slope stability; visible rock is not clearance |
| **Morene** | Till / glacial moraine | Most of the country | Dense, mixed; generally good bearing |
| **Sand/grus** | Sand/gravel | River valleys, coastal | Good bearing; drains well; frost-susceptible |
| **Silt** | Silt | River deltas, coastal flats | Moderate bearing; compressible; frost-susceptible |
| **Leire** | Clay | Oslo fjord area, coastal lowlands | Poor bearing; compressible; quick clay risk |
| **Kvikkleire** | Quick clay | Marine clay areas | Catastrophic failure risk — see §Quick Clay |
| **Torv/myr** | Peat/bog | Wetlands, low areas | Extremely compressible; must be excavated |
| **Fyllmasse** | Fill (made ground) | Urban areas, old industrial sites | Unknown composition; must investigate |

### EN 1997 Design Approach for Norway
Norway uses **Design Approach 2 (DA2)** as the National Annex default for most geotechnical calculations:

```
Verification of bearing capacity (GEO limit state):
Ed ≤ Rd

where:
  Ed = design effect of actions = γG × Gk + γQ × Qk
  Rd = design resistance = Rk / γR

DA2 partial factors:
  γG = 1.35 (permanent unfavourable)
  γQ = 1.50 (variable unfavourable)
  γR = 1.40 (bearing capacity of spread foundations on soil)
  γR = 1.10 (bearing on rock)
```

---

## Bearing Capacity — Spread Foundations

### Presumed Bearing Capacity (Quick Assessment)
Use only for preliminary sizing. A proper calculation requires soil parameters from investigation.

| Soil Type | Presumed q_allow [kN/m²] | Notes |
|---|---|---|
| Dense sand/gravel | 200–400 | Confirm with CPT or SPT |
| Compact moraine | 150–300 | Variable; depends on composition |
| Stiff clay (su > 100 kPa) | 100–200 | Settlement check required |
| Soft clay (su 25–100 kPa) | 50–100 | Settlement governs; consolidation analysis needed |
| Very soft clay (su < 25 kPa) | < 50 | Pile foundation likely needed |
| Peat | DO NOT FOUND | Remove and replace or pile through |
| Bedrock | 500–2000+ | Surface quality matters; test high-load cases |

### Terzaghi Bearing Capacity (Strip Footing)
For preliminary hand calculations:

```
qu = c'·Nc + q·Nq + 0.5·γ·B·Nγ

where:
  c' = cohesion [kPa]
  q = overburden pressure at foundation depth = γ·Df [kPa]
  γ = soil unit weight [kN/m³] (sand ≈ 19, clay ≈ 18, moraine ≈ 20)
  B = footing width [m]
  Df = foundation depth [m]

Bearing capacity factors (selected values):
  φ' = 25°: Nc = 20.7, Nq = 10.7, Nγ = 10.9
  φ' = 30°: Nc = 30.1, Nq = 18.4, Nγ = 22.4
  φ' = 35°: Nc = 46.1, Nq = 33.3, Nγ = 48.0

Allowable bearing (FS = 3): qa = qu / 3
EN 1997 DA2: verify Rd = Rk / 1.40 ≥ Ed
```

---

## Settlement Analysis

### Settlement Types
| Type | When it occurs | Duration | Predictability |
|---|---|---|---|
| **Immediate** | During loading (elastic) | Seconds–days | Good |
| **Primary consolidation** | Clay — water squeezed out | Months–decades | Fair with lab data |
| **Secondary consolidation (creep)** | Organic soils, very soft clay | Decades–centuries | Poor |
| **Differential settlement** | Varies across footprint | Depends on soil variability | Requires mapping |

### Allowable Settlement — Norwegian Practice

| Structure type | Max total settlement | Max differential | Source |
|---|---|---|---|
| Residential (timber, flexible) | 50–75 mm | L/300 | NGF guidance |
| Residential (masonry, stiff) | 25–40 mm | L/500 | NGF guidance |
| Industrial buildings | 75–100 mm | L/200 | NGF guidance |
| Settlement-sensitive (facades, finishes) | 15–25 mm | L/600 | Project-specific |

**Primary consolidation estimate (Terzaghi 1D):**
```
s = (Cc / (1 + e0)) × H × log10(σ'v0 + Δσ / σ'v0)

where:
  Cc = compression index (from oedometer test)
  e0 = initial void ratio
  H = compressible layer thickness [m]
  σ'v0 = initial effective vertical stress [kPa]
  Δσ = stress increase from building load [kPa]

Time for 90% consolidation: t90 = (T90 × d²) / cv
  T90 = 0.848 (time factor)
  d = drainage path length [m]
  cv = coefficient of consolidation [m²/year] (lab test)
```

---

## Quick Clay (Kvikkleire)

Quick clay is Norway's most dangerous geotechnical hazard. It is a legacy of post-glacial marine sedimentation: salt was the binding agent in the clay. Freshwater leaching has removed the salt, leaving a structured clay that behaves normally until disturbed — at which point it liquefies and flows catastrophically.

### How to Recognize Quick Clay Risk

**Geographic indicators:**
- Below the marine limit (marin grense) — varies 50–220 m above sea level depending on location
- In river valleys where erosion exposes old marine clay
- Near previous quick clay slides (NVE database)
- In areas with historic drainage or infilling of streams

**NGU Sensitivity Classification (from field testing):**
| NGU Class | Sensitivity (St) | Remoulded shear strength (su,r) | Risk level |
|---|---|---|---|
| Low | St < 15 | su,r > 2 kPa | Low |
| Medium | St 15–50 | su,r 0.5–2 kPa | Moderate |
| High | St 50–200 | su,r 0.15–0.5 kPa | High |
| **Extra high (quick clay)** | St > 200 | su,r < 0.15 kPa | **Critical** |

**Check relevant NVE hazard and NGU ground-condition layers**, with dataset date and limitations. Mapped potential on or near a plot triggers `GROUND_HAZARD_REVIEW`, not a confirmed site diagnosis; absence from a mapped zone does not rule out quick clay.

### Quick Clay — Applicable Assessment
Verify current TEK17 §7-3 and NVE guidance for the measure, terrain, and local/area hazard. The geotechnical professional determines screening steps, investigation, stability analysis, safety criteria, and independent review where applicable. Do not treat a fixed safety factor, CPTU minimum, or piles to rock as universally sufficient. Piles do not by themselves resolve area instability.

### Quick Clay Response Protocol
When quick clay is mapped on or near a plot:
1. **Flag immediately**: `GROUND_HAZARD_REVIEW`.
2. **Tell the user**: "Mapping indicates a potential quick-clay/area-stability concern. It does not confirm conditions at every support. Obtain qualified geotechnical assessment before relying on a foundation or excavation proposal."
3. **Authority route**: Verify any municipal/NVE notification or permit obligations for the specific work; do not assert universal pre-notification regardless of scope.
4. **Do not estimate**: Do not assign bearing capacity for a potentially quick-clay site from generic tables. Ask the geotechnical professional to establish the necessary evidence and design basis.

---

## Ground Investigation Methods

### Field Tests
| Test | Norwegian | What it measures | When to use |
|---|---|---|---|
| **CPTU** (Piezocone) | CPTU / trykksondering | Continuous profile: resistance, friction, pore pressure | Most Norwegian projects — fast, reliable |
| **Total Sounding** | Totalsondering | Penetration resistance to bedrock | Quick depth-to-rock check; low cost |
| **Rotary Pressure Sounding** | Dreietrykksondering | Relative density of coarse material | Sand, gravel, moraine |
| **SPT** | Standard Penetration Test | N-value for sand/gravel | Less common; used for imported codes |
| **Borehole sampling** | Kerneboring / prøvetaking | Undisturbed samples for lab testing | Required for consolidation analysis |

### Laboratory Tests
| Test | What it gives | When required |
|---|---|---|
| **Fall cone** | Undrained shear strength (su); remoulded strength (su,r); sensitivity St | Quick clay assessment |
| **Oedometer** | Compression index Cc, preconsolidation pressure, cv | Settlement analysis |
| **Triaxial** | Effective friction φ', cohesion c', stress paths | Slope stability, retaining walls |
| **Grain size distribution** | Soil classification | All investigation programs |
| **Plasticity / Atterberg** | Liquid limit, plastic limit; classify clay | Clay identification |

### Minimum Investigation for Residential (NGF Melding Nr. 2)

| Project type | Minimum program |
|---|---|
| Single-family house, no basement | 3–5 total soundings to bedrock or refusal + 1 CPTU in soft soil zones |
| Single-family house, basement | 5–8 soundings + CPTU if clay or silt present + groundwater monitoring |
| Multi-family (up to 4 floors) | 8–12 soundings + 3–5 CPTU + 1–2 boreholes with sampling |
| Quick clay zone | All above + fall cone + oedometer + stability analysis |

---

## Foundation Type Selection

### Decision Framework

```
Step 1: What is the depth to bedrock or competent bearing layer?
  ≤ 1.5 m → Spread or strip footing on rock/moraine
  1.5–4 m → Pad or strip footing with deeper embedment; check settlement
  > 4 m in soft soil → Piles or ground improvement

Step 2: Is there quick clay or very soft clay?
  YES → Geotechnical assessment of local/area stability and foundation options; no automatic piles-to-rock clearance
  NO → Continue to Step 3

Step 3: Is there frost-susceptible soil (silt, fine sand, silty clay)?
  YES → Found below frost depth (frostfri dybde)
  Frost depth by zone: Oslo coast ≈ 1.5 m; Inland ≈ 2.0 m; North/mountains ≈ 2.5–3.0 m

Step 4: Is the plot sloped or near a water course?
  YES → Slope stability check required; set-back from edge per NVE 7/2014
```

### Foundation Types — Norwegian Residential

| Type | When used | TEK17 compliance |
|---|---|---|
| **Strip footing on bedrock** | Shallow rock, good quality | OK; check frost protection at edges |
| **Strip footing on moraine/gravel** | Dense, well-graded soil ≤ 2 m deep | OK; check bearing and frost depth |
| **Pad footing + ground beams** | Isolated columns, variable soil | OK; differential settlement check |
| **Raft (plate on ground)** | Variable soil, moderate loads | OK; verify uniform stiffness |
| **Driven timber piles to rock** | Traditional; <5 m to bedrock | OK for historic buildings; corrosion risk in groundwater change |
| **Driven steel piles** | Moderate depth; good bearing | Standard for modern work |
| **Bored concrete piles** | Deep; urban; vibration-sensitive | Standard for larger residential |
| **Micro-piles (spunting)** | Limited access, heritage buildings | OK; engineer design required |

---

## Radon

Per TEK17 §13-5b, new construction in radon risk zones must provide radon barriers.

**DSA Radon Risk Classification:**
| Class | Rn ground concentration | Required measures |
|---|---|---|
| Low | < 10 kBq/m³ | Standard vapor barrier sufficient |
| Moderate | 10–50 kBq/m³ | Radon membrane + installation sleeve for sub-slab depressurization |
| High | > 50 kBq/m³ | Full sub-slab depressurization system + membrane |

**TEK17 indoor air limit**: 200 Bq/m³ (annual average). Measure after construction if in risk zone.

**Check DSA radonkart before design.** The map is available through NGU/Geonorge as a WMS layer.

---

## Frost Protection

Foundation depth below frost-free depth (frostfri dybde) is mandatory for all bearing elements in frost-susceptible soil:

| Region | Minimum depth (general) | Frost-susceptible soil |
|---|---|---|
| Coastal west (Bergen, Stavanger) | 0.8–1.0 m | 1.2 m |
| Oslo / Akershus | 1.2–1.5 m | 1.8 m |
| Inland Østlandet | 1.6–2.0 m | 2.2 m |
| Northern Norway (Tromsø, Finnmark) | 2.0–3.0 m | 3.0–3.5 m |

**Frost-susceptible soil**: Fine-grained (silt, clay, fine sand) with high capillary suction. Ice lenses form and cause heave. Gravel and bedrock are not frost-susceptible.

Non-frost-susceptible backfill (pukk, knust fjell) around foundation perimeter eliminates frost heave risk regardless of frost depth.

---

## Interaction with Other Skills
- **TEK17 §7**: Natural hazard safety requirements (flood, landslide, quick clay) — always load `building-code-tek17` when geotechnical hazards are present.
- **Structural Engineering**: Foundation design is structural; geotechnical provides soil parameters, structural engineering uses them for design.
- **Construction Execution**: Excavation sequencing, temporary shoring, dewatering — coordinate with `construction-execution`.

---

*Authority: NS-EN 1997-1, NS-EN 1997-2, NGF Melding Nr. 2, NVE Veileder 7/2014, TEK17 §7*
*Key data sources: geo.ngu.no (NGU), atlas.nve.no (NVE), geonorge.no (Kartverket)*
*Last reviewed: 2026-08-09*
