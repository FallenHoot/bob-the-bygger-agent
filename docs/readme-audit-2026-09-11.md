# README Capability Audit

**Date:** 2026-09-11

**Scope:** Repository documentation, current local implementation, relevant
instructions and public references supplied by the user. No private project
documents were opened or used as examples.

**Follow-up:** Findings below are the historical audit baseline. The subsequent
[reliability implementation](reliability-implementation-2026-09-11.md) repairs a
defined subset; use its status for current capabilities and remaining limitations.

## Conclusion

The previous README mixed working code, instruction-only capabilities, optional
third-party tools and future features. It also retained claims superseded by the
current system prompt. The rewrite separates these states and makes detailed
construction planning the next development priority rather than claiming it is
already automated.

This is a capability/source audit, not a full engineering, legal or security audit.
The working tree already contained a local beam-calculator addition and related
changes; these were retained, not represented as new work from this review.

## Findings and Disposition

| Previous claim / issue | Evidence in current repository | Change / remaining work |
|---|---|---|
| Version 2.0, 20 skills, router loads first | 25 immediate skill directories; explicit system → shared constraints → startup → routing order | Removed stale version/completion claims; describe the actual loading contract |
| “Professional-grade”, mandatory stamps and fixed escalation thresholds | [system_prompt.md](../system_prompt.md) rejects credentials and generic foreign approval rules | Replaced with task-specific Norwegian evidence/review boundaries |
| Codes “current through all 2026 amendments”, broad knowledge-verification date | Source-specific verification is required; no comprehensive checked rule pack | Removed blanket currency and future institutional/amendment assertions; retain source starting points |
| Working MCP integrations | Configuration examples, CLIs, libraries and service notes are not live connection evidence | No connector is advertised as verified. The local config is ignored and not part of a normal clone |
| Norwegian geodata server ready to configure | [mcp/tools/norwegian-building-data.md](../mcp/tools/norwegian-building-data.md) is an implementation specification, with no server source | Explicitly unbuilt; API availability/access, coverage and hazard interpretation require review before implementation |
| Production drawing pipeline identifying walls and exact dimensions | [text extractor](../skills/drawing-reader/scripts/extract_drawing.py) and [geometry prototype](../skills/drawing-reader/scripts/extract_geometry.py) exist; optional packages and heuristic assumptions remain | Describe prototypes and dependencies, not reliable wall semantics or automatic structural classification |
| DXF/DWG supported interchangeably | Dispatcher routes DWG to ezdxf; no DWG conversion implemented | README limits the route to supported DXF input; direct DWG support remains unestablished |
| Complete scoped/structured extraction | Text extractor processes all PDF pages; geometry reads page one, accepts a scale string, samples candidate lines and leaves room segmentation unresolved | Page/view selection, calibration, element identities and regression fixtures are priorities; no extractor code changed here |
| Complete security-fenced extraction | Instructions specify untrusted-content handling; script outputs are not uniformly fenced or behaviorally tested | No claim that instruction text or an output note is a tested security boundary |
| All six templates complete | Files exist, but older templates retain generic approval roles, unsourced defaults and inconsistent draft labeling | Removed “complete” label; source/wording review remains open. Added one original blank construction-detail template |
| Complete BIM/IFC integration / universal Norwegian BIM mandate | [BIM skill](../skills/bim-ifc/SKILL.md) is procedural guidance with examples and client-specific requirements | State guidance-only integration status; no automatic acceptance or universal SIMBA/TFM requirement |
| Project memory available from an included root template | Root context and project folders are ignored; lifecycle relies on files actually saved/read | Fresh-clone instructions no longer depend on private local files or promise automatic memory |
| Development example uses nested metadata and a system skill-stack table | [local authoring standard](../skills/README.md) uses flat fields; current system has no such table | README points to the maintained authoring standard and routing rather than duplicating them |
| Quick Ask onboarding | [.github/prompts/btba.prompt.md](../.github/prompts/btba.prompt.md) had a nonexistent route path and hardcoded project context | Corrected to the actual entry point, scope ownership and evidence-summary contract; no private fallback |
| Contributor guidance contradicts current agent | [CONTRIBUTING.md](../CONTRIBUTING.md) retained forced reasoning and legacy escalation wording | Updated directly relevant authoring, safety and validation guidance; repository tests remain bounded |
| Wall-by-wall construction and well dimensions | Related domain guidance exists, but no dedicated coordinated detail package | Added an optional procedure to existing execution skill, route and template. CAD generation, sizing engine and behavioral evaluation remain future work |

## Technical Debt Not Closed by the README Rewrite

- **Building physics and construction examples:** some existing numerical values,
  generic assemblies and authority claims need primary-source review. Do not
  lift a legacy wall build-up into a project as a compliant specification.
- **Drawing extraction:** dimensions labeled in millimetres need actual input-unit
  handling; mixed-scale views need calibration; page selection and errors need
  tests. In-skill example code also needs execution review.
- **Legacy output templates:** professional/authority roles, sequencing, assumed
  dimensions/durations and release wording need a separate focused pass.
- **External services:** installation commands, transport compatibility,
  authentication, licensing, availability and data handling are unverified.
- **Norwegian building-data specification:** older hazard/return-period,
  snow-source and “all APIs open” shortcuts must be checked. No mapped result
  does not establish site safety or absence of a hazard.
- **Behavior and source validation:** passing text checks is not proof that a host
  follows instructions, calculations model real conditions, or technical guidance
  reflects the applicable current law/standard/product.

## External Reference Review

The [construction-plans roadmap](construction-plans-roadmap.md#supplied-references-findings-and-relevance)
records what was retrieved from SmartPlansAI, Amir Rafe's civil-agent overview
and SciML4StructEng, with scope and reuse limitations. None is an installed BTBA
dependency or a source for Norwegian wall/well dimensions.

## Validation Scope

Source-contract coverage was extended to the README, new roadmap/audit/template,
Quick Ask prompt, construction-detail route and workflow. These check paths,
document states, evidence fields and guard text—not a generated building design.
Actual run results are recorded in [IMPROVEMENTS.md](../IMPROVEMENTS.md).

The extraction pipelines, external connectors and CAD applications were not run.
No ignored data was staged or published; no send, move, deletion, commit or push
was performed by this update.