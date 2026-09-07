---
name: hvac-mechanical
description: Norwegian HVAC — ventilation, heating (heat pumps, district heating, radiators), cooling, ductwork, commissioning, TEK17 Chapter 14 compliance, noise control, maintenance.
triggers: [HVAC, ventilation, ventilasjonsanlegg, varme, heating, kjøling, cooling, varmepumpe, heat pump, lufting, lufing, luftkvalitet, air quality, energi, energy, TEK17, Chapter 14, U-verdi, U-value, inneklima, indoor climate, komfort, comfort, lydnivå, noise, støy, vedlikehold, maintenance, NS 3031, NS 3951, FVF, friskluftsystemer, fläktventilation, eksoss, exhaust, tilluft, supply air, avluft, extract air, filter, filtrering, varmegjenvinding, heat recovery, ERV, MVHR, radiator, radiatorovn, termostat, thermostatic valve, trykktap, pressure drop, luftmengde, air flow, lufthastighet, air velocity, lyddemping, sound attenuation]
load_with: [building-code-tek17, electrical-nek400]
safety_level: high
license: Proprietary
---

# Skill: HVAC & Mechanical Systems (NS 3031, NS 3951)

## ⚠️ DISCLAIMER

This skill is for reference and educational purposes. HVAC design, installation, and commissioning must be performed by licensed HVAC engineers and installers. Poor system design causes discomfort, energy waste, mold growth, and structural damage. Bob cannot replace professional HVAC consultation.

---

## Trust Boundary

**Bob may, on his own analysis:** explain ventilation strategy options, identify TEK17 §14 requirements, and flag an obviously undersized or missing system from a description.

**Bob may flag only as preliminary:** duct sizing, airflow rates, or heat-load estimates — illustrative, not a design basis.

**Always requires a licensed HVAC engineer/installer before it can be acted on:** system design, commissioning, and any measure affecting airtightness/fire compartmentation.

---

## Domain

Norwegian HVAC (Heating, Ventilation, Air-Conditioning) standards — NS 3031 (Energy performance of buildings), NS 3951 (Ventilation for buildings), ventilation system types (mechanical/natural), heating systems (heat pumps, district heating, radiators, boilers), cooling (active/passive), ductwork design, commissioning protocols, noise control, maintenance schedules, and indoor climate quality (inneklima).

---

## Key Standards & References

| Standard | Coverage | Authority |
|---|---|---|
| **NS 3031** | Energy performance of buildings (includes HVAC efficiency, heating demand) | Standardiseringskomiteen |
| **NS 3951** | Ventilation for buildings (air quality, flow rates, safety) | Standardiseringskomiteen |
| **NS 3940** | Energy installations (heat pump sizing, performance, efficiency) | Standardiseringskomiteen |
| **TEK17 Chapter 14** | Energy requirements (U-values, net heating demand netto energibehov, renewable integration) | DiBK |
| **TEK17 Chapter 15** | Indoor climate (temperature, humidity, air quality targets) | DiBK |
| **EN 12098-1** | Building automation and control (thermostat requirements) | European Committee |
| **ISO 3744** | Acoustic noise testing (equipment dB(A) ratings) | ISO |
| **Forskrift om arbeidsmiljø** | Workplace requirements (ventilation in commercial buildings) | Arbeidsdepartementet |

---

## Core Concepts

### 1. Ventilation System Types

**Mechanical ventilation (Mekanisk ventilasjon):**

| Type | Supply | Extract | Heat Recovery | Use Case | Pros | Cons |
|---|---|---|---|---|---|---|
| **Exhaust only (Avtrekkssystem)** | Natural infiltration through leakage + planned openings | Mechanical exhaust fan (kitchen, bathroom) | None | Older homes, passive houses (rare) | Simple, low cost | Poor control; drafts; uneven distribution |
| **Supply only (Tilluftssystem)** | Mechanical supply (filtered, preheated) | Natural exhaust through openings | Partial (air-to-air heat exchanger in supply) | New energy-efficient homes | Better control; filtered air | Requires balanced infiltration design |
| **Balanced with heat recovery (MVHR / Varmegjenvinding)** | Mechanical supply (filtered, preheated) | Mechanical extract | Plate or rotary heat exchanger (80–95% efficiency) | Standard modern construction (TEK17) | High efficiency; excellent control; indoor air quality | Complex; regular filter maintenance needed |
| **Decentralized (Desentralisert ventilasjon)** | Individual room units (wall-mounted or window-mounted) | Same units extract air locally | Varies (unit-dependent) | Retrofits, room-by-room upgrades | Retrofit-friendly; room-level control | Limited heat recovery; noise if not well-designed |

