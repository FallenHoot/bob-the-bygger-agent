---
name: routing
description: Skill router — reads first on every query to determine which skills to activate. Maps query intent to the minimum necessary skill set. Prevents context bloat from loading all skills when only one is needed.
triggers: [ALWAYS_LOAD_FIRST]
load_with: []
safety_level: high
license: Proprietary
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

**Pre-classification — Always run these three checks first:**

1. **Scope guard**: Which project is active in this session? If the query references a different project, address, or property than the locked scope — stop and confirm before routing. Do not answer a question about Project B using any fact loaded for Project A.
2. **Lessons-learned scan**: Does the query trigger any lesson in `lessons-learned`? If yes, note the lesson ID and apply the prevention check before proceeding.
3. **Municipality detection**: Does the query mention a municipality name, address, or location? If yes, add `municipalities` to the skill set and check local rules before applying generic TEK17 defaults.

Read the user's message and apply the first matching rule:

### Rule 0 — Drawing or Image Present
**Triggers**: Any image attachment, reference to a drawing, "plantegning", "snitt", "fasade", "tegning", "IFC file", "PDF plan"
**Sub-rule 0a — File provided (PDF, JPEG, PNG, DXF)**: Load `drawing-reader` FIRST to extract structured data from the file, then load `architectural-drawing-reading` to interpret it, then re-classify using Rules 1–9
**Sub-rule 0b — Image in conversation (no file upload)**: Load `drawing-investigation-protocol` (ask systematic questions) + `architectural-drawing-reading` → re-classify after gathering data
**Sub-rule 0c — IFC file**: Load `bim-ifc` instead of `drawing-reader`
**Primary response**: Bob runs the extraction pipeline, produces the structured summary (title block, scale, key dimensions, gaps), then asks targeted follow-up questions for missing data before any structural assessment

### Rule 1 — Structural / Safety Question
**Triggers**: Removing a wall, sizing a beam, checking a floor, load paths, foundation concerns, structural failure signs, anything where someone could get hurt if the answer is wrong

**Pre-check — Drawing Freeze Gate:**
If the user has drawings (PDF, JPEG, DXF) that have NOT yet been reviewed, run Rule 0 first. Do not proceed to structural calculations until the drawing package is reviewed and accepted. Exception: if no drawings exist, state this and proceed with qualitative analysis only.

**Load**: If image present: `drawing-investigation-protocol` + `structural-engineering` + `building-code-tek17`. If no image: `structural-engineering` + `building-code-tek17`
**Add if soil or foundation work involved**: `geotechnical`
**Protocol**: Lock calculation inputs (span, loads, materials) BEFORE any formula. State confidence level for each input.
**Safety flag**: HIGH — escalation flags fire first if present (see Escalation Matrix in system_prompt.md)

### Rule 2 — Regulatory / Permit Question
**Triggers**: Do I need a søknad? Is this legal? What does TEK17 say? Setbacks, heights, use changes, permits, dispensasjon, fire safety, energy requirements
**Load**: `building-code-tek17`
**Add if søknad package or document list needed**: `soknad-package`
**Add if heritage building**: `historic-preservation`

### Rule 2a — Søknad Package / Permit Application Preparation
**Triggers**: What goes in the søknad? Which drawings do I need? Nabovarsel, ansvarlig søker, forhåndskonferanse, ferdigattest, igangsettingstillatelse, SAK10 document requirements, BRA/BYA calculation for permit
**Load**: `soknad-package` + `building-code-tek17`
**Add if drawings are involved**: `architectural-drawing-reading`
**Primary response**: Walk through the completeness checklist for the specific project type (tilbygg, fasadeendring, nybygg, riving)
**Template**: Use `templates/pre-application-meeting-notes.md` for forhåndskonferanse preparation

### Rule 2b — Geotechnical / Ground Condition Question
**Triggers**: Soil, kvikkleire, quick clay, ground investigation, borehole, bearing capacity, settlement, foundation type, radon, slope stability, NGU, NVE flood zone
**Load**: `geotechnical` + `building-code-tek17`
**Add if foundation is being designed**: `structural-engineering`
**Safety flag**: HIGH — quick clay escalation is automatic: `GEOTECHNICAL_REPORT_REQUIRED`

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

### Rule 7 — BIM / IFC / Digital Model Question
**Triggers**: IFC file, BIM model, Revit, ArchiCAD, Bonsai, IfcOpenShell, clash detection, BCF issues, model coordination, buildingSMART IDS, digital permit (eByggesøknad), LOD, model federation, IFC export problems, Statsbygg BIM manual
**Load**: `bim-ifc` + `architectural-drawing-reading`
**Add if structural content in model**: `structural-engineering`
**Add if permit compliance**: `building-code-tek17`
**Primary response**: Bob identifies IFC entity types present, checks storey hierarchy, flags missing properties, and advises on clash resolution sequence

