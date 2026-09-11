"""Local advisory detail validation, rectangular arithmetic and revision impact.

No CAD editing, network access, code execution, file writes or compliance decision.
CLI reads only explicit files inside --project-root and emits a report on stdout.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import sys
from xml.etree import ElementTree as ET

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/detail-package.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA)
DISCLAIMER = "Prepared by BTBA, AI advisory draft, not professional certification."
FIELDS = {
    "wall": {"length", "height", "thickness"},
    "opening": {"width", "height", "offset", "sill", "frame_width", "frame_height", "clear_width", "clear_height", "sash_projection"},
    "well": {"width", "projection", "bottom_level", "rim_level", "drain_invert"},
    "junction": set(),
}
FACTORS = {"mm": 1.0, "cm": 10.0, "m": 1000.0}
TOOL_VERSION = "1.1.0"
MIN_NONZERO_MM = 1e-6  # Numeric implementation bound, not a construction tolerance.
MAX_ABS_MM = 1e9
LAYER_ARITHMETIC_TOLERANCE_MM = 0.01


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_package(path, project_root):
    root = Path(project_root).resolve(strict=True)
    candidate = Path(path).resolve(strict=True)
    if not root.is_dir() or not candidate.is_relative_to(root):
        raise ValueError("Input must resolve inside the selected project root")
    if not candidate.is_file():
        raise ValueError("Input must be a regular file")
    with candidate.open("rb") as handle:
        raw = handle.read(2_000_001)
    if len(raw) > 2_000_000:
        raise ValueError("Input exceeds 2 MB limit")
    def reject_constant(value):
        raise ValueError(f"Nonfinite JSON constant: {value}")
    return json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object,
                      parse_constant=reject_constant)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    allow_nan=False, separators=(",", ":")).encode()).hexdigest()


def check_text(value):
    """Reject invalid XML/control text in input values and field names."""
    if isinstance(value, str):
        if any(not (ord(c) in (9, 10, 13) or 0x20 <= ord(c) <= 0xD7FF or
                    0xE000 <= ord(c) <= 0xFFFD or 0x10000 <= ord(c) <= 0x10FFFF) for c in value):
            raise ValueError("Unsupported control character in input text")
    elif isinstance(value, dict):
        for key, item in value.items():
            check_text(key)
            check_text(item)
    elif isinstance(value, list):
        for item in value:
            check_text(item)


def element_quantities(element):
    return list(element["fields"].items()) + [
        (f"layers/{index}/thickness", layer["thickness"])
        for index, layer in enumerate(element["layers"])
    ]


def validate(package):
    # JSON serialization rejects nonfinite values even for direct Python callers.
    check_text(package)
    digest(package)
    errors = sorted(VALIDATOR.iter_errors(package), key=lambda e: str(list(e.path)))
    if errors:
        raise ValueError("; ".join(f"{list(e.path)}: {e.message}" for e in errors[:10]))
    sources = {source["id"]: source for source in package["sources"]}
    elements = {element["id"]: element for element in package["elements"]}
    holds = {hold["id"]: hold for hold in package["holds"]}
    if len(sources) != len(package["sources"]) or len(elements) != len(package["elements"]) or len(holds) != len(package["holds"]):
        raise ValueError("Duplicate source, element or hold ID")
    if package["basis"] == "synthetic" and any(s["evidence_status"] != "synthetic" for s in sources.values()):
        raise ValueError("Synthetic package sources must remain synthetic")
    if package["basis"] == "project_advisory" and any(s["evidence_status"] == "synthetic" for s in sources.values()):
        raise ValueError("Synthetic sources cannot be relabeled as project evidence")
    for element in elements.values():
        kind = element["kind"]
        if set(element["fields"]) != FIELDS[kind]:
            raise ValueError(f"{element['id']}: expected fields {sorted(FIELDS[kind])}")
        deps = element["depends_on"]
        if any(dep not in elements for dep in deps) or element["id"] in deps:
            raise ValueError("Missing or self-referencing dependency")
        if kind in ("opening", "well"):
            expected = "wall" if kind == "opening" else "opening"
            if len(deps) != 1 or elements[deps[0]]["kind"] != expected:
                raise ValueError(f"{kind} needs exactly one {expected} dependency")
        if kind != "wall" and element["layers"]:
            raise ValueError("Only walls can declare layer stacks")
        for name, quantity in element_quantities(element):
            if name in ("bottom_level", "rim_level", "drain_invert") and not quantity.get("datum"):
                raise ValueError("Levels require an explicit datum, including unknown levels")
            if any(s not in sources for s in quantity["source_ids"]):
                raise ValueError("Unknown source reference")
            value = quantity["value"]
            refs = quantity.get("evidence_refs", [])
            if refs and {r["source_id"] for r in refs} != set(quantity["source_ids"]):
                raise ValueError("Evidence locators must match declared source IDs")
            if package["basis"] == "project_advisory":
                if quantity["status"] == "synthetic":
                    raise ValueError("Synthetic quantities cannot be promoted to project evidence")
                if value is not None and not refs:
                    raise ValueError("Project quantities require exact evidence_refs locators")
            if quantity["status"] in ("annotated", "measured") and any(
                sources[s]["evidence_status"] in ("reported", "proposed", "unverified", "synthetic")
                for s in quantity["source_ids"]
            ):
                raise ValueError("Annotated/measured values require documented source status; labels remain unverified")
            if package["basis"] == "synthetic" and value is not None and quantity["status"] != "synthetic":
                raise ValueError("Synthetic numbers cannot be promoted to observed evidence")
            if value is not None:
                try:
                    finite = math.isfinite(value)
                except OverflowError as exc:
                    raise ValueError("Quantity exceeds supported numeric range") from exc
                if isinstance(value, bool) or not finite:
                    raise ValueError("Quantity must be a finite number")
                if name not in ("bottom_level", "rim_level", "drain_invert") and value < 0:
                    raise ValueError("Lengths cannot be negative")
                if name not in ("offset", "sill", "sash_projection", "bottom_level", "rim_level", "drain_invert") and value == 0:
                    raise ValueError("Dimensions must be positive")
                normalized = value * FACTORS[quantity["unit"]]
                if not math.isfinite(normalized) or abs(normalized) > MAX_ABS_MM:
                    raise ValueError("Quantity exceeds supported local geometry range")
                if value != 0 and abs(normalized) < MIN_NONZERO_MM:
                    raise ValueError("Quantity below supported nonzero numeric range")
        if kind == "well" and len({q["datum"] for n,q in element["fields"].items() if n in ("bottom_level", "rim_level", "drain_invert")}) != 1:
            raise ValueError("Well levels must use the same declared datum; transform evidence required before comparison")
    visiting, visited = set(), set()
    def visit(key):
        if key in visiting:
            raise ValueError("Dependency cycle")
        if key in visited:
            return
        visiting.add(key)
        for dep in elements[key]["depends_on"]:
            visit(dep)
        visiting.remove(key)
        visited.add(key)
    for key in elements:
        visit(key)
    for hold in holds.values():
        if any(key not in elements for key in hold["elements"]):
            raise ValueError("Hold references missing element")
    return elements


def mm(quantity):
    return None if quantity["value"] is None else quantity["value"] * FACTORS[quantity["unit"]]


def assess(package):
    elements = validate(package)
    checks, quantities = [], []
    reasons = {
        "layer_total_matches_wall": "Layer total differs from wall thickness within the fixed arithmetic comparison tolerance.",
        "opening_deductions_known_nonoverlapping": "Structural opening rectangles overlap; net area is withheld.",
        "rectangular_opening_inside_wall": "Opening rectangle extends outside the supplied wall face.",
        "opening_frame_clear_width": "Clear, frame and structural opening widths are not ordered consistently.",
        "opening_frame_clear_height": "Clear, frame and structural opening heights are not ordered consistently.",
        "positive_well_depth": "Rim must be above bottom on the common datum.",
        "projection_minus_sash_nonnegative": "Simplified sash projection exceeds the well projection.",
        "well_opening_alignment": "Well placement relative to the opening is not modeled.",
    }
    def check(key, rule, passed, inputs, *, input_elements=None, reason=None):
        referenced = input_elements or [key]
        refs = [{"element": k, "field": field, "source_ids": q["source_ids"],
                 "evidence_refs": q.get("evidence_refs", []), "evidence_status": q["status"]}
                for k in referenced for field,q in element_quantities(elements[k])]
        checks.append({"element": key, "rule": rule, "rule_version": "1.1",
                       "inputs_mm": inputs, "input_refs": refs,
                       "reason": reason if reason else "Required inputs or valid geometry unavailable." if passed is None else reasons[rule] if not passed else None,
                       "status": "not_assessed" if passed is None else "consistent" if passed else "discrepancy"})
    for key, element in elements.items():
        f = {name: mm(value) for name, value in element["fields"].items()}
        if element["kind"] == "wall":
            layers = [mm(layer["thickness"]) for layer in element["layers"]]
            total = math.fsum(layers) if layers and all(x is not None for x in layers) else None
            check(key, "layer_total_matches_wall", None if total is None or f["thickness"] is None else math.isclose(total, f["thickness"], rel_tol=0, abs_tol=LAYER_ARITHMETIC_TOLERANCE_MM), {"layers": total, "wall": f["thickness"], "arithmetic_tolerance_not_installation_tolerance": LAYER_ARITHMETIC_TOLERANCE_MM})
            openings = [e for e in elements.values() if e["kind"] == "opening" and key in e["depends_on"]]
            rects = []
            if f["length"] is not None and f["height"] is not None:
                for opening in openings:
                    of = {n: mm(q) for n, q in opening["fields"].items()}
                    vals = [of[n] for n in ("offset", "sill", "width", "height")]
                    if any(x is None for x in vals):
                        rects = None
                        break
                    x, y, w, h = vals
                    if x + w > f["length"] or y + h > f["height"]:
                        rects = None
                        break
                    rects.append((x, y, w, h))
            else:
                rects = None
            overlap = rects is not None and any(a[0] < b[0]+b[2] and b[0] < a[0]+a[2] and a[1] < b[1]+b[3] and b[1] < a[1]+a[3] for i,a in enumerate(rects) for b in rects[i+1:])
            net = None if rects is None or overlap else (f["length"]*f["height"] - sum(w*h for _,_,w,h in rects))/1e6
            dependencies = [key] + [e["id"] for e in openings]
            quantities.append({"element": key, "input_elements": dependencies, "net_face_area_m2": net, "method": "rectangular face minus nonoverlapping structural openings; one face only", "status": "not_assessed" if net is None else "derived_arithmetic_only"})
            check(key, "opening_deductions_known_nonoverlapping", None if rects is None else not overlap, {}, input_elements=dependencies)
        elif element["kind"] == "opening":
            wall = elements[element["depends_on"][0]]
            wf = {n: mm(q) for n,q in wall["fields"].items()}
            values = [f[n] for n in ("offset", "sill", "width", "height")] + [wf["length"], wf["height"]]
            check(key, "rectangular_opening_inside_wall", None if any(v is None for v in values) else f["offset"]+f["width"] <= wf["length"] and f["sill"]+f["height"] <= wf["height"], {**f, "wall_length": wf["length"], "wall_height": wf["height"]}, input_elements=[key, wall["id"]])
            for axis in ("width", "height"):
                vals = [f[axis], f["frame_"+axis], f["clear_"+axis]]
                check(key, "opening_frame_clear_"+axis, None if any(v is None for v in vals) else vals[2] <= vals[1] <= vals[0], dict(zip(("structural", "frame", "clear"),vals)))
        elif element["kind"] == "well":
            depth = None if f["rim_level"] is None or f["bottom_level"] is None else f["rim_level"]-f["bottom_level"]
            check(key, "positive_well_depth", None if depth is None else depth > 0, {"depth": depth})
            opening = elements[element["depends_on"][0]]
            sash = mm(opening["fields"]["sash_projection"])
            residual = None if sash is None or f["projection"] is None else f["projection"]-sash
            check(key, "projection_minus_sash_nonnegative", None if residual is None else residual >= 0, {"residual": residual}, input_elements=[key, opening["id"]])
            check(key, "well_opening_alignment", None,
                {"well_width": f["width"], "opening_clear_width": mm(opening["fields"]["clear_width"])},
                input_elements=[key, opening["id"]],
                reason="Well offset/alignment, full sash sweep, cover/ladder and access geometry are not modeled; widths alone cannot verify fit or escape.")
            quantities.append({"element": key, "depth_mm": depth, "projection_minus_sash_mm": residual,
                               "status": "arithmetic_only_not_escape_or_drainage_approval"})
    unknowns = [{"element": key, "field": name, "reason": q["note"]} for key,e in elements.items() for name,q in element_quantities(e) if q["value"] is None]
    return copy.deepcopy({"schema_version": 1, "tool_version": TOOL_VERSION, "package_id": package["package_id"], "revision": package["revision"],
            "basis": package["basis"], "source_manifest": package["sources"],
            "input_elements": package["elements"],
            "input_sha256": digest(package), "disclaimer": DISCLAIMER, "status": "draft_not_for_construction",
            "design_compliance": "not_assessed", "release": "not_authorized", "checks": checks,
            "quantities": quantities, "unknowns": unknowns, "holds": package["holds"],
            "limits": ["Source labels/locators/hashes are not independently verified.", "Rectangular geometry only; no support, moisture, escape, drainage or code design.", "No installation tolerances, cover/ladder obstructions or product fit design.", "This tool cannot close professional or authority holds."]})


ABSENT = object()


def field_changes(before, after, path=""):
    """JSON-pointer differences; distinguish an absent value from JSON null."""
    if isinstance(before, dict) and isinstance(after, dict):
        for key in sorted(before.keys() | after.keys()):
            escaped = key.replace("~", "~0").replace("/", "~1")
            yield from field_changes(before.get(key, ABSENT), after.get(key, ABSENT), path + "/" + escaped)
    elif isinstance(before, list) and isinstance(after, list):
        for index in range(max(len(before), len(after))):
            yield from field_changes(before[index] if index < len(before) else ABSENT,
                                     after[index] if index < len(after) else ABSENT, path + "/" + str(index))
    elif before != after:
        def state(value):
            return {"present": False} if value is ABSENT else {"present": True, "value": copy.deepcopy(value)}
        yield {"path": path or "/", "before": state(before), "after": state(after)}


def revision_impact(before, after):
    old, new = validate(before), validate(after)
    if before["package_id"] != after["package_id"]:
        raise ValueError("Cannot compare different package identities")
    if before["revision"] == after["revision"] and before != after:
        raise ValueError("Changed package must have a new revision")
    old_sources = {s["id"]: s for s in before["sources"]}
    new_sources = {s["id"]: s for s in after["sources"]}
    changed_sources = {s for s in old_sources.keys() | new_sources.keys() if old_sources.get(s) != new_sources.get(s)}
    changed = {key for key in old.keys() | new.keys() if old.get(key) != new.get(key)}
    old_holds = {h["id"]: h for h in before["holds"]}
    new_holds = {h["id"]: h for h in after["holds"]}
    changed_holds = {key for key in old_holds.keys() | new_holds.keys() if old_holds.get(key) != new_holds.get(key)}
    changes = []
    metadata = ("revision", "basis", "scope", "status")
    changes.extend({"record_type": "package", "record_id": before["package_id"], **change}
                   for change in field_changes({key: before[key] for key in metadata},
                                               {key: after[key] for key in metadata}))
    for record_type, old_map, new_map in (("element", old, new), ("source", old_sources, new_sources), ("hold", old_holds, new_holds)):
        for key in sorted(old_map.keys() | new_map.keys()):
            changes.extend({"record_type": record_type, "record_id": key, **change}
                           for change in field_changes(old_map.get(key, ABSENT), new_map.get(key, ABSENT)))
    if any(before[k] != after[k] for k in ("basis", "scope")):
        changed.update(old.keys() | new.keys())
    for elements in (old, new):
        for key,e in elements.items():
            qs = list(e["fields"].values()) + [layer["thickness"] for layer in e["layers"]]
            if any(changed_sources.intersection(q["source_ids"]) for q in qs):
                changed.add(key)
    impacted = set(changed)
    for key in changed_holds:
        impacted.update(old_holds.get(key, {}).get("elements", []))
        impacted.update(new_holds.get(key, {}).get("elements", []))
    # Both dependency graphs matter when an element is removed or reparented.
    while True:
        prior = set(impacted)
        for elements in (old, new):
            for key,e in elements.items():
                if impacted.intersection(e["depends_on"]):
                    impacted.add(key)
                # Opening geometry also contributes to its parent wall's net quantity.
                if key in impacted and e["kind"] == "opening":
                    impacted.update(e["depends_on"])
        if prior == impacted:
            break
    return {"schema_version": 1, "tool_version": TOOL_VERSION, "before_sha256": digest(before), "after_sha256": digest(after),
            "changes": changes, "changed_holds": sorted(changed_holds),
            "removed_holds": sorted(old_holds.keys() - new_holds.keys()),
            "hold_review": "required_not_closed" if changed_holds else "no_hold_change",
            "before_revision": before["revision"], "after_revision": after["revision"],
            "changed_sources": sorted(changed_sources), "changed_elements": sorted(changed),
            "requires_revalidation": sorted(impacted), "holds_changed": bool(changed_holds),
            "release": "not_authorized", "note": "Conservative dependency impact; no files changed or holds closed."}


def render_svg(package):
    """Deterministic single-wall preview, not a construction or escape drawing."""
    elements = validate(package)
    walls = [e for e in elements.values() if e["kind"] == "wall"]
    openings = [e for e in elements.values() if e["kind"] == "opening"]
    wells = [e for e in elements.values() if e["kind"] == "well"]
    if len(walls) != 1 or len(openings) != 1 or len(wells) != 1:
        raise ValueError("Preview supports exactly one wall, opening and well")
    wall, opening, well = walls[0], openings[0], wells[0]
    wf = {n: mm(q) for n,q in wall["fields"].items()}
    of = {n: mm(q) for n,q in opening["fields"].items()}
    lf = {n: mm(q) for n,q in well["fields"].items()}
    needed = [wf["length"], wf["height"], of["width"], of["height"], of["offset"], of["sill"],
              of["sash_projection"], lf["width"], lf["projection"], lf["rim_level"], lf["bottom_level"]]
    if any(v is None for v in needed):
        raise ValueError("Preview requires evidenced geometry; unknown dimensions are not drawn as zero")
    result = assess(package)
    if any(c["status"] == "discrepancy" for c in result["checks"]):
        raise ValueError("Resolve geometry discrepancies before rendering a preview")
    svg = ET.Element("svg", {"xmlns": "http://www.w3.org/2000/svg", "viewBox": "0 0 1000 800", "role": "img"})
    ET.SubElement(svg, "title").text = "BTBA advisory geometry preview — not for construction"
    ET.SubElement(svg, "rect", {"width": "1000", "height": "800", "fill": "#f8fafc"})
    def text(x, y, value, size=15):
        full = " ".join(str(value).split())
        maximum = min(110, int((970 - x) / (size * 0.6)))
        short = full if len(full) <= maximum else full[:maximum-23] + "… [full record in JSON]"
        node = ET.SubElement(svg, "text", {"x": str(x), "y": str(y), "font-family": "sans-serif",
                                         "font-size": str(size), "fill": "#172554"})
        node.text = short
        if short != full:
            ET.SubElement(node, "title").text = full
    def rect(x,y,w,h,fill):
        ET.SubElement(svg, "rect", {"x": str(x), "y": str(y), "width": str(w), "height": str(h),
                                   "fill": fill, "stroke": "#334155", "stroke-width": "2"})
    text(30,35,"BTBA | DRAFT GEOMETRY PREVIEW — NOT FOR CONSTRUCTION",21)
    text(30,62,f"{package['package_id']} / {package['revision']} / {package['basis']}")
    text(30,87,"Schematic layout; use stated mm dimensions. No engineering, escape or drainage approval.")
    text(30,125,f"Wall elevation {wall['id']} — opening {opening['id']}",18)
    scale = min(520/wf["length"], 230/wf["height"])
    x,y = 40,155
    rect(x,y,wf["length"]*scale,wf["height"]*scale,"#cbd5e1")
    rect(x+of["offset"]*scale,y+(wf["height"]-of["sill"]-of["height"])*scale,
         of["width"]*scale,of["height"]*scale,"#dbeafe")
    text(40,410,f"Wall {wf['length']:g} × {wf['height']:g} mm; opening {of['width']:g} × {of['height']:g} mm")
    text(40,435,f"Offset {of['offset']:g} mm; sill {of['sill']:g} mm above declared wall origin")
    text(620,125,f"Well plan {well['id']}",18)
    scale = min(310/lf["width"],230/lf["projection"])
    rect(620,155,lf["width"]*scale,lf["projection"]*scale,"#e0f2fe")
    rect(620,155,lf["width"]*scale,of["sash_projection"]*scale,"#fed7aa")
    text(620,410,f"Clear {lf['width']:g} × {lf['projection']:g} mm")
    text(620,435,f"Sash envelope {of['sash_projection']:g} mm")
    text(30,485,"Well level section — declared common datum",18)
    depth = lf["rim_level"]-lf["bottom_level"]
    scale = min(360/lf["projection"],160/depth)
    rect(40,510,lf["projection"]*scale,depth*scale,"#e0f2fe")
    text(420,535,f"Rim {lf['rim_level']:g} mm; bottom {lf['bottom_level']:g} mm")
    text(420,562,f"Depth {depth:g} mm; datum: {well['fields']['rim_level']['datum']}")
    text(420,589,"Drain outlet/invert, retaining, waterproofing and access: review required")
    text(30,715,f"Open holds: {len(package['holds'])}; source labels not independently verified")
    text(30,741,f"Input SHA-256: {digest(package)}",12)
    text(30,770,DISCLAIMER,13)
    return ET.tostring(svg, encoding="unicode")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--compare-to", help="Later revision inside the same selected root")
    parser.add_argument("--format", choices=("json", "svg"), default="json")
    args = parser.parse_args()
    try:
        package = read_package(args.input, args.project_root)
        if args.format == "svg":
            if args.compare_to:
                raise ValueError("Revision comparison only supports JSON")
            print(render_svg(package))
            return 0
        result = revision_impact(package, read_package(args.compare_to, args.project_root)) if args.compare_to else assess(package)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        return 0
    except (ValueError, OSError, TypeError, RecursionError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())