# Source Card: F_GSD_009 - research_architecture

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_009 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/research_architecture.md |
| file_type | markdown |
| topic | GSD2 architecture, runtime state, database schema, and iOS architecture lessons |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：深入拆解 GSD2 runtime 架构、SQLite 状态模型、自动推进管线和恢复机制，并提炼对 iOS Harness 架构的启发。

## 3. File Summary

- 文件分析 GSD2 的源码结构、`.gsd/` 运行态投影、SQLite 数据库和 orchestrator。
- 它解释 auto mode 状态转换、milestone/slice/task 关系、phase 行为和 dispatch pipeline。
- 文件详细列出 schema V28 的核心表：milestones、slices、tasks、verification_evidence、replan_history、quality_gates、workers、leases、unit_dispatches、command_queue、memories、embeddings、relations、audit/soft state。
- 它区分数据库真相源和 Markdown 投影。
- 它覆盖 crash recovery、CLI loader/headless、MCP 和 ADR 决策。
- 最后提炼 iOS Harness 架构洞察。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-065 | Runtime Architecture Map | 用源码结构、`.gsd/`、SQLite 和 orchestrator 描述 GSD2 运行架构。 | E1 | high |
| M-GSD-066 | Auto Mode State Transition | auto mode 以状态转换驱动任务推进。 | E2 | high |
| M-GSD-067 | Dispatch Pipeline | milestone/slice/task 经过 phase 和 dispatch 管线分配给 worker。 | E3 | high |
| M-GSD-068 | Schema-Backed Truth Source | schema V28 用多张表保存任务、验证、质量门、worker、lease、command 和 memory。 | E4 | high |
| M-GSD-069 | Verification Evidence Table | 验证证据是结构化状态的一部分，而不是日志附属品。 | E5 | high |
| M-GSD-070 | Worker Lease and Command Queue | 用 worker、lease 和 command_queue 支撑并发与恢复。 | E6 | high |
| M-GSD-071 | CLI/Headless/MCP Surfaces | GSD2 同时提供 CLI、headless 和 MCP 操作面。 | E7 | high |
| M-GSD-072 | ADR-Guided Architecture Decisions | 用 ADR 记录关键架构决策，降低机制漂移。 | E8 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| architecture_opacity | runtime architecture map 让执行路径可理解。 | E1 |
| lost_task_state | schema-backed truth source 保存结构化任务状态。 | E4 |
| unverifiable_state | verification_evidence 表将验证纳入状态系统。 | E5 |
| worker_crash | worker lease 和 command queue 支撑恢复。 | E6 |
| interface_fragmentation | CLI/headless/MCP 使同一 runtime 可被不同入口驱动。 | E7 |
| design_drift | ADR 记录关键决策。 | E8 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| SQLite 做真相源 | 可靠保存多 agent 状态 | 长任务和 crash recovery 需要事务化状态 | v0.1 实现成本较高 |
| Markdown 做投影 | 便于 agent 读取 | 模型不适合直接理解数据库内部结构 | 投影可能滞后 |
| worker lease | 管理并发 worker | 需要检测失联、重分配和恢复 | 增加调度复杂度 |

## 7. 5 Why Analysis

### Mechanism: Schema-Backed Truth Source

- Why 1: 因为 GSD2 需要管理多层任务和多个 worker。
- Why 2: Markdown 难以可靠表达 lease、command、evidence 和恢复历史。
- Why 3: 数据库 schema 可以强制结构化状态。
- Why 4: 结构化状态让 crash recovery 和自动推进可计算。
- Why 5: 所以 iOS Harness v1.0 可以考虑 runtime DB，但 v0.1 先用 Markdown 投影模拟关键字段。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件分析 source tree、`.gsd/` runtime projection、SQLite DB 和 orchestrator。 | research_architecture.md: architecture overview sections | M-GSD-065 |
| E2 | 文件讨论 auto mode state transitions。 | research_architecture.md: auto mode state transition section | M-GSD-066 |
| E3 | 文件讨论 milestone/slice/task、phase behavior 和 dispatch pipeline。 | research_architecture.md: dispatch pipeline sections | M-GSD-067 |
| E4 | 文件列出 schema V28 的核心表。 | research_architecture.md: schema V28 sections | M-GSD-068 |
| E5 | schema 中包含 verification_evidence。 | research_architecture.md: verification_evidence table section | M-GSD-069 |
| E6 | schema 中包含 workers、leases、unit_dispatches 和 command_queue。 | research_architecture.md: worker/lease/command sections | M-GSD-070 |
| E7 | 文件覆盖 CLI loader、headless 和 MCP。 | research_architecture.md: CLI/headless/MCP sections | M-GSD-071 |
| E8 | 文件引用 ADR 决策。 | research_architecture.md: ADR sections | M-GSD-072 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-065 | Harness Maintenance Layer | ARCHITECTURE.md | v0_1 | 画出 iOS Harness 控制面架构 |
| M-GSD-066 | Memory / State Layer | STATE.md | v0_5 | 将任务状态转换显式化 |
| M-GSD-067 | Task Layer | TASKS.md | v0_5 | 引入 dispatch/owner/review 状态 |
| M-GSD-068 | Memory / State Layer | data/harness_state.sqlite | v1_0 | 长期引入结构化真相源 |
| M-GSD-069 | Feedback / Verification Layer | output/data/verification_evidence.jsonl | v0_5 | 将验证证据结构化保存 |
| M-GSD-070 | Action / ACI Layer | scripts/agent/runtime/lease_check.py | v1_0 | 支撑并发任务和 worker 恢复 |
| M-GSD-071 | Action / ACI Layer | .mcp.json; scripts/agent/cli/ | v1_0 | 提供 CLI/MCP 操作面 |
| M-GSD-072 | Harness Maintenance Layer | DECISIONS.md | v0_1 | 记录架构取舍 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | 架构思想必须迁移，但数据库和 worker runtime 不应在 v0.1 全量实现 |
| v0_1 | yes | 架构图、决策记录和 Markdown 状态字段立即迁移 |
| v0_5 | yes | 结构化 JSONL 验证证据和状态转换脚本可实现 |
| v1_0 | yes | SQLite truth source、lease 和 command queue 是长期 runtime 方向 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| iOS Harness 是否需要多 worker lease | 当前目标可能主要是单 agent Codex 使用 | 观察是否存在并行 agent 修改冲突需求 |
| SQLite 是否过重 | GSD2 runtime 需求强于当前清洗 harness | 先用 JSONL/Markdown 运行，出现状态漂移后再升级 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_006 | 提供架构概念总览 |
| F_GSD_004 | 将架构映射为 iOS Harness 文件树 |
| F_GSD_011 | crash recovery 与 worker 恢复相关 |
| F_GSD_005 | 提供验证证据脚本化方向 |

## 13. Clean Summary for Codex

这个文件是 GSD2 runtime 架构的深挖证据。它提醒 iOS Harness 不应只写 agent prompt，还需要明确状态真相源、可读投影、验证证据、恢复记录和操作面。当前阶段建议只迁移轻量形态：`ARCHITECTURE.md`、`STATE.md`、`DECISIONS.md`、JSONL evidence；等到 v1.0 需要并发、恢复和 runtime 执行时，再考虑 SQLite、lease、command queue 和 MCP/CLI 操作面。

