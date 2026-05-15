# RUN TRACE

Run trace records how the harness was used, not just what code changed.

Create one trace entry per meaningful task or module.

## Required Fields

| field | purpose |
|---|---|
| task_id | active task |
| timestamp | when the trace was written |
| context_read | files and evidence consulted |
| harness_rules_applied | gates and rules that controlled the work |
| reasoning_summary | concise rationale, without private chain-of-thought |
| actions_taken | files changed and commands run |
| verification_evidence | command results, simulator evidence, or blocked checks |
| usability_notes | where the harness helped or got in the way |
| next_step | next bounded action |

## Privacy Rule

Do not record secrets, credentials, personal user data, or raw private app content. Summarize sensitive evidence instead.

## Template

```markdown
## <timestamp> <task_id>

context_read:
- 

harness_rules_applied:
- 

reasoning_summary:

actions_taken:
- 

verification_evidence:
- 

usability_notes:
- 

next_step:
- 
```

## 2026-05-14 TASK-002

context_read:
- Current harness entry files: `START_HERE.md`, `CALL_GRAPH.md`, `AGENTS.md`, `STATE.md`, `TASKS.md`, `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, `VERIFICATION_MATRIX.md`, `RISK_CONTROL.md`.
- Framework synthesis outputs: `superpowers_summary.md`, `gstack_summary.md`, `aider_summary.md`, `gsd2_summary.md`, `swe_agent_summary.md`.
- Mechanism synthesis outputs: `skills_and_process.md`, `task_state_machine.md`, `verification.md`, `repo_context.md`, `agent_roles.md`, `aci_tools.md`, `risk_gate.md`.

harness_rules_applied:
- Start from an active task card.
- Only edit `allowed_files`.
- Add verification evidence before completion.
- Record execution trace for harness usability.

reasoning_summary:
The original harness had strong file-scope and risk controls but did not strongly prevent premature implementation or weak module validation. TASK-002 adds discovery, product confirmation, planning confirmation, task breakdown, verification-level policy, simulator policy, and run trace evidence.

actions_taken:
- Added discovery and product brief gates.
- Added planning layer with solution plan, task breakdown, user confirmation, and module plan template.
- Extended task card fields.
- Added module verification, simulator test, and acceptance checklist policies.
- Added run trace and retrospective records.
- Updated entry docs, call graph, context/file-scope rules, workflow, and validator.

verification_evidence:
- `python3 scripts/validate_harness.py`: pass.
- `git diff --stat -- ios_app_development_harness`: showed only harness changes.
- `git status --short`: showed tracked/untracked harness files only.

usability_notes:
- The previous `current_task: none` state made legitimate harness evolution awkward. TASK-002 documents the bootstrap boundary explicitly.
- The new flow should make users confirm product and plan decisions before agents create implementation tasks.

next_step:
- Run final TASK-002 verification.
- Review the framework diff before committing or using the harness in Cursor.

## 2026-05-14 TASK-002 Gate Clarity Follow-up

context_read:
- User feedback: an actual Cursor run mixed confirmed conclusions, open decisions, changed files, validation, and `confirmed` request in one response.
- Current files: `AGENTS.md`, `DISCOVERY_GATE.md`, `USER_CONFIRMATION.md`, `TASKS.md`, `STATE.md`, `validate_harness.py`.

harness_rules_applied:
- Keep harness iteration inside active `TASK-002`.
- Only edit allowed harness files.
- Add a rule where observed execution was unclear.

reasoning_summary:
The issue is not the presence of gates, but the lack of a strict output contract per gate. A gate response needs to say where the user is, what status the gate has, and exactly one action the user should take. Open decisions cannot be presented as non-blocking while also asking for confirmation.

actions_taken:
- Added `layers/01_planning/GATE_OUTPUT_PROTOCOL.md`.
- Updated `AGENTS.md` to require the protocol and one user action per gate response.
- Updated `DISCOVERY_GATE.md` and `USER_CONFIRMATION.md` to prevent confirmation prompts while blocking questions remain.
- Updated `TASKS.md`, `STATE.md`, and `scripts/validate_harness.py` so the protocol is part of TASK-002 and structural validation.

verification_evidence:
- Pending final `python3 scripts/validate_harness.py`.

usability_notes:
- This should make Cursor/agent replies easier to parse: the first lines must show gate, status, and the one requested user action.

next_step:
- Run harness validation.
- Review whether examples/prompts should be updated in a later task.

## 2026-05-14 TASK-002 Decision Placement Follow-up

context_read:
- User feedback: even with a single gate, putting `User action needed` at the top made the interaction hard to follow.
- Current files: `GATE_OUTPUT_PROTOCOL.md`, `AGENTS.md`, `USER_CONFIRMATION.md`, `validate_harness.py`.

harness_rules_applied:
- Keep the change in active `TASK-002`.
- Improve the user confirmation protocol from real execution feedback.

reasoning_summary:
The user should understand the gate status, confirmed context, blocking item, file changes, and verification before being asked to decide. The requested action should be the final block, so the interaction reads as context first, decision last.

actions_taken:
- Changed `GATE_OUTPUT_PROTOCOL.md` so `Decision needed` is the final block.
- Updated `AGENTS.md` to require final-block decision placement.
- Updated `USER_CONFIRMATION.md` with a decision placement rule.
- Updated `validate_harness.py` to keep the new rule structurally required.

verification_evidence:
- Pending final `python3 scripts/validate_harness.py`.

usability_notes:
- This should reduce cognitive load: users can read the status report and then answer the final decision prompt.

next_step:
- Run harness validation and whitespace check.

## 2026-05-15 TASK-002 Chinese Gate Reply Follow-up

context_read:
- User feedback: the gate response was not readable for normal users because it exposed English labels and mixed internal terms with the user decision.
- Superpowers process guidance: use explicit process discipline, keep one user action per checkpoint, and verify behavior before completion.
- Current files: `AGENTS.md`, `GATE_OUTPUT_PROTOCOL.md`, `USER_CONFIRMATION.md`, `codex_prompts.md`, `validate_harness.py`.

harness_rules_applied:
- Keep the change in active `TASK-002`.
- Use TDD-style red/green: first make validator require the Chinese gate fields, then update the protocol and examples.
- Keep the requested user action as the final block.

reasoning_summary:
The previous protocol was structurally strict but user-hostile. It looked like an internal state dump. The fix is to keep internal status values available for agents, but require user-facing gate replies to use Chinese labels, short explanations, and a final `需要你决定` block with exactly one action.

actions_taken:
- Updated `scripts/validate_harness.py` to require Chinese gate-output terms.
- Updated `layers/01_planning/GATE_OUTPUT_PROTOCOL.md` with a Chinese user-facing template and anti-pattern example.
- Updated `layers/01_planning/USER_CONFIRMATION.md` and `AGENTS.md` to point to the final `需要你决定` block.
- Updated `layers/10_examples/codex_prompts.md` with a Chinese standard gate reply example.

verification_evidence:
- `python3 scripts/validate_harness.py` before docs update: failed with 10 missing Chinese protocol terms.
- `python3 scripts/validate_harness.py` after docs update: pass.

usability_notes:
- This should make gate replies read as a guided product checkpoint instead of a protocol dump.
- The user decision is now visually isolated at the end and starts with `请只做一件事`.

next_step:
- Run final validation and diff review.

## 2026-05-14 TASK-002 Standard Gate Reply Example

context_read:
- User request: add a standard reply example.
- Current files: `layers/10_examples/codex_prompts.md`, `GATE_OUTPUT_PROTOCOL.md`, `TASKS.md`, `STATE.md`, `validate_harness.py`.

harness_rules_applied:
- Keep the change in active `TASK-002`.
- Add `layers/10_examples/codex_prompts.md` to allowed files before editing it.
- Validate the harness after updating required example content.

reasoning_summary:
The protocol needs a concrete example for Cursor/Codex runs. The example should show a Product Brief decision with current stage, review document, decision target, exact item, evidence, and a final `Decision needed` block.

actions_taken:
- Added `layers/10_examples/codex_prompts.md` to TASK-002 allowed files and active state.
- Updated the Execute Task prompt read order to include discovery, planning, gate protocol, and verification policy files.
- Added `Standard Gate Reply Example`.
- Updated `scripts/validate_harness.py` to require the example.

verification_evidence:
- Pending final `python3 scripts/validate_harness.py`.

usability_notes:
- This should give Cursor a copyable output shape instead of relying only on abstract protocol rules.

next_step:
- Run harness validation and whitespace check.

## 2026-05-14 TASK-002 Document Target Follow-up

context_read:
- User feedback: there are many harness files; each confirmation must clearly say which document to review, current stage, and what exactly is being confirmed.
- Current files: `GATE_OUTPUT_PROTOCOL.md`, `AGENTS.md`, `USER_CONFIRMATION.md`, `validate_harness.py`.

harness_rules_applied:
- Keep the change in active `TASK-002`.
- Convert real user confusion into a reusable gate-output requirement.

reasoning_summary:
The gate protocol needs document navigation fields, not just status fields. Users should not infer where to look or what will change after they answer.

actions_taken:
- Added `Stage`, `Review document`, `Decision record target`, and `What is being confirmed` to `GATE_OUTPUT_PROTOCOL.md`.
- Updated `AGENTS.md` to require document-target clarity in every gate response.
- Updated `USER_CONFIRMATION.md` with a document target rule.
- Updated `validate_harness.py` so those phrases are required.

verification_evidence:
- Pending final `python3 scripts/validate_harness.py`.

usability_notes:
- This should make each confirmation feel like a guided review rather than a free-form conversation.

next_step:
- Run harness validation and whitespace check.
