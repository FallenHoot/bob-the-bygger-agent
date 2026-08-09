# MCP Tool Specification: Norwegian Building Data MCP

**Status:** Specification — not yet built. APIs are confirmed open. Priority: HIGH.  
**Proposed name:** `norbygg-mcp`  
**Purpose:** Give Bob live, authoritative access to Norwegian building regulatory and geodata — replacing in-context knowledge approximations with real-time lookups from primary sources.  
**Last updated:** 2026-08-09

---

## Why This Exists

Every Norwegian-specific lookup Bob currently does from memory is a static approximation:
- "Lørenskog is probably in snow zone 2" → should be: query TEK17 snow map for coordinates
- "The site might have quick clay" → should be: query NGU kvikkleirekart for the property
- "Check NVE for flood zones" → should be: return the actual Q200 elevation for the coordinates

All of the APIs below are **open, no authentication required** (except Lovdata). Building this MCP server is the single highest-leverage improvement to Bob's accuracy and citability.

---

## Available Public APIs (Confirmed Open)

### 1. NVE Atlas — Flood, Landslide, Quick Clay Zones

**Base URL:** `https://atlas.nve.no/arcgis/rest/services/`  
**Format:** ArcGIS REST API (JSON, GeoJSON)  
**Auth:** None (public)

#### Available Services

| Service | Path | What it returns |
|---|---|---|
| Flood zones | `FlomAktsomhetsomrader/MapServer` | 10/100/200/500-year flood polygons |
| Quick clay risk zones | `Kvikkleire/MapServer` | NVE kvikkleire risk classification polygons |
| Landslide hazard | `Faresoner/MapServer` | Snow avalanche, rock slide, landslide zones |
| Storm surge | `Stormflo/MapServer` | Coastal storm surge zones |
| Debris flow | `Jordflomfare/MapServer` | Debris flow hazard zones |

#### Query Pattern (identify = point in polygon)

```http
GET https://atlas.nve.no/arcgis/rest/services/FlomAktsomhetsomrader/MapServer/identify
  ?geometry={"x":10.795,"y":59.894}
  &geometryType=esriGeometryPoint
  &sr=4326
  &layers=all
  &tolerance=0
  &mapExtent=10.793,59.892,10.797,59.896
  &imageDisplay=800,600,96
  &returnGeometry=false
  &f=json
```

**Response includes:** Flood zone class, return period, source dataset version

#### Python implementation:

```python
import requests

def check_nve_flood_zone(lon: float, lat: float) -> dict:
    """Check NVE flood zone for a coordinate (WGS84)."""
    base = "https://atlas.nve.no/arcgis/rest/services/FlomAktsomhetsomrader/MapServer/identify"
    params = {
        "geometry": f'{{"x":{lon},"y":{lat}}}',
        "geometryType": "esriGeometryPoint",
        "sr": "4326",
        "layers": "all",
        "tolerance": "1",
        "mapExtent": f"{lon-0.002},{lat-0.001},{lon+0.002},{lat+0.001}",
        "imageDisplay": "800,600,96",
        "returnGeometry": "false",
        "f": "json"
    }
    resp = requests.get(base, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    results = data.get("results", [])
    if not results:
        return {"status": "no_flood_zone", "message": "No flood zone found at this location"}
    return {
        "status": "flood_zone_found",
        "zones": [{"layer": r["layerName"], "attributes": r["attributes"]} for r in results]
    }

def check_nve_quick_clay(lon: float, lat: float) -> dict:
    """Check NVE quick clay risk zone for a coordinate."""
    base = "https://atlas.nve.no/arcgis/rest/services/Kvikkleire/MapServer/identify"
    params = {
        "geometry": f'{{"x":{lon},"y":{lat}}}',
        "geometryType": "esriGeometryPoint",
        "sr": "4326",
        "layers": "all",
        "tolerance": "1",
        "mapExtent": f"{lon-0.002},{lat-0.001},{lon+0.002},{lat+0.001}",
        "imageDisplay": "800,600,96",
        "returnGeometry": "false",
        "f": "json"
    }
    resp = requests.get(base, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    results = data.get("results", [])
    if not results:
        return {"status": "no_quick_clay_zone", "message": "Not in a mapped quick clay zone"}
    return {
        "status": "quick_clay_zone_found",
        "zones": [{"layer": r["layerName"], "attributes": r["attributes"]} for r in results],
        "escalation": "GEOTECHNICAL_REPORT_REQUIRED"
    }
```

