# Source Card: F_GSD_007 - report_stages_4_5_6

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_007 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/report_stages_4_5_6.md |
| file_type | markdown |
| topic | task state machine, context management, and model routing |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把 GSD2 的任务状态机、上下文注入策略和模型路由规则细化为可迁移到 iOS Harness 的工作单元协议。

## 3. File Summary

- Stage 4 定义 task state machine，以及 milestone/slice/task 的任务卡字段。
- 文件强调任务需要大小、输入、输出、must-haves、上下文窗口、模型路由、验证和失败恢复信息。
- Stage 5 分析 context rot，提出 fresh session、pre-inlined injection、P0/P1/P2/P3 priority、excluded content、summary/projection/database 和弱模型最小上下文策略。
- Stage 6 分析模型路由：tier、启发式信号、任务类型默认模型、失败升级、预算压力、能力评分和 progressive routing。
- 文件将三者连接：任务卡同时绑定上下文、模型、验证和恢复。
- 对 iOS Harness 的价值是提供 task card schema 和 context/model 联动规则。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-046 | Task Card Schema | 任务卡必须记录目标、大小、输入、输出、must-haves 和状态。 | E1 | high |
| M-GSD-047 | Context Window Binding | 每个任务显式绑定应注入的上下文窗口。 | E2 | high |
| M-GSD-048 | Model Routing Binding | 每个任务显式绑定或推导模型路由策略。 | E3 | high |
| M-GSD-049 | Verification and Recovery Binding | 任务卡包含验证要求和失败恢复路径。 | E4 | high |
| M-GSD-050 | Context Priority Bands | 用 P0/P1/P2/P3 区分必须、相关、可选和排除上下文。 | E5 | high |
| M-GSD-051 | Excluded Content Rule | 明确禁止注入会污染任务的上下文。 | E6 | high |
| M-GSD-052 | Weak Model Minimal Context | 给弱模型只提供高度压缩、任务相关上下文。 | E7 | high |
| M-GSD-053 | Capability and Budget Routing | 使用复杂度、预算压力和能力评分选择模型。 | E8 | high |
| M-GSD-054 | Progressive Routing | 从低成本模型开始，失败后逐级升级。 | E9 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| underspecified_task | task card schema 要求目标、输入、输出和 must-haves。 | E1 |
| context_rot | fresh session、priority bands 和 excluded content 控制上下文。 | E5 |
| weak_model_confusion | 弱模型最小上下文减少噪声。 | E7 |
| model_overkill | capability/budget routing 避免简单任务使用过强模型。 | E8 |
| model_underfit | progressive routing 在失败后升级模型。 | E9 |
| no_recovery_path | verification/recovery binding 让任务失败可处理。 | E4 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| task card 承载上下文和模型 | 任务执行前就能准备环境 | 任务是上下文、模型和验证的交汇点 | card 字段变多 |
| P0-P3 上下文优先级 | 控制 token 使用 | 上下文质量比上下文数量更重要 | 需要人工判断优先级 |
| 失败后升级模型 | 平衡成本和成功率 | 默认强模型会浪费，默认弱模型会卡住 | 需要记录失败原因 |

## 7. 5 Why Analysis

### Mechanism: Context Priority Bands

- Why 1: 因为 agent 上下文窗口有限。
- Why 2: 多余上下文会引发 context rot 和注意力稀释。
- Why 3: 任务成功通常依赖少量高相关材料。
- Why 4: 优先级能让 harness 决定什么必须注入、什么必须排除。
- Why 5: 所以 iOS Harness 应把上下文选择做成任务字段，而不是依赖 agent 临时判断。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Stage 4 讨论 task card 的大小、输入、输出和 must-haves。 | report_stages_4_5_6.md: Stage 4 task card sections | M-GSD-046 |
| E2 | Stage 4 包含 context window binding。 | report_stages_4_5_6.md: context binding section | M-GSD-047 |
| E3 | Stage 4 包含 model routing binding。 | report_stages_4_5_6.md: model routing binding section | M-GSD-048 |
| E4 | Stage 4 包含 verification 和 failure recovery binding。 | report_stages_4_5_6.md: verification/recovery sections | M-GSD-049 |
| E5 | Stage 5 使用 P0/P1/P2/P3 priority。 | report_stages_4_5_6.md: context priority section | M-GSD-050 |
| E6 | Stage 5 包含 excluded content。 | report_stages_4_5_6.md: excluded content section | M-GSD-051 |
| E7 | Stage 5 给出 weak model context minimal strategy。 | report_stages_4_5_6.md: weak model context section | M-GSD-052 |
| E8 | Stage 6 讨论 budget pressure 和 capability scoring。 | report_stages_4_5_6.md: routing/scoring sections | M-GSD-053 |
| E9 | Stage 6 讨论 failure escalation 和 progressive routing。 | report_stages_4_5_6.md: progressive routing sections | M-GSD-054 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-046 | Task Layer | TASKS.md | v0_1 | 增加 task card 字段模板 |
| M-GSD-047 | Context Layer | CONTEXT_RULES.md | v0_1 | 每个任务列出 allowed_context |
| M-GSD-048 | Role / Review Layer | MODEL_ROUTING.md | v0_5 | 任务类型映射模型 tier |
| M-GSD-049 | Feedback / Verification Layer | VERIFICATION_MATRIX.md; FAILURE_LOG.md | v0_1 | 每个任务有验证与恢复字段 |
| M-GSD-050 | Context Layer | CONTEXT_INDEX.md | v0_1 | 用 P0-P3 管理上下文注入 |
| M-GSD-051 | Context Layer | CONTEXT_RULES.md | v0_1 | 增加 forbidden_context 字段 |
| M-GSD-052 | Context Layer | docs/agent/WEAK_MODEL_CONTEXT.md | v0_5 | 定义弱模型最小上下文包 |
| M-GSD-053 | Role / Review Layer | MODEL_ROUTING.md | v0_5 | 使用复杂度、预算和能力评分 |
| M-GSD-054 | Feedback / Verification Layer | FAILURE_LOG.md | v0_5 | 失败后记录升级模型路径 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 这是 GSD2 对 iOS Harness 最关键的任务/上下文/模型协议 |
| v0_1 | yes | task card、context priority、verification binding 应立即迁移 |
| v0_5 | yes | 模型路由和弱模型策略可进入增强版 |
| v1_0 | yes | 可实现自动复杂度分类和模型升级 runtime |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| P0-P3 是否过细 | iOS v0.1 可能只需要 required/optional/forbidden | 在首轮任务执行后比较上下文错误率 |
| progressive routing 是否需要自动化 | 当前阶段可能由 Codex 人工判断模型 | 记录失败升级案例后再决定是否脚本化 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_006 | 提供核心概念总览 |
| F_GSD_010 | 深入 context rot 和上下文策略 |
| F_GSD_012 | 深入模型路由和升级策略 |
| F_GSD_005 | 提供 STATE/TASKS/MODEL_ROUTING 模板 |

## 13. Clean Summary for Codex

这个文件是 GSD2 任务执行协议的核心。它告诉 Codex：任务不是一句目标，而应同时包含输入、输出、must-haves、上下文优先级、模型路由、验证标准和失败恢复路径。对 iOS Harness 来说，v0.1 应立即迁移 task card schema、context priority 和 forbidden context；v0.5 再加入复杂度分类、弱模型上下文包和 progressive routing。后续与 Aider 的 repo map、SWE-agent 的 tool/verification 机制融合时，这张卡可作为任务级控制面的主锚点。

