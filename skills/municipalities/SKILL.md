---
name: municipalities
description: Norwegian municipality-specific building rules — snow loads, BYA limits, heritage zones, municipal plan overrides, and local authority contacts. Load whenever a specific municipality is named or when a project address is provided. Overrides generic TEK17 assumptions with actual local requirements.
license: Proprietary
metadata:
  triggers: Lørenskog, Oslo, Bergen, Trondheim, Stavanger, Kristiansand, Tromsø, Drammen, Fredrikstad, Sandnes, Bodø, Ålesund, Asker, Bærum, kommune, municipality, reguleringsplan, kommuneplan, local plan, local rules
  load_with: building-code-tek17
  safety_level: high
---

# Skill: Municipality-Specific Rules

## Why This Skill Exists

TEK17 sets the minimum floor. Every municipality can — and frequently does — set stricter requirements through their **kommuneplan** (municipal master plan) and **reguleringsplaner** (zoning plans). Generic TEK17 knowledge will miss:

- Higher BYA/TU limits than TEK17 baseline
- Protected view corridors (siktlinjer)
- Heritage zones not registered in SEFRAK
- Municipal stormwater standards (overvannsnorm) stricter than TEK17 §15-8
- Local snow load zone verification (TEK17 gives zones, municipalities apply locally)
- Municipal requirements for solar, EV charging, bicycle storage beyond TEK17 minimums
- Pre-application meeting (forhåndskonferanse) requirements and contacts

**Always check the specific kommuneplan and reguleringsplan for the address.** This skill provides a starting point — it does not replace a site-specific plan check.

---

## How to Use This Skill

1. Identify the municipality from the project address or `project.md`
2. Check the municipality-specific section below for known overrides
3. Flag any items that differ from TEK17 baseline
4. Always direct the user to the municipality's own plan portal for the specific plot

**Finding the relevant reguleringsplan:**
- Most municipalities: `[kommunenavn].kommune.no/byggesak`
- National portal: `arealplaner.no` — search by address for the applicable reguleringsplan
- Property register: `infoland.no` or `seeiendom.no` — shows plan status and document list

---

## Lørenskog Kommune

**Contact:** byggesak@lorenskog.kommune.no  
**Portal:** lorenskog.kommune.no/byggesak  
**Plan portal:** arealplaner.no → search Lørenskog  
**Institutional note:** Lørenskog becomes part of **Lillestrøm kommune** (merged 2020). Plans and permits are now administered by Lillestrøm. Some older plans still reference "Lørenskog." Address permits to: Lillestrøm kommune, postmottak@lillestrom.kommune.no

**Snow zone:** Zone 2 (Østlandet interior) — s_k = 2.5–3.0 kN/m² for most of Fjellhamar/Lørenskog area. Higher in elevated terrain.

**Known local rules:**
- Single-family residential (S1/S2 zoning): max %-BYA typically 25% in older plans, 30% in newer plans. Always confirm from the specific reguleringsplan — varies significantly between areas.
- Carport vs. garage: Lørenskog/Lillestrøm counts covered carports toward BYA. Detached carports ≤ 15 m² are typically søknadsfri, but counted in BYA.
- Secondary dwelling unit (sekundærleilighet): strictly regulated. Garage deck conversion to living quarters may trigger secondary dwelling unit classification — this has stricter requirements and may require dispensasjon from the plan.
- Heritage: Fjellhamar area has limited SEFRAK coverage (mostly post-war). Contact Lillestrøm kommune for any building with "1967" heritage interest notation.
- Parking: standard minimum 2 spaces per single-family dwelling; check if the reguleringsplan requires more for extensions.

**Known geology (Fjellhamar area):**
- Fjellhamar sits on a bedrock ridge within a wider marine clay/kvikkleire zone
- Properties at higher elevation (e.g., Aasmund Vinjes vei area) are often on bedrock
- Lower-lying areas toward Nitelva and coastal zones: marine clay, potential quick clay
- Always verify NGU løsmassekart for the specific plot — bedrock and soft ground can be within 50m of each other

**Stormwater:** Lillestrøm/Lørenskog has its own VA-norm (water and sewer standard). For extensions, the VA-norm may require formal connection evaluation — contact kommunalteknikk@lillestrom.kommune.no.

---

## Oslo Kommune

**Contact:** plan@pbe.oslo.kommune.no (Plan og bygningsetaten)  
**Portal:** www.oslo.kommune.no/plan-bygg-og-eiendom  
**Plan portal:** planinnsyn.oslo.kommune.no  

