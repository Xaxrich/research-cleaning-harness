# Source Card: F_SWE_007 - SWE-agent Trajectory/Replay 体系、配置系统、环境抽象深度研究报告

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SWE_007 |
| framework | swe-agent |
| raw_path | raw/Kimi_Agent_SWE-agent 迁移研究/research/swe_trajectory_config.md |
| file_type | markdown |
| topic | SWE-agent Trajectory/Replay 体系、配置系统、环境抽象深度研究报告 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 SWE-agent 的 `trajectory` 机制转成 iOS Harness 可审计、可执行、可回放的 ACI 资产。

## 3. File Summary

- 文件属于 SWE-agent `trajectory` 主题清洗资料。
- 它围绕 `SWE-agent Trajectory/Replay 体系、配置系统、环境抽象深度研究报告` 展开，主要贡献 ACI、工具、环境反馈、trajectory、workflow 或安全边界。
- 本卡只抽取当前 raw 文件中的机制，不跨文件自由综合。
- 核心迁移方向是 iOS Harness 的 Action / ACI Layer、Feedback / Verification Layer、Memory / State Layer 和 Risk / Release Layer。
- 后续合成阶段需要与 Aider 的 repo/file scope、GSD2 的状态机、gstack 的角色矩阵和 Superpowers 的工程纪律去重。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SWE-025 | Trajectory Log Format | 记录 task metadata、thought/action/observation、state snapshot、termination 和 escalation。 | E1 | high |
| M-SWE-026 | Replay for Debugging | 用 trajectory 重放定位 stuck loop、错误命令和越界编辑。 | E2 | high |
| M-SWE-027 | Config and Trajectory Coupling | 把模型、工具、环境配置写入轨迹，保证结果可解释。 | E3 | high |
| M-SWE-028 | Privacy-Aware Logging | trajectory 不能无边界记录 secrets、隐私数据或完整源码。 | E4 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| untraceable_failure | trajectory 记录每步 action/observation。 | E1 |
| stuck_loop | replay 帮助定位循环。 | E2 |
| privacy_leak | 日志需 redaction。 | E4 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 逐文件清洗 SWE-agent trajectory 资料 | 保持 source card 可追溯 | SWE-agent raw 同时包含完整报告、分段报告、docx 和研究章节，需要先标准化再合成 | 机制会重复，需要 framework summary 去重 |
| 将工具、命令、轨迹落到 iOS Harness ACI 层 | 让 Codex 后续能直接实现 view/search/edit/run/verify 等工具 | SWE-agent 的核心价值是 agent-computer interface 和环境反馈，而不是角色治理 | v0.1 只能先沉淀契约和风险规则，脚本/runtime 延后 |
| 标注安全和版本边界 | 防止把研究建议误称为已实现能力 | iOS release、privacy、Firebase、签名和原生桥接都有高风险 | 需要后续实现脚本并跑真实测试 |

## 7. 5 Why Analysis

### Mechanism: Trajectory Log Format

- Why 1: 因为 iOS Harness 后续需要让 agent 读取文件、搜索代码、编辑、执行命令、测试和记录结果。
- Why 2: 如果这些动作只靠自由文本提示，模型容易越界、臆造结果或遗漏验证。
- Why 3: SWE-agent 的 ACI 思路把动作压缩为工具契约和环境反馈。
- Why 4: 这些契约可以迁移为 `scripts/agent/`、`VERIFICATION_MATRIX.md`、`RISK_CONTROL.md` 和 trajectory 数据。
- Why 5: 所以该文件的价值在于提供工具执行层和可回放证据，而不是替代 Superpowers/GSD2/Aider/gstack 的其他层。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 主标题/首个 heading 指向：SWE-agent Trajectory/Replay 体系、配置系统、环境抽象深度研究报告。 | raw/Kimi_Agent_SWE-agent 迁移研究/research/swe_trajectory_config.md:1 | source topic |
| E2 | 关键结构摘要：SWE-agent Trajectory/Replay 体系、配置系统、环境抽象深度研究报告; 目录; 第一部分：Trajectory 体系; 1.1 概述; 1.2 TrajectoryStep 类型定义; sweagent/types.py。 | raw/Kimi_Agent_SWE-agent 迁移研究/research/swe_trajectory_config.md:structure | mechanism structure |
| E3 | inventory 主题为：SWE-agent Trajectory/Replay 体系、配置系统、环境抽象深度研究报告。 | SOURCE_INVENTORY.md | estimated topic |
| E4 | 文件类别 `markdown`，度量值 804，细节：markdown headings。 | raw/Kimi_Agent_SWE-agent 迁移研究/research/swe_trajectory_config.md:full file | scope and density |
| E5 | 该文件归类为 SWE-agent `trajectory` 清洗资料。 | raw/Kimi_Agent_SWE-agent 迁移研究/research/swe_trajectory_config.md:path | framework category |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-SWE-025 | Memory / State Layer | output/data/trajectory.jsonl | v0_5 | 建立 iOS Harness 可回放日志。 |
| M-SWE-026 | Feedback / Verification Layer | scripts/agent/replay_trajectory.sh | v1_0 | 后续实现回放工具。 |
| M-SWE-027 | Memory / State Layer | CONFIG.md | v0_5 | 将 config hash 或参数写入日志。 |
| M-SWE-028 | Risk / Release Layer | PRIVACY_CHECKLIST.md | v0_1 | 加入 redaction 和敏感文件规则。 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 当前文件提供 SWE-agent trajectory 机制，可转成 iOS Harness 的 ACI 工具、验证、轨迹或风险规则 |
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
| F_GSD_008 | task state and verification |
| F_SWE_021 | trajectory section |

## 13. Clean Summary for Codex

这张卡把 `SWE-agent Trajectory/Replay 体系、配置系统、环境抽象深度研究报告` 从原始 SWE-agent 调研文件转成可被 Codex 消费的 clean asset。后续 iOS Harness 构建时，不应直接读取 raw 文件理解 SWE-agent，而应读取这张 Source Card 及其 framework summary。它的主要价值是把 SWE-agent 的 Agent-Computer Interface、受控工具调用、环境反馈、trajectory/replay、命令验证、安全权限和 iOS 场景 workflow 迁移到 Harness 的 Action、Feedback、Memory 和 Risk 层。合成阶段需要与 Aider 的 repo/file scope、GSD2 的状态机与验证闭环、gstack 的角色/审查治理、Superpowers 的工程纪律融合。
