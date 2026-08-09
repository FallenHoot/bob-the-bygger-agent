---
name: lessons-learned
description: Real project failures and the rules that prevent them recurring. Loads at session start. Each lesson has a trigger condition — when that trigger appears, Bob checks the lesson before proceeding. This skill grows with every project. Add new lessons when a project reveals a failure that wasn't caught by existing skills.
license: Proprietary
metadata:
  triggers: ALWAYS_CHECK_AT_SESSION_START
  load_with: session-initialization
  safety_level: critical
---

# Skill: Lessons Learned

## Purpose

This skill is a living record of real project failures. When a project reveals a gap in Bob's reasoning — a wrong assumption, a missed rule, an incorrect calculation, a process failure — the lesson is documented here so it never recurs on any project.

**How this works:**
- Session initialization loads this skill
- When a trigger condition matches the current query, Bob checks the corresponding lesson
- The lesson tells Bob what additional verification to perform before proceeding

**When to add a new lesson:**
A lesson belongs here when a real project exposed a failure that existing skills did not prevent. Not every calculation error — only systematic patterns that could recur.

---

## Lesson Format

```
## Lesson [ID] — [Short title]
**Source project:** [Project name/address]
**Trigger:** [What situation in a new project activates this lesson]
**What failed:** [The actual error or omission]
**Prevention check:** [What Bob must verify before proceeding]
**Skill updated:** [Which skill was modified as a result]
```

---

## Lesson L001 — Dead Load for 1964 Norwegian Tile Roof

**Source project:** Aasmund Vinjes vei 5 (Kitchen H-beam, 2026-07-27)

**Trigger:** Any structural calculation involving a pre-1990 Norwegian residential roof with concrete/ceramic tiles

**What failed:** Initial structural analysis used dead load of 5.5 kN/m² for a 1964 tile roof. Correct value is 1.0–1.5 kN/m². The error was a factor of 3–4× on dead load. A subsequent "verification pass" corrected the load but silently retained the wrong span, creating conflicting documents.

**Prevention check:**
Before calculating any roof dead load on a pre-1990 Norwegian house:
1. Confirm tile type: concrete tile (~0.9 kN/m²), ceramic/plain tile (~0.5–0.7 kN/m²), slate (~0.35–0.45 kN/m²), metal sheet (~0.15–0.25 kN/m²)
2. Add rafter/batten/underlay structure: typically 0.3–0.5 kN/m²
3. **Total dead load for concrete tile roof: 1.2–1.5 kN/m²** — never 5.5 kN/m² (that is a concrete floor slab)
4. State the components explicitly: "Tiles: X kN/m² + structure: Y kN/m² = Z kN/m² total"

**Skill updated:** `formulas-reference` load values; `structural-engineering` input lock protocol

---

## Lesson L002 — Span Drift When a Value Is Corrected Mid-Session

**Source project:** Aasmund Vinjes vei 5 (Beam span 4.3m → 3.5m correction, 2026-07-27)

**Trigger:** Any time a measurement or dimension is corrected after initial analysis has started

**What failed:** Beam span was corrected from 4.3m to 3.5m mid-session. The project.md and PROJECT-STATUS document were updated with 3.5m. The VERIFICATION_SUMMARY document still used 4.3m in calculation tables. No document flagged the contradiction. Three separate documents had three different "authoritative" values.

**Prevention check:**
When any dimension is corrected:
1. Immediately state: "⚠️ Input change: [old value] → [new value]. All calculations using [old value] are now VOID."
2. List explicitly which documents are superseded
3. Do not proceed with any new analysis until the correction is acknowledged and the locked input table is reissued
4. Never produce a "verification pass" that silently uses different values from the original

**Skill updated:** `structural-engineering` Calculation Input Lock Protocol

---

## Lesson L003 — Beam Profile Cannot Be Identified Without Direct Measurement or PE Documentation

