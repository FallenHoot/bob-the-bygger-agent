---
name: technical-education-support
description: Simplifies technical jargon into plain language with real-world analogies and points to learning resources, when a user seems unfamiliar with construction terminology.
triggers: [what does that mean, can you explain, I don't understand, simpler, too technical, help me understand, what's a, define, learning, teach me, resources, links, references]
load_with: []
safety_level: low
license: Proprietary
---

# Skill: Technical Education Support

## Purpose

When user appears confused by technical terminology or asks Bob to explain something, Bob:
1. **Translates jargon to plain language** with real-world analogies
2. **Provides concrete examples** (visual, quantitative, story-based)
3. **Shares learning resources** (links, references, documents)
4. **Gauges understanding** and adjusts depth (beginner vs. advanced)
5. **Builds confidence** that technical building concepts are learnable
6. **Supports both languages** — Provides Norwegian ↔ English term pairs when explaining technical concepts

---

## Bilingual Technical Glossary (Norwegian ↔ English)

Quick reference for translating technical terms between Norwegian and English:

| Norwegian | English | Category | Example |
|---|---|---|---|
| **Strukturelle termer** | **Structural terms** | | |
| Lastfordeling | Load path | Structural | "Lastfordelingen går fra tak → vegger → fundament" |
| Bærende vegg | Bearing wall | Structural | "Denne veggen er bærende og kan ikke fjernes" |
| Gjennomheng | Deflection | Structural | "Gjennomhenget skal være mindre enn spennvidden/250" |
| Moment | Bending moment | Structural | "Momentet øker med lengden på spennvidden" |
| Spennvidde | Span | Structural | "Spennvidden er 6 meter fra vegg til vegg" |
| Skjærkraft | Shear force | Structural | "Skjærkraften virker ved opplagringspunktene" |
| **Materialer** | **Materials** | | |
| Betonggklasse | Concrete grade | Material | "C30 betong er vanlig for boligbygg" |
| Stålkvalitet | Steel grade | Material | "S275 stål er standard i Europa" |
| Tømmerkvalitet | Timber grade | Material | "C24 tømmer klassifiseres som strukturelt tømmer" |
| U-verdi | U-value | Material | "Ny vindu skal ha U-verdi ≤ 1,2 W/m²K" |
| **Regulering** | **Regulation** | | |
| Teknisk Forskrift 2017 | TEK17 | Code | "TEK17 krever energieffektivitet for nybygg" |
| Plan- og bygningsloven | Planning and Building Act (PBL) | Code | "PBL regulerer søknadsprosessen" |
| Byggesøknad | Building permit / søknad | Permit | "Du trenger byggesøknad for betydelig ombygging" |
| Dispensasjon | Exemption / waiver | Permit | "Du kan søke om dispensasjon fra TEK17 for fredede bygninger" |
| SEFRAK | SEFRAK register (cultural heritage) | Heritage | "Hvis bygningen er SEFRAK-registrert, må Byantikvaren godkjenne endringer" |
| Byantikvaren | Heritage Authority (Byantikvaren) | Heritage | "Byantikvaren vurderer fredete hus" |
| **HVAC/Mekanisk** | **HVAC/Mechanical** | | |
| Varmepumpe | Heat pump | HVAC | "En luft-til-vann varmepumpe har COP omkring 3,5" |
| COP | Coefficient of Performance | HVAC | "COP 3,0 betyr at 1 kWh elektrisitet gir 3 kWh varme" |
| Ventilasjon | Ventilation | HVAC | "Mekanisk ventilasjon med varmegjenvinding (MVHR)" |
| Varmegjenvinding | Heat recovery | HVAC | "Virkningsgrad på varmegjenvinding er typisk 85%" |
| **Elektro** | **Electrical** | | |
| Strøm | Electricity / current | Electrical | "Huset har 3-fase strømtilkobling" |
| RCD / Jordfeilbryter | Residual Current Device (RCD/RCCB) | Electrical | "RCD må installeres i våtrom" |
| Jording | Grounding / earthing | Electrical | "Jordingssystemet må ha motstand ≤ 10 Ω" |
| Sikringsautomat | Circuit breaker | Electrical | "Hver krets må ha egne sikringsautomater" |
| **Rør/VA** | **Plumbing** | | |
| Vannforsyning | Water supply | Plumbing | "Vannforsyningen kommer fra kommunal ledning" |
| Avløp | Drainage | Plumbing | "Avløpet må ha fall på minst 0,5%" |
| Septiktank | Septic tank | Plumbing | "Septiktanken må tømmes hvert 2-5 år" |
| Sifon | Trap | Plumbing | "Sifonen under vasken holder tilbake kloakkgass" |
| **Arealtermer** | **Area/Space terms** | | |
| Etasje | Floor / storey | Space | "Bygningen har tre etasjer" |
| Loft | Ceiling / attic | Space | "Loftet er 2,4 meter høyt" |
| Gulv | Floor | Space | "Gulvet er betong med varmekabler" |
| Vegg | Wall | Space | "Ytterveggen er 300 mm isolert" |
| Fasade | Facade | Space | "Fasaden er klinket murstein" |
| **Tilstandsvurdering** | **Condition Assessment** | | |
| Fukt | Moisture / damp | Condition | "Fuktighet over 60% øker muggrisko" |
| Sprekk | Crack | Condition | "Det er små sprekker i betongen" |
| Setning | Settlement | Condition | "Bygningen har gjennomgått en setning på 5 cm" |
| Korrosjon | Corrosion | Condition | "Rustning av armeringen er et problem" |

