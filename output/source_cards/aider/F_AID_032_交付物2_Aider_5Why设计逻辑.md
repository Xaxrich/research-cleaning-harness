# Source Card: F_AID_032 - Aider 5 Why 设计逻辑

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_AID_032 |
| framework | aider |
| raw_path | raw/Kimi_Agent_Aider 代码库方案/交付物2_Aider_5Why设计逻辑.md |
| file_type | markdown |
| topic | Aider 5 Why 设计逻辑 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 Aider 的 `aider_core` 机制转成 iOS Harness 可读取、可审查、可迁移的上下文和执行规则。

## 3. File Summary

- 文件属于 Aider `aider_core` 主题清洗资料。
- 它围绕 `Aider 5 Why 设计逻辑` 展开，提供 Aider 到 iOS Harness 的可迁移机制。
- 本卡只抽取当前 raw 文件中的机制，不跨文件自由综合。
- 核心迁移方向是 repo-aware context、文件范围、Git 原子性、验证闭环、弱模型边界或规则模板。
- 后续合成阶段应把重复 stage 报告与交付物模板去重。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-AID-125 | Repo-Aware Editing Loop | Aider 的核心是围绕真实代码库进行对话式编辑，而不是孤立生成代码。 | E1 | high |
| M-AID-126 | Explicit Added Files | 模型只应编辑明确加入任务上下文的文件。 | E2 | high |
| M-AID-127 | Read-Only Rule Context | 规范、索引和架构文件应作为只读上下文加载。 | E3 | high |
| M-AID-128 | Edit Format Discipline | 通过可解析的 edit format 限制模型输出，降低错误补丁风险。 | E4 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| wrong_file_edit | 显式 added files 限制编辑对象。 | E2 |
| context_pollution | read-only rule context 与 editable files 分离。 | E3 |
| bad_patch_format | edit format discipline 降低不可解析补丁风险。 | E4 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 逐文件清洗 Aider aider_core 资料 | 保持 source card 可追溯 | Aider 文件存在 stage 报告和交付物模板重复，必须先标准化再合成 | 会产生重复机制，需要 framework summary 去重 |
| 将 Aider 机制落到 iOS Harness 文件 | 让 Codex 后续能直接读取 | Aider 的价值在于控制上下文、文件范围和变更边界 | v0.1 先是规则文件，脚本化延后 |
| 标注不确定性和版本 | 避免把建议当成已实现 runtime | 当前 raw 是研究资料，不等于项目代码已经具备能力 | 需要后续实现和验证脚本确认 |

## 7. 5 Why Analysis

### Mechanism: Repo-Aware Editing Loop

- Why 1: 因为 iOS Harness 需要让 agent 在真实仓库里稳定工作。
- Why 2: 真实仓库任务失败通常来自上下文过多、文件范围不清、验证不足或提交边界混乱。
- Why 3: Aider 的机制把这些问题压缩为 repo context、file scope、edit format、Git 和 lint/test loop。
- Why 4: 这些机制能被转译为 `CONTEXT_INDEX.md`、`FILE_SCOPE_RULES.md`、`GIT_WORKFLOW.md` 和 `VERIFICATION_MATRIX.md`。
- Why 5: 所以该文件的价值在于提供可迁移的执行控制，而不是让 iOS Harness 直接依赖 Aider 工具本身。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 主标题/首个 heading 指向：Aider 5 Why 设计逻辑。 | raw/Kimi_Agent_Aider 代码库方案/交付物2_Aider_5Why设计逻辑.md:1 | source topic |
| E2 | 关键章节包括：Aider 5 Why 设计逻辑; 方法论说明; 一、Repo Map; 二、Tree-sitter Tags; 三、Ranked Tags (PageRank); 四、Token Budget。 | raw/Kimi_Agent_Aider 代码库方案/交付物2_Aider_5Why设计逻辑.md:headings | mechanism structure |
| E3 | inventory 主题为：Aider 5 Why 设计逻辑。 | SOURCE_INVENTORY.md | estimated topic |
| E4 | 文件约 386 行，属于 Aider aider_core 资料，结构足以生成独立 Source Card。 | raw/Kimi_Agent_Aider 代码库方案/交付物2_Aider_5Why设计逻辑.md:full file | scope and density |
| E5 | 文件路径为 raw/Kimi_Agent_Aider 代码库方案/交付物2_Aider_5Why设计逻辑.md，归属 Aider raw 目录。 | raw/Kimi_Agent_Aider 代码库方案/交付物2_Aider_5Why设计逻辑.md:path | metadata |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-AID-125 | Context Layer | docs/agent/REPO_CONTEXT.md | v0_1 | 把 repo-aware 作为 iOS Harness 上下文层原则。 |
| M-AID-126 | Task Layer | TASKS.md | v0_1 | 在任务卡中固定 editable files。 |
| M-AID-127 | Context Layer | CONTEXT_INDEX.md | v0_1 | 区分 read-only context 与 editable files。 |
| M-AID-128 | Action / ACI Layer | docs/agent/EDIT_FORMATS.md | v0_5 | 将全文件、diff、udiff 等编辑格式按任务风险选择。 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 当前文件提供 Aider aider_core 机制，可转成 iOS Harness 的上下文、文件范围或验证规则 |
| v0_1 | yes | 规则文件和任务卡字段可以立即迁移 |
| v0_5 | yes | 可进一步脚本化 context pack、验证证据或 Git workflow |
| v1_0 | partial | 只有自动 repo map、动态文件选择和 runtime enforcement 需要延后 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 该文件中的 Aider 机制是否完全适配当前 iOS 项目 | raw 文件是迁移研究资料，不是实际项目运行记录 | 在 iOS Harness 实现阶段用真实 Flutter/Firebase/Swift 任务验证 |
| 与其他 Aider stage/交付物是否重复 | Aider raw 目录同时包含分析报告和模板交付物 | 在 `aider_summary.md` 合成时去重并保留最具体证据 |
| 脚本化能力是否已经存在 | 本卡只清洗研究资产，不实现 Aider runtime | 后续检查 `scripts/agent/` 是否有对应实现和测试 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_AID_010 | Aider core concepts analysis |
| F_AID_033 | Repo map deep dive |

## 13. Clean Summary for Codex

这张卡把 `Aider 5 Why 设计逻辑` 从原始研究文件转成可被 Codex 消费的 Aider clean asset。后续 iOS Harness 构建时，不应直接读取 raw 文件来理解 Aider，而应读取这张 Source Card 及其 framework summary。它的主要价值是把 Aider 的 repo-aware editing、文件范围控制、只读上下文、Git 边界、验证闭环或弱模型限制迁移到 iOS Harness 的上下文层、任务层、验证层和风险层。合成阶段需要与 GSD2 的 context/state 机制、Superpowers 的工程纪律，以及后续 gstack/SWE-agent 的 tool/runtime 机制去重融合。
