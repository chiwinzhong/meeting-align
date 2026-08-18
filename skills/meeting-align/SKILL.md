---
name: meeting-align
description: Turn a complete meeting recording, transcript, or detailed record into a traceable, meeting-type-aware Meeting Truth, decision-maturity map, Host View, role briefs and guardrails, strategic open questions, alignment gaps, and understanding checks. Use when a team needs to safely transcribe audio or video before interpretation; distinguish ideas, hypotheses, directional consensus, confirmed decisions, and committed actions; adapt output standards for strategy, decision, kickoff, execution, review, sales, discovery, or brainstorming meetings; expose maturity or readiness mismatches; or translate shared truth across roles without forcing every meeting into an action list. Do not use it to invent transcript coverage, speaker identity, decision maturity, owners, deadlines, acceptance criteria, authority, guardrails, or performance judgments, and do not send briefs or update systems without explicit authorization.
---

# MeetingAlign

Do not merely summarize the meeting. Align the people around one shared, traceable interpretation.

## Required outcome

Produce a governed package containing:

1. a traceable `transcript.md` when the source is a recording;
2. one `meeting-type.md` describing type, confidence, expected output standard, and outcome state;
3. one canonical `meeting-truth.md` separating maturity levels;
4. one `host-view.md` focused on the control needs of that meeting type;
5. one `alignment-gaps.md` showing only material ambiguity or maturity/readiness mismatch;
6. one brief and evidence-based guardrail set for each key role;
7. lightweight understanding checks;
8. source pointers for major decisions, maturity upgrades, guardrails, and gaps;
9. optional `meeting-align.json` for validation and downstream handoff.

All derivatives must use the same Meeting Truth. Never create a different underlying decision for a different role.

## Guardrails

- Treat a transcript as a source record, not proof that every statement is correct.
- Separate decisions, facts, rejected or deferred options, open questions, role inferences, execution implications, and AI suggestions.
- Treat implied consensus as an inference until the transcript clearly confirms it.
- Do not convert `ASAP`, `ready`, `premium`, `better`, `run it through`, or `close the loop` into invented precision.
- Do not assign a new owner, deadline, scope, or acceptance criterion because it seems reasonable.
- Do not force a strategy or discovery meeting into a kickoff-style action list.
- Do not promote an idea, hypothesis, or directional consensus into a confirmed decision or committed action.
- Keep rejected and deferred options out of action lists.
- Preserve missing owners, deadlines, definitions of done, and dependencies as visible gaps.
- Do not infer intelligence, competence, attitude, or employee performance.
- Do not expose confidential meeting content beyond the authorized audience.
- Do not guess participant identity from voice alone or infer protected or biometric traits.
- Do not upload a recording to an external transcription service without authority to process it there.
- Do not send briefs, update project tools, create tasks, or publish any output without explicit human authorization.

## Step 1 — Establish the meeting contract

Determine from the input:

- meeting title, date, purpose, and scope;
- transcript completeness and whether speaker or timestamp labels exist;
- participant names and roles when supplied or reliably stated;
- requested outputs and intended audience;
- confidentiality, redaction, and storage requirements;
- whether an authorized host or decision-maker will review the package.
- whether the operator is authorized to record, transcribe, retain, and process the source in the selected environment.

Classify the input as `recording`, `transcript`, or `detailed_record`.

Ask for clarification only when missing information would materially change a major decision, owner, scope, high-risk action, or confidential distribution boundary. Continue with `not yet defined` for ordinary gaps.

## Step 2 — Ingest raw audio or video safely

Run this step only for a raw recording. Read [references/audio-ingestion.md](references/audio-ingestion.md) before processing it.

- Use a reliable transcription capability already available in the authorized runtime; do not require one named provider.
- Preserve chronological order, speaker turns, useful timestamps, corrections, reversals, disagreement, mixed-language source wording, and explicit uncertainty markers.
- Use supplied names only when mapping is reliable. Otherwise use neutral labels such as `Speaker A` and `Speaker B`.
- Reassemble long recordings into one ordered transcript before interpreting the meeting.
- Never substitute an upstream audio summary for a traceable transcript.

Enter semantic analysis only when transcript coverage is sufficient to support meeting-wide decisions. If it is not, return:

`INGESTION_BLOCKED — Raw recording received, but no reliable complete transcription is available in the current runtime.`

