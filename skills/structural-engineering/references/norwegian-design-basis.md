# Norwegian Beam Design Basis — Source and Verification Register

*Prepared by BTBA, AI advisory draft, not professional certification.*

**Scope/date:** 2026-09-10, repository guidance for preliminary beam analysis.
No property, permit, installed condition or full structural design is assessed.
This distinguishes source-checked requirements from numerical rules still
unverified. It is not an assertion that the whole repository is source-verified.

## Public Requirements Checked

Both sources below were retrieved successfully (HTTP 200) on 2026-09-10.
Retrieval date is not the source's amendment/revision date. These are concise
paraphrases; consult the live text for exact wording and current applicability.

| Source and scope | Verified content | What it does not establish |
|---|---|---|
| [DiBK TEK17 §10-2](https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17/10/10-2), regulation (1)–(2) | Material/product properties must meet mechanical resistance/stability requirements; design and execution must provide satisfactory safety against failure and sufficient stiffness/stability under intended loads, during execution and in the final condition. | A universal span limit, material value or L/n deflection criterion. |
| Same source, regulation (3) | NS-EN 1990 and the underlying NS-EN 1991–1999 series with associated national annexes provide a route for meeting the stated structural requirements. | That an isolated elastic beam calculation meets the complete route. |
| Same source, **guidance** to (1) and (3) | Strength properties need documentation; local geographic/climatic conditions matter; Norwegian NAs are to be used for the Eurocode route. Other methods require documentation of equivalent safety. | A generic foreign PE/wet-stamp regime, or a legal finding based on missing files. Guidance is distinguished from the regulation text. |
| [Standard Norge: Eurokoder](https://standard.no/fagomrader/bygg-anlegg-og-eiendom/eurokoder1/), publisher overview | Common European design standards are complemented by national parameters, including climate/geography and safety choices. | Numeric coefficients, tables or current editions of individual parts/annexes. A publisher overview is not a clause-by-clause technical source. |

The checked DiBK provision does **not** prescribe a universal L/250, L/300 or
L/360 limit. This is not a claim that no applicable material standard, contract,
finish specification or other provision may require a particular limit.

## Numerical Design Rules — Not Yet Verified or Implemented

Full applicable standard/NA clauses and product records were not available as
verified calculation sources in this review. No numerical NA rule pack is
implemented in the local calculator. Do not guess values or treat previously
retained tables, metadata, a source URL or a user affirmation as verification.

| Needed for design use | Source/evidence to obtain | Current state |
|---|---|---|
| ULS and SLS combinations | Applicable NS-EN 1990/NA edition, design situation, expressions, partial/combination factors, leading/accompanying actions and arrangements | Unverified; no hard-coded factors. |
| Imposed loads | Applicable NS-EN 1991-1-1/NA, use category, distributed/concentrated loads and applicability | Unverified; no residential default. |
| Snow | Applicable NS-EN 1991-1-3/NA, location/altitude, ground load, roof shape, exposure, thermal, drift/unbalanced cases and horizontal-area basis | Unverified; no city/roof default. |
| Wind | Applicable NS-EN 1991-1-4/NA, location/terrain, geometry, pressure/exposure and relevant arrangements | Unverified; no wind-zone default. |
| Permanent loads and self-weight | Source-dated product/assembly quantities, force versus mass units, tributary widths and load path | Project-specific; never assumed included. |
| Steel stiffness/resistance/stability | Applicable NS-EN 1993/NA and product standards, traceable grade/thickness, section/axis/class, restraints and connections | No grade or capacity presets implemented. |
| Timber stiffness/resistance/creep | Applicable NS-EN 1995/NA, solid timber or glulam product/grade standard, service class, load duration, k_mod/k_def and response definition | No grade/factor/creep presets implemented. |
| Concrete stiffness/long-term effects | Applicable NS-EN 1992/NA, material/age, reinforcement, cracking, creep/shrinkage and effective stiffness | Elastic input alone does not cover these. |
| Deflection acceptance | Applicable material standard/NA plus project/finish/equipment criteria; exact displacement component, reference span, combination and long-term effects | No universal ratio; absent/unverified criterion remains not assessed. |

## Project Design Handoff

Before relying on a solution, a qualified structural designer needs the
source-dated geometry/support evidence, full action takeoff/load path, separate
ULS/SLS combination basis, section/material condition, restraint and connection
details, reaction transfer through supports/foundations, and checks outside the
elastic model. Identify ansvarlig prosjekterende where the Norwegian
responsibility system applies; check actual scope/roles rather than importing
a foreign licensing/stamp requirement.

For any future numerical rule addition, record the exact standard/NA edition,
clause/table, applicability, source status, reviewer and independent benchmark
before enabling it. Include missing/conflicting-source regression cases and
preserve the applicable design-basis version in each report. A test pass proves
neither clause applicability nor statutory acceptance.

## Scoped Corrections Made

The structural skill's former blanket timber deflection ratios and simplified
universal load-combination guidance are replaced with sourced-criterion and
combination-selection procedures. Related city snow examples are no longer
design defaults. The MCP guide no longer claims an available tool, automatic
Eurocode checking or a wet stamp merely from a configuration/example.
Earlier project analyses have **not** been revalidated by these changes; if
they relied on these defaults, identify affected calculations before reuse
under the [lifecycle dependency procedure](../../project-lifecycle/SKILL.md).