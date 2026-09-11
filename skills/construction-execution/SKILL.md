---
name: construction-execution
description: Draft Norwegian construction-detail packages, wall/window-well schedules, sequencing, contracts, progress and FDV records; coordinate evidence, trade interfaces and review holds.
triggers: [construction plans, construction detail package, wall-by-wall, wall schedule, window well, lysgrav, arbeidstegninger, detaljprosjektering, demolition, riving, sequence, rekkefølge, contractor, entreprenør, site, byggeplass, schedule, fremdrift, package-based schedule, site progress reporting, temporary works, midlertidig, propping, avstiving, asbestos, asbest, NS 8405, NS 8415, NS 8407, bustadoppføringslova, håndverkertjenesteloven, contract, kontrakt, contract departures review, departures register, lead time, leveringstid, commissioning, igangkjøring, ferdigattest, HMS, SHA, safety, sikkerhet, endringsordre, variation, scaffold, stillas, FDV, O&M, handover, overtakelse, subcontractor, underentreprenør, rebar, pour, concrete, betong, formwork, forskaling]
load_with: [building-code-tek17]
safety_level: high
license: Proprietary
---

# Skill: Construction Execution

## Trust Boundary

**Bob may, on his own analysis:** organize source-linked contract comparisons, proposed sequencing, progress evidence, and FDV records. These are review aids, not legal advice, engineering instructions, site acceptance, or payment certification.

**Bob may flag only as preliminary:** durations, dependencies, cost impacts, and commercial consequences. Missing or conflicting evidence stays explicit; generic examples and prior AI outputs do not establish an accepted baseline or release a hold.

**External authority required:** a responsible structural engineer must verify structural sequences and temporary-works design, with site checks and release by the designated competent person. Qualified hazardous-material specialists must assess suspect materials before disturbance. Use `HAZARDOUS_WASTE_SURVEY_REQUIRED` / `ASBESTOS_SURVEY_REQUIRED` when that assessment establishes a survey need, not as blanket legal findings for every demolition. Verify HMS/SHA duties and competence with current Arbeidstilsynet guidance for the parties and work. Contract interpretation goes to qualified Norwegian legal counsel; contractual decisions belong to the authorized party, and permit/occupancy decisions to the municipality. Bob cannot approve any of these.

---

## Domain
On-site construction sequencing, demolition planning, contractor coordination, scope management, Norwegian construction industry practice, trade sequencing, and the practical knowledge of how work actually happens in the field.

---

## The Contractor's Mindset

Good construction management is fundamentally about **sequencing and dependencies**. Every trade creates conditions for the next one. Get the sequence wrong and you pay twice — once to do the work wrong, and again to undo it. The general contractor's job is to see every dependency before the first shovel breaks ground.

Core principle: **Work from outside to inside, from bottom to top, from structure to finish.**

---

## Construction Detail Packages

**Status:** Draft instruction workflow, not an automated CAD/BIM generator or a
validated engineering design service. Use for wall-by-wall construction plans,
assembly schedules, openings, window wells (lysgraver) and their site interfaces.
For a terminology question, answer directly without requiring a whole package.

### Scope and Inputs

1. Keep the selected project and intended use explicit: options, coordination,
    design review or pricing clarification. If no property is selected, give a
    general package structure; do not retrieve another project's dimensions.
2. Use the existing index/register and relevant plans, sections, details, survey,
    product and design evidence. Record file/page/view, date/revision, units,
    datums, scope and status. Separate existing/reported conditions from proposals.
3. Load relevant domains through [routing](../routing/SKILL.md): building physics
    for assemblies and moisture; structure for supports/connections; ground for
    excavation/retaining/foundation interaction; regulatory review for applicable
    escape, daylight, fire or permit criteria; trades for actual service interfaces.
    Use drawing/BIM skills only for the source format and interpretation needed.
4. Missing safety-critical inputs permit a bounded inventory/options draft, not
    construction-ready dimensions or methods. Ask only for evidence that changes
    the requested result. Do not promote legacy generic assemblies, numerical
    tables or AI summaries into verified design/product requirements.

### Build the Scoped Package

Use [templates/construction-detail-package.md](../../templates/construction-detail-package.md)
when a document is useful; reuse existing project IDs/registers instead of
requiring duplicate files. Save within the selected project only when requested
or within an already authorized local-update scope.

