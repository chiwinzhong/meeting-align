# Audio and video ingestion

Read this reference whenever the source is a raw recording.

## Boundary

MeetingAlign performs alignment reasoning. Speech recognition is an input adapter supplied by the host environment or an authorized external service.

```text
recording → authorized transcription adapter → traceable transcript → MeetingAlign core
```

Do not claim built-in transcription. Do not select or upload to an external service without authorization.

## Minimum transcript contract

Preserve:

- chronological order;
- speaker turns;
- timestamps or time ranges useful for traceability;
- corrections, reversals, disagreement, and rejected proposals;
- uncertainty such as `[inaudible 32:14–32:22]`;
- source-language wording when translation could change meaning;
- sequential coverage across the complete recording.

Use participant names only when supplied and reliably mapped. Otherwise assign neutral labels. Never identify a person from voice alone or infer age, gender, ethnicity, health, emotion, or other sensitive traits.

## Quality gate

Set one status:

- `transcript_ready` — a complete, ordered working transcript exists and supports meeting-wide interpretation;
- `blocked` — reliable complete transcription is unavailable.

If blocked, preserve known metadata and limitations, but keep decisions, actions, gaps, roles, and understanding checks empty. Return the exact `INGESTION_BLOCKED` status defined in `SKILL.md`.

A partial transcript may support an explicitly scoped excerpt analysis, but it must not be represented as the truth of the complete meeting.

## Retention and authorization

Before processing a recording, confirm that the operator is authorized to record, transcribe, retain, and process it in the chosen environment. Prefer approved local or organizational workflows for sensitive meetings. Delete unnecessary intermediate audio chunks and temporary transcripts according to the authorized retention policy.
