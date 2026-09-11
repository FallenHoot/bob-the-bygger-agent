"""Offline numerical/contract regressions, not structural or code certification.

Run: python -m unittest discover -s tests -p test_beam_calculator.py -v
Fixtures are public benchmarks or fictional models, never private project data.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/structural-engineering/scripts/beam_calculator.py"
EXAMPLE = ROOT / "skills/structural-engineering/assets/beam-example.json"
SPEC = importlib.util.spec_from_file_location("beam_calculator", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
beam = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(beam)


def model(support="simply_supported", kind="udl", position=3.0):
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    data["support"] = support
    if kind == "point":
        data["load"] = {"kind": kind, "magnitude": {"value": 8, "unit": "kN"},
                        "position": {"value": position, "unit": "m"}}
    return data


def criterion(status="user_supplied"):
    return {"span_ratio": 360, "source": "Fictional client criterion for test only",
            "evidence_status": status, "component": "elastic_load_case"}


class NumericalTests(unittest.TestCase):
    def test_published_udl(self):
        r = beam.analyse(model())["response"]
        self.assertAlmostEqual(r["max_deflection_down_mm"], 4.726890756302521)
        self.assertEqual(r["max_deflection_at_mm"], 3000)
        self.assertEqual(r["max_abs_moment_kn_m"], 22.5)
        self.assertEqual(r["max_abs_shear_kn"], 15)
        self.assertEqual(r["reaction_left_up_kn"], 15)
        self.assertEqual(r["reaction_right_up_kn"], 15)

    def test_published_cantilever(self):
        data = model("cantilever", "point")
        data["span"]["value"] = 3
        data["second_moment"]["value"] = 3200
        r = beam.analyse(data)["response"]
        self.assertAlmostEqual(r["max_deflection_down_mm"], 10.714285714285714)
        self.assertEqual(r["max_abs_moment_kn_m"], 24)
        self.assertEqual(r["max_abs_shear_kn"], 8)
        self.assertIsNone(r["reaction_right_up_kn"])

    def test_supplied_link_example(self):
        data = model("cantilever", "point", 4.5)
        data["span"]["value"] = 4.5
        data["load"]["magnitude"]["value"] = 12
        data["second_moment"]["value"] = 8560
        r = beam.analyse(data)["response"]
        self.assertAlmostEqual(r["max_deflection_down_mm"], 20.277036048064)
        self.assertEqual(r["max_abs_moment_kn_m"], 54)

    def test_central_point_closed_form(self):
        r = beam.analyse(model(kind="point"))["response"]
        expected = 8000 * 6000**3 / (48 * 210000 * 85000000)
        self.assertAlmostEqual(r["max_deflection_down_mm"], expected)
        self.assertEqual(r["max_abs_moment_kn_m"], 12)
        self.assertEqual(r["max_abs_shear_kn"], 4)

    def test_cantilever_udl_closed_form(self):
        r = beam.analyse(model("cantilever"))["response"]
        expected = 5 * 6000**4 / (8 * 210000 * 85000000)
        self.assertAlmostEqual(r["max_deflection_down_mm"], expected)
        self.assertEqual(r["reaction_moment_left_ccw_kn_m"], 90)
        self.assertEqual(r["stations"][0]["moment_kn_m"], -90)
        self.assertEqual(r["max_abs_shear_kn"], 30)

    def test_offcentre_point_extremum_and_mirror(self):
        r = beam.analyse(model(kind="point", position=2))["response"]
        mirrored = beam.analyse(model(kind="point", position=4))["response"]
        expected_x = 6000 - math.sqrt((6000**2 - 2000**2) / 3)
        self.assertAlmostEqual(r["max_deflection_at_mm"], expected_x)
        self.assertNotEqual(r["max_deflection_at_mm"], 2000)
        self.assertAlmostEqual(r["max_deflection_down_mm"], mirrored["max_deflection_down_mm"])
        self.assertAlmostEqual(r["max_deflection_at_mm"] + mirrored["max_deflection_at_mm"], 6000)
        load_station = next(s for s in r["stations"] if s["x_mm"] == 2000)
        self.assertAlmostEqual(load_station["shear_before_load_kn"] - load_station["shear_after_load_kn"], 8)

    def test_cantilever_interior_point(self):
        r = beam.analyse(model("cantilever", "point", 2))["response"]
        expected = 8000 * 2000**2 * (3 * 6000 - 2000) / (6 * 210000 * 85000000)
        self.assertAlmostEqual(r["max_deflection_down_mm"], expected)
        self.assertEqual(r["max_deflection_at_mm"], 6000)
        self.assertEqual(r["max_abs_moment_kn_m"], 16)

    def test_equilibrium_and_boundary_conditions(self):
        for support in ("simply_supported", "cantilever"):
            for kind in ("point", "udl"):
                with self.subTest(support=support, kind=kind):
                    r = beam.analyse(model(support, kind, 2))["response"]
                    total, lever = (8, 2) if kind == "point" else (30, 3)
                    right = r["reaction_right_up_kn"] or 0
                    self.assertAlmostEqual(r["reaction_left_up_kn"] + right, total)
                    self.assertAlmostEqual(r["reaction_moment_left_ccw_kn_m"] + right * 6,
                                           total * lever)
                    start, end = r["stations"][0], r["stations"][-1]
                    self.assertAlmostEqual(start["deflection_down_mm"], 0)
                    self.assertAlmostEqual(end["moment_kn_m"], 0)
                    if support == "simply_supported":
                        self.assertAlmostEqual(end["deflection_down_mm"], 0)
                        self.assertAlmostEqual(start["moment_kn_m"], 0)

    def test_unit_load_integration_independent_cross_check(self):
        # Virtual-work midpoint integration of M*m/EI, not the implementation's
        # closed-form displacement expressions. Includes all four cases.
        for support in ("simply_supported", "cantilever"):
            for kind in ("udl", "point"):
                for a in ((1.1, 4.7) if kind == "point" else (3,)):
                    with self.subTest(support=support, kind=kind, a=a):
                        r = beam.analyse(model(support, kind, a))["response"]
                        x = r["max_deflection_at_mm"] / 1000
                        L = 6.0
                        count = 20000
                        dx = L / count
                        integral = 0.0
                        for i in range(count):
                            s = (i + 0.5) * dx
                            if support == "simply_supported":
                                M = (5 * L / 2 * s - 5 * s*s / 2) if kind == "udl" else (
                                    8 * (L - a) / L * s - 8 * max(s - a, 0))
                                m = (L - x) / L * s - max(s - x, 0)
                            else:
                                M = -5 * (L - s)**2 / 2 if kind == "udl" else -8 * max(a - s, 0)
                                m = -max(x - s, 0)
                            integral += M * m * dx
                        # E=210e6 kN/m², I=8500e-8 m⁴; convert m to mm.
                        numerical_mm = integral / (210e6 * 8500e-8) * 1000
                        self.assertAlmostEqual(r["max_deflection_down_mm"], numerical_mm,
                                               delta=max(1e-7, abs(numerical_mm) * 1e-7))

    def test_unit_equivalence(self):
        data = model()
        original = beam.analyse(data)["response"]
        for key, value in (("span", {"value": 6000, "unit": "mm"}),
                           ("elastic_modulus", {"value": 210000, "unit": "MPa"}),
                           ("second_moment", {"value": 85000000, "unit": "mm^4"})):
            data[key] = value
        data["load"]["magnitude"] = {"value": 5, "unit": "N/mm"}
        converted = beam.analyse(data)["response"]
        # Unit-library scale factors introduce normal floating-point rounding.
        for key, value in original.items():
            if isinstance(value, (int, float)):
                self.assertAlmostEqual(value, converted[key])
        for before, after in zip(original["stations"], converted["stations"]):
            for key in before:
                self.assertAlmostEqual(before[key], after[key])
        # Independently defined inch/lbf conversion factors, not Pint.
        data["span"] = {"value": 6000 / 304.8, "unit": "ft"}
        data["elastic_modulus"] = {"value": 210000 / 6.894757293168361, "unit": "ksi"}
        data["second_moment"] = {"value": 85000000 / 25.4**4, "unit": "in^4"}
        data["load"]["magnitude"] = {"value": 5 / (4448.2216152605 / 304.8), "unit": "kip/ft"}
        self.assertAlmostEqual(original["max_deflection_down_mm"],
                               beam.analyse(data)["response"]["max_deflection_down_mm"])

    def test_unit_conversions_and_fourth_power(self):
        cases = [("length", 1, "in", 25.4), ("force", 1, "kip", 4448.2216152605),
                 ("inertia", 1, "cm^4", 10000), ("modulus", 1, "GPa", 1000),
                 ("line_load", 1, "kN/m", 1)]
        for kind, value, unit, expected in cases:
            with self.subTest(unit=unit):
                self.assertAlmostEqual(beam.quantity({"value": value, "unit": unit}, kind, "test"), expected)

    def test_scaling_laws(self):
        baseline = beam.analyse(model())["response"]["max_deflection_down_mm"]
        for field, multiplier in (("span", 16), ("elastic_modulus", 0.5), ("second_moment", 0.5)):
            data = model()
            data[field]["value"] *= 2
            self.assertAlmostEqual(beam.analyse(data)["response"]["max_deflection_down_mm"], baseline * multiplier)

    def test_zero_load_and_support_applied_point(self):
        for support in ("simply_supported", "cantilever"):
            for kind in ("udl", "point"):
                data = model(support, kind)
                data["load"]["magnitude"]["value"] = 0
                r = beam.analyse(data)["response"]
                self.assertEqual(r["max_deflection_down_mm"], 0)
                self.assertEqual(r["max_abs_shear_kn"], 0)
            for position in ((0, 6) if support == "simply_supported" else (0,)):
                with self.subTest(support=support, position=position):
                    r = beam.analyse(model(support, "point", position))["response"]
                    self.assertEqual(r["max_deflection_down_mm"], 0)
                    self.assertEqual(r["max_abs_moment_kn_m"], 0)
                    self.assertEqual(r["max_abs_shear_kn"], 0)
                    for station in r["stations"]:
                        self.assertEqual(station["shear_before_load_kn"], 0)
                        self.assertEqual(station["shear_after_load_kn"], 0)


class ValidationTests(unittest.TestCase):
    def test_nonfinite_nonpositive_and_wrong_types(self):
        for value in (0, -1, True, "6", None, float("nan"), float("inf"), 10**400):
            for key in ("span", "elastic_modulus", "second_moment"):
                with self.subTest(key=key, value=str(value)):
                    data = model()
                    data[key]["value"] = value
                    with self.assertRaises(ValueError):
                        beam.analyse(data)

    def test_reject_unit_dimension_mismatches(self):
        for key, unit in (("span", "kN"), ("second_moment", "mm^3"),
                          ("elastic_modulus", "GPA"), ("span", "__import__('os')")):
            data = model()
            data[key]["unit"] = unit
            with self.assertRaises(ValueError):
                beam.analyse(data)
        for kind, unit in (("point", "kN/m"), ("udl", "kN")):
            data = model(kind=kind)
            data["load"]["magnitude"]["unit"] = unit
            with self.assertRaises(ValueError):
                beam.analyse(data)

    def test_no_silent_load_or_position_clamping(self):
        for position in (-0.001, 6.001, float("nan")):
            with self.assertRaises(ValueError):
                beam.analyse(model(kind="point", position=position))
        data = model()
        data["load"]["magnitude"]["value"] = -1
        with self.assertRaises(ValueError):
            beam.analyse(data)

    def test_missing_extra_and_unsupported_fields(self):
        for field in model():
            data = model()
            del data[field]
            with self.assertRaises(ValueError):
                beam.analyse(data)
        bad = [([],), (None,)]
        for (value,) in bad:
            with self.assertRaises(ValueError):
                beam.analyse(value)
        for key, value in (("schema_version", True), ("support", "fixed_fixed"),
                           ("support", []), ("automatic_snow_load", 2.5)):
            data = model()
            data[key] = value
            with self.assertRaises(ValueError):
                beam.analyse(data)
        data = model(kind="point")
        del data["load"]["position"]
        with self.assertRaises(ValueError):
            beam.analyse(data)
        data = model()
        data["load"]["position"] = {"value": 2, "unit": "m"}
        with self.assertRaises(ValueError):
            beam.analyse(data)

    def test_provenance_is_required_not_verification(self):
        for key in model()["basis"]:
            data = model()
            data["basis"][key] = " "
            with self.assertRaises(ValueError):
                beam.analyse(data)
        report = beam.analyse(model())
        self.assertEqual(report["design_compliance"], "not_assessed")
        self.assertIn("not independently verified", " ".join(report["limitations"]))

    def test_numeric_range_rejected(self):
        for value in (1e100, 1e-200):
            data = model()
            data["span"]["value"] = value
            with self.assertRaises(ValueError):
                beam.analyse(data)
        with self.assertRaises(ValueError):
            beam.quantity({"value": 5e-324, "unit": "N/m"}, "line_load", "tiny load")
        data = model()
        data["load"]["magnitude"]["value"] = 1e-300
        data["second_moment"]["value"] = 1e100
        with self.assertRaises(ValueError):
            beam.analyse(data)

    def test_input_not_mutated_and_deterministic(self):
        data = model()
        previous = copy.deepcopy(data)
        one = beam.analyse(data)
        self.assertEqual(data, previous)
        self.assertEqual(one, beam.analyse(data))
        json.dumps(one, allow_nan=False)


class CriterionTests(unittest.TestCase):
    def test_no_default_limit(self):
        report = beam.analyse(model())
        self.assertEqual(report["deflection_comparison"]["status"], "not_assessed")

    def test_within_and_exceeds_are_arithmetic_only(self):
        for span, expected in ((6, "within"), (12, "exceeds")):
            data = model()
            data["span"]["value"] = span
            data["criterion"] = criterion()
            data["basis"]["load_basis"] = "SLS"
            report = beam.analyse(data)
            self.assertEqual(report["deflection_comparison"]["status"],
                             f"arithmetic_{expected}_supplied_limit")
            self.assertEqual(report["design_compliance"], "not_assessed")

    def test_unverified_uls_and_unknown_self_weight_hold(self):
        for change in ("unverified", "ULS", "unknown"):
            data = model()
            data["criterion"] = criterion()
            if change == "unverified":
                data["criterion"]["evidence_status"] = change
            elif change == "ULS":
                data["basis"]["load_basis"] = change
            else:
                data["basis"]["self_weight"] = change
            self.assertEqual(beam.analyse(data)["deflection_comparison"]["status"], "not_assessed")

    def test_unsupported_final_component_or_verified_claim(self):
        for key, val in (("component", "final_with_creep"), ("evidence_status", "verified"),
                         ("source", ""), ("span_ratio", 0), ("span_ratio", float("nan"))):
            data = model()
            data["criterion"] = criterion()
            data["criterion"][key] = val
            with self.assertRaises(ValueError):
                beam.analyse(data)


class CLITests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, check=False)

    def test_example_cli(self):
        result = self.run_cli("--input", str(EXAMPLE))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["response"]["max_abs_moment_kn_m"], 22.5)
        self.assertEqual(result.stderr, "")

    def test_invalid_json_and_schema_no_success_output(self):
        for content in ('{"span":1,"span":2}', '{"x":NaN}', '{"x":Infinity}', '{', '{}'):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "input.json"
                path.write_text(content, encoding="utf-8")
                result = self.run_cli("--input", str(path))
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertEqual(json.loads(result.stderr)["status"], "error")

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_cli("--input", str(Path(directory) / "absent.json"))
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stderr)["status"], "error")


if __name__ == "__main__":
    unittest.main()