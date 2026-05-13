# Source Card: F_GSD_006 - report_stages_1_2_3

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_006 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/report_stages_1_2_3.md |
| file_type | markdown |
| topic | GSD2 overview, core concepts, and iOS migration value |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：建立 GSD2 的整体认知基线，解释其多 agent runtime、核心概念和可迁移到 iOS Harness 的控制机制。

## 3. File Summary

- Stage 1 定义研究问题和资料收集边界。
- Stage 2 解释 GSD2 的架构和运行模型。
- Stage 3 提炼核心概念：milestone、slice、task、fresh session、context injection、worktree、database truth、markdown projection、auto mode、stuck loop、crash recovery、model routing、verification gate。
- 文件强调 GSD2 是通过状态、上下文和验证来约束 agent 执行。
- 它为后续 Stage 4-14 的细化机制提供总览。
- 对 iOS Harness 的主要价值是定义哪些 GSD2 概念值得迁移。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-037 | Research Question Framing | 先明确研究要回答哪些 GSD2 机制和迁移问题。 | E1 | high |
| M-GSD-038 | GSD2 Runtime Overview | 将 GSD2 理解为多 agent 编排、状态持久化和自动推进系统。 | E2 | high |
| M-GSD-039 | Milestone-Slice-Task Hierarchy | 用三层工作单元拆解目标、阶段和可执行任务。 | E3 | high |
| M-GSD-040 | Fresh Session per Task | 用 fresh session 降低上下文污染和旧对话残留。 | E4 | high |
| M-GSD-041 | Context Injection Instead of Chat History | 每个任务注入必要上下文，而不是依赖完整聊天历史。 | E5 | high |
| M-GSD-042 | Database Truth with Markdown Projection | 用数据库作为真实状态源，用 Markdown 作为 agent 可读投影。 | E6 | high |
| M-GSD-043 | Auto Mode and Recovery Loop | 用自动推进、卡住检测和 crash recovery 维持长任务连续性。 | E7 | high |
| M-GSD-044 | Dynamic Model Routing and Token Control | 根据任务复杂度、预算和上下文压力选择模型与 token 策略。 | E8 | high |
| M-GSD-045 | Verification Gate Completion | 任务完成需要验证证据和完成条件，而不是只看模型声明。 | E9 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| unclear_research_goal | Stage 1 先设定核心问题。 | E1 |
| weak_work_breakdown | Milestone/Slice/Task 将大目标切成可执行层级。 | E3 |
| context_pollution | fresh session 和 context injection 限制旧上下文影响。 | E4 |
| lost_state | 数据库真相源和 Markdown 投影分离状态存储与读取界面。 | E6 |
| stuck_loop | auto mode 配合卡住检测和恢复策略。 | E7 |
| model_mismatch | 动态模型路由避免复杂任务使用过弱模型或简单任务浪费强模型。 | E8 |
| false_completion | verification gate 要求证据。 | E9 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 先总览再细化 | 让读者建立共同词汇 | 后续细节才能稳定映射到同一机制库 | 总览文件会与后续报告重复 |
| 引入三层任务模型 | 管理复杂目标 | agent 需要比普通待办更强的层级状态 | 小任务可能显得繁琐 |
| 数据库与 Markdown 分层 | 兼顾可靠状态和模型可读性 | runtime 需要结构化真相源，agent 需要轻量上下文 | iOS v0.1 可能只能先实现 Markdown 子集 |

## 7. 5 Why Analysis

### Mechanism: Database Truth with Markdown Projection