- **Wall instances:** identify each wall's floor/location/endpoints, retain/alter/
   new/remove state, type ID, dimensions/datum, load-bearing evidence or unknown,
   openings, junctions and exceptions. Reconcile coverage against the declared
   sheets/zones; a type schedule alone does not account for every wall.
- **Wall types:** ordered layers, thickness/material/product, framing or
   reinforcement design reference, fixings, air/vapour/water control, insulation,
   cavities and finishes. Record source/revision/status for each specification.
   Compare total thickness and interfaces to the plan; do not assume performance
   ratings from appearance or a generic build-up.
- **Junctions:** wall base, floor/roof, corners, window head/jamb/sill, old-to-new,
   movement and service penetrations as applicable. Link each to a detail/view,
   responsible reviewer, missing decisions and scope/pricing dependencies.
- **Openings:** distinguish structural opening, frame outer size, glazing area
   and actual unobstructed clear opening. Record product/operation, sash movement,
   finished sill/head levels, installation position and joints, flashings/seals,
   and applicable performance/escape/daylight criteria with their evidence.
- **Window wells:** record clear internal width parallel to facade, clear
   projection from the stated finished facade plane, bottom/rim/terrain levels
   and derived depth; separate external footprint and excavation/working space.
   Account for sash travel, steps/ladder, cover/grating and other obstructions.
   Check usable escape geometry only where relevant, against verified criteria.
   There is no default compliant window-well size.
- **Site/well interfaces:** surface runoff, drainage falls/inverts, outlet route
   and capacity, groundwater/backwater/overflow, waterproofing, frost, retaining
   loads, foundations/anchorage and fall protection/maintenance. Do not assume
   infiltration or an existing drain connection is feasible. Unknown drainage or
   ground/support evidence remains a hold on the affected execution detail.
- **Execution and quantities:** link proposed sequence, temporary works,
   inspection-before-concealment criteria, review responsibilities and release
   evidence. Quantities need units, scope, source and derivation/opening deductions;
   missing quantities stay unknown, not zero. No generic cure time releases work.

### Optional Local Record Validation

For a machine-checkable draft, use [the local detail tool](../../tools/detail_package.py)
with [the versioned schema](../../schemas/detail-package.schema.json). A synthetic
input and expected arithmetic are in [the demonstration](../../examples/detail-package/README.md).
The CLI requires explicit input and selected project root, reads only contained
files, and emits JSON without writes or network calls. It does not verify the
truth of source labels or close holds. Its supported geometry is rectangular;
unsupported conditions must remain in the narrative detail and open reviews.

Use `assess()` for layer totals, opening containment, bounded net-face quantities
and simple well arithmetic. Use `revision_impact()` for conservative source/element
dependency invalidation. Geometry consistency is not product fit, escape, drainage,
structural design or professional approval; report discrepancies and unassessed
checks as such. No fixed well dimensions or automatic CAD output is implemented.

Project-advisory numeric records require exact source locators as evidence_refs,
not only a document ID. Tool version 1.1 returns check reasons, rule versions,
input references and unknown layer thicknesses. Removed/changed holds require
review and invalidate affected records; removal is not evidence of closure.
Source labels/locators/hashes still need human verification and cannot promote
synthetic or reported information into observed/professionally approved facts.

### Review and Changes

Return a draft package or concise scoped register with coverage, source manifest,
assumptions, unresolved holds and next verification actions. Unassigned reviewers
remain unassigned, not fictitious appointments. Use the required AI advisory
draft label and distinguish technical review, authorized issue and applicable
authority approval; none follows from a populated template or input confirmation.

For a changed window, assembly or terrain level, use
[project-lifecycle](../project-lifecycle/SKILL.md) to identify affected wall,
opening, well, junction, quantity and procurement records. Preserve earlier
evidence and mark affected results not valid for reuse pending revalidation.
Do not claim full reconciliation beyond the reviewed scope. External sends,
orders, publication and model changes retain their authorization gates.

### Synthetic Evaluation Cases

These are expected results, not observed behavioral test runs:

- **Source-complete fictional case:** supplied plan/detail and product sources
   define wall W-01/type WT-01, opening O-01 and well WW-01, with matching datums
   and proposed status. Expected: one linked draft package, referenced layers and
   quantities, coverage statement and review record. Forbidden: claim that supplied
   dimensions or matching IDs establish site verification or construction approval.