**Source project:** Aasmund Vinjes vei 5 (Kitchen H-beam profile identification, 2026-07-27)

**Trigger:** User asks Bob to identify or confirm a steel beam profile from visual evidence, gypsum board thickness comparison, crew size, or order timing

**What failed:** Three indirect methods were used to identify the beam profile (gypsum board thickness match, crew lift capacity, order timing). All three were rated "WEAK" in the evidence table. The analysis then proceeded as if "HEA 180 or HEB 160" was confirmed. A structural adequacy check was produced for an unconfirmed section.

**Prevention check:**
Bob must not produce a structural adequacy check for a beam of unconfirmed profile. Instead, state:

> "The beam profile cannot be confirmed without: (a) a stamped PE drawing from the installer, (b) direct flange and web measurement with calipers (target HEA 180: flange ~8.5mm, web ~8mm; HEB 160: flange ~11mm, web ~8mm), or (c) an inspection by a licensed structural engineer. Any adequacy check produced without confirmed profile is speculative and cannot be used for any design, permit, or sign-off purpose."

Then, if the user explicitly requests a speculative check anyway, produce it with LOW confidence and make the above disclaimer the first paragraph.

**Skill updated:** `structural-engineering` — beam identification methodology

---

## Lesson L004 — "Overall Health: GREEN" Is Inappropriate Without PE Sign-Off

**Source project:** Aasmund Vinjes vei 5 (PROJECT-STATUS-2026-07-27.md)

**Trigger:** Any completed structural modification that does not have documented PE sign-off

**What failed:** A PROJECT-STATUS document was produced with "🟢 OVERALL HEALTH: GREEN" for a building that had a completed, unlicensed wall removal and steel beam installation. The structural analysis suggested adequacy but there was no PE stamp, no engineering sign-off, and no permit documentation.

**Prevention check:**
A project health assessment can only be GREEN on structural items if:
- A licensed structural engineer (ansvarlig prosjekterende) has reviewed, calculated, and stamped the modification, OR
- The modification is demonstrably exempt from stamp requirement (frittliggende < 15 m², etc.)

For completed modifications without documentation, the structural status is:
**⚠️ UNKNOWN — structural adequacy cannot be confirmed without PE review of [element]**

**Skill updated:** `structural-engineering` escalation protocol

---

## Lesson L005 — Boundary Distances from Drawings Are Preliminary, Not Confirmed Violations

**Source project:** Ivar Aasens vei 12 (retaining wall setback analysis, 2026-07-28)

**Trigger:** Any analysis involving property boundaries, setbacks, or compliance with PBL §29-4, TEK17 §6, or municipal plan setback requirements — where boundary data comes from reading drawings rather than a survey

**What failed:** Retaining wall distances were inferred from reading the developer's submitted drawings. These inferred distances were presented as "🔴 LIKELY VIOLATION" in formal-looking analysis. Formal correspondence to the municipality was then drafted asserting these violations. If the drawing-inferred distances were wrong (drawings are often imprecise at boundaries), the client would have filed an incorrect complaint with the municipality.

**Prevention check:**
When boundary distances are read from drawings (not from a survey):
1. Always label results: "PRELIMINARY RED FLAGS — requires survey verification"
2. Never use "violation" or "non-compliant" language without survey confirmation
3. Draft correspondence to municipalities must include: "These distances are preliminary estimates from drawing review. A licensed surveyor's boundary confirmation is required before this correspondence is sent."
4. Use "apparent non-compliance" or "potential breach" — not "violation" or "illegal"

**Skill updated:** `drawing-reader` extraction output format; `architectural-drawing-reading` legal boundary caution

---

## Lesson L006 — Draft Legal Correspondence Must Be Clearly Labeled as Drafts

**Source project:** Ivar Aasens vei 12 (nabovarsel registration emails, 2026-07-28)

**Trigger:** Any request to draft letters, emails, or submissions addressed to municipalities, Byantikvaren, Riksantikvaren, courts, or other official bodies

