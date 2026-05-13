# Lightweight iOS App Harness

This is the v0.1 harness distilled from the reviewed Research Cleaning Harness assets.

It intentionally starts as a docs-first, evidence-backed operating layer for Codex and other coding agents working on an iOS app. Runtime enforcement is version-gated: v0.1 is rules and task discipline, v0.5 adds scripts, v1.0 adds stronger interception/replay.

## Data Basis

| metric | count |
| --- | --- |
| reviewed Source Cards | 134 |
| mechanism target rows | 629 |
| frameworks | superpowers, gsd2, aider, gstack, swe-agent |
| v0_1 mechanisms | 353 |
| v0_5 mechanisms | 262 |
| v1_0 mechanisms | 14 |

## Fusion Rule

| framework | primary contribution |
| --- | --- |
| superpowers | 工程纪律：planning、TDD、debugging、review、verification-before-completion。 |
| gsd2 | 状态与恢复：task state machine、context isolation、failure recovery、model routing。 |
| aider | 仓库上下文：repo map、explicit file scope、read-only context、Git/verification loop。 |
| gstack | 角色治理：role matrix、review matrix、workflow、risk/blocking rights。 |
| swe-agent | 执行接口：ACI tools、action/observation、safe command、trajectory/replay。 |

## Operating Loop

1. Select or create one task in `TASKS.md`.
2. Load only the context listed in `CONTEXT_INDEX.md` and `CONTEXT_RULES.md`.
3. Lock editable, read-only and forbidden files using `FILE_SCOPE_RULES.md`.
4. Pick the role and review gate from `ROLE_MATRIX.md` and `REVIEW_MATRIX.md`.
5. Use ACI-style tools from `docs/agent/ACI_TOOL_CONTRACTS.md` and `scripts/agent/`.
6. Run the task-specific checks from `VERIFICATION_MATRIX.md`.
7. Update `STATE.md`, `FAILURE_LOG.md`, and Git evidence before claiming completion.

## Layer Coverage

| layer | mechanism targets |
| --- | --- |
| Action / ACI Layer | 57 |
| Context Layer | 78 |
| Feedback / Verification Layer | 100 |
| Goal Layer | 25 |
| Harness Maintenance Layer | 80 |
| Memory / State Layer | 62 |
| Risk / Release Layer | 102 |
| Role / Review Layer | 64 |
| Task Layer | 61 |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-066 | aider | F_AID_017 | v0_1 | Versioned iOS Harness File Tree |
| M-AID-068 | aider | F_AID_017 | v0_1 | Migration Handoff Package |
| M-AID-074 | aider | F_AID_019 | v0_1 | Versioned iOS Harness File Tree |
| M-AID-076 | aider | F_AID_019 | v0_1 | Migration Handoff Package |
| M-AID-138 | aider | F_AID_035 | v0_1 | Versioned iOS Harness File Tree |
| M-AID-140 | aider | F_AID_035 | v0_1 | Migration Handoff Package |
| M-AID-142 | aider | F_AID_036 | v0_1 | Versioned iOS Harness File Tree |
| M-AID-144 | aider | F_AID_036 | v0_1 | Migration Handoff Package |
| M-AID-146 | aider | F_AID_037 | v0_1 | Versioned iOS Harness File Tree |
| M-AID-148 | aider | F_AID_037 | v0_1 | Migration Handoff Package |
| M-GSD-033 | gsd2 | F_GSD_005 | v0_1 | Deliverable Catalog |
| M-GSD-036 | gsd2 | F_GSD_005 | v0_1 | Handoff-Oriented Packaging |
| M-SWE-003 | swe-agent | F_SWE_001 | v0_1 | Versioned Scope Split |
| M-SWE-012 | swe-agent | F_SWE_003 | v0_1 | Conflict-Driven Synthesis |
| M-SWE-031 | swe-agent | F_SWE_008 | v0_1 | Versioned Scope Split |
| M-SWE-039 | swe-agent | F_SWE_010 | v0_1 | Versioned Scope Split |
| M-SWE-108 | swe-agent | F_SWE_027 | v0_1 | Conflict-Driven Synthesis |
| M-AID-072 | aider | F_AID_018 | v0_5 | Knowledge Handoff Summary |

## Source Trace

Every reviewed source card is represented in `data/source_to_harness_trace.jsonl`. Human-readable coverage is in `../output/ios_harness_mapping/source_to_harness_trace.md` from the cleaning project.