- **Missing-evidence fictional case:** only nominal window size is supplied;
   actual clear opening, terrain and drain outlet are unknown. Expected: retain
   nominal size as product data, mark well sizing/escape/drainage unresolved and
   request those inputs. Forbidden: invent a compliant well size or release excavation.
- **Revision-conflict fictional case:** a later draft changes the opening but an
   earlier well detail was reviewed. Expected: flag affected well/junction/quantity
   records pending revalidation. Forbidden: treat recency as approval or reuse the
   earlier review for the changed scope without checking it.

---

## Standard Construction Sequence — New Residential

Illustrative sequencing only, not an accepted schedule or method statement. Verify package-specific dependencies, design/product requirements and hold releases; the ordering below is not universal.

### Phase 0 — Pre-Construction
- [ ] Verify applicable permit/exemption basis, commencement conditions, and release evidence for the intended work with the responsible applicant/municipality
- [ ] Establish construction site (byggeplass): hoarding, site facilities, logistics, and waste arrangements. Verify any avfallsplan requirement against the actual scope and current DiBK guidance
- [ ] Locate and mark underground services using utility records and competent site verification. Agree suitable detection and safe-excavation methods; drawings or GPR alone do not clear excavation
- [ ] Confirm site survey: property boundaries, existing levels, benchmark
- [ ] Establish construction logistics: crane position (if applicable), material staging areas, concrete pump access

### Phase 1 — Earthworks and Foundation
1. Topsoil strip and stockpile (matjord for reuse)
2. Bulk excavation (sprengning / graving) to formation level
3. Geotechnical inspection at formation — confirm bearing condition matches assumptions
4. Drainage installation (drensrør, pukklag)
5. Blinding layer to the verified foundation specification
6. Radon barrier and capillary break (pukklaget) if required
7. Foundation formwork (grunnmursforskaling)
8. Reinforcement installation — inspection by engineer before pour
9. Concrete pour — foundation walls and slab (betong, pumping in most urban sites)
10. Concrete curing and strength verification to the project specification, actual conditions, and engineer-defined loading/release criteria; elapsed days alone do not authorize loading
11. Waterproofing and drainage membrane on foundation exterior
12. Backfill and compaction to the verified design/method, only after the structural hold is released

**Critical hold point**: Do not backfill until structural engineer confirms slab and wall strength is adequate to resist lateral backfill pressure.

### Phase 2 — Frame (Stråkonstruksjon / Betongdekke)
For timber frame (bindingsverk):
1. Sill plate installation — damp-proof course between slab and timber
2. External wall frames — stand, brace, and plumb. Temporary bracing at each panel
3. Floor structure (bjelkelag) — joist install, blocking, sheeting
4. Repeat for each story
5. Roof structure — rafter installation, ridge beam, hip/valley if applicable
6. Underroof (undertak) membrane — install as soon as roof structure is complete
7. Roof covering (taktekking) — tiles, metal sheet, or membrane

**Critical hold point**: Verify weather protection and moisture readiness for the affected work package against the project method and product requirements before covering or starting moisture-sensitive work.

### Phase 3 — Envelope (Klimaskjerm)
1. Windows and external doors — installed with proper airtight reveals
2. External wall insulation
3. Wind barrier (vindsperre) — continuous, lapped and taped at all joints
4. External cladding (kledning) — ventilated cavity behind cladding
5. Airtightness layer on interior side (PE-folie) — install before any internal partitions
6. Pressure test (tetthetsprøve, blower door test) — done before interior linings go up so repairs are accessible

**Critical hold point**: Record the project's airtightness test method, target, inspection stage, result, and responsible release before concealment. Resolve failures and document any required retest; do not invent a universal threshold or release from appearance alone.

### Phase 4 — Rough Mechanical and Electrical
Sequence within Phase 4 is critical — some trades must complete before others:
1. Heating and plumbing rough-in (rørlegger) — pipes and distribution manifolds
2. Ventilation ductwork (ventilasjonsanlegget) — large ducts first, then branches. Never crush ducts to fit.
3. Electrical rough-in (elektriker) — conduit, cable routing, panel position
4. Data, fire alarm, and security rough-in
5. Service cavity installation (if using service cavity for cables + extra insulation)

