# Source Card: F_GSD_001 - GSD2 技术报告：阶段 1-3

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_001 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md |
| file_type | markdown |
| topic | GSD2 技术报告：阶段 1-3 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 GSD2 定义为长任务 agent runtime，用数据库真相源、三层任务分解、fresh session、自动调度、失败恢复、动态路由和验证门禁支撑 iOS Harness 的可恢复执行。

## 3. File Summary

- 文件以 GSD2 v2.82.0 为基准，目标是评估其机制对 Flutter + Firebase iOS Harness 的迁移价值。
- 它把 GSD2 的底层问题定义为 Context Rot 和状态不可控。
- 它区分 Superpowers 与 GSD2：前者约束 task 内的软件工程纪律，后者约束 task 间的执行环境。
- 它主张 iOS Harness 不应只是 AGENTS/CLAUDE 静态规则，而应是动态运行时系统。
- 它将工作分解成 milestone、slice、task，并给出 iOS App Store 版本、端到端功能、上下文窗口级任务的映射。
- 它强调每个 task 使用 fresh session，并通过数据库与 summary 传递跨任务状态。
- 它描述数据库真相源、Markdown 投影、auto mode dispatch loop、stuck detection、crash recovery、dynamic routing、verification gate 等机制。
- 它也明确 GSD2 不适合替代代码库理解、实时 hot reload、复杂 UI 审美、深度 Xcode 操作和 App Store 沟通。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-001 | Database-backed Runtime State | 用 SQLite/Firestore 作为唯一真相源，替代对话历史和模型记忆。 | E2, E17 | high |
| M-GSD-002 | Milestone Slice Task Hierarchy | 用 milestone→slice→task 约束长任务粒度，让每个 task 能放进一个上下文窗口。 | E6, E11, E12, E13 | high |
| M-GSD-003 | Fresh Session Execution | 每个 task 创建零历史 session，并从数据库重建最小上下文。 | E7, E14, E15 | high |
| M-GSD-004 | Orchestrator-controlled Context Injection | 由 orchestrator 预构建 prompt，按 unit type 与 token profile 注入必要上下文。 | E4, E16 | high |
| M-GSD-005 | Auto Mode Dispatch Loop | 用状态机自动派生下一个 unit、分类复杂度、路由模型、构建 prompt、执行并持久化结果。 | E5, E19 | high |
| M-GSD-006 | Stuck Loop Detection | 通过跨 session 的滑动窗口和重试上限检测重复失败，避免 doom loop。 | E20 | high |
| M-GSD-007 | Crash Recovery With Session Forensics | 用 lock、持久化状态、session logs 和自动重启恢复中断的工作单元。 | E21 | high |
| M-GSD-008 | Dynamic Model Routing | 按任务复杂度、能力评分、预算压力和历史失败率选择 Light/Standard/Heavy 模型。 | E22 | high |
| M-GSD-009 | Verification Gate And Completion Criteria | 用 must-haves、验证命令、退出码证据和完成标准阻止未验证任务 closeout。 | E23, E24 | high |
| M-GSD-010 | Markdown Projection | 将数据库状态渲染成 STATE/ROADMAP/DECISIONS 等人类可读投影，但不作为运行时真相源。 | E18 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| context_rot | Fresh session、context reset 和数据库 summary 避免长对话历史累积。 | E2, E7, E14, E15 |
| state_loss | 数据库真相源和 Markdown 投影分离让状态可恢复、可审计。 | E17, E18 |
| vague_large_task | milestone/slice/task 约束把大目标拆成上下文窗口级任务。 | E6, E11, E12, E13 |
| context_pollution | orchestrator 控制注入内容，明确排除无关代码、生成代码和第三方库。 | E16 |
| stuck_loop | stuck detector 对重复派发、重复错误、产物缺失设置停止条件。 | E20 |
| crash_progress_loss | active session/lock、session forensics 和数据库状态用于崩溃恢复。 | E21 |
| model_cost_overrun | dynamic routing 与 token profile 用低成本模型处理简单任务。 | E22 |
| weak_model_overreach | complexity classification 和 escalation chain 限制弱模型任务边界。 | E8, E22 |
| fake_verification | verification gate 以命令退出码和 evidence 表替代 agent 自述。 | E23, E24 |
| wrong_tool_for_job | 文件明确 GSD2 不适合 UI 审美、热重载、深度原生平台和 App Store 沟通。 | E9 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 从 prompt 变成 runtime | prompt 无法持久化状态、恢复崩溃或检测 stuck | 长任务需要可恢复作业系统，而不是一次性聊天 | 实现成本明显高于静态规则文件 |
| 数据库是真相源 | 状态需要事务、索引、并发和查询 | 模型记忆和 Markdown 都不可靠 | 需要维护 schema、迁移和投影 |
| 每 task fresh session | 避免历史工具输出和失败尝试污染 | 结构化 summary 的信噪比高于完整对话历史 | 每次都要重建上下文包 |
| orchestrator 注入上下文 | LLM 自主读文件会读多、读少、读错 | runtime 更适合利用任务依赖和元数据选择上下文 | 需要准确的 key_files、summaries 和 profile 策略 |
| 动态模型路由 | 成本与能力需要匹配 | 大量任务不需要最强模型，失败可升级 | 分类器初期可能误判，需要历史校准 |
| 验证门禁 | 不信任 agent 的完成自述 | 编译器、测试和命令退出码是更可靠证据 | 机械验证无法覆盖审美和政策判断 |