**Natural ventilation (Naturlig ventilasjon):**
- Wind pressure + stack effect drive air flow through openings
- Minimal mechanical components (window operators, dampers)
- Used in passive houses, heritage buildings (constraints), or as backup/supplementary
- Challenge: Cannot guarantee air flow on calm days → risk of inadequate ventilation or stale indoor air

### 2. Heating Systems

**Heat pump (Varmepumpe):**

| Type | Source | Efficiency (COP) | Cost | Notes |
|---|---|---|---|---|
| **Air-to-air (Luft-til-luft)** | Ambient air (outdoor unit) | 2.5–3.5 in typical Norwegian climate | Low–medium | Common for residential; outdoor unit noise; seasonal efficiency loss in deep winter |
| **Air-to-water (Luft-til-vann)** | Ambient air → heats water loop | 3.0–4.0 | Medium | Integrates with radiators, underfloor heating, hot water tank |
| **Ground-source (Jord-til-vann)** | Borehole (150–200 m deep) → stable ~8°C year-round | 4.0–5.0 | High (borehole: 5k–10k NOK) | Best efficiency; minimal noise; space requirement for borehole |
| **Water-source (Vann-til-vann)** | Lake/river water (if available) | 4.0–5.0 | High (site-dependent) | Excellent if water source available; environmental permits required |

**COP = Coefficient of Performance** = Heating output (kW) / Electrical input (kW)
- Norwegian standard test: EN 14511 @ –7°C outdoor, +35°C water return (seasonal average)
- Real-world performance varies: Winter –15°C may drop COP to 2.5; Summer may exceed 4.0 if heating demand low

**District heating (Fjernvarme):**
- Hot water supplied by central utility plant (biomass, waste heat, solar thermal)
- Building requires heat exchanger + circulation pump
- Cost: Connection fee (3k–10k NOK) + per-kWh charge (0.08–0.15 NOK/kWh typical)
- Advantage: No on-site equipment, no maintenance burden; lower annual cost in urban areas
- Disadvantage: Less flexibility; dependent on utility supply continuity

**Electric resistance (Elektrisk varme):**
- Direct heating element (immersion heater in tank, or resistive baseboards)
- COP = 1.0 (all electricity → heat, 100% efficient at point of use, but high upstream electricity losses)
- Acceptable for supplementary heating; NOT recommended as primary in new construction (violates TEK17 Chapter 14 efficiency targets)
- Common for backup/emergency heating in heat pump systems

**Boiler (Kjele):**
- Gas, oil, or wood-fired combustion
- Rare in modern Norwegian residential (gas rare; oil outdated; biomass OK but complex)
- If used: Requires combustion air intake, flue gas exhaust (through roof), annual maintenance
- Efficiency: 85–95% (modern condensing); heat losses in flue

### 3. Distribution & Delivery

**Radiators (Radiatorer):**
- Hot water circulates through finned aluminum or steel panels
- Thermostatic valve (termostatventil) controls room temperature
- Typical flow: 60–80°C supply, 50–60°C return
- Sized per room heating load (calculated from insulation U-values, window area, orientation, outdoor design temperature)

**Underfloor heating (Gulvvarme):**
- Warm water pipes embedded in concrete slab or under wooden floor
- Lower supply temperature (35–45°C) → higher heat pump COP
- Slower response to setpoint changes (large thermal mass)
- Risk if not carefully designed: Uneven heating; cold spots; floor temperature > 29°C discomfort

**Warm air (Varmluft):**
- Air ducted from central unit → supply vents in rooms
- Less common in Norwegian residential (noise, draft comfort issues)
- May be used in commercial, open-plan, or high-ceilings spaces

### 4. Indoor Climate Targets (Inneklima) — TEK17 Chapter 15

| Parameter | Target Range | Measurement | Health/Comfort Impact |
|---|---|---|---|
| **Temperature (Temperatur)** | 20–22°C (winter); 23–25°C comfortable | Thermostat / wall sensor | Below 18°C: discomfort, cold feet; above 25°C: overheating |
| **Relative humidity (Relativ fuktighet)** | 30–60% | Hygrometer / automated sensor | Below 30%: dry skin, respiratory irritation; above 60%: mold risk, dust mite proliferation |
| **Air change rate (Luftskifte)** | 0.3–0.5 ACH (air changes per hour) in winter; higher in summer with natural ventilation | Fan speed setting / CO₂ probe (proxy) | Below 0.3: stale air, CO₂ buildup (> 1000 ppm); above 0.7: excessive draft, energy waste |
| **CO₂ concentration (CO₂ nivå)** | < 800 ppm (excellent); < 1200 ppm (acceptable); > 1500 ppm (poor) | CO₂ sensor | Elevated CO₂ correlates with reduced cognitive performance, lethargy |
| **Acoustic privacy (Lydnivå)** | ≤ 30 dB(A) in bedrooms; ≤ 35 dB(A) in living areas (nighttime external noise) | Decibel meter | Noise ≥ 50 dB(A) disrupts sleep; impacts long-term health |
| **Radiant temperature asymmetry (Strålingsubalanse)** | < 10°C difference between warm surface (sun, radiator) and cold surface (exterior wall, window) | Infrared thermometer | Cold wall radiates to occupant → discomfort (cold feet/face) even if mean air temperature OK |

