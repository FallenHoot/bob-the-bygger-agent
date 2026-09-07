# Leveled Drawing Reading Model (C4-Inspired)

**Part of the `drawing-reader` skill. Load when you need a systematic, cross-referenced
read of a born-digital architectural PDF instead of a single flat OCR/vision pass.**

## Why

The [C4 model](https://c4model.com/) reads a software system at four zoom levels —
Context, Container, Component, Code — instead of one diagram trying to show everything
at once. Each level answers a different question, and lower levels are cross-checked
against the ones above them.

Reading a construction/architecture drawing has the same failure mode as reading a
system with one diagram: feeding a flat rendered image (`rendered/*.png`) straight to
a vision model produces plausible-sounding but frequently wrong dimensions, because
the model is pattern-matching pixels instead of reading the drawing's actual geometry.
Born-digital PDFs can carry a vector model — every
line, every piece of text, at its true coordinate — that a flat render throws away.

This skill applies the same "same subject, different zoom, cross-referenced" idea to
drawings, backed by data extracted straight from the PDF's vector layer rather than
pixels.

## The Four Levels

| Level | C4 analogue | Question it answers | Extracted from |
|---|---|---|---|
| **L1 Sheet Context** | System Context | What is this drawing? Project, sheet number, drawing type, stated scale, how it relates to other sheets | Title block region text + `1:NNN` regex on the full page text |
| **L2 Zone Layout** | Container | What is the overall envelope, and what are the major zones/rooms inside it? | Sheet dimensions converted through the confirmed scale; room-label text block clustering (future work — see Known Limitations) |
| **L3 Element Grid** | Component | What are the individual walls, openings, and structural lines, and where exactly do they sit? | Vector line paths (`page.get_drawings()`), classified into structural candidates vs. sheet-frame/decorative lines, converted to real-world mm via the confirmed scale |
| **L4 Annotation Detail** | Code | What does every dimension string and note actually say, and does it agree with the geometry above it? | Text words with bounding boxes, clustered into colinear rows as candidate dimension chains |

**The cross-reference is the point.** A dimension chain in L4 that sums to 8000mm should
line up with an 8m × 8m rectangle found independently in L3. If it doesn't, that's a
real discrepancy worth flagging — not just an OCR error to shrug off.

## Running It

```bash
python skills/drawing-reader/scripts/extract_geometry.py "example-plan.pdf" --out geometry.json
```

Requires PyMuPDF (`pip install pymupdf`). Only works on **born-digital PDFs** — if
`L1_sheet_context.scale.confirmed` is `false` and the file is a scanned drawing or a
photorealistic visualization render, fall back to the vision-model pipelines in the
main `drawing-reader` SKILL.md instead.

## How to Use the Output

1. Read `L1_sheet_context` first — confirm scale before trusting any real-world mm
   values downstream. If scale isn't confirmed, stop and flag it (per
   `architectural-drawing-reading`'s core principle: never fabricate).
2. Skim `L3_element_grid.interior_candidates_sample` for plausible wall/room rectangles
   — closed 4-line loops with matching opposite-side lengths are the strongest signal.
3. Cross-check `L4_annotation_detail.dimension_chains` against the L3 candidates. A
   chain whose `sum_if_dimension_chain` matches an L3 rectangle's side length is a
   **confirmed** dimension. A chain that doesn't match anything in L3 is either off a
   different plane (e.g., a roof dimension read from a plan) or needs visual
   verification against the render.
4. Report findings using the same confirmed/inferred/unknown framing as
   `architectural-drawing-reading` — this pipeline produces candidates to verify, not
   ground truth.

## Known Limitations (Reported Prototype Observations)

- **Wall isolation is a shortlist, not a solved problem.** This office's PDF export
  does not preserve CAD layers, and stroke width is *not* a reliable wall/dimension-line
  discriminator here — most vector paths share the same ~0.37pt "object line" weight.
  The script instead filters by axis-alignment + minimum real-world length (300mm) +
  excluding the title-block quadrant and the sheet's printed frame. This surfaces a
  much smaller, higher-signal candidate list (from thousands of raw segments down to
  tens), but a human or vision pass must still confirm which candidates are walls.
- **L2 zone/room segmentation is not yet implemented** — it requires spatial clustering
  of room-label text blocks against the L3 envelope, which `extract_drawing.py`
  (Pipeline A) already extracts as `text_blocks` with bounding boxes. Wiring these
  together is the next iteration.
- **Dimension chain clustering is naive row-grouping** — it will pick up unrelated
  numbers (room numbers, elevation values, revision dates) that happen to sit on the
  same horizontal band. Always read the `note` field and sanity-check against the
  render before treating a chain as a confirmed dimension string.
- **Only useful on born-digital PDFs.** Scanned drawings and photorealistic
  visualization renders without readable scale text report
  `scale.confirmed: false` and should route to the vision-model pipelines instead.

*Last reviewed: 2026-09-06 — private prototype source identifiers omitted;
these observations are not independent validation.*
