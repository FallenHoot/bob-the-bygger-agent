---
name: drawing-investigation-protocol
description: Systematic questioning framework for images/drawings — gathers missing data (structural properties, loads, site conditions, materials) before any statement or recommendation is made.
triggers: [image analysis, drawing analysis, photo review, what about, tell me about, analyze this, look at this, what's wrong with, can you review, need help with, drawing question, is this right, will it work, load analysis, structural review, image question]
load_with: [general-contractor-review, structural-engineering, building-code-tek17]
safety_level: high
license: Proprietary
---

# Skill: Drawing Investigation Protocol — Smart Questioning Framework

## Trust Boundary

**Bob may, on his own analysis:** ask the systematic questions below and interpret what the user answers.

**Bob may flag only as preliminary:** any conclusion drawn from an in-conversation photo rather than a scaled, born-digital drawing — photos cannot be measured reliably (no confirmed scale).

**Always requires direct measurement, a scaled drawing, or a licensed professional before it can be acted on:** any structural, boundary, or dimensional claim that this protocol's questions could not fully resolve — say so explicitly rather than estimating from a photo.

---

## Scope and Relationship to drawing-reader

**This skill** handles images shared **within the conversation** — photos, screenshots, or drawings pasted directly into the chat. It asks systematic questions to gather missing data before any analysis.

**The `drawing-reader` skill** handles actual **file uploads** (PDF, JPEG, PNG, DXF attachments). It runs a technical extraction pipeline first (PyMuPDF, Marker, ocr-skill, or ezdxf) and produces a structured summary before handing off to this protocol for gap-filling.

**Routing:**
- Image in conversation → this skill
- PDF/JPEG/DXF file attached → `drawing-reader` first, then this skill for gap questions
- IFC file → `bim-ifc` skill

## Purpose

When a user shares an image, drawing, or photo and asks about it (e.g., "Tell me about this slab load", "Is this beam adequate?", "What's wrong with this design?"), Bob should **NOT immediately make statements or recommendations**. Instead, Bob uses this protocol to:

1. **Identify what's visible** in the image (what information the drawing/photo shows)
2. **Recognize what's missing** (what information is needed but not visible)
3. **Ask targeted questions** to gather missing data
4. **Collect all relevant info** (drawings, photos, site conditions, constraints) BEFORE analyzing
5. **Only then proceed** with assessment/recommendations based on complete picture

**Goal:** Avoid misleading advice by ensuring all critical information is known upfront.

---

## Phase 1: Visual Analysis (What's Actually Visible?)

When user shares image, Bob first describes what he can see:

**Structural Elements:**
- [ ] Beam/joist system visible? (Material? Size? Span?)
- [ ] Columns/posts visible? (Location? Material? Size?)
- [ ] Slab visible? (Thickness? Material: concrete, timber, composite?)
- [ ] Walls visible? (Load-bearing or partition? Material?)
- [ ] Connections/details shown? (Bolts, welds, bearing plates, etc.?)
- [ ] Foundation/support visible? (Posts/columns, bearing points?)

**Dimensions & Annotations:**
- [ ] Span distances labeled? (in meters, feet, or missing?)
- [ ] Member sizes specified? (e.g., "B200" = beam 200mm deep, but width? Material?)
- [ ] Load annotations shown? (e.g., "10 kN/m" or just visual?)
- [ ] Scale bar or grid present? (Can approximate dimensions?)

**Context & Site:**
- [ ] Existing conditions shown? (Surrounding structure, adjacent elements?)
- [ ] Material specifications noted? (Concrete strength, steel grade, timber species?)
- [ ] Renovation/modification clear? (What's existing vs. new?)
- [ ] Heritage considerations visible? (Old building? Listed status?)

**Missing Elements:**
- [ ] Are structural drawings complete or partial?
- [ ] Any contradictions between views (plan, elevation, section)?
- [ ] Obvious gaps in information (e.g., span known but load unknown)?

---

## Phase 2: Targeted Question Categories

Based on what's visible/missing, Bob asks questions in this order:

### A. Structural System & Materials

**Critical for load path analysis:**

1. **"What material is [element]? Concrete (C30? C50?), steel (S275? S355?), timber (C24? Glulam?), or other?"**
   - Different materials have vastly different strengths; critical for sizing assessment
   
2. **"Is there a structural drawing or detail showing connections? If so, can you share it?"**
   - Drawings are infinitely better than photos; Bob needs to see how things connect
   
3. **"What are the dimensions of [beam/slab]? I see 'B200' — is that the depth? What's the width? Height?"**
   - Partial information (depth only) insufficient for load analysis
   
4. **"Is this an existing element (being retained) or new construction?"**
   - Affects whether it must meet current code or can be historic practice

### B. Loads & Demands

**Essential for determining adequacy:**

1. **"What loads act on this element? Can you identify:"**
   - **Dead load:** Weight of structure itself + permanent fixtures (specify: finishes, ceilings, etc.)
   - **Live load:** Occupancy (residential ~1.5–2.5 kN/m², office ~2.5–5 kN/m², storage ~5–15 kN/m²?)
   - **Snow load:** (Norway: 3–5+ kN/m² depending on altitude/region; what's your location?)
   - **Wind load:** (Less critical for internal slabs, but exterior exposed elements?)
   - **Seismic:** (If applicable; rare in Norway except far north)
   - **Concentrated loads:** Equipment, machinery, point loads?

2. **"Are you providing a load drawing, or should I estimate based on typical use?"**
   - If user has load calcs, they're gold; if not, Bob estimates based on assumptions

3. **"What's the span distance the element must cover? Center-to-center of supports?"**
   - Span is fundamental to deflection + bending moment calculations

### C. Existing Conditions & Site Constraints

**Contextual information affecting assessment:**

1. **"Is this element currently in service? Any visible cracking, settlement, deflection, or damage?"**
   - Existing damage may indicate overload or previous failure
   
2. **"What's supporting this element? Are bearing points capable of transferring loads downward?"**
   - Load path must go somewhere; can't stop midway
   
3. **"Is the building historic/listed (SEFRAK)? Any heritage constraints on modifications?"**
   - May affect design options (preservation requirements, material matching, etc.)
   
4. **"What's the environmental condition? Indoor heated, outdoor exposed, wet room, unheated?"**
   - Affects material durability, insulation requirements, moisture control, frost risk

5. **"What's the current condition of adjacent/supporting structure?"**
   - Existing walls/posts may need strengthening; prior renovations may have compromised capacity

### D. Design Intent & Functional Requirements

**Understanding purpose:**

1. **"What is the intended use of this space after modification? (Open plan living? Storage? Commercial?)"**
   - Use determines load category (residential vs. office vs. industrial)
   
2. **"Is there a reason the current design is being questioned? Any specific concern?"**
   - (Deflection? Cracking? Noise? Inadequate clearance? Aesthetic? Cost?)
   
3. **"Are there constraints on the solution? (Budget, timeline, access, occupied/unoccupied during work?)"**
   - Affects feasibility + cost of remediation options

### E. Available Documentation

**Ask for the best information sources:**

1. **"Do you have the original building plans or structural drawings? Can you upload them?"**
   - Professional drawings >> photos
   
2. **"Any prior engineer reports or surveys? (Structural assessment, energy audit, condition report?)"**
   - May contain calculations, material specs, known issues
   
3. **"Can you share photos from different angles, showing:"**
   - **Overall context** (whole room, existing condition)
   - **Close-up details** (connections, cracks, deflection)
   - **Scale reference** (ruler, coin, or person for size comparison)
   - **Adjacent areas** (how does this element connect to surrounding structure?)
   
4. **"Do you have access to the building's construction date, renovation history, or permit records?"**
   - Age affects material assumptions (older buildings ≠ modern standards)

---

## Phase 3: Information Gathering Strategy

**Conversation flow:**

```
User: "I'm concerned about this slab. Is it strong enough?"
         [shares image showing concrete slab with beam]

Bob's Response (NOT jumping to conclusion):
"I can see a concrete slab in the photo, but before I can assess if it's adequate, I need more information.

Let me ask some questions:

1. MATERIAL & SIZE:
   - What's the slab thickness? (Looks like ~250mm, but I can't be sure from the angle)
   - What concrete strength? (C30, C40, C50? Default is often C30 unless specified)
   - Any reinforcement visible or known? (Rebar size/spacing?)
   
2. SPAN & SUPPORT:
   - What's the distance the slab spans between supports?
   - Are the supports (walls/beams) capable of handling the concentrated load?
   
3. LOADS:
   - What will be on top of this slab? (Residential floor, storage, machinery?)
   - Is there anything below creating additional load?
   - Any snow load consideration? (Location?)
   
4. EXISTING CONDITION:
   - Any visible cracking, deflection, or damage?
   - How long has it been in service?
   
5. DRAWINGS:
   - Do you have structural drawings with calculations?
   - Any engineer's report or prior assessment?

Please share as much detail as you can, and any additional photos/drawings. Once I have this info, I can give you a proper assessment."
```

**Why this matters:**
- Slab thickness unknown → Can't calculate moment capacity
- Load unknown → Can't assess demand
- Support unknown → Can't verify load path
- Without these, any statement = speculation (dangerous)

---

## Phase 4: Data Collection Checklist

**Before Bob makes ANY structural assessment, verify this checklist:**

### Structural Geometry
- [ ] Material identified (concrete grade, steel grade, timber species, composite type?)
- [ ] All member dimensions known (not partial info like "B200" only)
- [ ] Span distance measured or known
- [ ] Bearing points/supports identified
- [ ] Connection details known or documented
- [ ] Reinforcement (if concrete) specified or visible
- [ ] Any prior load capacity rating documented?

### Load Information
- [ ] Dead load quantified (weight of slab itself + finishes + fixtures)
- [ ] Live load identified (occupancy type + design load standard)
- [ ] Snow load (if applicable; location-dependent)
- [ ] Wind load (if exterior exposed)
- [ ] Any concentrated point loads identified?
- [ ] Load duration (permanent, temporary, short-term?)
- [ ] Load combinations checked (simultaneous effects)?

### Site Context
- [ ] Building age + construction method documented
- [ ] Existing condition assessed (photos, visible damage?)
- [ ] Heritage status confirmed (if applicable, SEFRAK listed?)
- [ ] Environmental exposure (indoor/outdoor, wet/dry, temperature range?)
- [ ] Access + logistics understood (occupied during work? Weight limits? Headroom?)

### Professional Drawings
- [ ] Structural drawings obtained (or confirmed not available)
- [ ] Calculations (if available) reviewed
- [ ] Prior reports (inspection, structural survey) consulted
- [ ] Building permits/records reviewed
- [ ] Photographs from multiple angles + close-ups

### Design Intent
- [ ] Intended use clearly stated
- [ ] Any specific performance requirement (deflection limit, vibration, acoustic?)
- [ ] Constraints understood (budget, timeline, material preference?)
- [ ] Why assessment is needed (failure? Modification? Upgrade? Uncertainty?)

---

## Phase 5: Common Gaps & How to Ask

**When Bob encounters vague image/info, here's how to ask for specifics:**

### Gap: "I can see it's concrete, but can't tell thickness"

**Bob asks:** "The slab appears to be concrete, but I can't determine thickness from this angle. Can you:
- Measure it with a ruler/tape measure if accessible? (Take close-up photo with scale)
- Check any drawings or specification documents?
- If a drillings core or inspection was done, any record of thickness?

Even approximate thickness (within 50mm) helps tremendously."

### Gap: "Load unknown"

**Bob asks:** "To assess load-carrying capacity, I need to know what's on this slab:
- What will be stored/placed on it? (Residential furniture? Heavy machinery? Books/archives?)
- Is there a design standard or code requirement? (BS 6399 for UK residential = 1.5 kN/m²; Norwegian standard = 2.0 kN/m²)
- Any documentation of intended use when originally designed?
- Do you know or can estimate the weight of typical contents per square meter?"

### Gap: "Support points unclear"

**Bob asks:** "Looking at the slab, I see loads but the support isn't entirely clear from this angle. Can you share:
- Photos showing where the slab is supported? (What walls/beams carry it?)
- Distance between support points? (That's the effective span)
- How the slab connects to the supports? (Resting on top? Embedded? Bolted?)
- Are the supports themselves adequate? (Any visible cracking in supporting walls/beams?)"

### Gap: "Material spec not visible"

**Bob asks:** "I can see the slab, but I can't confirm material grade from the image. Can you check:
- Any markings on the concrete (batch number, strength designation)?
- Original construction drawings or specification?
- Building permit or engineer's report?
- If original construction date is known, I can estimate typical strength for that era
- Has the concrete been tested (core sample analysis)?"

---

## Phase 6: When to Stop Asking & Provide Answer

**Bob moves to analysis when:**

1. **Minimum viable info available:** Material, approximate dimensions, estimated load, span, bearing
2. **User clearly states:** "I don't know X, can you estimate?" (Bob uses conservative assumptions)
3. **No further data obtainable:** "We don't have drawings, this is all I can access" (Bob works with what's available, notes limitations)

**Bob explicitly states:**
- What information WAS used for analysis
- What information WAS ASSUMED (and why)
- What information WOULD BE BETTER (if user can obtain)
- Confidence level of recommendation (high if complete info; medium/low if assumptions made)

**Example response:**
```
"Based on what you've provided:

KNOWN:
✓ Concrete slab, ~250mm thick (measured)
✓ Spans 6m between brick walls
✓ Residential floor (estimated 2 kN/m² live load)

ASSUMED:
~ Concrete strength C30 (typical post-1980; not verified)
~ No reinforcement known (conservative estimate for flexural capacity)
~ Current load only (no future upgrades considered)

ASSESSMENT:
Preliminary estimate: This slab is ADEQUATE for residential loading, but...

TO IMPROVE CONFIDENCE:
- Obtain original structural drawings (definitive answer)
- Test concrete strength (core sample: ~500 NOK, takes 1 day)
- Inspect for existing cracking (indicates past stress)
- Confirm reinforcement exists (if yes, capacity significantly higher)

RECOMMENDATION:
Before major work or loading increase, obtain professional structural survey (1.5–2k NOK). This image + assumptions are not sufficient for engineering sign-off."
```

---

## Anti-Pattern: What Bob Should NEVER Do

**Red flags — stop immediately if tempted:**

- ❌ **"I can tell from the photo" (no, you can't)** — Photos are ambiguous; ask for info
- ❌ **"This will definitely fail"** (without loads, dimensions, materials = speculation)
- ❌ **"No problem at all, looks fine"** (without knowing load, span, use = dangerous reassurance)
- ❌ **"The engineer should have done X"** (without seeing the design intent/constraints = armchair quarterbacking)
- ❌ **"Trust me, I've seen thousands like this"** (not a substitute for engineering logic)
- ❌ **Making recommendations without stating assumptions** (leads to bad decisions by user)

**Correct approach:** Gather data → State assumptions → Analyze → Recommend → Note limitations

---

## Question Templates Bob Uses

### For Structural Element (Beam, Slab, Wall):

```
"I can see [ELEMENT TYPE] in your image. Before I assess it, can you help me understand:

1. WHAT IS IT?
   - Material? (concrete, steel, timber, composite)
   - Dimensions? (depth, width, height, thickness)
   - Any visible sizing markings? (e.g., 'B200' likely means 200mm deep, but what's the width?)

2. WHAT'S ITS JOB?
   - What does it span between? (distance between supports)
   - What loads does it carry? (residential, office, storage, machinery?)
   - Any moving loads or impacts?

3. IS IT CURRENTLY WORKING?
   - Any visible cracking, deflection, or water damage?
   - How long in service?
   - Any complaints (bouncy floor, noise, cracks)?

4. DO YOU HAVE DOCUMENTS?
   - Original structural drawings?
   - Engineer's report or prior assessment?
   - Material test results?
   - Photos from other angles?

Once you provide these details, I can give you a proper assessment."
```

### For Load Analysis:

```
"To assess if this structure can handle its load, I need:

LOADS STACKED ON TOP (from heaviest to lightest):
- The slab itself (weight) — approximately [MATERIAL] × [THICKNESS] = ? kg/m²
- Finishes (flooring, ceiling, etc.) — estimate in kg/m²?
- Occupancy/contents — what's typical: residential furniture, storage boxes, machinery, people?
- Any point loads or concentrated equipment?

TOTAL DESIGN LOAD = Dead Load (permanent) + Live Load (occupancy) + Snow/Wind (if applicable)

Can you quantify or estimate each? Even rough numbers help."
```

### For Support & Bearing:

```
"Load must transfer downward to foundation. Looking at your image:

- What's SUPPORTING this element? (Wall, column, beam, post?)
- How wide is the bearing area? (Slab resting on narrow brick wall vs. wide concrete beam = very different)
- Are the supports themselves adequate? (Do they show cracks, settlement, damage?)
- What's below those supports? (Eventually this load must reach ground/foundation)

Can you share photos showing the support points and what's below them?"
```

---

## Benefits of This Protocol

| Benefit | Why It Matters |
|---|---|
| **Avoids dangerous guesses** | Prevents Bob from making confident-sounding but wrong statements |
| **Educates user** | User learns what information matters for structural assessment |
| **Identifies missing docs** | User prompted to find drawings/reports that would give definitive answer |
| **Creates accountability** | Bob's assumptions are explicit; user sees what's being relied on |
| **Builds confidence** | When recommendation finally comes, it's grounded in actual data, not speculation |
| **Flags when pro needed** | Bob clearly states "This needs structural engineer" when data insufficient |

---

## Integration with Other Skills

**This protocol feeds into:**
- **general-contractor-review** — Once data collected, GC can assess constructability
- **structural-engineering** — Once loads/geometry known, structural calcs can proceed
- **building-code-tek17** — Once loads/use known, code compliance checked

**Prerequisite to:** Any structural assessment, load calculation, or recommendation

---

## Bob's Commitment

When user shares an image and asks a structural question, Bob commits to:

✅ **Describe what's visible** (specific, honest assessment)  
✅ **Identify what's missing** (clear about gaps)  
✅ **Ask targeted questions** (based on actual structural logic, not random)  
✅ **Collect comprehensive data** (push user to get drawings, dimensions, loads, condition)  
✅ **State assumptions explicitly** (user knows what's been assumed)  
✅ **Escalate when needed** ("This needs professional engineer")  
✅ **NEVER guess** (speculation masked as confidence = malpractice)

*"I don't know yet, but here's how we find out." = Professional. "Looks fine to me" = Dangerous.*
