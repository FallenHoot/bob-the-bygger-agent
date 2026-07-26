---
name: building-code-tek17
description: Norwegian TEK17, PBL, SAK10 — permit process, energy requirements, fire safety, structural class, zoning, søknad, and the ansvarssystem. The legal minimum floor for all Norwegian construction.
triggers: [TEK17, PBL, SAK10, søknad, permit, byggetillatelse, fire, brann, energy, energi, U-value, U-verdi, zoning, regulering, setback, avstand, ceiling height, takhøyde, stair, trapp, ansvarlig, dispensasjon, ferdigattest, bruksendring, tilbygg, påbygg, byggesak, kommune, DiBK, igangsettingstillatelse, radon, accessibility, universell utforming, brannklasse, overvann, stormwater, klima, livsløp, ombruk, reuse, klimagass, EPD, LCA, carbon, frittliggende, 30 m²]
load_with: [structural-engineering]
safety_level: high
---

# Skill: Building Code TEK17 (Teknisk Forskrift 2017)

## ⚠️ DISCLAIMER

This skill contains information intended to be accurate as of **2026-07-26**. However, TEK17 regulations are subject to frequent amendments, and this knowledge base may contain errors. **Do not rely on this skill for official documentation or permit applications.** Always verify against authoritative sources (lovdata.no, dibk.no) and consult licensed professionals.

---

## Domain
Norwegian building regulations — TEK17 (Forskrift om tekniske krav til byggverk), the Plan- og bygningsloven (PBL), søknadsprosess, zoning, fire safety, energy requirements, and accessibility.

---

## Currency Warning — English Translation Is Stale

**DiBK's official English translation of TEK17 was last updated July 2017 and has not been amended since.**

The Norwegian text at [dibk.no/regelverk/byggteknisk-forskrift-tek17](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17) is the only authoritative, current version. This skill documents the Norwegian regulation including all amendments through **01.01.2024**. Significant post-2017 changes not reflected in the English translation:

| Amendment | Date | What changed |
|---|---|---|
| §1-2 frittliggende boligbygning | 01.07.2023 | New simplified rules for detached residential buildings ≤ 30 m² BRA |
| §7-2 Flom og stormflo | 15.03.2023 | Stricter flood safety provisions; preakseptert ytelse nr. 3 revised |
| §7-3 Skred | 01.09.2022 | Revised scope for RC2/RC3 — no longer applies to storulykkeforskriften facilities |
| §9-5, §9-7, §9-8, §9-9 | 01.07.2022 | Material reuse (ombruk) requirements, revised waste mapping and reporting |
| §11-6 Brannspredning | 01.03.2022 | New seventh paragraph on fire spread between buildings |
| §14-1, §14-3 | 01.07.2022 | Terminology: "minimumskrav" changed to "minimumsnivå" throughout energy chapter |
| §14-4 Energiforsyning | 01.07.2022 | 60% flexible heating requirement moved from guidance into regulation text |
| **Chapter 17 — Klima og livsløp** | **01.07.2022** | **Entirely new chapter — greenhouse gas calculation and lifecycle requirements** |
| **§15-8 — Overvann og drensvann** | **01.01.2024** | **New provision — stormwater management on-site** |
| SAK10 — søknadsfritak solar/insulation | **01.07.2026** | **Solar panels + additional insulation on small residential: no søknad required** |
| SAK10 — søknadsfritak EV charging | **01.07.2026** | **EV charging ≤ 50 m² on regulated sites: no søknad required** |
| TEK17 Chapter 2 — documentation guidance | **01.07.2026** | Guidance updated: clarifies analysis path to compliance and how firms document fulfilment |

**Pending amendments (consultation closed May 2026 — not yet in force, expected 2026–2027):**

| Proposal | Status | What is proposed |
|---|---|---|
| Chapter 14 energy | 86 responses received — being processed | Shift from netto energibehov to **vektet levert energi** (weighted delivered energy) as the calculation basis; tighten some requirements; introduce **separate energy requirements for existing buildings** |
| Chapter 17 climate | 133 responses received — being processed | Expand scope of klimagassregnskap; introduce **binding grenseverdier (CO₂ emission limits)** for materials — currently only calculation is required, proposed amendment adds a cap |
| SAK10 søknad/documentation | 51 responses received — being processed | Clarify what constitutes a complete søknad; improve predictability for applicants and municipalities |