### Rule 8 — Combined / Complex Query
**Triggers**: Multiple topics in one question, or any query where Rules 1–7 conflict or overlap
**Load**: All skills triggered by any individual matching rule, maximum 3 skills simultaneously
**Note**: If 4+ skills appear necessary, decompose the query into sequential questions

### Rule 9 — Educational / Simplification Request
**Triggers**: User says "what does that mean?", "explain", "simpler", "I don't understand", "too technical", "can you teach me", "links/resources"
**Load**: `technical-education-support`
**Primary response**: Bob translates jargon to plain language, provides real-world analogies, shares learning resources and official links, assesses understanding ("Does that make sense?")
**Note**: This skill can be loaded ALONGSIDE other skills (e.g., structural-engineering + technical-education-support if user asks "explain that beam calculation in simpler terms")

---

## BIM / IFC Routing Note
- `bim-ifc` always loads `architectural-drawing-reading` — IFC files are read using the same drawing-reading framework
- IFC validation for permit submission always escalates to a licensed responsible designer (ansvarlig prosjekterende)

---

## Template Routing

When producing a formal deliverable, use the matching template from `templates/`:

| Output needed | Template |
|---|---|
| Site visit or structural assessment memo | `templates/structural-assessment-memo.md` |
| Heritage / antikvarisk assessment | `templates/heritage-assessment.md` |
| Construction sequence plan | `templates/construction-sequence.md` |
| Forhåndskonferanse notes | `templates/pre-application-meeting-notes.md` |
| Compliance gap analysis | `templates/compliance-gap-analysis.md` |
| Post-approval / ferdigattest checklist | `templates/post-approval-checklist.md` |

Always offer the template when the user appears to be producing documentation for a project.

---

## Never Load Together (Except on Heritage Projects)
- `classical-architecture` + `structural-engineering` in the same response (answer the structural question first, offer design review as a follow-up)
- `sintef-byggforsk` + `classical-architecture` (different layers of the problem)

## Always Load Together
- `structural-engineering` always loads `building-code-tek17` — structural work without regulatory context is incomplete
- `historic-preservation` always loads `building-code-tek17` — heritage work always has regulatory implications
- `geotechnical` always loads `building-code-tek17` — TEK17 §7 governs natural hazard safety requirements
- `soknad-package` always loads `building-code-tek17` — permits cannot be assessed without the underlying regulation
- `drawing-reader` always loads `architectural-drawing-reading` — extraction feeds interpretation
- `bim-ifc` always loads `architectural-drawing-reading` — IFC reading uses the same drawing-reading framework
- `municipalities` always loads `building-code-tek17` — local rules override or extend TEK17 requirements
- `lessons-learned` always loads at session start via `session-initialization` — triggers are scanned before any technical response

---

## Quick Classification Table

| User says... | Skills to load |
|---|---|
| "Can I remove this wall?" | `structural-engineering` + `building-code-tek17` |
| "Can I remove this wall? Here's a photo" | `drawing-investigation-protocol` + `structural-engineering` + `building-code-tek17` |
| "Here's my floor-plan.pdf" (file attachment) | `drawing-reader` + `architectural-drawing-reading` → re-classify |
| "Here's my model.ifc" | `bim-ifc` + `architectural-drawing-reading` |
| "Do I need a søknad for this?" | `building-code-tek17` |
| "What documents go in the søknad?" | `soknad-package` + `building-code-tek17` |
| "I need to prepare my nabovarsel" | `soknad-package` + `building-code-tek17` |
| "How do I insulate the roof?" | `sintef-byggforsk` |
| "The building is from 1895..." | `historic-preservation` + `building-code-tek17` |
| "SEFRAK registered, can we change the windows?" | `historic-preservation` + `building-code-tek17` |
| "What soil type should I assume for my foundation?" | `geotechnical` + `building-code-tek17` |
| "Is this site in a kvikkleire zone?" | `geotechnical` + `building-code-tek17` |
| "What are the local rules in Lørenskog / Oslo / Bergen?" | `municipalities` + `building-code-tek17` |
| "The building is from 1965 in Trondheim" | `municipalities` + `historic-preservation` + `building-code-tek17` |
| "How should we sequence the demolition?" | `construction-execution` |
| "What do you think of these proportions?" | `classical-architecture` |
| "Is this TEK17 compliant?" | `building-code-tek17` |
| "Moisture problem in the wall" | `sintef-byggforsk` |
| "The beam is sagging" | `structural-engineering` + `building-code-tek17` |
| "How does the contractor get paid?" | `construction-execution` |
| "Clash detection in my BIM model" | `bim-ifc` + `architectural-drawing-reading` |
| "What does that mean?" / "Can you explain simpler?" | `technical-education-support` |
| Multiple topics in one question | All matching skills, max 3 simultaneously |

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
*Last reviewed: 2026-08-09*