---

### 2. NGU Map Services — Soil Types, Quick Clay Sensitivity, Radon, Bedrock

**Base URL:** `https://geo.ngu.no/mapserver/`  
**Format:** WMS (GetFeatureInfo) + WFS  
**Auth:** None (public)

#### Available WMS Services

| Service name | Endpoint path | What it returns |
|---|---|---|
| Løsmassekart (soil types) | `LosmasserkartWMS` | Quaternary deposits (clay, moraine, sand, rock) |
| Kvikkleirekart (quick clay) | `KvikkleirekartWMS` | NGU sensitivity classification (Low/Medium/High/Extra high) |
| Radon risk | `RadonWMS` | Ground radon risk class (Low/Medium/High) |
| Berggrunn (bedrock) | `BerggrunnWMS2` | Bedrock type and depth |
| Maringrense (marine limit) | `MarinGrenseWMS` | Maximum post-glacial sea level — below this line = marine clay risk |

#### WMS GetFeatureInfo Query Pattern

```python
import requests
from pyproj import Transformer

def ngu_get_feature_info(lon: float, lat: float, service: str, layer: str) -> dict:
    """Query NGU WMS GetFeatureInfo for a coordinate (WGS84 in, UTM33 internal)."""
    
    # NGU WMS services use EPSG:25833 (ETRS89/UTM33N)
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:25833", always_xy=True)
    x, y = transformer.transform(lon, lat)
    
    # Small bbox around the point
    delta = 100  # meters
    bbox = f"{x-delta},{y-delta},{x+delta},{y+delta}"
    
    # Pixel position of the query point within a 200x200 image
    i, j = 100, 100
    
    base = f"https://geo.ngu.no/mapserver/{service}"
    params = {
        "SERVICE": "WMS",
        "VERSION": "1.3.0",
        "REQUEST": "GetFeatureInfo",
        "LAYERS": layer,
        "QUERY_LAYERS": layer,
        "CRS": "EPSG:25833",
        "BBOX": bbox,
        "WIDTH": "200",
        "HEIGHT": "200",
        "I": str(i),
        "J": str(j),
        "INFO_FORMAT": "application/json",
        "FEATURE_COUNT": "5"
    }
    resp = requests.get(base, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()

def check_soil_type(lon: float, lat: float) -> dict:
    """Get soil type from NGU løsmassekart."""
    result = ngu_get_feature_info(lon, lat, "LosmasserkartWMS", "losmasse")
    features = result.get("features", [])
    if not features:
        return {"status": "no_data", "message": "No soil type data at this location"}
    props = features[0].get("properties", {})
    return {
        "status": "ok",
        "soil_type_code": props.get("JORDTYPE", "unknown"),
        "soil_type_name": props.get("JORDTYPE_NAVN", "unknown"),
        "source": "NGU løsmassekart"
    }

def check_quick_clay_ngu(lon: float, lat: float) -> dict:
    """Get quick clay sensitivity from NGU kvikkleirekart."""
    result = ngu_get_feature_info(lon, lat, "KvikkleirekartWMS", "kvikkleire")
    features = result.get("features", [])
    if not features:
        return {"status": "no_quick_clay", "message": "Not in NGU mapped quick clay zone"}
    props = features[0].get("properties", {})
    sensitivity = props.get("SENSITIVITET", "unknown")
    escalation = sensitivity in ["Høy", "Ekstra høy (kvikkleire)"]
    return {
        "status": "quick_clay_mapped",
        "sensitivity_class": sensitivity,
        "properties": props,
        "escalation": "GEOTECHNICAL_REPORT_REQUIRED" if escalation else None,
        "source": "NGU kvikkleirekart"
    }

def check_radon_risk(lon: float, lat: float) -> dict:
    """Get radon ground risk from NGU radonkart."""
    result = ngu_get_feature_info(lon, lat, "RadonWMS", "radon")
    features = result.get("features", [])
    if not features:
        return {"status": "no_data", "message": "No radon data at this location"}
    props = features[0].get("properties", {})
    risk_class = props.get("RISIKOKLASSE", "unknown")
    return {
        "status": "ok",
        "radon_risk_class": risk_class,  # Lav / Moderat / Høy
        "tek17_requirement": {
            "Lav": "Standard vapour barrier sufficient",
            "Moderat": "Radon membrane + sub-slab depressurization sleeve required",
            "Høy": "Full sub-slab depressurization system + membrane required"
        }.get(risk_class, "Verify at DSA"),
        "source": "NGU radonkart"
    }
```

