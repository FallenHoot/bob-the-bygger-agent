---
name: lessons-learned
description: Load matching lessons only for retrospectives or known failures in loads, input drift, beam identification, safety status, boundary claims, correspondence, drawing evidence, or review triggers.
license: Proprietary
triggers: [explicit retrospective, matching known failure mode, roof load provenance error, corrected input drift, unconfirmed beam profile, unsupported safety status, drawing-derived boundary claim, unverified correspondence claim, unresolved drawing basis, unmatched review concern]
load_with: []
load_priority: on-demand
safety_level: critical
status: unreviewed
---

# Skill: Lessons Learned

## Trust Boundary

Process-integrity skill — `critical` reflects that a missed lesson recurs as a real error (see L001–L008), not that this skill itself needs professional sign-off.

**Bob may, on his own analysis:** apply the relevant prevention checks when a
known failure mode matches the task or an explicit retrospective is requested.

**Bob may also:** record evidenced failure patterns and make reversible local
lesson/checklist corrections within the authorized scope, without requesting
approval for each edit. Separate observed facts from proposed prevention rules.

**Requires external review or confirmation as applicable:** engineering or
legal conclusions, professional sign-off, outbound correspondence, destructive
changes, and consequential project decisions. Recording a lesson does not
verify a calculation, establish site safety, or authorize construction.

## Purpose

This skill records reported project failures and prevention checks intended to
reduce recurrence. Historical incident summaries below have not been independently
reverified in this audit; they are not confirmation of engineering conclusions.

