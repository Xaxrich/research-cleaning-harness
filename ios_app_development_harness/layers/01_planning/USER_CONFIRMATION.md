# USER CONFIRMATION

The user is the product owner. The agent must stop for confirmation at these gates.

All confirmation prompts must follow `GATE_OUTPUT_PROTOCOL.md`.
User-facing confirmation prompts must be in Chinese by default.

## Confirmation Gates

1. Product brief confirmation:
   - Is the problem, MVP scope, non-goals, and privacy boundary correct?

2. Solution plan confirmation:
   - Is the architecture and module order acceptable?

3. Task breakdown confirmation:
   - Is the task sequence correct before implementation starts?

4. Verification strategy confirmation:
   - Are the simulator, device, unit, and manual checks appropriate?

5. High-risk action confirmation:
   - Required before signing, upload, destructive commands, production backend changes, or credential access.

## Confirmation Format

Use one of these statuses:

```text
not_requested
requested
confirmed
changes_requested
waived_by_user
```

If a confirmation is waived, record the waiver in `layers/08_memory_state/DECISIONS.md` or the active run trace.

## Single-action Rule

When asking for confirmation, do not also ask the user to resolve unrelated open questions.

If an open question blocks the gate, ask that question first. Ask for confirmation only after the open question is resolved and reflected in the relevant gate document.

## Decision Placement Rule

Place the user-facing decision request at the end of the response in the `## 需要你决定` block defined by `GATE_OUTPUT_PROTOCOL.md`.

Do not start the response with the requested action. The user should first see the gate, status, confirmed context, open blocker, file changes, and verification evidence.

## Document Target Rule

Every confirmation request must name:

- 当前阶段
- 你要看的文档
- 回答后会写入的文档
- 本次确认什么

If the user cannot tell which document to inspect and what field or section will change, the confirmation request is invalid.
