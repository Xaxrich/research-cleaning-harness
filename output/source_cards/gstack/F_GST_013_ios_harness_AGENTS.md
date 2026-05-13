# Source Card: F_GST_013 - iOS Harness Agent 集群总纲

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GST_013 |
| framework | gstack |
| raw_path | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/AGENTS.md |
| file_type | markdown |
| topic | iOS Harness Agent 集群总纲 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 gstack 的 `ethos_core` 机制转成 iOS Harness 可读取、可审查、可迁移的 agent 集群治理资产。

## 3. File Summary

- 文件属于 gstack `ethos_core` 主题清洗资料。
- 它围绕 `iOS Harness Agent 集群总纲` 展开，提供 agent 集群治理、角色、工作流、审查或 guardrail 相关机制。
- 本卡只抽取当前 raw 文件中的机制，不跨文件自由综合。
- 核心迁移方向是 iOS Harness 的角色矩阵、审查矩阵、风险控制、工作流和弱模型任务边界。
- 后续合成阶段应把报告、模板、角色卡和 research 文件之间的重复机制去重。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GST-049 | Search Before Building | 先搜索现有知识和实现，再新增能力。 | E1 | high |
| M-GST-050 | User Sovereignty | 用户目标和约束优先于框架偏好。 | E2 | high |
| M-GST-051 | Long-Running Task Persistence | 长任务不要轻易放弃，需要计划、状态和恢复。 | E3 | high |
| M-GST-052 | Engineering Quality Over AI Style | 关注真实质量问题，不做表面化 AI 文风修饰。 | E4 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| reinventing_work | search before building 减少重复建设。 | E1 |
| framework_overreach | user sovereignty 保持用户目标优先。 | E2 |
| task_abandonment | 长任务状态和恢复防止半途丢失。 | E3 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 逐文件清洗 gstack ethos_core 资料 | 保持 source card 可追溯 | gstack 目录同时包含研究报告、角色卡、工作流和模板包，需要先标准化再合成 | 机制会重复，需要 framework summary 去重 |
| 将角色/审查/风险落到 iOS Harness 文件 | 让 Codex 后续能直接读取治理规则 | gstack 的价值在于虚拟工程团队和 agent 集群治理 | v0.1 先是文档规则，hook/runtime 延后 |
| 标注模板与 runtime 边界 | 防止把交付物误认为已执行能力 | 当前 raw 是研究资产和模板，不代表本项目已有自动拦截 runtime | 需要后续脚本实现和验证 |

## 7. 5 Why Analysis

### Mechanism: Search Before Building

- Why 1: 因为 iOS Harness 后续会涉及 Flutter、Firebase、Swift、QA、安全和发布多类工作。
- Why 2: 单一 agent 规则很难同时覆盖所有角色责任和阻断权。
- Why 3: gstack 用角色、workflow、review chain 和 guardrails 把 agent 行为组织成虚拟工程团队。
- Why 4: 这些机制可以落到 `ROLE_MATRIX.md`、`REVIEW_MATRIX.md`、`RISK_CONTROL.md` 和 workflow 文档。
- Why 5: 所以该文件的价值在于提供 agent 集群治理零件，而不是要求直接复制 gstack 工具链。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 主标题/首个 heading 指向：iOS Harness Agent 集群总纲。 | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/AGENTS.md:1 | source topic |
| E2 | 关键结构摘要：iOS Harness Agent 集群总纲; 目录; 一、项目目标和范围; 1.1 目标; 1.2 范围; 1.3 设计哲学。 | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/AGENTS.md:structure | mechanism structure |
| E3 | inventory 主题为：iOS Harness Agent 集群总纲。 | SOURCE_INVENTORY.md | estimated topic |
| E4 | 文件类别 `markdown`，度量值 776，细节：markdown headings。 | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/AGENTS.md:full file | scope and density |
| E5 | 该文件归类为 gstack `ethos_core` 清洗资料。 | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/AGENTS.md:path | framework category |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GST-049 | Context Layer | CONTEXT_RULES.md | v0_1 | 要求任务前检索相关 source cards。 |
| M-GST-050 | Goal Layer | AGENTS.md | v0_1 | 写入 harness 执行原则。 |
| M-GST-051 | Memory / State Layer | STATE.md | v0_1 | 维护任务进度和阻塞。 |
| M-GST-052 | Feedback / Verification Layer | QUALITY_GATE.md | v0_1 | 把质量门聚焦到行为和证据。 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 当前文件提供 gstack ethos_core 机制，可转成 iOS Harness 的角色、审查、风险或工作流规则 |
| v0_1 | yes | 角色矩阵、审查规则和风险边界可以立即迁移为文档 |
| v0_5 | yes | guardrails、workflow checks 和 evidence 记录可进一步脚本化 |
| v1_0 | partial | hook enforcement、自动 review chain 和 agent cluster runtime 需要延后 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 该文件中的 gstack 机制是否完全适配当前 iOS 项目 | raw 文件是研究/模板资料，不是实际项目运行记录 | 在 iOS Harness 实现阶段用真实 Flutter/Firebase/Swift/release 任务验证 |
| 与其他 gstack report/template 是否重复 | gstack raw 同时包含完整报告、分段报告、角色卡和交付物 | 在 `gstack_summary.md` 合成时去重并保留最具体证据 |
| hook 或命令 guardrail 是否已经可执行 | 本卡只清洗研究资产，不实现 runtime hook | 后续检查 `scripts/agent/` 是否有对应实现和测试 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_001 | Superpowers methodology overview |
| F_AID_010 | Aider concepts |

## 13. Clean Summary for Codex

这张卡把 `iOS Harness Agent 集群总纲` 从原始 gstack 研究或模板文件转成可被 Codex 消费的 clean asset。后续 iOS Harness 构建时，不应直接读取 raw 文件理解 gstack，而应读取这张 Source Card 及其 framework summary。它的主要价值是把 gstack 的虚拟工程团队、角色矩阵、审查链路、风险控制、工作流、技能路由或 guardrail 机制迁移到 iOS Harness 的 Role/Review、Risk/Release、Task、Action 和 Feedback 层。合成阶段需要与 Superpowers 的工程纪律、GSD2 的状态/上下文/验证机制、Aider 的 repo/file scope 机制以及后续 SWE-agent 的 tool/runtime 机制去重融合。
