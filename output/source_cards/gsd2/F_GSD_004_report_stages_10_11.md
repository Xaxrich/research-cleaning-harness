# Source Card: F_GSD_004 - report_stages_10_11

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_004 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/report_stages_10_11.md |
| file_type | markdown |
| topic | iOS Harness architecture migration and Superpowers-GSD2 combination |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把 GSD2 的机制具体落到 iOS Harness 文件架构，并定义它与 Superpowers 方法论如何组合、冲突如何处理、版本如何分层。

## 3. File Summary

- Stage 10 从设计目标、约束和 backward design 出发设计 iOS Harness。
- 文件给出目标文件树，覆盖 agent 文档、skills、脚本、MCP、CI 和 GitHub workflow。
- 它逐个说明 AGENTS、PRODUCT_SPEC、ARCHITECTURE、CONTEXT_INDEX、TASKS、STATE、MODEL_ROUTING、FAILURE_LOG、GIT_WORKFLOW、VERIFICATION_MATRIX、RELEASE_CHECKLIST 等文件的职责。
- Stage 11 分析 Superpowers 与 GSD2 的角色分工。
- 文件认为 Superpowers 更偏方法论和 skill，GSD2 更偏 runtime/state/context/verification。
- 它列出重叠、冲突和保留策略，并给出 v0.1/v0.5/v1.0 的组合方案。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-021 | Backward iOS Harness Design | 从 iOS 开发中的失败模式反推 Harness 文件和控制层。 | E1 | high |
| M-GSD-022 | Target File Tree as Architecture | 用完整文件树表达 Harness 架构，而不是只写概念说明。 | E2 | high |
| M-GSD-023 | Agent Document Responsibility Split | 为 AGENTS、SPEC、ARCHITECTURE、CONTEXT、TASKS、STATE 等文件分配清晰职责。 | E3 | high |
| M-GSD-024 | Model/Failure/Git/Verification Control Files | 将模型路由、失败日志、Git workflow 和验证矩阵拆成独立控制文件。 | E4 | high |
| M-GSD-025 | Skills and Scripts as Executable Surface | 把 `.agents/skills` 与 `scripts/agent` 作为方法论落地层。 | E5 | high |
| M-GSD-026 | Superpowers-GSD2 Role Split | 将 Superpowers 定位为方法论/skill，将 GSD2 定位为状态、上下文、路由和验证控制。 | E6 | high |
| M-GSD-027 | Conflict Resolution Policy | 对两套框架重叠和冲突部分做保留、改写或降级。 | E7 | medium |
| M-GSD-028 | Versioned Combination Strategy | 用 v0.1/v0.5/v1.0 定义最小、增强和完整组合形态。 | E8 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| abstract_harness_design | 通过目标文件树和文件职责把抽象机制落成具体资产。 | E2 |
| document_role_confusion | 每类文档有明确责任，减少 AGENTS/TASKS/STATE 混写。 | E3 |
| missing_control_surface | 模型、失败、Git、验证均有独立控制文件。 | E4 |
| methodology_runtime_conflict | 用角色分工处理 Superpowers 与 GSD2 的定位差异。 | E6 |
| over_complex_initial_version | 用版本策略限制 v0.1 的实现范围。 | E8 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 用目标文件树表达架构 | 让迁移方案可实施 | Harness 的真实接口就是 Codex 会读取和修改的文件 | 文件树可能早于实现，需要后续校正 |
| 分离控制文件 | 避免单个 AGENTS.md 过载 | 不同控制面需要不同更新频率和审查规则 | 增加文件数量 |
| Superpowers + GSD2 组合 | 两者优势互补 | 方法论解决“怎么做”，GSD2 解决“如何约束过程” | 冲突时必须明确优先级 |

## 7. 5 Why Analysis

### Mechanism: Agent Document Responsibility Split

