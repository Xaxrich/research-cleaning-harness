# Source Card: F_GSD_002 - GSD2深度研究_iOS_Harness迁移方案

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_002 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/GSD2深度研究_iOS_Harness迁移方案.docx |
| file_type | docx |
| topic | comprehensive GSD2 to iOS Harness migration report |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：以可交付文档形式复刻 GSD2 深度研究报告，并把 GSD2 的任务状态、上下文、模型路由、失败恢复和验证机制迁移到 iOS App Harness。

## 3. File Summary

- 该文件是 DOCX 版本的 GSD2 研究交付物，内容结构与综合迁移报告高度重合。
- 它以目录化方式组织 GSD2 的架构、任务模型、上下文策略、模型路由、失败恢复、Git 隔离和验证门。
- 文件强调 iOS Harness 不是复制 GSD2 runtime，而是迁移其工程控制机制。
- 报告把 GSD2 的数据库真相源、Markdown 投影、fresh session 和 per-task context 转换为 iOS agent 文档和脚本。
- 它给出 v0.1、v0.5、v1.0 的分层迁移判断。
- 对后续清洗的价值主要是提供一份“正式交付版”证据，可用于核对 Markdown 报告是否遗漏迁移项。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-011 | Deliverable-Grade Report Projection | 将研究结果整理为可交付文档，用目录和章节稳定承载架构结论。 | E1 | medium |
| M-GSD-012 | Runtime Mechanism Transfer Boundary | 明确 iOS Harness 应迁移 GSD2 的机制，而不是完整复制其数据库 runtime。 | E2 | medium |
| M-GSD-013 | End-to-End Harness Control Stack | 将状态、任务、上下文、模型、失败、Git、验证连成一条控制链。 | E3 | medium |
| M-GSD-014 | Versioned Migration Scope | 用 v0.1/v0.5/v1.0 区分文档化、脚本化和 runtime 化迁移范围。 | E4 | medium |
| M-GSD-015 | Evidence Cross-Check Source | 作为 DOCX 交付物保留另一份正式来源，供 Markdown source card 之间做一致性核对。 | E5 | low |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| report_drift | 通过正式文档版本保存完整目录和结论，降低零散 Markdown 报告被误读的风险。 | E1 |
| over_transfer | 明确区分机制迁移和 runtime 复制，避免为 iOS Harness 过早引入复杂数据库/调度系统。 | E2 |
| fragmented_harness_design | 将状态、任务、上下文、模型、失败和验证作为同一系统处理。 | E3 |
| scope_confusion | 用版本层级切分可立即落地与未来增强。 | E4 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 保留 DOCX 交付版 | 便于人工审阅和转交 | 让研究结论具备可交付形态，而不只停留在工作笔记 | DOCX 不利于脚本 diff 和自动抽取 |
| 用迁移边界替代照搬架构 | iOS Harness 不需要完整 GSD2 runtime | 防止研究成果变成过重系统设计 | 需要后续手工判断哪些 runtime 能力只保留为文档规则 |
| 将机制按版本落位 | 先跑通最小闭环 | 避免一次性构建超出当前阶段的 agent runtime | v0.1 只能获得部分自动化能力 |

## 7. 5 Why Analysis

### Mechanism: Runtime Mechanism Transfer Boundary

- Why 1: 因为 GSD2 是完整多 agent runtime，而当前目标是 iOS App Harness。
- Why 2: iOS Harness 当前更需要稳定的 agent 工作协议，而不是新的执行平台。
- Why 3: 如果复制 runtime，会增加数据库、调度、锁和恢复成本。
- Why 4: 这些成本会拖慢 v0.1 的可用交付。
- Why 5: 所以文档应把 GSD2 的原则压缩成文件结构、状态字段、任务规则和验证脚本。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | DOCX 转文本后呈现完整目录化报告结构。 | docx converted text: table of contents | M-GSD-011 |
| E2 | 报告围绕 iOS Harness 迁移方案组织，而非要求复刻 GSD2 产品。 | docx title and migration sections | M-GSD-012 |
| E3 | 章节覆盖 architecture、task state、context、model routing、failure recovery、git 和 verification。 | docx chapter outline | M-GSD-013 |
| E4 | 报告以 v0.1、v0.5、v1.0 方式组织迁移优先级。 | docx migration scope sections | M-GSD-014 |
| E5 | DOCX 与 Markdown 综合报告存在高重合，可作为交付形态核对源。 | comparison with F_GSD_001 during processing | M-GSD-015 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-011 | Harness Maintenance Layer | docs/research/gsd2_delivery_index.md | v0_5 | 记录 DOCX 与 Markdown source card 的对应关系 |
| M-GSD-012 | Goal Layer | AGENTS.md | v0_1 | 写入“迁移机制，不复制 runtime”的设计边界 |
| M-GSD-013 | Memory / State Layer | STATE.md | v0_1 | 将控制链拆成状态、任务、上下文、模型、失败、验证字段 |
| M-GSD-014 | Harness Maintenance Layer | ROADMAP.md | v0_1 | 用 v0.1/v0.5/v1.0 维护迁移范围 |
| M-GSD-015 | Harness Maintenance Layer | docs/research/source_crosscheck.md | v0_5 | 用交付版做报告一致性核对 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | DOCX 主要作为正式交付和核对源，机制应从 Markdown 卡片中去重后迁移 |
| v0_1 | yes | 保留迁移边界和版本范围 |
| v0_5 | yes | 建立交付物交叉核对索引 |
| v1_0 | no | DOCX 本身不构成 runtime 功能 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| DOCX 是否完全等同于 F_GSD_001 | 当前只做结构和重点内容比对，没有逐段 diff | 后续可用 docx 转文本后与 F_GSD_001 做规范化差异比较 |
| DOCX 中是否有 Markdown 版本没有的细节 | 文件格式不利于精确行号引用 | 在框架合成前运行转换文本差异审查 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_001 | 同一综合报告的 Markdown/文档形态高度重合 |
| F_GSD_004 | 覆盖迁移架构和 Superpowers 融合部分 |
| F_GSD_005 | 覆盖交付物、脚本和输出质量要求 |

## 13. Clean Summary for Codex

这个文件对 iOS Harness 的价值不是新增大量独立机制，而是作为 GSD2 研究的正式交付形态，帮助 Codex 核对“迁移边界、版本范围、控制链完整性”是否在 clean outputs 中被保留。后续开发时，Codex 应优先读取 Source Cards 和框架总结，不应直接依赖 DOCX；但在发现 Markdown 卡片之间有冲突时，可以把该 DOCX 作为交付级证据源回查。它提醒 iOS Harness 的核心不是照搬 GSD2 runtime，而是把 GSD2 的工程治理方法压缩为可维护的 agent 文件、任务协议和验证脚本。

