# MCP Tool: structural-analysis-mcp

**Source**: [github.com/Elandu/structural-analysis-mcp](https://github.com/Elandu/structural-analysis-mcp)
**Status**: Available (MVP, June 2026) — no Eurocode compliance checks yet
**Language**: Python
**Protocol**: MCP over stdio

---

## What It Does

Exposes deterministic structural engineering calculations to AI agents via MCP tool calls. Uses established open-source Python engineering libraries:
- `sectionproperties` — geometric section properties
- `concreteproperties` — concrete section analysis
- `PyniteFEA` — finite element analysis

This fills BTBA's biggest gap: **real numbers instead of in-context estimates**.

---

## Available Tools

### `calculate_rectangle_section_properties`
Gross geometric properties for a solid rectangular section.

```json
{
  "name": "calculate_rectangle_section_properties",
  "arguments": {
    "width_mm": 90,
    "depth_mm": 315
  }
}
```

Returns: `area_mm2`, `centroid_x_mm`, `centroid_y_mm`, `ixx_mm4`, `iyy_mm4`, `j_mm4`

**Halvard use case**: Before sizing a glulam beam, confirm Ixx for the proposed section before calculating deflection.

---

### `analyse_simple_beam_udl`
Simply supported beam under full-span UDL — reactions, max shear, max moment, max deflection.

```json
{
  "name": "analyse_simple_beam_udl",
  "arguments": {
    "span_m": 5.4,
    "udl_kn_per_m": 12.0,
    "elastic_modulus_mpa": 13600,
    "ixx_mm4": 666450000
  }
}
```

Returns: `reaction_left_kn`, `reaction_right_kn`, `max_shear_kn`, `max_moment_knm`, `max_deflection_mm`

**Halvard use case**: Verify deflection of a GL30h 90×315 glulam over 5.4m span against L/250 limit.

---

### `calculate_rectangular_concrete_section_summary`
Gross rectangular concrete section summary (no reinforcement, no cracking, no capacity check).

```json
{
  "name": "calculate_rectangular_concrete_section_summary",
  "arguments": {
    "width_mm": 300,
    "depth_mm": 500,
    "concrete_strength_mpa": 35
  }
}
```

**Halvard use case**: Foundation beam section properties for preliminary design.

---

## What It Does NOT Do (Yet)

- No Eurocode (NS-EN 1995, NS-EN 1993, NS-EN 1992) code checks
- No load combinations (1.35G + 1.5Q)
- No lateral-torsional buckling
- No reinforcement design
- No steel section database
- No unit conversion (inputs must match field names exactly)
- No interaction with Norwegian National Annexes

**Halvard workflow with this limitation**: Use the tool for deterministic statics, then apply Eurocode checks manually from `skills/structural-engineering.md`. The tool gives numbers; Halvard applies the code.

---

## Halvard Integration Protocol

When invoking this tool:

1. **State what you're calculating** before the tool call: *"Checking deflection of the proposed GL30h 90×315 beam at 5.4m span under design UDL of 12.0 kN/m."*
2. **Show the inputs** you're passing and why
3. **Interpret the output** against the TEK17/Eurocode limits: deflection limit = L/250 = 21.6 mm for this span
4. **State the result clearly**: pass or fail, with margin
5. **Flag** `WET_STAMP_REQUIRED` if the result is load-bearing and permit-relevant

---

## Installation

```bash
git clone https://github.com/Elandu/structural-analysis-mcp.git
cd structural-analysis-mcp
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -e ".[dev]"
```

Add to MCP client config (see `mcp/mcp-config.json`):
```json
{
  "mcpServers": {
    "structural-analysis": {
      "command": "python",
      "args": ["-m", "structural_analysis_mcp"]
    }
  }
}
```

---

## Roadmap (from Elandu)
- Steel section database
- Reinforced concrete interaction diagrams
- 2D frame analysis
- Load combinations
- Unit conversion
- Optional Australian Standards examples (Eurocode would require separate contribution)

*Note: Eurocode Norwegian national annex support would require a contribution to the Elandu project or a fork. This is the most valuable contribution Halvard's development could make to the open-source ecosystem.*

---

*Last reviewed: 2026-07-26*
