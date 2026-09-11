# Reliability Hardening — Evidence, Revisions and Evaluation Records

**Date:** 2026-09-11

**Scope:** Follow-up to [the first implementation batch](reliability-implementation-2026-09-11.md).
Local repository work and synthetic tests only. No private project records, external
model runs, publishing or licensing changes.

## Reproduced Problems and Fixes

New tests were run against the prior implementation before fixes. The detail suite
exposed nine assertion failures and two missing-result errors; the drawing suite
also exposed rectangle/rotation/calibration/omission gaps. These are observed tool
defects, not professional assessments or assertions about any real building.

| Problem observed | Implemented correction | Regression evidence |
|---|---|---|
| Reports referenced mutable input objects | Deep-copy returned source/element/hold data | Editing a returned report no longer changes its input package |
| Unknown layer thickness absent from uncertainty summary | Include layer quantities with stable field paths | Unknown layer appears as layers/0/thickness, not omitted or treated as zero |
| Synthetic fixture could be relabeled as a project package | Reject synthetic source/quantity states in project_advisory packages | Relabeling the package alone fails; no claim that labels prove factual provenance |
| Source references identified only a whole document | Project numeric quantities require matching evidence_refs with source ID and exact locator; optional page/view and source hash | Missing/mismatched locators rejected; quoted source truth still needs review |
| Subnormal values and relative tolerance hid numeric problems | Explicit supported nonzero range and fixed absolute layer-sum tolerance | Extreme small/large inputs controlled; large wall values do not expand arithmetic tolerance |
| Removed holds did not invalidate affected records | Report changed/removed holds and seed the revalidation graph from their affected elements | Hold removal is review-required, never evidence of closure |
| Revision reports lacked exact changed fields | JSON-pointer before/after differences with absent versus null distinction | Changes identify the element/source/hold and field; both dependency graphs retained |
| A propagation-loop placement error surfaced during development | Return after reaching a fixed point, not during the first iteration | No-change and reverse-order deep dependency tests pass |
| Undefined well-to-opening alignment could look implicitly checked | Explicit not_assessed result for alignment, full sash sweep and obstructions | Narrow well does not become a fit/escape pass or receive an invented minimum size |
| Long/invalid text could break or overrun SVG output | Reject invalid control characters, escape XML, bound labels and retain full label as tooltip | XML parse/escaping/long-label tests; saved fixture matches current renderer |
| PDF rectangle paths were ignored | Expand rectangle items to four traceable edges | Real synthetic PDF rectangle yields four unique candidate IDs |
| Rotated crop dimensions did not match extraction coordinates | Use unrotated crop-relative PDF points; report cropbox and page rotation | Rotated/cropped PDF selection and text coordinates exercised |
| Skipped curves, clipped lines and sample truncation were invisible | Report omission counts, total interior candidates and sample_truncated | 50-line/curve fixture reports truncation and unsupported items |
| Source identity was only a filename | Hash the exact PDF bytes opened by the local parser; attach extraction version | Repeat extraction yields the same input hash and scoped candidate IDs |

## Detail Contract Changes

[tools/detail_package.py](../tools/detail_package.py) reports tool version 1.1.0;
the draft package schema remains version 1 with additional validated metadata and
stricter semantic checks. Existing synthetic fixtures remain valid. Previously
accepted project packages need evidence_refs before they can be processed.

Each numeric project quantity must have one or more source locators covering the
same source IDs as source_ids. A locator identifies the page/view/detail/record
location actually used; optional content_sha256 is a supplied identity assertion,
not an independently verified document hash. The tool does not open those sources.
Reported, proposed and documented evidence remain distinct. A user can still make
false assertions; schema validation does not establish truth or professional review.

Every check now includes rule_version, input_refs and a reason for discrepancy or
not_assessed. References identify the input records used, including parent-wall
and opening dependencies. Unknown layer values are explicit. The 0.01 mm layer-sum
tolerance is an arithmetic implementation tolerance, **not an installation tolerance**.
Nonzero normalized lengths smaller than 1e-6 mm or magnitudes above 1e9 mm are outside
the supported implementation range; no Norwegian design threshold is implied.

