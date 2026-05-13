# TASKS

All tasks must be small enough that one task handles one source file or one synthesis action.

## TASK-001: Build superpowers source inventory

status: completed
goal: Scan processable files under the superpowers raw folder and generate source inventory.

allowed_read:
  - raw/Kimi_Agent_Superpowers 体系探究/

allowed_write:
  - SOURCE_INVENTORY.md
  - output/data/source_index.yaml

forbidden:
  - modifying raw/
  - generating framework summaries
  - generating mechanism index

acceptance:
  - every processable file has a unique source_id
  - every processable file has framework, path, type, estimated_topic
  - AppleDouble `._*` metadata files are ignored

result:
  - 14 source records generated

## TASK-002: Process source file F_SUP_001

status: completed
source_id: F_SUP_001
framework: superpowers
raw_path: raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md

goal:
Read exactly this file and generate one standardized Source Card.

allowed_read:
  - raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md
  - EXTRACTION_SCHEMA.md
  - QUALITY_GATE.md
  - templates/source_card_template.md

allowed_write:
  - output/source_cards/superpowers/F_SUP_001_00_final_report.md
  - output/data/source_cards.jsonl

forbidden:
  - reading other framework folders
  - writing mechanism summaries
  - changing raw/

acceptance:
  - Source Card follows schema
  - important conclusions have evidence
  - iOS Harness mapping is included

## TASK-003: Review source card F_SUP_001

status: completed
source_id: F_SUP_001
framework: superpowers
source_card: output/source_cards/superpowers/F_SUP_001_00_final_report.md

goal:
Check whether F_SUP_001 Source Card is faithful to its single raw file and schema.

allowed_read:
  - output/source_cards/superpowers/F_SUP_001_00_final_report.md
  - raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md
  - QUALITY_GATE.md
  - templates/review_template.md

allowed_write:
  - output/reviews/source_cards/superpowers/F_SUP_001_00_final_report_review.md
  - STATE.md
  - TASKS.md
  - SOURCE_INVENTORY.md
  - output/data/source_index.yaml

forbidden:
  - adding new mechanisms not present in the card/raw file
  - reading other raw files

acceptance:
  - review decision is recorded
  - status is updated to reviewed

## TASK-004: Process source file F_SUP_002

status: completed
source_id: F_SUP_002
framework: superpowers
raw_path: raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md

goal:
Read exactly this file and generate one standardized Source Card.

allowed_read:
  - raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md
  - EXTRACTION_SCHEMA.md
  - QUALITY_GATE.md
  - templates/source_card_template.md

allowed_write:
  - output/source_cards/superpowers/F_SUP_002_01_superpowers_anatomy_report.md
  - output/data/source_cards.jsonl

forbidden:
  - reading other framework folders
  - writing framework summaries
  - changing raw/

acceptance:
  - Source Card follows schema
  - every mechanism has evidence
  - iOS Harness mapping is included
  - uncertainties are explicit

result:
  - Source Card and review generated for F_SUP_002

## Backlog

| task | source_id | raw_path | status |
|---|---|---|---|
| TASK-005 | F_SUP_003 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md | completed |
| TASK-006 | F_SUP_004 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md | completed |
| TASK-007 | F_SUP_005 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md | completed |
| TASK-008 | F_SUP_006 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md | completed |
| TASK-009 | F_SUP_007 | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md | completed |
| TASK-010 | F_SUP_008 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md | completed |
| TASK-011 | F_SUP_009 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md | completed |
| TASK-012 | F_SUP_010 | raw/Kimi_Agent_Superpowers 体系探究/plan.md | completed |
| TASK-013 | F_SUP_011 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md | completed |
| TASK-014 | F_SUP_012 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md | completed |
| TASK-015 | F_SUP_013 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md | completed |
| TASK-016 | F_SUP_014 | raw/Kimi_Agent_Superpowers 体系探究/superpowers_architecture.png | completed |
| TASK-017 | superpowers | all reviewed superpowers Source Cards | ready |

