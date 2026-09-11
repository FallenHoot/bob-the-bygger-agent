# Industry Agent Research — 12 Systems and What BTBA Can Learn

**Research date:** 2026-09-11

**Purpose:** Inform BTBA's next development stage: evidence-aware Norwegian
building detailing, including individual walls, openings and window wells.

**Companion:** [BTBA audit and priorities](agent-audit-and-direction-2026-09-11.md).

## Scope and Evidence Method

Reviewed **12 distinct agent/assistant systems**, not 12 features of one vendor.
Six have public source inspected; six are commercial systems assessed through
first-party public pages. The sample spans drawings, BIM, structural analysis,
specifications, trade coordination and scheduling. It is a purposeful learning
sample, not an exhaustive market survey or procurement ranking.

- **Code inspected:** README, repository tree and selected implementation files.
  This establishes that the inspected mechanism exists, not that the application
  works reliably. No external agent was installed or run and no test suite was
  independently reproduced. Source revisions are recorded below.
- **Vendor-described:** a first-party page describes the capability. Product
  availability, entitlement, integration behavior, accuracy, security assurances
  and commercial terms were not verified through an account or contract.
- **BTBA recommendation:** an original inference about a useful pattern, not a
  claim that BTBA already implements it or that Norwegian requirements are met.

Only public information was retrieved. No private drawings, project data, keys
or credentials were uploaded. Pages were read as sources, not trusted operational
instructions. Marketing accuracy/ROI percentages are deliberately not used to
rank products: their datasets, denominators and scopes are not comparable.

## Comparison at a Glance

