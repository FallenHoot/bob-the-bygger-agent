# Local Development and Validation

Use Python 3.12 and PowerShell 7 for the full suite. The same Python environment
must run dependency installation, lint and tests. No private project or MCP
configuration is needed. [requirements-dev.txt](../requirements-dev.txt) pins the
principal test libraries; transitive dependencies are not a complete lockfile.

## Setup and Checks

From the repository root on Windows:

```powershell
python -m venv .venv
& ./.venv/Scripts/python.exe -m pip install -r requirements-dev.txt
& ./.venv/Scripts/python.exe -m pip check
& ./.venv/Scripts/python.exe skills/validate_skills.py
& ./.venv/Scripts/python.exe -m unittest discover -s tests -p 'test_*.py' -v
& ./tests/Test-AgentContracts.ps1
git diff --check
```

On Linux/macOS use the environment interpreter at `.venv/bin/python`; PowerShell
7 is still needed for the source-contract script. The [CI definition](../.github/workflows/validate.yml)
uses Windows and Ubuntu. Adding it locally does not prove a hosted run passed.

No workflow uses project folders, external OCR, hosted LLMs or customer data.
Dependencies are fetched only during explicit setup; tests use local synthetic
fixtures. Review package licences, including PyMuPDF's AGPL/commercial options,
before distributing an application. The root MIT versus skill Proprietary labels
remain a maintainer decision; this pass has not changed their grants.

## Local Detail Example

```powershell
& ./.venv/Scripts/python.exe tools/detail_package.py --project-root examples/detail-package --input examples/detail-package/synthetic-wall.json
```

The tool writes JSON to stdout by default. Source locations inside its input are
opaque evidence labels: the tool does not open URLs or source documents and cannot
verify their truth. Add `--format svg` to emit the supported one-wall/opening/well
preview instead; missing/conflicting required geometry is rejected. Both modes
use stdout, not file writes. The selected root bounds explicitly read package
inputs, not all possible agent tools or host access. It is not a general sandbox.

For two local revisions within the same root, add `--compare-to` with the later
input file. Reports contain input hashes, direct changes and conservative dependent
records requiring revalidation. No files or holds are automatically changed.

Detail tool version 1.1 adds exact before/after field differences, hold-removal
review and complete layer uncertainty. Project-advisory numeric quantities require
source-matched evidence_refs locators; synthetic sources/quantities cannot be
reclassified simply by changing the package basis. These labels are not verified
facts. Returned reports are independent copies and cannot mutate the input package.

## Drawing Migration

Drawing outputs now use **schema version 2** and explicit selected-page records.
Text extraction defaults to page 1; use `--pages` or `--all-pages` intentionally.
Geometry uses a pages array and withholds real-world lengths without an explicit
single-view calibration. Old output fields that called detected scales confirmed
or paper extent a building envelope are no longer valid evidence.

Extraction version 2.1 uses unrotated crop-relative coordinates, reports page
rotation/crop metadata and hashes the exact opened PDF bytes. Rectangle path items
are expanded to line candidates. Candidate IDs apply only to identical source
bytes/version, not persistent walls. Omission counts and sample truncation must
be considered before interpreting the 40-candidate sample as coverage.

DXF raw coordinates remain in declared drawing units. Only supported linear
dimension types are converted to millimetres; angular/unknown types are not.
Unknown units produce unresolved quantities, not a guessed conversion. DWG must
be exported/converted through a separately authorized supported workflow.

## Evaluation Records

Generate a pending local record without calling any model:

```powershell
& ./.venv/Scripts/python.exe tools/evaluation_report.py --template --run-id pending-host-review --repetitions 2
```

The output intentionally contains no passing results. For actual collected records
use `--input` and `--evidence-root`. Required artifacts must be local and hash-matched;
the checker verifies record consistency, not model behavior or engineering truth.
See [the case and record guide](evaluations/README.md).

## What the Tests Do Not Prove

- General OCR/wall recognition accuracy, CAD/BIM round-trip correctness or site conditions.
- Professional/authority approval or legal correctness across all technical topics.
- Host model obedience, context efficiency or zero prompt-injection risk.
- External connector availability, access control or data-retention policies.

The [behavioral evaluation specification](evaluations/README.md) defines live-host
cases still to run. Keep expected and observed outcomes separate; never promote a
deterministic tool test into an LLM behavior or professional-review result.