## Cleaning Results

| range | result |
|---|---|
| F_SUP_001-F_SUP_014 | Source Card generated and reviewed |
| superpowers inventory | all processable files marked reviewed |
| next synthesis input | reviewed Source Cards only |

## TASK-018: Harden superpowers clean data package

status: completed
framework: superpowers

goal:
Add machine-readable mechanism data, explicit conflict records, and stronger validators before framework synthesis.

allowed_read:
  - output/source_cards/superpowers/
  - output/reviews/source_cards/superpowers/
  - output/data/source_cards.jsonl
  - output/data/source_index.yaml

allowed_write:
  - output/data/mechanisms.jsonl
  - output/conflicts/superpowers_conflicts.md
  - scripts/build_mechanisms_jsonl.py
  - scripts/validate_clean_data.py
  - scripts/validate_source_cards.py
  - tests/
  - QUALITY_GATE.md
  - EXTRACTION_SCHEMA.md
  - DECISIONS.md
  - STATE.md

forbidden:
  - modifying raw/
  - generating cross-framework mechanism summaries

acceptance:
  - every mechanism listed by Source Cards has a JSONL record
  - clean-data validator checks Source Card, review, index, mechanism, and conflict files
  - Superpowers conflicts are explicit before synthesis

result:
  - 97 mechanism records generated
  - Superpowers conflict ledger added
  - validators strengthened with tests

## TASK-019: Build GSD2 source inventory

status: completed
framework: gsd2
raw_root: raw/Kimi_Agent_多 Agent GSD2

goal:
Scan processable files under the GSD2 raw folder and add them to the source inventory.

allowed_read:
  - raw/Kimi_Agent_多 Agent GSD2/

allowed_write:
  - SOURCE_INVENTORY.md
  - output/data/source_index.yaml
  - STATE.md
  - TASKS.md

forbidden:
  - modifying raw/
  - generating GSD2 Source Cards during inventory
  - generating framework summaries

acceptance:
  - every processable GSD2 file has a unique F_GSD source_id
  - every GSD2 file has framework, path, type, estimated_topic
  - every GSD2 file starts with processing_status = queued

result:
  - 12 GSD2 source records added

## TASK-020: Process source file F_GSD_001

status: completed
source_id: F_GSD_001
framework: gsd2
raw_path: raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md

goal:
Read exactly this file and generate one standardized Source Card.

allowed_read:
  - raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md
  - EXTRACTION_SCHEMA.md
  - QUALITY_GATE.md
  - templates/source_card_template.md

allowed_write:
  - output/source_cards/gsd2/F_GSD_001_GSD2_深度研究_iOS_Harness_迁移报告.md
  - output/data/source_cards.jsonl

forbidden:
  - reading other GSD2 raw files
  - reading other framework raw folders
  - writing framework summaries
  - changing raw/

acceptance:
  - Source Card follows schema
  - every mechanism has evidence
  - iOS Harness mapping is included
  - uncertainties are explicit
  - no cross-file synthesis is introduced

result:
  - Source Card and review generated for F_GSD_001
  - 10 GSD2 mechanisms extracted

## TASK-021: Review source card F_GSD_001

status: completed
source_id: F_GSD_001
framework: gsd2
source_card: output/source_cards/gsd2/F_GSD_001_GSD2_深度研究_iOS_Harness_迁移报告.md

goal:
Check whether F_GSD_001 Source Card is faithful to its single raw file and schema.

allowed_read:
  - output/source_cards/gsd2/F_GSD_001_GSD2_深度研究_iOS_Harness_迁移报告.md
  - raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md
  - QUALITY_GATE.md
  - templates/review_template.md

