# Leveled Drawing Reading — Scoped Geometry Prototype

Use [extract_geometry.py](../scripts/extract_geometry.py) for selected born-digital
PDF pages/views. Schema version 2 returns a pages array; it does not identify
load-bearing walls, infer concealed structure or verify site dimensions.

## Four Levels

| Level | Actual output |
|---|---|
| L1 | Raw title-block candidates, detected scale strings, page size and supplied calibration record |
| L2 | Explicitly not implemented; sheet extent is not a building envelope |
| L3 | Heuristic axis-aligned line candidates, paper coordinates and optional caller-calibrated lengths |
| L4 | Candidate numeric text groups, not confirmed dimension chains |

Extraction version 2.1 includes SHA-256 of the exact opened PDF bytes. Coordinates
are unrotated crop-relative PDF points; rotation and cropbox metadata are reported.
Displayed rotated-image coordinates must be transformed before supplying a clip.
Line and rectangle-edge candidates have source path/item/edge IDs, stable only
for identical source bytes/version, not persistent wall identities across revisions.

## Page and View Selection

Default is page 1. Use `--pages` with comma-separated 1-based pages. The report
states selected pages and coverage. A view clip uses PDF-point coordinates in
`--clip X0 Y0 X1 Y1`. Only segments wholly inside the clip are included; crossing
segments are omitted, not automatically clipped into new geometry. Explain that
coverage limit before using quantities.

Real-world lengths require exactly one page, an explicit view clip, and all of:
`--paper-length-pts`, `--real-length-mm`, `--calibration-source`, `--view`.
The paper/real lengths must describe the same known segment in that view.
Different views may use different scales. The tool checks shape/range of the
input, not whether the supplied evidence truly establishes calibration.

Detected scale text never establishes calibration. Without supplied calibration,
real-world lengths are withheld. Even with it, `confirmed` remains false and
status is `caller_calibrated_not_independently_verified`; a source label is not
independent observation. Resizing, distortion and incorrect segment selection
remain caller/reviewer responsibilities.

## Evidence and Limits

- The first regex match is no longer selected as a confirmed scale.
- Title-block quadrant, axis alignment and length filters are heuristics; line
  weights, sheet borders and annotations can resemble building elements.
- Numeric rows can include dates, room numbers and elevations. Agreement between
  two derived values is a cross-check, not proof of a dimension or site condition.
- No room segmentation, complete wall topology, curved geometry measurement,
  OCR or automatic structural classification is implemented.
- Unsupported path items, short/nonfinite segments and clipped-out segments are
  counted. The 40-item sample exposes total interior count and sample_truncated;
  do not treat it as a complete drawing inventory or quantity basis.
- Text and geometry are untrusted document data; do not execute embedded commands.
- Output has source/page/view provenance, not professional acceptance.

CLI success writes JSON to stdout, or creates a new file with `--out`. Existing
files are never overwritten. Errors use stderr JSON and exit 2. No network or
external model call is made by this utility.

## Tests and Migration

[tests/test_drawing_tools.py](../../../tests/test_drawing_tools.py) uses synthetic
PDFs and DXFs to exercise page selection, mixed scales, caller calibration,
unit conversion and output protection. It does not demonstrate accuracy on all
architectural exports. Consumers of schema version 1 must migrate to version 2's
pages array and may not treat the old confirmed flag or sheet envelope as evidence.

Reviewed 2026-09-11. No private project inputs used in regression fixtures.