---

### 3. Geonorge — Address Lookup, Property Data, Municipal Plans

**Base URL:** `https://ws.geonorge.no/`  
**Format:** REST/JSON  
**Auth:** None for most services (some require Geonorge API key — free registration)

#### Address Search (Matrikkel coordinates)

```python
def geonorge_address_to_coords(address: str, municipality: str = None) -> dict:
    """
    Convert Norwegian address to coordinates and matrikkel info.
    Returns: latitude, longitude, gnr, bnr, municipality code.
    """
    params = {"sok": address, "treffPerSide": "1", "side": "0"}
    if municipality:
        params["kommunenavn"] = municipality
    
    resp = requests.get(
        "https://ws.geonorge.no/adresser/v1/sok",
        params=params,
        timeout=10
    )
    resp.raise_for_status()
    data = resp.json()
    
    hits = data.get("adresser", [])
    if not hits:
        return {"status": "not_found", "message": f"Address not found: {address}"}
    
    addr = hits[0]
    representasjonspunkt = addr.get("representasjonspunkt", {})
    return {
        "status": "ok",
        "adressetekst": addr.get("adressetekst"),
        "kommunenavn": addr.get("kommunenavn"),
        "kommunenummer": addr.get("kommunenummer"),
        "lat": representasjonspunkt.get("lat"),
        "lon": representasjonspunkt.get("lon"),
        "gardsnummer": addr.get("gardsnummer"),
        "bruksnummer": addr.get("bruksnummer"),
        "postnummer": addr.get("postnummer"),
        "source": "Geonorge adressetjeneste"
    }
```

#### Elevation Data (Kartverket høydedata)

```python
def get_terrain_elevation(lon: float, lat: float) -> dict:
    """Get terrain elevation in meters above sea level from Kartverket."""
    resp = requests.get(
        "https://ws.geonorge.no/hoydedata/v1/punkt",
        params={"nord": lat, "ost": lon, "koordsys": "4326"},
        timeout=10
    )
    resp.raise_for_status()
    data = resp.json()
    return {
        "status": "ok",
        "elevation_moh": data.get("terreng", {}).get("z"),
        "source": "Kartverket høydedata"
    }
```

#### Municipal Plan Zone Lookup

```python
def get_plan_zone(lon: float, lat: float) -> dict:
    """
    Get municipal plan (reguleringsplan/kommuneplan) zone for coordinates.
    Uses the Arealplan WMS from Geonorge.
    """
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:25833", always_xy=True)
    x, y = transformer.transform(lon, lat)
    delta = 50
    bbox = f"{x-delta},{y-delta},{x+delta},{y+delta}"
    
    resp = requests.get(
        "https://openwms.statkart.no/skwms1/wms.arealplan",
        params={
            "SERVICE": "WMS",
            "VERSION": "1.3.0",
            "REQUEST": "GetFeatureInfo",
            "LAYERS": "reguleringsplan",
            "QUERY_LAYERS": "reguleringsplan",
            "CRS": "EPSG:25833",
            "BBOX": bbox,
            "WIDTH": "100", "HEIGHT": "100",
            "I": "50", "J": "50",
            "INFO_FORMAT": "application/json"
        },
        timeout=15
    )
    resp.raise_for_status()
    data = resp.json()
    features = data.get("features", [])
    if not features:
        return {"status": "no_plan_data", "message": "No regulatory plan data found"}
    return {
        "status": "ok",
        "plan_zones": [f["properties"] for f in features],
        "source": "Kartverket arealplan WMS"
    }
```

---

### 4. SEFRAK — Cultural Heritage Registry

**Base URL:** `https://kulturminnesok.no/`  
**API:** The SEFRAK data is available via Riksantikvaren's kulturminne API  
**Auth:** None (public read)