allowed_write:
  - output/reviews/source_cards/gsd2/F_GSD_001_GSD2_深度研究_iOS_Harness_迁移报告_review.md
  - STATE.md
  - TASKS.md
  - SOURCE_INVENTORY.md
  - output/data/source_index.yaml

forbidden:
  - adding new mechanisms not present in the card/raw file
  - reading other GSD2 raw files

acceptance:
  - review decision is recorded
  - status is updated to reviewed

result:
  - Review approved with over-inference and conflict notes

## TASK-022: Process source file F_GSD_002

status: completed
source_id: F_GSD_002
framework: gsd2
raw_path: raw/Kimi_Agent_多 Agent GSD2/GSD2深度研究_iOS_Harness迁移方案.docx

goal:
Read exactly this file and generate one standardized Source Card.

allowed_read:
  - raw/Kimi_Agent_多 Agent GSD2/GSD2深度研究_iOS_Harness迁移方案.docx
  - EXTRACTION_SCHEMA.md
  - QUALITY_GATE.md
  - templates/source_card_template.md

allowed_write:
  - output/source_cards/gsd2/F_GSD_002_GSD2深度研究_iOS_Harness迁移方案.md
  - output/data/source_cards.jsonl

forbidden:
  - reading other GSD2 raw files
  - reading other framework raw folders
  - writing framework summaries
  - changing raw/

acceptance:
  - Source Card follows schema
  - every mechanism has evidence
  - iOS Harness mapping is included
  - uncertainties are explicit
  - document extraction method is recorded

result:
  - Source Card generated and reviewed
  - Status updated to reviewed

## TASK-023: Build Aider, Gstack, and SWE-agent source inventories

status: completed
frameworks:
  - aider
  - gstack
  - swe-agent

goal:
Scan processable files under the remaining framework raw folders and add them to the source inventory as queued records.

allowed_read:
  - raw/Kimi_Agent_Aider 代码库方案/
  - raw/Kimi_Agent_gstack 多 Agent 迁移/
  - raw/Kimi_Agent_SWE-agent 迁移研究/

allowed_write:
  - SOURCE_INVENTORY.md
  - output/data/source_index.yaml
  - output/source_cards/aider/
  - output/source_cards/gstack/
  - output/source_cards/swe-agent/
  - output/reviews/source_cards/aider/
  - output/reviews/source_cards/gstack/
  - output/reviews/source_cards/swe-agent/
  - scripts/sync_all_framework_inventories.py
  - STATE.md
  - TASKS.md

forbidden:
  - modifying raw/
  - generating Source Cards for these frameworks during inventory
  - writing framework summaries

acceptance:
  - Aider files have F_AID source IDs and queued status
  - Gstack files have F_GST source IDs and queued status
  - SWE-agent files have F_SWE source IDs and queued status
  - Existing reviewed Superpowers and F_GSD_001 statuses are preserved

result:
  - Aider: 39 queued records
  - Gstack: 40 queued records
  - SWE-agent: 29 queued records
  - Total indexed framework records: 134

## TASK-024: Complete remaining GSD2 Source Cards and reviews

status: completed
framework: gsd2

goal:
Process and review every remaining GSD2 source file after F_GSD_002 so the framework is ready for synthesis.

allowed_read:
  - raw/Kimi_Agent_多 Agent GSD2/report_stages_10_11.md
  - raw/Kimi_Agent_多 Agent GSD2/report_stages_12_13_14.md
  - raw/Kimi_Agent_多 Agent GSD2/report_stages_1_2_3.md
  - raw/Kimi_Agent_多 Agent GSD2/report_stages_4_5_6.md
  - raw/Kimi_Agent_多 Agent GSD2/report_stages_7_8_9.md
  - raw/Kimi_Agent_多 Agent GSD2/research_architecture.md
  - raw/Kimi_Agent_多 Agent GSD2/research_context.md
  - raw/Kimi_Agent_多 Agent GSD2/research_failure_recovery.md
  - raw/Kimi_Agent_多 Agent GSD2/research_model_routing.md

