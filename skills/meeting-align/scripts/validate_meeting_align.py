#!/usr/bin/env python3
"""Validate a MeetingAlign JSON package without external dependencies."""

import json
import sys
from pathlib import Path


EVIDENCE_TYPES = {
    "CONFIRMED_DECISION", "CONFIRMED_FACT", "REJECTED_OPTION",
    "DEFERRED_OPTION", "OPEN_QUESTION", "ROLE_INFERENCE",
    "EXECUTION_IMPLICATION", "AI_SUGGESTION",
}
CONFIDENCE = {"high", "medium", "low"}
RISK = {"high", "medium", "low"}
GAP_TYPES = {
    "VAGUE_TIME", "VAGUE_QUALITY", "VAGUE_COMPLETION", "MISSING_OWNER",
    "MISSING_DEADLINE", "MISSING_DEFINITION_OF_DONE", "CONFLICTING_INTERPRETATION",
    "HIDDEN_DEPENDENCY", "MISSING_PARTICIPANT", "AUTHORITY_AMBIGUITY", "DECISION_DRIFT",
}
CHECK_STATUS = {"pending", "aligned", "needs_correction"}
REVIEW_STATUS = {"draft", "reviewed", "approved"}
SCHEMA_VERSIONS = {"1.0", "1.1"}
INPUT_TYPES = {"recording", "transcript", "detailed_record"}
INGESTION_STATUS = {"not_required", "transcript_ready", "blocked"}
COVERAGE = {"complete", "partial", "unknown"}
SPEAKER_LABELS = {"named", "neutral", "mixed", "unavailable"}
TIMESTAMP_STATUS = {"full", "partial", "unavailable"}


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def collect_ids(items, label, errors):
    ids = [item.get("id") for item in items]
    require(all(isinstance(item_id, str) and item_id for item_id in ids), f"{label} IDs must be non-empty strings", errors)
    require(len(ids) == len(set(ids)), f"{label} IDs must be unique", errors)
    return set(ids)


