---
name: electrical-nek400
description: Norwegian electrical installation standards (NEK 400, IEC 60364), circuit design, grounding, protection, renewable energy integration, EV charging, solar electrical systems, heat pump electrical requirements, inspection protocols.
triggers: [NEK 400, electrical, strøm, spenning, krets, circuit, cable, kabel, grounding, jording, RCD, RCCB, overcurrent, overstrøm, fault, feil, EV charging, ladestasjoner, solar, solceller, heat pump, varmepumpe, ventilasjonsanlegg, elektrisk installasjon, inspeksjon, testing, IP rating, feuchtigkeitsmessung, wet room, våtrom, distribution, fordeling, earthing, jordforbindelse, surge protection, overspenningsvern, harmonics, resonance]
load_with: [building-code-tek17]
safety_level: critical
license: Proprietary
---

# Skill: Electrical — NEK 400 (IEC 60364 Norwegian)

## ⚠️ DISCLAIMER

This skill is for reference and educational purposes only. **Electrical installation design, inspection, and approval must be performed by a licensed electrician (strømmeister with NEK 400 competence).** Bob cannot replace professional electrical engineering. Errors in electrical work can cause fire, electrocution, or system failure.

---

## Domain

Norwegian electrical installation standards — NEK 400 (Norsk Elektroteknisk Komité; based on IEC 60364), circuit design, cable sizing, grounding systems, protection devices, renewable energy integration (solar, heat pumps, EV charging), inspection/testing protocols, and commissioning.

NEK 400 is mandatory for all new electrical installations in Norway. Failure to comply voids insurance and creates legal liability.

---

## Key Standards & References

| Standard | Coverage | Authority |
|---|---|---|
| **NEK 400** | Main installation standard (IEC 60364 adapted for Norway) | NEK (Norsk Elektroteknisk Komité) |
| **NS 3031** | Energy performance of buildings (includes electrical efficiency) | Standardiseringskomiteen |
| **TEK17 Chapter 14** | Energy requirements (increasingly delegated to NS 3031 + NEK 400) | DiBK |
| **IEC 60364** | International standard for low-voltage electrical installations | International Electrotechnical Commission |
| **IEC 62196** | EV charging connectors and safety | IEC |
| **NS 3950** | Renewable energy — solar PV systems safety | Standardiseringskomiteen |
| **Forskrift om elektriske installasjoner** | Electrical Installation Regulation (enforces NEK 400) | Arbeidsdepartementet |

---

## Core Concepts

### 1. Electrical System Architecture

**Main components:**
- **Service entrance (hovedopptak):** Where power enters the building (utility supply or renewable generation)
- **Main breaker (hovedbryter):** Disconnect device
- **Distribution board (hovedtavle):** Central hub for circuit protection and organization
- **Circuits (kretser):** Individual branch circuits serving loads
- **Grounding system (jordingssystem):** Safety path for fault currents

### 2. Grounding Systems (Jording)

Norway uses primarily **TT grounding** (two independent earth electrodes: one at utility, one at building):

| System | Earth Path | Use Case | Fault Current | RCD Required |
|---|---|---|---|---|
| **TT** | Separate electrodes (utility + building) | Common in rural areas, solar + batteries | Low (depends on electrode resistance) | YES (mandatory) |
| **TN-S** | Neutral + separate earth from utility | Urban areas with good grounding | High (low impedance) | YES (recommended) |
| **TN-C-S** | Combined neutral/earth until building, then separate | Increasingly rare in Norway | Medium | YES (recommended) |

**Electrode resistance:**
- Target: ≤ 10 Ω (practical minimum in Norway: 5–20 Ω depending on soil)
- Measured annually or after structural changes
- Poor grounding forces lower breaker sensitivity → longer fault clearing → greater shock risk

### 3. Cable Sizing

Cable size determined by:
1. **Load current (A):** Sum of all connected devices on circuit
2. **Installation method:** Embedded, conduit, exposed, buried
3. **Ambient temperature (°C):** Standard = 30°C; adjust if hotter
4. **Voltage drop limit:** Max 3% for branch circuits (NIOSH rule)
5. **Short-circuit capacity:** Cable must not be damaged by fault current

**Common Norwegian installations:**