```python
def check_sefrak(gnr: int, bnr: int, municipality_code: str) -> dict:
    """
    Check if a property has SEFRAK-registered buildings.
    Uses Riksantikvaren's open API.
    """
    # Riksantikvaren cultural heritage API
    resp = requests.get(
        "https://ws.ra.no/kulturminnesok/api/kulturminne/sok",
        params={
            "type": "SEFRAK",
            "gardsnummer": gnr,
            "bruksnummer": bnr,
            "kommunenummer": municipality_code,
            "antall": 10
        },
        timeout=10
    )
    resp.raise_for_status()
    data = resp.json()
    
    results = data.get("kulturminner", [])
    if not results:
        return {
            "status": "not_sefrak_registered",
            "message": "No SEFRAK registration found for this property"
        }
    
    return {
        "status": "sefrak_registered",
        "count": len(results),
        "buildings": [
            {
                "sefrak_id": b.get("lokalId"),
                "building_type": b.get("bygningstype"),
                "estimated_year": b.get("anslatt_arstall"),
                "protection_status": b.get("vernestatus")
            }
            for b in results
        ],
        "escalation": "BYANTIKVAREN_CONSULTATION_REQUIRED",
        "source": "Riksantikvaren kulturminnesok"
    }
```

---

### 5. Lovdata (TEK17 Live Text)

**Status:** Requires licensing for full machine-readable access. Free web access only.  
**Base URL:** `https://lovdata.no/dokument/SF/forskrift/2017-06-19-840`

Lovdata does not provide a free programmatic API for regulation text. Options:
1. **Web scraping** — fragile, terms unclear
2. **Lovdata Pro API** — subscription required (law firms, municipalities)
3. **DiBK veiledning** — DiBK provides the guidance text at `dibk.no/regelverk/byggteknisk-forskrift-tek17` which is freely accessible

**Interim approach** — scrape DiBK's guidance page for specific sections:

```python
def get_tek17_guidance(section: str) -> dict:
    """
    Attempt to fetch TEK17 guidance text for a section from DiBK.
    Note: This is a web scrape — may break with DiBK site updates.
    """
    import urllib.parse
    anchor = section.replace("§", "").replace(" ", "-").replace(".", "-")
    url = f"https://www.dibk.no/regelverk/byggteknisk-forskrift-tek17/#{urllib.parse.quote(anchor)}"
    
    return {
        "status": "manual_lookup_required",
        "url": url,
        "message": f"TEK17 {section} — open this URL for authoritative current text. Machine-readable API requires Lovdata Pro subscription.",
        "note": "For BTBA in-context use: TEK17 is documented in skills/building-code-tek17/SKILL.md through 2026-08-09"
    }
```

---

## MCP Server Implementation

### Proposed Tool List

| Tool | Inputs | Output | Data source |
|---|---|---|---|
| `check_flood_zone` | lon, lat | Zone class, return period | NVE Atlas |
| `check_quick_clay_risk` | lon, lat | NGU sensitivity class + GEOTECHNICAL flag | NVE Atlas + NGU |
| `check_landslide_zone` | lon, lat | Hazard zone type | NVE Atlas |
| `check_soil_type` | lon, lat | Soil type (clay/moraine/rock/sand) | NGU løsmassekart |
| `check_radon_risk` | lon, lat | Risk class + TEK17 requirement | NGU radonkart |
| `check_sefrak` | gnr, bnr, municipality_code | Registration status + BYANTIKVAREN flag | Riksantikvaren |
| `address_to_coords` | address, municipality | lat, lon, gnr, bnr | Geonorge adresser |
| `get_elevation` | lon, lat | Elevation m.o.h. | Kartverket høydedata |
| `get_plan_zone` | lon, lat | Regulatory zone | Kartverket arealplan |
| `get_marine_limit` | lon, lat | Is site below marine limit? | NGU maringrense |

### Suggested Implementation Stack

```
norbygg-mcp/
├── server.py              # FastMCP server entry point
├── tools/
│   ├── nve.py             # NVE Atlas tools (flood, quick clay, landslide)
│   ├── ngu.py             # NGU tools (soil, quick clay sensitivity, radon)
│   ├── geonorge.py        # Geonorge tools (address, elevation, plan zone)
│   └── sefrak.py          # Riksantikvaren SEFRAK tool
├── cache/
│   └── cache.py           # Simple TTL cache (WMS responses are slow)
├── requirements.txt       # requests, pyproj, fastmcp, cachetools
└── README.md
```