def validate(data):
    errors = []
    required = {
        "schema_version", "meeting", "evidence", "decisions", "rejected_or_deferred",
        "open_questions", "actions", "alignment_gaps", "roles", "understanding_checks",
        "review", "limitations",
    }
    require(required <= set(data), f"missing top-level fields: {sorted(required - set(data))}", errors)
    if errors:
        return errors

    schema_version = data.get("schema_version")
    require(schema_version in SCHEMA_VERSIONS, "schema_version must be 1.0 or 1.1", errors)

    ingestion = data.get("ingestion")
    if schema_version == "1.1":
        require(isinstance(ingestion, dict), "schema 1.1 requires ingestion object", errors)
    if isinstance(ingestion, dict):
        for field in ("input_type", "status", "transcript_path", "coverage", "speaker_labels", "timestamps", "adapter", "limitations"):
            require(field in ingestion, f"ingestion.{field} is required", errors)
        input_type = ingestion.get("input_type")
        status = ingestion.get("status")
        require(input_type in INPUT_TYPES, "ingestion.input_type is invalid", errors)
        require(status in INGESTION_STATUS, "ingestion.status is invalid", errors)
        require(ingestion.get("coverage") in COVERAGE, "ingestion.coverage is invalid", errors)
        require(ingestion.get("speaker_labels") in SPEAKER_LABELS, "ingestion.speaker_labels is invalid", errors)
        require(ingestion.get("timestamps") in TIMESTAMP_STATUS, "ingestion.timestamps is invalid", errors)
        require(bool(ingestion.get("adapter")), "ingestion.adapter is required", errors)
        require(isinstance(ingestion.get("limitations"), list), "ingestion.limitations must be an array", errors)

        if input_type == "recording":
            require(status in {"transcript_ready", "blocked"}, "recording ingestion must be transcript_ready or blocked", errors)
        else:
            require(status != "blocked", "non-recording input cannot use blocked ingestion status", errors)

        if status == "transcript_ready":
            require(bool(ingestion.get("transcript_path")), "transcript_ready requires ingestion.transcript_path", errors)
            require(ingestion.get("coverage") == "complete", "transcript_ready requires complete coverage", errors)

        if status == "blocked":
            semantic_sections = (
                "evidence", "decisions", "rejected_or_deferred", "open_questions",
                "actions", "alignment_gaps", "roles", "understanding_checks",
            )
            for section in semantic_sections:
                require(not data.get(section), f"blocked ingestion requires empty {section}", errors)
            require(data.get("alignment_score") is None, "blocked ingestion cannot include alignment_score", errors)
    meeting = data.get("meeting", {})
    for field in ("id", "title", "date", "purpose", "source_status"):
        require(bool(meeting.get(field)), f"meeting.{field} is required", errors)
    require(meeting.get("source_status") in {"complete", "partial", "unverified"}, "meeting.source_status is invalid", errors)

    evidence = data.get("evidence", [])
    evidence_ids = collect_ids(evidence, "evidence", errors)
    evidence_by_id = {item.get("id"): item for item in evidence}
    for item in evidence:
        item_id = item.get("id")
        require(item.get("type") in EVIDENCE_TYPES, f"evidence {item_id} has invalid type", errors)
        require(bool(item.get("text")), f"evidence {item_id} requires text", errors)
        require(bool(item.get("pointer")), f"evidence {item_id} requires pointer", errors)
        require(item.get("confidence") in CONFIDENCE, f"evidence {item_id} has invalid confidence", errors)

    for section in ("decisions", "rejected_or_deferred", "open_questions"):
        collect_ids(data.get(section, []), section, errors)
        for item in data.get(section, []):
            require(bool(item.get("statement")), f"{section} {item.get('id')} requires statement", errors)
            for evidence_id in item.get("evidence_ids", []):
                require(evidence_id in evidence_ids, f"{section} {item.get('id')} references unknown evidence {evidence_id}", errors)
            require(bool(item.get("evidence_ids")), f"{section} {item.get('id')} requires evidence_ids", errors)

    allowed_section_evidence = {
        "decisions": {"CONFIRMED_DECISION"},
        "rejected_or_deferred": {"REJECTED_OPTION", "DEFERRED_OPTION"},
        "open_questions": {"OPEN_QUESTION"},
    }
    for section, allowed_types in allowed_section_evidence.items():
        for item in data.get(section, []):
            for evidence_id in item.get("evidence_ids", []):
                evidence_type = evidence_by_id.get(evidence_id, {}).get("type")
                require(evidence_type in allowed_types, f"{section} {item.get('id')} references incompatible evidence {evidence_id}", errors)

    action_ids = collect_ids(data.get("actions", []), "action", errors)
    for item in data.get("actions", []):
        action_id = item.get("id")
        require(bool(item.get("action")), f"action {action_id} requires action text", errors)
        require("owner" in item, f"action {action_id} requires owner field", errors)
        require("deadline" in item, f"action {action_id} requires deadline field", errors)
        require("definition_of_done" in item, f"action {action_id} requires definition_of_done field", errors)
        require("dependencies" in item, f"action {action_id} requires dependencies field", errors)
        for evidence_id in item.get("evidence_ids", []):
            require(evidence_id in evidence_ids, f"action {action_id} references unknown evidence {evidence_id}", errors)
        require(bool(item.get("evidence_ids")), f"action {action_id} requires evidence_ids", errors)
        for evidence_id in item.get("evidence_ids", []):
            evidence_type = evidence_by_id.get(evidence_id, {}).get("type")
            require(evidence_type not in {"REJECTED_OPTION", "DEFERRED_OPTION", "OPEN_QUESTION", "AI_SUGGESTION"}, f"action {action_id} references non-action evidence {evidence_id}", errors)
        action_evidence_types = {evidence_by_id.get(evidence_id, {}).get("type") for evidence_id in item.get("evidence_ids", [])}
        require("CONFIRMED_DECISION" in action_evidence_types, f"action {action_id} requires confirmed-decision evidence", errors)

    gap_ids = collect_ids(data.get("alignment_gaps", []), "alignment gap", errors)
    for item in data.get("alignment_gaps", []):
        gap_id = item.get("id")
        require(item.get("type") in GAP_TYPES, f"alignment gap {gap_id} has invalid type", errors)
        require(item.get("risk") in RISK, f"alignment gap {gap_id} has invalid risk", errors)
        require(bool(item.get("what_is_missing")), f"alignment gap {gap_id} requires what_is_missing", errors)
        for evidence_id in item.get("evidence_ids", []):
            require(evidence_id in evidence_ids, f"alignment gap {gap_id} references unknown evidence {evidence_id}", errors)

    role_ids = collect_ids(data.get("roles", []), "role", errors)
    for item in data.get("roles", []):
        role_id = item.get("id")
        require(bool(item.get("name")), f"role {role_id} requires name", errors)
        require(bool(item.get("domain")), f"role {role_id} requires domain", errors)
        require(bool(item.get("brief_path")), f"role {role_id} requires brief_path", errors)
        for action_id in item.get("action_ids", []):
            require(action_id in action_ids, f"role {role_id} references unknown action {action_id}", errors)
        for gap_id in item.get("gap_ids", []):
            require(gap_id in gap_ids, f"role {role_id} references unknown gap {gap_id}", errors)

    checks = data.get("understanding_checks", [])
    collect_ids(checks, "understanding check", errors)
    for item in checks:
        check_id = item.get("id")
        require(item.get("role_id") in role_ids, f"understanding check {check_id} references unknown role", errors)
        require(bool(item.get("statement")), f"understanding check {check_id} requires statement", errors)
        require(item.get("status") in CHECK_STATUS, f"understanding check {check_id} has invalid status", errors)

    score = data.get("alignment_score")
    if score is not None:
        require(isinstance(score.get("total"), int) and 0 <= score.get("total") <= 100, "alignment_score.total must be an integer from 0 to 100", errors)
        require(bool(score.get("components")), "alignment_score.components must not be empty", errors)
        require(bool(score.get("disclaimer")), "alignment_score.disclaimer is required", errors)

    review = data.get("review", {})
    require(review.get("status") in REVIEW_STATUS, "review.status is invalid", errors)
    require(isinstance(review.get("external_actions_authorized"), bool), "review.external_actions_authorized must be boolean", errors)
    if isinstance(ingestion, dict) and ingestion.get("status") == "blocked":
        require(review.get("status") == "draft", "blocked ingestion review must remain draft", errors)
        require(review.get("external_actions_authorized") is False, "blocked ingestion cannot authorize external actions", errors)
    if review.get("status") == "approved":
        require(review.get("reviewer") not in {None, "", "not yet defined"}, "approved package requires a named reviewer", errors)

    require(bool(data.get("limitations")), "limitations must not be empty", errors)

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_meeting_align.py path/to/meeting-align.json")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read valid JSON: {exc}")
        raise SystemExit(1)
    errors = validate(data)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("PASS")
    print(f"Meeting: {data['meeting']['id']}")
    print(f"Decisions: {len(data['decisions'])}")
    print(f"Actions: {len(data['actions'])}")
    print(f"Alignment gaps: {len(data['alignment_gaps'])}")
    print(f"Roles: {len(data['roles'])}")


if __name__ == "__main__":
    main()
