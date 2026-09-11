# Beam Calculator — Supporting Reference Review

*Prepared by BTBA, AI advisory draft, not professional certification.*

**Purpose:** optional preliminary beam-response cross-checks, unit checking,
and explanations. This is a third-party website reference, not an installed
MCP tool, an authoritative material database, or a Norwegian design checker.
Load only when using or evaluating these calculators.

## Evidence and Review Scope

- **BTBA review: 2026-09-10.** All seven supplied pages returned HTTP 200.
  Their HTTP Last-Modified header was 2026-04-30. The beam-analysis and
  section-properties pages display a site review date of 2026-04-15; this is
  the publisher's claim, not independent certification.
- Read the page content and relevant portions of the served JavaScript as
  text. Inspected the [input mapping](https://beam-calculator.github.io/_next/static/chunks/0_er0om5glae-.js)
  and [one-span solver](https://beam-calculator.github.io/_next/static/chunks/00w~ypvd-k.sh.js).
  These build-specific URLs may change; rediscover the scripts from the page
  when rechecking. No third-party code was executed or copied into this repository.
- Independently recomputed the two published benchmark deflections and the
  supplied example using local closed-form arithmetic. **The interactive
  browser UI was not run**, and no whole-site solver audit was performed.
  Formula display and solver pages are not independent implementations merely
  because they have different URLs. Advanced/Eurocode pages linked by the site
  were not assessed for Norwegian National Annex support.
- No private project records were accessed or uploaded. The supplied prefilled
  values also appear as the site's default example in the inspected source;
  they are not evidence about any property or installed beam.

## Resource Map

| Resource | Useful for | Boundary |
|---|---|---|
| [Documentation](https://beam-calculator.github.io/en/documentation/) | Method, assumptions, scope and page selection | Describes preliminary elastic analysis, not full code compliance. |
| [Beam analysis, supplied example](https://beam-calculator.github.io/en/calculator/beam-deflection/?st=c&lt=p&l=4.5&e=210&i=8560&w=12&a=4.5) | Deflection, reactions, shear and bending moment | Basic page covers ideal cantilever or simply supported one-span models with a point load or full-span UDL. |
| [Formulas shown](https://beam-calculator.github.io/en/calculator/beam-deflection-formulas-shown/) | Explaining equations and hand-checking cases | Rebuild substitutions in coherent units; the displayed substitutions omit conversion factors. |
| [Unit converter](https://beam-calculator.github.io/en/calculator/beam-deflection-unit-converter/) | Length, force, line load, elastic modulus and second moment of area | Confirm quantity and exponent; area, section modulus and second moment are different properties. |
| [L/360 limit helper](https://beam-calculator.github.io/en/calculator/beam-deflection-limit-l-360/) | Arithmetic comparison with a selected deflection ratio | L/360 is not a universal Norwegian requirement. This is not a strength or vibration check. |
| [Material reference](https://beam-calculator.github.io/en/calculator/material-reference/) | Finding candidate material properties to verify | Indicative only; do not adopt its timber Fy/Fu labels as design properties. |
| [Section properties](https://beam-calculator.github.io/en/calculator/section-properties/) | Ideal rectangle, box, circle, pipe and I-section geometry | Omits fillets, rolling tolerances and cut-outs. Verify actual product tables and bending axis. |

## Use Procedure

1. **Declare the basis.** Record conceptual versus project use; input values,
   units, source/revision and evidence status; span and support conditions;
   load type, position, direction and load path; material and section axis.
   Distinguish permanent/variable actions, tributary-area conversion and beam
   self-weight. Do not assume self-weight is included. A URL cannot verify
   installed conditions or replace the structural input evidence checks.
2. **Match the model.** The basic cases assume small-deflection, linear-elastic
   Euler–Bernoulli bending with constant E and I. Do not turn a continuous,
   partially restrained, propped, variable-stiffness or otherwise different
   member into a simple span merely to fit the page. Establish a suitable
   analysis for shear deformation, staged loading or other material effects.
3. **Normalize units before substitution.** With N and mm, use E in N/mm²,
   I in mm⁴, point force in N and line load in N/mm. For the metric site inputs:
   1 GPa = 1,000 N/mm²; 1 cm⁴ = 10,000 mm⁴; 1 cm³ = 1,000 mm³;
   1 kN = 1,000 N; 1 kN/m = 1 N/mm; 1 kN·m = 1,000,000 N·mm.
   Use I about the bending axis, not section modulus W or polar inertia.
4. **Check an independent result.** Use the matching
   [local formula case](../../formulas-reference/SKILL.md), coherent units,
   equilibrium, support boundary conditions, sign convention and critical
   locations. Compare like-for-like inputs and outputs. Investigate a
   discrepancy rather than averaging results or selecting the preferred answer.
   If only page text/source was inspected, do not claim a live calculator run.
5. **Separate response from design checks.** Establish the applicable NS-EN
   1990/1991 load combinations and Norwegian National Annexes. Use the relevant
   SLS combination for the defined deflection check, not an unexplained ULS
   factored load. Verify the deflection component (instantaneous/final,
   total/variable, net of any relevant camber), span definition and criterion
   against the applicable material standard/NA and project/finish requirements.
   L/360 and the other presets are not automatic TEK17 limits; without a sourced
   criterion, report **criterion unverified**, not pass/fail.
6. **Retain the remaining checks.** Elastic deflection alone does not establish
   bending/shear resistance, lateral-torsional buckling, bearing, connections,
   restraints, vibration, fire performance, foundations or temporary works.
   Timber needs the relevant duration, service-class and creep treatment;
   concrete may require cracked/effective stiffness and long-term effects.
   Obtain a qualified structural designer's review before design/construction
   reliance. A calculator pass is not structural approval.
7. **Record only the scoped result.** Include the source URL/date, full input
   table, model, formulas, independently derived values, any actually observed
   calculator output, discrepancies, excluded checks and next evidence needed.
   Keep project records in the active project folder when saving is in scope.
   Do not send private project inputs through external URLs, forms or report
   services without explicit authorization. No automatic integration is installed
   by retaining this reference.

## Observed Cautions

- **Formula display:** the default formula page displays m, kN/m, GPa and cm⁴
  directly in a numeric deflection substitution while reporting mm. The
  inspected solver converts to N/m-based SI internally, but that displayed
  substitution is not a unit-complete calculation to copy into a report.
- **Material labels:** the page puts C16/C24 timber under generic “Yield
  Strength (Fy)” and “Ultimate Strength (Fu)” headings. Do not equate those
  fields with verified timber bending/tension/compression design strengths.
  Source the actual grade properties and material factors separately. Steel
  strength likewise needs product, grade, thickness and condition verification.
- **Section properties:** the displayed geometric W is not evidence of a
  verified plastic section modulus or steel section classification. A nominal
  I-section entered without fillets is not an exact rolled-profile database.
- **Input handling:** the inspected basic solver clamps several inputs to
  positive minima and constrains point-load position to the span. Do not assume
  zero, uplift/negative loads or out-of-span inputs were accepted unchanged;
  verify the actual analyzed case before interpreting any result.

## Bounded Arithmetic Checks

These are public examples, not project design inputs. Assume ideal stated
supports, constant stiffness, small elastic deflection and only the listed load.
No additional self-weight, strength, connection or compliance check is implied.

| Public example | Inputs | Independent deflection | Published page value |
|---|---|---|---|
| Simply supported, full-span UDL | L = 6 m; q = 5 kN/m; E = 210 GPa; I = 8,500 cm⁴ | 5qL⁴/(384EI) = 4.72689 mm | 4.73 mm |
| Cantilever, free-end point load | L = a = 3 m; P = 8 kN; E = 210 GPa; I = 3,200 cm⁴ | PL³/(3EI) = 10.71429 mm | 10.71 mm |

The two published values agree with local arithmetic at the displayed precision.
This checks those examples only, not runtime behavior across all load cases.

### Supplied Link Interpretation

The inspected mapping decodes the supplied/default example as follows:

| Parameter | Meaning | Example value / coherent calculation value |
|---|---|---|
| `st=c` | Cantilever, fixed left and free right | Idealized support, not a simply supported beam |
| `lt=p` | Point load | Not a uniformly distributed load |
| `l=4.5` | Span | 4.5 m = 4,500 mm |
| `e=210` | Elastic modulus | 210 GPa = 210,000 N/mm² |
| `i=8560` | Second moment of area | 8,560 cm⁴ = 85,600,000 mm⁴ |
| `w=12` | Load magnitude; units depend on load type | P = 12 kN = 12,000 N here, not 12 kN/m |
| `a=4.5` | Load position from the fixed end | 4.5 m, at the free end |

Using these example inputs, the independent response magnitudes are:

$$\delta_{\mathrm{tip}} = \frac{PL^3}{3EI}
= \frac{12{,}000\times4{,}500^3}
{3\times210{,}000\times85{,}600{,}000}
= 20.277\ \mathrm{mm}$$

The vertical support reaction is 12 kN upward for a downward load; the maximum
shear magnitude is 12 kN and fixed-end bending-moment magnitude is 54 kN·m.
These are **derived values, not observed browser outputs**. For illustration
only, 4,500/360 = 12.5 mm; this does not establish the governing cantilever
criterion or a project failure.

**Missing-evidence example:** a user supplies this link and asks whether an
installed beam is adequate, but its supports, section, loads and applicable
deflection criterion are unverified. Expected response: explain the encoded
example, identify those evidence gaps, and request the relevant drawings,
member evidence and design basis. Forbidden inference: assign this example
to a project, identify a profile from I alone, or declare the member safe/unsafe.