allowed_write:
  - output/source_cards/gsd2/
  - output/reviews/source_cards/gsd2/
  - output/conflicts/gsd2_conflicts.md
  - output/data/source_cards.jsonl
  - output/data/source_index.yaml
  - output/data/mechanisms.jsonl
  - SOURCE_INVENTORY.md
  - STATE.md
  - TASKS.md

forbidden:
  - modifying raw/
  - generating Aider, Gstack, or SWE-agent Source Cards in this task
  - writing cross-framework synthesis before validation

acceptance:
  - F_GSD_003 through F_GSD_012 each have one Source Card
  - F_GSD_003 through F_GSD_012 each have one review file
  - all GSD2 records are reviewed in SOURCE_INVENTORY.md and source_index.yaml
  - mechanisms.jsonl includes GSD2 mechanisms from all reviewed cards
  - conflict ledger records GSD2 version/scope tensions

result:
  - GSD2 reviewed Source Cards: 12/12
  - GSD2 review files: 12/12
  - GSD2 conflict ledger created
  - Aider, Gstack, and SWE-agent remain queued only

processed_files:
  - F_GSD_003 -> output/source_cards/gsd2/F_GSD_003_plan.md
  - F_GSD_004 -> output/source_cards/gsd2/F_GSD_004_report_stages_10_11.md
  - F_GSD_005 -> output/source_cards/gsd2/F_GSD_005_report_stages_12_13_14.md
  - F_GSD_006 -> output/source_cards/gsd2/F_GSD_006_report_stages_1_2_3.md
  - F_GSD_007 -> output/source_cards/gsd2/F_GSD_007_report_stages_4_5_6.md
  - F_GSD_008 -> output/source_cards/gsd2/F_GSD_008_report_stages_7_8_9.md
  - F_GSD_009 -> output/source_cards/gsd2/F_GSD_009_research_architecture.md
  - F_GSD_010 -> output/source_cards/gsd2/F_GSD_010_research_context.md
  - F_GSD_011 -> output/source_cards/gsd2/F_GSD_011_research_failure_recovery.md
  - F_GSD_012 -> output/source_cards/gsd2/F_GSD_012_research_model_routing.md

## TASK-025: Complete Aider Source Cards and reviews

status: completed
framework: aider

goal:
Process and review every indexed Aider source file so the framework is ready for synthesis.

allowed_read:
  - raw/Kimi_Agent_Aider 代码库方案/
  - SOURCE_INVENTORY.md
  - output/data/source_index.yaml
  - EXTRACTION_SCHEMA.md
  - QUALITY_GATE.md
  - templates/source_card_template.md
  - templates/review_template.md

allowed_write:
  - output/source_cards/aider/
  - output/reviews/source_cards/aider/
  - output/conflicts/aider_conflicts.md
  - output/data/source_cards.jsonl
  - output/data/source_index.yaml
  - output/data/mechanisms.jsonl
  - SOURCE_INVENTORY.md
  - STATE.md
  - TASKS.md
  - scripts/generate_aider_source_cards.py
  - scripts/validate_clean_data.py

forbidden:
  - modifying raw/
  - generating Gstack or SWE-agent Source Cards in this task
  - writing cross-framework synthesis before validation

acceptance:
  - F_AID_001 through F_AID_039 each have one Source Card
  - F_AID_001 through F_AID_039 each have one review file
  - all Aider records are reviewed in SOURCE_INVENTORY.md and source_index.yaml
  - mechanisms.jsonl includes Aider mechanisms from all reviewed cards
  - conflict ledger records Aider scope, repo map, Git, weak model, and validation tensions

result:
  - Aider reviewed Source Cards: 39/39
  - Aider review files: 39/39
  - Aider mechanism references: 156
  - Aider conflict ledger created
  - Gstack and SWE-agent remain queued only

processed_files:
  - F_AID_001-F_AID_039 -> output/source_cards/aider/