| Application | Typical Circuit | Cable Size | Breaker Rating | Notes |
|---|---|---|---|---|
| Lighting (20–30 luminaires) | 1 circuit, 10A | 1.5 mm² | 10A | Grouped by room/zone |
| General outlets (20 sockets) | 1–2 circuits, 16A | 2.5 mm² | 16A | Wet rooms use 20A + RCD |
| Kitchen heavy loads | 2–3 circuits, 20A each | 4 mm² | 20A | Dishwasher, cooktop separate |
| Heating element (3–5 kW) | 1 circuit, 16–25A | 4–6 mm² | 16–25A | Direct connection to main board |
| EV charging (3.7–22 kW) | 1 circuit, 16–32A | 6–16 mm² | 16–32A | Wallbox hardwired; residual current supervision |
| Heat pump (9–15 kW) | 3-phase, 16–32A | 6–16 mm² per phase | 16–32A | Requires 3-phase supply; balancing needed |
| Solar inverter (5–10 kW) | 1 circuit, 16–25A | 4–10 mm² | 16–25A | DC side + AC side breakers |

### 4. Protection Devices

**Main breakers (sikringsautomater):**
- **Type B:** Trips at 3–5× rated current (instant) — unsuitable for residential
- **Type C:** Trips at 5–10× rated current — standard for lighting, outlets
- **Type D:** Trips at 10–20× rated current — for motors, transformers
- **Type K/Z:** Special characteristics (rarely used in residential)

**RCD (Residual Current Device / jordfeilbryter):**
- Detects small leakage currents (as low as 30 mA)
- **Class A (AC):** Standard residential
- **Class B (AC + DC):** Required for solar, some heat pump systems
- **Class A + superimposed DC (Si):** Required for solar + battery systems
- **Mandatory locations:**
  - All wet areas (bathrooms, kitchens, laundry)
  - All outdoor/garden outlets
  - All circuits serving pools, saunas
  - All circuits for renewable energy systems

**Surge protection (overspenningsvern):**
- Required at main board if building has lightning strike history or is in high-risk zone
- Additional surge protection recommended for:
  - Heat pump controllers
  - Solar inverters
  - EV charger electronics
  - Network infrastructure (fiber modem, WiFi)

### 5. Renewable Energy Integration

#### Solar (Solceller)

**DC side (before inverter):**
- String combiner box with breakers + fuses
- DC wiring in conduit, UV-resistant cable
- Grounding: 2 × electrode system (solar frame + inverter case)
- Protection: DC circuit breaker + surge protector

**AC side (after inverter):**
- AC breaker (Type B or C) rated for inverter output
- RCD Class B (detects AC + DC leakage)
- Bidirectional meter (if grid-connected)
- Islanding protection (prevents back-feeding if grid fails)

**Commissioning checklist:**
- [ ] DC string voltage (open circuit)
- [ ] AC output frequency + phase (grid-connected)
- [ ] Earth loop resistance
- [ ] RCD trip test (push test button)
- [ ] Inverter firmware + firmware updates
- [ ] Performance data logging (check actual yield vs. PVSyst estimate)

#### Heat Pump (Varmepumpe)

**Electrical requirements:**
- **Single-phase (monofase):** ≤ 7–8 kW (typical residential, 230V, 16–25A)
- **Three-phase (3-fas):** > 8 kW (requires 400V supply)
- **Protection:** Soft starter or variable frequency drive (VFD) to reduce inrush current
- **RCD:** Class B or Si (some modern heat pumps inject DC ripple)
- **Grounding:** Separate earth to heat pump enclosure (metal chassis)

**Integration with solar:**
- Load shifting: Run heat pump during peak solar hours (morning/afternoon)
- Battery backup: Heat pump off-grid operation (rare; requires oversized battery)
- Hybrid logic: Monitor solar output → boost heating during surplus generation

#### EV Charging (Ladestasjoner)

**Charging levels:**
- **Mode 2 (portable):** 1.4–2.3 kW, 230V, 10A — not recommended for permanent installation
- **Mode 3 (wall-mounted, cable tethered):** 3.7–22 kW, 230V/400V, 16–32A — standard residential
- **Mode 4 (DC fast charging):** 50–350 kW — public infrastructure only

**Residential wallbox (Mode 3, 11 kW typical):**
- 400V 3-phase, 16A per phase (requires 3-phase supply in most Norwegian homes)
- **Cabling:** 3×6 mm² + earth (buried or conduit from main board to garage)
- **Protection:** RCD Type B (EV battery chargers may inject DC) or Type A + superimposed DC Si
- **Breaker:** 3×16A or 3×20A (C-type)
- **Residual current supervision:** Wallbox monitors charging cable for damage; halts charging if fault detected
- **Circuit isolation:** Contactor or relay to disconnect wallbox from supply when not charging