### 5. Energy Efficiency (TEK17 Chapter 14)

**Netto energibehov (Net heating demand):**
Calculated as: Heating load (W) = (U-value × Area × ΔT) for each building element

Example for 150 m² house:
- Exterior walls: U = 0.18 W/m²K, Area = 200 m² (net) → 36 W/K
- Windows: U = 1.2 W/m²K, Area = 25 m² → 30 W/K
- Roof: U = 0.10 W/m²K, Area = 150 m² → 15 W/K
- Floor: U = 0.10 W/m²K, Area = 150 m² → 15 W/K
- **Total load:** 96 W/K
- **At –14°C outdoor, 21°C indoor:** 96 × 35 = 3,360 W = 3.36 kW design heating power

**Annual heating demand (kWh/year):**
- Norwegian average: 20–30 kWh/m²/year for well-insulated homes (TEK17 requirement ~ 21 kWh/m²/year)
- Old homes (1950–1990): 50–100 kWh/m²/year
- Passive houses: < 15 kWh/m²/year (extreme insulation)

**Seasonal performance factor (SPF):**
Real-world heat pump efficiency over full heating season
- SPF = Total useful heat delivered (kWh) / Total electrical energy consumed (kWh)
- Target: ≥ 3.0 (i.e., for every 1 kWh electricity, 3 kWh heat)
- Measured via energy meter + heat meter over 12 months

### 6. Commissioning & Balancing (Inregulering)

**Ductwork balancing:**
1. Measure actual air flow at each supply/extract grille (anemometer)
2. Compare to design (from system drawings)
3. Adjust dampers (spjeldventiler) in branches to match design flow
4. Goal: ±10% of design flow per room

**Pressure drop testing:**
- Fan power loss if ductwork is too small or too long
- Low pressure drop = smaller fan motor = lower energy, less noise
- Target: Total system pressure drop ≤ 100 Pa (fan work measured in Pascal)
- Measure with manometer (U-tube or digital)

**Temperature verification:**
- Supply air temperature ≤ 15°C in summer (comfort); ≥ 18°C winter (frost protection)
- Heat recovery effectiveness: (T_supply – T_outdoor) / (T_extract – T_outdoor) × 100%
  - Target: ≥ 75%
- Return water temperature from radiators (should drop 10–15°C from supply)

**Noise testing:**
- Measure at grilles, in ducts, at fan unit
- Target: ≤ 35 dB(A) in living rooms, ≤ 30 dB(A) in bedrooms (per EN 12098)
- If > target: Add acoustic lining, larger ducts, lower fan speed, vibration isolation mounts

**Documentation:**
- Commissioning report (Igangsettingsrapport) must be signed by installer + system manufacturer
- Included: Flow measurements, temperature readings, noise levels, filter replacement schedule, warranty details

---

## Common Scenarios & Escalation

### Scenario 1: Heat Pump Installation in Existing Home

**Design phase:**
1. **Heating load calculation:** U-value audit (measure insulation, window type) → design heating power (kW)
   - Old home (1970s): Likely 8–12 kW needed
   - Renovated (TEK17-compliant): 5–7 kW
2. **Heat pump sizing:** Select unit ≤ design load (oversizing wastes money + efficiency)
3. **Distribution choice:**
   - **Option A:** Keep radiators (air-to-water heat pump @ 55°C supply)
   - **Option B:** Add underfloor heating (lower supply temp → higher COP, but slower response)
   - **Option C:** Replace radiators with larger units (achieve comfort with lower supply temp)
4. **Electrical integration:** Coordinate with electrician
   - 3-phase 16A supply (5–7 kW) or 3-phase 25A (9–11 kW)
   - Soft starter to reduce inrush current
   - Heat pump controller may require 24V control wiring (run from main board)
