# Source Card: F_SUP_009 - TASKS.md - 任务队列与执行历史

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_009 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md |
| file_type | markdown |
| topic | TASKS.md - 任务队列与执行历史 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：定义 iOS Harness 的任务状态机、任务模板、更新规则、分级分配和执行历史格式。

## 3. File Summary

- 文件追踪任务从创建到完成、失败或升级的完整生命周期。
- 它定义元数据，包括 total、completed、failed、escalated 任务计数。
- 它提供状态图：pending → in-progress → review → completed，以及 failed → escalated。
- 它定义 pending、in-progress、review、completed、failed、escalated、blocked、cancelled 的含义和允许操作。
- 它将活跃任务分为进行中、待开始、审核中、被阻塞。
- 它提供任务创建模板，包含 YAML 元数据、输入、预期产出、验收标准、执行记录、验证结果、关联文件。
- 它定义创建、开始、进度更新、完成、失败、升级的更新规则。
- 它提供任务分级速查和一个用户登录页面示例任务。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-056 | Task Lifecycle State Machine | 用 pending、in-progress、review、completed、failed、escalated、blocked、cancelled 管理任务生命周期。 | E2, E3 | high |
| M-SUP-057 | Structured Task Card | 每个任务包含 id、title、description、skill、assignee、dates、status、priority、effort、dependencies 等字段。 | E5 | high |
| M-SUP-058 | Acceptance And Verification Coupling | 任务模板要求验收标准和验证结果，完成时必须填写验证。 | E5, E8 | high |
| M-SUP-059 | Task Update Protocol | 创建、开始、进度、完成、失败、升级都有明确更新步骤。 | E6 | high |
| M-SUP-060 | Capability-based Assignment Guide | 按任务场景分配弱模型、强模型、人工，并标注审查和失败升级。 | E7 | high |
| M-SUP-061 | Execution History Log | 任务记录时间戳事件，保留执行过程。 | E5, E8 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| task_state_loss | 任务状态机和活跃/历史区使任务可恢复。 | E2, E4 |
| vague_task_scope | 结构化任务卡要求输入、产出、验收标准和关联文件。 | E5 |
| unverified_completion | 完成规则要求填写验证结果，模板绑定验收和验证。 | E5, E6 |
| repeated_failed_attempts | 失败规则要求记录失败原因、尝试修复，并决定重试/升级/终止。 | E6 |
| weak_model_overreach | 分级速查定义哪些任务给弱模型、强模型或人工。 | E7 |
| missing_task_history | 执行记录保存每个时间点事件。 | E8 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 状态机 | 任务生命周期清晰 | 弱模型能按状态迁移而非自由发挥 | 需要持续维护 |
| YAML 任务元数据 | 字段稳定 | 方便模型和脚本读取 | 纯 Markdown 编辑容易格式错 |
| 验收标准 + 验证结果 | 防止“做完就算” | 完成状态必须有证据 | 需要定义可执行验证命令 |
| 分级速查 | 快速分配执行者 | 控制弱模型任务边界 | 分级需要随项目调整 |

## 7. 5 Why Analysis

### Mechanism: Task Lifecycle State Machine

- Why 1: 为什么需要任务状态机？因为任务不只是待办项，还会失败、阻塞、审查和升级。
- Why 2: 为什么状态要有允许操作？因为模型需要知道当前状态下一步能做什么。
- Why 3: 为什么要有 review 和 escalated？因为弱模型输出不能直接等同完成，高风险或失败任务需要转交。
- Why 4: 为什么要记录执行历史？因为后续会话需要复盘已经尝试过什么。
- Why 5: 为什么对 iOS Harness 重要？因为移动端任务常涉及测试、构建、发布、人工确认，状态必须可追溯。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件开头说明追踪所有任务完整生命周期，助手开始前读、完成后更新。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md:1-5 | M-SUP-056 |
| E2 | 元数据记录 total/completed/failed/escalated 任务数。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md:8-19 | M-SUP-056 |
| E3 | 任务状态图显示 pending、in-progress、review、completed、failed、escalated 关系。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md:22-28 | M-SUP-056 |
| E4 | 状态定义表给出每个状态说明和允许操作。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md:29-42 | M-SUP-056 |
| E5 | 任务创建模板包含 YAML 字段、输入、预期产出、验收标准、执行记录、验证结果、关联文件。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md:80-124 | M-SUP-057, M-SUP-058 |
| E6 | 更新规则定义创建、开始、进度、完成、失败、升级时怎么更新。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md:126-170 | M-SUP-059 |
| E7 | 任务分级速查按场景分配弱模型、强模型、人工和审查/升级。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md:172-188 | M-SUP-060 |
| E8 | 示例任务展示执行记录、验证结果和关联文件。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/TASKS.md:190-252 | M-SUP-061 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Task Lifecycle State Machine | Task Layer | docs/agent/TASKS.md | v0_1 | Use as canonical task queue and status machine |
| Structured Task Card | Task Layer | docs/agent/TASKS.md | v0_1 | Require id, scope, inputs, outputs, acceptance, verification |
| Acceptance And Verification Coupling | Feedback / Verification Layer | docs/agent/TASKS.md | v0_1 | Link each task completion to validation evidence |
| Task Update Protocol | Memory / State Layer | docs/agent/TASKS.md | v0_1 | Define update procedure for every task transition |
| Capability-based Assignment Guide | Role / Review Layer | docs/agent/RISK_GATE.md | v0_1 | Move assignment matrix into risk gate |
| Execution History Log | Memory / State Layer | docs/agent/TASKS.md | v0_5 | Preserve timestamped task history |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | Task state machine is core to the harness execution model. |
| v0_1 | yes | Need task IDs, status, acceptance, verification, allowed transitions immediately. |
| v0_5 | yes | Add counters, richer execution histories, and assignment matrix. |
| v1_0 | partial | Automated task state validation can be added later. |
| no_transfer | yes | Do not keep example login task in final template except as documentation. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether task status names should match current research_cleaning_harness statuses | This raw file uses pending/in-progress/review, while current harness uses queued/source_card_done/reviewed. | Normalize during synthesis for research cleaning vs app development. |
| Whether metadata counters should be manually maintained | Counters can drift if edited manually. | Consider validator or generation script. |
| Whether one TASKS file scales to large projects | Long task history can become unwieldy. | Add archive policy in v0.5/v1.0. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_007 | AGENTS requires reading TASKS before starting work |
| F_SUP_008 | STATE summarizes task state while TASKS holds full lifecycle |
| F_SUP_004 | migration design defines task capability matrix |

## 13. Clean Summary for Codex

这份 TASKS.md 是 iOS Harness 的任务层核心模板。它把任务从普通待办列表提升为有状态、有验收、有验证、有升级路径的执行资产。对当前研究清洗 Harness 来说，它证明了“一文件一任务”和“完成后 review”的结构是合理的；对后续 iOS App Harness 来说，v0.1 应保留任务状态机、结构化任务卡、验收标准和验证结果，v0.5 再加入执行历史、计数和分配矩阵。最终 synthesis 时要处理状态名差异，避免 research cleaning 和 app development 混用状态字段。
