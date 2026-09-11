---
name: soknad-package
description: SAK10 søknad completeness — exactly which drawings/forms/documents each project type needs. Load for permit-application prep questions.
license: Proprietary
triggers: [søknad, byggesøknad, permit, application, what do I need, what documents, drawings required, SAK10, nabovarsel, situasjonsplan, BRA calculation, søknadspliktig, tilbygg, fasadeendring, bruksendring, riving, nybygg, forhåndskonferanse, dispensasjon, igangsettingstillatelse, ferdigattest, eByggesøk, ansvarlig søker, ansvarsrett, tiltakshaver]
load_with: [building-code-tek17]
safety_level: high
---

# Skill: Søknad Package Completeness (SAK10)

## Trust Boundary

**Bob may, on his own analysis:** walk through the SAK10 completeness checklist for a given measure type and identify which documents are typically required.

**Bob may flag only as preliminary:** BRA/BYA calculations or setback figures based on unverified geometry. Apply the [boundary evidence gate](../architectural-drawing-reading/SKILL.md#step-3-establish-scale-and-dimensions); readable drawings and cadastral lines are not automatically surveyed legal boundaries.

**Submission boundary:** Bob prepares drafts and checks evidence, not grants permission or submits. Verify whether ansvarlig søker/ansvarlige foretak are required or tiltakshaver may apply directly. Obtain the authorized sender's approval and appropriate technical/planning/legal review for consequential unresolved claims; do not impose a universal PE, wet stamp, or lawyer requirement. Missing documents mean unresolved evidence/completeness, not automatically illegal work.

## Official Correspondence Gate (L005/L006)

For letters, emails, objections, and submissions to municipalities, heritage bodies, courts, or other official recipients:

> **DRAFT FOR REVIEW — AI-assisted advisory draft, not submitted or approved. Verify factual and legal claims and obtain the appropriate professional review and sender authorization before sending.**

End each draft with this pre-send checklist; unresolved consequential claims stay on hold or are rewritten as explicit requests for verification:
- [ ] **Exact supporting documents:** Each claim cites the actual record inspected, title/file, date/revision, section, and scope. Do not infer permit, technical approval, or legal breach from a summary or absent file.
- [ ] **Attachment manifest:** Exact filenames/titles, revisions/dates, purpose, and draft/reviewed/decision status match the intended attachments; missing or superseded items are flagged.
- [ ] **Dispatch status:** Draft, approved for issue, sent, and receipt confirmed are separate states. Sent/issued requires dispatch evidence for recipients, date, and exact document set; receipt requires separate evidence. Otherwise state **dispatch unverified**.
- [ ] **Deadline and currency:** Verify the response/submission deadline and its triggering event against current rules or the actual notice, with absolute date and time/time zone where relevant. Check legal-source effective date and document currency; do not reuse an expired deadline or outdated rule as current.
- [ ] **Boundary and factual claims:** Retain source/method/accuracy labels. For drawing-derived distances include: "These distances are preliminary estimates from drawing review, not survey-confirmed boundary distances." Request competent survey/authority clarification; do not send a confirmed-violation allegation until the boundary, relevant geometry, and legal basis are verified.
- [ ] **Scope and money:** State exactly which work/decision is covered and any exclusions. If costs appear, verify monetary currency, estimate/quote date/validity, VAT inclusion/exclusion and rate/basis, and consistent net/gross totals. Mark not applicable if no monetary claim.
- [ ] **Review and release:** Name the reviewer and scope where professional review is needed; verify legal references and facts, and obtain explicit authorized-sender approval. Completion of this checklist does not itself send anything or establish authority approval.

---

## Legal Basis

**SAK10** (Byggesaksforskriften — FOR 2010-03-26 nr. 488) is the procedural regulation under PBL. Check its current text, the measure, application stage, and municipal requests to establish required documentation. A missing item may require supplementation; it is not automatically rejection or proof of unlawful work. Distinguish design records retained in the project from attachments required for the application.

**eByggesøk** (DiBK's online søknad portal) automates many of these checks but does not replace knowledge of what is required — the portal will ask you to upload things you haven't prepared.

---

## Step 1: Is a Søknad Required?

### Exempt Measures (Søknadsfritt — PBL §20-5 / SAK10 §4)

The following do not require a søknad (as of 2026, including SAK10 amendments effective 01.07.2026):

| Measure | Maximum size | Conditions |
|---|---|---|
| **Frittliggende byggverk** (shed, garage, outbuilding) | ≤ 15 m² BYA | ≤ 1 floor; not for dwelling; ≥ 1.0 m from property line |
| **Tilbygg** (addition to existing house) | ≤ 15 m² BRA | ≤ 1 floor; not habitable; ≥ 1.0 m from property line |
| **Terrasse** | — | Attached to dwelling; not elevated > 0.5 m above ground without enclosure |
| **Fasadeendring** | — | No change in character; not heritage building |
| **Additional insulation on exterior** | — | NEW (01.07.2026): No søknad required for additional insulation on small residential |
| **Solar panels on roof** | — | NEW (01.07.2026): No søknad required for solar on small residential; must notify municipality |
| **EV charging** | ≤ 50 m² plot coverage | NEW (01.07.2026): No søknad if on regulated site |
| **Internal work** | — | Non-structural, no change of use, no fire safety impact |

**Always check**: Municipal plan (reguleringsplan) can impose stricter requirements. Heritage buildings never get exemptions without Byantikvaren sign-off.

### Søknadspliktig — Requires a Søknad

| Category | Who handles it |
|---|---|
| Tiltak with neighborly impact (nabovarsel required) | Simple application (§20-2 søknad) with ansvarlig søker |
| Tiltak requiring ansvarlige foretak | Requires ansvarlig søker + project team with ansvarsrett |
| Demolition (riving) | Separate rive-søknad — see below |

---

## Step 2: Which Type of Søknad?

### §20-2 — Standard Application (Most Common)

Covers: tilbygg, påbygg, nybygg, fasadeendring with impact, bruksendring, major renovation.

**Who submits**: Establish the applicable route under PBL §§20-2–20-4. For measures requiring responsible enterprises, ansvarlig søker coordinates the submission; this is not a generic personal licensing requirement.

### §20-4 — Measures Without Responsible Enterprises

Covers qualifying measures that tiltakshaver may apply for directly. Verify the current categories and conditions; neighbor notification and documentation may still be required.

### §20-3 — Measures Requiring Responsible Enterprises; Selvbygger Route

Do not treat §20-3 itself as a self-build exemption. If a personal selvbygger responsibility route is proposed, verify SAK10 §6-8 eligibility, scope, competence, and municipal approval. Neither an exemption nor self-build approval confirms structural or ground safety.

---

## Step 3: Required Documents by Project Type

Treat the lists below as prompts to verify against the current rules, measure, application stage, and municipal requests, not a universal attachment or licensing schedule. Identify technical records retained in the project separately from submitted attachments. Assign ansvarlig prosjekterende and review records only under the applicable responsibility route; no generic PE/wet-stamp requirement is implied.

### 3A — Tilbygg / Påbygg (Addition to Existing Building)

**Drawings required (SAK10 §5-4):**
- [ ] **Situasjonsplan** — scale 1:500 or 1:1000. Shows: plot boundaries (from matrikkelkart), existing buildings, proposed addition footprint, setbacks to all boundaries, setback to road. Must include north arrow, scale bar, BYA calculation.
- [ ] **Plantegning** — floor plan of the addition at 1:100 or 1:50. Shows room layout, dimensions, door/window positions, existing building interface. Must show *before* and *after* states or clearly mark new work.
- [ ] **Snitt** (section) — minimum 1 section through the addition showing: floor-to-ceiling heights, floor build-up, foundation depth, roof structure.
- [ ] **Fasadetegning** (elevation) — all affected facades at 1:100. Must show existing building + addition in same drawing. Mark terrain level (existing and proposed).
- [ ] **Konstruksjonstegning** (structural drawing) — for new load paths, beams, or foundations, identify the qualified designer's design/review records and applicable responsibility and submission stage.

**Documents required:**
- [ ] **Søknadsskjema** — standard application form (SAK10 Vedlegg 2 / eByggesøk form)
- [ ] **Nabovarsel** (neighbor notification) — sent to all owners within 60 m of the plot boundary, 2 weeks before søknad submission. Use form 5154 (naboliste) and 5155 (nabovarsel). Submit proof of dispatch + any neighbor feedback (merknader) with søknad.
- [ ] **Ansvarsrett declarations** — for all responsible professionals (ansvarlig søker, prosjekterende, utførende). In eByggesøk these are submitted digitally.
- [ ] **Reguleringsbestemmelser excerpt** — identify the applicable zone and show the proposed measure complies with height, BYA, and use restrictions.
- [ ] **BRA/BYA calculation** — tabular calculation showing existing and proposed floor area; demonstrate compliance with maximum %-BYA.

**If heritage building:**
- [ ] **Antikvarisk vurdering** — heritage assessment if SEFRAK-registered or in heritage zone.
- [ ] **Byantikvaren pre-approval** (if required by heritage zone regulations).

---

### 3B — Fasadeendring (Facade Change)

**When a søknad is required**: Change of cladding material, new window openings, moving windows, changing window proportions (beyond like-for-like replacement), any change affecting the building's "karakter" (character).

**Drawings required:**
- [ ] **Fasadetegning** — all affected facades. Show existing (or use photos) and proposed side by side. Mark all changes clearly.
- [ ] **Situasjonsplan** — confirm building footprint unchanged.
- [ ] **Detailtegning** — new window details, cladding profiles, or cornice details if non-standard.

**Documents required:**
- [ ] Søknadsskjema
- [ ] Nabovarsel (only if neighbours have visual impact — e.g., large roof window facing neighbours)
- [ ] Ansvarsrett declarations
- [ ] Material and color samples / product specifications for new cladding

**Heritage buildings**: Every fasadeendring on a SEFRAK-registered building requires Byantikvaren consultation before søknad. Reversibility and material authenticity are the key criteria.

---

### 3C — Bruksendring (Change of Use)

**Common scenarios**: Attic (loft) to habitable bedroom, basement to habitable space, garage to dwelling, commercial to residential.

**Triggers a full søknad because**:
- The changed space must comply with TEK17 requirements for the new use category (ceiling height, escape window, ventilation, fire safety, accessibility)
- BRA calculation changes (affects %-BYA)
- Potential change in fire class (risikoklasse)

**Drawings required:**
- [ ] **Plantegning** — before and after floor plans of the converted space. Show all new partitions, windows, escape routes.
- [ ] **Snitt** — show actual room height and measurement convention; verify the applicable [§12-7 room/use-change route](../building-code-tek17/references/verified-requirements.md#rooms), not a universal 2.20 m rule.
- [ ] **Fasadetegning** — if new windows or escape windows are added.
- [ ] **Ventilasjon** — schematic showing how the new space is ventilated (fresh air supply, extract).

**Documents required:**
- [ ] Søknadsskjema
- [ ] Nabovarsel (if new windows face neighbours)
- [ ] Ansvarsrett (including ansvarlig prosjekterende for structural if ceiling is lowered or partition relocated)
- [ ] TEK17 compliance statement — demonstrate ceiling height, escape route, ventilation, and fire safety are satisfied
- [ ] New BRA calculation

---

### 3D — Nybygg (New Building)

**The most comprehensive søknad type.** Requires a full set of drawings and the full ansvarssystem.

**Drawings required:**
- [ ] **Situasjonsplan** — 1:500. Plot boundaries, all buildings (existing + new), terrain contours, setbacks, access, BYA calculation.
- [ ] **Plantegning** — every floor, 1:100. Full room layout, dimensions, door/window positions, areas.
- [ ] **Snitt** — minimum 2 cross-sections (longitudinal + transverse), showing floor-to-ceiling heights, floor build-up depths, foundation depth, roof structure.
- [ ] **Fasadetegninger** — all 4 facades (or all visible facades), 1:100. Show terrain line (both existing and finished).
- [ ] **Fundamentplan / grunnmursplan** — foundation plan showing footing positions, basement walls, drainage.
- [ ] **Konstruksjonstegninger** — structural drawings and review records for the primary load-bearing system; identify ansvarlig prosjekterende where applicable and verify which records accompany this submission.
- [ ] **Bjelkeplan / dekkeplan** — floor structure plans showing joist direction, beam positions.

**Documents required:**
- [ ] Søknadsskjema + all sub-forms (SAK10 annexes)
- [ ] Nabovarsel — sent to all neighbours within 60 m, proof of dispatch, 2-week waiting period
- [ ] Ansvarsrett for all roles: søker, prosjekterende (architectural + structural + MEP), utførende
- [ ] SHA-plan (Sikkerhet, Helse, Arbeidsmiljø) — if more than one employer or professional is involved in construction
- [ ] Avfallsplan (waste management plan) — for new construction over 300 m²
- [ ] Geotechnical report if: unknown soil, slope, coastal, quick clay zone
- [ ] Energy calculation (TEK17 §14) — demonstrate compliance with U-value or energy frame
- [ ] Fire strategy statement (brannstrategi) — if BKL2 or higher
- [ ] Reguleringsbestemmelser compliance statement

---

### 3E — Riving (Demolition)

Demolition of buildings that are søknadspliktig (most permanent buildings > 15 m²) requires a **rive-søknad**.

**Drawings required:**
- [ ] **Situasjonsplan** — show which building is being demolished; final state of the plot.
- [ ] **Photos** — document existing building condition (all 4 sides).

**Documents required:**
- [ ] Søknadsskjema (rive-søknad specific)
- [ ] **Kartlegging av farlig avfall** — hazardous waste survey conducted by accredited party. Must identify asbestos, lead paint, PCBs, mercury. Submitted as annex. `HAZARDOUS_WASTE_SURVEY_REQUIRED` is always triggered for demolition.
- [ ] Proof that utility connections are isolated (gas, electricity, water, sewer)
- [ ] Nabovarsel (demolition affects neighbours — vibration, access, dust)
- [ ] Ansvarsrett for demolition contractor (utførende)
- [ ] Avfallsplan — waste destination for all demolition material. Minimum 60% by weight must be sorted and recycled (TEK17 §9-7).

---

## Step 4: The Nabovarsel Process

**Who gets notified**: All property owners (not tenants) within 60 m of the plot boundary. The municipality provides the naboliste (neighbour list) via matrikkel. eByggesøk generates this automatically.

**How to notify**: Send form 5155 (nabovarsel) by registered mail or deliver in person. eByggesøk allows digital notification if neighbours are registered.

**Waiting period**: 14 days from last documented delivery. If no response — proceed. If neighbours object (merknad) — attach their objection to the søknad with your response. The municipality decides.

**What triggers a nabovarsel**: Any søknadspliktig measure. Not required for søknadsfri measures.

---

## Step 5: Forhåndskonferanse (Pre-Application Meeting)

**When to use it**: Before a complex søknad — unusual project, heritage building, dispensasjon from plan, large new building. The municipality's byggesaksavdeling answers questions before you invest in drawings.

**What to bring**:
- Plot address and matrikkel number
- Current state: photos, existing drawings if available
- Rough sketch of proposed project
- Questions about: zoning compliance, heritage status, required drawings, expected processing time
- Information on who the ansvarlig søker will be

**What you get**: A written record (forhåndskonferansereferat) that documents the municipality's preliminary position. Not legally binding but extremely useful for directing design effort.

**Reference**: The template at `templates/pre-application-meeting-notes.md` structures this conversation.

---

## Step 6: Processing and Permits

### Timeline (Normal — no dispensasjon, complete søknad)
| Step | Deadline |
|---|---|
| Municipality confirms receipt | 3 working days |
| Completeness check | No formal deadline, but typically within 1–2 weeks |
| Decision (simple cases — §20-2) | **12 weeks** from complete søknad (SAK10 §7-3) |
| Decision (complex / dispensasjon) | No statutory deadline — can take months |

### After Approval
- **Igangsettingstillatelse (IG)** — separate permit to begin construction; issued after conditions in approval are met (e.g., detailed structural drawings submitted and approved)
- **Ferdigattest** — must be issued before the building can be occupied. Apply after all work is complete and all commissioning documentation is submitted. Municipality has 3 weeks to issue.
- **Midlertidig brukstillatelse** — temporary occupancy permit if some minor items remain outstanding.

---

## Common Rejection Reasons

1. **Missing or incomplete nabovarsel** — wrong neighbours notified; insufficient waiting period documented
2. **Situasjonsplan not from matrikkelkart base** — hand-drawn without accurate boundary data
3. **BYA exceeds allowed %-BYA** — calculation error or missing terrace/parking area
4. **Applicant/responsibility route unresolved** — establish whether responsible enterprises are required, tiltakshaver may apply under §20-4, or an approved selvbygger route applies
5. **Ansvarsrett declarations missing** — digital submission in eByggesøk incomplete
6. **TEK17 compliance not documented** — ceiling height, fire escape, ventilation missing from drawings
7. **Structural documentation/review incomplete** — identify the responsible designer and applicable records; no generic PE/wet-stamp requirement or automatic illegality inference
8. **Hazardous waste survey missing** (for demolition) — automatic rejection

---

## Dispensasjon (Waiver from Plan Requirements)

If the project doesn't comply with the municipal plan (e.g., exceeds %-BYA, wrong setback, wrong use), a dispensasjon must be applied for and granted separately from the søknad.

**Grounds for dispensasjon (PBL §19-2)**:
- The plan's purpose is not substantially undermined
- The benefits outweigh the disadvantages for affected parties and society

**In practice**: Municipalities are selective. For minor exceedances (setback 3.5 m instead of 4.0 m, 1–2% BYA over limit), dispensasjoner are commonly granted. For major deviations from plan intent, they are rarely granted.

**Process**: Apply for dispensasjon in the same søknad or before. The municipality must consult affected agencies (Statsforvalter for heritage, NVE for hazard zones). Processing time: 3–12 months in complex cases.

---

## Escalation Flags for Søknad Context

| Situation | Flag |
|---|---|
| Work with unresolved permit status | `PERMIT_STATUS_REVIEW` — verify scope, exemptions, decisions, and conditions with the municipality/applicant; missing records alone do not prove unlawful work |
| Demolition of any building | `HAZARDOUS_WASTE_SURVEY_REQUIRED` |
| Project in heritage zone or SEFRAK building | `BYANTIKVAREN_CONSULTATION_REQUIRED` |
| Basement excavation / unknown soil | `GEOTECHNICAL_REPORT_REQUIRED` |
| Flood or landslide zone | `NVE_CHECK_REQUIRED` |
| Structural modification | `STRUCTURAL_REVIEW` — scope-specific qualified structural assessment and applicable Norwegian responsibility/documentation route, not a generic wet stamp |

---

*Authority: SAK10 (FOR 2010-03-26 nr. 488 med endringer), PBL (LOV 2008-06-27 nr. 71), TEK17*
*Reference: [dibk.no/byggesok](https://www.dibk.no/byggesok) — DiBK søknadsveiledere*
*eByggesøk: [ebyggesok.no](https://www.ebyggesok.no)*
*Last reviewed: 2026-08-09*