**Commissioning:**
- [ ] Ground continuity (test between charger frame and building earth)
- [ ] Voltage + frequency at wallbox location
- [ ] Test with vehicle: Charging current ramp-up, safe shutdown, fault scenarios
- [ ] Earth loop resistance (should be < 2 Ω for safety margin)

### 6. Inspection & Testing

**Mandatory testing (Vedlikeholds- og inspeksjonsprotokoll):**

| Test | Frequency | Method | Pass Criteria |
|---|---|---|---|
| **Visual inspection** | Annually | Walk-through for damage, corrosion, heat marks | No visible damage |
| **Earth loop resistance** | Annually | Clamp meter or earth resistance tester | < 2 Ω (residential) |
| **RCD trip test** | Annually | Press test button on each RCD | Trips within 0.1 s |
| **Load circuit test** | Every 3 years | Check for overheating under full load | Temperature rise < 20°C |
| **Fault simulation** | Every 5 years | Inject small fault current, verify breaker trips | Trip time per NEK 400 tables |
| **Documentation** | With each test | Log results + date; corrective actions | Dated records kept on file |

**Who performs testing:**
- **Routine inspections:** Building owner or authorized facility manager
- **Commissioning:** Licensed electrician (strømmeister)
- **Major repairs:** Licensed electrician
- **Insurance verification:** Third-party inspector (required if claim filed)

---

## Common Scenarios & Escalation

### Scenario 1: Adding a Heat Pump (9 kW)

**Electrical assessment:**
1. **Current supply:** Check if 3-phase available at building entrance
   - If YES: Confirm 16A per phase available (48A total); may need capacity upgrade at utility
   - If NO: Request 3-phase connection from utility (cost: 5k–15k NOK, 4–8 week lead time)
2. **Main board capacity:** Heat pump breaker + existing loads must not exceed 25A per phase
3. **Grounding:** Test earth electrode resistance (target ≤ 2 Ω); if > 5 Ω, upgrade electrode
4. **Soft starter:** VFD or soft starter recommended to reduce inrush current (smooths load profile)
5. **Commissioning:** Licensed electrician tests voltage, frequency, thermal protection, contactor operation

**Integration with solar (if present):**
- Load shifting logic: Monitor solar inverter output → boost heat pump compressor frequency during peak generation
- Over-generation protection: If solar > heat pump demand, excess goes to grid (or battery if installed)

### Scenario 2: Solar Installation (10 kW)

**Electrical sequence:**
1. **Structural support:** Verify roof can handle panel + mounting load (load-bearing assessment)
2. **DC system design:**
   - String configuration: Typically 2–3 strings of panels in series
   - Combiner box: Breaker + fuse per string; earthing lug
   - Inverter selection: Must be Class B or Si (accepts 400V 3-phase OR single-phase + neutral)
3. **AC connection:**
   - RCD Type B at inverter output (detects DC leakage from battery charge/discharge)
   - Bidirectional meter installation (if grid-connected)
   - Relay for island detection (prevent backfeeding if grid fails)
4. **Earthing:**
   - DC earth: Separate electrode or bonded to building earth (check local utility rules)
   - AC earth: Use building main earth
   - Test: Earth loop resistance ≤ 2 Ω
5. **Commissioning + documentation:**
   - Performance baseline (PVSyst estimate vs. actual yield Year 1)
   - Annual electrical inspection (RCD test, earth test, visual)
   - Keep inverter data logs for 5+ years (warranty claims, insurance)

### Scenario 3: Bathroom Renovation (Wet Room Classification)

**Electrical requirements:**
- **RCD protection:** All outlets in bathroom zone (including vent fan, heated mirror, etc.)
- **Safety zones (IEC 60364-7-701):** 
  - Zone 0 (inside tub/shower): No electrical equipment except low-voltage (≤ 12V AC) fixtures
  - Zone 1 (directly above tub/shower, 2.25 m height): Only submersible or IPX4-rated equipment (recessed lights, fan, heated mirror)
  - Zone 2 (1–0.6 m horizontally from Zone 1): IPX1-rated minimum (splashing possible)
  - Outside zones: Normal IP20 standard (but still RCD-protected)
- **Moisture detection:** If bathroom lacks active ventilation, consider moisture sensor to detect high humidity → alert homeowner
- **GFCI/RCD testing:** Monthly test button pushes; replace RCD if won't trip

**Escalation flag:** If bathroom renovation involves wall removal or structural changes near electrical main board, consult electrician before starting work.

### Scenario 4: Off-Grid System (Solar + Battery + Backup Generator)

