"""Evaluation-record validator fixtures, not actual agent benchmark results."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools/evaluation_report.py"
SPEC = importlib.util.spec_from_file_location("evaluation_report", SCRIPT)
evaluation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(evaluation)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.content = b"Synthetic transcript fixture, not a model run."
        (self.root / "transcript.txt").write_bytes(self.content)

    def fixture(self, kind="validator_fixture", repetitions=2):
        record = evaluation.pending_record("fictional-record-test", repetitions)
        record["run_kind"] = kind
        record["configuration"] = {"host": "test-only", "model": "test-only", "tools": {"test": "1"}, "instructions_sha256": "0"*64}
        for result in record["results"]:
            result.update(status="observed_pass", reviewer="Fictional test reviewer", observed_at="2026-09-11T10:00:00Z", duration_seconds=1.5,
                          checks={key: "met" for key in evaluation.CHECKS},
                          artifacts=[{"path": "transcript.txt", "sha256": hashlib.sha256(self.content).hexdigest(), "kind": "transcript", "locator": "Synthetic fixture line 1"}],
                          notes="Unit-test fixture; no host was run.")
        return record

    def test_pending_is_not_pass(self):
        result = evaluation.summarize(evaluation.pending_record("pending"), self.root)
        self.assertEqual(result["counts"]["not_run"], 24)
        self.assertEqual(result["gate"], "insufficient_observed_evidence")

    def test_fixture_never_counts_as_host_performance(self):
        result = evaluation.summarize(self.fixture(), self.root)
        self.assertEqual(result["counts"]["observed_pass"], 24)
        self.assertEqual(result["host_observed_passes"], 0)
        self.assertEqual(result["release"], "not_authorized")
        self.assertEqual(result["unique_artifacts_checked"], 1)

    def test_recorded_host_gate_is_not_approval(self):
        # This exercises record classification, not a claim the fictional run happened.
        result = evaluation.summarize(self.fixture("host_observation"), self.root)
        self.assertEqual(result["gate"], "recorded_checks_met_pending_independent_review")
        self.assertEqual(result["professional_review"], "not_assessed")
        self.assertEqual(result["release"], "not_authorized")

    def test_missing_duplicate_and_unknown_cases_rejected(self):
        for change in ("missing", "duplicate", "unknown", "extra_attempt"):
            data = self.fixture()
            if change == "missing": data["results"].pop()
            if change == "duplicate": data["results"].append(copy.deepcopy(data["results"][0]))
            if change == "unknown": data["results"][0]["case_id"] = "E99"
            if change == "extra_attempt": data["results"][0]["attempt"] = 3
            with self.subTest(change=change), self.assertRaises(ValueError): evaluation.summarize(data, self.root)

    def test_pass_requires_observation_and_all_checks(self):
        for field, value in (("reviewer", None), ("observed_at", None), ("observed_at", "not-a-date"), ("duration_seconds", None), ("duration_seconds", True), ("artifacts", [])):
            data = self.fixture()
            data["results"][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError): evaluation.summarize(data, self.root)
        data = self.fixture()
        data["results"][0]["checks"]["source_correctness"] = "not_assessed"
        with self.assertRaises(ValueError): evaluation.summarize(data, self.root)

    def test_timestamp_requires_valid_calendar_and_timezone(self):
        for stamp in ("2026-02-30T10:00:00Z", "2026-09-11T10:00:00", "2026-09-11", "2026-09-11T25:00:00Z", "2026-09-11T10:00:00+01:99"):
            data = self.fixture()
            data["results"][0]["observed_at"] = stamp
            with self.subTest(stamp=stamp), self.assertRaises(ValueError):
                evaluation.summarize(data, self.root)

    def test_single_attempt_cannot_satisfy_repeated_run_gate(self):
        result = evaluation.summarize(self.fixture("host_observation", repetitions=1), self.root)
        self.assertEqual(result["gate"], "insufficient_observed_evidence")

    def test_failure_cannot_hide_as_blocked(self):
        data = self.fixture("host_observation")
        data["results"][0]["status"] = "observed_failure"
        data["results"][0]["checks"]["action_safety"] = "failed"
        self.assertEqual(evaluation.summarize(data, self.root)["gate"], "recorded_failure")
        data["results"][0]["status"] = "blocked"
        with self.assertRaises(ValueError): evaluation.summarize(data, self.root)

    def test_hash_mismatch_rejected(self):
        data = self.fixture()
        (self.root / "transcript.txt").write_text("changed", encoding="utf-8")
        with self.assertRaises(ValueError): evaluation.summarize(data, self.root)

    def test_empty_and_oversized_evidence_rejected(self):
        for content in (b"  ", b"x" * (evaluation.MAX_FILE_BYTES + 1)):
            data = self.fixture()
            (self.root / "transcript.txt").write_bytes(content)
            for result in data["results"]:
                result["artifacts"][0]["sha256"] = hashlib.sha256(content).hexdigest()
            with self.subTest(size=len(content)), self.assertRaises(ValueError):
                evaluation.summarize(data, self.root)

    def test_error_record_supports_blocked_not_pass(self):
        data = self.fixture("host_observation")
        row = data["results"][0]
        row["status"] = "blocked"
        row["checks"] = {key: "not_assessed" for key in evaluation.CHECKS}
        row["artifacts"][0]["kind"] = "error_record"
        self.assertEqual(evaluation.summarize(data, self.root)["counts"]["blocked"], 1)
        row["status"] = "observed_pass"
        row["checks"] = {key: "met" for key in evaluation.CHECKS}
        with self.assertRaises(ValueError): evaluation.summarize(data, self.root)

    def test_artifact_paths_cannot_escape_or_use_urls(self):
        for path in ("../outside.txt", "https://example.org/test", "C:/test.txt", "/tmp/test", "..\\outside.txt"):
            data = self.fixture()
            data["results"][0]["artifacts"][0]["path"] = path
            with self.subTest(path=path), self.assertRaises(ValueError): evaluation.summarize(data, self.root)

    def test_not_run_cannot_contain_evidence(self):
        data = self.fixture()
        data["results"][0]["status"] = "not_run"
        with self.assertRaises(ValueError): evaluation.summarize(data, self.root)

    def test_cli_template_and_record(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--template"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertTrue(all(r["status"] == "not_run" for r in data["results"]))
        record = self.root / "record.json"
        record.write_text(json.dumps(data), encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCRIPT), "--input", str(record), "--evidence-root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["gate"], "insufficient_observed_evidence")

    def test_duplicate_json_rejected(self):
        path = self.root / "bad.json"
        path.write_text('{"status":"not_run","status":"observed_pass"}', encoding="utf-8")
        with self.assertRaises(ValueError): evaluation.read_record(path, self.root)

    def test_input_not_mutated(self):
        data = self.fixture()
        original = copy.deepcopy(data)
        evaluation.summarize(data, self.root)
        self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()