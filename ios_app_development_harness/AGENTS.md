# AGENTS

You are operating inside an iOS App Development Harness.

## Required Read Order

1. `START_HERE.md`
2. `CALL_GRAPH.md`
3. `layers/08_memory_state/STATE.md`
4. Current task in `layers/01_task/TASKS.md`
5. `layers/00_goal/DISCOVERY_GATE.md`
6. `layers/00_goal/PRODUCT_BRIEF.md`
7. `layers/01_planning/SOLUTION_PLAN.md`
8. `layers/01_planning/TASK_BREAKDOWN.md`
9. `layers/01_planning/USER_CONFIRMATION.md`
10. `layers/01_planning/GATE_OUTPUT_PROTOCOL.md`
11. `layers/02_context/CONTEXT_INDEX.md`
12. `layers/03_file_scope/FILE_SCOPE_RULES.md`
13. `layers/06_verification/VERIFICATION_MATRIX.md`
14. `layers/06_verification/MODULE_VERIFICATION_POLICY.md`
15. `layers/06_verification/SIMULATOR_TEST_POLICY.md`
16. `layers/07_risk_release/RISK_CONTROL.md`

## Non-Negotiable Rules

1. Do not implement product behavior before `DISCOVERY_GATE.md` and `PRODUCT_BRIEF.md` are satisfied.
2. Do not create implementation task cards before `SOLUTION_PLAN.md`, `TASK_BREAKDOWN.md`, and `USER_CONFIRMATION.md` are satisfied.
3. Use `GATE_OUTPUT_PROTOCOL.md` whenever asking for user confirmation or a user decision.
4. Ask for exactly one user action per gate response.
5. Every gate response must state the current stage, review document, decision record target, and exact thing being confirmed.
6. Put the requested user action in the final `需要你决定` block, after status, evidence, files, and verification.
7. Do not ask for `confirmed` while the same gate still has blocking open questions.
8. Start execution from an active task card.
9. Only edit `allowed_files`.
10. Treat `read_only_files` as read-only.
11. Do not touch `forbidden_files` without explicit approval.
12. Search before broad reading.
13. View before edit.
14. Run task-specific verification before completion.
15. Meet the task's declared verification level.
16. Run simulator/device checks when required by `SIMULATOR_TEST_POLICY.md`.
17. Record failures in `layers/08_memory_state/FAILURE_LOG.md`.
18. Record task execution in `layers/08_memory_state/RUN_TRACE.md`.
19. Use review/risk gates for high-risk work.
20. Never perform release/signing/upload actions without manual approval.

## Completion Response Must Include

- Files changed.
- Verification commands run.
- Result of each command.
- Verification level met, including simulator/device evidence when applicable.
- Remaining risks.
- Whether review/manual approval is required.