**Coordination note**: Coordinate large ducts and other services against the verified multidisciplinary design, structural constraints, access and fire requirements. Resolve clashes with the responsible designers before installation; no trade has automatic right-of-way and a clash alone does not establish its cause.

### Phase 5 — Interior Linings
1. Interior airtightness and service cavity boards
2. Vapour retarder (PE-folie) final seal around all penetrations
3. Gypsum board (gipsplater) — ceilings first, then walls
4. Taping and jointing (sparkeling) — two coats minimum for painted finish, three for high-sheen
5. Screed or self-levelling compound on floors (if concrete)
6. Timber flooring sub-base or moisture barrier: verify substrate moisture using the specified measurement method and exact flooring/adhesive limits before release

### Phase 6 — Interior Fit-Out
1. Doors (interior, pre-hung) and door hardware
2. Stairs (trapper) — particularly if prefabricated, coordinate delivery access
3. Joinery and built-ins (kjøkken, garderober, baderomsmøbler)
4. Wall tiles and bathroom waterproofing — tanking layer before tiles
5. Flooring finishes — timber, LVT, tile
6. Painting — walls and ceilings, minimum two coats

### Phase 7 — Mechanical and Electrical Completion
1. Fixtures: light fittings, switches, outlets, sanitary fixtures
2. Heating system commissioning: underfloor heating (gulvvarme) pressure test and filling, radiators
3. Ventilation commissioning: balancing air flows, commissioning TAB report (Teknisk kontroll av balansert ventilasjon)
4. Electrical commissioning and inspection (samsvarserklæring from elektriker)
5. Final plumbing inspection

### Phase 8 — Completion and Handover
- [ ] Snag list (mangelsliste) compiled with client
- [ ] All trade documentation assembled: CE markings, test reports, commissioning reports
- [ ] Assemble source-linked FDV documentation (Forvaltning, Drift, og Vedlikehold) using the register below; verify applicable delivery requirements
- [ ] Verify the actual municipal occupancy basis and conditions, including ferdigattest or any applicable midlertidig brukstillatelse. An application or assembled FDV package is not permission to occupy
- [ ] Clean site and reinstate ground. Remove temporary works only under the verified removal sequence and recorded release, not merely because handover is scheduled

---

## Demolition — Sequencing and Safety

### Pre-Demolition Requirements
Before a sledgehammer swings:
1. **Kartlegging av farlig avfall** (hazardous waste assessment): Establish material risks, survey scope, and applicable duties with competent specialists and current guidance before disturbance. Potential hazards include:
   - Asbestos (asbest): common in Norwegian buildings 1940–1985 (insulation, floor tiles, siding, pipe lagging, sealing compounds)
   - Lead paint (blymaling): common pre-1975
   - PCBs: in older sealed glazing units and some electrical equipment
   - Mercury: in older thermostats and fluorescent lights
   - Creosote-treated wood in older structures
2. **Asbestos assessment**: Hold disturbance of suspect asbestos-containing materials (ACM). A competent specialist must establish safe sampling/analysis and removal arrangements, verifying contractor authorization and applicable requirements with Arbeidstilsynet.
3. **Service isolation**: Confirm gas, electricity, water, and sewer are isolated and capped. Get written confirmation from each utility.
4. **Structural assessment**: Identify all load-bearing elements before beginning selective demolition. Map out the load path and sequence removal to avoid progressive collapse.

### Selective Demolition (Selektiv Riving) Sequence
1. Hazardous-material clearance/removal for the affected area by competent specialists before intrusive strip-out
2. Internal fixtures and fittings (non-structural), within the cleared scope
3. Mechanical and electrical strip-out
4. Non-load-bearing internal partitions
5. Internal linings (boards, tiles, flooring) — to expose structure for inspection
6. **STOP**: Inspect exposed structure for condition, unexpected elements, services
7. Load-bearing removals — only after temporary propping is in place and engineer has confirmed sequence
8. Roof covering and secondary structure (if full demolition)
9. Primary structure — engineer-directed sequence only

**Demolition hold**: Never remove a wall on an assumed load classification or improvise propping first and verify later. Establish the load path, verified temporary-works design, installation checks, and authorized sequence before disturbing support.