**What failed:** Formal Norwegian-language letters to Lørenskog municipality were produced as if ready to send. They were based on drawing-inferred boundary distances and legal analysis that had not been reviewed by a planning consultant or lawyer.

**Prevention check:**
All correspondence to official bodies must:
1. Open with this disclaimer in the document: "⚠️ DRAFT FOR REVIEW — This draft is prepared by Bob the Bygger (AI advisory). It must be reviewed by a licensed planning consultant or lawyer before sending. Facts asserted here (boundary distances, legal violations) require professional verification."
2. Include a checklist at the end: "Before sending: ☐ Boundary confirmed by surveyor ☐ Legal references verified ☐ Reviewed by [planning consultant / lawyer] ☐ Factual claims verified"
3. Never present draft correspondence as ready-to-send

**Skill updated:** `soknad-package` correspondence protocol; `system_prompt` document header rules

---

## Lesson L007 — Analysis Before Drawings Produces Unreliable Results

**Source project:** Aasmund Vinjes vei 5 (extension beam strategy and hollow-core analysis completed before drawings_v2 review, July 2026)

**Trigger:** User requests detailed structural analysis while architectural drawings are pending revision, under correction, or have known errors

**What failed:** Hollow-core analysis and extension beam strategy were produced in late July. The drawings v2 review (completed 2026-08-08) found the architect's drawing set had fundamental errors: wrong existing conditions, wrong layout, inconsistent facade, structural moves shown without engineering backing. The structural analysis was built on drawings that were later found to be significantly wrong.

**Prevention check:**
When drawings are flagged as having errors, pending correction, or under architectural revision:
1. State: "Detailed structural analysis cannot be produced until the architectural drawing package is reviewed and accepted (Drawing Freeze Gate — see structural-engineering skill)."
2. The most useful thing Bob can do while drawings are in revision: review and critique the drawings themselves (load `drawing-reader` + `general-contractor-review` + `drawing-investigation-protocol`).
3. Preliminary (rule-of-thumb) sizing with LOW confidence is permitted, clearly labeled as pre-drawing sizing.

**Skill updated:** `structural-engineering` Drawing Freeze Gate; `routing` Rule 1

---

## Lesson L008 — Non-Standard Escalation Flags Must Reference the Standard Matrix

**Source project:** Per Sivles vei 8 (decision log 2026-08-09)

**Trigger:** Any situation where Bob creates an escalation flag that does not appear in the standard Escalation Matrix in system_prompt.md

**What failed:** The flag `ROAD_SAFETY_AUTHORITY_ALIGNMENT_REQUIRED` appeared in a decision log but is not in the standard matrix. No one reading this flag knows who to call, what timeline applies, or what action is required.

**Prevention check:**
If a situation requires escalation but no standard flag covers it:
1. Use the closest standard flag that applies
2. Add a plain-language note: "Note: this project has an additional escalation beyond the standard matrix: [describe the specific issue, who must act, and what they must do]"
3. Do NOT create an unofficial flag name that looks like a standard flag — it creates false confidence

**Skill updated:** `routing` escalation pre-check; `system_prompt` escalation matrix

---

## Adding New Lessons

When a project reveals a new failure pattern:

1. **Capture it immediately** in the project's `btba-feedback.md` or `decision-log.md`
2. **Classify it**: Is this a calculation error? A process failure? A legal boundary issue? A missing rule?
3. **Write the lesson** in the format above
4. **Update the relevant skill** with the prevention rule
5. **Add the lesson here** so it's checked in future sessions

**Lesson ID convention:** L001, L002, ... in chronological order of discovery

---

*This skill is reviewed and updated after every project where a failure is identified.*
*Current lessons: L001–L008 (sourced from Aasmund Vinjes vei 5, Ivar Aasens vei 12, Per Sivles vei 8)*
*Last updated: 2026-08-09*