Revision differences report exact before/after fields. A removed hold is a proposal
requiring review, not a closed issue. Conservative dependency propagation may flag
more records than physically affected; the reviewer narrows the actual change scope.
No file, authority record, price or engineering hold is rewritten by the tool.

## Drawing Contract Changes

Geometry extraction version 2.1 retains schema version 2. Both local PDF tools use
unrotated crop-relative PDF-point coordinates and record rotation/crop metadata.
The view clip uses those coordinates, not the displayed rotated image coordinates.
Callers must transform a screen selection correctly before passing it to the tool.

Line/rectangle candidates now have source path/item/edge indices and a scoped ID.
These IDs are repeatable for identical source bytes and extraction version, **not
persistent BIM wall IDs across revisions**. Source SHA-256 identifies bytes, not
approval or correctness. Files are read with an explicit 50 MB input bound.

Unsupported curves and segments not wholly inside a view are counted, not silently
reconstructed. The displayed candidate list remains limited to 40 entries, with
total counts and sample_truncated exposed. It is not a complete wall model or a
quantity takeoff from that sample. Calibration still requires caller evidence and
never becomes independently confirmed merely by a source label.

Paths outside the PDF's visible crop are excluded and counted even when the parser
returns them. Crossing segments are not geometrically clipped into new segments;
that omission remains explicit. Rotated/cropped synthetic pages exercise this limit.

## Evaluation Evidence Is Now Machine-Checkable

[tools/evaluation_report.py](../tools/evaluation_report.py) and
[schemas/evaluation-run.schema.json](../schemas/evaluation-run.schema.json) implement
the record contract for [the twelve host cases](evaluations/README.md).

- A generated template contains every declared case/attempt, **not_run** status,
  no observations and no artifacts. It cannot satisfy an observed-pass gate.
- Observed records require host/model/tool/instruction identity, named reviewer,
  valid timezone-aware timestamp, duration and per-dimension verdicts.
- Transcript/artifact paths must resolve within the selected evidence root.
  Relative paths, byte limits, duplicate-key rejection and SHA-256 checks are applied;
  artifact content is not executed or treated as instructions.
- Missing cases, duplicate attempts, invalid dates, missing evidence, altered
  artifacts, inconsistent pass/failure claims and disguised failures are rejected.
- Validator fixtures never count toward host performance. A complete repeated
  host record produces only recorded_checks_met_pending_independent_review.
  Release stays not_authorized and professional review stays not_assessed.

The validator does not call a model, score transcript semantics or prove a reviewer
was truthful. Hash identity cannot prove provenance. The host benchmark itself
remains **not run**; the observed work here is deterministic validation of records.
An optional JSON Schema date-time dependency was absent locally, so explicit
calendar/timezone validation was implemented and tested instead of assuming it ran.

## Verification and Remaining Work

Final counts and commands are recorded in [IMPROVEMENTS.md](../IMPROVEMENTS.md).
The final local run passed **97 automated tests and 81 static source checks**.
Skill lint: 0 errors and 19 existing unreviewed-status warnings. Dependency and
whitespace checks passed. Updated and long-label SVG renders were visually inspected;
full labels remain available in JSON/tooltips rather than overflowing the diagram.
Tests cover actual synthetic PDF/DXF files, detail arithmetic/uncertainty/revisions,
CLI behavior, evaluation-record failure modes and existing beam/configuration
regressions. Editor/static/dependency/whitespace checks remain separate evidence.

Still open: live-host evaluations and qualified domain review; full wall/room
topology, view-to-screen UX and complete CAD/BIM authoring; verified source content,
product/standard/NA applicability and site evidence; general runtime sandboxing;
hosted CI execution; maintainer resolution of conflicting license labels.
No overall “top-tier,” compliance, safety or autonomous-construction certification
follows from these finite test results.