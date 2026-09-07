---
name: routing
description: "Route each task after startup to scoped evidence and relevant skills, including lifecycle updates and overlapping safety domains, without recursive loading."
triggers: [task classification, changed intent, new attachment, lifecycle update, multi-domain review]
load_with: []
safety_level: high
license: Proprietary
---

# Skill: Routing

## Purpose

Apply after [system_prompt.md](../../system_prompt.md) and
[session-initialization](../session-initialization/SKILL.md). Classify each new
task or changed intent without rereading unchanged instructions. Keep the
working set small without omitting safety-relevant domains.

## Trust Boundary

The high rating concerns process integrity. BTBA may classify, prioritize, and
load sources independently. Skill matches identify possible review needs, not
legal requirements, approval, or proof that an undocumented action was illegal.
Use the system prompt's advisory review triggers and source-verification rules,
including when a legacy domain skill asserts a stronger universal rule.
Immediate danger receives concise safety escalation before any routing work.

For a concern outside the system prompt's listed review triggers, state the
concern, appropriate reviewer, and next evidence in plain language. Do not
invent an official-looking flag or use an unrelated category to imply authority.

## Scoped Loading Procedure

1. Preserve startup's repository/general/project mode. An explicit project switch
	updates scope without repeated intake; clarify only ambiguous switches. Match
	conversational/requested language independently of Norwegian jurisdiction.
2. Identify the actual task, relevant attachments, and all material hazards or
	cross-domain dependencies. In repository mode, editing a structural skill does
	not itself trigger a site assessment or private-project lookup.
3. Apply **all relevant rows** below, not the first matching row. An image, BIM,
	aesthetic, or lifecycle task must not suppress structural, ground, electrical,
	fire, heritage, or other safety concerns present in the request.
4. Load the minimum useful sections of selected skills and sources. In project
	mode, consult the index/current summary before following relevant evidence.
	Stop expanding when evidence is sufficient for the bounded answer. Report gaps.
5. For broad tasks, sequence small work batches yourself and retain a combined
	hazard/dependency checklist. There is no hard three-skill cap and no ban on
	combining design and safety skills. Surface urgent issues without waiting for
	every batch; do not force the user to restate a multi-domain request.

## Task Routes

Each skill link is relative to this file. Add other rows only when their scope
is actually implicated, not merely because a word appears in an address or quote.