**How this works:**
- Load only matching lessons for the current query or explicit retrospective,
	per [Task Routes](../routing/SKILL.md#task-routes). No unconditional startup
	load, startup scan, or mandatory per-response lesson scan.
- Apply the matched lesson's scoped verification checks, preserving useful
	bounded guidance while holding unsupported consequential conclusions.
- Do not reload startup, routing, or lifecycle from this skill. Return to the
	caller afterward; references to related skills are not recursive load commands.

**When to add a new lesson:**
A lesson belongs here when a real project exposed a failure that existing skills did not prevent. Not every calculation error — only systematic patterns that could recur.

---

## Lesson Format

```
## Lesson [ID] — [Short title]
**Source basis:** [De-identified failure pattern; keep private provenance in the project]
**Trigger:** [What situation in a new project activates this lesson]
**What failed:** [The actual error or omission]
**Prevention check:** [What Bob must verify before proceeding]
**Guard evidence:** [Target file and section actually inspected, what is present,
and what is missing. Instruction text is not runtime enforcement.]
**Target skill(s):** [Where the guard belongs; this is not a claim of an edit]
**Promotion status:** [Not implemented | Partial | Implemented (instruction text)]
**Validation:** [Review date, evidence scope, behavioral test result or unvalidated]
```

**Why a `Guard evidence` field, not just prose:** a prevention check that lives only
as a paragraph here is read once and then forgotten under context pressure.
The `Guard evidence` field directs the lesson toward a concrete checklist item,
gate condition, or table row in the target skill — something that is present
every time that skill loads, not just when someone happens to re-read this
file. A guard is not complete merely because this lesson claims it exists.

**2026-09-06 static guard review:** L001–L008 have scoped guards implemented
in the inspected instruction text, including the governing system/routing
limits described below. All eight remain **behaviorally unvalidated**. The earlier
eight `Promoted: Yes` labels are withdrawn. This review does not validate
historical incidents, engineering values, legal findings, or whole target skills.

---

## Lesson L001 — Roof Dead Load Requires Assembly-Specific Evidence

**Source basis:** De-identified roof-load input incident; private project identity omitted.

**Trigger:** Any structural calculation involving a pre-1990 Norwegian residential roof with concrete/ceramic tiles

**What failed:** The incident record reports use of a roof-load value
without a verified assembly-based load takeoff. A later pass changed the
load while retaining a disputed span. Neither the original value nor its
replacement is validated here; a universal replacement range would repeat
the unsupported-input error.

**Prevention check:**
Before calculating any roof dead load on a pre-1990 Norwegian house:
1. Establish the actual assembly and source each component's mass or density
	and thickness, including covering, battens, structure, insulation, ceilings,
	services, and any other permanent loads within the calculation scope.
2. State units and whether each value is per sloping roof area or horizontal
	projected area. Show any conversion and avoid double counting.
3. Label missing components and assumptions as unverified. Do not prescribe
	an accepted total merely from the roof's age, nationality, or tile type.
4. Record a component-by-component takeoff in the locked inputs and obtain
	the responsible structural engineer's verification before design use.

**Guard evidence:** [Dead Loads](../structural-engineering/SKILL.md#dead-loads-egenlast)
contains the L001 assembly takeoff, units, area-basis, missing-component, and
designer-verification guard. [Dead Load Material Properties](../formulas-reference/SKILL.md#24-dead-load-material-properties)
removes the malformed tile value without guessing a replacement and requires
sourced manufacturer mass/coverage and explicit conversions. The structural
warning against using that former mixed-unit row remains a valid prohibition,
not evidence of a usable load. Other reference-table values are not validated.

**Target skill(s):** `formulas-reference`; `structural-engineering`

**Promotion status:** Implemented (instruction text).
**Validation:** 2026-09-06, static text inspection only; engineering values and behavior unvalidated.

---

## Lesson L002 — Span Drift When a Value Is Corrected Mid-Session

**Source basis:** De-identified corrected-span incident; private identity and measurements omitted.

**Trigger:** Any time a measurement or dimension is corrected after initial analysis has started

**What failed:** A beam span was corrected mid-session. Some summaries used
the corrected span while a calculation document retained the superseded
value. No document flagged the contradiction, leaving inconsistent claims
of an authoritative input.

**Prevention check:**
When any dimension is corrected:
1. Immediately state: "⚠️ Input change: [old value] → [new value]. All calculations using [old value] are now VOID."
2. List explicitly which documents are superseded
3. Do not proceed with any new analysis until the correction is acknowledged and the locked input table is reissued
4. Never produce a "verification pass" that silently uses different values from the original

**Guard evidence:** [structural-engineering](../structural-engineering/SKILL.md),
"Calculation Input Lock Protocol", requires the locked table before formulas,
voids the package on input change, and calls for supersession and recalculation.
This is implemented as instruction text, not an automated consistency check.

**Target skill(s):** `structural-engineering` Calculation Input Lock Protocol

**Promotion status:** Implemented (instruction text).
**Validation:** 2026-09-06, static presence confirmed; cross-document propagation and behavior unvalidated.

---

## Lesson L003 — Installed Beam Profile Needs Traceable Identification Evidence

**Source basis:** De-identified installed-section identification incident; private identity omitted.

**Trigger:** User asks Bob to identify or confirm a steel beam profile from visual evidence, gypsum board thickness comparison, crew size, or order timing

**What failed:** Indirect visual and circumstantial methods were rated weak
but then treated as confirmation of an installed section. A structural
adequacy check was produced for an unconfirmed profile.

**Prevention check:**
Bob must not produce a structural adequacy check for a beam of unconfirmed profile. Instead, state:

> "The installed beam profile is unconfirmed. Resolve it through reliable
> as-built documentation or sufficient direct measurements compared with a
> verified section table, with engineer inspection where needed. A photograph,
> presumed nominal dimensions, or an order record alone does not confirm the
> installed member. Section identification also does not establish steel grade,
> condition, restraints, connections, or adequacy."

If the user requests a hypothetical comparison, identify the assumed section
and all unresolved inputs, label it LOW confidence and not for design or
sign-off, and respect the Drawing Freeze Gate. Do not present it as an adequacy
check of the installed beam.

**Guard evidence:** [Steel Beam Assessment](../structural-engineering/SKILL.md#steel-beam-assessment)
contains the installed-section identification gate (L003), including rejected
indirect methods, traceable as-built/direct-measurement evidence, and the
separate limits on grade, condition, restraint, connections, and adequacy.
Its [Trust Boundary](../structural-engineering/SKILL.md#trust-boundary) permits
only labeled hypothetical comparisons, not installed-member confirmation.

**Target skill(s):** `structural-engineering`, beam identification methodology

**Promotion status:** Implemented (instruction text).
**Validation:** 2026-09-06, static text inspection only; identification and behavior unvalidated.

---

## Lesson L004 — Positive Safety Status Requires Scope-Specific Verification

**Source basis:** De-identified unsupported safety-status incident; private identity omitted.

**Trigger:** A structural or ground-safety status is requested without scope-specific professional verification, or permission/exemption is offered as safety evidence

**What failed:** The incident record reports an overall GREEN status after
a completed wall removal and steel beam installation, without documented
scope-specific structural review or permit records in the reviewed material.
The work's authorization and adequacy were **undocumented**, not established
as illegal or unsafe. The historical "unlicensed" description is unsupported
absent verified evidence of the applicable requirements and actual status.

**Prevention check:**
A structural status needs evidence specific to the installed or proposed
work, its load path, supports, connections, and condition, reviewed by the
responsible structural professional where required. Any positive status must
state exactly which scope was verified and identify the supporting record.

**A permit or responsibility exemption is not evidence of structural or
geotechnical safety.** It does not confirm ground conditions, bearing capacity,
or slope stability and cannot turn an unknown safety status GREEN. Keep
administrative permission and technical verification as separate decisions.

For completed modifications without documentation, the structural status is:
**UNKNOWN: structural adequacy not established for [element/scope]. Seek a
qualified structural designer's assessment and the supporting records.**
Identify ansvarlig prosjekterende where the Norwegian responsibility route
applies; do not import foreign credential or stamping requirements.

**Guard evidence:** [Trust Boundary](../structural-engineering/SKILL.md#trust-boundary)
requires scope-specific verification and prohibits GREEN via an exemption
or a limited calculation. The [ground evidence gate](../geotechnical/SKILL.md#trust-boundary)
separates photographs, mapping, investigation, and professional assessment;
visible bedrock or absent map hazards do not establish bearing or stability.
[System safety guards](../../system_prompt.md#safety-and-review-triggers)
also prohibit inferring illegality or safety from missing documentation.

**Target skill(s):** `structural-engineering`; `geotechnical`; system safety guards

**Promotion status:** Implemented (instruction text).
**Validation:** 2026-09-06, static text inspection only; behavior unvalidated, no engineering or geotechnical certification.

---

## Lesson L005 — Boundary Distances from Drawings Are Preliminary, Not Confirmed Violations

**Source basis:** De-identified drawing-derived boundary claim; private identity omitted.

**Trigger:** Boundary/setback or compliance claims rely on drawings, uncertain cadastral lines, or measurements not establishing the relevant legal boundary and applicable rule

**What failed:** Retaining wall distances were inferred from reading the developer's submitted drawings. These inferred distances were presented as "🔴 LIKELY VIOLATION" in formal-looking analysis. Formal correspondence to the municipality was then drafted asserting these violations. If the drawing-inferred distances were wrong (drawings are often imprecise at boundaries), the client would have filed an incorrect complaint with the municipality.

**Prevention check:**
1. Record source/revision, method/accuracy, boundary segment, relevant geometry,
	and measurement endpoints/datum. Distinguish drawing-dimensioned, scaled,
	cadastral, site-measured, and survey-confirmed evidence.
2. Label drawing-derived distances preliminary and not survey-confirmed.
	Describe an apparent discrepancy or potential breach, not a confirmed violation.
3. A confirmed violation needs the relevant boundary and geometry verified,
	plus the applicable plan/rule, measurement method, and decisions/exemptions.
	Survey evidence alone does not establish legal noncompliance.
4. A bounded clarification request may ask the municipality or competent
	survey professional to establish those facts. A new survey is not an absolute
	prerequisite to that query. Retain: "These distances are preliminary estimates
	from drawing review, not survey-confirmed boundary distances."
5. Hold unsupported consequential allegations, not the request for evidence;
	apply the appropriate review and sender-authorization gate before release.

**Guard evidence:** [Step 3: Establish Scale and Dimensions](../architectural-drawing-reading/SKILL.md#step-3-establish-scale-and-dimensions)
contains the L005 boundary-source labels and requires applicable-rule checks
as well as boundary evidence. Its survey-verification warning concerns the
distance claim, not a blanket ban on clarification. The [Official Correspondence Gate](../soknad-package/SKILL.md#official-correspondence-gate-l005l006)
allows unresolved claims to be rewritten as verification requests while
holding confirmed-violation allegations pending verified facts and legal basis.

**Target skill(s):** `architectural-drawing-reading`; `soknad-package`

**Promotion status:** Implemented (instruction text).
**Validation:** 2026-09-06, static text inspection only; survey facts and behavior unvalidated.

---

## Lesson L006 — Draft Legal Correspondence Must Be Clearly Labeled as Drafts

**Source basis:** De-identified correspondence-release incident; private identity omitted.

**Trigger:** Any request to draft letters, emails, or submissions addressed to municipalities, Byantikvaren, Riksantikvaren, courts, or other official bodies

**What failed:** Formal letters to a municipality were produced as if ready
to send, despite relying on drawing-inferred boundary distances and
unreviewed legal analysis.

**Prevention check:**
All correspondence to official bodies must:
1. Carry **DRAFT FOR REVIEW**, identifying AI advisory preparation, intended
	use, evidence basis, and unresolved claims. Drafting does not submit or approve.
2. Use the official correspondence pre-send checklist: inspected claim sources,
	exact attachment manifest/revisions, dispatch evidence/status, current deadline
	and legal basis, boundary/factual claims, scope, and money/VAT where relevant.
3. Match review to the claims and consequences: survey/authority clarification
	for boundaries, technical designer for safety, planning or legal review where
	needed. A routine factual or clarification query does not universally require
	a lawyer. Rewrite unsupported allegations as bounded questions or hold them.
4. Obtain authorized-sender approval before sending. Distinguish prepared,
	reviewed, approved for issue, sent, and receipt confirmed; verify each claimed
	status. Do not present an unreviewed draft as ready to send.

**Guard evidence:** [Official Correspondence Gate](../soknad-package/SKILL.md#official-correspondence-gate-l005l006)
provides the header and scoped pre-send checklist for official recipients;
its [Trust Boundary](../soknad-package/SKILL.md#trust-boundary) rejects a universal
lawyer requirement. [Correspondence Claims Gate](../residential-tender-writing/SKILL.md#correspondence-claims-gate)
implements related source, attachment, dispatch, deadline, scope, currency,
VAT, and owner-release checks for tenders and addenda. [Output and Completion](../../system_prompt.md#output-and-completion)
preserves advisory labeling and distinct document/release statuses.

**Target skill(s):** `soknad-package`; `residential-tender-writing`; system document rules

**Promotion status:** Implemented (instruction text).
**Validation:** 2026-09-06, static text inspection only; pre-send behavior unvalidated.

---

## Lesson L007 — Analysis Before Drawings Produces Unreliable Results

**Source basis:** De-identified drawing-basis incident; private identity and revisions omitted.

**Trigger:** User requests detailed structural analysis while architectural drawings are pending revision, under correction, or have known errors

**What failed:** Structural analysis preceded review of the relevant drawing
basis. Later review reported material errors in existing conditions, layout,
and structural proposals, undermining the earlier analysis inputs.

**Prevention check:**
When drawings are flagged as having errors, pending correction, or under architectural revision:
1. Identify which safety-critical geometry, load path, supports, or loads are
	unresolved and which calculations/recommendations depend on them. Hold
	affected detailed design and installed-member adequacy claims.
2. Inspect relevant available pages/revisions and request only evidence needed
	for the bounded question. Do not require the entire drawing package or load
	every drawing-review skill for a concept explanation.
3. Clearly labeled bounded conceptual guidance, qualitative alternatives, and
	LOW-confidence preliminary guidance remain allowed with missing drawings.
	Do not disguise design calculations or a build-ready recommendation as a concept.
4. A drawing freeze or user-confirmed input does not establish technical or
	statutory approval. Revalidate affected results when the evidence changes.

**Guard evidence:** [structural-engineering](../structural-engineering/SKILL.md),
"Drawing Freeze Gate", contains a detailed-calculation hold and preliminary
exceptions. Apply its package-wide wording within the governing
[Evidence Before Conclusions](../../system_prompt.md#evidence-before-conclusions)
and [Evidence and BIM Gates](../routing/SKILL.md#evidence-and-bim-gates): review
relevant evidence, permit bounded concepts, and block unsupported build-ready
advice. The old routing "Rule 1" anchor no longer exists. These text guards do
not establish that any particular drawing basis passed or that execution obeyed them.

**Target skill(s):** `structural-engineering` Drawing Freeze Gate; routing evidence gates; system evidence rules

**Promotion status:** Implemented (instruction text).
**Validation:** 2026-09-06, static presence confirmed; runtime gate behavior unvalidated.

---

## Lesson L008 — Unmatched Concerns Need Plain-Language Review, Not Invented Flags

**Source basis:** De-identified unmatched-review-trigger incident; private identity omitted.

**Trigger:** A concern needs review but no standard advisory review trigger applies, or a legacy/custom flag is encountered

**What failed:** The flag `ROAD_SAFETY_AUTHORITY_ALIGNMENT_REQUIRED` appeared in a decision log but is not in the standard matrix. No one reading this flag knows who to call, what timeline applies, or what action is required.

**Prevention check:**
If a situation requires escalation but no standard flag covers it:
1. Check [Safety and Review Triggers](../../system_prompt.md#safety-and-review-triggers).
	Use a standard trigger only when its actual scope applies, not merely the
	closest-sounding label. Advisory review triggers are not legal findings.
2. If none applies, state the **plain-language concern, appropriate reviewer,
	and next evidence/verification step**, including relevant uncertainty or urgency.
3. Do not invent an official-looking flag, force-fit an unrelated trigger, or
	claim an invented timeline or authority requirement. Explain legacy labels
	using the current evidence and reviewer rather than silently endorsing them.

**Guard evidence:** [Routing Trust Boundary](../routing/SKILL.md#trust-boundary)
and [system review triggers](../../system_prompt.md#safety-and-review-triggers)
establish advisory status, source verification, and scoped review. Both now
explicitly require a plain-language concern, reviewer and next evidence when
no listed trigger fits, without inventing an official-looking flag.

**Target skill(s):** routing Trust Boundary; system Safety and Review Triggers

**Promotion status:** Implemented (instruction text).
**Validation:** 2026-09-06, static text inspection only; escalation behavior unvalidated.

---

## Adding New Lessons

When a project reveals a new failure pattern:

1. **Capture it immediately** in the project's `btba-feedback.md` or `decision-log.md`
2. **Classify it**: Is this a calculation error? A process failure? A legal boundary issue? A missing rule?
3. **Write the lesson** in the format above
4. **Update the relevant skill** with a reversible prevention rule when within
	scope; otherwise record the missing guard for the owning editor
5. **Add the lesson here** with evidence and separate implementation/validation
	status. Routine local capture does not require a fresh approval. Do not
	promote assumptions into engineering facts or bypass consequential-action gates.
6. **Keep shared lessons de-identified.** Retain client names, addresses, exact
	project inputs and source records in the private project. Publication of
	specific private data requires explicit authorization for that destination.

**Lesson ID convention:** L001, L002, ... in chronological order of discovery

---

## Promotion Pass

Review when a target guard changes, a contradictory claim is found, or the
queue reaches **10 lessons**. Inspect the actual target file and section;
record missing, partial, or implemented instruction text separately from
behavioral validation. Record test cases and results when testing is permitted.
Never infer runtime enforcement from prose or a clean structural lint run.

Retain these eight write-ups while validation gaps remain. Do not trim a
lesson solely because a guard exists in text. Later consolidation must preserve
the incident provenance, guard location, review date, tests, and open limitations.

---

*Review this skill after an evidenced recurring failure; do not assume review occurred.*
*Current lessons: L001–L008 (de-identified failure patterns; private project identities omitted)*
*Last updated: 2026-09-06 (static guard review; behavior unvalidated)*
