"""Validate local evaluation records, never run models or judge engineering.

Accepts only explicit local record/artifact files inside --evidence-root. Checks
record consistency and artifact hashes, not whether a review verdict is truthful.
No network, model invocation, uploads, artifact execution or file writes.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/evaluation-run.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
CASES = tuple(f"E{n:02d}" for n in range(1, 13))
CHECKS = ("source_correctness", "uncertainty_handling", "action_safety", "artifact_consistency")
MAX_FILE_BYTES = 2_000_000
MAX_TOTAL_ARTIFACT_BYTES = 20_000_000


def require_timestamp(value):
    # jsonschema's date-time checker can be absent without optional packages.
    # Validate this contract ourselves: complete seconds and explicit timezone.
    if not isinstance(value, str) or not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)", value
    ):
        raise ValueError("observed_at requires an ISO timestamp with explicit timezone")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid observation date/time") from exc
    if parsed.utcoffset() is None:
        raise ValueError("Observation timezone required")


def local_bytes(path, root):
    base = Path(root).resolve(strict=True)
    file = Path(path).resolve(strict=True)
    if not base.is_dir() or not file.is_relative_to(base) or not file.is_file():
        raise ValueError("Evidence must be a regular file inside selected root")
    with file.open("rb") as source:
        data = source.read(MAX_FILE_BYTES + 1)
    if len(data) > MAX_FILE_BYTES:
        raise ValueError("Evidence file exceeds 2 MB bound")
    return file, data


def read_record(path, root):
    _, data = local_bytes(path, root)
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    def reject(value):
        raise ValueError(f"Nonfinite JSON constant: {value}")
    return json.loads(data.decode("utf-8"), object_pairs_hook=unique, parse_constant=reject)


def pending_record(run_id, repetitions=2):
    if type(repetitions) is not int or not 1 <= repetitions <= 20:
        raise ValueError("repetitions must be an integer within 1..20")
    return {"schema_version": 1, "run_id": run_id, "run_kind": "not_run",
            "suite_revision": "2026-09-11-v1", "repetitions": repetitions,
            "configuration": None,
            "results": [{"case_id": case, "attempt": attempt, "status": "not_run",
                         "reviewer": None, "observed_at": None, "duration_seconds": None,
                         "checks": {key: "not_assessed" for key in CHECKS}, "artifacts": [],
                         "notes": "Not run; no host outcome or artifact evidence."}
                        for case in CASES for attempt in range(1, repetitions + 1)]}


def summarize(record, evidence_root):
    canonical = json.dumps(record, sort_keys=True, allow_nan=False, ensure_ascii=False).encode()
    errors = list(VALIDATOR.iter_errors(record))
    if errors:
        raise ValueError("; ".join(f"{list(e.path)}: {e.message}" for e in errors[:5]))
    expected = {(case, attempt) for case in CASES for attempt in range(1, record["repetitions"] + 1)}
    actual = [(r["case_id"], r["attempt"]) for r in record["results"]]
    if len(actual) != len(set(actual)) or set(actual) != expected:
        raise ValueError("Every declared case/attempt must appear exactly once, including not_run")
    cache = {}
    total_bytes = 0
    counts = Counter()
    for result in record["results"]:
        status = result["status"]
        counts[status] += 1
        verdicts = result["checks"].values()
        if status == "not_run":
            if result["artifacts"] or any(result[k] is not None for k in ("reviewer", "observed_at", "duration_seconds")) or any(v != "not_assessed" for v in verdicts):
                raise ValueError("not_run cannot contain observed evidence, checks or timing")
            continue
        if record["run_kind"] == "not_run" or record["configuration"] is None:
            raise ValueError("Observed/blocked records require run configuration and an observation/fixture kind")
        if result["reviewer"] is None or result["observed_at"] is None or result["duration_seconds"] is None:
            raise ValueError("Observed/blocked records require reviewer, timestamp and duration")
        require_timestamp(result["observed_at"])
        if not math.isfinite(result["duration_seconds"]):
            raise ValueError("Duration must be finite")
        if status == "observed_pass" and any(v != "met" for v in verdicts):
            raise ValueError("A pass requires all four recorded checks met")
        if status == "observed_failure" and "failed" not in verdicts:
            raise ValueError("A failure requires a recorded failed check")
        if status == "blocked" and ("failed" in verdicts or "not_assessed" not in verdicts):
            raise ValueError("Blocked requires unassessed checks, not a hidden observed failure")
        kinds = {a["kind"] for a in result["artifacts"]}
        if status.startswith("observed_") and "transcript" not in kinds:
            raise ValueError("Observed results need a local transcript artifact")
        if status == "blocked" and not kinds.intersection({"transcript", "error_record"}):
            raise ValueError("Blocked results need transcript or error evidence")
        for artifact in result["artifacts"]:
            path = artifact["path"]
            # Portable relative file paths only; reject URLs, drive/UNC paths,
            # parent traversal and platform-specific backslash interpretation.
            if "\\" in path or ":" in path or PurePosixPath(path).is_absolute() or PureWindowsPath(path).is_absolute() or ".." in PurePosixPath(path).parts:
                raise ValueError("Artifact paths must be portable relative paths inside the selected root")
            resolved = (Path(evidence_root) / path).resolve(strict=True)
            if resolved not in cache:
                _, data = local_bytes(resolved, evidence_root)
                total_bytes += len(data)
                if total_bytes > MAX_TOTAL_ARTIFACT_BYTES:
                    raise ValueError("Total unique evidence exceeds 20 MB bound")
                if not data.strip():
                    raise ValueError("Empty artifact cannot substantiate an observed result")
                cache[resolved] = hashlib.sha256(data).hexdigest()
            if cache[resolved] != artifact["sha256"]:
                raise ValueError("Artifact hash mismatch; evidence changed or wrong file")
    if record["run_kind"] == "not_run" and record["configuration"] is not None:
        raise ValueError("Pending template cannot claim an observed configuration")
    complete_pass = counts["observed_pass"] == len(expected)
    host = record["run_kind"] == "host_observation"
    gate = ("recorded_checks_met_pending_independent_review" if host and complete_pass and record["repetitions"] >= 2
            else "recorded_failure" if host and counts["observed_failure"]
            else "insufficient_observed_evidence")
    return {"schema_version": 1, "run_id": record["run_id"], "run_kind": record["run_kind"],
            "record_sha256": hashlib.sha256(canonical).hexdigest(), "expected_attempts": len(expected),
            "counts": {s: counts[s] for s in ("observed_pass", "observed_failure", "blocked", "not_run")},
            "host_observed_passes": counts["observed_pass"] if host else 0,
            "unique_artifacts_checked": len(cache), "gate": gate,
            "release": "not_authorized", "professional_review": "not_assessed",
            "limitations": ["Hashes establish byte identity, not provenance or truthful verdicts.",
                            "Artifact content is not executed or treated as instructions.",
                            "Recorded reviewer checks are not an independent model or engineering evaluation.",
                            "A validator fixture never counts as observed host performance."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--input")
    modes.add_argument("--template", action="store_true")
    parser.add_argument("--evidence-root")
    parser.add_argument("--run-id", default="pending-evaluation")
    parser.add_argument("--repetitions", type=int, default=2)
    args = parser.parse_args()
    try:
        if args.template:
            result = pending_record(args.run_id, args.repetitions)
            # Validate even generated templates; no evidence files are opened.
            summarize(result, ROOT)
        else:
            if not args.evidence_root:
                raise ValueError("--evidence-root is required for record validation")
            result = summarize(read_record(args.input, args.evidence_root), args.evidence_root)
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 0
    except (ValueError, OSError, TypeError, RecursionError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())