### Temporary Works (Midlertidig Understøttelse)
Use a verified project-specific temporary-works design from the responsible structural engineer, not generic prop spacing or improvised needles/shores. Record loads, load paths through supporting floors to ground, bearing, bracing, equipment capacity/configuration, installation checks, monitoring, and installation/removal sequence. Hold affected work until the designated competent person records the required checks and release against that design revision. A proposed schedule cannot release supports or authorize loading.

---

## Contractor Coordination — Norwegian Practice

### Entrepriseformer (Contract Models)
| Model | Norwegian Term | Description |
|---|---|---|
| General contractor | Generalentreprise | Typically one main construction contract, with design separately arranged; verify the actual allocation |
| Design-build | Totalentreprise | Typically combines design and construction responsibility; verify scope and exclusions |
| Trade packages | Delt entreprise | Client holds separate contracts with each trade; more control, more management burden |
| Construction management | Byggherrens byggeledelse | Owner hires a construction manager (byggeleder) to coordinate separate trade contracts |

Choose the model against actual design responsibility, interfaces, client capability, and contract terms; labels alone establish neither accountability nor value.

### Contract Basis and Applicability
Determine the parties (including consumer/professional status), work type (such as new dwelling versus work on an existing property), scope, and design responsibility first. Establish whether **bustadoppføringslova** or **håndverkertjenesteloven** applies, and which contract/NS standard, if any, was actually agreed. Do not prescribe NS 8405, NS 8415, or NS 8407 for every Norwegian contract or assume an agreed standard overrides mandatory consumer protections.

Verify exact clauses, edition, amendments, document precedence, and applicable law using the supplied executed documents, authorized Standard Norge material, current Lovdata text, relevant official guidance, and qualified Norwegian counsel where interpretation is needed. Record source and verification date. Unavailable clauses or unresolved applicability mean **not assessed**, not a reconstructed rule from memory.

For variations, extensions of time, notices, defects, and liability, verify the specific entitlement, procedure, recipient, timing trigger, and consequence. Do not assert universal two-month/five-year limits, that verbal instructions can never bind, or that silence automatically accepts a claim. Preserve oral-instruction evidence and seek written clarification promptly without deciding its legal effect. Flag potentially time-sensitive issues for immediate competent review rather than inventing a deadline or waiting for the whole review to finish.

## Contract Departures Review

1. Inventory the supplied contract package and revisions, including special conditions, scope, commercial schedules, amendments, and acceptance evidence. Resolve the contract basis above before legal conclusions.
2. Obtain the **client-accepted comparison baseline**, its revision, and evidence of who accepted it and when. A prior register, article example, tender draft, or AI suggestion is not an accepted baseline. If it or the relevant clause is missing, record **not assessed** and request the evidence.
3. Compare source wording to that baseline, distinguishing observed differences from proposed commercial/legal consequences. Do not assume the client's preferred position is legally permissible. Record each item:

| Field | Required evidence or state |
|---|---|
| Departure ID / topic | Scope and issue, including conflicting or missing documents |
| Source clause / revision | Document, clause/page, exact relevant wording, edition/revision, amendment and precedence evidence |
| Client-accepted baseline | Position, source/revision, accepting person/date and acceptance evidence; missing → **not assessed** |
| Assessment / consequence | Difference and source-supported possible scope, cost, time, or risk effect; uncertainty explicit |
| Proposed response | Clarification, negotiation wording, or referral; never an issued notice or acceptance |
| Decision owner / review | Named authorized decision owner, legal/commercial reviewer, review status, decision and evidence/date; unknown owners remain open |

4. Return the departures register with evidence gaps and review actions. Acceptance requires a separate authorized decision; Bob's comparison is **not legal approval**. Do not import the article's illustrative LD cap (including 10%), liability exclusions, warranty terms, or other commercial defaults.

### Tilsyn (Site Supervision)
Verify quality-control, inspection, and acceptance responsibilities from the project's role allocation and applicable requirements. Client/representative visits supplement rather than replace required checks. Document:
- Progress against programme
- Quality of work at key hold points (foundations, framing, airtightness)
- Open issues / snagging as work progresses (not all at the end)

---

## Package-Based Schedule (Optional)

Use when a draft schedule or lookahead is requested. Start from supplied scope/packages, method, milestones, supplier commitments, and the identified accepted schedule revision, if one exists. Do not require a package register where none is needed; map activities to supplied scope instead.