Then stop. Do not infer Meeting Truth, actions, owners, or gaps from metadata, isolated samples, or a partial audio summary.

## Step 3 — Detect meeting type before extracting actions

Read [references/meeting-type-and-outcome.md](references/meeting-type-and-outcome.md).

Identify one primary meeting type, optional secondary types, confidence, a one-sentence evidence-based rationale, and the expected output standard. Note mode transitions when a meeting moves from exploration into decision or execution.

Treat the type as an interpretation aid, not a rigid label. A strategy meeting may succeed with direction and explicit open questions; a kickoff requires substantially clearer owners, timing, acceptance, and handoffs.

## Step 4 — Reconstruct before summarizing

Read the complete transcript. Identify:

1. why the meeting happened;
2. decisions that were actually made;
3. facts the meeting treated as true;
4. proposals that were rejected or deferred;
5. issues that remain open;
6. actions, owners, deadlines, definitions of done, and dependencies;
7. shared success criteria and governing execution principles;
8. statements that remain suggestions, hypotheses, or inferences.
9. broad directions or boundaries that participants share but have not operationalized;
10. whether participants share direction but differ on readiness to act.

Read [references/evidence-and-decision-model.md](references/evidence-and-decision-model.md) and apply its classification rules. Preserve a short speaker/timestamp or section pointer for every high-impact decision and gap.

## Step 5 — Classify decision maturity and outcome state

Read [references/decision-maturity.md](references/decision-maturity.md).

Assign the highest evidence-supported maturity to each important statement:

- `IDEA`
- `HYPOTHESIS`
- `DIRECTIONAL_CONSENSUS`
- `CONFIRMED_DECISION`
- `COMMITTED_ACTION`

Use the latest supported state while preserving the earlier path in source pointers. Then select one outcome state: `EXPLORING`, `DIRECTION_SET`, `EXECUTION_READY`, `IN_EXECUTION`, or `REVIEWING`.

Do not treat politeness, silence, enthusiasm, or repeated discussion as a maturity upgrade.

## Step 6 — Build one Meeting Truth

Create the canonical fact base before writing role briefs.

Include:

- meeting type, confidence, expected output standard, and outcome state;
- meeting purpose;
- ideas and hypotheses that materially shaped the meeting;
- directional consensus and strategic boundaries;
- confirmed decisions;
- committed actions;
- confirmed facts;
- explicitly rejected or deferred options;
- open questions;
- actions with owner, deadline, definition of done, dependency, evidence pointer, and confidence;
- shared definition of success;
- main execution principle;
- ranked strategic open questions when they block movement toward execution;
- package limitations and review status.

Mark missing fields `not yet defined`. If two speakers conflict, preserve both positions and classify the item as open unless a later statement clearly resolves it.

## Step 7 — Identify key roles

Classify relevant participants by meeting function:

- Decision Maker
- Meeting Host
- Owner
- Executor
- Collaborator
- Reviewer / Approver
- Informed Stakeholder

Infer a professional domain only when the transcript supports it. Read [references/role-translation.md](references/role-translation.md) before generating role briefs.

If a critical owner cannot be inferred, expose the missing-owner gap. Do not ask the user to label every participant by default.

## Step 8 — Detect material alignment gaps

Read [references/alignment-gaps-and-score.md](references/alignment-gaps-and-score.md).

Check for:

- vague time;
- vague quality;
- vague completion;
- missing owner;
- missing definition of done;
- conflicting interpretations;
- hidden dependency;
- affected but unrepresented role;
- authority ambiguity;
- decision or scope drift inside the meeting.
- maturity mismatch, when participants assign different commitment levels to the same direction;
- readiness mismatch, when direction is shared but readiness to build, launch, sell, or operationalize differs.

For each material gap record:

1. the phrase or decision;
2. why interpretations may diverge;
3. what the meeting already clarifies;
4. what remains undefined;
5. the likely consequence;
6. who should clarify it, when inferable;
7. an evidence pointer.

Do not flag harmless conversational ambiguity. Prioritize the smallest set of gaps capable of changing execution.

## Step 9 — Generate the Host View

Create a compact control surface, not another narrative summary.

Include:

1. meeting type and outcome state;
2. what direction is already aligned;
3. decision-maturity map for the most important items;
4. what was decided and explicitly not decided;
5. who owns what;
6. definitions of done, dependencies, and handoffs when execution requires them;
7. ranked open questions and the next validation step;
8. high-risk alignment gaps, including maturity or readiness mismatch;
9. understanding-confirmation status, when collected;
10. optional meeting-type-aware Alignment Score and separate Execution Readiness.

Lead with the few issues most likely to break execution.

For strategy or co-creation, read [references/strategic-open-questions.md](references/strategic-open-questions.md) and lead with direction, boundaries, hypotheses, blocking questions, and next validation. Do not penalize missing deadlines that are not yet appropriate.

## Step 10 — Generate role briefs

For each key execution role, answer exactly these six questions:

1. **What matters to you** — meeting content relevant to this role.
2. **What it means for your role** — professional implications of the shared decision.
3. **What you need to do** — concrete actions supported by the transcript.
4. **What matters most** — the priority or interpretation that must not drift.
5. **Definition of done** — the meeting's stated criterion, or `not yet defined`.
6. **Who you depend on** — inputs, approvers, collaborators, and downstream handoffs.

Then add:

- **Don't / Guardrail** — one or two evidence-based boundaries when supported;
- **Alignment gap for this role** — the most relevant unresolved ambiguity;
- **Understanding check** — adapt it to the meeting type.

Read [references/role-guardrails.md](references/role-guardrails.md) before adding a guardrail. Never invent a prohibition as generic management advice.

For execution-ready work use: `My understanding: I own X, by Y, and done means Z.`

For strategic work use: `My understanding: we are aligned on X; my role is Y; before execution, Z still needs to be decided or validated.`

If X, Y, or Z is missing, write `not yet defined`. Offer only:

- ✅ Aligned
- ⚠️ Needs correction

Translate shared decisions into role implications without rewriting the facts or inventing a strategy.

## Step 11 — Use meeting-type-aware scores carefully

The score is optional. Use it only when the user or host wants a compact diagnostic.

- Select the scoring profile before assigning weights.
- For strategy, emphasize direction, boundaries, maturity visibility, open questions, role complementarity, and next validation.
- For kickoff or execution, emphasize decisions, owners, deadlines, definitions of done, blockers, dependencies, and handoffs.
- When useful, show Alignment Score and Execution Readiness as separate indicators.
- Explain every deduction and list the gaps that would improve the score.
- Do not present it as a scientific measure of people, culture, intelligence, competence, or organizational performance.
- Never use it for employee ranking, compensation, discipline, or surveillance.

## Step 12 — Validate the package

Use the human-readable structure in [references/output-contract.md](references/output-contract.md). When structured output is requested, conform to [references/meeting-align.schema.json](references/meeting-align.schema.json).

Validate JSON with:

```bash
python3 scripts/validate_meeting_align.py path/to/meeting-align.json
```

Fix every contract failure before presenting a package as reviewed or ready for downstream use.

## Step 13 — Stop at the external-action gate

MeetingAlign may prepare files and understanding checks. It may not:

- send role briefs;
- collect responses;
- create or change tasks in project systems;
- notify employees or external parties;
- update permanent organizational memory;
- treat silence as confirmation.

Require explicit authorization for the exact audience, channel, and action. Record corrections before promoting the package from `draft` to `reviewed` or `approved`.

## Quality check

Before delivery, verify:

- raw recordings passed the ingestion quality gate before semantic analysis;
- the transcript preserves source order, uncertainty, and neutral speaker labeling where identity is unverified;
- meeting type and expected output standard are set before action extraction;
- decision maturity and outcome state are not overstated;
- directional consensus is visibly separate from confirmed decisions and committed actions;
- every role brief derives from the same Meeting Truth;
- every major decision has a source pointer;
- discussion, proposals, decisions, and actions remain distinct;
- rejected options are not actions;
- open questions remain open;
- missing owners, deadlines, definitions of done, and dependencies are visible;
- no gap has been silently repaired with invented precision;
- strategic open questions remain open and ranked by blocking power;
- role guardrails trace to exclusions, rejections, boundaries, or necessary execution implications;
- strategy meetings are not penalized merely for lacking kickoff-level deadlines;
- role briefs remain readable in under three minutes;
- understanding confirmation requires one click or one short response;
- sensitive content is limited to the authorized package;
- external actions remain unexecuted unless explicitly authorized.
