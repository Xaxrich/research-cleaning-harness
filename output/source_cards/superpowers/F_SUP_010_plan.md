# Source Card: F_SUP_010 - Superpowers → iOS Harness 迁移项目计划

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_010 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/plan.md |
| file_type | markdown |
| topic | Superpowers → iOS Harness 迁移项目计划 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：规划 Superpowers 到 Flutter/Firebase iOS Harness 的研究、抽象、迁移设计、skill 编写、学习路径和综合交付阶段。

## 3. File Summary

- 文件目标是系统研究 Superpowers agentic skills framework，并迁移为轻量 iOS Harness。
- 核心约束包括弱模型兼容、强模型复杂设计、agent 集群分工、repo 文件沉淀、多工具复用。
- Stage 1 深度研究读取仓库结构和 SKILL.md，并安排 Research、Architecture、Skeptic 三类代理。
- Stage 2 做 5 Why 分析和底层原则抽象。
- Stage 3 将机制迁移到 Flutter + Firebase iOS 场景并设计目标结构。
- Stage 4 编写核心 SKILL.md、AGENTS、STATE、TASKS 模板。
- Stage 5 设计三天学习路径和自测问题。
- Stage 6 合并报告并生成最终交付文件。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-062 | Staged Research-to-Harness Pipeline | 将研究项目拆成深度研究、抽象、迁移设计、skill 编写、学习路径、综合交付六阶段。 | E2 | high |
| M-SUP-063 | Triangulated Research Roles | Stage 1 使用 Research、Architecture、Skeptic 三种视角读同一框架。 | E3 | medium |
| M-SUP-064 | Constraint-first Migration Scope | 在计划顶部明确弱模型、强模型、agent 分工、repo 沉淀、多工具复用等约束。 | E1 | high |
| M-SUP-065 | Deliverable-driven Research | 每个阶段都有明确产出物，如研究笔记、设计逻辑、迁移方案、skill 文件、学习路径、综合报告。 | E2 | high |
| M-SUP-066 | Skill Loading Strategy | 指定研究和报告阶段加载不同技能，不加载 docx。 | E4 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| unfocused_research | 六阶段计划明确每阶段目标和产出。 | E2 |
| one_sided_analysis | Research、Architecture、Skeptic 三角色降低只看优点的风险。 | E3 |
| non_reusable_output | 核心约束要求沉淀到 repo 文件结构并被多工具复用。 | E1 |
| premature_template_writing | Stage 4 在研究、抽象、迁移设计之后才写 skill/templates。 | E2 |
| deliverable_gap | 每个阶段显式列产出。 | E2 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 先研究后迁移 | 避免直接照搬框架 | 需要理解机制和不适配点 | 前期不产出可运行 harness |
| 加入 Skeptic Agent | 找不适合迁移和冲突 | 避免只做正向总结 | 可能增加决策成本 |
| Stage 4 才写 skill | 先确定目标结构和原则 | 避免模板和机制脱节 | 延后可用文件产出 |
| 明确不加载 docx | 用户要技术文档和代码/模板 | 避免偏离交付格式 | 不覆盖 Word 报告场景 |

## 7. 5 Why Analysis

### Mechanism: Staged Research-to-Harness Pipeline

- Why 1: 为什么要分阶段？因为从框架研究到 iOS Harness 不是单步总结。
- Why 2: 为什么 Stage 1 要读仓库和 SKILL.md？因为机制证据来自源结构和技能文件。
- Why 3: 为什么 Stage 2 要做 5 Why？因为迁移需要理解机制根因，而非复制表面形式。
- Why 4: 为什么 Stage 3 后才写 skill？因为目标场景和约束会改变 skill 形态。
- Why 5: 为什么这对当前清洗 Harness 有价值？因为当前 source-card 流程正是把“研究→结构化资产→合成”的阶段化思想落地。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 核心约束包括弱模型兼容、强模型复杂设计、agent 集群分工、repo 沉淀和多工具复用。 | raw/Kimi_Agent_Superpowers 体系探究/plan.md:6-11 | M-SUP-064 |
| E2 | 阶段设计从深度研究、分析抽象、迁移设计、skill 编写、学习路径到综合报告。 | raw/Kimi_Agent_Superpowers 体系探究/plan.md:13-49 | M-SUP-062, M-SUP-065 |
| E3 | Stage 1 子代理包括 Research、Architecture、Skeptic。 | raw/Kimi_Agent_Superpowers 体系探究/plan.md:20-24 | M-SUP-063 |
| E4 | 技能加载顺序指定 deep-research-swarm、report-writing，不加载 docx。 | raw/Kimi_Agent_Superpowers 体系探究/plan.md:51-55 | M-SUP-066 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Staged Research-to-Harness Pipeline | Harness Maintenance Layer | docs/agent/WORKFLOW_CHAIN.md | v0_5 | Document research-to-implementation phases |
| Triangulated Research Roles | Role / Review Layer | docs/agent/REVIEW_MATRIX.md | v0_5 | Preserve Research/Architecture/Skeptic review angles |
| Constraint-first Migration Scope | Goal Layer | AGENTS.md | v0_1 | Keep weak/strong/repo/tool constraints visible |
| Deliverable-driven Research | Task Layer | TASKS.md | v0_1 | Require each task to name deliverables |
| Skill Loading Strategy | Context Layer | CONTEXT_RULES.md | v0_5 | Load only task-relevant skills/docs |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | Useful as process planning source, not as final mechanism evidence. |
| v0_1 | yes | Constraint-first scope and deliverable-driven tasks are immediate. |
| v0_5 | yes | Workflow chain and review roles can support later synthesis/review. |
| v1_0 | no | This plan is not runtime logic. |
| no_transfer | yes | Do not preserve specific agent swarm/tool loading assumptions without target runtime support. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether original agent swarm actually ran as planned | File is a plan, not execution evidence. | Cross-check produced reports and templates. |
| Whether agent cluster support should transfer | Later skeptic/final reports warn against weak-model subagents. | Use F_SUP_005 to constrain transfer. |
| Whether report-writing/deep-research-swarm are available in target environment | They are named but not provided in this raw folder. | Treat as planning labels only. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_001 | final report produced by this plan |
| F_SUP_002 | anatomy report from Stage 1 |
| F_SUP_003 | design logic report from Stage 2 |
| F_SUP_004 | migration design from Stage 3 |
| F_SUP_005 | skeptic review from Stage 1/critique |
| F_SUP_006 | learning path from Stage 5 |

## 13. Clean Summary for Codex

这份 plan.md 的价值在于解释 superpowers raw 文件为什么会形成现在这组产物：先研究结构和 skills，再做 5 Why 抽象，再做 iOS 迁移设计，再写模板和学习路径。它适合作为 Harness 维护层的流程来源，而不是直接作为机制事实来源。后续 Codex 可以借鉴它的阶段化和 deliverable-driven 思路，但不应直接采用 agent swarm 假设；当前研究清洗 Harness 已经用 Source Card 方式替代了“读很多文件并总结”的原始计划。