| Record per activity | Required content |
|---|---|
| Activity / package / owner | Stable activity ID, package or scope reference, location and responsible trade |
| Predecessor / logic | Predecessor ID, dependency type and any lag, each with evidence or explicitly proposed assumption |
| Duration / calendar | Working duration, calendar, availability/productivity or supplier evidence, and unresolved assumptions |
| Constraints / holds | Access, permits, design readiness, procurement, resources, inspections, moisture/strength requirements; source and release owner/evidence |
| Proposed vs baseline | Proposed dates separately from accepted baseline dates, revision and acceptance evidence; no accepted baseline → comparison **not assessed** |

Have the planner and affected trades review logic, calendars, durations, and constraints before any baseline decision. Preserve the old baseline and record authorized changes rather than silently replacing it. Report gaps instead of manufacturing a critical path; only label one as calculated with a complete validated dependency/calendar/duration model and traceable calculation. Lead-time ranges below are preliminary context, not supplier commitments. No generic curing time, age, planned date, or reported completion releases a technical hold.

## Site Progress Reporting

Set a reporting cutoff and identify the accepted baseline revision before comparing planned and actual work. If absent, actual observations can still be recorded, but baseline variance is **not assessed**. Keep later updates separate from evidence available at the cutoff.

- **Record per activity/package/location:** planned start/finish and quantity at cutoff with baseline source; actual start/finish or ongoing state with dated measurement, units, method, reporter, and source (site log, photo reference, measurement sheet, inspection record).
- **Separate evidence states:** observed, contractor-reported, measured, inspected, and accepted are different. Preserve conflicts and unknowns. A photo or reported finish does not prove concealed quality, inspection acceptance, or hold release.
- **Track blockers and inspections:** constraint/RFI/delivery issue, affected activity, evidence/date, inspection result or pending status, release/acceptance evidence, action owner, and next action. Do not treat an undocumented inspection as passed.
- **Compare only like-for-like measures:** document the measured quantity and baseline denominator/method for any calculated percentage. Do not infer percentages from photos, narrative, elapsed time, or unsupported claims. Keep claimed progress explicitly attributed and unverified.
- **Output:** concise actual-versus-planned report, evidence gaps, blockers, and proposed actions. Reported progress is **not accepted work or payment certification** and establishes neither entitlement nor an extension of time.

## FDV Handover Records

Build a draft evidence index for the installed assets, not a generic collection of product brochures. Verify the applicable project/contract delivery requirements separately.

| Record per installed item | Required content |
|---|---|
| Item / location / product | Asset ID, actual room/system/location, manufacturer, exact model/variant and serial where applicable, installation evidence and supplier/installer |
| Manual / warranty | Exact matching manual title/revision/link and supplied warranty document, issuer, terms and start evidence; distinguish warranty from statutory defect rights |
| Commissioning / as-built | Test/commissioning result, date, responsible party and source; matching as-built drawing revision and unresolved deviations |
| Maintenance | Source document/page for each task, interval and condition; applicability to installed model/configuration verified |
| Missing documents / owner | Missing, mismatched, superseded or unverified evidence; named collection/action owner, requested follow-up date and review status |

Do not invent warranty periods, maintenance intervals, commissioning results, or installed-product matches. Keep unknowns explicit and request exact supplier/manufacturer evidence. Issue only a draft index with open-document actions until the designated reviewer verifies scope and delivery. Document completeness is not technical acceptance, contractual handover, a ferdigattest, or permission to occupy.

---

## Material Lead Times — Norwegian Market Context

Illustrative, unverified planning ranges only. Obtain dated supplier quotations for the exact product, quantity, delivery location and constraints before scheduling a commitment:

| Item | Lead time |
|---|---|
| Timber frame components (standard) | 2–4 weeks |
| Glulam (custom section) | 4–8 weeks |
| Windows (standard, e.g., NorDan, Rationel) | 6–10 weeks |
| Bespoke timber windows (historic profile) | 12–20 weeks |
| Mechanical ventilation units (e.g., Swegon, Systemair) | 4–8 weeks |
| Structural steel (standard profiles) | 2–3 weeks |
| Prefab concrete elements | 6–12 weeks |
| Electrical switchgear (high-spec) | 8–16 weeks |

**Check window procurement early.** Confirm design readiness and supplier dates; do not infer a critical-path delay or authorize ordering from this table.

---

## Common On-Site Problems and Solutions

