# BTBA — Bob the Bygger Agent

**A Norway-first AI assistant for understanding a building project and developing
traceable construction plans.**

BTBA helps turn drawings, measurements, product information, and project decisions
into a clearer answer to **“What are we building, how will it fit together, and
what still needs to be resolved?”** It supports homeowners, designers, and
contractors preparing renovations, extensions, and other building work.

This repository is the agent's working toolkit: instructions, 25 modular skills,
document templates, and a small set of local Python utilities. It runs inside a
tool-enabled AI host such as GitHub Copilot in VS Code. It is **not a standalone
CAD application, a trained engineering model, or an autonomous design service**.

**Current stage:** advisory workflows and local tools, moving into element-by-element
construction detailing. **Documentation reviewed:** 2026-09-11; this is not a
blanket verification date for laws, standards, or technical guidance.

## What BTBA Is For

- **Understand the evidence:** read relevant drawings and records; distinguish
  existing conditions, proposed changes, assumptions, and unresolved questions.
- **Coordinate the design:** connect structure, moisture protection, insulation,
  openings, services, ground conditions, and construction sequence.
- **Prepare useful documents:** draft drawing reviews, design questions, tender
  scope, estimate reconciliations, schedules, and handover-document registers.
- **Keep the project coherent:** retain source revisions and decisions in local
  project records; identify affected work when an input changes.
- **Develop construction details:** organize how each wall, opening, and site
  interface is intended to be built, with dimensions and evidence still needed.
  The first detail-package workflow is a draft; automated drawing production is
  not implemented.

The aim is more specific than answering building questions, and more bounded
than “AI designs your house”: **a reviewable connection between project evidence,
design decisions, and the work someone must carry out.**

## What Exists Today

“Guidance” below means an agent procedure, not a tested software integration.
Instructions guide the host; they do not guarantee that every check is executed.

| Area | Current state | Important limit |
|---|---|---|
| Agent startup, routing, evidence and project records | Instruction workflows with static source-contract checks | No standalone orchestration engine or automatic background monitoring |
| Norwegian building and trade guidance | Skills for structure, TEK17/permits, ground, building physics, heritage, architecture, and services | Legacy technical tables and claims remain; verify applicable sources before use |
| Drawing extraction | Tested page selection, sparse-text retention, supported DXF unit conversion and explicit view-calibration inputs | Geometry remains heuristic; optional OCR and wall identification are not comprehensively validated |
| Beam response | Local explicit-unit calculator with numerical regression tests | One-span elastic response, not member design or code approval |
| BIM/IFC and civil/site models | Review procedures and tool examples | No bundled, validated end-to-end BIM/CAD connector |
| Tender, cost and execution support | Drafting, supplied-price arithmetic, scope reconciliation, schedule/RFI/FDV procedures | No live construction-price database, binding quotation, or certified schedule |
| Wall and window-well detailing | Draft template plus [local record validation, arithmetic and SVG preview](tools/detail_package.py), strict schema and synthetic revision tests | Rectangular geometry only; no actual project design, automated CAD generator or construction release |
| Live Norwegian geodata | [mcp/tools/norwegian-building-data.md](mcp/tools/norwegian-building-data.md) is a specification only | Server not implemented; endpoint, access and dataset claims need revalidation |

The [claim audit](docs/readme-audit-2026-09-11.md) records what was overstated and
what remains unfinished. Existing templates are starting points, not completed
designs. The shared templates now use source/applicability fields rather than
generic construction thresholds. See [reliability implementation status](docs/reliability-implementation-2026-09-11.md)
for completed repairs, test evidence and remaining review needs.

The [follow-up hardening report](docs/reliability-hardening-2026-09-11.md) adds
rotated/cropped PDF and rectangle-path handling, precise evidence/revision records,
and a local evaluation-record checker. These are tested tool improvements, not
completed live-agent evaluations.

### Local Calculation and Drawing Tools

- [skills/structural-engineering/references/local-beam-calculator.md](skills/structural-engineering/references/local-beam-calculator.md)
  documents setup, JSON input/output, and test coverage. The calculator supports
  simply supported and cantilever beams with one point load or full-span uniformly
  distributed load. It does not select sections, add load factors/self-weight, or
  check strength, connections, foundations, or Norwegian design compliance.
- [skills/structural-engineering/references/norwegian-design-basis.md](skills/structural-engineering/references/norwegian-design-basis.md)
  separates checked source material from numerical standard/NA rules still needing
  verification. Numerical tests are not professional design certification.
- [skills/drawing-reader/scripts/extract_drawing.py](skills/drawing-reader/scripts/extract_drawing.py)
  contains PyMuPDF, optional Marker OCR, and ezdxf paths. Direct DWG support is not
  established; obtain a supported DXF export. IFC takes a separate BIM route.
- [skills/drawing-reader/scripts/extract_geometry.py](skills/drawing-reader/scripts/extract_geometry.py)
  defaults to page 1 and accepts explicit page/view selection. Schema v2 separates
  detected scale from caller-supplied calibration and never claims independent
  confirmation. Candidate lines are not verified walls or load-bearing evidence.
