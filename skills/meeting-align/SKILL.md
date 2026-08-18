---
name: meeting-align
description: Turn a complete meeting transcript, recording transcript, or detailed meeting record into one traceable Meeting Truth, a host control view, role-specific action briefs, visible alignment gaps, and lightweight understanding checks. Use when a team needs to distinguish decisions from discussion, translate one shared decision for product, engineering, design, marketing, sales, operations, or other roles, expose vague deadlines and definitions of done, document dependencies, or prevent everyone from leaving the same meeting with different meanings. Do not use it to invent decisions, owners, deadlines, acceptance criteria, authority, or employee-performance judgments, and do not send briefs or update project systems without explicit authorization.
---

# MeetingAlign

Do not merely summarize the meeting. Align the people around one shared, traceable interpretation.

## Required outcome

Produce a governed package containing:

1. one canonical `meeting-truth.md`;
2. one `host-view.md` focused on execution control;
3. one `alignment-gaps.md` showing only material ambiguity;
4. one brief for each key execution role;
5. lightweight understanding checks;
6. source pointers for major decisions and gaps;
7. optional `meeting-align.json` for validation and downstream handoff.

All derivatives must use the same Meeting Truth. Never create a different underlying decision for a different role.

## Guardrails

- Treat a transcript as a source record, not proof that every statement is correct.
- Separate decisions, facts, rejected or deferred options, open questions, role inferences, execution implications, and AI suggestions.
- Treat implied consensus as an inference until the transcript clearly confirms it.
- Do not convert `ASAP`, `ready`, `premium`, `better`, `run it through`, or `close the loop` into invented precision.
- Do not assign a new owner, deadline, scope, or acceptance criterion because it seems reasonable.
- Keep rejected and deferred options out of action lists.
- Preserve missing owners, deadlines, definitions of done, and dependencies as visible gaps.
- Do not infer intelligence, competence, attitude, or employee performance.
- Do not expose confidential meeting content beyond the authorized audience.
- Do not send briefs, update project tools, create tasks, or publish any output without explicit human authorization.

## Step 1 — Establish the meeting contract

Determine from the input:

- meeting title, date, purpose, and scope;
- transcript completeness and whether speaker or timestamp labels exist;
- participant names and roles when supplied or reliably stated;
- requested outputs and intended audience;
- confidentiality, redaction, and storage requirements;
- whether an authorized host or decision-maker will review the package.

If only audio or video is supplied, transcribe it when the environment has a reliable transcription capability. Otherwise request a transcript and state the limitation. Never claim to have reviewed audio that was not processed.

Ask for clarification only when missing information would materially change a major decision, owner, scope, high-risk action, or confidential distribution boundary. Continue with `not yet defined` for ordinary gaps.

## Step 2 — Reconstruct before summarizing

Read the complete transcript. Identify:

1. why the meeting happened;
2. decisions that were actually made;
3. facts the meeting treated as true;
4. proposals that were rejected or deferred;
5. issues that remain open;
6. actions, owners, deadlines, definitions of done, and dependencies;
7. shared success criteria and governing execution principles;
8. statements that remain suggestions, hypotheses, or inferences.

Read [references/evidence-and-decision-model.md](references/evidence-and-decision-model.md) and apply its classification rules. Preserve a short speaker/timestamp or section pointer for every high-impact decision and gap.

## Step 3 — Build one Meeting Truth

Create the canonical fact base before writing role briefs.

Include:

- meeting purpose;
- confirmed decisions;
- confirmed facts;
- explicitly rejected or deferred options;
- open questions;
- actions with owner, deadline, definition of done, dependency, evidence pointer, and confidence;
- shared definition of success;
- main execution principle;
- package limitations and review status.

Mark missing fields `not yet defined`. If two speakers conflict, preserve both positions and classify the item as open unless a later statement clearly resolves it.

## Step 4 — Identify key roles

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

## Step 5 — Detect material alignment gaps

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

For each material gap record:

1. the phrase or decision;
2. why interpretations may diverge;
3. what the meeting already clarifies;
4. what remains undefined;
5. the likely consequence;
6. who should clarify it, when inferable;
7. an evidence pointer.

Do not flag harmless conversational ambiguity. Prioritize the smallest set of gaps capable of changing execution.

## Step 6 — Generate the Host View

Create a compact control surface, not another narrative summary.

Include:

1. what was decided;
2. what was explicitly not decided;
3. who owns what;
4. definitions of done;
5. dependencies and handoffs;
6. open questions;
7. high-risk alignment gaps;
8. missing owners or deadlines;
9. understanding-confirmation status, when collected;
10. optional explanatory Alignment Score.

Lead with the few issues most likely to break execution.

## Step 7 — Generate role briefs

For each key execution role, answer exactly these six questions:

1. **What matters to you** — meeting content relevant to this role.
2. **What it means for your role** — professional implications of the shared decision.
3. **What you need to do** — concrete actions supported by the transcript.
4. **What matters most** — the priority or interpretation that must not drift.
5. **Definition of done** — the meeting's stated criterion, or `not yet defined`.
6. **Who you depend on** — inputs, approvers, collaborators, and downstream handoffs.

Then add:

- **Alignment gap for this role** — the most relevant unresolved ambiguity;
- **Understanding check** — `My understanding: I own X, by Y, and done means Z.`

If X, Y, or Z is missing, write `not yet defined`. Offer only:

- ✅ Aligned
- ⚠️ Needs correction

Translate shared decisions into role implications without rewriting the facts or inventing a strategy.

## Step 8 — Use the Alignment Score carefully

The score is optional. Use it only when the user or host wants a compact diagnostic.

- Score decision, ownership, deadline, definition-of-done, dependency, and cross-role clarity.
- Explain every deduction and list the gaps that would improve the score.
- Do not present it as a scientific measure of people, culture, intelligence, competence, or organizational performance.
- Never use it for employee ranking, compensation, discipline, or surveillance.

## Step 9 — Validate the package

Use the human-readable structure in [references/output-contract.md](references/output-contract.md). When structured output is requested, conform to [references/meeting-align.schema.json](references/meeting-align.schema.json).

Validate JSON with:

```bash
python3 scripts/validate_meeting_align.py path/to/meeting-align.json
```

Fix every contract failure before presenting a package as reviewed or ready for downstream use.

## Step 10 — Stop at the external-action gate

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

- every role brief derives from the same Meeting Truth;
- every major decision has a source pointer;
- discussion, proposals, decisions, and actions remain distinct;
- rejected options are not actions;
- open questions remain open;
- missing owners, deadlines, definitions of done, and dependencies are visible;
- no gap has been silently repaired with invented precision;
- role briefs remain readable in under three minutes;
- understanding confirmation requires one click or one short response;
- sensitive content is limited to the authorized package;
- external actions remain unexecuted unless explicitly authorized.
