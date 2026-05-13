# Superpowers Conflict Ledger

Scope: reviewed Superpowers Source Cards `F_SUP_001` through `F_SUP_014`.

This file records cross-card tensions that must be resolved before Superpowers mechanisms are merged with other frameworks or transferred into the iOS App Harness.

## Conflict Summary

| conflict_id | conflict | source_cards | synthesis_resolution | iOS Harness implication |
|---|---|---|---|---|
| C-SUP-001 | Strict TDD iron law vs weak-model Flutter/iOS cost | F_SUP_003, F_SUP_005, F_SUP_012 | Keep test-first culture; downgrade delete-and-restart rule to risk-based guidance. | v0.1 keeps verification culture only; v0.5 adds mobile testing guide and scripts. |
| C-SUP-002 | Subagent/reviewer isolation vs weak-model orchestration failure | F_SUP_002, F_SUP_003, F_SUP_005, F_SUP_007 | Preserve role separation as templates/review gates; do not default to subagent execution. | v0.1 uses inline execution plus human/static review for high risk. |
| C-SUP-003 | Worktree isolation vs Xcode/Flutter path fragility | F_SUP_001, F_SUP_003, F_SUP_005 | Treat worktree as non-default for iOS; use branch or in-place execution unless manually chosen. | Add worktree to `DO_NOT_TRANSFER.md` defaults and risk gate notes. |
| C-SUP-004 | 1% automatic skill trigger vs weak-model over-trigger/skip behavior | F_SUP_002, F_SUP_003, F_SUP_005, F_SUP_007 | Replace probabilistic trigger rule with explicit checkpoints: start, implementation, debugging, completion. | `AGENTS.md` should stay short and route details to task/risk docs. |
| C-SUP-005 | Model self-verification vs external tool enforcement | F_SUP_001, F_SUP_003, F_SUP_004, F_SUP_005, F_SUP_011, F_SUP_012, F_SUP_013 | Verification claims require command evidence; mature versions add scripts/CI. | v0.1 requires evidence fields; v0.5 adds scripts; v1.0 adds CI enforcement. |
| C-SUP-006 | Broad cross-platform adapter design vs single iOS Harness focus | F_SUP_002, F_SUP_005, F_SUP_010 | Keep only current platform/runtime adapters until a real second runtime exists. | Avoid platform abstraction in v0.1; defer adapters to v1.0 if justified. |
| C-SUP-007 | Learning-path artifacts vs authoritative mechanism evidence | F_SUP_006, F_SUP_011, F_SUP_012, F_SUP_013 | Use learning file for onboarding patterns, not as primary runtime mechanism evidence. | Do not let exercises override concrete skill cards or migration risk cards. |
| C-SUP-008 | Architecture diagram as visual map vs Codex-readable execution source | F_SUP_003, F_SUP_014 | Use diagram as human-facing map only; text Source Cards remain authoritative. | Include visual appendix only in handoff, not normal execution context. |

## Precedence Rules

1. Risk-critical constraints from `F_SUP_005` constrain positive transfer claims from `F_SUP_002`, `F_SUP_003`, and skill cards.
2. iOS-specific migration design from `F_SUP_004` is the primary source for target file placement, unless contradicted by `F_SUP_005`.
3. Concrete skill files `F_SUP_011`, `F_SUP_012`, and `F_SUP_013` define domain details, but their strictness is downgraded when weak-model risks are explicit.
4. `F_SUP_006` is onboarding evidence, not implementation authority.
5. `F_SUP_014` is a visual index, not a runtime dependency.

## Required Follow-up During Synthesis

| output | required handling |
|---|---|
| `output/frameworks/superpowers_summary.md` | Include a conflicts section and cite this ledger. |
| `output/mechanisms/*.md` | Mark downgraded mechanisms as `partial` or `v0_5`, not unconditional v0.1 defaults. |
| `output/failure_modes/*.md` | Include fake verification, weak-model overreach, subagent orchestration failure, worktree iOS path breakage, and pseudo RED. |
| `output/ios_harness_mapping/*.md` | Separate retained principles from rejected defaults. |