5. **Outdoor unit placement:**
   - Minimum 1 m from property line (noise ordinance)
   - Not directly under windows (noise complaint risk)
   - Access for maintenance (annual filter cleaning, refrigerant check)

**Installation phase:**
- Refrigerant line insulation + sealing (moisture protection)
- Pressure test (5 bar nitrogen, 24 h hold)
- Evacuate (vacuum pump, remove air/moisture)
- Charge refrigerant (weight per manufacturer spec)
- Electrical termination (soft starter, contactor, RCD)
- Hydronic loop fill (water + glycol antifreeze if ground-source)

**Commissioning:**
- [ ] COP test at standard conditions (–7°C outdoor, 35°C water return)
- [ ] Thermostatic valve calibration (target room temperatures achieved)
- [ ] Backup element test (if auxiliary electric heater present)
- [ ] Annual maintenance schedule documented (filter, refrigerant check, compressor noise baseline)

**Escalation:** Heat pump installation ALWAYS requires licensed HVAC installer (fører med varmepumpekompetanse). Improper refrigerant charging or electrical connection can damage compressor or create safety hazard.

### Scenario 2: Ventilation System Retrofit (Existing Home → MVHR)

**Site assessment:**
1. **Existing insulation level:** Measure U-values (will dictate ventilation air change rate)
2. **Ductwork routing:** Identify pathways through ceiling/walls (minimize runs > 15 m; friction loss increases)
3. **Equipment location:** Utility room, attic, or crawlspace? (access for filter maintenance)
4. **Electrical supply:** 230V outlet within 3–5 m of unit (reduce voltage drop)

**Design:**
1. **Air change rate:** Typically 0.4 ACH (air change hour) winter; higher in summer if operable windows
   - Calculate: Total air volume (m³) × 0.4 / 60 min = Required supply airflow (m³/s)
   - Example: 250 m³ house × 0.4 / 60 = 1.67 m³/s ≈ 100 m³/h per fan
2. **Supply/extract balance:** Must be equal (prevent pressure imbalance)
3. **Duct sizing:** Larger ducts = lower pressure drop = smaller motor = quieter
   - Typical: 160–250 mm diameter main ducts; 100–150 mm branches
4. **Heat recovery:** Plate or rotary core efficiency ≥ 80% (typical: 85–90%)

**Installation sequence:**
1. Ductwork installation (insulated, sealed with sealant tape at joints)
2. Unit mounted (vibration isolation pads to reduce transmission noise)
3. Electrical connection (230V + control wiring)
4. Filters inserted (pre-filters for coarse; fine filters for pollen/PM2.5)
5. Balancing dampers set (preliminary; final tuning during commissioning)
6. System test run (fan operation, no air leaks, no excessive noise)

**Commissioning (Inregulering):**
- Measure air flow at each room (supply + extract)
- Adjust dampers to achieve ±10% of design flow
- Measure supply air temperature (heat recovery performance)
- Noise measurement at grilles (target ≤ 35 dB(A) living areas)
- Establish filter replacement schedule (every 6–12 months depending on use)

**Long-term operation:**
- Winter: Close external damper in winter if extreme cold (frost risk); adjust fan speed to maintain 0.3–0.4 ACH
- Summer: Open damper, increase fan speed or use night cooling (cool outdoor air when T < 18°C)
- Annual maintenance: Replace filters, check for condensation/frost in heat exchanger core

**Escalation:** MVHR system design + commissioning should be done by HVAC professional. Poor commissioning results in inadequate ventilation or excessive energy use.

### Scenario 3: Indoor Climate Issues (Cold, Drafty, or Humid)

**Diagnostics:**

| Symptom | Likely Cause | Quick Check | Solution |
|---|---|---|---|
| **Cold feet/face despite 21°C air temp** | Radiant asymmetry (cold window/exterior wall) | Measure wall surface temp with IR gun; should be > 15°C | Improve window U-value; relocate thermostat to mean radiant sensor; add thermal curtains |
| **Stuffy air, CO₂ > 1000 ppm** | Inadequate ventilation (blocked grille, fan off, low setpoint) | Check CO₂ sensor; verify fan running; listen for airflow | Increase fan speed; check filter (may be clogged); verify damper position |
| **Humidity > 65%, mold forming in corner** | Inadequate ventilation + thermal bridge (cold corner) | Measure humidity + corner surface temp | Increase extract air in bathroom/kitchen (fan runtime); improve insulation at corner (risk expensive; may require exterior work) |
| **Draughts/windy feeling** | Excessive air velocity through grille (fan too fast, duct too small) | Anemometer reading > 0.3 m/s at grille = drafty | Reduce fan speed if possible; increase grille area (larger diffuser); add acoustic lining |
| **Noise from HVAC system** | Fan speed too high, ductwork undersized, vibration transmission | Measure noise + identify source (unit itself, ductwork, grille) | Reduce fan speed; increase duct size (retrofit expensive); add vibration isolation feet under unit |

