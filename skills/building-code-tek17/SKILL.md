---
name: building-code-tek17
description: Source-check Norwegian TEK17/PBL/SAK10 applicability, room/energy/escape requirements, permit routes and responsibility; distinguish regulation, guidance, project evidence and approval.
triggers: [TEK17, PBL, SAK10, permit, søknad, energy, fire, escape, room height, daylight, accessibility, setback, zoning, radon, stormwater, responsibility]
load_with: []
safety_level: high
status: draft
license: Proprietary
---

# Skill: Building Code TEK17

## Purpose

Determine the applicable Norwegian requirement and compare it with scoped evidence.
This is a source-verification workflow, not a complete code database. Use the
[checked requirement register](references/verified-requirements.md) for the limited
room, energy and escape comparisons reviewed on 2026-09-11. No source access means
the affected requirement stays **unverified**; do not reconstruct exact clauses.

## Trust Boundary

BTBA may identify relevant sources, explain distinctions and draft a requirements
comparison. Compliance conclusions based on unverified geometry, use or conditions
remain preliminary. Missing documentation means **UNKNOWN / evidence required**,
not automatically illegal. A permit/responsibility exemption never establishes
structural or geotechnical safety. No generic PE credential or wet stamp is
universally required by Norwegian law.

For setbacks, apply the [boundary evidence gate](../architectural-drawing-reading/SKILL.md#step-3-establish-scale-and-dimensions):
distinguish drawing-dimensioned/scaled, cadastral, site-measured and survey-confirmed
evidence. A drawing or tape measurement to an unconfirmed boundary is not survey
confirmation. Label drawing-derived concerns **PRELIMINARY RED FLAGS — requires
survey verification**; do not assert a violation without reliable geometry and
verification of the applicable rule/decision.

BTBA drafts, not approves or submits. Determine the applicable Norwegian responsible
roles and actual decisions. Apply the [official correspondence gate](../soknad-package/SKILL.md#official-correspondence-gate-l005l006)
before release. A source-linked assessment, supplied permit or filled checklist is
not authority to commence work outside its actual scope and conditions.

## Source and Applicability Procedure

1. Identify the actual measure, existing/new conditions, room/building use, relevant
   application dates, local plan and permit conditions. Do not apply every
   new-building provision to every existing-building intervention.
2. Read the current Norwegian provision and relevant guidance. Record URL, paragraph,
   retrieval date, edition and transition provisions. Translations, consultations,
   press announcements and vendor summaries are not enacted law.
3. Separate statutory requirements, preaccepted guidance, alternative documented
   solutions, standards/NA editions and contractual preferences. A client target is
   not a legal minimum; a minimum level alone is not a complete compliance pathway.
4. Compare like-for-like quantities with units, datums and evidence. Distinguish
   proposed, reported, measured, derived, reviewed and approved states. Missing
   information produces an unassessed comparison, not a breach or a passing result.
5. Return criterion/source/scope, project evidence, result/uncertainty, appropriate
   reviewer and next verification. Ask only questions material to that decision.
6. On revised evidence, use [project-lifecycle](../project-lifecycle/SKILL.md) to flag
   affected outputs pending revalidation. Preserve prior source and issue records.

## Topic Routes and Known Limits

| Topic | What to establish before a consequential conclusion |
|---|---|
| Rooms, height, access and stairs | Function, new/existing-building route, actual geometry, measurement convention and applicable provision; no fixed 7 m² minimum room area or universal 2.20 m height |
| Energy | Applicable §14-1/§14-5 scope; §14-2 pathway and §14-3 minimum levels separately; actual assembly/product calculations, not nominal thickness |
| Escape/fire | Risikoklasse and brannklasse separately; coordinated fire strategy, clear openings, operation, access and rescue arrangements; no universal escape window in every bedroom or default well size |
| Daylight/ventilation | Actual room, glazing/transmission, external obstruction/well geometry, ventilation system and applicable method; no generic window-area percentage pass |
| Structure | Applicable §10-2 documentation route, actual loads/supports and standards/NA; [structural-engineering](../structural-engineering/SKILL.md) only when implicated |
| Ground/flood/landslide | Hazard type, applicable safety class, NVE/NGU evidence and site conditions; structural reliability classes are not flood/landslide classes; no universal return period or map-based site clearance |
| Boundaries, heights, BRA/BYA and roads | Applicable PBL/local-plan/road rule, actual measurement definitions, boundary evidence and decisions; not every paved area is automatically BYA |
| Moisture and below-ground water | Current Chapter 13, product/design evidence, terrain, groundwater and drying/drainage strategy; see [building physics](../sintef-byggforsk/SKILL.md) |
| Stormwater/drainage | [Current §15-8](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17/15/iii/15-8), municipal conditions, catchment, infiltration evidence, outlet capacity, backwater and overflow; no generic 10-year event or climate-factor default |
| Climate, waste and reuse | Current Chapters 9/17, actual measure/category and calculation/report scope; earlier universal 500 m² thresholds, chapter summaries and survey obligations are withdrawn |
| Heritage | Actual protection decision/local plan and affected works, not SEFRAK alone; [heritage skill](../historic-preservation/SKILL.md) subject to shared constraints |
| Electrical/water/HVAC | Actual system and qualified trade/designer scope; no generic licensing, insulation, airflow or insurance conclusion from the old skill tables |

Unverified legacy numerical examples in companion skills/templates cannot override
this source procedure. Load only relevant domains through routing, not recursively
through companion hints.

## Permit and Responsibility Review

Determine scope under current PBL/SAK10 and local plans rather than applying a
memorized shed/extension threshold. Separate:

- whether a measure is covered by application requirements;
- whether a specific exemption applies with all conditions satisfied;
- whether tiltakshaver can apply or responsible enterprises are required;
- neighbour notification, dispensation and technical-documentation duties;
- commencement, inspection/control and occupancy/completion conditions.

A permit exemption is not a technical exemption. An appointment enquiry or preliminary
pricing request can disclose unresolved design issues; it does not release fixed-price
scope, procurement or construction. Do not invent processing deadlines or declare
work unauthorized because its permit is absent from the reviewed folder.

Use current evidence for ansvarlig søker, prosjekterende, utførende and kontrollerende
where applicable. Sentral godkjenning is not a universal professional license.
Identify actual accepted responsibility; do not assign a named person by inference.
Occupancy can depend on the actual ferdigattest or applicable midlertidig
brukstillatelse and its conditions, not merely an assembled completion package.

## DOK and Municipal Evidence

DOK is a source of relevant spatial evidence, not a universal automatic approval
service. Verify dataset identity, date, resolution, coverage, CRS and limitations;
use the municipality's actual requirements for the measure. Do not infer terrain,
legal boundaries or absence of hazards from an empty query. No connector is assumed
installed. Do not load private properties merely because an address occurs in text.

## Output Contract

| Field | Required content |
|---|---|
| Requirement | Exact source/paragraph/version; law, guidance, standard or project criterion |
| Applicability | Building/room/measure scope and evidence, or unverified |
| Evidence | Source/page/revision, units/datum, actual versus proposed state |
| Comparison | Met / discrepancy / unassessed for that criterion only; explain uncertainty |
| Next action | Needed source/measurement, appropriate reviewer and unresolved dependency |
| Release | AI advisory draft; actual review/issue/authority decisions recorded separately |

## Synthetic Cases

- **Small room:** a fictional drawing shows a room below 7 m². Expected: evaluate
  function, furniture, access and applicable requirements; no fixed-area breach.
- **Energy minimum:** fictional product meets the applicable §14-3 value. Expected:
  report that limited comparison; §14-2 pathway remains separately assessed.
- **Escape window:** only nominal frame dimensions supplied. Expected: clear opening,
  sash operation, access and relevant fire strategy remain unresolved; no well-size pass.
- **Missing permit:** no permit in the supplied material. Expected: request the actual
  decision/exemption basis; do not infer illegality or structural safety.

## Review Status

The prior blanket amendment/currency, institutional-merger, default room/energy,
fire-class, permit, DOK and climate claims were withdrawn on 2026-09-11. Limited
source comparisons are in the linked register; this is not a full legal review.
Synthetic expectations require separate behavioral evaluation; a source check is
not a model-behavior test or professional certification.
