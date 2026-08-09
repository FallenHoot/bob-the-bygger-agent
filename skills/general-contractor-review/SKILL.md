---
name: general-contractor-review
description: General contractor drawing analysis — load paths, structural support verification, dimensional coordination, trade dependencies, constructability assessment, common modification pitfalls, risk identification, sequencing implications, cost/scope impacts.
triggers: [drawing analysis, code review, design review, modification feasibility, wall removal, beam addition, opening, aperture, load path, support, post, column, foundation, coordination, constructability, what if, what's wrong, needs improvement, things to consider, trade coordination, sequencing, dependencies, site impact, feasibility assessment]
load_with: [structural-engineering, building-code-tek17, architectural-drawing-reading, electrical-nek400, hvac-mechanical, plumbing-vs6050]
safety_level: critical
license: Proprietary
---

# Skill: General Contractor Review & Drawing Analysis

## Purpose

When architectural drawings arrive, Bob (as general contractor) performs a **holistic review** to identify:
- ✅ Structural feasibility of proposed changes
- ✅ Coordination issues across trades (electrical, HVAC, plumbing, structural, heritage)
- ✅ Common pitfalls and constructability concerns
- ✅ Things to improve or reconsider
- ✅ Sequence and timing implications
- ✅ Cost/scope impacts

This is the **eyes of the experienced GC** looking at drawings and saying: "Here's what's wrong. Here's what needs work. Here's what to think about before breaking ground."

---

## Drawing Review Methodology

### Phase 1: Understand the Scope (5 minutes)

**Questions to ask:**
1. **What is being modified?** (Wall removal? Addition? Renovation? New construction?)
2. **Where?** (Which rooms, floors, exterior faces?)
3. **Why?** (Open plan? Accessibility? Energy upgrade? Functional need?)
4. **Constraints?** (Budget, timeline, heritage protection, occupied/unoccupied during work?)

**Red flags at this stage:**
- Scope poorly defined ("make it feel bigger" vs. "remove wall between kitchen-dining")
- No clear reason for proposed change (design-driven vs. functional-driven affects constructability)
- Unrealistic timeline (major structural work compressed into too-short schedule)

---

### Phase 2: Structural Logic (10–15 minutes)

**For any modification involving walls, openings, loads:**

#### A. Load Path Analysis

**Always ask: WHERE DOES THE LOAD GO?**

1. **Identify loads above the modification:**
   - Weight of walls, floor, roof above? (Visual scan of drawing: Are there upper floors, roof?)
   - Is the element being removed BEARING (supporting weight) or NON-BEARING (partition)?
   
2. **Check existing supports:**
   - What's currently holding up the loads? (Bearing walls, columns, beams — all visible on structural drawing?)
   - If removing a wall, where do those loads transfer? (Must have alternative support designed)
   
3. **Verify proposed support:**
   - Is a beam being added? What size? What material? (Structural calc required — outside Bob's scope, but verify one exists)
   - Are new columns/posts required? Where do they bear? (Down to footings? Must verify)
   - Can existing footings support the new load? (Soil bearing capacity assessment needed)

**Common pitfall:**
- Removing a load-bearing wall without adding beam → ceiling/roof sags or collapses
- Adding a beam but undersizing it or supporting it inadequately

**Example: Wall Removal with Beam Addition**

```
BEFORE (load-bearing wall):
┌─────────────────┐  (Roof/upper floor loads)
│      WALL       │  (bearing load from above)
└─────────────────┘
(Foundation below)

AFTER (wall removed, beam added):
┌─────────────────┐
│     BEAM        │  (Must span distance, support all above loads)
│   ▌         ▌   │  (Posts at each end, bearing on footings)
└────▌───────▌────┘
     ▲        ▲
   Posts at  Posts at
   each end  each end
```

**Questions to verify:**
- [ ] Beam span adequate for load? (Structural engineer calc exists?)
- [ ] Posts/columns sized correctly? (Loads, materials, connections?)
- [ ] Footings beneath posts capable of supporting concentrated load? (Soil bearing capacity verified?)
- [ ] Connections between beam + posts detailed? (Bolted? Welded? Bearing plates specified?)

#### B. Dimensional Verification

1. **Check floor-to-ceiling heights:**
   - If removing wall in upper floor, does beam depth eat into headroom?
   - Minimum headroom per TEK17: 2.1 m (living areas), 2.0 m (kitchens), 1.9 m (corridors)
   - Example: 8" steel beam (200 mm) may reduce headroom from 2.4 m to 2.2 m (acceptable, tight but OK)

2. **Opening sizes (if adding windows/doors in new location):**
   - TEK17 fenestration: Minimum 5–10% of floor area for daylight
   - Verify new opening doesn't reduce daylighting below minimum

3. **Clearances around new structure:**
   - New posts/columns: Do they obstruct views, doors, circulation?
   - Ductwork/pipe headroom: HVAC, electrical conduit running above? (May need to reroute)

---

### Phase 3: Trade Coordination (10–15 minutes)

**For each trade affected, ask: "What conflicts, dependencies, or relocations required?"**

#### Electrical

- [ ] **Are there electrical outlets/switches/fixtures in the wall being removed?** (Must relocate)
- [ ] **Is the main panel or distribution board nearby?** (New circuits need routing; may conflict with structural work)
- [ ] **New fixtures being added?** (New circuits, RCD protection per wet room code?)
- [ ] **Beam location:** Do electrical runs go through it? (Notching/drilling may weaken structure; coordinate with structural engineer)

**Questions:**
- [ ] Licensed electrician consulted? Drawing shows new circuit locations?
- [ ] Temporary power for construction planned? (Safer than DIY extension cords)

#### HVAC/Mechanical

- [ ] **Supply/return air ductwork routing:** Does proposed change require duct relocation?
- [ ] **Thermostat placement:** If room is being reconfigured, is new thermostat location sensible? (Should be away from sun, drafts, occupied zone)
- [ ] **Heat source location:** If adding heating zone or relocating hot water use, does existing boiler/heat pump capacity suffice?
- [ ] **Ventilation:** Does proposed modification affect ventilation balance? (Closing off one room, opening another?)

**Questions:**
- [ ] HVAC engineer reviewed layout? Changes documented?
- [ ] Commissioning/rebalancing scheduled post-work?

#### Plumbing

- [ ] **Is there existing plumbing in the wall/floor being modified?** (Water supply, drain, vent stack?)
- [ ] **Drainage routing:** If floor plan changes, do drain lines maintain 0.5–1.0% slope?
- [ ] **Traps & vents:** New fixtures need traps + vent connection (can use existing stack if nearby, or new vent required)
- [ ] **Winterization:** Any new runs in unheated spaces? (Insulation, heat tape needed?)

**Questions:**
- [ ] Licensed plumber consulted? Rerouting shown on drawings?
- [ ] Vent stack location clear? (Routing through structural elements must be coordinated)

#### Structural

- [ ] **Load paths verified?** (Existing supports sufficient or new beam/posts needed?)
- [ ] **Connection details:** How does new beam/post connect to existing structure? (Bolted plate? Welded? Bearing pad?)
- [ ] **Deflection & vibration:** Large opening or cantilever can cause floor movement (acceptable limit per Eurocode: L/250 to L/400 depending on use)
- [ ] **Material compatibility:** If existing structure is timber + new beam is steel, how do they join? (Different thermal expansion)

**Questions:**
- [ ] Structural engineer designed beam/posts? Calcs provided?
- [ ] Load test required before occupancy?

#### Heritage (if applicable)

- [ ] **Building listed (SEFRAK)?** If YES: Any modification to exterior, interior character, original materials requires Byantikvaren approval (see heritage-preservation skill)
- [ ] **Original structural elements visible/significant?** (Timber framing, stone walls, exposed beams — preserve if possible)
- [ ] **Material matching:** If removing/replacing elements, must use compatible materials (color, texture, profile)

**Questions:**
- [ ] Byantikvaren consulted? Formal approval or exemption documented?
- [ ] Heritage impact assessment completed?

---

### Phase 4: Constructability & Logistics (10 minutes)

#### Sequencing

**Ask: In what order must work happen?**

Example: **Wall Removal + Beam Addition**

1. **Temporary support:** Install temporary bracing/posts to hold up ceiling while removing wall (required by safety code)
2. **Utilities relocation:** Move electrical, plumbing, HVAC out of wall (before removal)
3. **Wall demolition:** Remove wall carefully (dust control, asbestos survey if old building?)
4. **Foundation prep:** If new posts required, install footings (may require excavation, concrete pour, cure time)
5. **Beam installation:** Once footings set (concrete cured), install beam + permanent posts
6. **Remove temporary bracing:** Once beam load-tested
7. **Finishes:** Drywall, painting, flooring, trim
8. **Utilities reinstallation:** New circuits, ducts, pipes in new locations

**Critical dependencies:**
- Footings must cure 7 days before beam weight applied
- Temporary bracing must stay in place until beam fully installed + tested
- Utilities must be moved BEFORE wall removal (can't be done mid-work)

#### Site Constraints

- [ ] **Occupied during work?** (Dust, noise, power disruption management required)
- [ ] **Adjacent occupied spaces?** (Noise, vibration, dust mitigation for neighbors)
- [ ] **Utility shutoffs:** Can electric/water be interrupted during relocation? (Temporary supply lines needed?)
- [ ] **Debris removal:** Where does demolition waste go? (Dumpster size, access, weight)
- [ ] **Material delivery:** Where do new materials (beam, lumber, finishes) arrive and stage? (Site congestion risk)

#### Equipment & Access

- [ ] **Heavy equipment:** Beam installation may need crane, boom truck (access to site? width, height, weight limits?)
- [ ] **Temporary support structures:** Shoring equipment rental cost (often $500–2k for major projects)
- [ ] **Safety systems:** Fall protection, dust barriers, temporary lighting (costs money; timeline impact)

---

### Phase 5: Cost & Timeline Impact Assessment (5 minutes)

**Estimate rough order of magnitude:**

| Aspect | Impact | Consideration |
|---|---|---|
| **Temporary support (shoring)** | +1–2 weeks timeline; +5k–15k NOK cost | Depends on complexity; longer for large spans |
| **Utility relocation** | +1–2 weeks; +10k–30k NOK | Electrical, plumbing, HVAC all need new routing + testing |
| **Foundation work (if new footings)** | +2–3 weeks (concrete cure time); +20k–50k NOK | Soil conditions matter (excavation cost varies) |
| **Structural fabrication (beam, posts, connections)** | +2–4 weeks (fab + delivery); +30k–100k NOK | Steel expensive; timber cheaper but may have deflection issues |
| **Finishes (drywall, painting, flooring)** | +2–3 weeks; +20k–50k NOK | Standard for any interior work |
| **Testing & commissioning (electrical, HVAC, structural)** | +1 week; +5k–10k NOK | Required by code; often overlooked in timeline |

**Total rough estimate:** 8–12 weeks; 90k–255k NOK for major modification (wall removal + beam addition + utilities + finishes)

---

## Common Modification Scenarios

### Scenario 1: Wall Removal (Load-Bearing)

**What to assess:**

1. **Is the wall load-bearing?** (Ask: Walls above? Roof load?) → If YES, requires beam
2. **Beam span required:** Distance the wall spans (measure from bearing points on each end)
3. **Load magnitude:** Area above the wall × roof snow load (estimated at +5–10 kN/m² in Norway) + dead load of structure
4. **Support locations:** Where will posts/columns sit? On existing footings? New footings required?

**Common pitfalls:**
- Underestimating beam size (looks small; insufficient capacity)
- Inadequate post support (not anchored to foundation; can shift)
- Headroom lost due to beam depth (< 2.1 m minimum)
- Electrical/plumbing in wall not relocated (delays construction, quality issues)

**Questions to ask architect/engineer:**
- [ ] Structural calculations provided? (Beam size, material, connections?)
- [ ] Posts sized? Footings designed? (Bearing capacity verified?)
- [ ] Temporary support plan in place?

---

### Scenario 2: Adding an Opening (Window or Door in Existing Wall)

**What to assess:**

1. **Wall type:** Exterior (weather-exposed) or interior (simpler)?
2. **Load-bearing?** (Ask: Loads above?)
3. **Opening size:** Must structural lintel (horizontal beam) support loads above?
4. **Utilities:** Electrical, plumbing, ductwork in wall path? (May require rerouting)
5. **Daylighting:** New window brings light to interior; check if meets TEK17 fenestration minimum

**Common pitfalls:**
- Lintel too small (loads above cause deflection, cracking drywall/plaster above opening)
- Opening too wide → lintel spans too far → requires unnecessarily large/expensive beam
- Electrical wiring in opening path damaged during installation

---

### Scenario 3: Floor/Ceiling Modification (Raising, Lowering, Creating Open Plan)

**What to assess:**

1. **Structural system:** Timber joists? Concrete slab? Steel beams? (Affects method)
2. **Load redistribution:** Removing intermediate supports (posts, walls) → loads concentrate elsewhere
3. **HVAC ductwork:** Does it run in ceiling? New ducting routing required? (May lose headroom)
4. **Electrical conduit:** Runs in ceiling? Rerouting needed?
5. **Accessibility:** Does new ceiling height meet minimum 2.1 m per TEK17?
6. **Acoustics:** Open plan changes sound propagation (noise from kitchen to living room increases)

**Timeline impact:** Significant; sequencing complex (support + ductwork + electrical + structural work all interdependent)

---

### Scenario 4: Exterior Wall Work (New Window, Door, or Adding Extension)

**What to assess:**

1. **Insulation value:** New opening reduces overall U-value; must comply with TEK17 Chapter 14 (max 1.2 W/m² for residential windows)
2. **Weather protection:** New opening exposes interior to water, wind; flashing details critical
3. **Thermal bridging:** Window frames, sills can transfer heat; design must minimize
4. **Heritage concerns:** If building is SEFRAK-listed, modifications to exterior profile may require Byantikvaren approval
5. **Structural:** Lintel support if removing wall section for door/window opening

**Common pitfalls:**
- Window installed before flashing detail approved → water infiltration, mold
- No thermal break between frame + structure → condensation, thermal loss
- Window placement interferes with existing structure (conflicts with joists, rafters, etc.)

---

## Escalation Triggers (Red Flags for Professional Review)

**Escalate immediately if:**

- [ ] **Load-bearing wall removal without beam design** → Structural failure risk
- [ ] **Large openings in exterior walls** → Water infiltration + thermal performance risk
- [ ] **Significant load redistribution** (removing posts, walls below roof) → Requires structural engineer
- [ ] **Utility conflicts unresolved** (electrical panel moved, plumbing rerouted) → Safety + code violations
- [ ] **Timeline compressed** (major work in < 4 weeks) → Quality/safety risk
- [ ] **Building is SEFRAK-listed or heritage-protected** → Byantikvaren approval required before modification
- [ ] **Occupied during construction** → Phasing complexity, temporary systems needed
- [ ] **Site access/logistics unclear** → Equipment, debris, staging strategy undefined
- [ ] **Budget under-estimated** (no allowance for utilities, temporary support, testing) → Scope creep inevitable

---

## Red Flags in Drawing Set

**Things to look for that indicate incomplete design:**

- [ ] **Missing structural details** (connections not specified, beam sizing missing)
- [ ] **No mechanical plan** (HVAC routing not shown; conflicts likely)
- [ ] **No electrical plan** (circuit locations, rerouting not addressed)
- [ ] **No plumbing plan** (drain routing, vent stack location unclear)
- [ ] **Dimensions missing or inconsistent** (actual vs. drawing measurements don't match)
- [ ] **Finish details vague** ("paint walls" but color, type not specified)
- [ ] **Schedule or notes incomplete** (material specs, equipment choices undefined)
- [ ] **No timeline or sequencing** (unclear which work happens first)
- [ ] **Cost estimate missing** or significantly under market (indicates incomplete scope)

**If major elements missing:** Ask architect to complete drawings before construction starts. Starting work with incomplete drawings = cost overruns, delays, quality issues.

---

## General Contractor's Checklist

**Before signing off on design for construction:**

- [ ] **Structural logic sound?** (Load paths clear, supports adequate, calcs provided)
- [ ] **All trades coordinated?** (Electrical, HVAC, plumbing conflicts resolved, routing shown)
- [ ] **Constructability assessed?** (Sequencing makes sense, temporary support planned, equipment access confirmed)
- [ ] **Accessibility & code compliance verified?** (Headroom, daylight, fire egress, universal design)
- [ ] **Heritage/conservation status confirmed?** (If applicable, Byantikvaren approval documented)
- [ ] **Budget realistic?** (Includes structural, utilities, testing, contingency ~10–15%)
- [ ] **Timeline achievable?** (Major dependencies identified, weather/cure time factored in)
- [ ] **Site logistics planned?** (Debris removal, temporary power, access routes, safety barriers)
- [ ] **Commissioning/testing scheduled?** (Structural load test, electrical inspection, HVAC balancing, final inspection)

---

## Coordination with Architect & Engineers

**GC's role is to ask hard questions, not to redesign. Questions to pose:**

1. **"I don't see structural calcs for the beam. Who's designing it, and when?"** (Prevents gaps)
2. **"Electrical panel stays in the same location? Outlets in the old wall will need new circuits?"** (Clarifies scope)
3. **"HVAC ductwork currently runs above the wall being removed. Rerouting plan?"** (Identifies conflicts)
4. **"Timeline shows 6 weeks total. Concrete footings need 7 days to cure before beam install. Realistic?"** (Challenges schedule)
5. **"Budget is 200k NOK. Structural work alone (beam, posts, footings) typically 100k+. Where does testing, utilities, finishes fit?"** (Questions scope)
6. **"Building was constructed 1920. Any asbestos survey scheduled before demolition?"** (Safety critical)

**Outcome:** Good questions early prevent expensive changes mid-construction.

---

## Bob's Role in Drawing Review

Bob can:
- ✅ Identify structural load paths and support logic
- ✅ Spot coordination issues across trades
- ✅ Flag constructability concerns and sequencing risks
- ✅ Raise hard questions about feasibility, timeline, budget
- ✅ Escalate to appropriate licensed professionals

Bob cannot:
- ❌ Design structural solutions (licensed PE required)
- ❌ Approve architectural drawings (architect + owner sign-off)
- ❌ Provide binding cost estimates (requires detailed takeoff)
- ❌ Take responsibility for structural safety (engineer's liability)

**When in doubt, ask architect/engineer to clarify before construction starts.**

---

## References

- **TEK17** — Building code requirements (structural, accessibility, energy, fire)
- **Eurocode 2/3/5** — Structural design (concrete, steel, timber)
- **SINTEF Byggforsk** — Construction details, best practices
- **NS 3940** — Energy installations (mechanical, electrical integration)
- **DiBK Byggdetaljsamlingen** — Standard construction details

---

*"A good design review catches 90% of problems before a shovel hits the ground. A bad design review catches 0% and costs 10× as much to fix during construction."* — Experienced GC wisdom
