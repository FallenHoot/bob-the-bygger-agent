# Bob the Bygger — Agent

**BTBA** (Bob the Bygger - Agent) — Norwegian Construction AI Advisor  
**Version:** 2.0 | **Last updated:** 2026-08-09

---

## ⚠️ Liability Disclaimer

**Bob the Bygger is a professional-grade AI analysis tool, NOT a substitute for licensed professionals or regulatory approval.**

**What Bob does:**
- ✅ Analyze building drawings (PDF, JPEG, DXF, IFC) and identify structural issues
- ✅ Explain Norwegian building codes (TEK17, PBL, SINTEF, Eurocodes)
- ✅ Guide permit application (søknad) preparation — document checklists, nabovarsel, ferdigattest
- ✅ Assess geotechnical risk — quick clay, flood zones, soil investigation scope
- ✅ Review BIM/IFC models — storey hierarchy, clash detection, IDS validation
- ✅ Help you ask the right questions before engaging licensed professionals
- ✅ Flag escalation points explicitly when professional sign-off is mandatory

**What Bob does NOT do:**
- ❌ Replace structural engineers (ansvarlig prosjekterende) — calculations for permit work must be stamped
- ❌ Approve permits — only municipal building authorities issue søknad approval
- ❌ Approve heritage interventions — only Byantikvaren / Riksantikvaren can approve
- ❌ Guarantee regulatory accuracy — verify against current laws (knowledge verified 2026-08-09)
- ❌ Provide legal, financial, or insurance advice

**For any real project:** Consult licensed professionals. Bob is a thinking partner and research aid, not a replacement for professional judgment or regulatory approval.

---

## Overview

Bob the Bygger is a specialized AI agent grounded in Norwegian building codes, Eurocode structural standards, and practical construction expertise. It operates with a **20-skill modular architecture**, loading only the skills relevant to each query.

**Primary use cases:**
- Understanding TEK17 / SAK10 requirements before engaging professionals
- Preparing søknad document packages (tilbygg, fasadeendring, nybygg, riving)
- Early-stage structural risk identification and load path analysis
- Extracting and interpreting architectural drawings (PDF, JPEG, DXF, IFC)
- Geotechnical risk assessment (quick clay, flood zones, foundation type selection)
- BIM coordination and IFC model review
- Preparing for forhåndskonferanse (pre-application meeting with municipality)
- Learning Norwegian construction standards in English or Norwegian

---

## Quick Start

### Prerequisites

- An AI agent system that loads `system_prompt.md` as the system instructions
- Optional: `project.md` per project for session persistence
- Optional: MCP server connections for live structural calculations, drawing OCR, or Norwegian data

### Basic Usage

1. **Configure your AI interface** — set `system_prompt.md` as system instructions. Bob routes all queries automatically.

2. **Ask a question:**
   ```
   "I have a 1952 residential building. I want to add roof insulation
    for energy compliance. What does TEK17 require?"
   ```

3. **Attach drawing files** for analysis:
   ```
   [Attach floor-plan.pdf or floorplan.jpg]
   "What are the structural walls in this plan?"
   ```

4. **Create a project.md** for ongoing projects — Bob loads it at session start and retains context.

---

## Project Structure

