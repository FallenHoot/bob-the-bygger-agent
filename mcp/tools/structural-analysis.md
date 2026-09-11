# Structural Calculation Tools — Local Engine and Optional MCP

*Prepared by BTBA, AI advisory draft, not professional certification.*

## Implemented Local Calculator

The [local Python engine](../../skills/structural-engineering/scripts/beam_calculator.py)
provides explicit-unit, deterministic elastic beam response without an MCP
connection. See [setup, JSON inputs, supported cases and tests](../../skills/structural-engineering/references/local-beam-calculator.md).
It supports simply supported/cantilever beams with one point load or full-span
UDL. Pint converts allowed units; invalid inputs are rejected, not clamped.
No third-party calculator code is embedded.

Inputs and reports stay local. The CLI reads a specified JSON file and prints
the report; it does not upload inputs, change project files or submit a design.
The [public benchmark input](../../skills/structural-engineering/assets/beam-example.json)
is illustrative, not a project default. No graphical UI or MCP endpoint is
installed by this implementation.

## Norwegian Design Checks Remain Separate

Read the [Norwegian design-basis register](../../skills/structural-engineering/references/norwegian-design-basis.md):
the DiBK structural requirements and Eurocode/NA route were checked against
public official sources; numerical standard/NA factors are not implemented or
verified merely by that check. Tool arithmetic and legal/design applicability
are different layers.

Before relying on a result:
1. Record source/revision and evidence status for span, supports, stiffness,
   section axis, load path, load magnitude and self-weight inclusion.
2. Select and verify the applicable action arrangements and ULS/SLS combinations.
   The engine evaluates only the supplied load; it adds no factors or snow loads.
3. Independently check the matching model, coherent units, equilibrium and
   response. Distinguish moment/shear signs from magnitude summaries.
4. For deflection, establish a sourced response definition, reference span,
   combination and limit. No universal L/250 or L/360 requirement is assumed.
   Missing/unverified criteria remain not assessed, not pass/fail.
5. Retain stability, strength, creep/cracking, vibration, connections, bearing,
   fire, foundations and temporary-works checks where relevant. Obtain qualified
   structural review before project reliance. A tool pass is not approval or
   a generic Norwegian wet-stamp requirement.

The older glulam example is withdrawn: its stated section and supplied inertia
were not a verified matched pair. Do not reuse it as a sizing/design benchmark.
Earlier project results have not been recalculated or revalidated by this edit.

## Optional External MCP — Unverified Availability

**External reference:** [Elandu/structural-analysis-mcp](https://github.com/Elandu/structural-analysis-mcp).
Prior repository notes described a Python stdio server using `sectionproperties`,
`concreteproperties` and `PyniteFEA`, with tools named
`calculate_rectangle_section_properties`, `analyse_simple_beam_udl` and
`calculate_rectangular_concrete_section_summary`. These are historical
descriptions, not tool calls verified in this session.

**Current installation, schemas, runtime connectivity and upstream capabilities
are unverified.** A configuration entry does not establish availability. Before
installing or invoking an external implementation, inspect its current release,
dependencies, tool schema/units and limitations, and run independent benchmarks.
Use only actually exposed tools; do not claim Eurocode/NA checking from the name
or an older README. Any transmission of private project data needs explicit
authorization for that destination.

For optional website cross-checks, use the
[Beam Calculator resource review](../../skills/structural-engineering/references/beam-calculator.md).
The website, local script and possible MCP server are separate tools with
separate validation and availability claims.

*Last reviewed: 2026-09-10 — scoped documentation correction and local-tool addition.*