**Snow zone:** Zone 1 (coastal) — s_k ≈ 2.0–2.5 kN/m² for most of Oslo. Higher in Marka areas (Nordmarka, Sørmarka) — check NVE snow zone map for specific elevation.

**Known local rules — heritage (most important):**
- Oslo Byantikvaren is the most active municipal heritage authority in Norway
- **Gul liste (Yellow list):** Oslo's supplementary register of buildings with heritage interest — many buildings not on SEFRAK are still subject to antikvarisk assessment
- **Gul liste check:** www.oslo.kommune.no/byutvikling/kulturminner — search before any facade intervention
- Pre-application meeting (forhåndskonferanse) is strongly recommended for any building on the Gul liste or in conservation areas (bevaring_) in reguleringsplanen
- Contact: byantikvaren@byantikvaren.oslo.kommune.no

**Known local rules — density:**
- Oslo has many different zoning plans. BYA limits vary from 20% (villa areas) to 60%+ (urban mixed use)
- Many Oslo residential areas (especially pre-war villa areas) have view corridors (siktlinjer) that strictly limit height and placement of extensions
- Always check the specific reguleringsplan — Oslo's plans are detailed and frequently updated

**Stormwater:** Oslo has a strict overvannsnorm (Blue-Green Infrastructure requirements). New impermeable surfaces may trigger requirements for on-site detention. Contact VA-etaten.

**Building heights:** Oslo regulates height from "gjennomsnittlig planert terreng" (average finished grade). On sloped sites, this significantly affects allowed height — confirm with Plan og bygningsetaten.

**SEFRAK in Oslo:** High coverage, especially pre-1940 buildings. Always check SEFRAK and Gul liste together.

---

## Bergen Kommune

**Contact:** byggesak@bergen.kommune.no  
**Portal:** www.bergen.kommune.no/hverdagslivet/bygg-eiendom  
**Plan portal:** webgis.bergen.kommune.no  

**Snow zone:** Zone 2–3 depending on elevation. Bergen city: 2.5–3.0 kN/m². Interior areas (Arna, Osterøy): up to 3.5–4.0 kN/m². Bergen is also exposed to high wind loads from North Sea exposure.

**Wind load:** Bergen is in wind zone IV (highest) for exposed sites. Check NS-EN 1991-1-4 terrain category carefully — Bergen's terrain is complex.

**Known local rules — heritage:**
- Bergen Byantikvaren is Norway's most active heritage authority outside Oslo
- Bryggen (UNESCO) and historic neighbourhoods (Sandviken, Nordnes) have extremely strict controls
- Even outside the UNESCO zone, Bergen has extensive bevaring zones in reguleringsplaner
- Heritage assessment (antikvarisk vurdering) is often required before any exterior work on pre-1940 buildings

**Known local rules — terrain:**
- Bergen's steep terrain creates unique structural and geotechnical requirements
- Slope stability (skredfare) is a significant concern — many Bergen properties are in landslide risk zones
- Always check NVE faresoner before any excavation or foundation work
- Foundation depth on sloped sites often requires engineering design beyond standard strip footing rules

**Stormwater:** Bergen has severe stormwater challenges (highest rainfall in Scandinavia). Strict VA-norm. Any significant increase in impermeable area requires stormwater assessment.

**Radon:** Bergen area has elevated radon risk in granite bedrock zones. Check NGU radonkart.

---

## Trondheim Kommune

**Contact:** postmottak@trondheim.kommune.no (Byplankontoret)  
**Portal:** www.trondheim.kommune.no/tema/bygg-og-eiendom  

**Snow zone:** Zone 3 — s_k = 3.5–4.5 kN/m² for Trondheim city area. Mountain areas significantly higher.

**Known local rules:**
- Trondheim has a strong heritage culture with NTNU (architecture faculty) involvement
- Midtbyen (city centre) has strict heritage zoning for pre-1940 buildings
- Kvikkleirekart coverage: significant — Trondheim fjord area has historic kvikkleire zones. Always check NGU before foundation work.
- Marine clay: widespread in lower-lying areas around Trondheimsfjord

**Stormwater:** Trondheim has ongoing flood issues. Check NVE flomkart before siting or foundation design near watercourses.

---

## Stavanger / Sandnes

**Contact:** postmottak@stavanger.kommune.no  
**Portal:** www.stavanger.kommune.no/byutvikling  

**Snow zone:** Zone 1 (coastal) — s_k ≈ 1.5–2.5 kN/m². Lowest snow loads in Norway.

**Wind load:** Highly exposed coastal location. Wind loads often govern structural design where snow does not. Apply terrain category I–II for coastal exposure.

