# Source Card: F_GST_007 - Role: Product Spec（产品规格 Agent）

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GST_007 |
| framework | gstack |
| raw_path | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/.agents/roles/product-spec.md |
| file_type | markdown |
| topic | Role: Product Spec（产品规格 Agent） |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 gstack 的 `role_card` 机制转成 iOS Harness 可读取、可审查、可迁移的 agent 集群治理资产。

## 3. File Summary

- 文件属于 gstack `role_card` 主题清洗资料。
- 它围绕 `Role: Product Spec（产品规格 Agent）` 展开，提供 agent 集群治理、角色、工作流、审查或 guardrail 相关机制。
- 本卡只抽取当前 raw 文件中的机制，不跨文件自由综合。
- 核心迁移方向是 iOS Harness 的角色矩阵、审查矩阵、风险控制、工作流和弱模型任务边界。
- 后续合成阶段应把报告、模板、角色卡和 research 文件之间的重复机制去重。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GST-025 | Specialized Agent Role Card | 为单个 iOS agent 角色定义职责、输入、输出和边界。 | E1 | high |
| M-GST-026 | Role-Specific File Ownership | 角色只处理自己负责的 Flutter/Firebase/Swift/QA/Release 范围。 | E2 | high |
| M-GST-027 | Role Handoff Contract | 角色间通过明确输入输出交接，避免职责混乱。 | E3 | high |
| M-GST-028 | Role Escalation Boundary | 超出职责时升级给 orchestrator 或高风险 reviewer。 | E4 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| role_confusion | 角色卡固定职责和边界。 | E1 |
| wrong_file_edit | 角色绑定文件范围。 | E2 |
| handoff_gap | 输入输出契约减少交接缺口。 | E3 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 逐文件清洗 gstack role_card 资料 | 保持 source card 可追溯 | gstack 目录同时包含研究报告、角色卡、工作流和模板包，需要先标准化再合成 | 机制会重复，需要 framework summary 去重 |
| 将角色/审查/风险落到 iOS Harness 文件 | 让 Codex 后续能直接读取治理规则 | gstack 的价值在于虚拟工程团队和 agent 集群治理 | v0.1 先是文档规则，hook/runtime 延后 |
| 标注模板与 runtime 边界 | 防止把交付物误认为已执行能力 | 当前 raw 是研究资产和模板，不代表本项目已有自动拦截 runtime | 需要后续脚本实现和验证 |

## 7. 5 Why Analysis

### Mechanism: Specialized Agent Role Card

- Why 1: 因为 iOS Harness 后续会涉及 Flutter、Firebase、Swift、QA、安全和发布多类工作。
- Why 2: 单一 agent 规则很难同时覆盖所有角色责任和阻断权。
- Why 3: gstack 用角色、workflow、review chain 和 guardrails 把 agent 行为组织成虚拟工程团队。
- Why 4: 这些机制可以落到 `ROLE_MATRIX.md`、`REVIEW_MATRIX.md`、`RISK_CONTROL.md` 和 workflow 文档。
- Why 5: 所以该文件的价值在于提供 agent 集群治理零件，而不是要求直接复制 gstack 工具链。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 主标题/首个 heading 指向：Role: Product Spec（产品规格 Agent）。 | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/.agents/roles/product-spec.md:1 | source topic |
| E2 | 关键结构摘要：Role: Product Spec（产品规格 Agent）; 身份定义; 职责范围; 输入; 输出; 输出格式规范。 | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/.agents/roles/product-spec.md:structure | mechanism structure |
| E3 | inventory 主题为：Role: Product Spec（产品规格 Agent）。 | SOURCE_INVENTORY.md | estimated topic |
| E4 | 文件类别 `markdown`，度量值 259，细节：markdown headings。 | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/.agents/roles/product-spec.md:full file | scope and density |
| E5 | 该文件归类为 gstack `role_card` 清洗资料。 | raw/Kimi_Agent_gstack 多 Agent 迁移/ios-harness/.agents/roles/product-spec.md:path | framework category |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GST-025 | Role / Review Layer | ROLE_MATRIX.md | v0_1 | 将角色卡汇总进角色矩阵。 |
| M-GST-026 | Task Layer | TASKS.md | v0_1 | 任务卡绑定 owner_role。 |
| M-GST-027 | Memory / State Layer | STATE.md | v0_5 | 记录 upstream/downstream role。 |
| M-GST-028 | Risk / Release Layer | RISK_CONTROL.md | v0_1 | 把 role boundary breach 作为风险事件。 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 当前文件提供 gstack role_card 机制，可转成 iOS Harness 的角色、审查、风险或工作流规则 |
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
| F_GST_017 | ROLE_MATRIX 汇总角色定义 |
| F_GSD_007 | GSD2 task binding |

## 13. Clean Summary for Codex

这张卡把 `Role: Product Spec（产品规格 Agent）` 从原始 gstack 研究或模板文件转成可被 Codex 消费的 clean asset。后续 iOS Harness 构建时，不应直接读取 raw 文件理解 gstack，而应读取这张 Source Card 及其 framework summary。它的主要价值是把 gstack 的虚拟工程团队、角色矩阵、审查链路、风险控制、工作流、技能路由或 guardrail 机制迁移到 iOS Harness 的 Role/Review、Risk/Release、Task、Action 和 Feedback 层。合成阶段需要与 Superpowers 的工程纪律、GSD2 的状态/上下文/验证机制、Aider 的 repo/file scope 机制以及后续 SWE-agent 的 tool/runtime 机制去重融合。
