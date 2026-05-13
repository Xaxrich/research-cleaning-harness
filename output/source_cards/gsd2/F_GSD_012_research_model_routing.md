# Source Card: F_GSD_012 - research_model_routing

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_012 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/research_model_routing.md |
| file_type | markdown |
| topic | model routing, complexity classification, capability scoring, budget pressure, and escalation |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：解释 GSD2 如何根据任务复杂度、成本、能力、预算和失败情况选择模型，并把路由策略迁移到 iOS Harness。

## 3. File Summary

- 文件说明为什么需要模型路由：成本、速度、provider availability、弱模型价值和“用对的模型”。
- 它给出 complexity classification：heuristic zero LLM、tier definitions、default tier、budget pressure、adaptive learning 和 token profiles。
- 文件分析 capability scoring，包括 ADR-004、七个能力维度、动态权重、任务元数据调整、scoring selection 和 model families。
- 它讨论 failure escalation：失败后升级模型、context keep/drop、限制、adaptive 和 budget interplay。
- 文件提供 iOS routing table、PREFERENCES、弱模型边界、Composer2 特殊策略、success improvement 和 progressive routing。
- 对 iOS Harness 的价值是形成 `MODEL_ROUTING.md` 和任务复杂度字段。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-089 | Routing Rationale | 模型选择要平衡成本、速度、可用性和任务成功率。 | E1 | high |
| M-GSD-090 | Heuristic Complexity Classification | 使用启发式分类减少额外 LLM 判断成本。 | E2 | high |
| M-GSD-091 | Tiered Model Defaults | 为不同任务复杂度定义默认模型 tier。 | E3 | high |
| M-GSD-092 | Budget Pressure Adjustment | 在预算压力下改变路由选择。 | E4 | high |
| M-GSD-093 | Adaptive Learning | 根据历史成功率调整路由。 | E5 | medium |
| M-GSD-094 | Capability Scoring | 使用多维能力评分和动态权重选择模型。 | E6 | high |
| M-GSD-095 | Failure Escalation with Context Policy | 失败后升级模型，并决定保留或丢弃上下文。 | E7 | high |
| M-GSD-096 | iOS Model Routing Table | 为 iOS 任务提供具体模型偏好和弱模型边界。 | E8 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| model_underfit | tiered defaults 和 capability scoring 避免复杂任务选错模型。 | E3 |
| model_overkill | heuristic classification 和 budget pressure 避免简单任务浪费强模型。 | E2 |
| provider_unavailable | routing rationale 把 provider availability 纳入选择。 | E1 |
| repeated_failure_same_model | failure escalation 在失败后升级或改变上下文策略。 | E7 |
| weak_model_overreach | iOS routing table 和弱模型边界定义低能力模型可做范围。 | E8 |
| static_policy_decay | adaptive learning 用历史成功率修正路由。 | E5 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 启发式优先 | 降低路由成本 | 不应为了选模型再消耗一个复杂模型调用 | 启发式可能误判 |
| 能力评分 | 更细地匹配任务 | iOS 任务需要代码、架构、调试、发布等不同能力 | 评分表需要维护 |
| 失败后决定 context keep/drop | 避免把污染上下文带到强模型 | 有些失败来自坏上下文，不只是弱模型 | 丢弃上下文可能损失调查信息 |

## 7. 5 Why Analysis

### Mechanism: Failure Escalation with Context Policy

- Why 1: 因为任务失败可能来自模型能力不足。
- Why 2: 也可能来自上下文污染或错误假设。
- Why 3: 只升级模型会把错误上下文带给更贵模型。
- Why 4: 路由策略必须同时决定模型升级和 context keep/drop。
- Why 5: 所以 iOS Harness 的 `MODEL_ROUTING.md` 应与 `CONTEXT_RULES.md` 和 `FAILURE_LOG.md` 联动。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件说明模型路由动机包含 cost、speed、provider availability 和 weak model value。 | research_model_routing.md: rationale sections | M-GSD-089 |
| E2 | 文件讨论 heuristic zero LLM complexity classification。 | research_model_routing.md: complexity sections | M-GSD-090 |
| E3 | 文件定义 tier 和 default tier。 | research_model_routing.md: tier sections | M-GSD-091 |
| E4 | 文件讨论 budget pressure。 | research_model_routing.md: budget pressure section | M-GSD-092 |
| E5 | 文件讨论 adaptive learning。 | research_model_routing.md: adaptive learning section | M-GSD-093 |
| E6 | 文件讨论 ADR-004、七个能力维度、动态权重和 scoring selection。 | research_model_routing.md: capability scoring sections | M-GSD-094 |
| E7 | 文件讨论 failure escalation、context keep/drop、limits 和 budget interplay。 | research_model_routing.md: escalation sections | M-GSD-095 |
| E8 | 文件提供 iOS routing table、PREFERENCES、弱模型边界和 progressive routing。 | research_model_routing.md: iOS routing sections | M-GSD-096 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-089 | Role / Review Layer | MODEL_ROUTING.md | v0_1 | 记录模型选择原则 |
| M-GSD-090 | Task Layer | TASKS.md | v0_5 | 为任务添加 complexity 字段和启发式分类 |
| M-GSD-091 | Role / Review Layer | MODEL_ROUTING.md | v0_5 | 建立 tiered defaults |
| M-GSD-092 | Risk / Release Layer | MODEL_ROUTING.md | v0_5 | 在预算压力下调整策略 |
| M-GSD-093 | Harness Maintenance Layer | output/data/model_routing_feedback.jsonl | v1_0 | 记录历史成功率用于自适应 |
| M-GSD-094 | Role / Review Layer | MODEL_ROUTING.md | v1_0 | 引入多维能力评分 |
| M-GSD-095 | Feedback / Verification Layer | FAILURE_LOG.md | v0_5 | 失败后记录模型升级和 context policy |
| M-GSD-096 | Role / Review Layer | docs/agent/IOS_MODEL_ROUTING_TABLE.md | v0_5 | 为 iOS 任务建立路由表和弱模型边界 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 模型路由能提升成本、速度和任务成功率 |
| v0_1 | partial | v0.1 只需原则和人工判断 |
| v0_5 | yes | 增加复杂度字段、tier defaults、失败升级和 iOS routing table |
| v1_0 | yes | 能力评分和自适应学习适合 runtime 版本 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 源文档中的模型名称是否仍是最新 | 模型可用性和价格会变化 | 实现前用当前 provider 文档更新表格 |
| Composer2 特殊策略是否适用于用户环境 | 依赖具体工具和模型权限 | 在实际 Codex/iOS 开发环境中测试 |
| 自适应学习是否值得实现 | 需要足够历史数据 | 先记录 JSONL 路由反馈，观察样本量 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_007 | Stage 6 概括模型路由策略 |
| F_GSD_010 | token profile 和上下文策略相互影响 |
| F_GSD_011 | failure escalation 与失败恢复联动 |
| F_GSD_005 | MODEL_ROUTING 模板来源 |

## 13. Clean Summary for Codex

这个文件是 GSD2 模型路由专项卡。它的关键贡献是把“用哪个模型”从临时判断变成 task complexity、tier default、budget pressure、capability scoring、failure escalation 和 context policy 的组合。iOS Harness v0.1 只需写入人工路由原则；v0.5 应加入任务复杂度字段、iOS routing table 和失败升级记录；v1.0 再考虑能力评分和自适应学习。后续与其他框架融合时，它应作为模型选择和弱模型边界的主证据。

