# Output contract

## Package structure

```text
meeting-package/
├── meeting-truth.md
├── host-view.md
├── alignment-gaps.md
├── understanding-checks.md
├── roles/
│   └── <role>.md
└── meeting-align.json
```

## `meeting-truth.md`

Use this order:

1. status and review owner;
2. meeting purpose;
3. confirmed decisions;
4. confirmed facts;
5. rejected or deferred options;
6. open questions;
7. action table;
8. shared definition of success;
9. main execution principle;
10. limitations and evidence note.

Action table fields:

| Action | Owner | Deadline | Definition of done | Dependency | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- |

## `host-view.md`

Keep it compact. Lead with high-risk gaps, then list decisions, owners, definitions of done, dependencies, open questions, missing fields, confirmation status, and optional score.

## `alignment-gaps.md`

For each gap record:

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

Answer the required six questions in the Skill, followed by one role-specific gap and one understanding check. Keep the brief usable in under three minutes.

## `understanding-checks.md`

Collect the exact one-sentence checks and one of three states:

- `pending`
- `aligned`
- `needs_correction`

Silence remains `pending`.

## `meeting-align.json`

Use [meeting-align.schema.json](meeting-align.schema.json). Structured output exists for validation and handoff; Markdown remains the human-facing package.