- Why 1: 因为 iOS Harness 会被 Codex 逐文件读取。
- Why 2: 如果一个文件承载所有规则，模型容易遗漏或混淆。
- Why 3: 分层文件能让任务只注入当前需要的上下文。
- Why 4: 上下文缩小后，弱模型也更容易遵守约束。
- Why 5: 因此文件职责拆分本身就是 harness 的控制机制。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Stage 10 包含设计目标、约束和 backward design。 | report_stages_10_11.md: Stage 10 headings | M-GSD-021 |
| E2 | 文件列出完整 target file tree。 | report_stages_10_11.md: full target file tree section | M-GSD-022 |
| E3 | 文件逐项分析 AGENTS、PRODUCT_SPEC、ARCHITECTURE、CONTEXT_INDEX、TASKS、STATE。 | report_stages_10_11.md: file analysis sections | M-GSD-023 |
| E4 | 文件包含 MODEL_ROUTING、FAILURE_LOG、GIT_WORKFLOW、VERIFICATION_MATRIX、IOS_RELEASE_CHECKLIST。 | report_stages_10_11.md: control file sections | M-GSD-024 |
| E5 | 文件把 `.agents/skills`、`scripts/agent`、`.mcp.json`、workflow 纳入迁移架构。 | report_stages_10_11.md: skills/scripts/MCP/workflow sections | M-GSD-025 |
| E6 | Stage 11 分析 Superpowers 与 GSD2 的角色分工。 | report_stages_10_11.md: Stage 11 headings | M-GSD-026 |
| E7 | Stage 11 包含 overlap、conflict、keep/modify/drop 判断。 | report_stages_10_11.md: conflict sections | M-GSD-027 |
| E8 | Stage 11 给出 v0.1、v0.5、v1.0 组合方案。 | report_stages_10_11.md: versioned combination sections | M-GSD-028 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-021 | Goal Layer | PRODUCT_SPEC.md | v0_1 | 从 iOS 失败模式反推 harness 目标 |
| M-GSD-022 | Harness Maintenance Layer | docs/agent/FILE_PLACEMENT_MAP.md | v0_1 | 将目标文件树作为维护索引 |
| M-GSD-023 | Context Layer | CONTEXT_INDEX.md | v0_1 | 定义各 agent 文档的读取优先级和职责 |
| M-GSD-024 | Memory / State Layer | MODEL_ROUTING.md; FAILURE_LOG.md; GIT_WORKFLOW.md; VERIFICATION_MATRIX.md | v0_1 | 拆分关键控制面文件 |
| M-GSD-025 | Action / ACI Layer | scripts/agent/ | v0_5 | 将可执行检查脚本化 |
| M-GSD-026 | Role / Review Layer | AGENTS.md | v0_1 | 写入 Superpowers/GSD2 的组合职责 |
| M-GSD-027 | Risk / Release Layer | DECISIONS.md | v0_1 | 冲突处理写入决策记录 |
| M-GSD-028 | Harness Maintenance Layer | ROADMAP.md | v0_1 | 分版本规划组合能力 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 这是 GSD2 迁移到 iOS Harness 的文件架构核心 |
| v0_1 | yes | 文件职责、控制文件和组合边界应立即建立 |
| v0_5 | yes | skills/scripts 可进入半自动化 |
| v1_0 | yes | 可演进为 runtime 级状态和验证拦截 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 文件树是否适合当前 iOS 项目 | 源文件是迁移方案，不知道实际 repo 结构 | 在 iOS harness 实现前对照真实 Xcode 项目和 CI |
| Superpowers 与 GSD2 冲突优先级是否最终确定 | 文件提供策略但不是执行记录 | 框架合成阶段建立 conflict ledger |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_001 | 综合报告包含相同迁移主题 |
| F_GSD_003 | plan 中 Stage 3 对应该报告 |
| F_GSD_005 | 后续交付物和脚本实现细化 |
| F_SUP_001 | Superpowers 总览可用于角色分工对照 |

## 13. Clean Summary for Codex

这个文件是 GSD2 清洗中最直接可迁移到 iOS Harness 架构的材料。它把 GSD2 的状态、上下文、模型路由、失败恢复和验证思想落实到具体文件树，并明确 Superpowers 与 GSD2 的组合方式。后续 Codex 构建 iOS App Harness 时，应优先从这里抽取 `AGENTS.md`、`TASKS.md`、`STATE.md`、`CONTEXT_INDEX.md`、`MODEL_ROUTING.md`、`FAILURE_LOG.md`、`VERIFICATION_MATRIX.md` 和 `scripts/agent/` 的职责边界，再用 Superpowers 的方法论 skill 填充执行流程。