- [tools/detail_package.py](tools/detail_package.py) checks source/element links,
  layer totals, opening geometry, limited quantities and revision dependencies.
  [examples/detail-package/README.md](examples/detail-package/README.md) demonstrates
  one fictional wall/opening/well with a generated, dimension-labeled SVG schematic.
  The tool cannot close holds or authorize work.
- [tools/evaluation_report.py](tools/evaluation_report.py) validates complete
  case/attempt records and local artifact hashes. Pending templates stay not_run;
  fixture passes never count as host performance. It does not run or grade models.

## Next Stage: Detailed Construction Plans

The next milestone is **detaljprosjektering / arbeidstegninger support**: moving
from “there is a wall here” to a coordinated description of how it is built.
Building details come first; civil/site work covers their interfaces with terrain,
excavation, drainage, foundations, and retaining structures.

For the declared scope, the intended package includes:

| Deliverable | What it should answer |
|---|---|
| Wall register and type schedule | Where is every wall? Existing, retained, altered or new? Which assembly applies, and where are the exceptions? |
| Layer-by-layer wall details | Materials, thicknesses, framing or reinforcement basis, insulation, air/vapour/water control, cavities, finishes and fixings |
| Junction details | How do wall-to-foundation, floor, roof, corner, opening and old-to-new interfaces work? |
| Window and door schedule | Structural opening versus frame dimensions versus actual clear opening; installation position, sill/head levels and operation |
| Window-well schedule — lysgraver | Clear width/projection/depth; relation to the window and terrain; escape access where applicable; drainage, waterproofing, frost, retaining and fall-protection details |
| Construction and inspection plan | Dependencies, temporary works, trade responsibilities, checks before concealment and unresolved release holds |
| Quantities and revision links | Which detail drives which quantity or pricing line, and what needs recalculation after a change? |

**No universal window-well size or wall build-up is assumed.** Dimensions depend
on the actual opening, sash movement, finished surfaces, surveyed levels,
drainage arrangement, ground conditions, intended room use, and applicable
requirements. A window's catalogue size is not its clear escape opening.