## 7. 5 Why Analysis

### Mechanism: Database-backed Runtime State

- Why 1: 为什么需要数据库真相源？因为长任务状态不能可靠保存在对话历史里。
- Why 2: 为什么对话历史不可靠？因为 Context Rot 会让模型遗忘目标、混入过时错误尝试并降低注意力权重。
- Why 3: 为什么 Markdown 不足够？因为 Markdown 缺少事务、索引和并发控制，且直接编辑会造成 drift。
- Why 4: 为什么 iOS Harness 要映射到 Firestore？因为目标 harness 需要跨设备、可视化、可恢复的云端状态。
- Why 5: 为什么这比静态 AGENTS 更关键？因为它让弱模型只消费当前 task 的结构化上下文，而不是在长上下文里自行找状态。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件说明报告性质、资料来源、版本基准和迁移研究目的。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:1-6 | metadata |
| E2 | 文件把核心问题定义为 Context Rot 和状态不可控，并提出 fresh session、SQLite 真相源、状态机推进。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:16 | M-GSD-001 |
| E3 | 文件区分 Superpowers 和 GSD2：前者是工程纪律，后者是长任务执行基础设施。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:17 | framework relation |
| E4 | 文件说明 GSD2 是动态运行时系统，按任务类型和 token profile 动态注入上下文。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:18 | M-GSD-004 |
| E5 | 文件解释 prompt 无法解决状态持久化、stuck loop、模型路由和 crash recovery，因此需要 CLI/runtime/harness。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:19 | M-GSD-005 |
| E6 | 文件定义 milestone、slice、task 的层级和上下文窗口约束，并映射到 App Store 版本、端到端功能和独立工作单元。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:20 | M-GSD-002 |
| E7 | 文件强调每个 task 创建全新 LLM 调用上下文，从 Firestore 读取当前 task、最近 summary 和架构摘要。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:21 | M-GSD-003 |
| E8 | 文件列出 GSD2 适合 iOS Harness 的问题：长任务分解、弱模型参与、失败恢复、验证门禁、状态可视化和成本控制。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:22 | transfer |
| E9 | 文件列出 GSD2 不适合代码库自动理解、实时 hot reload、复杂 UI 视觉调优、深度 iOS 工具链和 App Store 沟通。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:23 | no_transfer |
| E10 | 关键位置表把 runtime/orchestration、数据库、headless、worktree、routing、verification 等列为核心结构。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:81-94 | architecture |
| E11 | milestone 代表可发布版本，含状态生命周期、依赖、验证和渐进式规划，并映射到 Firestore milestones。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:114-165 | M-GSD-002 |
| E12 | slice 代表可演示垂直能力，包含 1-7 个 tasks、依赖、sketch 和 UAT 输出，并映射到 feature slice。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:169-219 | M-GSD-002 |
| E13 | task 是上下文窗口大小的工作单元，最多 3 个文件、3 个步骤，并有 must-haves 与验证命令。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:223-275 | M-GSD-002 |
| E14 | fresh session 机制要求每个 unit 零历史执行，并从数据库预注入 task/slice/summaries。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:279-333 | M-GSD-003 |
| E15 | context reset 明确排除完整对话历史、失败尝试、过时代码和无关文件，以 summary 和数据库替代。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:337-392 | M-GSD-003 |
| E16 | context injection 由 auto-prompts 按 unit type、token profile、P0-P3 优先级预构建 prompt。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:396-451 | M-GSD-004 |
| E17 | database as source of truth 说明 SQLite 是唯一运行时真相源，Markdown 是投影，并映射到 Firestore collections。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:565-620 | M-GSD-001 |
| E18 | markdown projection 将数据库状态渲染为 STATE/ROADMAP 等文件，但不反向覆盖运行时状态。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:624-678 | M-GSD-010 |
| E19 | auto mode 定义 13 步 dispatch pipeline、状态转换、headless mode、timeout 和 gate evaluation。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:682-741 | M-GSD-005 |
| E20 | stuck loop detection 使用 Level 1/Level 2、滑动窗口、跨 session 状态和 cap=2 retry。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:745-796 | M-GSD-006 |
| E21 | crash recovery 使用 auto.lock、stale worker、session forensics、DB-backed state 和 headless auto-restart。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:800-852 | M-GSD-007 |
| E22 | dynamic model routing 使用启发式复杂度、unit type 默认层级、能力评分、预算压力、失败升级和自适应学习。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:856-919 | M-GSD-008 |
| E23 | verification gate 以 static checks、commands、must-haves、禁用危险 shell 组合、auto-fix retry 和 evidence 表作为门禁。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:1041-1103 | M-GSD-009 |
| E24 | completion criteria 规定 task/slice/milestone 的机械可验证完成标准和 iOS 专用完成标准。 | raw/Kimi_Agent_多 Agent GSD2/GSD2_深度研究_iOS_Harness_迁移报告.md:1107-1160 | M-GSD-009 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Database-backed Runtime State | Memory / State Layer | docs/agent/STATE_SCHEMA.md | v0_5 | Map GSD2 SQLite schema concepts to Firestore collections and local cache |
| Milestone Slice Task Hierarchy | Task Layer | docs/agent/TASKS.md | v0_1 | Add milestone/slice/task identifiers, max files and must-haves to task records |
| Fresh Session Execution | Context Layer | docs/agent/CONTEXT_RULES.md | v0_1 | Require each task to be executed from a rebuilt context package, not accumulated chat |
| Orchestrator-controlled Context Injection | Context Layer | docs/agent/CONTEXT_RULES.md | v0_5 | Define P0/P1/P2/P3 context tiers and file injection limits |
| Auto Mode Dispatch Loop | Action / ACI Layer | docs/agent/AUTO_MODE.md | v1_0 | Specify runtime dispatch stages before building automation |
| Stuck Loop Detection | Risk / Release Layer | docs/agent/ESCALATION_RULES.md | v0_5 | Add repeated failure and repeated file-change thresholds |
| Crash Recovery With Session Forensics | Memory / State Layer | docs/agent/RECOVERY.md | v0_5 | Define active session, heartbeat and recovery briefing records |
| Dynamic Model Routing | Role / Review Layer | docs/agent/MODEL_ROUTING.md | v0_5 | Add tier, complexity classifier and escalation chain |
| Verification Gate And Completion Criteria | Feedback / Verification Layer | docs/agent/VERIFICATION_MATRIX.md | v0_1 | Require must-haves and command evidence before completion |
| Markdown Projection | Memory / State Layer | docs/agent/STATE.md | v0_1 | Treat markdown as human-readable projection, not truth source |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | The file provides core runtime mechanisms missing from a pure prompt or skill harness. |
| v0_1 | yes | Milestone/slice/task, fresh context rules, verification matrix, markdown projection semantics can be adopted as docs immediately. |
| v0_5 | yes | Context tiers, model routing, stuck detection and recovery records need stronger templates/scripts. |
| v1_0 | yes | Auto mode runtime, Firestore truth source, background dispatch and automated recovery are mature runtime features. |
| no_transfer | yes | Do not use GSD2 as repo-map replacement, visual UI judge, hot reload loop, Xcode operator or App Store policy decision maker. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| File contains claims sourced from several GSD2 docs but this Source Card has not independently checked those upstream files | This task is single-file extraction only. | Process later GSD2 raw files and compare mechanism evidence. |
| Some line 87 stuck detector path is explicitly marked inferred in the source | The file says `auto-stuck-detection.ts` is inferred. | Verify against `research_failure_recovery.md` or source repository notes in later cards. |
| Firestore replacement may overfit the user's intended iOS architecture | File proposes Firestore, but actual iOS Harness runtime may choose local-first storage. | Resolve during iOS mapping synthesis after other frameworks. |
| v1_0 auto mode may be too heavy before v0.1 docs prove useful | Runtime automation requires state backend, dispatcher, LLM API and safety gates. | Keep v0.1/v0.5 lightweight until GSD2 framework summary is reviewed. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_001-F_SUP_014 | Superpowers provides task-internal engineering discipline that this file positions as complementary to GSD2 orchestration |
| F_GSD_003 | expected plan source for GSD2 research scope |
| F_GSD_009 | expected deeper architecture source for auto mode and runtime components |
| F_GSD_010 | expected deeper context management source |
| F_GSD_011 | expected deeper failure recovery and stuck detection source |
| F_GSD_012 | expected deeper dynamic model routing source |

## 13. Clean Summary for Codex

这份文件对 iOS Harness 的价值很高：它把 GSD2 的核心定位从“更好的提示词”转成“可恢复的长任务运行时”。对后续设计最重要的迁移点是：用数据库/Firestore 作为状态真相源；把工作拆成 milestone、slice、task；每个 task 用 fresh session 和受控上下文包执行；用 verification gate 阻止虚假完成；用 dynamic routing 控制弱模型边界和成本；用 stuck/crash recovery 防止长任务失控。它也给出明确边界：GSD2 不替代 repo map、UI 审美判断、hot reload、Xcode 深度操作或 App Store 政策判断。