> **Monitor**: Check [dibk.no/regelverk](https://www.dibk.no/regelverk) for when these consultations become enacted amendments. The Chapter 14 and 17 changes are significant and will affect compliance calculations for new construction.

**Institutional change — effective 01.01.2027:**
DiBK (Direktoratet for byggkvalitet) merges with Husbanken into a new **Bolig- og bygningsdirektoratet**. DiBK ceases to exist as an independent entity. The building regulation authority and the TEK17/SAK10 function will transfer to the new directorate. Update any references to DiBK after 01.01.2027.

**For any legal or permit-critical question, always verify against the current Norwegian text.**

---

## Legal Framework Overview

### Hierarchy of Authority
```
Plan- og bygningsloven (PBL) — Parliament statute
       ↓
SAK10 — Byggesaksforskriften (procedure / process)
       ↓
TEK17 — Teknisk forskrift (technical requirements)
       ↓
Kommunal arealplan / reguleringsplan (local plan)
       ↓
Antikvariske bestemmelser / SEFRAK (heritage restrictions)
```

All construction must comply with the entire hierarchy. Municipal plans can be more restrictive than TEK17 but cannot be less restrictive.

---

## TEK17 — Chapter by Chapter Reference

### §1 — Formål og virkeområde
TEK17 applies to all new buildings, rebuilding, and major alterations. Small measures (tiltak) below defined thresholds may be exempt. Key exemption category: **tiltak etter PBL §20-5** (exempt from søknadsplikten — e.g., small sheds under 15 m²).

**2023 amendment — §1-2 annet ledd**: New simplified rules for frittliggende boligbygning (detached residential buildings) ≤ 30 m² BRA. These buildings are now treated more like outbuildings for certain requirements. Accessibility (§12-2 tilgjengelig boenhet) and ventilation requirements (§13-1) are relaxed for buildings in this category. Check current text at dibk.no for the exact scope.

### §5 — Grad av utnytting (Density / Utilization)
- **BYA** (bebygd areal): footprint of buildings + parking + paved areas
- **BRA** (bruksareal): usable floor area per NS 3940
- **%-BYA** and **%-TU** are set by the municipal plan (reguleringsplan), not TEK17 itself
- Conversion of attic (loft) or basement to habitable space counts toward BRA and may trigger søknad

### §6 — Bebyggelse og omgivelser (Site and surroundings)
- Minimum setback from property line: typically 4.0 m unless municipal plan specifies otherwise
- Minimum setback from road: typically 4.0 m from property line side of road, but check reguleringsplan
- Building height is regulated by the local plan, not directly by TEK17

### §7 — Sikkerhet mot naturpåkjenninger (Natural hazards)
Critical for Norwegian construction:
- **Flom (flooding) — §7-2**: Habitable space must be above the 200-year flood level (Q200) plus required freeboard. **2023 amendment (15.03.2023)**: Provisions strengthened; preakseptert ytelse nr. 3 revised to remove a clause that allowed certain exceptions. Freeboard requirements are now stricter in practice. Always check against the current NVE flood maps (nve.no/kart) for the specific location.
- **Stormflo (storm surge)**: Coastal buildings must also account for sea level rise projections per the current NVE/Kartverket guidelines.
- **Skred (landslide/avalanche) — §7-3**: 1-in-1000 annual probability limit for residential buildings (RC2). **2022 amendment (01.09.2022)**: §7-3 first paragraph now applies only to buildings critical for national/regional emergency response — no longer applies to facilities under the major accident regulations (storulykkeforskriften). Skred risk assessment methodology: use NVE's guide for steep terrain and quick clay separately.
- **Kvikkleire (quick clay)**: Areas of sensitive quick clay require geotechnical assessment before siting or foundation design. NGU kvikkleirekart is the primary reference. If in a mapped kvikkleire zone, a professional geotechnical report (grunnundersøkelse) is mandatory — `GEOTECHNICAL_REPORT_REQUIRED` flag applies.
- Obtain NVE hazard map check and NGU ground condition check before siting or foundation design.

### §8 — Uteareal og parkering (Outdoor areas and parking)
- Parking minimum: typically 1.5 spaces/dwelling for new residential (varies by municipality and zone)
- Accessible parking: min. 1 space per 50 regular spaces must be HC-plass (UU compliant)
- Bicycle parking: municipal plans increasingly require covered cycle storage

### §9 — Energi (Energy)
TEK17 sets minimum energy requirements for new and significantly renovated buildings.

**Energy frame (energiramme) — Residential (§14-2):**
- All buildings must achieve a net energy need (netto energibehov) within the allowed frame
- The simplest compliance path: follow §14-3 minimum component values

**Minimum U-values — Residential buildings (§14-3):**
| Component | U-value (W/m²K) |
|---|---|
| Exterior wall | ≤ 0.18 |
| Roof | ≤ 0.13 |
| Floor to ground/crawlspace | ≤ 0.10 |
| Windows + doors | ≤ 0.80 |
| Thermal bridges (normalized) | ≤ 0.03 W/m²K |

**Heating — §14-4 (updated 01.07.2022):**
- Heat pump or district heating (fjernvarme) must be possible as primary heat source
- Electric direct heating alone is not permitted as the sole system in new construction > 500 m² BRA
- **2022 amendment**: The requirement that energy-flexible heating systems cover minimum 60% of normert netto varmebehov was moved from guidance text into the regulation itself (§14-4 annet ledd). This is now a binding requirement, not a recommendation.

**Ventilation:**
- Residential: mechanical extract + supply ventilation (balansert ventilasjon) with heat recovery ≥ 80% for new construction
- Minimum airflow: 26 m³/h per person + dilution flows per room

> **⚠️ PENDING AMENDMENT — Chapter 14**: A consultation closed 05.05.2026 proposes fundamental changes to how energy requirements are calculated and applied. Key proposals: (1) shift the calculation basis from **netto energibehov** (net energy demand) to **vektet levert energi** (weighted delivered energy — which accounts for energy carrier efficiency); (2) tighten some minimum requirements; (3) introduce **separate energy requirements for existing buildings** being significantly renovated (currently TEK17 largely only applies fully to new construction). If enacted, these changes will require new energy calculations and potentially affect renovation scope thresholds. Monitor dibk.no for enactment date.

### §10 — Konstruksjonssikkerhet (Structural safety)
- Design according to Eurocodes (NS-EN 1990 through NS-EN 1999) with Norwegian national annexes
- Pålitelighetsklasse (Reliability Class):
  - RC1: Low consequence (small outbuildings)
  - RC2: Normal consequence (residential)
  - RC3: High consequence (public buildings, high occupancy)
- Structural calculations must be documented and signed by ansvarlig prosjekterende

### §11 — Sikkerhet ved brann (Fire safety)
**Brannklasse (Risk class):**
| Risikoklasse | Use |
|---|---|
| 1 | Storage, garages without people sleeping |
| 2 | Agriculture, some industry |
| 3 | Offices, retail |
| 4 | Residential (single-family, up to 2 units) |
| 5 | Residential (apartments, care facilities) |
| 6 | Hospitals, high-risk special occupancies |

**Brannklasse (Consequence class) — determines construction requirements:**
| Brannklasse | Description |
|---|---|
| BKL1 | 1–2 floors, low occupancy |
| BKL2 | Up to 4 floors, residential |
| BKL3 | Over 4 floors, complex buildings |

**Key fire distances:**
- Minimum 8.0 m between buildings unless fire-rated walls or sprinkler
- Buildings on same plot: check BKL and risikoklasse for reduced distances

**Smoke alarms and fire suppression:**
- All dwellings: minimum one interconnected smoke alarm (røykvarsler) per floor
- Buildings BKL2+: automatic fire suppression system (sprinkler) increasingly required

**Means of escape:**
- Every sleeping room: operable window or door to safe area as secondary escape
- Max escape route length varies by risikoklasse

### §12 — Planløsning og bygningsdeler (Layout and building components)
- Minimum ceiling height: 2.20 m in habitable rooms (TEK17 §12-7)
- Headroom in stairwell: min. 2.10 m
- Minimum room dimensions: floor area ≥ 7.0 m² for habitable rooms
- **Loft (attic) conversion to habitable**: must meet ceiling height, fire escape, and ventilation requirements. Triggers søknadspliktig tiltak (§20-2 søknad).

**Stairways (§12-17):**
- Max rise: 200 mm (residential) / 180 mm (public)
- Min going: 200 mm (residential) / 250 mm (public)
- Min width: 900 mm clear (residential) / 1,200 mm (required accessible)
- Handrail required both sides if width > 1.2 m or > 3 risers

### §13 — Miljø (Environment)
- Radon: max 200 Bq/m³ indoor air for new construction. Radon barrier required in high-risk zones (check radonkart from DSA).
- Sound insulation (§13-5): Airborne sound Rw ≥ 55 dB between dwellings; impact sound Ln,w ≤ 53 dB
- VOC and material emissions: materials must not cause unacceptable indoor air quality

### §15-8 — Overvann og drensvann (NEW — in force 01.01.2024)

This provision was added to TEK17 effective 01.01.2024 and is entirely absent from DiBK's English translation. It addresses stormwater (overvann) and drainage water management.

**Core requirement**: Stormwater must be handled on-site as far as practically possible before discharge to the public stormwater system.

**Priority order for stormwater management:**
1. **Infiltration** into the ground on-site (infiltrasjon) — preferred first solution where soil conditions permit
2. **Surface flow / delay** — designed overland flow paths and detention on-site
3. **Local discharge** to watercourse, ditch, or similar — with permission from water authority
4. **Connection to public stormwater system** — only after the above options are exhausted or impractical

**Key design requirements:**
- Stormwater must not cause flooding of adjacent properties, public roads, or infrastructure
- Design must account for a minimum 10-year storm event (10-årsflom)
- A **climate factor (klimafaktor)** must be applied to design precipitation — typically 1.2–1.4 depending on location and projection period. Check the municipality's climate plan and NVE guidance.
- Stormwater and sewage must be separated where the public system is separate (separatsystem)
- On plots where soil conditions prevent infiltration (clay, rock), a detention solution with controlled discharge rate is required

**Municipal requirements:** Many municipalities have their own overvannsnorm (stormwater standard) that is more specific than TEK17 §15-8. Always check the local norm (e.g., Oslo's VA-norm, Bergen's overvannsveileder) before designing drainage.

**Renovation vs. new construction:** §15-8 applies to new construction. For renovations, the provision applies when surface conditions are significantly changed (e.g., new paving, building extensions that increase impermeable surface area).

*Verify exact preaksepterte ytelser at [dibk.no/regelverk/byggteknisk-forskrift-tek17](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17) §15-8.*

---

## Chapter 17 — Klima og livsløp (NEW — in force 01.07.2022)

Entirely absent from DiBK's English translation. This chapter was added as a new Chapter 17; the previous Chapter 17 (transitional provisions) is now Chapter 18.

**Purpose**: Reduce the climate and environmental impact of buildings over their full lifecycle — from material production through construction, operation, and end-of-life.

### §17-1 — Generelle krav (General requirements)
Buildings must be designed, constructed, and operated to minimise climate and environmental impact. This applies to both embodied carbon (materials and construction) and operational carbon (energy in use).

### §17-2 — Klimagassberegning (Greenhouse gas calculation)

**Applies to**: New buildings with heated floor area (oppvarmet BRA) > 500 m².

**Requirement**: A greenhouse gas calculation must be completed for the building's life cycle using a recognized calculation method. The standard reference method is **NS 3720:2018** (Metode for klimagassberegninger for bygninger).

**What must be included in the calculation:**
- All building materials and products (embodied carbon, expressed as kg CO₂-equivalent per m²)
- Construction process (machinery, transport, waste)
- Operational energy (over a 60-year reference period)
- End-of-life (demolition, waste)

**Data source**: Environmental Product Declarations (EPD) for all major materials. EPD-Norge maintains the Norwegian EPD database. Generic data from NS 3720 Annex may be used where project-specific EPDs are not available.

**Documentation**: The klimagassberegning must be submitted with the søknad for projects above the threshold. No maximum CO₂ limit is set by TEK17 — the requirement is to calculate and document, not to achieve a specific target. This may change in future amendments.

**Exemptions**: Buildings < 500 m² BRA, temporary buildings, and agricultural buildings are exempt.

> **⚠️ PENDING AMENDMENT — Chapter 17**: A consultation closed 05.05.2026 (133 responses) proposes two significant changes: (1) **expand the scope** of the klimagassregnskap requirement to cover more building categories, more lifecycle phases, and more building elements; (2) introduce **binding grenseverdier (maximum CO₂ emission limits)** for materials — a fundamental shift from the current "calculate and document" approach to "calculate, document, and comply with a cap." If enacted, projects above the threshold will need to achieve a specific climate performance standard, not just report their footprint. This would be the most significant change to Chapter 17 since it was introduced. Monitor dibk.no for enactment date.

### §17-3 — Ombruk (Material reuse)

**Requirement**: Buildings must be designed to facilitate future disassembly and reuse of materials and components where practically possible.

**In practice:**
- Prefer demountable connections (mechanical fasteners, not adhesive) where structural constraints permit
- Document materials in a **materialpassport** or material register for future reuse identification
- When demolishing an existing building as part of a project, an **ombrukskartlegging** (reuse mapping) is required — see also §9-7 (amended 2022)

### §9-5, §9-7, §9-8, §9-9 — Waste and Reuse (2022 amendments)

These sections were amended in 2022 to align with Chapter 17's ombruk requirements:

- **§9-5 Byggavfall og ombruk**: Materials suitable for reuse must be identified and separated. The requirement to facilitate ombruk is now more explicit.
- **§9-7 Kartlegging (Environmental survey)**: The environmental survey (formerly called miljøsaneringsbeskrivelse, now **rapport fra miljøkartlegging**) must now include an ombrukskartlegging section identifying materials suitable for reuse, not just hazardous materials for removal.
- **§9-8 Avfallssortering**: Waste sorting requirements updated — specific fractions must be separated.
- **§9-9 Sluttrapport**: Final waste report (sluttrapport) must document actual disposal of all waste fractions, including what was reused.

**Practical implication for demolition projects**: The hazardous waste survey (`HAZARDOUS_WASTE_SURVEY_REQUIRED`) now has a dual purpose — it must assess both hazardous materials (asbest, bly, etc.) AND materials suitable for reuse. A single combined survey document typically covers both.

*Verify exact current text at [dibk.no/regelverk/byggteknisk-forskrift-tek17](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17) Chapters 9 and 17.*

---

## Søknadsprosess (Permit Process)

### PBL §20-1 — Søknadspliktige tiltak (Full permit required)
- New buildings
- Extensions and additions (påbygg/tilbygg)
- Change of use (bruksendring)
- Demolition of buildings
- Foundation work
- Structural modifications

### PBL §20-3 — Forenklet søknad (Simplified permit, no neighbors' consent)
For measures by an ansvarlig søker where:
- No dispensation from plans is needed
- Neighbors are not affected

### PBL §20-4 — Søknad uten ansvarsrett (Self-administered permit)
For simple measures by the property owner themselves, if:
- Small structures (≤ 50 m² BYA, ≤ 1 story, no habitation)
- No special conditions (no flood zone, no heritage)

### PBL §20-5 — Unntatt søknadsplikt (Exempt from permit — no filing needed)
- Small frittliggende buildings ≤ 15 m² BYA (storage sheds, outbuildings)
- Cannot be habitable, cannot contain sanitary or kitchen facilities
- Must comply with setback rules even if no permit needed
- **2023**: Frittliggende boligbygning ≤ 30 m² BRA has simplified requirements but still requires søknad (§20-4 or §20-3)

**SAK10 amendments in force since 01.07.2026** (FOR 2026-06-12 nr. 1130):
The following tiltak no longer require any søknad on eneboliger, tomannsboliger, and rekkehus:
- **Solenergianlegg (solar energy systems)** — installing solar panels or solar thermal. Owner must verify that the exemption conditions are met before starting work.
- **Etterisolering (additional insulation)** — adding insulation to the external envelope of the building.

The following no longer require søknad on regulated land (bensinstasjoner, parkeringsplasser, havner/kaianlegg):
- **Ladestasjoner ≤ 50 m²** (EV charging infrastructure) — both on built and unbuilt areas within the regulated site.

**Practical note**: The exemption from søknad does not mean exemption from TEK17 or other technical requirements. The homeowner or contractor still bears responsibility for ensuring the work is done correctly. An electrician (for solar) and any relevant qualifications still apply.

### Dispensasjon (Variance / Dispensation) — PBL §19-2
Required when you need to deviate from a plan or regulation. Must show:
1. The deviation does not undermine the plan's intent (hensynet bak bestemmelsen)
2. The advantages clearly outweigh the disadvantages

Municipal processing time for søknad: 3 weeks (forenklet), 12 weeks (full søknad), up to 16 weeks with neighbors' hearing.

---

## Ansvarssystem (Responsibility System)

| Role | Norwegian Term | Responsibility |
|---|---|---|
| Applicant owner | Tiltakshaver | Final legal responsibility |
| Lead designer | Ansvarlig søker | Coordinates application, signs drawings |
| Designer | Ansvarlig prosjekterende | Designs to code, signs calculations |
| Contractor | Ansvarlig utførende | Builds to drawings and code |
| Controller | Ansvarlig kontrollerende | Independent review of design/execution |

All roles require formal qualification (sentral godkjenning from DiBK or lokal godkjenning from municipality).

---

## Key Abbreviations
| Term | Meaning |
|---|---|
| TEK17 | Teknisk forskrift 2017 |
| PBL | Plan- og bygningsloven |
| SAK10 | Byggesaksforskriften |
| BYA | Bebygd areal (footprint) |
| BRA | Bruksareal (usable floor area) |
| TU | Total utnyttelse |
| BKL | Brannklasse |
| DiBK | Direktoratet for byggkvalitet |
| NVE | Norges vassdrags- og energidirektorat |
| NGU | Norges geologiske undersøkelse |
| EPD | Environmental Product Declaration |
| LCA | Life Cycle Assessment |
| NS 3720 | Method for greenhouse gas calculations for buildings |

---

## Interaction with Other Skills
- **Structural Engineering**: TEK17 §10 mandates Eurocode compliance. Structural drawings and calculations are required in søknad documentation.
- **SINTEF Byggforsk**: Provides execution details (anvisninger) that document how to meet TEK17's energy, moisture, and construction requirements in practice.
- **Historic Preservation**: Dispensasjon from TEK17 energy requirements is possible for listed/heritage buildings (§14-8). Cultural heritage law overrides where in direct conflict.
- **Construction Execution**: Søknad must include an igangsettelses- and ferdigattest process. No occupancy before ferdigattest is issued. §9-7 environmental survey required before demolition.

---

*Authority: TEK17 (FOR 2017-06-19 nr. 840), SAK10 (FOR 2010-03-26 nr. 488, last amended FOR 2026-06-12 nr. 1130), PBL (LOV 2008-06-27 nr. 71)*
*Norwegian authoritative text: [dibk.no/regelverk/byggteknisk-forskrift-tek17](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17)*
*DiBK English translation status: Last updated July 2017 — does not reflect amendments made 2017–2026*
*Institutional note: DiBK merges with Husbanken → Bolig- og bygningsdirektoratet from 01.01.2027. URLs and authority name will change.*
*This skill last verified against DiBK news and høringer: 2026-07-26 (TEK17 current through §15-8 01.01.2024; SAK10 current through søknadsfritak 01.07.2026; two major amendments pending)*