Start with the [detail-package template](templates/construction-detail-package.md)
and [construction-detail workflow](skills/construction-execution/SKILL.md#construction-detail-packages).
The [implementation plan](docs/construction-plans-roadmap.md) defines inputs,
deliverables, validation cases and later CAD/BIM work. These are a first workflow
increment, **not an implemented automatic construction-plan generator**.

### Development Priorities

1. **Evaluate the detail workflow in the host:** the local schema, arithmetic and
  synthetic revision tests exist; live agent behavior and designer review remain.
2. **Extend extraction:** broader format/export fixtures, persistent element IDs
  and verified wall topology beyond the corrected page/scale/unit handling.
3. **Extend visual output:** the single-wall SVG schematic exists; native CAD/BIM
  details, full product/junction geometry and professional review remain future work.
4. **Improve sources and integrations:** review legacy technical guidance and
   templates; validate any chosen connector; implement Norwegian geodata separately.

Dedicated market-cost data, accessibility checking and energy-assessment tools
remain future work. They are not complete merely because related skills exist.

## Quick Start

1. Open this repository in VS Code with a tool-enabled GitHub Copilot setup and
   select **BTBA Agent**, defined in
   [.github/agents/btba-agent.agent.md](.github/agents/btba-agent.agent.md).
   The optional **BTBA Quick Ask** prompt is in
   [.github/prompts/btba.prompt.md](.github/prompts/btba.prompt.md).
2. Ask a general question, or explicitly identify a project folder and the
   decision or document you want. No address or project setup is needed for
   general advice or repository maintenance.
3. For project work, supply relevant drawings/revisions, measurements and product
   data. BTBA should read the project's existing index/current summary first,
   then the sources needed for that question—not every private project.
4. Install only the optional dependencies needed for the selected local tool.
   MCP is not required for the basic file-based workflow or local beam calculator.

Example requests:

> Review these plans for missing construction details. Separate what is shown
> from what is assumed, and draft questions for the designers.

> For the selected project, make a wall-by-wall construction register and a
> window-well schedule. Link each dimension to its source; leave unknowns open.

> Explain the difference between a structural opening, window frame size, and
> clear escape opening before we choose a product.

Other hosts must be able to read the repository files and follow
[system_prompt.md](system_prompt.md). Loading that file alone does not install
tools, provide current standards, or establish host compatibility.

## How the Agent Works

The loading order is [system_prompt.md](system_prompt.md) →
[.instructions.md](.instructions.md) →
[skills/session-initialization/SKILL.md](skills/session-initialization/SKILL.md) →
[skills/routing/SKILL.md](skills/routing/SKILL.md) → relevant skills and sources.

Startup selects **repository**, **general**, or **project** mode once. Routing
selects task-specific guidance; the 25 skills include orchestration and lifecycle
skills, not 25 engineering engines. The routing table is the maintained topic map.
Relevant groups include drawings/BIM, structure/ground, envelope/services,
architecture/heritage, permits, tender/execution, and document lifecycle.

Project continuity comes from records actually saved and read again. It is not
guaranteed model memory. Changed inputs should invalidate affected conclusions
pending revalidation. BTBA responds in the user's language, with Norway as the
default jurisdiction and SI units as the default—not Norwegian as a forced language.

## Evidence, Safety and Privacy

BTBA provides **AI advisory drafts, not professional certification**. It cannot
verify concealed site conditions, approve a design or permit, or authorize work.
The appropriate Norwegian designer, trade, reviewer or authority depends on the
actual scope; generic foreign licensing/stamp rules are not substituted for it.
Missing documents are evidence gaps, not proof that work is illegal or unsafe.

Use the [shared safety and review boundaries](system_prompt.md) for structural,
ground, permit, heritage, hazardous-material and trade concerns. A drawing review,
filled template, successful calculation or BIM validation is not construction
release. External-use technical documents must identify their draft status,
sources, unresolved holds, and intended review.

Verify applicable law and guidance with [DiBK](https://www.dibk.no/) and
[Lovdata](https://lovdata.no/), standards/NA editions with
[Standard Norge](https://standard.no/), construction details with
[SINTEF Byggforsk](https://www.byggforsk.no/), and site evidence with relevant
municipal and [NVE](https://www.nve.no/)/[NGU](https://www.ngu.no/) sources.
These links are source starting points, not proof that every requirement has
been checked. Some standards and details require authorized access.

Project folders, root project context and local MCP configuration are Git-ignored
and are not distributed with a normal clone. Git ignore rules do not prevent
uploads through tools: private files must not be sent to external OCR, model,
CAD or project services without explicit authorization. Reversible local edits
within scope are distinct from sending, ordering, publishing or deleting.

MCP means **Model Context Protocol**, a way to connect a host to tools. A library,
CLI example or configuration entry is not a running MCP server. Optional
structural-service notes are in
[mcp/tools/structural-analysis.md](mcp/tools/structural-analysis.md); no external
connector is claimed tested or connected by this README.

## Related Work

Public sources reviewed on 2026-09-11; inspiration, not BTBA integrations or
Norwegian design authority:

- [SmartPlansAI](https://github.com/4EvrEvolving/SmartPlansAI): a Civil 3D/OCR
  automation experiment. The inspected repository contains a README and Git
  attributes, not an executable plan-generation implementation to adopt.
- [Agentic AI in Civil Engineering — Amir Rafe](https://pozapas.github.io/aicivil.html):
  a useful overview of skills, tool connections, evaluation and controlled
  engineering workflows; not a ready-made construction-detail engine.
- [SciML4StructEng Repository](https://sciml4structeng.github.io/Repository/):
  structural-engineering datasets for scientific ML research. Potential future
  evaluation material, not a Norwegian wall-detail catalogue or design approval.

The [implementation plan](docs/construction-plans-roadmap.md) explains what is
useful from each and what has not been evaluated or integrated.

For the broader review, see the [BTBA audit and improvement priorities](docs/agent-audit-and-direction-2026-09-11.md)
and [research of 12 industry agents and assistants](docs/industry-agent-research-2026-09-11.md).
These are evidence-based findings and proposals, not completed integrations or fixes.

## Development and Validation

Use [skills/README.md](skills/README.md) for the local authoring schema and workflow
contract, and [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance. Extend
an existing skill when practical; update routing, affected tests and documentation.
There is no duplicated skill-stack table to maintain in the system prompt.

- [skills/validate_skills.py](skills/validate_skills.py): frontmatter and structural
  lint, not upstream-host certification or technical validation.
- [tests/Test-AgentContracts.ps1](tests/Test-AgentContracts.ps1): static source/link
  regressions; the default run does not read private projects.
- [tests/test_beam_calculator.py](tests/test_beam_calculator.py): numerical and CLI
  tests for the supported local beam cases.
- [requirements-dev.txt](requirements-dev.txt) and [.github/workflows/validate.yml](.github/workflows/validate.yml):
  shared Python 3.12 test setup and Windows/Linux CI definition. CI execution is
  not claimed until the workflow runs remotely; local tests use synthetic fixtures.
- [tests/test_drawing_tools.py](tests/test_drawing_tools.py),
  [tests/test_detail_package.py](tests/test_detail_package.py) and
  [tests/test_skill_validator.py](tests/test_skill_validator.py): extraction,
  record/arithmetic/revision and malformed-configuration regressions.
- [tests/test_evaluation_report.py](tests/test_evaluation_report.py): evaluation
  evidence, timestamps, coverage, status consistency and local path/hash boundaries.
- [IMPROVEMENTS.md](IMPROVEMENTS.md): change history; old release claims are not a
  current feature or verification register.

Passing these checks does not establish live agent reliability, extraction
accuracy across arbitrary drawings, or engineering/legal correctness.