### Scenario 4: Heat Pump + Solar Integration

**Load shifting strategy:**
1. **Monitor solar output** (inverter API or manual reading)
2. **Boost heat pump during peak solar hours** (10 AM–3 PM):
   - Increase setpoint or increase compressor frequency (if variable-capacity unit)
   - Heat water tank to maximum (store thermal energy)
3. **Reduce or stop heating during low-solar hours** (evening/night):
   - Rely on stored heat from tank; coast down setpoint
4. **Battery coordination** (if present):
   - Prioritize solar → heat pump over battery charging (thermal storage is cheaper than electrical)

**System architecture:**
- Solar inverter + battery inverter (if hybrid) must communicate with heat pump controller
- Requires smart relay or automation system (costs 3k–8k NOK; integration complexity medium-high)
- Payback: Reduced grid electricity use, but depends on electricity price + solar resource (Southern Norway better than north)

---

## Escalation Flags

When to REQUIRE HVAC professional involvement:

- [ ] **Heat pump sizing/installation:** Always requires licensed HVAC installer
- [ ] **Ventilation system design:** System with ductwork, fan, heat recovery
- [ ] **Indoor climate problems:** Persistent cold spots, humidity, or CO₂ issues
- [ ] **Commissioning/balancing:** Air flow measurement, temperature verification, noise testing
- [ ] **Energy performance validation:** Seasonal COP measurement, heating demand calculation
- [ ] **Distribution system redesign:** Adding radiators, changing from air to water heating, underfloor heating retrofit
- [ ] **Acoustic issues:** Noise > 40 dB(A) from HVAC system

---

## Coordination with Other Disciplines

**With electrical:**
- Heat pump 3-phase supply + soft starter (reduces inrush)
- Fan motor size + soft-start coordination
- Smart thermostats (WiFi, integration with other building controls)
- Battery charging prioritization (if solar + battery present)

**With plumbing:**
- Hot water tank integration (solar thermal or heat pump backup)
- Radiator/underfloor heating loop pressure + temperature coordination
- Drain pan safety switch (water detection near mechanical room)
- Fluid transfer lines (insulation, routing, support)

**With structural:**
- Ductwork routing (ceiling depth impact, insulation R-value addition)
- Mechanical room location (floor loading, vibration transmission to living spaces)
- Borehole access (if ground-source heat pump — space requirement, drilling equipment access)

**With building code/architect:**
- Solar integration impact on roof aesthetics
- Heat pump outdoor unit visibility + noise (zoning setback requirements)
- Ventilation grille placement (exterior appearance, security)

---

## Common Regulatory Traps

1. **"I'll just close vents in unused rooms to save energy":** Creates imbalance → pressure differential → infiltration through cracks elsewhere. Worse efficiency overall.
2. **Undersized ducts to save cost:** High friction loss forces larger fan motor + higher energy use + noise.
3. **No commissioning:** System installed but never balanced or tested → underperformance + poor indoor climate.
4. **Heat pump rated at +7°C, installed in –15°C climate:** Performance collapses in winter; must add backup electric resistance (defeats efficiency goal).
5. **Thermostatic valve set wrong:** Excessive heating or inadequate comfort (must be correctly calibrated).

---

## References

- **NS 3031** — Energy performance of buildings
- **NS 3951** — Ventilation for buildings
- **NS 3940** — Energy installations (heat pump design + performance)
- **TEK17 Chapter 14 & 15** — Energy + indoor climate
- **EN 14511** — Heat pump testing standard
- **ISO 3744** — Acoustic noise measurement
- **DiBK Byggdetaljsamlingen** — Construction details (ventilation, heating integration)

---

## Bob's Role

Bob can help with:
- ✅ Understanding HVAC system types and tradeoffs
- ✅ Identifying indoor climate problems
- ✅ Explaining heat pump COP and energy efficiency basics
- ✅ Coordinating HVAC + electrical + plumbing integration
- ✅ Flagging when HVAC professional is needed

Bob cannot:
- ❌ Design heating/ventilation systems (requires HVAC engineer)
- ❌ Size heat pumps or ductwork
- ❌ Calculate seasonal COP or energy demand
- ❌ Commission or balance any system
- ❌ Troubleshoot equipment failures

**For any HVAC project beyond basic troubleshooting, escalate to licensed HVAC installer/designer.**