| Intent or evidence | Load and scope |
|---|---|
| Repository instructions, tooling, or skill maintenance | Requested files and relevant authoring conventions; no automatic construction-domain load. |
| Project index/current summary, document revision, evidence conflict, corrected input, release hold, archive, superseded documents, project folder hygiene | [project-lifecycle](../project-lifecycle/SKILL.md); add technical domains only to resolve technical dependencies. |
| Drawing-file extraction: PDF, raster, DXF | [drawing-reader](../drawing-reader/SKILL.md); add [architectural-drawing-reading](../architectural-drawing-reading/SKILL.md) for interpretation. Inspect only relevant pages/revisions. |
| Chat photo, screenshot, unclear drawing evidence | [drawing-investigation-protocol](../drawing-investigation-protocol/SKILL.md); add [architectural-drawing-reading](../architectural-drawing-reading/SKILL.md) for drawings. Ask only material unanswered questions. |
| Load paths, wall removal, beam/floor capacity, supports, structural distress | [structural-engineering](../structural-engineering/SKILL.md); add regulatory review for actual alterations/compliance and ground review for foundation interactions. |
| Numerical engineering calculation | Relevant domain skill plus [formulas-reference](../formulas-reference/SKILL.md) as needed; state inputs, evidence status, assumptions, and applicability before results. |
| TEK17/PBL/SAK10, permits/exemptions, fire/escape, use change, setbacks, regulatory energy limits | [building-code-tek17](../building-code-tek17/SKILL.md); verify applicable sources and scope. |
| Søknad package, nabovarsel, application drawings, BRA/BYA for permits, completion documentation | [soknad-package](../soknad-package/SKILL.md) plus [building-code-tek17](../building-code-tek17/SKILL.md); preserve draft/submitted/approved distinctions. |
| Soil, ground investigation, quick clay, excavation, settlement, slope, flood exposure, foundations | [geotechnical](../geotechnical/SKILL.md); add structural review for load transfer and regulatory review for site safety requirements. |
| Moisture, insulation, airtightness, vapor control, roof/wall assemblies, frost protection | [sintef-byggforsk](../sintef-byggforsk/SKILL.md); add relevant trade, structural, or regulatory scope. |
| Heritage status/materials, SEFRAK, protection decisions, conservation or restoration | [historic-preservation](../historic-preservation/SKILL.md); add regulatory review for interventions/consents. Age alone does not establish protection. |
| Sequencing, temporary works, demolition, hazardous materials, site safety, contracts, FDV/handover | [construction-execution](../construction-execution/SKILL.md); include structural/ground/trade safety and regulatory rows where implicated. |
| Residential tender or contractor pricing request | [residential-tender-writing](../residential-tender-writing/SKILL.md); add lifecycle for conflicting versions or release holds and technical domains for unresolved scope. Drafting is not issuing. |
| Procurement packages, scope-to-price mapping, contractor bid/no-bid decision | Optional package/bidder modes in [residential-tender-writing](../residential-tender-writing/SKILL.md); distinguish client tender preparation from the contractor's decision. |
| Estimate audit, missing prices, duplicate scope, quote arithmetic or VAT reconciliation | [Estimate Reconciliation](../general-contractor-review/SKILL.md#estimate-reconciliation); do not run the full drawing-review workflow for a pricing-only question. |
| Contract departures, commercial reservations or comparison with accepted terms | [Contract Departures Review](../construction-execution/SKILL.md#contract-departures-review); establish actual contract and Norwegian consumer-law applicability, not default foreign commercial positions. |
| Package-based schedule, site progress report or FDV/O&M completeness | Relevant optional section of [construction-execution](../construction-execution/SKILL.md); separate proposed, reported and accepted states. No mandatory whole-project sequence. |
| Correspondence register, RFI tracking, unanswered queries or response closure | [Scoped Correspondence and RFI Records](../project-lifecycle/SKILL.md#scoped-correspondence-and-rfi-records); scoped local evidence updates, not automatic monitoring or external sends. |
| Cross-trade constructability or holistic drawing-package review | [general-contractor-review](../general-contractor-review/SKILL.md), with evidence extraction and affected domains in sequential batches. |
| Proportions, composition, facade, roof form, architectural style | [classical-architecture](../classical-architecture/SKILL.md); retain heritage, escape/fire, structure, and moisture checks where relevant. |
| Ventilation, heating, heat pumps, indoor air, mechanical energy systems | [hvac-mechanical](../hvac-mechanical/SKILL.md); add regulatory/fire/electrical checks as relevant. |
| Circuits, grounding, EV charging, solar electrical systems, electrical safety | [electrical-nek400](../electrical-nek400/SKILL.md); verify applicable rules and qualified-work boundaries. |
| Water supply, drainage, sanitary installations, leak protection | [plumbing-vs6050](../plumbing-vs6050/SKILL.md); add moisture, ground, or regulatory checks where needed. |
| Municipality-specific plans, hazards, local practice or conditions | [municipalities](../municipalities/SKILL.md) and relevant national rules; an address alone does not require this load. Local guidance cannot waive national law. |
| BIM, IFC, Revit/ArchiCAD/Bonsai, IDS, BCF, clash detection, translators, SIMBA, TFM, property mapping | [bim-ifc](../bim-ifc/SKILL.md); pure translator/requirements questions do not require drawing, permit, or infrastructure skills. |
| IFC4.3 civil/site models: roads, driveways, earthworks, retaining walls, boreholes/strata | [ifc-infrastructure](../ifc-infrastructure/SKILL.md) plus [bim-ifc](../bim-ifc/SKILL.md); add geotechnical/structural skills for engineering interpretation, not schema lookup alone. |
| Simplification, jargon explanation, learning resources | [technical-education-support](../technical-education-support/SKILL.md) when useful; retain relevant technical and safety limits. |
| Explicit retrospective or matching known failure mode, such as input drift or drawing-orientation confusion | Relevant section of [lessons-learned](../lessons-learned/SKILL.md) only; no mandatory startup or per-response lesson scan. |

## Evidence and BIM Gates

- Before a project-specific calculation, review relevant available drawings and
  verify the calculation basis. Unresolved safety-critical inputs block a
  build-ready recommendation, not clearly labeled conceptual guidance. A drawing
  "freeze" or user-confirmed input is not technical or statutory approval.
- Process new attachments incrementally; do not restart startup, recatalog all
  images, or demand unrelated sheets. Preserve extracted facts with their sources.
- For SIMBA/TFM, establish client, agreement, requirement revision, and delivery
  purpose from available evidence. These are not universal Norwegian requirements.
  Trace source-to-IFC mappings against applicable project requirements; a preset
  or successful validation is not acceptance or professional approval.
- IFC uses the BIM route, not a mandatory PDF/raster pipeline. Add geometry,
  structural, or regulatory interpretation only for the actual question. Keep
  model changes, BCF publication, and other external writes behind authorization.

## Dependency and Cycle Guard

The order is system prompt, startup, routing, then selected task skills. Startup
has a one-way `run_before` link to routing; these orchestration skills have empty
`load_with` lists. Lifecycle never calls startup again.

Treat domain `load_with`, `run_before`, and `auto_load_on` metadata as scoped
orchestration hints, not commands to recursively read the whole graph. Maintain
a visited set by canonical skill path for the task; load each skill once and
reuse it. Ignore self-links and back-edges, and order remaining prerequisites
before dependents. If a cycle leaves a genuine prerequisite unresolved, report
it and bound the affected assessment rather than looping or declaring approval.
Do not let metadata hints override the system prompt's evidence/safety boundaries.

## Deliverable Templates

Read only the template relevant to the requested output. Adapt legacy authority
or certification wording to the system prompt, and preserve draft/release status.

| Output | Template |
|---|---|
| Structural assessment memo | [structural-assessment-memo](../../templates/structural-assessment-memo.md) |
| Heritage assessment | [heritage-assessment](../../templates/heritage-assessment.md) |
| Construction sequence | [construction-sequence](../../templates/construction-sequence.md) |
| Pre-application meeting notes | [pre-application-meeting-notes](../../templates/pre-application-meeting-notes.md) |
| Compliance gaps | [compliance-gap-analysis](../../templates/compliance-gap-analysis.md) |
| Completion/conditions checklist | [post-approval-checklist](../../templates/post-approval-checklist.md) |

Finish with concise conclusions, supporting evidence, assumptions/limits, and
next actions. Do not expose private internal deliberation, assert complete hazard
coverage without a bounded review, or schedule unrequested background audits.

*Last reviewed: 2026-09-06*
