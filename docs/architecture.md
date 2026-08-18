# Architecture

MeetingAlign is packaged as an inspectable Agent Skill, not as a hosted meeting bot. One authorized source becomes one governed, meeting-type-aware truth package, then role-specific views are derived from it. A recording must first become a complete, traceable transcript through a host-provided adapter.

```mermaid
flowchart TD
    A["Recording or transcript"] --> B{"Complete traceable transcript?"}
    B -- "No" --> X["INGESTION_BLOCKED"]
    B -- "Yes" --> C["Meeting type + outcome state"]
    C --> M["Evidence + decision maturity"]
    M --> D["Canonical Meeting Truth"]
    D --> E["Host View"]
    D --> F["Role Briefs"]
    D --> G["Alignment Gaps"]
    E --> H["Understanding checks"]
    F --> H
    G --> H
    H --> I{"Explicit authorization?"}
    I -- "No" --> J["Stop with local draft"]
    I -- "Yes" --> K["External handoff"]
```

## Components

- `SKILL.md` defines the operating workflow and authority boundary.
- `references/` contains evidence classification, role translation, gap detection, and output rules.
- `audio-ingestion.md` defines the recording adapter boundary and transcript quality gate.
- `meeting-type-and-outcome.md` defines the meeting taxonomy, expected output standards, mode transitions, and outcome states.
- `decision-maturity.md` prevents ideas, hypotheses, directional consensus, decisions, and committed actions from being conflated.
- `strategic-open-questions.md` preserves high-value uncertainty in strategy and discovery work.
- `role-guardrails.md` constrains role-specific boundaries to explicit evidence or direct execution implications.
- `meeting-align.schema.json` defines the machine-readable package.
- `validate_meeting_align.py` checks cross-reference and completeness invariants without third-party dependencies.
- `run_contract_tests.py` verifies that known failure modes are rejected.
- `tests/adversarial-contracts.json` and its runner encode T00–T15 as 16 synthetic golden contracts.
- `examples/launch-meeting/` provides a synthetic end-to-end fixture.

## Design invariants

1. **One truth, many views.** Every role brief derives from the same canonical Meeting Truth.
2. **Evidence before interpretation.** Decisions and facts require source pointers; inferences and AI suggestions remain explicitly labeled.
3. **Missing stays missing.** The system does not invent owners, deadlines, scope, dependencies, or definitions of done.
4. **Silence is pending.** Understanding is confirmed only by an explicit response.
5. **External action is gated.** Sending briefs, creating tasks, or writing organizational memory requires separate authorization.
6. **No transcript, no semantic truth.** A blocked or partial recording cannot produce meeting-wide decisions or actions.
7. **Meeting type before output standard.** Exploration is not penalized for lacking kickoff detail; execution is not excused from owners, timing, acceptance, and dependencies.
8. **Maturity cannot be promoted by tone.** Enthusiasm, repetition, politeness, and silence do not upgrade commitment.
9. **Guardrails require evidence.** Role boundaries come from explicit exclusions, rejected options, or direct execution implications—not generic advice.

## Trust boundary

The open package performs no network calls and contains no service credentials or speech-recognition engine. An agent environment may add transcription, storage, or collaboration integrations, but those integrations are outside this repository's trusted core and must preserve its evidence, privacy, and authorization rules.