---

## How Bob Uses This Glossary

When explaining technical concepts **to a Norwegian speaker** → Bob uses Norwegian term + simple explanation + analogy
When explaining **to an English speaker** → Bob uses English term + simple explanation + analogy

**Example (Norwegian):**
```
Bruker spør: "Hva er lastfordeling?"
Bob svarer: "Lastfordeling = hvor vekten går. Som vann som renner ned en bakke, 
går strukturens vekt fra taket → ned gjennom veggene → ned til fundamentet. 
Hvis noe av kjeden er brutt, kollapser hele bygningen. Tenk på det som domino-steiner stilt opp vertikalt."
```

**Example (English):**
```
User asks: "What's a load path?"
Bob responds: "Load path = where weight goes. Like water flowing downhill, structural 
loads flow from roof → walls → foundation → ground. If any part breaks, entire building fails. 
Think of it as dominoes stacked vertically."
```

---

## Common Technical Terms Explained (Simple & Linked)

### Structural Terms

**Load Path**
- **Simple:** "Where does weight go?" Like water flowing downhill, structural loads flow from the roof → walls → foundation → ground.
- **Example:** When you stand on a floor, your weight travels through the wooden planks → through joists (beams) → through walls → down to concrete footings in the ground. If any part is broken, weight can't flow → floor fails.
- **Visual:** Imagine dominoes stacked vertically. Remove the bottom domino, top ones fall. Load path = the chain of dominoes.
- **Link:** [Eurocode 2 (Concrete) basics](https://www.en-standard.eu/en-1992-1-1-2004-eurocode-2/) — official but dense; see SINTEF guides instead.

**Bearing (Bearing Wall, Bearing Point)**
- **Simple:** A wall or post that's "working" — actively holding up weight from above.
- **Example:** The wall between your kitchen and living room may be non-bearing (just a divider). But the wall at the front of your house IS bearing (holds up the roof). Don't remove a bearing wall without replacing it.
- **Visual:** Like a waiter holding a tray of glasses. Remove the waiter's arm? Glasses fall. That's a bearing point.

**Deflection**
- **Simple:** Bending or sagging over time. A beam that's too thin or loaded too heavily will sag slightly.
- **Tolerance:** Usually OK if sag < span/250. Example: 6-meter span allows up to 2.4 cm sag (not ideal, but not failure).
- **Analogy:** Trampoline. Step on it, it bends. More weight = more bend. Too much bend = feels unstable.
- **Link:** [Structural Deflection Limits](https://www.structures.unsw.edu.au/undergraduate-resources) — university-friendly explanations.

**Moment (Bending Moment)**
- **Simple:** Twisting or bending force. A beam experiences moment (bending stress) when loaded.
- **Example:** Bend a stick. The harder you push, the bigger the moment, and the more likely it snaps.
- **Formula (simple):** Moment = Load × Distance. Bigger load or longer distance = bigger moment = stronger beam needed.
- **Link:** Khan Academy has great animation videos on moments/forces: [Intro to Moments](https://www.khanacademy.org/)

**Span**
- **Simple:** Distance a beam must reach between supports (like a bridge between two cliffs).
- **Example:** A 6-meter span = beam must stretch 6 meters from one wall to the opposite wall.
- **Matters because:** Longer span = heavier/deeper beam needed (cost, headroom impact).

**Shear (Shear Force, Shear Stress)**
- **Simple:** Sliding or tearing force. When a beam is loaded, the fibers try to slide past each other.
- **Example:** Cutting with scissors. The force pushing the two blades together tries to "shear" (cut) the paper.
- **Analogy:** Cards stacked on a table. Push the bottom card sideways hard enough, cards above slide/shear relative to it.

---

### Material Terms

**Concrete Grade (C30, C40, C50)**
- **Simple:** The "strength" of concrete. Higher number = stronger concrete, more expensive.
- **What it means:** C30 = 30 Newtons/mm² (30 MPa) compressive strength. Typical residential. C50 = 50 MPa, used when more strength needed.
- **Real world:** C30 is fine for floors, walls. C50 used for bridge decks, heavy loading.
- **Age matters:** Concrete takes 28 days to reach full strength (why construction delays happen).
- **Link:** [Concrete Strength Explained](https://www.britannica.com/technology/concrete) — short, clear overview.

**Steel Grade (S275, S355)**
- **Simple:** Like concrete grades, but for steel. S275 = 275 MPa yield strength (common European standard).
- **Comparison:** S275 is standard; S355 is stronger/more expensive; rarely need higher.
- **Why it matters:** You can't just use any steel. Structural engineer specifies which grade based on loads.

**Timber Grade (C24, C30, Glulam)**
- **Simple:** Classification of wood strength. C24 = common structural timber. Glulam = engineered wood (stronger, consistent).
- **Real:** Glulam is wood pieces glued together for consistent strength (natural wood has knots, variations). More expensive but more reliable.
- **Link:** [Eurocode 5 (Timber)](https://www.en-standard.eu/en-1995-1-1-2004/) — see SINTEF summaries instead for plain language.

**U-Value (Thermal Transmittance)**
- **Simple:** How much heat escapes through a material. Lower = better (less heat loss).
- **Units:** W/m²K (Watts per square meter per degree Kelvin difference).
- **Examples:**
  - Old single-pane window: U ≈ 5.9 W/m²K (lot of heat loss)
  - Modern double-glazed: U ≈ 1.2–1.5 W/m²K (much better)
  - Well-insulated wall: U ≈ 0.18 W/m²K (very good)
- **TEK17 requirement:** Residential windows max U = 1.2 W/m²K.
- **Link:** [U-Values Explained](https://www.thegreenbuilder.co.uk/u-values-explained/) — visual comparisons, easy.

---

### Regulatory Terms (TEK17, PBL)

**TEK17 (Teknisk Forskrift 2017)**
- **Simple:** Norwegian building code. Rules for everything: how strong walls must be, how much insulation, fire safety, etc.
- **Why it exists:** Protects people. Without it, builders could cut corners → unsafe buildings.
- **Chapters:**
  - Chapter 7: Fire safety (evacuate quickly)
  - Chapter 14: Energy (keep heat in, don't waste energy)
  - Chapter 15: Indoor climate (comfortable temperature, good air quality)
  - Chapter 17: Climate/GHG (sustainable, low carbon)
- **Link:** [DiBK (Directive for Building Quality)](https://www.dibk.no/) — official Norwegian source (Norwegian language).

**Søknad (Building Permit)**
- **Simple:** Permission you need from the municipality before starting work.
- **When needed:** Any "significant" construction. Some small work exempt (SAK10: solar panels ≤ 25 kW, insulation, EV charging).
- **Process:** Submit drawings + calculations → municipal review (4–8 weeks) → approval or requests for changes.
- **Cost:** Varies; typically 5k–15k NOK administrative fee.
- **Link:** [Your local municipality's building department website](https://www.kommuner.no/) — municipality-specific process.

**Dispensasjon (Exemption)**
- **Simple:** Permission to break the rules. Example: Building too close to property line (normally not allowed) → apply for dispensasjon → maybe granted.
- **When used:** Can't meet TEK17 standard for heritage building → apply for exemption (may be approved if justified).
- **Not guaranteed:** Municipality decides case-by-case.

**SEFRAK (Register of Cultural Heritage)**
- **Simple:** Database of old buildings in Norway that are considered historically valuable.
- **What it means:** If your building is SEFRAK-listed, you can't modify it without approval from Byantikvaren (heritage authority).
- **Grades:** A = highest cultural value; B = significant; C = noteworthy.
- **Link:** [SEFRAK Registry Search](https://sefrak.ra.no/) — searchable database (Norwegian).

---

### HVAC/MEP Terms

**COP (Coefficient of Performance, Heat Pump)**
- **Simple:** Efficiency rating for heat pumps. COP 3.0 = for every 1 unit of electricity, you get 3 units of heat.
- **Why it matters:** Higher COP = lower operating cost. Goal: COP ≥ 3.0 for residential heat pumps.
- **Real world:** Norwegian winter at –7°C, heat pump might achieve COP 2.5–3.0 (still good). Efficiency drops in extreme cold (–15°C).
- **Link:** [Heat Pump COP Explained](https://www.heatpumpskennisbank.nl/) — Dutch source but applies internationally.

**RCD / RCCB (Residual Current Device)**
- **Simple:** Safety device that stops electricity flow if it detects a leak (prevents electrocution).
- **Analogy:** Like a fire extinguisher for electricity. If you touch a live wire, RCD cuts power in milliseconds.
- **Where needed:** Bathrooms, outdoor outlets, anywhere water is present.
- **Link:** [RCD Explained - IET](https://www.theiet.org/wiring-matters/) — electrical safety basics.

**ACH (Air Changes Per Hour)**
- **Simple:** How many times the entire room's air is replaced per hour. Higher = more fresh air.
- **Typical:** Residential buildings: 0.3–0.5 ACH in winter (energy-efficient), up to 1.0 ACH in summer (natural ventilation).
- **Why it matters:** Too low = stuffy air, CO₂ buildup. Too high = waste energy heating/cooling.
- **Link:** [Ventilation Guidelines](https://www.ashrae.org/) — ASHRAE standards; technical but authoritative.

---

### Site/Soil Terms

**Bearing Capacity (Soil)**
- **Simple:** How much weight the soil can support before it compresses/fails.
- **Example:** Sandy soil might support 100 kN/m² (weak). Bedrock supports 1000+ kN/m² (very strong).
- **Why it matters:** If soil is weak, must dig deeper to bedrock or use piles/footings (expensive).
- **Link:** [Geotechnical Basics](https://www.usgs.gov/faqs/what-soil-bearing-capacity) — USGS plain language.

**Kvikkleire (Quick Clay)**
- **Simple:** Rare clay found in Norway/Sweden that can suddenly lose strength if disturbed (can collapse like quicksand).
- **Risk zone:** Central Norway, valleys, coastal areas. Map available from NGU (Norwegian Geological Survey).
- **If present:** Requires special foundation design; geotechnical engineer must assess.
- **Link:** [NGU Quick Clay Map](https://www.ngu.no/topics/natural-hazards/quick-clay) — searchable by location (Norwegian).

**Q200 (Flood Risk Standard)**
- **Simple:** A flood that happens once every 200 years. TEK17 requires buildings in Q200 zones to survive flooding.
- **Why it matters:** If your site is in a flood zone, you must design accordingly (higher floor elevation, flood-resistant materials, pumps).
- **Check it:** NVE (Norwegian Water Resources Authority) publishes flood maps.
- **Link:** [NVE Flood Maps](https://www.nve.no/english/water-resources-and-flood-management/) — public searchable maps.

---

## Educational Strategy: How Bob Explains

### When User Shows Confusion

**Bob's response:**

1. **Pause & acknowledge:** "I used some technical terms there. Let me explain what they mean."

2. **Translate to plain language:** Use simple words, avoid jargon. One sentence max per concept.

3. **Provide concrete example:** Real-world scenario (house, building, city) that illustrates the concept.

4. **Visual analogy:** Comparison to everyday objects (cards stacking, water flowing, trampoline, etc.).

5. **Share a link:** Point to learning resource (video, article, diagram) if available.

6. **Ask back:** "Does that make sense? Any part you'd like me to dig deeper on?"

### Example Dialog

**User:** "The inspector said my beam's U-value is too high. What does that mean?"

**Bob:** "The U-value measures heat loss. High U-value = a lot of heat escapes through the beam (bad). Low U-value = less heat escapes (good).

Think of it like a blanket. A thin blanket (high U-value) doesn't keep you warm. A thick blanket (low U-value) keeps you warmer. Beams, windows, walls all have U-values.

For residential windows in Norway, the rule (TEK17) says U ≤ 1.2 W/m²K. Your beam doesn't meet that, meaning it's not insulated well enough.

Solution: Add insulation around the beam, or if it's inside the heated space, it might not matter.

Want to understand more? Here's a simple explainer: [Building U-Values Explained](https://example.com/u-values)"

---

## Common Knowledge Gaps & Resources

### Building Basics (No Experience)

**"I'm not a builder, I own a 1970s house and want to understand what's happening."**

Bob's strategy:
- Start VERY simple. Assume no technical knowledge.
- Use household analogies (roof = umbrella, insulation = jacket, etc.)
- Share: [How Buildings Work (TED-Ed)](https://www.youtube.com/) — short animated videos
- Recommend: "Building Science 101" courses (free, online)
- Link: [Catalyst.ca - Building Science](https://www.buildingscience.com/) — plain-language explainers

### Code/Regulation Questions

**"What's TEK17 and why should I care?"**

Bob explains:
- It's Norway's building safety rules (like traffic laws for buildings)
- Protects: You (safe), environment (energy efficient), future owners (resale value)
- Covers: Structure (won't collapse), fire (can escape), energy (bills reasonable), climate (low carbon)
- If you modify: Must meet TEK17 (or get exemption)

Links:
- [DiBK Official](https://www.dibk.no/) (Norwegian authority, comprehensive)
- [SINTEF Building Research](https://www.sintef.no/) (Norwegian research institute; excellent explanations)
- [Statsbygg (State Buildings)](https://www.statsbygg.no/) — practical guidance from government builder

### Structural Questions

**"How do I know if my wall can be removed?"**

Bob's approach:
- Explain load path: weight flows from roof → walls → foundation
- Show: If you remove a bearing wall, the roof weight must go somewhere else (beam + posts)
- Need: Professional engineer to calculate (not guesswork)
- Don't ask Bob alone; ask structural engineer (this is critical safety decision)

Links:
- [Understanding Structural Loads](https://www.explainthatstuff.com/structures.html) — simple, visual
- [Eurocode 2 Basics](https://www.en-standard.eu/) — official standard (dense, but authoritative)
- [Local structural engineer contact info](https://www.tekna.no/) — professional association (Norwegian)

### Energy/Efficiency Questions

**"What's a heat pump and is it worth the cost?"**

Bob explains:
- Heat pump = machine that moves heat from outside to inside (or vice versa in summer)
- Why it works: Even at –10°C, air contains heat; heat pump extracts it (efficient, saves money)
- Cost: 80k–150k NOK installed; payback ~10–15 years through lower heating bills
- Reality: Better in cold climates (Norway = ideal), worse in already-heated places

Links:
- [Heat Pump Guide for Homeowners](https://www.energiverket.no/) — Norwegian energy utility (plain language)
- [Compare Energy Systems Calculator](https://www.klimavenlig.no/) — interactive tool (Norwegian)
- [Heat Pump Association](https://www.heat-pump-association.org/) — international technical info

---

## Resource Library (Curated Links)

### Official Norwegian Resources

| Resource | URL | Content | Audience |
|---|---|---|---|
| **DiBK (Building Quality Director)** | https://www.dibk.no/ | Building code, regulations, permits | Professionals + public |
| **SINTEF Building Research** | https://www.sintef.no/byggforsk/ | Moisture, energy, construction details | Professionals + educators |
| **NVE (Water Resources Authority)** | https://www.nve.no/ | Flood maps, natural hazards | Professionals + homeowners |
| **NGU (Geological Survey)** | https://www.ngu.no/ | Ground conditions, quick clay, geology | Professionals + curious |
| **Statsbygg (State Buildings)** | https://www.statsbygg.no/ | Design guidance, building standards | Architects + builders |
| **FinnByggebok** | https://www.finnbyggebok.no/ | Construction details, best practices | Builders + specifiers |

### International Resources (English)

| Resource | URL | Content | Audience |
|---|---|---|---|
| **Eurocode Standards** | https://www.en-standard.eu/ | Structural, fire, energy design codes | Engineers |
| **Building Science Explained** | https://www.buildingscience.com/ | Moisture, air leakage, energy | Professionals + homeowners |
| **TED-Ed: How Buildings Work** | https://www.youtube.com/teded | Animated building concept videos | General audience |
| **Explain That Stuff** | https://www.explainthatstuff.com/structures.html | Structures, materials, physics | Students + curious |
| **ASHRAE (Heating/Cooling)** | https://www.ashrae.org/ | HVAC design standards + guides | Engineers + installers |
| **IET (Electrical Safety)** | https://www.theiet.org/ | Wiring, electrical safety, codes | Electricians + homeowners |

---

## Bob's Educational Principles

When teaching technical concepts, Bob:

✅ **Uses analogies to everyday life** (blanket = insulation, water flow = load path, etc.)

✅ **Provides real numbers** (not vague: "This slab can hold X kg/m²" not "probably OK")

✅ **Shares official links** (not Bob's interpretation, but authoritative source)

✅ **Assesses understanding** ("Does that make sense? Ask if unclear.")

✅ **Scales to audience** (homeowner gets simple; engineer gets detailed)

✅ **Admits limits** ("I'm an AI; consult professional engineer for final sign-off")

✅ **Provides action steps** ("Here's what to do next..." with links/contacts)

❌ **Never uses jargon without explanation** (every technical term defined)

❌ **Never assumes prior knowledge** (ask if unsure: "Are you familiar with...?")

❌ **Never sends only links** (explains first, then provides link to go deeper)

❌ **Never oversimplifies to the point of wrong** (accuracy > simplicity)

---

## Integration

This skill is loaded whenever user:
- Asks "what does X mean?"
- Says "I don't understand"
- Asks for "simpler" explanation
- Requests links or resources
- Shows confusion (Bob detects via language like "confused", "lost", "don't get it")

**Primary goal:** Make technical building knowledge accessible to non-engineers, so homeowners, contractors, and curious people can understand what's happening.

*"If the user doesn't understand, Bob hasn't explained it well yet. It's Bob's job to find better analogies, simpler words, or better resources — not the user's job to 'learn' technical jargon."*
