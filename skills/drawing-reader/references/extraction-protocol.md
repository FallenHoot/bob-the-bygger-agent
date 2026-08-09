# Norwegian Drawing Extraction: Annotated Examples & Symbol Reference

**Part of the drawing-reader skill. Load when interpreting extracted text from Norwegian drawings.**

---

## Title Block Field Mapping

Norwegian title blocks vary by firm but always contain these fields (Norwegian → location hints):

| Norwegian label | English | Typical position | What to extract |
|---|---|---|---|
| **Prosjekt / Prosjektnavn** | Project name | Top of block | Full name |
| **Tiltakshaver / Oppdragsgiver** | Client | Upper section | Name/company |
| **Prosjektnummer** | Project number | Upper section | Number |
| **Tegningsnummer** | Drawing number | Prominent; often bottom right | Full number (e.g., A-101) |
| **Tegningsnavn / Innhold** | Drawing title | Large text | What the drawing shows |
| **Målestokk** | Scale | Often bottom section | Ratio (e.g., 1:100) |
| **Dato / Tegnet** | Date drawn | Bottom section | Date |
| **Rev** | Revision | Small table; bottom | Latest revision letter + date |
| **Tegnet av** | Drawn by | Bottom | Initials |
| **Kontrollert av** | Checked by | Bottom | Initials |
| **Ansvarlig / Prosjektleder** | Project manager | Bottom | Name |

**Common drawing number conventions:**
- `A-101`: Architecture, drawing 101
- `K-101`: Konstruksjon (structural), drawing 101
- `V-101`: VVS (plumbing/HVAC)
- `E-101`: Elektro (electrical)
- `L-101`: Landskap (landscape)
- `S-101`: Situasjonsplan (site plan)

---

## Scale Reference — Pixel to Millimeter Conversion

When working from raster images (JPEG/PNG) without stated scale, estimate from known elements:

| Known element | Typical real dimension | Use to calibrate |
|---|---|---|
| Standard door | 900 mm wide, 2050–2100 mm tall | Most reliable calibration point |
| Standard interior door | 800 mm wide | If exterior door not visible |
| Stair tread depth | 250–270 mm | Stairs visible in plan |
| A4 paper (if shown in title block frame) | 210 × 297 mm | Very reliable |
| Standard room height (from snitt) | 2400–2700 mm | Section drawings |
| Brick/block module | 300 mm (Norway) | Masonry walls |
| Timber stud spacing | 600 mm (Norway standard) | Timber frame walls |

**Formula:**
```
Real dimension (mm) = Pixel measurement × (Known real size / Known pixel measurement)
Scale = Real dimension / Drawing dimension
```

---

## Norwegian Wall Hatch Conventions (NS 3041)

When describing wall hatching in extracted drawings:

| Hatch pattern (description) | Material | Structural? |
|---|---|---|
| Dense diagonal lines (45°) | Concrete (betong) | Usually YES |
| Brick-pattern (horizontal courses) | Masonry (teglstein/murstein) | Usually YES |
| Dot grid pattern | Lightweight block (lettklinker) | Sometimes |
| No hatch, thin lines | Timber frame (trestenderverk) | Sometimes YES |
| "X" diagonal cross-hatch | Steel section | YES |
| Wavy horizontal lines | Insulation (isolasjon) | NO |
| Empty / hollow | Air gap / cavity | NO |
| Dense dots | Sand/fill/pukk | NO |

**Critical:** Double-line walls with NO hatch = partition walls (skille vegger). 
Heavy/hatched walls = load-bearing walls (bærende vegger).

---

## Dimension String Reading

Norwegian drawings use chain dimensioning and overall dimensions. Reading order:

```
Outer dimension (total) ──────────────────────────────────────────
                    │                                              │
Inner chain ────────┼───────┼───────────┼──────────┼─────────────┤
                    │  900  │   3600    │   1200   │     2400    │
                    │       │           │          │             │
           Wall     Door    Wall span   Window     Wall to corner
```

**Red flags in dimension extraction:**
- Dimension total ≠ sum of chain components (drafting error or missed dimension)
- Dimension followed by asterisk (*) = non-standard / verify on site
- Dimension in parentheses = reference dimension (informational, not tolerance)
- Dimension with "ca." prefix = approximate

