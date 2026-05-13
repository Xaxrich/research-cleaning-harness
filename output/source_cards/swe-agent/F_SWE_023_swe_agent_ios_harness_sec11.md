# Source Card: F_SWE_023 - 11. iOS Harness ACI 工具设计

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SWE_023 |
| framework | swe-agent |
| raw_path | raw/Kimi_Agent_SWE-agent 迁移研究/swe_agent_ios_harness_sec11.md |
| file_type | markdown |
| topic | 11. iOS Harness ACI 工具设计 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 SWE-agent 的 `ios_aci_design` 机制转成 iOS Harness 可审计、可执行、可回放的 ACI 资产。

## 3. File Summary

- 文件属于 SWE-agent `ios_aci_design` 主题清洗资料。
- 它围绕 `11. iOS Harness ACI 工具设计` 展开，主要贡献 ACI、工具、环境反馈、trajectory、workflow 或安全边界。
- 本卡只抽取当前 raw 文件中的机制，不跨文件自由综合。
- 核心迁移方向是 iOS Harness 的 Action / ACI Layer、Feedback / Verification Layer、Memory / State Layer 和 Risk / Release Layer。
- 后续合成阶段需要与 Aider 的 repo/file scope、GSD2 的状态机、gstack 的角色矩阵和 Superpowers 的工程纪律去重。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SWE-089 | iOS ACI Tool Suite | 把 iOS Harness 需要的工具拆成 view/search/context/edit/run/test/build/privacy/release/trajectory 等脚本。 | E1 | high |
| M-SWE-090 | Tool Contract Schema | 每个工具需要输入、输出、失败码和安全级别。 | E2 | high |
| M-SWE-091 | Task-to-Tool Routing | 不同 iOS 任务选择不同工具组合。 | E3 | high |
| M-SWE-092 | ACI Version Gate | v0.1 保留文档规则，v0.5 引入脚本，v1.0 才做 runtime 拦截。 | E4 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| tooling_gap | 工具套件覆盖 iOS agent 常用动作。 | E1 |
| tool_contract_ambiguity | 工具契约规定输入输出失败码。 | E2 |
| version_confusion | 版本 gate 区分文档、脚本和 runtime。 | E4 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 逐文件清洗 SWE-agent ios_aci_design 资料 | 保持 source card 可追溯 | SWE-agent raw 同时包含完整报告、分段报告、docx 和研究章节，需要先标准化再合成 | 机制会重复，需要 framework summary 去重 |
| 将工具、命令、轨迹落到 iOS Harness ACI 层 | 让 Codex 后续能直接实现 view/search/edit/run/verify 等工具 | SWE-agent 的核心价值是 agent-computer interface 和环境反馈，而不是角色治理 | v0.1 只能先沉淀契约和风险规则，脚本/runtime 延后 |
| 标注安全和版本边界 | 防止把研究建议误称为已实现能力 | iOS release、privacy、Firebase、签名和原生桥接都有高风险 | 需要后续实现脚本并跑真实测试 |

## 7. 5 Why Analysis

### Mechanism: iOS ACI Tool Suite

- Why 1: 因为 iOS Harness 后续需要让 agent 读取文件、搜索代码、编辑、执行命令、测试和记录结果。
- Why 2: 如果这些动作只靠自由文本提示，模型容易越界、臆造结果或遗漏验证。
- Why 3: SWE-agent 的 ACI 思路把动作压缩为工具契约和环境反馈。
- Why 4: 这些契约可以迁移为 `scripts/agent/`、`VERIFICATION_MATRIX.md`、`RISK_CONTROL.md` 和 trajectory 数据。
- Why 5: 所以该文件的价值在于提供工具执行层和可回放证据，而不是替代 Superpowers/GSD2/Aider/gstack 的其他层。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 主标题/首个 heading 指向：11. iOS Harness ACI 工具设计。 | raw/Kimi_Agent_SWE-agent 迁移研究/swe_agent_ios_harness_sec11.md:1 | source topic |
| E2 | 关键结构摘要：11. iOS Harness ACI 工具设计; 11.1 目标结构概览; 11.1.1 scripts/agent/ 目录：17个脚本; 核心脚本（5个）— 文件查看、搜索、编辑、上下文管理、命令执行; 验证脚本（4个）— 静态分析、测试、构建; iOS 专用脚本（3个）— Firebase、隐私、发布。 | raw/Kimi_Agent_SWE-agent 迁移研究/swe_agent_ios_harness_sec11.md:structure | mechanism structure |
| E3 | inventory 主题为：11. iOS Harness ACI 工具设计。 | SOURCE_INVENTORY.md | estimated topic |
| E4 | 文件类别 `markdown`，度量值 384，细节：markdown headings。 | raw/Kimi_Agent_SWE-agent 迁移研究/swe_agent_ios_harness_sec11.md:full file | scope and density |
| E5 | 该文件归类为 SWE-agent `ios_aci_design` 清洗资料。 | raw/Kimi_Agent_SWE-agent 迁移研究/swe_agent_ios_harness_sec11.md:path | framework category |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-SWE-089 | Action / ACI Layer | scripts/agent/ | v0_5 | 形成 iOS ACI 工具目录。 |
| M-SWE-090 | Action / ACI Layer | docs/agent/ACI_TOOL_CONTRACTS.md | v0_5 | 为工具调用写契约。 |
| M-SWE-091 | Task Layer | TASKS.md | v0_5 | 在 task card 中加入 required_tools。 |
| M-SWE-092 | Risk / Release Layer | output/ios_harness_mapping/v0_5_scope.md | v0_5 | 区分版本能力。 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 当前文件提供 SWE-agent ios_aci_design 机制，可转成 iOS Harness 的 ACI 工具、验证、轨迹或风险规则 |
| v0_1 | yes | 概念、契约、安全边界、任务模板和验证矩阵可立即迁移为文档 |
| v0_5 | yes | view/search/edit/run/verify、trajectory 和 context pack 可脚本化 |
| v1_0 | partial | replay、runtime interception、权限系统和自动工具调度需要真实实现和测试 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 该文件的 SWE-agent 机制是否完全适配当前 iOS 项目 | raw 文件是研究资产，不是实际项目执行记录 | 在 iOS Harness 实现阶段用 Flutter/Firebase/Swift/release 任务验证 |
| 与完整报告、converted 报告或分节文件是否重复 | SWE-agent raw 包含重复报告形态和章节拆分 | 在 `swe_agent_summary.md` 合成时去重并优先保留最具体章节证据 |
| ACI 工具是否已经可执行 | 本卡只清洗研究资料，不实现工具 runtime | 后续检查 `scripts/agent/` 实现、权限和测试结果 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SWE_005 | ACI mechanism research |

## 13. Clean Summary for Codex

这张卡把 `11. iOS Harness ACI 工具设计` 从原始 SWE-agent 调研文件转成可被 Codex 消费的 clean asset。后续 iOS Harness 构建时，不应直接读取 raw 文件理解 SWE-agent，而应读取这张 Source Card 及其 framework summary。它的主要价值是把 SWE-agent 的 Agent-Computer Interface、受控工具调用、环境反馈、trajectory/replay、命令验证、安全权限和 iOS 场景 workflow 迁移到 Harness 的 Action、Feedback、Memory 和 Risk 层。合成阶段需要与 Aider 的 repo/file scope、GSD2 的状态机与验证闭环、gstack 的角色/审查治理、Superpowers 的工程纪律融合。
