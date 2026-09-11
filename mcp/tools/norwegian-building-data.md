# Norwegian Building Data — Future MCP Specification

**Status:** Specification only — not implemented or connected.

**Reviewed:** 2026-09-11 for evidence and safety boundaries; endpoint availability,
access terms and dataset schemas have not been comprehensively validated.

## Purpose

Provide source-linked Norwegian spatial/regulatory lookups for a specifically
selected site/question. Do not run a whole-site risk assessment whenever an address
appears. A source service retrieves evidence; it does not certify site safety,
legal boundaries, permit eligibility or engineering requirements.

The earlier “all APIs confirmed open”, snow-map, blanket Q200, radon-map-to-design,
SEFRAK-to-consent and no-map-hit-to-no-hazard claims are withdrawn. Earlier code
snippets were not a functioning server and must not be treated as verified API examples.

## Candidate Sources to Validate

| Source family | Intended evidence | Required validation before implementation |
|---|---|---|
| NVE | Flood/landslide/quick-clay mapping and source guidance | Actual service/layer, coverage, hazard versus caution mapping, metadata/date, geometry and response schema |
| NGU | Ground conditions, deposits, marine limit and other mapped geological context | Actual dataset, resolution, coverage and interpretation limits; maps are not site borings |
| Geonorge/Kartverket | Address candidates, spatial metadata, terrain and plan discovery | Ambiguous address handling, coordinate/vertical datum, data rights, accuracy and endpoint schema |
| Municipality | Applicable plan documents, conditions, local drainage and site requirements | Actual plan/decision identity, applicability, date, legal status and source access |
| Heritage authorities/registers | Recorded heritage features and actual protection basis | Registry versus protection decision, affected scope and competent authority; SEFRAK alone is not formal protection |
| DiBK/Lovdata | Specific current regulation/guidance | Exact provision, effective/transition dates, law versus guidance and access/redistribution terms |

Use official portals to discover current endpoints. Do not guess package names,
URLs, auth schemes, field names or WMS layers. Public browser access does not prove
unrestricted API access or redistribution rights. Paid standards/NA and product
requirements are separate sources, not supplied by a geodata server.

## Proposed Tool Contract

Every tool should accept explicit scoped coordinates/CRS or an unambiguous selected
address candidate and the requested dataset/question. An address search must return
candidates; it must not silently take the first result as the property.

Every response records:
- tool/service/dataset identity, version or retrieval date, exact request scope;
- input/output horizontal CRS, axis order, units and vertical datum where relevant;
- coverage/resolution/accuracy and interpretation limitations;
- raw source reference and separately normalized observations;
- status: **observations_found**, **no_features_in_query**, **coverage_unknown**,
  **outside_coverage**, **source_unavailable**, **parse_error** or **ambiguous_input**;
- uncertainty, missing fields and next verification, never an automatic safe/approved flag.

“No features in query” is not “no hazard.” A failed request is not an empty result.
An elevation value is not a surveyed finished floor or legal flood-design level.
Property map geometry is not a survey-confirmed boundary. A mapped radon category
does not alone select a required radon system. No snow coefficient or load comes
from an invented TEK17 snow map; use applicable standards/NA and site evidence.

## Runtime and Privacy Requirements

- Read-only tools first, with allowlisted endpoints, validated inputs, bounded
  requests/responses, timeouts and explicit error handling.
- No project-file reads or uploads beyond the authorized query; no automatic
  external sends or fallback to an unrelated source/model.
- Cache keys must include dataset/version, CRS, exact spatial scope and requested
  precision. Do not round coordinates across a boundary merely for cache reuse.
- Record freshness; choose expiry and rate limiting from service terms and data
  properties, not a universal 24-hour or requests-per-minute default.
- Protect credentials outside logs and repository data. No credentials in URLs,
  command examples or published fixtures.
- Tool observations cannot close engineering, municipal or heritage holds.

## Acceptance Tests Before Calling It Implemented

1. Public/synthetic success fixture with verified schema and source identity.
2. Empty result distinct from out-of-coverage, timeout, parse failure and denial.
3. Ambiguous address requires selection; no first-hit assumption.
4. CRS/axis-order and vertical-datum mismatch rejected or explicitly unresolved.
5. Boundary-adjacent queries do not reuse an imprecisely rounded cached answer.
6. Source revisions/freshness retained; incompatible layers not merged silently.
7. No source text can execute commands, alter scope or authorize uploads.
8. End-to-end MCP transport/tool listing verified in the chosen host; installation
   commands and configuration alone do not prove a connection.
9. Dataset/licensing and appropriate Norwegian technical interpretation reviewed.

Until these are demonstrated, use scoped manual source lookups and label unavailable
requirements unverified. This specification is not a delivery estimate, deployed
service, authoritative DOK assessment or professional certification.