## TASK-026: Complete gstack Source Cards and reviews

status: completed
framework: gstack

goal:
Process and review every indexed gstack source file so the framework is ready for synthesis.

allowed_read:
  - raw/Kimi_Agent_gstack 多 Agent 迁移/
  - SOURCE_INVENTORY.md
  - output/data/source_index.yaml
  - EXTRACTION_SCHEMA.md
  - QUALITY_GATE.md
  - templates/source_card_template.md
  - templates/review_template.md

allowed_write:
  - output/source_cards/gstack/
  - output/reviews/source_cards/gstack/
  - output/conflicts/gstack_conflicts.md
  - output/data/source_cards.jsonl
  - output/data/source_index.yaml
  - output/data/mechanisms.jsonl
  - SOURCE_INVENTORY.md
  - STATE.md
  - TASKS.md
  - scripts/generate_gstack_source_cards.py
  - scripts/validate_clean_data.py
  - scripts/validate_source_cards.py
  - README.md
  - PROGRESS.md
  - VALIDATION_LOG.md
  - GITHUB_PUBLISHING.md

forbidden:
  - modifying raw/
  - generating SWE-agent Source Cards in this task
  - writing cross-framework synthesis before validation

acceptance:
  - F_GST_001 through F_GST_040 each have one Source Card
  - F_GST_001 through F_GST_040 each have one review file
  - all gstack records are reviewed in SOURCE_INVENTORY.md and source_index.yaml
  - mechanisms.jsonl includes gstack mechanisms from all reviewed cards
  - conflict ledger records gstack role, workflow, review, guardrail and weak-model tensions

result:
  - gstack reviewed Source Cards: 40/40
  - gstack review files: 40/40
  - gstack mechanism references: 160
  - gstack conflict ledger created
  - SWE-agent remains queued only

processed_files:
  - F_GST_001-F_GST_040 -> output/source_cards/gstack/

## TASK-027: Complete SWE-agent Source Cards and reviews

status: completed
framework: swe-agent

goal:
Process and review every indexed SWE-agent source file so all five framework folders have reviewed Source Cards.

allowed_read:
  - raw/Kimi_Agent_SWE-agent 迁移研究/
  - SOURCE_INVENTORY.md
  - output/data/source_index.yaml
  - EXTRACTION_SCHEMA.md
  - QUALITY_GATE.md
  - templates/source_card_template.md
  - templates/review_template.md

allowed_write:
  - output/source_cards/swe-agent/
  - output/reviews/source_cards/swe-agent/
  - output/conflicts/swe_agent_conflicts.md
  - output/data/source_cards.jsonl
  - output/data/source_index.yaml
  - output/data/mechanisms.jsonl
  - SOURCE_INVENTORY.md
  - STATE.md
  - TASKS.md
  - scripts/generate_swe_agent_source_cards.py
  - scripts/validate_clean_data.py
  - README.md
  - PROGRESS.md
  - VALIDATION_LOG.md

forbidden:
  - modifying raw/
  - writing cross-framework synthesis before validation
  - claiming runtime ACI implementation from research-only cards

acceptance:
  - F_SWE_001 through F_SWE_029 each have one Source Card
  - F_SWE_001 through F_SWE_029 each have one review file
  - all SWE-agent records are reviewed in SOURCE_INVENTORY.md and source_index.yaml
  - mechanisms.jsonl includes SWE-agent mechanisms from all reviewed cards
  - conflict ledger records ACI, trajectory, safe edit, safe command, weak-model, security and duplicate-report tensions

result:
  - SWE-agent reviewed Source Cards: 29/29
  - SWE-agent review files: 29/29
  - SWE-agent mechanism references: 116
  - SWE-agent conflict ledger created
  - all indexed framework source files now have reviewed Source Cards

processed_files:
  - F_SWE_001-F_SWE_029 -> output/source_cards/swe-agent/
