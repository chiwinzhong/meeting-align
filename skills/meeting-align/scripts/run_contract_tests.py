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

    blocked_audio = copy.deepcopy(sample)
    blocked_audio["ingestion"] = {
        "input_type": "recording",
        "status": "blocked",
        "transcript_path": None,
        "coverage": "unknown",
        "speaker_labels": "unavailable",
        "timestamps": "unavailable",
        "adapter": "unavailable",
        "limitations": ["Reliable complete transcription is unavailable."],
    }
    blocked_audio["meeting"]["source_status"] = "unverified"
    for section in (
        "evidence", "decisions", "rejected_or_deferred", "open_questions",
        "actions", "alignment_gaps", "roles", "understanding_checks",
    ):
        blocked_audio[section] = []
    blocked_audio["alignment_score"] = None
    blocked_audio["review"] = {
        "status": "draft",
        "reviewer": "not yet defined",
        "external_actions_authorized": False,
    }
    blocked_audio["limitations"] = ["INGESTION_BLOCKED"]
    run(validator, blocked_audio, True, "blocked recording stops before semantic analysis")

    blocked_with_decision = copy.deepcopy(blocked_audio)
    blocked_with_decision["decisions"] = [copy.deepcopy(sample["decisions"][0])]
    run(validator, blocked_with_decision, False, "blocked recording cannot contain decisions")

    incomplete_recording = copy.deepcopy(sample)
    incomplete_recording["ingestion"] = {
        "input_type": "recording",
        "status": "transcript_ready",
        "transcript_path": "transcript.md",
        "coverage": "partial",
        "speaker_labels": "neutral",
        "timestamps": "partial",
        "adapter": "host-native",
        "limitations": ["The final segment is missing."],
    }
    run(validator, incomplete_recording, False, "partial recording cannot pass complete-transcript gate")

    unknown_evidence = copy.deepcopy(sample)
    unknown_evidence["decisions"][0]["evidence_ids"] = ["E999"]
    run(validator, unknown_evidence, False, "unknown decision evidence")

    suggestion_as_decision = copy.deepcopy(sample)
    decision_evidence_id = suggestion_as_decision["decisions"][0]["evidence_ids"][0]
    for item in suggestion_as_decision["evidence"]:
        if item["id"] == decision_evidence_id:
            item["type"] = "AI_SUGGESTION"
    run(validator, suggestion_as_decision, False, "AI suggestion promoted to decision")

    rejected_as_action = copy.deepcopy(sample)
    rejected_evidence_id = next(item["id"] for item in rejected_as_action["evidence"] if item["type"] in {"REJECTED_OPTION", "DEFERRED_OPTION"})
    rejected_as_action["actions"][0]["evidence_ids"] = [rejected_evidence_id]
    run(validator, rejected_as_action, False, "rejected work promoted to action")

    invented_precision = copy.deepcopy(sample)
    invented_precision["actions"][0].pop("definition_of_done")
    run(validator, invented_precision, False, "action missing definition-of-done field")

    silent_confirmation = copy.deepcopy(sample)
    silent_confirmation["understanding_checks"][0]["status"] = "assumed_aligned"
    run(validator, silent_confirmation, False, "silence treated as confirmation")

    print("ALL CONTRACT TESTS PASSED")


if __name__ == "__main__":
    main()
