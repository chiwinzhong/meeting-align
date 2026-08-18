# Output contract

## Package structure

```text
meeting-package/
├── transcript.md             # when the source is a recording
├── meeting-type.md
├── meeting-truth.md
├── host-view.md
├── alignment-gaps.md
├── understanding-checks.md
├── roles/
│   └── <role>.md
└── meeting-align.json
```

## `transcript.md`

For recording inputs, preserve chronological order, speaker turns, useful timestamps, uncertainty markers, and source-language wording where meaning could drift. Do not enter semantic analysis when reliable complete transcription is unavailable.

## `meeting-type.md`

Record the primary type, optional secondary types, confidence, evidence-based rationale, expected output standard, outcome state, and any material mode transition. The label guides the output contract; it does not override transcript evidence.

## `meeting-truth.md`

Use this order:

1. status and review owner;
2. meeting type, expected standard, and outcome state;
3. meeting purpose;
4. important ideas, hypotheses, and directional consensus;
5. decision-maturity map;
6. confirmed decisions and committed actions;
7. confirmed facts;
8. rejected or deferred options;
9. open questions and ranked strategic open questions when applicable;
10. action table;
11. shared definition of success;
12. main execution principle;
13. limitations and evidence note.

Action table fields:

| Action | Owner | Deadline | Definition of done | Dependency | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- |

## `host-view.md`

Keep it compact. Lead with meeting type, outcome state, direction, maturity, and the highest-risk control needs. Then list decisions, owners, definitions of done, dependencies, ranked open questions, missing fields, confirmation status, and optional meeting-type-aware scores.

## `alignment-gaps.md`

For each gap, including maturity or readiness mismatch, record:

- ID and risk;
- phrase or decision;
- split interpretations;
- what is known;
- what is missing;
- likely consequence;
- clarification owner;
- evidence pointer;
- status.

## `roles/<role>.md`

Answer the required six questions in the Skill, followed by evidence-based `Don't / Guardrail` boundaries when supported, one role-specific gap, and one understanding check. Keep the brief usable in under three minutes.

## `understanding-checks.md`

Collect the exact one-sentence checks and one of three states:

- `pending`
- `aligned`
- `needs_correction`

Silence remains `pending`.

## `meeting-align.json`

Use [meeting-align.schema.json](meeting-align.schema.json). Schema `1.1` adds the `ingestion` quality gate. Schema `1.2` adds `meeting_semantics`, decision maturity, directional consensus, strategic open questions, role guardrails, meeting-type-aware score profiles, and optional separate Execution Readiness. A blocked recording must contain no semantic meeting output.

Structured output exists for validation and handoff; Markdown remains the human-facing package.
