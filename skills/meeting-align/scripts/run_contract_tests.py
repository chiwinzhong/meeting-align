#!/usr/bin/env python3
"""Run positive and negative MeetingAlign contract tests."""

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def run(validator, payload, should_pass, label):
    with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8", delete=False) as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        path = Path(handle.name)
    try:
        result = subprocess.run([sys.executable, str(validator), str(path)], capture_output=True, text=True)
    finally:
        path.unlink(missing_ok=True)
    passed = result.returncode == 0
    if passed != should_pass:
        print(f"FAIL: {label}")
        print(result.stdout or result.stderr)
        raise SystemExit(1)
    print(f"PASS: {label}")


def main():
    if len(sys.argv) != 2:
        print("Usage: run_contract_tests.py path/to/valid-meeting-align.json")
        raise SystemExit(2)
    sample_path = Path(sys.argv[1])
    sample = json.loads(sample_path.read_text(encoding="utf-8"))
    validator = Path(__file__).with_name("validate_meeting_align.py")

    run(validator, sample, True, "valid meeting package")

    unknown_evidence = copy.deepcopy(sample)
    unknown_evidence["decisions"][0]["evidence_ids"] = ["E999"]
    run(validator, unknown_evidence, False, "unknown decision evidence")

    suggestion_as_decision = copy.deepcopy(sample)
    decision_evidence_id = suggestion_as_decision["decisions"][0]["evidence_ids"][0]
    for item in suggestion_as_decision["evidence"]:
        if item["id"] == decision_evidence_id:
            item["type"] = "AI_SUGGESTION"
    run(validator, suggestion_as_decision, False, "AI suggestion promoted to decision")

    invented_precision = copy.deepcopy(sample)
    invented_precision["actions"][0].pop("definition_of_done")
    run(validator, invented_precision, False, "action missing definition-of-done field")

    silent_confirmation = copy.deepcopy(sample)
    silent_confirmation["understanding_checks"][0]["status"] = "assumed_aligned"
    run(validator, silent_confirmation, False, "silence treated as confirmation")

    print("ALL CONTRACT TESTS PASSED")


if __name__ == "__main__":
    main()