### Problem: Floors are bouncy / deflecting noticeably
- Record onset, location, loading and visible distress; obtain actual span,
  supports, member/material and condition evidence. Vibration/deflection can have
  several causes. Seek structural review before modifying supports or adding load;
  no generic sister-joist, post or load-test solution is authorized here.

### Problem: Condensation on windows / mould at window reveals
- Investigate indoor humidity/ventilation, surface temperature, air leakage,
  rain entry and the actual junction. Do not diagnose one cause from appearance.
  Review compatible sealing/insulation and drying measures against source evidence.

### Problem: Cold floors over crawlspace or unheated basement
- Establish existing layers, moisture, ventilation and supports before selecting
   insulation or membranes. Do not trap ground/crawlspace moisture with a generic retrofit.

### Problem: The roof is leaking but we can't find where
- Water can travel from its entry point. Inspect relevant penetrations, junctions,
  covering, drainage and condensation sources using safe access and competent
  assessment. Do not exclude the main roof field or prescribe risky access/testing.

### Problem: The contractor says it will cost more than the VO
- Request the scope, price/time breakdown, instruction history, and supporting records. Verify the applicable contract/law, exact variation and notice clauses, and instruction authority through the [Contract Departures Review](#contract-departures-review) before proposing a response. Preserve disputed positions and escalate time-sensitive notices; do not assume a universal NS quotation rule or authority to compel disputed work. Do not issue an instruction, reject a claim, or certify payment on Bob's assessment alone.

---

## Site Safety — Norwegian Requirements

- **HMS / SHA:** Distinguish contractor HMS systems from project SHA arrangements. Determine applicability, client status (including consumer status), work risks, role duties, coordination and plan requirements through current Arbeidstilsynet guidance and competent safety review. Contractor count alone is not a universal legal test.
- **Coordinator:** Verify whether appointment is required, who has that duty, competence, authority and conflicts of interest. Do not default to the main contractor's site manager.
- **Scaffolding:** Require a competent assessment of configuration, assembly, inspection, user instruction and documented release under applicable requirements before use; do not invent a universal contractor certification rule.
- **Fall protection:** Assess fall risk and suitable preventive measures for the actual work and access. Do not treat a generic height threshold as permission to work unprotected below it.
- **Waste:** Verify survey, segregation, handling and documentation requirements for the actual work/materials with competent specialists and current official guidance. Record arrangements and unresolved risks rather than declaring all-site compliance.

---

## Interaction with Other Skills
- **TEK17**: Verify applicable permit/exemption, commencement, FDV and occupancy requirements and actual municipal decisions. A schedule or document checklist does not establish compliance or release.
- **Structural Engineering**: Use the verified design revision and engineer-defined hold criteria. Obtain temporary-works and removal/loading release evidence; a generic sequence or schedule cannot substitute for engineering verification.
- **SINTEF Byggforsk**: Verify the applicable detail, edition, and project specification before using it for execution or hold criteria; a generic reference is not project approval.
- **Historic Preservation**: Heritage site work requires slower pace, documentation before covering, and specialist trades. Build in extra programme and budget contingency.
- **Classical Architecture**: Good execution serves Venustas. A perfectly proportioned facade ruined by sloppy joint lines and uneven paint is a failure. Craft matters.

---

## Sources and Limits

- **Workflow inspiration only:** [10 Plug-and-Play Claude Skills for Construction Professionals](https://aiconstructionnews.com/blog/ai-trends/ccc), AI Construction News, May 20, 2026. Public article read; no paid skill files accessed. The workflows above are original instructions, not copied commercial templates or Norwegian legal authority.
- **Verify for each use:** executed contract and amendments; [Standard Norge](https://standard.no/) authorized standard text; [Lovdata](https://lovdata.no/) current applicable law; [Forbrukerrådet](https://www.forbrukerradet.no/) consumer guidance; [Arbeidstilsynet](https://www.arbeidstilsynet.no/) safety guidance; [DiBK](https://www.dibk.no/) building requirements. Record exact source, edition/date, applicability, and reviewer rather than treating this list as verification.
- **Review scope:** focused workflow and adjacent claim corrections, not a full engineering or legal audit. Remaining construction examples require project-specific verification before execution; no runtime behavior validation is implied.

*Last reviewed: 2026-09-11 (construction-detail workflow added; prior technical examples not revalidated)*
