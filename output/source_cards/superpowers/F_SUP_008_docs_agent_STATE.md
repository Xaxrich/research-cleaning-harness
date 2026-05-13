# Source Card: F_SUP_008 - STATE.md - 项目当前状态

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_008 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md |
| file_type | markdown |
| topic | STATE.md - 项目当前状态 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：定义 iOS App Harness 的可恢复项目状态快照，让所有助手在任务前后同步阶段、任务、技术状态、问题、发布状态和更新记录。

## 3. File Summary

- 文件要求所有助手在执行任务前后更新 STATE.md。
- 它用 YAML 元数据记录项目、时间、更新者、Flutter/iOS 版本和目标平台。
- 它用概览区记录项目阶段、进行中任务、待开始任务和最近完成任务。
- 它用技术状态记录架构方案、Firebase、Push、Swift 桥接、测试覆盖率、analyze/test/build 健康度。
- 它用依赖状态记录 Flutter dependencies、dev dependencies 和 iOS Pods。
- 它区分阻塞性问题和非阻塞性问题。
- 它记录版本、App Store Connect、TestFlight 发布状态。
- 它提供结构化更新记录模板，包含变更内容、影响文件、验证结果、状态变更和下一步。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-050 | Persistent Project State Snapshot | 用 STATE.md 持久化项目阶段、任务进度、技术健康和发布状态。 | E1, E2, E3 | high |
| M-SUP-051 | Structured Update Log | 每次更新写入时间、操作者、变更、影响文件、验证、状态变更和下一步。 | E8 | high |
| M-SUP-052 | Technical Health Dashboard | 用表格跟踪架构状态、测试覆盖、analyze/test/build 指标。 | E4 | high |
| M-SUP-053 | Issue Severity Split | 将已知问题拆成阻塞性和非阻塞性，明确根因、影响和负责人。 | E6 | medium |
| M-SUP-054 | Release State Tracking | 记录版本、App Store Connect 审核状态和 TestFlight 状态。 | E7 | medium |
| M-SUP-055 | Dependency State Registry | 记录 Flutter、dev dependencies 和 iOS Pods 版本。 | E5 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| state_loss | 将当前阶段、进行中任务、待办和最近完成写入文件。 | E2, E3 |
| stale_context | 要求任务前后更新，提供 last_updated 和 updated_by。 | E1, E2 |
| unverified_status_change | 更新记录必须包含验证结果。 | E8 |
| hidden_blocker | 阻塞性问题区要求记录严重级别、影响范围、根因、解决方案、负责人。 | E6 |
| release_risk | 发布状态区记录 App Store 审核和 TestFlight 状态。 | E7 |
| dependency_drift | 依赖状态区记录包和 Pod 版本。 | E5 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| Markdown + YAML | 人可读、机器可解析 | 弱模型和人类都能恢复上下文 | 需要格式纪律 |
| 技术健康表 | 快速看到项目质量指标 | 避免模型只看任务不看工程状态 | 指标需脚本更新才可靠 |
| 更新记录模板 | 统一任务后的状态写法 | 让后续会话能追踪为何变化 | 手工维护成本高 |
| 阻塞/非阻塞拆分 | 区分立即处理和延期 | 避免所有问题同等优先级 | 需要判断问题严重度 |

## 7. 5 Why Analysis

### Mechanism: Persistent Project State Snapshot

- Why 1: 为什么需要 STATE.md？因为长任务和多助手场景会丢失会话状态。
- Why 2: 为什么不能只靠聊天历史？因为上下文会压缩、遗忘或被无关内容污染。
- Why 3: 为什么要覆盖技术健康和发布状态？因为 iOS app 是否可交付不只取决于当前功能任务。
- Why 4: 为什么要写验证结果？因为状态变化没有验证证据就不可信。
- Why 5: 为什么对 iOS Harness 必须保留？因为 Flutter/Firebase/iOS 项目有构建、依赖、签名、审核等跨任务状态。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件开头说明记录实时状态，所有助手执行任务前后必须更新。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md:1-5 | M-SUP-050 |
| E2 | 元数据包含 project、created、last_updated、updated_by、Flutter/iOS 版本、目标平台。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md:9-21 | M-SUP-050 |
| E3 | 当前状态概览记录整体阶段、进行中、待开始、最近完成任务。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md:25-48 | M-SUP-050 |
| E4 | 技术状态记录架构模块和代码健康指标。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md:50-76 | M-SUP-052 |
| E5 | 依赖状态记录 Flutter dependencies、dev dependencies、iOS Pods。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md:78-92 | M-SUP-055 |
| E6 | 已知问题按阻塞性和非阻塞性分组。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md:96-112 | M-SUP-053 |
| E7 | 发布状态记录版本、App Store Connect 审核状态和 TestFlight。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md:116-126 | M-SUP-054 |
| E8 | 更新记录模板要求变更内容、影响文件、验证结果、状态变更、下一步建议。 | raw/Kimi_Agent_Superpowers 体系探究/docs/agent/STATE.md:130-167 | M-SUP-051 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Persistent Project State Snapshot | Memory / State Layer | docs/agent/STATE.md | v0_1 | Use as canonical project state file |
| Structured Update Log | Memory / State Layer | docs/agent/STATE.md | v0_1 | Append update records after each task |
| Technical Health Dashboard | Feedback / Verification Layer | docs/agent/STATE.md | v0_5 | Populate from validation scripts |
| Issue Severity Split | Risk / Release Layer | docs/agent/STATE.md | v0_1 | Record blockers and non-blockers separately |
| Release State Tracking | Risk / Release Layer | docs/agent/checklists/release-vX.Y.Z.md | v0_5 | Move detailed release tracking into checklist when needed |
| Dependency State Registry | Context Layer | docs/agent/STATE.md | v0_5 | Track key package/pod versions |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | Persistent state is core to weak-model and long-task reliability. |
| v0_1 | yes | Phase, tasks, blockers, update log, next step should exist immediately. |
| v0_5 | yes | Technical health, dependencies, release status can be populated after scripts exist. |
| v1_0 | partial | Script-generated STATE updates can be automated later. |
| no_transfer | yes | Do not preserve placeholders in final project state. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether all health metrics are needed in early harness | Some metrics require scripts and real project data. | Start minimal and add metrics when scripts exist. |
| Whether STATE should duplicate TASKS detail | File includes task summaries, while TASKS has full queue. | Keep STATE as snapshot and TASKS as full log. |
| Whether release state belongs in STATE or checklist | File includes release fields but release checklist may own details. | Decide during app-store-release synthesis. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_007 | AGENTS references STATE as required start context |
| F_SUP_009 | TASKS complements STATE with task queue/history |
| F_SUP_011 | app-store-release may populate release state |

## 13. Clean Summary for Codex

这份 STATE.md 是 iOS Harness 的记忆层模板。它的价值是让 Codex 不依赖聊天历史就能恢复项目阶段、当前任务、技术健康、依赖、问题和发布状态。v0.1 应保留最小字段：phase、current_task、completed_tasks、blockers、next、update log；v0.5 再补测试覆盖、Flutter analyze、build、依赖和发布状态。后续清洗和合成阶段应把 STATE 与 TASKS 区分清楚：STATE 是快照，TASKS 是完整任务队列与历史。