**FastMCP skeleton:**

```python
from fastmcp import FastMCP
from tools.nve import check_flood_zone, check_quick_clay_risk
from tools.ngu import check_soil_type, check_radon_risk
from tools.geonorge import address_to_coords, get_elevation, get_plan_zone
from tools.sefrak import check_sefrak

mcp = FastMCP("norbygg-mcp")

@mcp.tool()
def flood_zone_check(address: str, municipality: str) -> dict:
    """Check NVE flood zone classification for a Norwegian address."""
    coords = address_to_coords(address, municipality)
    if coords["status"] != "ok":
        return coords
    return check_flood_zone(coords["lon"], coords["lat"])

@mcp.tool()
def full_site_risk_assessment(address: str, municipality: str) -> dict:
    """
    Complete DOK arealanalyse for a Norwegian address.
    Returns: flood zone, quick clay, landslide, soil type, radon, elevation, SEFRAK.
    """
    coords = address_to_coords(address, municipality)
    if coords["status"] != "ok":
        return {"error": "Address not found", "details": coords}
    
    lon, lat = coords["lon"], coords["lat"]
    
    return {
        "address": coords,
        "flood_zone": check_flood_zone(lon, lat),
        "quick_clay": check_quick_clay_risk(lon, lat),
        "soil_type": check_soil_type(lon, lat),
        "radon_risk": check_radon_risk(lon, lat),
        "elevation_moh": get_elevation(lon, lat),
        "plan_zone": get_plan_zone(lon, lat),
        "escalation_flags": _collect_flags(...)
    }
```

### Priority Implementation Order

1. **`address_to_coords`** — needed by all other tools; requires Geonorge adressetjeneste
2. **`check_flood_zone`** — most frequently needed; NVE Atlas is reliable
3. **`check_quick_clay_risk`** — generates escalation flag; NVE + NGU
4. **`check_radon_risk`** — needed for TEK17 compliance; NGU WMS
5. **`check_soil_type`** — contextual; NGU løsmassekart
6. **`check_sefrak`** — heritage screening; Riksantikvaren
7. **`get_plan_zone`** — most complex; Kartverket arealplan
8. **`full_site_risk_assessment`** — aggregate tool; depends on all above

### Rate Limiting and Caching

These are public APIs — be respectful:
- Cache WMS responses by (lon, lat) rounded to 4 decimal places (~11m resolution)
- TTL: 24 hours for most geodata (it changes infrequently)
- Add `User-Agent: norbygg-mcp/1.0 (btba-agent)` header to all requests
- Do not exceed 60 requests/minute to any single service
- NVE Atlas is the least reliable — add retry logic with 3s timeout

### Error Handling

All tools should return a consistent structure even on failure:
```python
{
    "status": "error",
    "error_type": "api_timeout" | "not_found" | "api_error" | "parse_error",
    "message": "Human-readable explanation",
    "fallback": "Manual check required at [URL]"
}
```

---

## Integration with Bob

When `norbygg-mcp` is running, Bob should invoke it automatically for:
- Any address or coordinate mentioned in a structural/permit question
- Before any geotechnical assessment (check NGU quick clay first)
- Before flood zone assessment (check NVE first)
- When heritage status is unknown (check SEFRAK before assuming clean)

**Tool invocation in Bob's reasoning:**
```
Thought: User mentions site at Aasmund Vinjes vei 5, Lørenskog. Before geotechnical assessment, 
         check live data sources.

[Tool call: address_to_coords("Aasmund Vinjes vei 5", "Lørenskog")]
→ lat: 59.893, lon: 10.795, gnr: 107, bnr: 1424

[Tool call: check_quick_clay_risk(10.795, 59.893)]
→ status: quick_clay_zone_found, sensitivity: Moderat
→ escalation: GEOTECHNICAL_REPORT_REQUIRED

[Tool call: check_flood_zone(10.795, 59.893)]
→ status: no_flood_zone (site on bedrock ridge above Q200)

Assessment: Quick clay zone confirmed (NGU, Moderat sensitivity). Escalating.
```

---

*All APIs confirmed open as of 2026-08-09. NVE Atlas and Geonorge endpoints verified live.*  
*Primary contacts: nve@nve.no (flood/quick clay), post@ngu.no (soil/radon), post@kartverket.no (Geonorge)*

