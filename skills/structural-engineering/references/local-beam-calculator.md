# Local Beam Calculator — Usage and Validation Scope

*Prepared by BTBA, AI advisory draft, not professional certification.*

## Purpose and Boundaries

[The Python calculator](../scripts/beam_calculator.py) performs deterministic,
preliminary one-span elastic beam analysis. It runs locally; it does not need
MCP, transmit input, write reports to disk, choose a section, or approve work.
Use for explicit illustrative cases and source-documented project load cases.
Read the [Norwegian design-basis register](norwegian-design-basis.md) before
interpreting the results as part of a Norwegian structural assessment.

**Implemented:** simply supported (pin/roller idealization) and left-fixed
cantilever beams; one downward point load anywhere in the span, or a full-span
uniformly distributed load (UDL). Constant E and bending-axis I; small elastic
Euler–Bernoulli deflection. The tool returns reactions, shear and moment,
analytical deflection extrema, and sampled stations for checking/plotting.
It has no automatic material values, self-weight, load factors or limit ratios.

**Not implemented:** multiple simultaneous loads, continuous/fixed-fixed beams,
partial UDL, applied moments, springs, settlements, uplift, variable stiffness,
shear deformation, long-term timber/concrete response, strength/stability,
vibration, fire, connections, bearing or foundation design. Do not force a real
member into one of the supported idealizations. Use an appropriate independent
analysis when those effects matter. No whole-site or installed-beam adequacy
claim can follow from this output.

## Setup and Running

Python 3.10+ and [Pint requirements](../scripts/requirements.txt) are needed.
Use an isolated environment; use its interpreter for both the tool and tests.
From the repository root on Windows:

```powershell
python -m venv .venv
& ./.venv/Scripts/python.exe -m pip install -r ./skills/structural-engineering/scripts/requirements.txt
& ./.venv/Scripts/python.exe ./skills/structural-engineering/scripts/beam_calculator.py --input ./skills/structural-engineering/assets/beam-example.json
& ./.venv/Scripts/python.exe -m unittest discover -s tests -p test_beam_calculator.py -v
```

On POSIX systems the environment's interpreter is `.venv/bin/python`.
Successful CLI output is JSON on stdout, exit 0. Malformed JSON/input, missing
files and unsupported numeric ranges return an error on stderr and exit 2,
without a success report. Duplicate keys, NaN/Infinity, booleans in numeric
fields, unknown keys and unsupported units are rejected. Missing dependencies
must be installed; their presence is not established by the configuration file.

## Input Contract

Start from the [public illustrative example](../assets/beam-example.json), not
private project values. For project work, keep the input and output in that
project folder, preserving sources/revisions and assumptions. Record unresolved
inputs in the basis, never turn a guessed value into a verified measurement.

| Field | Required content |
|---|---|
| `schema_version` | Integer 1. |
| `support` | `simply_supported` or `cantilever`. |
| `span` | Positive quantity with explicit value and length unit. |
| `elastic_modulus` | Positive quantity; actual applicable stiffness, not inferred from a grade label. |
| `second_moment` | Positive second moment about the bending axis, not section modulus/polar moment. |
| `load` | `kind` is `point` or `udl`; magnitude has force or line-load units respectively. Zero is supported; negative loads are rejected, not clamped. |
| `load.position` | Required only for point loads, from the left/fixed end, within [0, span]. Endpoint loads are allowed. |
| `basis.source` | Source identity, revision/date and evidence status, or explicitly illustrative. |
| `basis.geometry_and_supports` | Geometry/support evidence or assumptions, including proposed/as-built status. |
| `basis.material_and_axis` | Material/stiffness/section-axis evidence or assumptions. |
| `basis.load_basis` | `illustrative`, `SLS` or `ULS`. No label verifies a combination. |
| `basis.combination` | Actual load expression, sources/factors, action arrangement and scope; no automatic combination generation. |
| `basis.self_weight` | `included`, `excluded` or `unknown`; it is never automatically added. |
| `criterion` | Optional explicit comparison object described below; none by default. |

Every quantity is an object with a numeric `value` and a `unit` string. Allowed
units are deliberately narrow and case-sensitive:

| Quantity | Units | Internal unit |
|---|---|---|
| Length/position | mm, cm, m, in, ft | mm |
| Point force | N, kN, lbf, kip | N |
| Line load | N/mm, N/m, kN/m, lbf/ft, kip/ft | N/mm |
| E | Pa, MPa, GPa, N/mm^2, psi, ksi | N/mm² |
| I | mm^4, cm^4, m^4, in^4, ft^4 | mm⁴ |

