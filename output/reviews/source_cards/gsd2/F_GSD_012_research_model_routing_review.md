# Source Card Review: F_GSD_012 - research_model_routing

## 1. Review Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_012 |
| source_card | output/source_cards/gsd2/F_GSD_012_research_model_routing.md |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/research_model_routing.md |
| reviewed_at | 2026-05-13 |
| reviewer | Codex |
| decision | approved |

## 2. Schema Check

| check | result | notes |
|---|---|---|
| 13 required sections | pass | Complete structure. |
| metadata | pass | One raw Markdown path. |
| version split | pass | v0.1 is partial, v0.5/v1.0 are explicit. |

## 3. Fidelity Check

| claim_or_mechanism | evidence_status | notes |
|---|---|---|
| heuristic complexity classification | supported | Source describes zero-LLM heuristic classification. |
| capability scoring | supported | Source includes ADR-004, dimensions and scoring selection. |
| failure escalation with context policy | supported | Source covers escalation and keep/drop context. |

## 4. Quality Gate Check

| gate | pass_fail | notes |
|---|---|---|
| exactly one raw file | pass | Scoped to model routing research. |
| failure modes included | pass | Underfit, overkill, provider unavailable and repeated failure covered. |
| uncertainty included | pass | Model availability staleness is noted. |

## 5. Over-inference And Conflict Check

| issue | source_card_location | review_judgment | required_synthesis_handling |
|---|---|---|---|
| Concrete model names may be stale | Sections 11, 13 | acceptable | Synthesis should preserve routing structure, not freeze provider-specific names. |

## 6. Required Fixes

| fix | severity |
|---|---|
| none | none |

## 7. Final Decision

Approved. This card is the main GSD2 source for model routing and escalation policy.

