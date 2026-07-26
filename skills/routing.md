---
name: routing
description: Skill router — reads first on every query to determine which skills to activate. Maps query intent to the minimum necessary skill set. Prevents context bloat from loading all skills when only one is needed.
triggers: [ALWAYS_LOAD_FIRST]
load_with: []
safety_level: high
---

# Skill: Routing

## Purpose

This skill is loaded first on every query. It classifies the incoming request and selects the minimum set of skills needed to answer it correctly and safely. Only load skills that are directly relevant — context window space is finite and unused skills add noise.

**Language Detection:** Before classification, detect user language (Norwegian or English). Respond in the same language throughout the session unless explicitly asked to switch.

---

## Language Detection (Run First)

**Detect user's primary language:**

| Signal | Language | Example |
|---|---|---|
| **Norwegian words present** | Norwegian | "Kan jeg fjerne denne veggen?", "TEK17", "søknad", "varmepumpe" |
| **English words present** | English | "Can I remove this wall?", "What about the load?" |
| **Mixed (code-switching)** | Use user's first language OR context (if project address is Norwegian, assume Norwegian) | "Can I do this renovation? Har jeg behov for søknad?" → Respond in Norwegian |
| **Ambiguous** | Default to Norwegian (Norwegian construction expertise is primary) | Single-word query like "recommendations?" → Respond in Norwegian |

**Response mode:** Match user's language exactly. If user switches languages mid-conversation, adapt. If user asks "svar på norsk" or "respond in English", honor that request for remainder of session.

---

## Classification Rules

Read the user's message and apply the first matching rule:

### Rule 0 — Drawing or Image Present
**Triggers**: Any image attachment, reference to a drawing, "plantegning", "snitt", "fasade", "tegning", "IFC file", "PDF plan"
**Load**: `drawing-investigation-protocol` (FIRST — asks clarifying questions before analysis) + `architectural-drawing-reading` → then re-classify the query using Rules 1–6 after reading the drawing
**Primary response**: Bob describes what's visible in image, then asks systematic questions to gather missing data (material, dimensions, loads, conditions) before making any structural assessment

### Rule 1 — Structural / Safety Question
**Triggers**: Removing a wall, sizing a beam, checking a floor, load paths, foundation concerns, structural failure signs, anything where someone could get hurt if the answer is wrong
**Load**: If image present: `drawing-investigation-protocol` + `structural-engineering` + `building-code-tek17`. If no image: `structural-engineering` + `building-code-tek17`
**Protocol**: Always gather comprehensive data FIRST (material, dimensions, loads, existing condition, available drawings) before making any structural statement
**Safety flag**: HIGH — state assumptions explicitly and require escalation check (see Escalation Matrix in system_prompt.md)

### Rule 2 — Regulatory / Permit Question
**Triggers**: Do I need a søknad? Is this legal? What does TEK17 say? Setbacks, heights, use changes, permits, dispensasjon, fire safety, energy requirements
**Load**: `building-code-tek17`
**Add if heritage building**: `historic-preservation`

### Rule 3 — Technical Execution Question
**Triggers**: How do I build this? Vapour barrier placement, insulation specification, moisture concerns, airtightness, drainage, frost protection, wall assembly, roof build-up
**Load**: `sintef-byggforsk`
**Add if regulatory check needed**: `building-code-tek17`

### Rule 4 — Heritage / Historic Building Question
**Triggers**: SEFRAK, old building, pre-1940, preservation, antikvarisk, Byantikvaren, Riksantikvaren, original windows, heritage materials, restoration
**Load**: `historic-preservation` + `building-code-tek17`
**Add if structural work on heritage building**: `structural-engineering`

### Rule 5 — Construction Management / Site Question
**Triggers**: Demolition sequence, contractor coordination, contracts, site safety, lead times, temporary works, asbestos, FDV, ferdigattest, HMS, handover
**Load**: `construction-execution`
**Add if regulatory conditions apply**: `building-code-tek17`

### Rule 6 — Design / Appearance Question
**Triggers**: Does this look right? Window proportions, facade composition, roof pitch, ornament, style, does this fit the neighbourhood, streetscape
**Load**: `classical-architecture`
**Add if heritage context**: `historic-preservation`

### Rule 7 — Combined / Complex Query
**Triggers**: Multiple topics in one question, or any query where Rules 1–6 conflict or overlap
**Load**: All skills triggered by any individual matching rule, maximum 3 skills simultaneously
**Note**: If 4+ skills appear necessary, decompose the query into sequential questions

### Rule 8 — Educational / Simplification Request
**Triggers**: User says "what does that mean?", "explain", "simpler", "I don't understand", "too technical", "can you teach me", "links/resources"
**Load**: `technical-education-support`
**Primary response**: Bob translates jargon to plain language, provides real-world analogies, shares learning resources and official links, assesses understanding ("Does that make sense?")
**Note**: This skill can be loaded ALONGSIDE other skills (e.g., structural-engineering + technical-education-support if user asks "explain that beam calculation in simpler terms")

---

## Never Load Together (Except on Heritage Projects)
- `classical-architecture` + `structural-engineering` in the same response (answer the structural question first, offer design review as a follow-up)
- `sintef-byggforsk` + `classical-architecture` (different layers of the problem)

## Always Load Together
- `structural-engineering` always loads `building-code-tek17` — structural work without regulatory context is incomplete
- `historic-preservation` always loads `building-code-tek17` — heritage work always has regulatory implications

---

## Quick Classification Table

| User says... | Load |
|---|---|
| "Can I remove this wall?" | structural-engineering + building-code-tek17 |
| "Can I remove this wall? Here's a photo" | drawing-investigation-protocol + structural-engineering + building-code-tek17 |
| "Do I need a søknad for this?" | building-code-tek17 |
| "How do I insulate the roof?" | sintef-byggforsk |
| "The building is from 1895..." | historic-preservation + building-code-tek17 |
| "How should we sequence the demo?" | construction-execution |
| "What do you think of these proportions?" | classical-architecture |
| "Here is a photo of the drawing" | drawing-investigation-protocol + architectural-drawing-reading → re-classify |
| "Is this TEK17 compliant?" | building-code-tek17 |
| "Moisture problem in the wall" | sintef-byggforsk |
| "SEFRAK registered, can we change the windows?" | historic-preservation + building-code-tek17 |
| "The beam is sagging" | structural-engineering + building-code-tek17 |
| "How does the contractor get paid?" | construction-execution |
| "What does that mean?" (if user confused) | technical-education-support (explain previous jargon with analogies + links) |
| "Can you explain in simpler terms?" | technical-education-support |
| "I don't understand the technical stuff" | technical-education-support |

---

## Escalation Pre-Check

Before loading any skill, check:
1. Is this a safety-critical structural question? → Flag `ESCALATION_CHECK_REQUIRED`
2. Is this a heritage building with formal protection (fredet)? → Flag `RIKSANTIKVAREN_CONSENT_REQUIRED`
3. Is there a known geotechnical risk (quick clay, flood zone)? → Flag `GEOTECHNICAL_REPORT_REQUIRED`
4. Does the work require a formal wet stamp (signed structural calculations)? → Flag `WET_STAMP_REQUIRED`

See Escalation Matrix in `system_prompt.md` for resolution rules.

---

*This skill has no domain knowledge — it is pure routing logic.*
*Last reviewed: 2026-07-26*