**Norwegian text in dimension strings:**
- `ca. 3600` = approximately 3600 mm
- `min. 900` = minimum 900 mm
- `fri åpning 860` = clear opening 860 mm (doorway width)
- `lysåpning` = clear opening (also for windows)
- `UK bjelke` = underside of beam (elevation)
- `OK dekke` = top of slab/floor
- `FH` / `FFL` = finished floor level (ferdig gulvhøyde)
- `RH` = raw floor height (råhøyde)

---

## Room Schedule Extraction

Look for a table (usually on the floor plan or a separate schedule sheet) with columns:

| Norwegian | English | Extract |
|---|---|---|
| Romnummer | Room number | Number |
| Romnavn / Betegnelse | Room name | Name |
| Areal / BRA | Floor area | m² value |
| Takhøyde | Ceiling height | m value |
| Gulvbelegg | Floor covering | Material |
| Himling | Ceiling type | Type |
| Vegger | Walls | Material/treatment |

If no schedule is present, extract room labels directly from the floor plan. Norwegian room names:

| Norwegian | English |
|---|---|
| Stue | Living room |
| Kjøkken | Kitchen |
| Soverom | Bedroom |
| Bad / Baderom | Bathroom |
| WC / Toalett | Toilet |
| Gang / Entre | Hallway / Entrance |
| Bod | Storage room |
| Teknisk rom | Utility / plant room |
| Garasje | Garage |
| Kjeller | Basement |
| Loft | Attic |
| Vaskerom | Laundry room |
| Kontor | Office |
| Trapperom | Stairwell |

---

## Structural Notation on Norwegian Drawings

When extracted text includes structural annotations:

| Notation | Meaning |
|---|---|
| `BV` or `BV:` | Bærende vegg (load-bearing wall) |
| `SV` | Skillevegg (partition wall) |
| `B [size]` or `Bjelke [size]` | Beam (bjelke) with section |
| `HEB [size]` / `IPE [size]` | Steel beam profile |
| `GL [size]` | Glulam timber |
| `C24 [size]` / `C30 [size]` | Structural timber grade + section |
| `S [size]` or `Søyle [size]` | Column (søyle) |
| `D [diameter]` | Pile diameter or rebar diameter |
| `Ø [diameter]` | Circular section (rebar: Ø16 = 16mm rebar) |
| `K [spacing]c` | Rebar spacing (e.g., K150c = 150mm centers) |
| `Fc [grade]` | Concrete class (e.g., Fc30 = C30/37) |
| `⊥` symbol on wall | Wall tied to adjoining wall |
| Arrow on beam | Load direction / span direction |
| `UK BJ` | Underside of beam (UK = underkant) |
| `OK DK` | Top of deck/slab (OK = overkant, DK = dekke) |

---

## Elevation Reference System

Norwegian drawings use a consistent elevation datum:

| Notation | Meaning |
|---|---|
| `±0.00` or `±0,00` | Reference level (usually finished ground floor) |
| `+2.70` | 2700 mm above reference (floor-to-ceiling) |
| `-0.30` | 300 mm below reference (e.g., step down) |
| `FH+0.00` | Finished floor height at reference |
| `FK` or `FG` | Ferdig gulv / Ferdig grunn (finished floor / ground) |
| `RH` / `RG` | Råhøyde / Rågrunn (raw height / sub-grade) |

The reference level (±0.00) must be established relative to known terrain. Check if the situasjonsplan or snitt states the reference in meters above sea level (m.o.h. — meter over havet).

---

## Common Extraction Failures and Fixes

| Problem | Likely cause | Fix |
|---|---|---|
| Dimensions read as letters (e.g., "39O0" instead of "3900") | OCR confusing zero with letter O | Post-process: replace isolated O in dimension context with 0 |
| Scale reads as "1:1OO" | Same issue | Replace O → 0 in scale strings |
| Room labels merged with dimensions | Low resolution, text too close | Ask for higher resolution image |
| Title block partially missing | Drawing cropped at scan | Ask user to rescan with more margin |
| Dimensions missing entirely | Drawing uses only graphical dimensions (no text) | Use scale bar calibration method; manual measurement required |
| Norwegian characters corrupted (æøå) | Wrong encoding in PDF | Re-extract with UTF-8 encoding specified |
| Rotated text not extracted | OCR not handling rotation | In Marker: --force_ocr; in vision model: explicitly ask for rotated text |
