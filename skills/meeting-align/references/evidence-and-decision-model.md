# Evidence and decision model

## Classification

| Type | Meaning | Treatment |
| --- | --- | --- |
| `CONFIRMED_DECISION` | The meeting clearly commits to a choice, scope, priority, owner, or action | May enter Meeting Truth as a decision |
| `CONFIRMED_FACT` | The meeting treats the statement as true and no conflict is visible | Record as a meeting fact, not necessarily external truth |
| `REJECTED_OPTION` | A proposed option is explicitly declined | Preserve under rejected/deferred; never turn into an action |
| `DEFERRED_OPTION` | A choice is postponed | Preserve with the next decision point when known |
| `OPEN_QUESTION` | The meeting leaves the matter unresolved | Keep open; do not complete it with AI judgment |
| `ROLE_INFERENCE` | A role or responsibility is inferred from context | Label inference and confidence |
| `EXECUTION_IMPLICATION` | A shared decision has a bounded professional implication for a role | May enter a role brief without changing the decision |
| `AI_SUGGESTION` | A useful action not decided in the meeting | Keep outside Meeting Truth unless a human approves it later |

## Decision test

Treat an item as a confirmed decision only when at least one of these is present:

- an authorized decision-maker explicitly confirms it;
- the group explicitly agrees and no later statement reverses it;
- an action, owner, or scope is assigned in decisive language;
- the host closes the topic with an unambiguous recap.

Do not treat these alone as confirmation:

- silence;
- politeness such as “got it”;
- brainstorming;
- one person's proposal;
- a repeated phrase without authority;
- a later role acting as if a decision existed.

## Conflict handling

When sources disagree:

1. preserve both statements and pointers;
2. check whether a later authorized statement resolves them;
3. if not resolved, classify the issue as `OPEN_QUESTION` and an alignment gap;
4. name the person or role that appears able to clarify, if supported;
5. do not choose the version that sounds more practical.

## Traceability

Use the shortest useful pointer:

- `Speaker · HH:MM:SS–HH:MM:SS`;
- `Speaker · nearby quote fragment`;
- `Transcript section / paragraph`.

Every major decision, rejected option, action, and high-risk gap needs a pointer. Routine context may be summarized without citation when it cannot change execution.
