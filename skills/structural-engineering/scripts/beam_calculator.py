"""Local, preliminary Euler-Bernoulli beam response; not a code design checker.

Run with --input <JSON file>, or pass a decoded object to analyse(). Only
explicitly supported units and downward nonnegative loads are accepted.
No network access, file writes, material presets, or automatic load factors.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

import pint


VERSION = "1.0.0"
DISCLAIMER = "Prepared by BTBA, AI advisory draft, not professional certification."
UNITS = pint.UnitRegistry()
# An allowlist avoids evaluating arbitrary unit expressions from input JSON.
UNIT_SETS = {
    "length": ({"mm", "cm", "m", "in", "ft"}, "mm"),
    "force": ({"N", "kN", "lbf", "kip"}, "N"),
    "line_load": ({"N/mm", "N/m", "kN/m", "lbf/ft", "kip/ft"}, "N/mm"),
    "modulus": ({"Pa", "MPa", "GPa", "N/mm^2", "psi", "ksi"}, "N/mm^2"),
    "inertia": ({"mm^4", "cm^4", "m^4", "in^4", "ft^4"}, "mm^4"),
}
LIMITATIONS = [
    "Ideal single span, constant E and I, small-deflection linear-elastic bending only.",
    "One downward point load or full-span UDL; no automatic self-weight or combinations.",
    "No shear deformation, creep, cracking, vibration, stability, strength or fire checks.",
    "No connection, bearing, foundation, temporary-works or installed-condition verification.",
    "No Norwegian National Annex coefficients or automatic compliance decision.",
    "Source labels and user-supplied criteria are recorded, not independently verified.",
    "A qualified structural designer must review the design basis before consequential use.",
]


def fields(value: Any, required: set[str], optional: set[str], name: str) -> dict:
    """Reject omissions and unknown fields (including misspelled units/load types)."""
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    missing = required - value.keys()
    extra = value.keys() - required - optional
    if missing or extra:
        raise ValueError(f"{name}: missing={sorted(missing)}, unknown={sorted(extra)}")
    return value


def number(value: Any, name: str, *, positive: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number, not text or boolean")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(f"{name} exceeds numeric range") from exc
    if not math.isfinite(result) or result < 0 or (positive and result == 0):
        bound = "positive" if positive else "nonnegative"
        raise ValueError(f"{name} must be finite and {bound}")
    return result


def text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be nonempty text")
    return value.strip()


def choice(value: Any, options: tuple[str, ...], name: str) -> str:
    if not isinstance(value, str) or value not in options:
        raise ValueError(f"{name} must be one of {options}")
    return value


def quantity(value: Any, kind: str, name: str, *, positive: bool = False) -> float:
    item = fields(value, {"value", "unit"}, set(), name)
    magnitude = number(item["value"], name, positive=positive)
    allowed, target = UNIT_SETS[kind]
    if not isinstance(item["unit"], str) or item["unit"] not in allowed:
        raise ValueError(f"{name}: expected {kind} unit from {sorted(allowed)}")
    converted = UNITS.Quantity(magnitude, item["unit"]).to(target).magnitude
    if magnitude > 0 and converted == 0:
        raise ValueError(f"{name} underflows during unit conversion")
    return number(converted, f"{name} after conversion", positive=positive)


def normalize(payload: Any) -> dict:
    data = fields(payload, {"schema_version", "support", "span", "elastic_modulus",
                           "second_moment", "load", "basis"}, {"criterion"}, "input")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError("schema_version must be integer 1")
    support = choice(data["support"], ("simply_supported", "cantilever"), "support")
    span = quantity(data["span"], "length", "span", positive=True)
    modulus = quantity(data["elastic_modulus"], "modulus", "elastic_modulus", positive=True)
    inertia = quantity(data["second_moment"], "inertia", "second_moment", positive=True)
    load = fields(data["load"], {"kind", "magnitude"}, {"position"}, "load")
    kind = choice(load["kind"], ("point", "udl"), "load.kind")
    magnitude = quantity(load["magnitude"], "force" if kind == "point" else "line_load",
                         "load.magnitude")
    position = None
    if kind == "point":
        if "position" not in load:
            raise ValueError("Point load requires position measured from the left end")
        position = quantity(load["position"], "length", "load.position")
        if position > span:
            raise ValueError("Point-load position must be within [0, span]; inputs are not clamped")
    elif "position" in load:
        raise ValueError("Full-span UDL cannot have a point-load position")
    basis = fields(data["basis"], {"source", "geometry_and_supports", "material_and_axis",
                                   "load_basis", "combination", "self_weight"}, set(), "basis")
    basis = {key: text(val, f"basis.{key}") for key, val in basis.items()}
    choice(basis["load_basis"], ("illustrative", "SLS", "ULS"), "basis.load_basis")
    choice(basis["self_weight"], ("included", "excluded", "unknown"), "basis.self_weight")
    criterion = None
    if "criterion" in data:
        c = fields(data["criterion"], {"span_ratio", "source", "evidence_status", "component"},
                   set(), "criterion")
        criterion = {
            "span_ratio": number(c["span_ratio"], "criterion.span_ratio", positive=True),
            "source": text(c["source"], "criterion.source"),
            "evidence_status": choice(c["evidence_status"],
                                      ("illustrative", "user_supplied", "unverified"),
                                      "criterion.evidence_status"),
            "component": choice(c["component"], ("elastic_load_case",), "criterion.component"),
        }
    return {"support": support, "span_mm": span, "elastic_modulus_n_mm2": modulus,
            "second_moment_mm4": inertia, "load_kind": kind,
            "load_n" if kind == "point" else "load_n_mm": magnitude,
            "position_mm": position, "basis": basis, "criterion": criterion}


def solve(n: dict) -> dict:
    """Analytical response in N/mm; no mesh-based extrema or code criteria."""
    L = n["span_mm"]
    E = n["elastic_modulus_n_mm2"]
    I = n["second_moment_mm4"]
    EI = number(E * I, "EI", positive=True)
    # Reject overflow/underflow in the geometric powers, not plausible-looking zeros.
    for power in (2, 3, 4):
        number(L ** power, f"span^{power}", positive=True)
    simple = n["support"] == "simply_supported"
    point = n["load_kind"] == "point"
    a = n["position_mm"] if point else L
    b = L - a
    load = n["load_n"] if point else n["load_n_mm"]
    total = load if point else load * L
    right = (load * a / L if point else total / 2) if simple else 0.0
    left = (load * b / L if point else total / 2) if simple else total
    reaction_moment = 0.0 if simple else total * (a if point else L / 2)

    def at(x: float) -> dict:
        if point:
            moment = left * x - reaction_moment - load * max(x - a, 0.0)
            before = left - (load if x > a else 0.0)
            after = left - (load if x >= a else 0.0)
            if simple:
                if x <= a:
                    deflection = load * b * x * (L * L - b * b - x * x) / (6 * L) / EI
                else:
                    z = L - x
                    deflection = load * a * z * (L * L - a * a - z * z) / (6 * L) / EI
            elif x <= a:
                deflection = load * x * x * (3 * a - x) / 6 / EI
            else:
                deflection = load * a * a * (3 * x - a) / 6 / EI
        else:
            moment = left * x - reaction_moment - load * x * x / 2
            before = after = left - load * x
            if simple:
                deflection = load * x * (L**3 - 2 * L * x*x + x**3) / 24 / EI
            else:
                deflection = load * x*x * (6 * L*L - 4 * L*x + x*x) / 24 / EI
        # At endpoints report the interior limit, not a zero-length region
        # between a support reaction and a collocated point load.
        if x == 0:
            before = after
        if x == L:
            after = before
        return {"x_mm": x, "moment_kn_m": moment / 1e6,
                "shear_before_load_kn": before / 1000, "shear_after_load_kn": after / 1000,
                "deflection_down_mm": deflection}

    if not simple:
        x_deflection = L
    elif not point:
        x_deflection = L / 2
    elif a == 0 or b == 0 or load == 0:
        x_deflection = 0.0  # Identically zero curve; deterministic representative location.
    elif a <= L / 2:
        x_deflection = L - math.sqrt((L*L - a*a) / 3)
    else:
        x_deflection = math.sqrt((L*L - b*b) / 3)
    x_moment = (a if point else L / 2) if simple else 0.0
    maximum = at(x_deflection)["deflection_down_mm"]
    moment_max = abs(at(x_moment)["moment_kn_m"])
    shear_max = max(abs(left), abs(right)) / 1000
    if point and (a == 0 or (simple and a == L)):
        shear_max = 0.0  # Load is transferred directly at a support.
    elif load > 0:
        # A nonzero downward load acting on the span has positive response
        # magnitudes. Reject numerical collapse rather than imply no movement.
        number(maximum, "nonzero-load deflection", positive=True)
        number(moment_max, "nonzero-load moment", positive=True)
        number(shear_max, "nonzero-load shear", positive=True)
    positions = sorted({L * i / 40 for i in range(41)} | {a, x_deflection, x_moment})
    if simple and not point:
        formula = "5*q*L^4/(384*E*I)"
        substituted = f"5*{load}*{L}^4/(384*{E}*{I})"
    elif simple:
        x = x_deflection
        # Use the appropriate side of the point load; maximum need not be at a.
        c, z = (b, x) if x <= a else (a, L - x)
        formula = "P*c*z*(L^2-c^2-z^2)/(6*L*E*I); (c,z)=(b,x) or (a,L-x)"
        substituted = f"{load}*{c}*{z}*({L}^2-{c}^2-{z}^2)/(6*{L}*{E}*{I})"
    elif point:
        formula = "P*a^2*(3*L-a)/(6*E*I)"
        substituted = f"{load}*{a}^2*(3*{L}-{a})/(6*{E}*{I})"
    else:
        formula = "q*L^4/(8*E*I)"
        substituted = f"{load}*{L}^4/(8*{E}*{I})"
    return {
        "reaction_left_up_kn": left / 1000,
        "reaction_right_up_kn": right / 1000 if simple else None,
        "reaction_moment_left_ccw_kn_m": reaction_moment / 1e6,
        "max_abs_shear_kn": shear_max,
        "max_abs_moment_kn_m": moment_max, "max_abs_moment_at_mm": x_moment,
        "max_deflection_down_mm": maximum, "max_deflection_at_mm": x_deflection,
        "deflection_formula": formula, "deflection_substitution": substituted,
        "substitution_units": "P=N; q=N/mm; L,a,b,c,x,z=mm; E=N/mm^2; I=mm^4; result=mm",
        "sign_convention": "Downward deflection positive; sagging moment positive; dM/dx=V. "
                           "Reactions upward/CCW positive. Endpoint shears are interior limits.",
        "stations": [at(x) for x in positions],
    }


def compare(n: dict, response: dict) -> dict:
    c = n["criterion"]
    if c is None:
        return {"status": "not_assessed", "reason": "No sourced deflection criterion supplied"}
    if c["evidence_status"] == "unverified":
        return {"status": "not_assessed", "reason": "Criterion unverified"}
    if n["basis"]["load_basis"] == "ULS":
        return {"status": "not_assessed", "reason": "ULS load case is not an SLS deflection check"}
    if n["basis"]["self_weight"] == "unknown":
        return {"status": "not_assessed", "reason": "Self-weight inclusion is unknown"}
    allowable = number(n["span_mm"] / c["span_ratio"], "allowable deflection", positive=True)
    actual = response["max_deflection_down_mm"]
    return {"status": "arithmetic_within_supplied_limit" if actual <= allowable
            else "arithmetic_exceeds_supplied_limit", "allowable_mm": allowable,
            "ratio_of_limit": actual / allowable,
            "scope": "Elastic listed load case only; not code compliance or member adequacy"}


def ensure_finite(value: Any) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("Calculation exceeds finite numeric range")
    if isinstance(value, dict):
        for item in value.values():
            ensure_finite(item)
    elif isinstance(value, list):
        for item in value:
            ensure_finite(item)


def analyse(payload: Any) -> dict:
    """Validate a JSON-compatible input and return a reproducible advisory report."""
    try:
        n = normalize(payload)
        response = solve(n)
        report = {"schema_version": 1, "calculator_version": VERSION,
                  "status": "preliminary_elastic_analysis", "disclaimer": DISCLAIMER,
                  "design_compliance": "not_assessed", "input": payload,
                  "normalized": n, "response": response,
                  "deflection_comparison": compare(n, response), "limitations": LIMITATIONS.copy()}
        ensure_finite(report)
        return report
    except (OverflowError, ZeroDivisionError) as exc:
        raise ValueError("Calculation outside supported numeric range") from exc


def unique_object(pairs: list[tuple[str, Any]]) -> dict:
    result: dict = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON field: {key}")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise ValueError(f"Non-finite JSON constant: {value}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Local UTF-8 JSON input; report goes to stdout")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8-sig"),
                             object_pairs_hook=unique_object, parse_constant=reject_constant)
        report = analyse(payload)
        print(json.dumps(report, indent=2, ensure_ascii=True, allow_nan=False))
    except (ValueError, OSError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())