- Why 1: 因为多 agent 长任务会频繁更新状态。
- Why 2: 纯 Markdown 容易出现并发覆盖、字段漂移和历史污染。
- Why 3: 数据库能保存结构化真相和恢复信息。
- Why 4: 但模型更适合读取简洁 Markdown。
- Why 5: 所以 GSD2 把 DB 作为真相源，把 Markdown 作为可读投影；iOS Harness 可以在 v0.1 先模拟该分层。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Stage 1 聚焦核心问题与资料收集。 | report_stages_1_2_3.md: Stage 1 headings | M-GSD-037 |
| E2 | Stage 2 解释 GSD2 架构和运行方式。 | report_stages_1_2_3.md: Stage 2 headings | M-GSD-038 |
| E3 | 文件讨论 milestone、slice、task 概念。 | report_stages_1_2_3.md: core concepts sections | M-GSD-039 |
| E4 | 文件讨论 fresh session 和 context reset。 | report_stages_1_2_3.md: context sections | M-GSD-040 |
| E5 | 文件讨论 context injection。 | report_stages_1_2_3.md: context injection section | M-GSD-041 |
| E6 | 文件讨论 database truth source 与 markdown projection。 | report_stages_1_2_3.md: state persistence sections | M-GSD-042 |
| E7 | 文件讨论 auto mode、stuck loop 和 crash recovery。 | report_stages_1_2_3.md: automation/recovery sections | M-GSD-043 |
| E8 | 文件讨论 dynamic model routing、task complexity 和 token optimization。 | report_stages_1_2_3.md: routing sections | M-GSD-044 |
| E9 | 文件讨论 verification gate 和 completion criteria。 | report_stages_1_2_3.md: verification sections | M-GSD-045 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-037 | Goal Layer | PRODUCT_SPEC.md | v0_1 | 写清 iOS Harness 要解决的 agent 失败模式 |
| M-GSD-038 | Harness Maintenance Layer | ARCHITECTURE.md | v0_1 | 将 GSD2 runtime 概念映射为文档化控制层 |
| M-GSD-039 | Task Layer | TASKS.md | v0_1 | 引入 milestone/slice/task 字段或等价层级 |
| M-GSD-040 | Context Layer | CONTEXT_RULES.md | v0_1 | 要求每个任务 fresh context |
| M-GSD-041 | Context Layer | CONTEXT_INDEX.md | v0_1 | 为任务注入最小必要上下文 |
| M-GSD-042 | Memory / State Layer | STATE.md | v0_1 | 先用 Markdown 模拟真相源/投影分层 |
| M-GSD-043 | Feedback / Verification Layer | FAILURE_LOG.md | v0_5 | 记录卡住和恢复事件 |
| M-GSD-044 | Role / Review Layer | MODEL_ROUTING.md | v0_5 | 维护任务复杂度到模型策略 |
| M-GSD-045 | Feedback / Verification Layer | VERIFICATION_MATRIX.md | v0_1 | 要求完成证据 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 该文件定义 GSD2 迁移的核心概念词表 |
| v0_1 | yes | 任务层级、上下文规则和验证门需要立即迁移 |
| v0_5 | yes | 模型路由、失败恢复和状态投影可脚本化 |
| v1_0 | yes | 数据库真相源与 runtime 恢复可作为长期方向 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 三层任务模型是否完全适配 iOS app 开发 | 原机制来自 GSD2 通用 runtime | 在 iOS feature、bugfix、release 三类任务中试运行 |
| v0.1 是否需要数据库 | 文件强调 DB，但当前 harness 阶段可能过重 | 先用 Markdown 状态文件运行，再评估并发和恢复需求 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_001 | 综合报告的 Stage 1-3 对应内容 |
| F_GSD_007 | 细化任务状态、上下文和模型路由 |
| F_GSD_008 | 细化失败恢复、Git 和验证门 |
| F_GSD_009 | 架构专项深入 DB 和 runtime |

## 13. Clean Summary for Codex

这个文件是理解 GSD2 的入口卡。它给后续 iOS Harness 提供了核心词汇：milestone/slice/task、fresh session、context injection、database truth、markdown projection、auto mode、stuck recovery、dynamic model routing 和 verification gate。后续 Codex 做框架融合时，应把它当作概念索引，而不是完整实现说明；真正落地时再读取 F_GSD_007、F_GSD_008、F_GSD_009、F_GSD_010、F_GSD_011、F_GSD_012 中的专项机制。

