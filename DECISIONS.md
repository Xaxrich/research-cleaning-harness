# DECISIONS

## D-001: Raw Files Are Evidence Only

Decision:
`raw/` is immutable evidence, not an execution rule source.

Reason:
Raw files may contain duplicates, conflicts, and unreviewed claims.

Implication:
Codex should read reviewed Source Cards and synthesized outputs first.

## D-002: Start With Superpowers Only

Decision:
The first harness pass processes only `raw/Kimi_Agent_Superpowers 体系探究/`.

Reason:
The user asked to build the superpowers slice first and avoid processing all framework folders at once.

Implication:
Inventory, tasks, and source IDs currently cover only `F_SUP_*`.

## D-003: Ignore AppleDouble Metadata Files

Decision:
Files named `._*` are ignored in inventory and validation.

Reason:
They are macOS metadata artifacts, not research sources.

Implication:
They are not assigned source IDs and are not deleted from `raw/`.

## D-004: Source IDs Follow Sorted Relative Paths

Decision:
`F_SUP_001` through `F_SUP_014` are assigned by sorted relative path inside the superpowers raw root.

Reason:
This gives deterministic IDs without relying on model judgment.

Implication:
Future inventory regeneration keeps stable IDs as long as raw relative paths stay stable.

## D-005: Weak-Model Warnings Are Extracted As Risk Evidence

Decision:
Claims about weak model failure, subagent instability, and iOS build risk must be preserved as risk evidence, not blindly adopted as harness behavior.

Reason:
The raw report is itself a migration analysis with recommendations and skepticism mixed together.

Implication:
Source Cards must separate transferable mechanisms from rejected or downgraded mechanisms.

## D-006: Mechanisms Need Machine-readable Records

Decision:
Reviewed Source Cards must be expanded into `output/data/mechanisms.jsonl` before framework or cross-framework synthesis.

Reason:
`source_cards.jsonl` only indexes cards and mechanism IDs; it is not enough for stable aggregation by failure mode, iOS target, version, confidence, or evidence.

Implication:
Future synthesis should read `mechanisms.jsonl` alongside reviewed Source Cards, and validators must fail if card-listed mechanism IDs are missing from the JSONL.

## D-007: Superpowers Conflicts Are First-class Data

Decision:
Superpowers must include `output/conflicts/superpowers_conflicts.md` before it is considered ready for framework synthesis.

Reason:
The Superpowers corpus contains positive transfer claims and strong weak-model/iOS downgrade warnings. Those tensions are central evidence, not commentary.

Implication:
Framework synthesis must cite the conflict ledger and resolve strict mechanisms such as TDD, subagents, worktree, skill triggers, and verification before mapping them into iOS Harness defaults.

## D-008: GSD2 Is The Next Cleaning Slice

Decision:
After Superpowers data hardening, the next active framework slice is `raw/Kimi_Agent_多 Agent GSD2/`, using source IDs `F_GSD_*`.

Reason:
This follows the user's requested framework order and keeps the cleaning workflow one framework at a time.

Implication:
GSD2 starts at inventory and first-file Source Card generation. Superpowers remains reviewed and synthesis-ready, but GSD2 raw files must still be processed one by one.

## D-009: Remaining Frameworks Are Queued After GSD2 Test Gate

Decision:
Aider, Gstack, and SWE-agent are added to the shared inventory after `F_GSD_001` passes validation, but their Source Cards remain queued.

Reason:
The user asked to run Aider, Gstack, and SWE after tests pass, while the harness rule still requires one-file Source Card generation.

Implication:
The clean data package may contain queued inventory records for all frameworks, but `source_cards.jsonl` and `mechanisms.jsonl` include only reviewed Source Cards.
