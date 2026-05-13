# Source Card Review: F_SWE_016 - 4. ACI 深挖

## 1. Review Metadata

| Field | Value |
|---|---|
| source_id | F_SWE_016 |
| source_card | output/source_cards/swe-agent/F_SWE_016_swe_agent_ios_harness_sec04.md |
| raw_path | raw/Kimi_Agent_SWE-agent 迁移研究/swe_agent_ios_harness_sec04.md |
| reviewed_at | 2026-05-13 |
| reviewer | Codex |
| decision | approved |

## 2. Schema Check

| check | result | notes |
|---|---|---|
| 13 required sections | pass | Source Card follows the cleaning schema. |
| metadata | pass | Card references exactly one SWE-agent raw file. |
| iOS mapping | pass | Mappings use valid target layers and version labels. |

## 3. Fidelity Check

| claim_or_mechanism | evidence_status | notes |
|---|---|---|
| SWE-agent topic extraction | supported | Based on file heading, file type, inventory topic and raw path. |
| mechanism extraction | supported with caution | Mechanisms are normalized from the current file category and structure. |
| iOS mapping | inferred | Mapping is a transfer decision and must be rechecked during framework synthesis. |

## 4. Quality Gate Check

| gate | pass_fail | notes |
|---|---|---|
| exactly one raw file | pass | No other SWE-agent raw file is summarized as evidence. |
| no large raw copy | pass | Evidence is summarized. |
| uncertainties included | pass | Card marks adaptation, duplicate-report and runtime risks. |

## 5. Over-inference And Conflict Check

| issue | source_card_location | review_judgment | required_synthesis_handling |
|---|---|---|---|
| Some mechanisms are normalized from file category and headings | Sections 4, 8, 11 | acceptable | During `swe_agent_summary.md`, prefer specific ACI/tool/trajectory section cards for final wording. |

## 6. Required Fixes

| fix | severity |
|---|---|
| none | none |

## 7. Final Decision

Approved. This card is acceptable for SWE-agent framework synthesis, with medium confidence where the raw file is a report, converted document or proposal rather than tested runtime evidence.
