"""Synthetic PDF/DXF fixtures; no private drawings or external OCR."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import fitz
import ezdxf

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills/drawing-reader/scripts"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


drawing = load("extract_drawing")
geometry = load("extract_geometry")


class DrawingTests(unittest.TestCase):
    def test_rectangle_paths_are_extracted_with_source_ids(self):
        path = Path(self.temp.name) / "rectangles.pdf"
        with fitz.open() as doc:
            page = doc.new_page(width=600, height=400)
            page.draw_rect(fitz.Rect(100, 100, 300, 250))
            doc.save(path)
        result = geometry.build_leveled_model(str(path))
        page = result["pages"][0]
        candidates = page["L3_element_grid"]["interior_candidates_sample"]
        self.assertEqual(len(candidates), 4)
        self.assertEqual(len({c["candidate_id"] for c in candidates}), 4)
        self.assertTrue(all(c["source_item_type"] == "re" for c in candidates))
        self.assertEqual(result["source_sha256"], geometry.build_leveled_model(str(path))["source_sha256"])

    def test_rotated_crop_uses_unrotated_extraction_coordinates(self):
        path = Path(self.temp.name) / "rotated.pdf"
        with fitz.open() as doc:
            page = doc.new_page(width=600, height=400)
            page.draw_rect(fitz.Rect(100, 100, 300, 250))
            page.set_cropbox(fitz.Rect(50, 50, 550, 350))
            page.set_rotation(90)
            doc.save(path)
        result = geometry.build_leveled_model(str(path), [1], clip=[0, 0, 500, 300])
        context = result["pages"][0]["L1_sheet_context"]
        self.assertEqual(context["page_rotation_degrees"], 90)
        self.assertEqual(context["sheet_size_pt"], {"width": 500, "height": 300})
        self.assertEqual(len(result["pages"][0]["L3_element_grid"]["interior_candidates_sample"]), 4)
        extracted = drawing.extract(str(path))
        self.assertEqual(extracted["pages"][0]["width_pts"], 500)
        self.assertEqual(extracted["pages"][0]["rotation_degrees"], 90)

    def test_extreme_calibration_is_controlled_error(self):
        with fitz.open(self.pdf) as doc:
            for value in (5e-324, 10**400):
                with self.subTest(value=value), self.assertRaises(ValueError):
                    geometry.calibrate_scale(doc[0], {"paper_length_pts": value,
                        "real_length_mm": 1000, "source": "test", "view": "test"})

    def test_unsupported_curves_and_sample_truncation_visible(self):
        path = Path(self.temp.name) / "many-lines.pdf"
        with fitz.open() as doc:
            page = doc.new_page(width=600, height=600)
            page.draw_circle((300, 300), 20)
            for i in range(50):
                page.draw_line((50, 50+i*5), (250, 50+i*5))
            doc.save(path)
        grid = geometry.build_leveled_model(str(path))["pages"][0]["L3_element_grid"]
        self.assertTrue(grid["sample_truncated"])
        self.assertEqual(grid["interior_candidate_count"], 50)
        self.assertGreater(grid["omissions"]["unsupported_path_items"], 0)

    def test_clip_omissions_reported(self):
        grid = geometry.build_leveled_model(str(self.pdf), [1], clip=[70, 90, 130, 110])["pages"][0]["L3_element_grid"]
        self.assertGreater(grid["omissions"]["segments_not_wholly_in_clip"], 0)

    def test_content_outside_visible_crop_not_reported_as_candidates(self):
        path = Path(self.temp.name) / "hidden-path.pdf"
        with fitz.open() as doc:
            page = doc.new_page(width=600, height=400)
            page.draw_line((10, 10), (300, 10))
            page.draw_line((100, 100), (250, 100))
            page.set_cropbox(fitz.Rect(50, 50, 550, 350))
            doc.save(path)
        grid = geometry.build_leveled_model(str(path))["pages"][0]["L3_element_grid"]
        self.assertEqual(grid["omissions"]["segments_outside_visible_crop"], 1)
        self.assertEqual(grid["interior_candidate_count"], 1)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.pdf = Path(self.temp.name) / "synthetic.pdf"
        with fitz.open() as doc:
            for label in ("Main plan 1:100; detail 1:5", "SECOND PAGE"):
                page = doc.new_page(width=400, height=400)
                page.insert_text((30, 30), label)
                page.draw_line((50, 100), (150, 100))
            doc.save(self.pdf)

    def test_sparse_text_retained_and_scope(self):
        result = drawing.extract(str(self.pdf))
        self.assertEqual(result["selected_pages"], [1])
        self.assertTrue(result["pages"][0]["text_blocks"])
        self.assertNotIn("SECOND PAGE", json.dumps(result))
        self.assertIn("SECOND PAGE", json.dumps(drawing.extract(str(self.pdf), pages=[2])))

    def test_invalid_page_selection(self):
        for pages in ([], [0], [3], [1, 1], [True]):
            with self.subTest(pages=pages), self.assertRaises(ValueError):
                drawing.extract(str(self.pdf), pages=pages)

    def test_no_implicit_ocr(self):
        result = drawing.extract(str(self.pdf))
        self.assertEqual(result["tool"], "pymupdf")
        with self.assertRaises(ValueError):
            drawing.extract("picture.png")
        with self.assertRaises(ValueError):
            drawing.extract_with_marker(str(self.pdf), use_llm=True)

    def test_format_and_mode_rejected(self):
        for path, mode in (("a.dwg", "auto"), ("a.ifc", "auto"), (str(self.pdf), "dxf"), ("a.dxf", "marker")):
            with self.subTest(path=path, mode=mode), self.assertRaises(ValueError):
                drawing.extract(path, mode=mode)

    def test_scale_is_not_confirmed(self):
        model = geometry.build_leveled_model(str(self.pdf))
        page = model["pages"][0]
        scale = page["L1_sheet_context"]["scale"]
        self.assertEqual(scale["detected_scales"], [5, 100])
        self.assertFalse(scale["confirmed"])
        self.assertIsNone(scale["denom"])
        self.assertNotIn("length_mm_real", json.dumps(page))
        self.assertEqual(page["L2_zone_layout"]["status"], "not_implemented")

    def test_explicit_calibration_scoped(self):
        c = {"paper_length_pts": 100, "real_length_mm": 1000,
             "source": "Synthetic known line A-B", "view": "Synthetic test view"}
        result = geometry.build_leveled_model(str(self.pdf), [1], c, [40, 80, 200, 120])
        page = result["pages"][0]
        self.assertFalse(page["L1_sheet_context"]["scale"]["confirmed"])
        self.assertEqual(page["L3_element_grid"]["interior_candidates_sample"][0]["length_mm_real"], 1000)
        for pages, clip in (([1, 2], [0, 0, 200, 200]), ([1], None), ([1], [-1, 0, 200, 200])):
            with self.assertRaises(ValueError):
                geometry.build_leveled_model(str(self.pdf), pages, c, clip)

    def test_invalid_calibration(self):
        with fitz.open(self.pdf) as doc:
            for value in (0, -1, True, float("inf"), None):
                with self.subTest(value=value), self.assertRaises(ValueError):
                    geometry.calibrate_scale(doc[0], {"paper_length_pts": value,
                        "real_length_mm": 1000, "source": "test", "view": "test"})

    def test_geometry_multiple_pages(self):
        result = geometry.build_leveled_model(str(self.pdf), [2, 1])
        self.assertEqual([p["page"] for p in result["pages"]], [2, 1])

    def make_dxf(self, units):
        path = Path(self.temp.name) / f"synthetic-{units}.dxf"
        doc = ezdxf.new()
        doc.units = units
        doc.modelspace().add_linear_dim(base=(0, 2), p1=(0, 0), p2=(10, 0)).render()
        doc.modelspace().add_mtext("Synthetic note")
        doc.saveas(path)
        return path

    def test_dxf_actual_unit_fixtures(self):
        for units, expected in ((6, 10000), (4, 10), (1, 254), (0, None)):
            with self.subTest(units=units):
                result = drawing.extract(str(self.make_dxf(units)))
                self.assertEqual(result["dimensions"][0]["value_mm"], expected)
                self.assertTrue(result["texts"])
                self.assertEqual(result["dimensions"][0]["raw_measurement"], 10)

    def test_cli_json_and_errors(self):
        script = SCRIPTS / "extract_drawing.py"
        result = subprocess.run([sys.executable, str(script), str(self.pdf), "--pages", "2"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["selected_pages"], [2])
        result = subprocess.run([sys.executable, str(script), str(self.pdf), "--pages", "99"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("error", json.loads(result.stderr))

    def test_geometry_will_not_overwrite(self):
        result = subprocess.run([sys.executable, str(SCRIPTS / "extract_geometry.py"), str(self.pdf), "--out", str(self.pdf)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        with fitz.open(self.pdf) as doc:
            self.assertEqual(len(doc), 2)

    def test_angular_dxf_not_labeled_mm(self):
        path = Path(self.temp.name) / "angle.dxf"
        doc = ezdxf.new()
        doc.units = 4
        doc.modelspace().add_angular_dim_3p(base=(3, 3), center=(0, 0), p1=(5, 0), p2=(0, 5)).render()
        doc.saveas(path)
        result = drawing.extract(str(path))
        self.assertEqual(len(result["dimensions"]), 1)
        self.assertNotIn("value_mm", result["dimensions"][0])


if __name__ == "__main__":
    unittest.main()