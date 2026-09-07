---
name: residential-tender-writing
description: Draft or review Norwegian residential tenders, preliminary pricing requests, procurement packages, and contractor bid/no-bid assessments with explicit scope and responsibility.
triggers: [tender, anbud, anbudsforespørsel, contractor bid, bid request, procurement package, bidder review, bid/no-bid, conditional bid, scope of work, budget pricing, construction loan, byggelån, milestone payment, RIB, totalentreprenør, hovedentreprenør, homeowner brief, construction brief]
load_with: [construction-execution]
safety_level: high
license: Proprietary
---

# Residential Tender Writing

## Trust Boundary

**Bob may, on his own analysis:** draft, rewrite, or review the tender document structure, scope clarity, and responsibility language; make advisory bidder recommendations against supplied evidence and criteria, not decide for the contractor.

**Bob may flag only as preliminary:** any price, quantity, or schedule figure included in a draft tender — these come from the owner/architect/RIB, not from Bob.

**Always requires the owner's and, where applicable, the architect's/RIB's sign-off before a client tender can be sent:** a tender is a legal/commercial document; Bob produces a draft, never a document presented as final or binding. In bidder mode, the contractor must authorize its own offer and obtain applicable professional reviews; Bob cannot accept obligations for either party.

---

## Purpose

Produce a contractor-friendly residential tender that is clear enough to price, honest about uncertainty, and explicit about responsibility. The tender should help a good contractor decide quickly whether to bid, what is included, what is provisional, and how the work will be managed.

Client-side tender writing is the default. Use the optional bidder review mode only for a contractor's assessment of whether and on what conditions to bid. Neither mode replaces architectural, structural, geotechnical, fire, moisture, electrical, plumbing, or legal advice.

## Core Principle

Write the tender in two layers:

1. **Tender body:** short, readable, commercially clear, and focused on the work, outcomes, interfaces, programme, and price response.
2. **Technical appendix:** drawings, structural concepts, calculation assumptions, alternative systems, code references, preliminary quantities, and unresolved design questions.

The tender body should state what must be achieved. The contractor and appointed designers should select and verify the compliant means of achieving it unless the owner has a genuine non-negotiable requirement.

## When To Use

Use this skill for:

- A new contractor bid request or preliminary budget estimate
- Rewriting a technical homeowner brief into a bid-friendly tender
- Comparing an English tender with a Norwegian contractor email
- Separating a tender from a design brief or structural appendix
- Clarifying contractor, architect, RIB, subcontractor, and owner responsibilities
- Adding milestone payments to a continuous construction project
- Reviewing a tender for ambiguity, scope creep, or contractor-unfriendly wording
- Structuring optional procurement package records or reviewing a contractor's bid/no-bid position

Do not use this skill as the primary workflow for structural calculations, permit determinations, drawing extraction, or contractor performance review. Route those questions to the relevant domain skill and use this skill only for the tender document.

## Required Inputs

Before drafting, identify:

- Property, municipality, project type, and whether the property remains occupied
- Current drawing and permit status
- Whether the request is preliminary pricing, a negotiated offer, or a fixed-price tender
- Intended contract model and who will coordinate the site
- Owner-supplied materials, trades, consultants, and resources
- Non-negotiable outcomes versus owner preferences
- Known site observations and what remains unverified
- Payment model, including whether construction is continuous or intentionally paused
- Desired language and recipient

If a critical input is missing, state an assumption and mark it for confirmation. Do not invent a scope, price, approval, site condition, or professional responsibility.

## Workflow

### 1. Classify The Document

Choose one primary form:

- **Short bid request:** normally 3-6 pages plus attachments
- **Preliminary budget request:** asks for assumptions, exclusions, provisional sums, and accuracy range
- **Fixed-price tender:** uses coordinated final drawings, defined quantities, contract terms, and change control
- **Technical appendix:** preserves engineering and design basis without making it the main bid letter

Never let one document silently act as a design brief, construction contract, execution plan, and permit application. State which function the document serves.

### Optional Procurement Package Record

Use when trade boundaries, multiple bids, or estimate reconciliation need traceability. Keep a small table or appendix within the requested deliverable, not a mandatory new file or prerequisite for a short enquiry. Reuse existing IDs; assign stable local IDs only where absent and label them as working identifiers, not issued references.