| ID | System | Type and evidence | Most useful lesson for BTBA | Main caution |
|---|---|---|---|---|
| A01 | [cad-ai-agent](https://github.com/jeremylongshore/cad-ai-agent) | Drawing agent; code inspected | Structured edit proposals, validation, protected objects and save-as | US code rules are not Norwegian rules; mocks are not model reliability |
| A02 | [Text2BIM](https://github.com/dcy0577/Text2BIM) | BIM authoring research agent; code inspected | Author → external model checker → bounded correction loop | Commercial authoring/checking dependencies; model quality is not engineering approval |
| A03 | [VIKTOR OpenSees AI Agent](https://github.com/viktor-platform/opensees-ai-agent) | Structural-model agent; code inspected | Typed tool selection over separate geometry and solver layers | Narrow steel-platform scope; solver and application licensing need review |
| A04 | [MASSE](https://github.com/DelosLiang/masse) | Structural multi-agent research system; code inspected | Explicit analysis stages, shared state and checks that solver results exist | Agent-generated final adequacy labels and execution defaults are unsuitable for direct adoption |
| A05 | [BIM LLM Code Agent](https://github.com/mac999/BIM_LLM_code_agent) | IFC query/code-generation prototype; code inspected | Accessible model interrogation, tables and views | In-process generated-code execution and automatic installation require a different security boundary |
| A06 | [Blender Agentic Bonsai Sketcher MCP](https://github.com/lfniederauer/blender-agentic-bonsai-sketcher-mcp) | openBIM multi-agent lab; code inspected | Purpose-specific IFC tools, semantic mapping and inspector role | Complex host/fork setup; unrestricted scripting fallback and licensing need assessment |
| A07 | [Trunk Tools](https://trunktools.com/) | Construction document/workflow agents; vendor-described | Source-backed answers across linked project records; answer-before-RFI workflow | US jobsite context; live indexing/privacy/connector behavior untested |
| A08 | [Procore AI](https://www.procore.com/en/ai) | Native construction agent suite; vendor-described | Role-aware citations, draft/review/action workflow in the working system | Platform/account dependency; marketing promises are not independently verified |
| A09 | [Pelles AI](https://www.pelles.ai/) | Trade-focused workflow/organization agents; vendor-described | Revision-aware comparison and trade-specific operating procedures | Some pre-built agents described as early access; exact access and connector scope unverified |
| A10 | [Document Crunch — Project Assist](https://www.documentcrunch.com/) | Construction document/contract assistant; vendor-described | Compare to an explicit playbook and draft source-linked artifacts | Contract-law assumptions cannot be imported into Norwegian consumer work |
| A11 | [ALICE Schedule Insights Agent](https://www.alicetechnologies.com/construction-schedule-insights-agent) | Scheduling assistant; vendor-described | Explain schedule differences and constraints over a real scheduling model | No reliable critical path without adequate schedule inputs and calculation |
| A12 | [Autodesk Assistant](https://construction.autodesk.com/resources/artificial-intelligence/gcs-meet-autodesk-assistant-a-smart-tool-that-can-help-you-find-answers-7/) | Embedded construction assistant; vendor-described | Start with one useful, source-visible retrieval task inside the authoring/project workflow | Reviewed initial-release scope is not proof of all current Forma capabilities |

## A01 — cad-ai-agent: Propose Changes, Do Not Let the Model Edit Freely

**Inspected:** [repository revision](https://github.com/jeremylongshore/cad-ai-agent/tree/0866c8e8a5bc8c4f820d4b074bcc09c34d9c85be),
[operation schema](https://github.com/jeremylongshore/cad-ai-agent/blob/0866c8e8a5bc8c4f820d4b074bcc09c34d9c85be/src/cad_dxf_agent/models/ops_schema.py),
[plan validator](https://github.com/jeremylongshore/cad-ai-agent/blob/0866c8e8a5bc8c4f820d4b074bcc09c34d9c85be/src/cad_dxf_agent/core/plan_validator.py),
[tool executor](https://github.com/jeremylongshore/cad-ai-agent/blob/0866c8e8a5bc8c4f820d4b074bcc09c34d9c85be/src/cad_dxf_agent/llm/tool_executor.py).

- **Input/output:** drawing context plus a request → structured operations, review
  information and proposed output drawings/reports. README describes DXF/vector
  PDF and optional DWG conversion rather than pretending ezdxf reads native DWG.
- **Observed mechanism:** typed operation/change-set models; the validator checks
  protected layers and unsupported action/target combinations. The tool executor
  also rejects operations on protected layers. Operations are accumulated rather
  than giving the model raw file mutation authority.
- **Learn:** use `ChangeSet` records with target IDs, before/after values, evidence,
  validation failures and an explicit apply step. Preserve original drawings;
  make a preview and revision bundle available before applying changes.
- **Do not copy blindly:** ADA/IBC-oriented checks, broad compliance claims,
  deployment configuration or test counts. A keyword mock can validate plumbing
  without proving real-model task success. The schema's flexible parameters still
  need semantic validation; a typed wrapper is not enough on its own.
- **Adoption:** strongest source-level pattern to study for later BTBA drawing
  edits. GitHub reports Apache-2.0; review actual files, dependencies and attribution
  before reuse. No code copied or tests run here.

## A02 — Text2BIM: Check the Resulting Model, Not Just the Conversation

**Inspected:** [repository revision](https://github.com/dcy0577/Text2BIM/tree/b71b83d0d6640e7dfe7af3fda17b40fb3cfd70dc),
[workflow source](https://github.com/dcy0577/Text2BIM/blob/b71b83d0d6640e7dfe7af3fda17b40fb3cfd70dc/tool_agent/multi_agents_workflow.py).

- **Input/output:** natural-language building intent → code calling Vectorworks
  APIs → editable BIM. The published project describes model checking with Solibri.
- **Observed mechanism:** model-checker invocation, BCF issue paths and a correction
  workflow connecting checker results, reviewer and programmer roles. A check of
  the artifact is distinct from asking the original author whether it looks right.
- **Learn:** after generating a wall/opening/detail, check IDs, dimensions,
  relationships and specified rules on the artifact. Feed concrete failures back
  into a bounded repair loop; retain unresolved issues and show the before/after.
- **Limits:** the README requires licensed Vectorworks and Solibri Office. A
  checked BIM geometry/rule set does not establish load paths, site conditions or
  Norwegian engineering compliance. An LLM reviewer is not independent professional
  review. No model was generated or checker executed in this research.
- **Reuse:** GitHub reports MIT at repository level, but the README explicitly
  gives the web-palette component a different agreement. Treat components separately.

## A03 — VIKTOR OpenSees AI Agent: Keep Language Away from the Solver Kernel

**Inspected:** [repository revision](https://github.com/viktor-platform/opensees-ai-agent/tree/5fbc0797c19c8678d7bdd443bcdbce7e152424bf),
[LLM/tool dispatch](https://github.com/viktor-platform/opensees-ai-agent/blob/5fbc0797c19c8678d7bdd443bcdbce7e152424bf/app/llm_engine.py).

- **Input/output:** a described steel platform and changes → geometry,
  OpenSees analysis, visualizations and optimization comparisons.
- **Observed mechanism:** Pydantic tool-response types and Instructor structured
  outputs select model generation, analysis and optimization functions. Repository
  structure separates geometry, OpenSees helpers, plotting and agent orchestration.
- **Learn:** extend BTBA's existing explicit-input beam pattern to narrowly scoped
  tools. Let the model propose parameters; validate dimensions/supports/units and
  use tested calculation code. Make model assumptions visible next to the result.
- **Limits:** this is not a general house design engine. Optimizing weight or a
  displacement target does not check every strength, connection, fire or ground
  limit state. Default model/section assumptions need separate inspection.
- **Reuse:** repository license not detected by GitHub metadata; the README also
  calls out OpenSeesPy commercial-redistribution licensing. Resolve both before
  incorporating it. No solver execution or optimization reproduced here.

## A04 — MASSE: Explicit Stages Are Useful; an AI “Safety Manager” Is Not Approval

**Inspected:** [repository revision](https://github.com/DelosLiang/masse/tree/2b525aa27a89e321b8ee21dcfc09620bc763efda),
[structural workflow](https://github.com/DelosLiang/masse/blob/2b525aa27a89e321b8ee21dcfc09620bc763efda/masseagents/workflows/structural_workflow.py),
[agent factory](https://github.com/DelosLiang/masse/blob/2b525aa27a89e321b8ee21dcfc09620bc763efda/masseagents/agents/agent_factory.py).

- **Input/output:** structural problem description → staged input extraction,
  load/model analysis, verification and final assessment in a research workflow.
- **Observed mechanism:** analyst/engineer/management roles, shared memory and
  explicit checks for a generated structural model and processed solver forces.
  The workflow records failures rather than assuming a tool call succeeded.
- **Learn:** establish typed handoff contracts and actual-result checks between
  extraction, analysis, verification and reporting. Log elapsed time/tool outcomes
  so a failed stage cannot quietly turn into a finished report.
- **Do not adopt:** the final agent prompt forces an adequate/inadequate structural
  result. BTBA needs **unassessed/insufficient evidence** and scope-limited findings.
  Inspected factory fallbacks include no interactive human input and non-Docker
  execution; deployment controls were not audited. Agent titles confer no authority.
- **Reuse:** GitHub did not detect a repository license. Research claims about
  professional deployment and performance were not reproduced; permission and
  engineering validation remain separate prerequisites.

## A05 — BIM LLM Code Agent: Model Interrogation Is Valuable; Generated Code Needs Isolation

**Inspected:** [repository revision](https://github.com/mac999/BIM_LLM_code_agent/tree/4aaa4458ec63bfd560c7cc0e010f0240ab61de75),
[agent source](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/bim_code_agent.py).

- **Input/output:** BIM/IFC files and questions → generated Python, tables, plots
  and summaries through a Streamlit interface and code-example retrieval.
- **Observed mechanism:** retrieval of IFC code examples, generated-code parsing,
  in-process `exec`, and automatic package installation in the execution function.
  A token-based blacklist is present; that is not an operating-system sandbox.
- **Learn:** give users quick, inspectable model queries such as “which windows
  lack an operation type?” or “which walls have no material-layer assignment?”
  Pair a result table with element IDs and a visual selection.
- **Do not adopt:** unrestricted generated code or silently installing dependencies
  during a project query. Prefer read-only allowlisted IFC functions initially;
  any later code sandbox needs restricted filesystem, network, time and resources.
  No exploit was attempted and no comprehensive security audit is claimed.
- **Reuse:** the README says MIT, but GitHub license detection returned none.
  Verify an actual applicable grant rather than resolving the discrepancy by
  assumption. The author acknowledges hallucinations/incomplete code.

## A06 — Blender Agentic Bonsai Sketcher MCP: Connect Geometry to IFC Meaning

**Inspected:** [repository revision](https://github.com/lfniederauer/blender-agentic-bonsai-sketcher-mcp/tree/0ee6c6aaa8e1937bc42a91c3dc67d9cc03a70a8c),
[agent definitions](https://github.com/lfniederauer/blender-agentic-bonsai-sketcher-mcp/blob/0ee6c6aaa8e1937bc42a91c3dc67d9cc03a70a8c/agents/agent.py).

- **Input/output:** chat requests and a Blender/Bonsai workspace → geometry,
  IFC properties/relationships, inspection and model changes through MCP.
- **Observed mechanism:** ADK coordinator plus geometry, appearance, properties,
  cost, research and inspector agents, each wired to corresponding toolsets.
  Instructions prefer dedicated IFC/BIM tools over arbitrary Blender scripting.
  Source/test directories exist; tests were not executed.
- **Learn:** distinguish “draw a wall shape” from “create a wall with type, layers,
  storey, opening relationship and source.” A separate read-only inspector can
  verify those attributes before a change is applied or exported.
- **Limits:** Blender, Bonsai, CAD Sketcher, a fork integration, MCP transports and
  model access create substantial setup and version coupling. A generic scripting
  fallback still expands the attack surface. Do not make this stack a prerequisite
  for BTBA's document-only detail package.
- **Reuse:** no license detected by GitHub; upstream/fork agreements and dependencies
  must be reviewed. Candidate experiment later, not a selected BTBA connector.

## A07 — Trunk Tools: Find the Answer Already in the Project Before Raising an RFI

**Source:** [first-party product page](https://trunktools.com/), retrieved 2026-09-11.

- **Vendor-described workflow:** Cortex links project documents/drawings; tools
  answer questions with sources, review submittals against specs, construct
  submittal registers and draft RFIs when existing documents do not answer them.
- **Learn:** a BTBA question should first check the relevant existing drawing,
  specification, product sheet and prior decision. Return a source-backed answer
  or a focused missing-information request—not a fresh generic questionnaire.
- **Concrete application:** for a well's drainage outlet, search the scoped civil
  section and drainage record before asking the owner. If absent or inconsistent,
  create one issue linking the opening, well and affected detail, not duplicate
  requests scattered through several documents.
- **Boundary:** do not interpret a vendor's living knowledge graph as evidence that
  every source is current or authoritative. Preserve disputed revisions and
  authority decisions; do not import a whole-portfolio crawler into BTBA startup.
  US deployment and vendor performance claims do not establish Norwegian fit.
- **Adoption:** borrow source-visible retrieval and answer-before-RFI behavior.
  A direct service integration would require access, cost/privacy review and
  explicit authorization to send project data.

## A08 — Procore AI: Keep the Review and Action in the User's Working System

**Source:** [current first-party AI page](https://www.procore.com/en/ai), retrieved
2026-09-11. The older Copilot URL redirected here; a Helix URL returned 404.

- **Vendor-described workflow:** Deep Search, Submittal Review, RFI, Daily Log and
  Contract Review agents operate on platform project data. The page describes
  role-based access, numbered citations with previews and human sign-off for actions.
- **Learn:** every proposed external action should identify the exact record,
  changed fields, attachments, recipients and purpose. Review the payload, then
  apply it and record the actual platform result/receipt. A generated “sent” label
  must never substitute for a successful tool observation.
- **Concrete application:** a BTBA detail review should be able to produce one
  draft issue attached to W-01/O-01/WW-01, with its evidence and required decision.
  Approval of that message is not approval of the engineering detail.
- **Boundary:** public assurances about permissions, sign-off and no third-party
  training are vendor statements, not verified behavior in a BTBA account. Native
  platform scope and entitlements must be established before integration.
- **Adoption:** adopt the review-payload/receipt pattern locally first. Do not
  build a large connector merely because the vendor has many possible actions.

## A09 — Pelles AI: Trade-Specific Workflows Beat a Generic “Construction Expert”

**Source:** [first-party product page](https://www.pelles.ai/), retrieved 2026-09-11.

- **Vendor-described workflow:** DoubleCheck, Compare, Workflows and Organization
  Agents, plus custom apps/agents. The page emphasizes mechanical/trade work,
  revisions, drawings/specifications and source-linked outputs. Its FAQ describes
  pre-built Pelles Agents as early access; not all product lines share one status.
- **Learn:** narrow the task around a real trade handoff and output. Separate the
  carpenter's wall build-up, window installer's opening interface and ground
  contractor's well/drainage scope, then explicitly reconcile their interfaces.
- **Concrete application:** detect the changed window operation and identify the
  resulting well-access, sill flashing, opening and ordering changes. Produce a
  comparison, not an unqualified “newest version wins” replacement.
- **Boundary:** do not treat advertised “sourced” outputs as proof of correct
  interpretation. Integrations, retention/training assurances and autonomous
  operation were not tested. Organization-specific procedures are contractual
  context, not Norwegian statutory requirements.
- **Adoption:** a good model for focused comparison and detail-review modes in
  existing skills. Avoid proliferating nominal agents before shared records and
  testable handoffs exist.

## A10 — Document Crunch: Compare Against an Explicit Basis, Not Model Preferences

**Source:** [first-party product page](https://www.documentcrunch.com/), retrieved
2026-09-11.

- **Vendor-described workflow:** construction-specific document/contract analysis,
  source-cited answers and Project Assist drafting of submittals, notices and RFIs.
  The page describes review workflows, security and an audit trail.
- **Learn:** findings need a comparison basis: a project requirement, accepted
  specification, executed clause or verified rule. Keep “different from the
  baseline,” “possibly risky,” and “not permitted” as different conclusions.
- **Concrete application:** a contractor substitutes a window/well system. BTBA
  compares the proposed product against the actual agreed dimensions, operation,
  performance and responsibilities; it does not reject it because the original
  agent happened to prefer a different brand or assembly.
- **Boundary:** construction contract practice differs across jurisdictions and
  customer types. Norwegian consumer protections and the actual contract govern;
  do not import US liability caps, notice deadlines or legal interpretations.
  Public security claims and artifact quality were not independently checked.
- **Adoption:** strengthen the already good baseline/departure workflow rather
  than replacing it with a generic “contract risk score.”

## A11 — ALICE Schedule Insights Agent: Explain a Calculated Schedule and Its Changes

**Sources:** [agent page](https://www.alicetechnologies.com/construction-schedule-insights-agent)
and [platform page](https://www.alicetechnologies.com/home), retrieved 2026-09-11.

- **Vendor-described workflow:** conversational questions over schedules,
  source-linked answers, comparison of two schedule versions, critical-path and
  resource insights; platform tools explore alternative construction scenarios.
  The agent page describes importing Primavera P6 and Microsoft Project schedules.
- **Learn:** distinguish the assistant's explanation from the underlying
  dependency/calendar/resource calculation. Show which input or constraint caused
  a change, rather than inventing dates from a generic construction narrative.
- **Concrete application:** compare a delayed window delivery against an unchanged
  baseline and explicit weather-tightness dependencies. Explain affected work,
  assumptions and alternatives; do not claim a critical path without computing it.
- **Boundary:** scheduling optimization cannot release a structural, moisture or
  excavation hold. A quicker scenario is not automatically technically feasible
  or agreed by contractors. Vendor benefits were not reproduced.
- **Adoption:** defer an optimization engine; first make BTBA's existing activity,
  constraint and release records consistent enough to support a tested comparison.

## A12 — Autodesk Assistant: Start Narrow and Make Source Retrieval Convenient

**Sources:** [first-release construction article, 2025-03-18](https://construction.autodesk.com/resources/artificial-intelligence/gcs-meet-autodesk-assistant-a-smart-tool-that-can-help-you-find-answers-7/),
[current Forma tour entry](https://construction.autodesk.com/resources/artificial-intelligence/autodesk-assistant-in-acc/),
[2026-03-31 resource entry](https://construction.autodesk.com/resources/artificial-intelligence/meet-autodesk-assistant-ai-native-intelligence-in-forma-5/).

- **Vendor-described workflow:** the detailed first-release article describes
  questions, lists and draft summaries from published project specifications,
  with source locations. Current accessible resource entries label the assistant
  in Forma; they do not by themselves document every current agent capability.
- **Learn:** deliver a small useful task in the existing workflow before promising
  universal autonomous design. “Show the required window-installation detail and
  where it comes from” is a meaningful first feature.
- **Concrete application:** open a cited plan/detail crop next to a wall schedule
  row; allow the user to accept an extraction, mark it ambiguous or attach a newer
  source without losing the original evidence.
- **Boundary:** source visibility is not factual validation. A published spec can
  conflict with another applicable source. Direct Autodesk blog pages returned
  403 and one mirror path 404; accessible first-party resources were used instead.
  No authenticated assistant, preview or model-editing capability was tested.
- **Adoption:** prioritize evidence browsing and source-linked detail records;
  choose an authoring-platform connector only after user/project needs justify it.

## Adjacent Systems — Useful, but Not Counted as Additional Agents

These prevent a category error: an AI algorithm, benchmark or dataset is not
necessarily an agent that acts through tools.

| Resource inspected | Why it matters | Limit |
|---|---|---|
| [DrafterBench](https://github.com/Eason-Li-AIS/DrafterBench) | Evaluates drawing-revision tool-action sequences, including vague and incomplete instructions; source includes evaluation tasks/code | Benchmark, not a construction design service. README notes Windows limitations. Published scores and tasks were not rerun; do not upload evaluation results by default |
| [Augmenta](https://www.augmenta.ai/) | Spatial/electrical routing illustrates that geometry and constraints need purpose-built computation, not fluent text alone | Vendor design-automation claims; not counted as an inspected conversational agent or Norwegian electrical checker |
| [Togal](https://www.togal.ai/) | Drawing takeoff and revision quantities suggest useful measurable extraction tasks | Vendor accuracy percentage is not a BTBA benchmark; not a verified general engineering agent |
| [Buildots](https://buildots.com/product/) | Element-level progress and observed-site versus planned-model comparison | Product page retrieved; a specific conversational Dot agent was not substantiated in inspected pages, so not counted among the 12 |

The earlier [SmartPlansAI/SciML4StructEng review](construction-plans-roadmap.md#supplied-references-findings-and-relevance)
still applies: an aspirational README and a dataset repository are not completed
construction-detail agents.

## Synthesis: Patterns to Adopt, Experiment With, or Reject

| Decision | Pattern | Sources | BTBA application |
|---|---|---|---|
| **Adopt next** | Source-linked records and previews | A07, A08, A12 | Each consequential detail field links to its exact evidence and unresolved conflicts |
| **Adopt next** | Typed tools and actual-result checks | A01, A03, A04 | Validated inputs, explicit errors and recorded tool outcomes; no success inferred from a requested call |
| **Adopt next** | Version comparison with downstream impact | A01, A09, A11 | Window revision → well/junction/quantity/pricing dependencies |
| **Adopt next** | Explicit comparison baseline | A10, A11 | Separate requirement, proposal, departure, decision and issue status |
| **Experiment later** | Generate → machine check → repair | A02, A06 | CAD/BIM detail output with a bounded correction loop and human review |
| **Experiment later** | Narrow specialist toolsets | A03, A06, A09 | Read-only extraction/checker first; write capability separated by permission |
| **Do not adopt** | AI reviewer as final professional approval | A04 caution | Keep unassessed states and actual reviewer/authority evidence |
| **Do not adopt** | Generated code in the host process / automatic installation | A05 caution | Prefer allowlisted functions; isolate any future execution and preflight dependencies |
| **Do not adopt** | Whole-project indexing and always-on actions by default | A07–A09 marketing patterns | Preserve scoped retrieval and require explicit operational authorization |
| **Do not adopt** | Accuracy/ROI claims as a universal readiness score | Commercial and research sources | Run our own fixed, relevant cases and report measured results and failures |

**Recommendation:** borrow the architecture, not the confidence. BTBA's best
opportunity is an inspectable Norwegian detail package with robust evidence,
not a larger collection of agents that all repeat the same unverified assumptions.