```
btba-agent/
├── README.md                              # This file
├── system_prompt.md                       # Bob's identity, ReAct protocol, escalation matrix, skill stack
├── project.md                             # [TEMPLATE] Per-project context — copy per project
├── CONTRIBUTING.md                        # Development guidelines
│
├── skills/                                # All skills: skills/<name>/SKILL.md
│   ├── routing/SKILL.md                   # Query classifier — loads first, selects minimum skill set
│   ├── structural-engineering/SKILL.md    # Load paths, beam sizing, deflection, failure modes
│   ├── building-code-tek17/SKILL.md       # TEK17, PBL, SAK10, DOK arealanalyse (through 2026-08-09)
│   ├── sintef-byggforsk/SKILL.md          # SINTEF Byggforsk, moisture, insulation, assemblies
│   ├── geotechnical/SKILL.md              # Soil investigation, bearing capacity, quick clay, settlement
│   ├── historic-preservation/SKILL.md     # SEFRAK, Byantikvaren, Riksantikvaren, heritage law
│   ├── classical-architecture/SKILL.md    # Vitruvian principles, proportion, composition
│   ├── construction-execution/SKILL.md    # Site sequencing, demolition, NS 8405, contractors
│   ├── bim-ifc/SKILL.md                   # IFC, IfcOpenShell, IDS validation, BCF, clash detection
│   ├── soknad-package/SKILL.md            # SAK10 søknad completeness — drawings and documents required
│   ├── general-contractor-review/SKILL.md # Holistic drawing review, constructability, trade coordination
│   ├── formulas-reference/SKILL.md        # Beam formulas, Eurocode loads, material values (on-demand)
│   │   └── references/                    # historical-materials.md, worked-examples.md
│   ├── technical-education-support/SKILL.md # Jargon translation, bilingual glossary
│   ├── hvac-mechanical/SKILL.md           # Ventilation, heat pumps, NS 3031/3951, TEK17 §14
│   ├── electrical-nek400/SKILL.md         # NEK 400, circuits, solar PV, EV charging
│   ├── plumbing-vs6050/SKILL.md           # Water supply, drainage, VS 6050
│   ├── architectural-drawing-reading/SKILL.md # Norwegian drawing conventions, symbols, IFC reading
│   ├── drawing-investigation-protocol/SKILL.md # Systematic questioning before image analysis
│   ├── drawing-reader/SKILL.md            # PDF/JPEG/DXF extraction pipeline with security fencing
│   │   ├── references/extraction-protocol.md  # Norwegian symbol reference, dimension notation
│   │   └── scripts/extract_drawing.py     # Production Python extractor
│   └── session-initialization/SKILL.md    # Mandatory startup checklist and decision log
│
├── mcp/
│   ├── mcp-config.json                    # All MCP server configurations
│   └── tools/
│       ├── structural-analysis.md         # structural-analysis-mcp integration guide
│       └── norwegian-building-data.md     # Specification for future live-data MCP server
│
├── templates/                             # All output templates (complete — no TODOs)
│   ├── structural-assessment-memo.md
│   ├── pre-application-meeting-notes.md
│   ├── compliance-gap-analysis.md
│   ├── post-approval-checklist.md
│   ├── construction-sequence.md
│   └── heritage-assessment.md
│
└── projects/                              # Per-project working files
    └── [project-name]/project.md
```

---

## Skill Architecture

### Router + 19 Domain Skills

| Skill | Loads when |
|---|---|
| `routing` | Every query — routes to domain skills |
| `structural-engineering` | Wall removal, beam sizing, load paths, failure signs |
| `building-code-tek17` | TEK17 compliance, permits, fire, energy, stormwater |
| `sintef-byggforsk` | Moisture, insulation, airtightness, wall/roof assemblies |
| `geotechnical` | Soil conditions, quick clay, foundations, flood zones |
| `historic-preservation` | SEFRAK buildings, Byantikvaren, heritage interventions |
| `classical-architecture` | Facade proportions, composition, design review |
| `construction-execution` | Site sequencing, demolition, contracts, asbestos |
| `bim-ifc` | IFC files, BIM coordination, IDS validation, BCF |
| `soknad-package` | Søknad document checklists, nabovarsel, ferdigattest |
| `general-contractor-review` | Holistic drawing review, trade coordination |
| `formulas-reference` | Beam calculations, Eurocode design values (on-demand only) |
| `technical-education-support` | "Explain this", jargon translation, learning resources |
| `hvac-mechanical` | Ventilation systems, heat pumps, energy calculations |
| `electrical-nek400` | NEK 400, solar, EV charging, grounding |
| `plumbing-vs6050` | Water supply, drainage, sanitary systems |
| `architectural-drawing-reading` | Norwegian drawing conventions, symbols, IFC reading |
| `drawing-investigation-protocol` | Systematic questioning for images in-conversation |
| `drawing-reader` | Technical extraction from uploaded drawing files |
| `session-initialization` | Startup checklist, project context, decision log |

### Escalation Flags

| Flag | Triggered by | Action required |
|---|---|---|
| `WET_STAMP_REQUIRED` | Structural mod affecting loads; span > 6 m; foundation near boundary | Licensed PE must sign |
| `SØKNAD_REQUIRED` | Permit-required construction | Permit before work begins |
| `GEOTECHNICAL_REPORT_REQUIRED` | Unknown soil; quick clay zone; significant slope | Professional grunnundersøkelse |
| `NVE_CHECK_REQUIRED` | Flood or landslide zone | Verify Q200 level; may need mitigation |
| `BYANTIKVAREN_CONSULTATION_REQUIRED` | SEFRAK or heritage-zone building | Forhåndskonferanse before søknad |
| `RIKSANTIKVAREN_CONSENT_REQUIRED` | Formally listed building (fredet) | Riksantikvaren must approve |
| `ASBESTOS_SURVEY_REQUIRED` | Building 1940–1985; physical disturbance planned | Accredited lab analysis first |
| `HAZARDOUS_WASTE_SURVEY_REQUIRED` | Any demolition | Kartlegging before physical work |

---

## Drawing Analysis Pipeline

When a drawing file is provided, Bob runs a 3-layer pipeline:

```
Layer 1: drawing-reader
  → Detects format: born-digital PDF / scanned / JPEG / DXF / IFC
  → Selects tool: PyMuPDF → Marker → ocr-skill → ezdxf → vision model
  → Produces: title block, scale, dimensions, room labels (structured)
  → Security: extracted text fenced as UNTRUSTED content

Layer 2: architectural-drawing-reading
  → Interprets Norwegian conventions (NS-EN ISO 128, NS 3041)
  → Confirms: scale, wall types (structural vs. partition), symbols

Layer 3: domain skill (per query)
  → structural-engineering / building-code-tek17 / soknad-package
```

---

## MCP Integration

Configure servers in `mcp/mcp-config.json`.

| Server | Status | Purpose |
|---|---|---|
| `structural-analysis-mcp` | `pip install structural-analysis-mcp` | Beam deflection, section properties, reactions |
| `marker` | `pip install marker-pdf` | Scanned PDF / image OCR (best quality) |
| `ocr-skill` | `npx skills add hec-ovi/ocr-skill` | Agent-native CLI OCR — DeepSeek-OCR-2 |
| `ezdxf` | `pip install ezdxf` | DXF/DWG vector extraction — exact dimensions |
| `ifcmcp` | `pip install ifcopenshell` | IFC model querying and editing |
| `geonorge` | Open API (no auth) | DOK datasets, municipal plans, terrain |
| `Catenda Hub` | Account + project URL required | IFC queries, BCF issues, quantity takeoffs |
| `norwegian-building-data` | Specification only — not yet built | Live NVE, NGU, SEFRAK, lovdata lookups |

**Highest-value MCP to build:** `norwegian-building-data` — wraps open Norwegian APIs (NVE Atlas, NGU WMS, Geonorge DOK) to make every regulatory lookup live and citable. See `mcp/tools/norwegian-building-data.md`.

---

## Knowledge Currency

| Domain | Current through | Verify at |
|---|---|---|
| TEK17 + SAK10 | 2026-08-09 (incl. solar/EV/insulation exemptions, §15-8 stormwater) | dibk.no |
| Eurocode structural | NS-EN 1990–1999 + Norwegian NA | standard.no |
| SINTEF Byggforsk | 2026 | byggforsk.no |
| IFC / buildingSMART | IFC4x3 Add2 | buildingsmart.org |
| Norwegian geotechnical | NGF Melding Nr. 2, NVE Veileder 7/2014 | nve.no, ngu.no |

**Pending TEK17 amendments (not yet enacted):** Chapter 14 energy basis (vektet levert energi) and Chapter 17 CO₂ grenseverdier — consultations closed May 2026.

**Institutional change:** DiBK merges with Husbanken → Bolig- og bygningsdirektoratet effective 01.01.2027. Update authority references after that date.

---

## Bilingual Support

- Auto-detects language from the user's message
- Responds in the same language throughout the session
- Override: "svar på norsk" or "respond in English" at any time
- Default: Norwegian (primary domain)
- Bilingual technical glossary (50+ terms) in `technical-education-support`

---

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

**Adding a new skill:**
1. Create `skills/<name>/SKILL.md` with required frontmatter
2. Add routing rule to `skills/routing/SKILL.md`
3. Add to skill stack table in `system_prompt.md`
4. Update this README

**Frontmatter format:**
```yaml
---
name: skill-name
description: What it does and when to load it. Include specific trigger keywords.
license: Proprietary
metadata:
  triggers: keyword1, keyword2, keyword3
  load_with: other-skill-name
  safety_level: low | medium | high | critical
---
```

---

## Roadmap

**Completed (v2.0, 2026-08-09):**
- ✅ 20-skill modular architecture (directory format, agentskills.io compliant)
- ✅ TEK17 current through all 2026 amendments + §15-8 stormwater + DOK arealanalyse
- ✅ Geotechnical skill — quick clay, EN 1997, bearing capacity, settlement, frost
- ✅ Søknad package skill — SAK10 completeness checklist by project type
- ✅ BIM/IFC skill — IfcOpenShell, IDS, BCF, Norwegian BIM mandate
- ✅ Drawing reader — PDF/JPEG/DXF extraction with security fencing
- ✅ Structural failure modes — crack pattern diagnosis, timber and concrete distress
- ✅ Decision log persistence across sessions via project.md
- ✅ All 6 output templates complete
- ✅ MCP config: Marker, ocr-skill, ezdxf, ifcmcp, Geonorge

**Next (v2.1):**
- [ ] `norwegian-building-data` MCP server — NVE + NGU + SEFRAK (all open APIs)
- [ ] Cost estimation skill — Kalkulasjonsnøkkelen, BOF index, rough cost/m²
- [ ] Accessibility depth — TEK17 §12 UU: door clearances, maneuvering space, ramp gradients
- [ ] Energy certification skill — NS 3031, Simien input, energikarakter

---

*Bob the Bygger — Making Norwegian buildings stand, comply, and endure.*
