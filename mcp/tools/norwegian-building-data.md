# MCP Tool Specification: Norwegian Building Data MCP

**Status**: NOT YET BUILT — this is a specification document
**Proposed name**: `halvard-norbygg-mcp` (Norwegian Building Data MCP)
**Purpose**: Give Halvard live, authoritative access to Norwegian building regulatory and geodata, replacing in-context knowledge lookups with real-time data from primary sources.

**Why this should exist**: Every Norwegian-specific lookup Halvard does from memory (SEFRAK status, flood zones, radon risk, TEK17 text) is a static approximation. This MCP server would make those lookups exact, current, and citable.

---

## Proposed Tools

### 1. `get_tek17_section`
Fetch the current text of a specific TEK17 section directly from lovdata.no or the DiBK live text.

```json
{
  "name": "get_tek17_section",
  "arguments": {
    "chapter": 7,
    "section": "7-2"
  }
}
```

**Returns**: Current regulation text (forskriftstekst) + current guidance text (veiledning) for that section.

**Why**: TEK17 is amended regularly. The in-context skill reflects knowledge up to a training cutoff. This tool would always return the live authoritative text.

**Data source**: [lovdata.no](https://lovdata.no/dokument/SF/forskrift/2017-06-19-840) has machine-readable access via their API (requires licensing). DiBK's own website would be the fallback.

---

### 2. `check_sefrak`
Look up SEFRAK registration status for a property.

```json
{
  "name": "check_sefrak",
  "arguments": {
    "municipality_code": "0301",
    "gnr": 123,
    "bnr": 45
  }
}
```

**Returns**: SEFRAK registration status (yes/no), SEFRAK number if registered, building type, estimated construction year, protection level, any Byantikvaren notes on record.

**Why**: Every heritage assessment requires SEFRAK lookup. Currently Halvard tells users to check kulturminnesok.no manually. This tool does it automatically.

**Data source**: [kulturminnesok.no](https://kulturminnesok.no) and Riksantikvaren's [SEFRAK API](https://www.riksantikvaren.no/fagomrader/kart-og-register/) (public, REST).

---

### 3. `get_nve_hazards`
Get NVE-registered natural hazard information for a location.

```json
{
  "name": "get_nve_hazards",
  "arguments": {
    "latitude": 59.9139,
    "longitude": 10.7522
  }
}
```

**Returns**:
- Flood zone status (100-year and 1000-year return periods)
- Q200 water level (metres above sea level) for the nearest watercourse
- Landslide/avalanche risk classification
- Quick clay (kvikkleire) risk classification
- Coastal flood (stormflo) risk for coastal properties

**Why**: `NVE_CHECK_REQUIRED` and `GEOTECHNICAL_REPORT_REQUIRED` flags trigger constantly. Currently Halvard tells users to check nve.no. This tool triggers automatically on any foundation or siting question.

**Data source**: [NVE Kartkatalog REST API](https://www.nve.no/kartkatalog/) — publicly accessible, no auth required for basic queries.

---

### 4. `get_ngu_ground_conditions`
Get NGU geological ground condition data for a location.

```json
{
  "name": "get_ngu_ground_conditions",
  "arguments": {
    "latitude": 59.9139,
    "longitude": 10.7522,
    "radius_m": 100
  }
}
```

**Returns**:
- Superficial deposit type (løsmassetype): rock, moraine, clay, sand/gravel, marine sediments
- Quick clay (kvikkleire) susceptibility: none / low / medium / high / very high
- Bedrock type if applicable
- Recommended geotechnical investigation level

**Data source**: [NGU Løsmassekart REST API](https://www.ngu.no/kartkatalog/) — publicly accessible.

---

### 5. `get_radon_risk_zone`
Get DSA radon risk classification for a municipality or specific location.

```json
{
  "name": "get_radon_risk_zone",
  "arguments": {
    "municipality_code": "0301"
  }
}
```

**Returns**: Radon risk classification (low / medium / high), whether radon barrier is required under TEK17, recommended measurement approach.

**Data source**: [DSA Radonkart](https://www.dsa.no/radon/radonkart) — map available but no public API currently. Would require scraping or partnership.

---

### 6. `get_reguleringsplan`
Get the applicable zoning plan (reguleringsplan) details for a property.

```json
{
  "name": "get_reguleringsplan",
  "arguments": {
    "municipality_code": "0301",
    "gnr": 123,
    "bnr": 45
  }
}
```

**Returns**:
- Plan name and ID
- Arealformål (land use category)
- Allowed %-BYA
- Maximum building height
- Setback requirements
- Any hensynssoner (consideration zones) including heritage zones
- Any special conditions (bestemmelser)

**Data source**: [Geonorge.no plan API](https://www.geonorge.no/aktuelt/om-geonorge/api-og-nedlasting/) — Norway's national spatial data infrastructure. Most plan data is publicly accessible via OGC services.

---

### 7. `lookup_ns_standard`
Look up key values from Norwegian/Eurocode standards (where Standard Norge allows access).

```json
{
  "name": "lookup_ns_standard",
  "arguments": {
    "standard": "NS-EN 1991-1-3",
    "location": "Oslo",
    "query": "ground_snow_load"
  }
}
```

**Returns**: The applicable value (e.g., s_k = 2.5 kN/m² for Oslo) with Norwegian national annex reference.

**Note**: Standard Norge's content is paid/licensed. This tool would likely require a licensing agreement. May be better implemented as a curated lookup table within Halvard's own data rather than an external API.

---

## Implementation Notes

### Technology Stack (Recommended)
- **Python** with `mcp` library (same as Elandu's approach)
- **FastAPI** for any web service layer
- Authentication: None required for most Norwegian public APIs
- Hosting: Can run locally as stdio server, same pattern as structural-analysis-mcp

### Priority Order for Implementation
1. `check_sefrak` — highest immediate value, most commonly needed
2. `get_nve_hazards` — NVE and NGU APIs are clean and public
3. `get_ngu_ground_conditions` — pairs with NVE
4. `get_reguleringsplan` — more complex, Geonorge APIs vary by municipality
5. `get_tek17_section` — requires Lovdata API licensing
6. `get_radon_risk_zone` — requires DSA data agreement
7. `lookup_ns_standard` — requires Standard Norge licensing

### Quick Win Path
Tools 1–3 (SEFRAK, NVE, NGU) use public REST APIs with no authentication and could be prototyped in a weekend. This would immediately make Halvard's `NVE_CHECK_REQUIRED` and `BYANTIKVAREN_CONSULTATION_REQUIRED` flags backed by live data rather than user manual lookups.

---

## Competitive Context
As of 2026-07-26, **no public implementation of these tools exists**. 

- Catenda AI (in development) focuses on IFC model data, not regulatory/geodata
- DiBK has no developer API
- NVE, NGU, and Riksantikvaren have public APIs but no AI-ready MCP wrapper

**This is the white space.** Building even tools 1–3 would make Halvard the only Norwegian construction AI with live authoritative data grounding.

---

## Contribution Opportunity
The structural-analysis-mcp (Elandu) explicitly welcomes contributions. Adding Eurocode/Norwegian national annex load combination support to that project would be a natural complement to building this Norwegian data MCP.

See: [github.com/Elandu/structural-analysis-mcp/blob/main/CONTRIBUTING.md](https://github.com/Elandu/structural-analysis-mcp/blob/main/CONTRIBUTING.md)

---

*Last reviewed: 2026-07-26*
*Status: Specification only — not implemented*