**Known local rules:**
- Oil industry proximity: many buildings have industrial heritage interest
- Stavanger has a well-preserved historic centre (Gamle Stavanger — wooden houses) with extremely strict heritage controls
- Contact Stavanger Byantikvaren before any work on pre-1940 wooden buildings

---

## General Pattern for Any Municipality

When Bob encounters a municipality not listed above, apply this pattern:

### Step 1: Identify the Plan
```
Reguleringsplan number: check arealplaner.no
Plan type: kommunedelplan / reguleringsplan / bebyggelsesplan
Permitted use: [arealformål]
Max BYA or TU: [%]
Max building height: [m] from [reference — planert terreng / BRA / fasadeliv]
Setback from property line: [m] — confirm if this is softer or stricter than TEK17 §6 default
Setback from road: [m]
```

### Step 2: Heritage Check
```
SEFRAK status: check kulturminnesok.no
Municipal register: does the municipality have its own heritage list? (Gul liste etc.)
Conservation zone in plan: look for "bevaring" in the reguleringsbestemmelser
```

### Step 3: Snow Zone
```
TEK17 Table 7.1 zone: [1/2/3/4]
Characteristic snow load s_k: [kN/m²]
Note: if the site is at elevated terrain or north-facing slopes, the actual s_k may be higher than the zone table value
```

### Step 4: Local Contacts
```
Byggesak: [municipality] byggesak email
Heritage authority: Byantikvaren (if municipality has one) or fylkeskommunen
VA-etaten (water/sewer): for stormwater questions
```

### Step 5: Stormwater
```
Municipality overvannsnorm: does the municipality have its own standard? (Bergen, Oslo, Trondheim, Stavanger all do)
If yes: the municipal norm overrides TEK17 §15-8 requirements where stricter
```

---

## Norwegian-Specific Rules That Generic AI Gets Wrong

These are rules that distinguish Norwegian practice from generic Eurocode application. Generic AI models frequently make these errors:

| What generic AI assumes | What Norwegian practice requires |
|---|---|
| Snow load 1.0–2.0 kN/m² (European baseline) | Norway: 2.5–9.0 kN/m² depending on zone. Mountain areas are extreme. |
| No quick clay risk (rare in Europe) | Kvikkleire is uniquely Norwegian — post-glacial marine clay. Must check NGU before any foundation work in Østlandet, Trøndelag, or coastal areas |
| Permit required for anything structural | Norway has søknadsfri system: many works ≤ 15 m² are exempt. But the exemptions are specific — always verify |
| Licensed engineer certifies work | Norway uses ansvarssystem: ansvarlig søker, prosjekterende, utførende — THREE separate licensed roles, each with specific responsibilities |
| Insulation upgrade is minor | Norwegian climate requires major insulation (TEK17 U-values are strict by European standards). Upgrades may require søknad if changing character |
| Heritage = listed building | Norway has SEFRAK (informational), Gul liste (local interest), bevaringsverdig (municipality decision), and fredet (Riksantikvaren/KML §15) — four separate levels with different requirements |
| Old building can be renovated freely | Pre-1940 Norwegian buildings in heritage zones require Byantikvaren consultation regardless of formal listing |
| Frost depth 0.5–1.0 m (central Europe) | Norway: 1.5–3.0 m depending on latitude and soil. Fjellhamar/Oslo area: 1.5–1.8 m in frost-susceptible soil |
| Concrete grades C20–C30 (modern) | 1920s–1960s Norwegian buildings used B200 (≈C16/20) — lower strength than generic assumptions |
| Any historical rebar is mild steel | Pre-1970 Norwegian buildings used H-40 (≈B400) and older E-stål grades — different from both modern and other European historical practices |
| Stormwater goes to municipal drain | TEK17 §15-8 (2024): stormwater must be handled on-site first. Municipal VA-norms often require infiltration or detention before connection |

---

## Adding a New Municipality

When a new municipality appears in a project, document what you find here:

```
## [Municipality Name] Kommune

**Contact:** [email]
**Portal:** [URL]
**Snow zone:** [TEK17 zone] — s_k = [value] kN/m²
**Heritage authority:** [Byantikvaren / fylkeskommunen]
**Known local rules:** [list]
**Known geology:** [soil type, kvikkleire risk]
**Stormwater norm:** [yes/no, where to find it]
```

---

*This skill is updated when a new municipality is encountered in a project.*
*Current coverage: Lørenskog/Lillestrøm, Oslo, Bergen, Trondheim, Stavanger/Sandnes*
*Last updated: 2026-08-09*