**Critical electrical decisions:**
1. **Grounding configuration:** TT system becomes complex with DC battery storage + inverter
   - **Negative grounding:** Battery negative bonded to earth (most common, simple)
   - **Floating ground:** Neither pole grounded (requires sophisticated fault detection)
   - Recommendation: Consult equipment manufacturer + licensed electrician (very specialized)
2. **Battery charging paths:**
   - Solar inverter → battery charger → battery (when solar > load)
   - Grid charger → battery (manual, if grid available; rare off-grid scenario)
   - Generator → battery charger (backup only)
3. **Load shedding logic:** If battery < 20% SOC, shed non-essential loads (heating, hot water, EV charging)
4. **Transfer switch:** Automatic changeover between solar/battery → generator (prevents backfeeding)
5. **Surge protection:** Critical (inverter can be damaged by generator frequency transients)

**Escalation:** Off-grid systems require specialized design. **ALWAYS escalate to licensed electrician + renewable energy consultant.**

---

## Escalation Flags

When to REQUIRE licensed electrician involvement:

- [ ] **New electrical supply:** Request 3-phase, expand main board capacity, upgrade from single-phase
- [ ] **Heat pump, EV charger, or solar installation:** Always requires licensed electrician (mandatory by Forskrift om elektriske installasjoner)
- [ ] **Wet room renovation:** RCD installation, moisture-rated equipment selection
- [ ] **Off-grid systems:** Solar + battery + generator load management
- [ ] **Fault current testing:** Any testing involving intentional fault injection
- [ ] **Grounding upgrade:** If earth loop resistance > 5 Ω
- [ ] **Safety repairs:** Burn marks, overheating, flickering lights, tripped breakers (potential fire hazard)
- [ ] **Code compliance verification:** If building > 50 years old or major renovation planned

---

## Coordination with Other Disciplines

**With structural engineer:**
- Conduit routing through beams/walls (structural integrity preserved)
- Solar panel mounting loads
- Heat pump outdoor unit vibration (isolation pads; noise transmission)

**With HVAC/mechanical:**
- Heat pump electrical + heating/cooling coordination (staging)
- Ventilation damper motor control (24V DC often)
- Heat recovery ventilator (ERV) control wiring

**With plumbing:**
- Hot water tank controller integration with heat pump
- Fluid pressure sensors for heating loop
- Drain pan safety switch (water detection near HVAC equipment)

**With building code/architect:**
- EV charging location accessibility (parking geometry)
- Solar panel visibility from street (heritage/zoning concerns)
- Main board location (safety, accessibility for future upgrades)

---

## Common Regulatory Traps

1. **"I'll do the electrical work myself":** Illegal without license. Insurance voids. Building inspector can refuse occupancy.
2. **Oversizing breakers to prevent nuisance trips:** Creates fire hazard. Cable can overheat before breaker trips.
3. **Skipping RCD in older homes:** Mandatory requirement. If missing, install as part of any renovation.
4. **DIY solar + battery without proper isolation:** Backfeeding can electrocute utility workers repairing lines. Criminal liability.
5. **EV charger on standard outlet:** 16A outlet on 20A circuit = fire risk. Wallbox must be hardwired + dedicated circuit.

---

## References

- **NEK 400** — [https://www.nek.no/produkter/nek-400/](https://www.nek.no/produkter/nek-400/) (Norwegian Electrotechnical Commission)
- **IEC 60364** — [https://www.electropedia.org/](https://www.electropedia.org/) (International standard)
- **Forskrift om elektriske installasjoner** — [https://lovdata.no](https://lovdata.no) (Norwegian electrical installation regulation)
- **NS 3031** — Energy performance of buildings (includes electrical efficiency requirements)
- **NS 3950** — Renewable energy systems safety (solar, wind, small hydro)
- **DiBK TEK17** — Chapter 14 (Energy) increasingly cross-references NEK 400 + NS standards

---

## Bob's Role

Bob can help with:
- ✅ Identifying electrical compliance gaps during project review
- ✅ Understanding renewable energy (solar, heat pump) electrical architecture
- ✅ Explaining RCD/grounding basics to homeowners
- ✅ Flagging when licensed electrician involvement is mandatory
- ✅ Reviewing project documents for electrical escalation risks

Bob cannot:
- ❌ Design electrical circuits (requires licensed engineer)
- ❌ Select cable sizes (requires load analysis)
- ❌ Approve grounding systems (requires testing)
- ❌ Commission any system for operation
- ❌ Replace professional electrical inspection

**When electrical is a major project element, escalate to licensed electrician (strømmeister med NEK 400 kompetanse) before proceeding.**
