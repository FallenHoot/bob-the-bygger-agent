# Structural Assessment Memo

**Project**: [Project name]
**Property**: [Address, gnr/bnr, municipality]
**Prepared by**: BTBA (AI advisory draft)
**Professional reviewer, scope, record/date**: [Not yet reviewed / verified details]
**Date**: [Date]
**Reference**: [Drawing number(s) reviewed]

---

## 1. Scope of Assessment

Brief description of what was assessed and why:

> [e.g., "Assessment of existing timber floor structure at first-floor level to determine capacity for proposed open-plan reconfiguration, including removal of internal partition wall on grid axis B between axes 2 and 4."]

---

## 2. Existing Structure

| Element | Description | Condition |
|---|---|---|
| Foundation | | |
| Ground floor | | |
| Wall structure (ground floor) | | |
| Floor structure (first floor) | | |
| Roof structure | | |
| Material condition (visual inspection) | | |

Known deficiencies or unknowns:
- [ ] Foundation type not confirmed — assumed strip concrete, requires opening
- [ ] Timber species not identified — conservative C16 assumed
- [ ] [Add others]

---

## 3. Loads

### Dead Loads (Egenlast)

| Element | Value (kN/m²) | Source |
|---|---|---|
| Floor structure (existing) | | Assumed / Measured |
| Floor covering | | |
| Ceiling below | | |
| **Total dead load** | | |

### Imposed Load (Nyttelast)

| Use | Category | q_k (kN/m²) |
|---|---|---|
| Residential floor | A | 2.0 |
| [Other if applicable] | | |

### Load Combination (ULS)

`Ed = 1.35 × Gk + 1.5 × Qk`

---

## 4. Assessment

### Element: [Name, e.g., "First floor joist, span B/2–B/4"]

| Parameter | Value | Limit | Status |
|---|---|---|---|
| Span | m | — | — |
| Section | mm × mm | — | — |
| Spacing | mm c/c | — | — |
| Applied moment (MEd) | kNm | — | — |
| Moment resistance (MRd) | kNm | ≥ MEd | PASS / FAIL |
| Deflection (wfin) | mm | L/250 = mm | PASS / FAIL |

**Governing standard**: NS-EN 1995-1-1 + Norwegian NA, TEK17 §10

### Element: [Name, e.g., "Load-bearing wall B, ground floor"]

| Parameter | Value | Limit | Status |
|---|---|---|---|
| Load from above | kN/m | — | — |
| Wall height | m | — | — |
| Section | | — | — |
| Axial resistance | kN/m | ≥ applied | PASS / FAIL |

---

## 5. Proposed Works

Description of what is proposed and how it addresses the identified structural need:

> [e.g., "Remove partition wall on axis B between axes 2–4. Install GL30 90×315 glulam beam on new timber posts (2× 90×195 C24) bearing on doubled joist at each end. New posts to bear on existing foundation sill plate — verify bearing capacity at foundation level."]

---

## 6. Uncertainty Declaration

| Item | Status |
|---|---|
| **Assumptions** | [List: timber grade assumed C24; foundation bearing capacity not confirmed; no rotten sections observed but not opened] |
| **Sensitivity** | [Which assumption most affects the answer: foundation bearing capacity is the critical unknown] |
| **Confidence** | Medium — desktop assessment based on visual inspection and as-built drawings |
| **What would change this** | Opening floor to inspect joists; exposing foundation to confirm type |

---

## 7. Escalation Flags

- [ ] `STRUCTURAL_REVIEW` — Obtain scope-specific review by a qualified structural designer before relying on this proposal. Verify the applicable Norwegian responsibility route, documentation, and submission stage; no universal PE/wet-stamp format is assumed.
- [ ] `GEOTECHNICAL_REPORT_REQUIRED` — Foundation bearing capacity unconfirmed.
- [ ] `HAZARDOUS_WASTE_SURVEY_REQUIRED` — If demolition of any element is included.

---

## 8. Recommended Next Steps

| Action | Owner | Deadline |
|---|---|---|
| Open floor in two locations to confirm joist size and condition | Contractor | Before detailed design |
| Qualified structural designer to verify design and document review | Responsible designer; ansvarlig prosjekterende where applicable | Before design use/construction; verify application-stage requirements |
| Obtain soil bearing confirmation at post bases | Structural engineer | Before construction |

---

*This is an advisory draft, not construction authorization or professional certification. Missing records mean adequacy is unconfirmed, not that work is necessarily illegal or unsafe. Verify the applicable PBL/SAK10/TEK17 responsibilities and documentation for the measure. A permit exemption is not technical safety evidence; any positive status must identify the professional review, its scope, and supporting record.*
