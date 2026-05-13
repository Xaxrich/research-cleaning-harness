# Source Card: F_GSD_005 - report_stages_12_13_14

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_005 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/report_stages_12_13_14.md |
| file_type | markdown |
| topic | learning path, implementation templates, deliverables, and output standards |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把 GSD2 迁移研究转成学习路径、可复制模板、验证脚本清单、交付物目录和最终输出质量标准。

## 3. File Summary

- Stage 12 给出面向 iOS Harness 的三天学习路径。
- Day 1 聚焦状态机和任务系统，Day 2 聚焦上下文、模型路由和失败恢复，Day 3 聚焦 iOS App Store Harness。
- 文件提供 STATE/TASKS、MODEL_ROUTING、FAILURE_LOG 等模板。
- 它设计多类脚本：verify-state、verify-tasks、verification-runner、stuck-detector、complexity-classifier、integration-test。
- Stage 13 汇总 16 个交付物，覆盖文档、脚本、矩阵、检查清单和 handoff。
- Stage 14 定义输出格式、证据标注、质量检查和 unknowns 处理。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-029 | Progressive Learning Path | 将 GSD2 迁移能力拆成 Day 1/2/3 学习与实现路径。 | E1 | high |
| M-GSD-030 | State and Task Templates | 给出 STATE/TASKS 的字段化模板，支撑任务状态管理。 | E2 | high |
| M-GSD-031 | Routing and Failure Templates | 给出 MODEL_ROUTING 与 FAILURE_LOG 模板，支撑模型选择和恢复记录。 | E3 | high |
| M-GSD-032 | Validation Script Suite | 设计 verify-state、verify-tasks、runner、stuck-detector、classifier、integration-test 等脚本。 | E4 | high |
| M-GSD-033 | Deliverable Catalog | 用固定交付物清单约束最终产物完整性。 | E5 | high |
| M-GSD-034 | Evidence-Aware Output Standards | 要求输出保留证据、质量检查和 unknowns。 | E6 | high |
| M-GSD-035 | Template-to-Script Migration | 从文档模板逐步过渡到可执行脚本检查。 | E7 | medium |
| M-GSD-036 | Handoff-Oriented Packaging | 将研究输出组织为后续 Codex 可以读取的交接包。 | E8 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| knowledge_not_operationalized | 通过学习路径和模板把研究转成可执行资产。 | E1 |
| inconsistent_state_format | STATE/TASKS 模板固定字段。 | E2 |
| untracked_failures | FAILURE_LOG 模板要求记录失败与恢复。 | E3 |
| unverified_completion | 验证脚本套件让完成状态可检查。 | E4 |
| missing_handoff | 交付物目录和 handoff 包降低后续开发漏读风险。 | E5 |
| unsupported_claims | 输出标准要求证据标注和 unknowns。 | E6 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 三天学习路径 | 降低 GSD2 理解门槛 | 让后续 agent 能按学习顺序继承机制 | 真实项目可能需要更长落地时间 |
| 模板先行 | 快速标准化文档 | 先统一数据结构，再实现自动化 | 早期依赖人工填写 |
| 脚本套件 | 检查格式和执行证据 | 将 harness 从规则文本推进到半自动质量门 | 脚本需要维护 |

## 7. 5 Why Analysis

### Mechanism: Validation Script Suite

- Why 1: 因为 agent 容易在没有证据时声称任务完成。
- Why 2: 文档规则无法保证状态、任务和验证输出一致。
- Why 3: 脚本可以把格式、字段和引用错误暴露出来。
- Why 4: 自动检查能减少 review 的机械负担。
- Why 5: 所以 iOS Harness 应把关键质量门脚本化，而不是只写在 AGENTS.md 中。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Stage 12 包含 Day 1/2/3 学习路径。 | report_stages_12_13_14.md: Stage 12 headings | M-GSD-029 |
| E2 | 文件给出 STATE.md 和 TASKS.md 模板。 | report_stages_12_13_14.md: state/task template sections | M-GSD-030 |
| E3 | 文件给出 MODEL_ROUTING.md 和 FAILURE_LOG.md 模板。 | report_stages_12_13_14.md: routing/failure templates | M-GSD-031 |
| E4 | 文件列出 verify-state、verify-tasks、verification-runner、stuck-detector、complexity-classifier、integration-test。 | report_stages_12_13_14.md: validation script sections | M-GSD-032 |
| E5 | Stage 13 列出 16 个交付物。 | report_stages_12_13_14.md: deliverables list | M-GSD-033 |
| E6 | Stage 14 定义输出风格、证据标注、质量检查和 unknowns。 | report_stages_12_13_14.md: output standards sections | M-GSD-034 |
| E7 | 模板与脚本在同一阶段配套出现。 | report_stages_12_13_14.md: Day 1-3 and script sections | M-GSD-035 |
| E8 | 交付物包含面向后续开发的 handoff 资产。 | report_stages_12_13_14.md: deliverable/handoff sections | M-GSD-036 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-029 | Goal Layer | docs/agent/LEARNING_PATH.md | v0_5 | 给新 agent 提供三阶段理解路径 |
| M-GSD-030 | Memory / State Layer | STATE.md; TASKS.md | v0_1 | 固定状态和任务字段 |
| M-GSD-031 | Memory / State Layer | MODEL_ROUTING.md; FAILURE_LOG.md | v0_1 | 建立模型选择和失败记录模板 |
| M-GSD-032 | Feedback / Verification Layer | scripts/agent/ | v0_5 | 实现状态、任务、验证、卡住检测和复杂度分类脚本 |
| M-GSD-033 | Harness Maintenance Layer | output/ios_harness_mapping/codex_handoff.md | v0_1 | 用交付物清单约束 handoff |
| M-GSD-034 | Feedback / Verification Layer | QUALITY_GATE.md | v0_1 | 将证据、unknowns 和质量检查写入验收 |
| M-GSD-035 | Action / ACI Layer | scripts/agent/verification_runner.sh | v0_5 | 从文档模板迁移到脚本执行 |
| M-GSD-036 | Harness Maintenance Layer | output/ios_harness_mapping/codex_handoff.md | v0_1 | 打包后续 Codex 优先读取内容 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 它把研究成果转为模板、脚本和 handoff，是清洗后可执行化的关键 |
| v0_1 | yes | STATE/TASKS、质量门和交付目录应立即迁移 |
| v0_5 | yes | 验证脚本套件进入半自动执行 |
| v1_0 | yes | 可演进为 runtime 的任务验证和卡住检测层 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 所有脚本是否有可运行实现 | 文件主要是设计和模板 | 在后续 iOS Harness repo 中实现并运行脚本测试 |
| 三天学习路径是否适合所有 agent | 学习路径是建议，不是实验数据 | 用后续 agent handoff 实践记录反馈 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_004 | 提供文件架构，本文提供模板和脚本化落地 |
| F_GSD_008 | 验证、失败和 Git 机制在 Stage 7-9 中更细 |
| F_GSD_001 | 综合报告包含这些交付物结论 |

## 13. Clean Summary for Codex

这个文件把 GSD2 迁移从“知道机制”推进到“能交付、能检查、能交接”。对 iOS Harness 最重要的迁移点是：标准化 `STATE.md`/`TASKS.md`/`MODEL_ROUTING.md`/`FAILURE_LOG.md`，把验证和卡住检测写成脚本，并把最终交付物整理为 Codex handoff。后续与 Aider、Gstack、SWE-agent 融合时，这张卡应作为 clean data 质量门的模板来源，保证每个框架的机制不是停留在总结里，而是能落到文件、脚本和验收。