Pint handles dimensional conversion behind an explicit unit allowlist. It does
not identify the correct physical input, stiffness or load path. In particular,
1 cm⁴ = 10,000 mm⁴; 1 GPa = 1,000 N/mm²; 1 kN/m = 1 N/mm.

## Deflection Comparison, Not Code Approval

An optional `criterion` requires all of:
- `span_ratio`: positive number, denominator in the illustrative L/ratio check;
- `source`: nonempty criterion reference/revision and scope;
- `evidence_status`: `illustrative`, `user_supplied` or `unverified`;
- `component`: `elastic_load_case` (the only response component implemented).

The tool does not accept a `verified` status: text is not independent evidence.
Missing criteria, unverified criteria, ULS load cases and unknown self-weight
inclusion return `not_assessed`. Otherwise the result is only
`arithmetic_within_supplied_limit` or `arithmetic_exceeds_supplied_limit`.
It compares the stated span divided by the stated ratio with that load case's
elastic deflection. Excluded self-weight is permissible for a clearly scoped
illustration or action-only check, not silently a complete total-load check.

**Always:** `design_compliance` remains `not_assessed`. No L/250, L/300 or
L/360 preset is supplied, and no statutory or material-standard acceptance is
implied. Final/net final or creep-sensitive checks require a different analysis
and verified material-standard/NA provisions. A sourced criterion still needs
review for its response definition, span definition and applicable combination.

## Formulas and Output Interpretation

Use the [four classic cases](../../formulas-reference/SKILL.md#11-simply-supported-beam--uniformly-distributed-load-q)
with N, mm, N/mm² and mm⁴. For a point load at a from the left end, b = L − a:

- Simply supported reactions: R_left = Pb/L; R_right = Pa/L; maximum moment
  Pab/L at the load. Maximum deflection is not generally at the load.
- For a ≤ L/2 the simple-span maximum deflection location is
  x = L − sqrt((L² − a²)/3); for a > L/2, x = sqrt((L² − b²)/3).
  A point load directly over a support gives zero internal response for this
  idealized model but still produces a support reaction.
- Simply supported deflection: Pbx(L² − b² − x²)/(6LEI) for x ≤ a;
  Pa(L − x)(L² − a² − (L − x)²)/(6LEI) for x ≥ a.
- Cantilever maximum is at the tip: Pa²(3L − a)/(6EI), reducing to PL³/(3EI)
  when a = L. Fixed-end moment magnitude is Pa.

Reports include original and normalized inputs, calculator version, formula and
numeric substitution with a coherent unit key, extrema, signs and limitations.
Downward deflection and sagging bending moment are positive; reactions are
positive upward/counterclockwise. Internal cantilever bending is negative under
the supported downward loads. Point-load station shear has before/after limits;
endpoint shear reports the interior member limit, not a fictitious segment
between collocated reaction and load. For identically zero deflection, its
reported location is just a representative point, not a unique maximum.

Stations are samples, not a finite-element mesh. Critical locations are inserted
analytically; the largest sampled displacement is not used to locate the maximum.
Never sum the maximum values of different cases as a deflection envelope.

## Verification and Remaining Work

[Offline tests](../../../tests/test_beam_calculator.py) cover public benchmarks,
all four cases, off-centre point loads and mirrored geometry, endpoint loads,
equilibrium, support displacements, signs, scaling, equivalent SI/imperial units,
bad inputs, CLI errors, deterministic reports and deflection-comparison holds.
An independent numerical virtual-work integration compares M·m/EI to the closed
forms for both support types and load types. It is not an independent certified
design tool, and agreement does not validate real inputs or Norwegian provisions.

**Run evidence, 2026-09-10:** first test run exposed a support-applied load shear
error and an overly strict exact floating-point comparison. The implementation
now handles endpoint internal shear separately; equivalent-unit tests use numeric
tolerance. The corrected suite passed 27 tests using Python 3.12.10 and Pint
0.25.3 on Windows; all 49 repository static contracts passed, including LF/CRLF
routing regression tests. Dependency compatibility checks passed. Skill lint
reported no errors, with the structural skill's existing unreviewed-status warning.
These are observed checks, not professional review. Retain the regressions and
re-run the suite after every engine change;
reported success covers only the exercised cases and supported numeric range.

**Unresolved design work:** source-check applicable editions/NA clauses and
material data before any numerical Norwegian rule is implemented. Obtain
qualified structural review before relying on a project solution. A broader
multi-span/design engine and a graphical interface are outside this version.