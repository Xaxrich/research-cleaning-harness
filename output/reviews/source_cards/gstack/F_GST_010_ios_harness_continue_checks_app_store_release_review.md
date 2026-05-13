# Source Card Review: F_GST_010 - App Store 发布检查模板

## 1. Review Metadata

| Field | Value |
|---|---|
| source_id | F_GST_010 |
| source_card | output/source_cards/gstack/F_GST_010_ios_harness_continue_checks_app_store_release.md |
| raw_path | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/.continue/checks/app-store-release.md |
| reviewed_at | 2026-05-13 |
| reviewer | Codex |
| decision | approved |

## 2. Schema Check

| check | result | notes |
|---|---|---|
| 13 required sections | pass | Source Card follows the cleaning schema. |
| metadata | pass | Card references exactly one gstack raw file. |
| iOS mapping | pass | Mappings use valid target layers and version labels. |

## 3. Fidelity Check

| claim_or_mechanism | evidence_status | notes |
|---|---|---|
| gstack topic extraction | supported | Based on file heading, file type, inventory topic and raw path. |
| mechanism extraction | supported with caution | Mechanisms are normalized from the current file category and structure. |
| iOS mapping | inferred | Mapping is a transfer decision and must be rechecked during framework synthesis. |

## 4. Quality Gate Check

| gate | pass_fail | notes |
|---|---|---|
| exactly one raw file | pass | No other gstack raw file is summarized as evidence. |
| no large raw copy | pass | Evidence is summarized. |
| uncertainties included | pass | Card marks adaptation and duplication risks. |

## 5. Over-inference And Conflict Check

| issue | source_card_location | review_judgment | required_synthesis_handling |
|---|---|---|---|
| Some mechanisms are normalized from file category and headings | Sections 4, 8, 11 | acceptable | During `gstack_summary.md`, prefer specific role/workflow/template cards for final mechanism wording. |

## 6. Required Fixes

| fix | severity |
|---|---|
| none | none |

## 7. Final Decision

Approved. This card is acceptable for gstack framework synthesis, with medium confidence where the raw file is a template/package or design proposal rather than runtime evidence.
