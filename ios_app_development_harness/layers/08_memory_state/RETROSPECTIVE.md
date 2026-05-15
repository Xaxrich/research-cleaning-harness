# RETROSPECTIVE

Use this file to improve the harness while building real apps.

## When To Update

Update after:

- a task feels ambiguous
- a verification gate is too weak or too heavy
- the user must correct the agent's process
- the agent is blocked by missing context
- a module is accepted or rejected

## Entry Format

```markdown
## <date> <task_id>

What worked:
- 

What was confusing:
- 

Quality risk:
- 

Proposed harness improvement:
- 

Status:
proposed | accepted | rejected | implemented
```

## Rule

Retrospective entries are not task completion evidence by themselves. They are inputs for future harness iteration.

## 2026-05-14 TASK-002

What worked:
- Existing layered structure made it easy to add planning and verification policies without replacing the harness.
- `validate_harness.py` gave a quick structural check after adding required files.

What was confusing:
- The harness had no explicit bootstrap path for improving itself when `STATE.md` had no active task.
- `TASKS.md` mixed planning and execution concerns, which encouraged task cards too early.

Quality risk:
- Documentation gates only work if agents and users consistently follow them; runtime enforcement is still light.

Proposed harness improvement:
- Add future scripts to validate active task cards, confirmation status, verification level, and run trace completeness.

Status:
implemented

## 2026-05-14 TASK-002 Standard Gate Reply Example

What worked:
- The protocol was clear enough to turn into a concrete prompt example.

What was confusing:
- Without an example, Cursor may still comply unevenly with the gate format.

Quality risk:
- Examples can drift from protocol if not validated or reviewed with later protocol changes.

Proposed harness improvement:
- Keep a standard gate reply example in `layers/10_examples/codex_prompts.md` and include key phrases in `validate_harness.py`.

Status:
implemented

## 2026-05-14 TASK-002 Document Target Follow-up

What worked:
- The gate protocol could absorb another interaction improvement without expanding the main workflow.

What was confusing:
- With many harness files, users still may not know which document to inspect or which section their answer affects.

Quality risk:
- A user may confirm the wrong level of decision if the prompt does not name the stage, document, and exact section.

Proposed harness improvement:
- Require gate responses to name the current stage, review document, decision target, and exact item being confirmed.

Status:
implemented

## 2026-05-14 TASK-002 Decision Placement Follow-up

What worked:
- The gate protocol provided a place to improve interaction shape without changing product-specific files.

What was confusing:
- Putting `User action needed` at the top still made the user feel asked to decide before reading the evidence.

Quality risk:
- If the decision request appears before context, users may confirm without understanding what changed or what is still out of scope.

Proposed harness improvement:
- Require gate responses to end with a single `Decision needed` block and forbid extra content after it.

Status:
implemented

## 2026-05-14 TASK-002 Gate Clarity Follow-up

What worked:
- The user caught the real UX failure early: gate files existed, but the response format still let agents mix multiple decisions.

What was confusing:
- A reply could say "these decisions remain" and still ask the user to reply `confirmed`, which makes the gate boundary ambiguous.

Quality risk:
- Without an explicit output protocol, different agents may comply with the documents structurally while still giving users unclear mixed-status replies.

Proposed harness improvement:
- Require a `Gate / Status / User action needed` header and one user action per confirmation response.

Status:
implemented