| Field | Record |
|---|---|
| Package ID and scope | Work/location and linked requirement IDs; identify included and excluded work explicitly. |
| Source basis | Exact document, section/drawing, date/revision, and status; preserve conflicting or missing sources as unresolved. |
| Design owner | Named responsible designer and agreed scope, or unassigned; distinguish proposed appointment from accepted responsibility. |
| Trade interfaces | Execution/coordination owner and boundaries for each adjacent trade and owner-direct supply, installation, testing, and handover. |
| Pricing lines | Stable line IDs linked to requirements; descriptions, quantities, units, rates or lump sums, currency and VAT basis; unknown values stay unpriced. |
| Allowances and alternatives | Allowance scope/basis and whether included; base option, mutually exclusive option groups, and replacement versus incremental prices. |
| Unresolved items | Question, evidence gap, affected lines, responsible resolver, target date if supplied, and impact on pricing or release purpose. |

Trace **requirement → package → pricing line** without silently expanding scope. An exclusion needs an explicit destination/owner or an unresolved gap, not disappearance. Reconcile returned prices using [Estimate Reconciliation](../general-contractor-review/SKILL.md#estimate-reconciliation) on demand; do not load unrelated disciplines for a commercial-only review.

### Optional Bidder Review Mode

Distinguish the **client's tender request** from the **contractor's proposed offer** before reviewing either. State whose decision is being supported. Do not turn client preferences into contractor commitments or a bidder review into a client award recommendation.

1. Record the supplied tender/addenda and proposed bid revisions, response deadline, scope, and design maturity. Apply the Correspondence Claims Gate below.
2. Record contractor-supplied capacity (people, supervision, trade availability, workload and dates), competence evidence, and bid criteria (mandatory requirements, commercial limits, risk appetite and any scoring thresholds). Label reported versus verified evidence. Do not invent availability, margins, scores, thresholds, or company policy.
3. Compare each supplied criterion with evidence and return met / unmet / unknown, the relevant package or line, and the clarification needed. Review exclusions, allowances, interfaces, programme and design obligations. Review contractual reservations through [Contract Departures Review](../construction-execution/SKILL.md#contract-departures-review) on demand, not by assuming a contract form or legal acceptability.
4. Return **bid**, **conditional bid**, or **no-bid recommendation** only where supplied evidence and criteria support it. For a conditional bid, list conditions, responsible resolver and required evidence/timing; for no-bid, identify the specific failed criterion and evidence. If decisive inputs are missing, return **insufficient evidence to recommend** with targeted questions, not an invented decision.
5. Separate recommendation from the contractor's actual decision. Record a decision/approval only if supplied, with its source and date. Contractor authorization is required before submitting its offer; owner authorization remains required for client correspondence. Neither recommendation authorizes sending, contracting, ordering, or construction.

Incomplete design does not automatically mean no-bid. An explicitly authorized preliminary enquiry may disclose design holds and request assumptions, ranges or designer appointment. Fixed-price, ordering and construction readiness require their own scope-specific gates; never present preliminary pricing as satisfying them.

### Correspondence Claims Gate

Apply to bid emails, tenders, cover letters, translations, and addenda. Keep **DRAFT FOR REVIEW** until the owner authorizes client correspondence, or the contractor authorizes its offer in bidder mode. Before describing a package as ready for the relevant party's review, check:

- [ ] **Exact documents:** Open the actual documents supporting each material claim. Record title/file, date/revision, relevant section, and what it establishes. A summary, filename, or later draft is not evidence of what a recipient received.
- [ ] **Attachment manifest:** List the exact filename/title, date/revision, purpose and scope/status (pricing basis, proposed design, reviewed design, etc.) of every intended attachment. Verify each exists, is the intended revision, and matches the body; flag missing or superseded items rather than silently substitute.
- [ ] **Dispatch status:** Distinguish draft, approved for issue, sent, and receipt confirmed. Only claim sent/issued with dispatch evidence identifying recipients, date, and the actual attachment set; only claim received with receipt evidence. If unavailable, write **dispatch unverified**. Preparing a draft does not send it.
- [ ] **Deadline:** Verify the absolute response date, time/time zone where relevant, source, and whether still current as of drafting. Do not silently renew a past deadline or treat a proposed date as agreed.
- [ ] **Currency and scope:** State monetary currency (e.g., NOK), estimate/quote date and validity, preliminary/fixed-price status, included/excluded work, owner supplies, allowances, alternatives, and any exchange-rate source/date. An addendum must state what it changes or supersedes; do not imply broader issued scope.
- [ ] **VAT:** State whether every quoted amount includes/excludes VAT, the applicable rate/basis if verified, and consistent totals. Unknown VAT treatment stays unknown; never compare net and gross as like-for-like.
- [ ] **Claims and approval:** Keep observations, assumptions, calculations, professional reviews, and authority decisions distinct. Match technical/legal claims to their evidence, name unresolved items/reviewer, and obtain the relevant sending party's authorization before any send (owner for client correspondence; contractor for its offer). Apply the same manifest, deadline, scope, currency, and VAT basis to all language versions.

### 2. Establish Responsibility Boundaries

Add a concise responsibility statement:

- Owner provides design objectives, available information, decisions, and access.
- Architect and responsible designers own their professional design scope.
- Contractor owns construction planning, site coordination, workmanship, and its contracted execution scope.
- Contractor-appointed RIB owns structural verification and structural design within the agreed scope.
- Each subcontractor remains responsible for its own workmanship and statutory documentation.
- The main contractor remains the day-to-day coordinator unless the contract expressly states otherwise.

If the contractor must appoint a RIB, do not simultaneously write as though the owner has selected the structural solution. Describe HC, timber, steel, roof, or foundation systems as comparison bases or owner preferences, then invite compliant alternatives.

### 3. Separate Outcomes From Methods

Use this conversion:

| Avoid | Prefer |
|---|---|
| "Install HC 320" | "Provide a floor solution that meets span, load, deflection, fire, acoustic, height, and support objectives. HC 320 is an owner comparison basis." |
| "No excavation is required" | "Prior site observations indicate excavation and exposed rock. Contractor and RIB shall verify ground conditions and price assumptions." |
| "The contractor must use this roof detail" | "Provide an independent, weatherproof, movement-tolerant roof junction. Contractor/RIB shall design and document the compliant detail." |
| "Raymond coordinates the plumbing" | "Raymond may perform only agreed tasks. The main contractor retains site coordination and must document interfaces." |
| "Phase 1, Phase 2, Phase 3" as funding periods | "Scope categories shown in construction order. One continuous build with milestone payments." |

Retain hard constraints only when they are genuinely required, such as no internal columns, an owner-supplied window, a planning decision, a required appearance, or an agreed excluded trade.

When a preferred system has meaningful functional reasons, state both the preference and the rationale. For example: "The owner's preference is for a concrete garage ceiling because of acoustic, fire, durability, and vibration considerations. Hollow-core is one comparison basis only. The contractor and RIB may propose another system that achieves the same performance, span, support, and clear-height objectives." This preserves useful technical understanding without turning a product choice into an owner-directed design.

### 4. Make Owner-Supplied Interfaces Explicit

Create an **Owner-Supplied Resources and Interfaces** section for every external party or owner resource. For each party state:

- Exact work included
- Work excluded from contractor price
- Who schedules access and deliveries
- Who approves changes
- Who owns workmanship, testing, documentation, and warranty
- How the contractor coordinates the interface

State that owner resources cannot direct the contractor's workers, approve deviations, alter the programme, or order variations unless formally authorized in writing.

### 5. Treat Existing Conditions As A Priced Risk

For an existing house or renovation:

- Describe observations as information, not guarantees.
- Require the contractor to inspect accessible framing, services, moisture, previous alterations, and connection points.
- Require temporary-support planning before structural openings.
- Require prompt written notice with photographs when hidden conditions are found.
- Require a cost and programme assessment before non-urgent variation work proceeds.
- Ask the contractor to identify included, provisional, and excluded existing-condition risks.

### 6. Handle Continuous Construction And Milestone Payments

If the build is continuous, say so plainly. Scope headings may still be numbered for pricing, but they are not separate contracts or planned stop-start periods.

Ask for:

- One integrated programme
- Earliest start date and estimated continuous duration
- Construction milestones with values
- Objective completion or inspection evidence for each payment
- Retention, holdback, and final-payment terms
- Monthly cost forecast and notice of budget risk
- Written change-order procedure
- No planned pause, demobilization, or remobilization unless agreed in writing

Do not request pause and restart pricing unless the owner genuinely intends to pause the build.

### 7. Keep The Tender Readable

Put the following in the body:

- Project and property summary
- Current design and permit status
- Continuous-build and payment model
- Occupied-home expectations
- Main scope and exclusions
- Owner-supplied interfaces
- Key outcomes and non-negotiables
- Bid response checklist
- Site visit and contact instructions

Move the following to an appendix unless essential to pricing:

- Detailed load assumptions and formulas
- Alternative structural profiles and preliminary calculations
- Repeated TEK17 citations
- Detailed roof junction commentary
- Trade-by-trade execution sequencing
- Drawing audit findings
- Historical design decisions

The appendix should be referenced, not silently mixed into the commercial request.

### 8. Add The Commercial Questions Contractors Need

Ask for:

- Company name, organization number, and contact details
- Contract form proposed and consumer-law basis
- Directly performed and subcontracted trades
- Responsibility roles and competence documentation
- Earliest start date and estimated duration
- Current workload and comparable references from the last three years
- Site manager or foreman
- Insurance and coverage boundaries
- Scaffolding, crane, waste, temporary works, and site protection assumptions
- Preliminary price excluding and including VAT
- Validity period, accuracy range, assumptions, exclusions, and provisional sums
- Confirmation that a later fixed-price offer can be produced after final design and approvals

## Output Format

For a new tender, use this order:

1. Title, date, recipient, attachments
2. Short purpose statement
3. Project summary and current status
4. Responsibility and design boundary
5. Occupied-home requirements
6. Continuous construction and milestone payments
7. Main scope and desired outcomes
8. Owner-supplied resources and interfaces
9. Existing-house and site-condition requirements
10. Exclusions and provisional items
11. Contractor response checklist
12. Site visit, contact, and next step
13. Technical appendix reference

For a review, report findings in this order:

1. Contractual or safety-critical ambiguity
2. Scope and responsibility conflict
3. Contractor pricing or bidding friction
4. Missing commercial information
5. Readability and document-structure improvements
6. Recommended replacement wording

For bidder review, instead report perspective and source set, criteria/capacity evidence, package/interface gaps, contract departures reference, supported recommendation or evidence shortfall, conditions and next decision owner. Append package records or reconciled pricing only when relevant.

## Quality Gate

Before declaring the tender ready for owner review (not sent or binding), check:

- The Correspondence Claims Gate is complete or unresolved items are explicitly held for confirmation.
- The document says whether pricing is preliminary or fixed-price.
- One party clearly owns construction coordination.
- Design responsibility is not split ambiguously between owner and contractor.
- Owner preferences are labeled as preferences, comparison bases, or non-negotiable outcomes.
- No ground, hidden-condition, or existing-structure assumption is presented as guaranteed.
- Owner-supplied trades and warranty boundaries are explicit.
- Continuous construction is separated from milestone-based payment.
- Change orders require written approval, subject to urgent damage-prevention exceptions.
- Occupied-home cost impacts are acknowledged and requested transparently.
- Insurance, programme, duration, references, and site management are requested.
- Technical appendix material is clearly identified and does not silently create extra contractor scope.
- English and Norwegian versions express the same responsibilities, exclusions, roof basis, and payment model.
- Where used, package records trace requirements to pricing lines; missing prices, alternatives and overlaps remain explicit, and arithmetic reconciliation is separate from price adequacy.
- Bidder recommendations use supplied capacity/criteria and remain distinct from authorized decisions; preliminary enquiries retain purpose-specific release boundaries.

## Common Failure Modes

| Failure | Correction |
|---|---|
| Tender reads like an engineering report | Move calculations and alternatives to an appendix; keep outcomes in the body. |
| Contractor is asked to design and merely price an owner-selected solution | State who owns design and invite compliant alternatives. |
| Owner resource is treated as a second project manager | Define its limited role and retain one site coordinator. |
| Site observations become guarantees | Use observation language and require independent verification. |
| Scope categories are mistaken for stop-start phases | State continuous construction and milestone payments explicitly. |
| Preliminary estimate sounds like a fixed price | Label status, assumptions, exclusions, provisional sums, and accuracy. |
| Existing-house surprises are ignored | Add an investigation, notice, and variation process. |
| Technical detail is repeated in two language versions inconsistently | Maintain one responsibility and interface matrix, then translate it consistently. |

## Post-Run Reflection

After completing a tender task, record what caused ambiguity, contractor friction, or repeated clarification. Add a durable prevention rule to the local [lessons learned skill](../lessons-learned/SKILL.md) when the issue is likely to recur across projects.

## References

| Reference | Use |
|---|---|
| [Construction execution](../construction-execution/SKILL.md) | Site sequence, contractor coordination, contract administration, safety, and handover. |
| [General contractor review](../general-contractor-review/SKILL.md) | Drawing-based constructability and coordination review. |
| [Building code and TEK17](../building-code-tek17/SKILL.md) | Regulatory requirements where a specific code issue affects tender wording. |
| [Structural engineering](../structural-engineering/SKILL.md) | Structural scope and escalation when the tender includes load-bearing work. |
| [Lessons learned](../lessons-learned/SKILL.md) | Record recurring tender failures and prevention checks. |
