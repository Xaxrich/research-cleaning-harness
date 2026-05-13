# Source Card: F_SUP_007 - AGENTS.md - iOS App 项目助手入口

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_007 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md |
| file_type | markdown |
| topic | AGENTS.md - iOS App 项目助手入口 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：为 iOS App Harness 定义 AI 助手进入项目时必须读取的入口、行为契约、skill 导航、文档导航、验证脚本和任务开始清单。

## 3. File Summary

- 文件声明 AGENTS.md 是 AI 助手在项目中应读取的第一个文件。
- 它记录项目基本信息模板，包括 Flutter、Firebase、Swift、iOS 版本等。
- 它定义助手必须读取 Skill、同步状态、验证完成声明、失败两次升级。
- 它禁止跳过上下文、跳过测试、未验证完成声明、随意修改 skills。
- 它列出 10 个移动专用 skill 的触发条件和适用模型。
- 它区分弱模型和强模型可以执行的任务边界。
- 它导航到 STATE、TASKS、specs、plans、decisions、checklists。
- 它列出验证脚本命令，并提供任务开始检查清单。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-043 | Project Entry Contract | 要求 AI 助手每次从 AGENTS.md 进入并刷新上下文。 | E1 | high |
| M-SUP-044 | Assistant Behavior Contract | 明确读取 skill、同步状态、验证优先和失败升级四条必须遵守规则。 | E2 | high |
| M-SUP-045 | Skill Navigation Table | 把移动专用 skills、触发条件和模型适用性集中放在入口文件。 | E3 | high |
| M-SUP-046 | Model Capability Routing | 弱模型做执行/检查，强模型做架构/需求/复杂设计。 | E4 | high |
| M-SUP-047 | Document Navigation Index | 将状态、任务、规格、计划、ADR、检查清单的路径集中暴露。 | E5 | high |
| M-SUP-048 | Verification Command Index | 在入口文件列出验证脚本命令，减少完成前验证路径搜索。 | E6 | medium |
| M-SUP-049 | Task Start Checklist | 每次任务开始时检查入口、状态、skill、任务记录和结束更新。 | E7 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| missing_context_bootstrap | 要求 AGENTS.md 是第一个读取文件，并在新任务前重读。 | E1 |
| skipped_skill | 任务开始前检查 `.agents/skills`，有适用 skill 必须读取。 | E2, E7 |
| state_drift | 任务前读 STATE，完成后更新 STATE。 | E2, E5, E7 |
| false_completion_claim | 完成声明必须附带验证证据。 | E2, E6 |
| weak_model_overreach | 弱模型遇到架构、需求澄清、复杂 Swift 时升级强模型。 | E4 |
| wrong_file_lookup | 文档导航和脚本索引集中列出路径。 | E5, E6 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| AGENTS 作为第一入口 | 所有助手先读同一文件 | 建立最低共同上下文和行为契约 | 需要持续保持摘要不过期 |
| Skill 导航表 | 快速定位触发条件 | 弱模型不必自行搜索全部 skill | 表格过期会误导 |
| 模型能力分区 | 明确弱/强模型边界 | 防止弱模型处理高风险决策 | 需要准确判断当前模型等级 |
| 验证脚本索引 | 完成前知道跑什么命令 | 将验证文化落到可执行命令 | 脚本本身必须存在并可运行 |

## 7. 5 Why Analysis

### Mechanism: Project Entry Contract

- Why 1: 为什么需要 AGENTS.md？因为模型需要一个统一入口来获得项目规则。
- Why 2: 为什么每次任务前重读？因为状态、任务和约束可能变化。
- Why 3: 为什么入口要包含 skill 导航？因为不检查 skill 会导致流程绕过。
- Why 4: 为什么入口要包含验证脚本？因为完成声明需要直接可执行的证据路径。
- Why 5: 为什么这对 iOS Harness 重要？因为移动端任务风险差异大，必须在入口处就限制执行者边界。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件开头声明 AI 助手应首先读取 AGENTS.md，并在新任务前重读。 | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md:1-5 | M-SUP-043 |
| E2 | 助手行为契约要求读取 skill、同步状态、验证优先、失败升级，并列出禁止事项。 | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md:19-34 | M-SUP-044 |
| E3 | 可用 Skill 导航表列出 10 个 skill、触发条件和适用模型。 | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md:35-59 | M-SUP-045 |
| E4 | 文件区分弱模型和强模型可执行范围及升级条件。 | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md:60-67 | M-SUP-046 |
| E5 | 项目文档导航列出 STATE、TASKS、specs、plans、decisions、checklists。 | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md:68-75 | M-SUP-047 |
| E6 | 验证脚本区列出 Flutter build、tests、pod、Firebase、App Store、integration test 命令。 | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md:76-93 | M-SUP-048 |
| E7 | 任务开始检查清单要求读 AGENTS、STATE、检查 skill、记录 TASKS、完成后更新状态。 | raw/Kimi_Agent_Superpowers 体系探究/AGENTS.md:106-113 | M-SUP-049 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Project Entry Contract | Goal Layer | AGENTS.md | v0_1 | Use as canonical assistant entry file |
| Assistant Behavior Contract | Goal Layer | AGENTS.md | v0_1 | Keep concise must/must-not rules |
| Skill Navigation Table | Context Layer | AGENTS.md | v0_1 | Embed current skill list and triggers |
| Model Capability Routing | Role / Review Layer | docs/agent/RISK_GATE.md | v0_1 | Move detailed weak/strong/human routing into risk gate |
| Document Navigation Index | Context Layer | AGENTS.md | v0_1 | Link to state/task/spec/plan/ADR/checklist paths |
| Verification Command Index | Feedback / Verification Layer | AGENTS.md | v0_1 | List validation scripts until dedicated docs exist |
| Task Start Checklist | Task Layer | docs/agent/TASKS.md | v0_1 | Turn checklist into task preflight requirements |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | This is a concrete AGENTS.md template for iOS Harness. |
| v0_1 | yes | Entry contract, skill navigation, state/task links, and verification commands are immediate. |
| v0_5 | yes | Split detailed routing into RISK_GATE and verification docs later. |
| v1_0 | partial | Dynamic status summary generation could be automated later. |
| no_transfer | yes | Do not keep placeholder project values in final app harness. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether project stack placeholders match final app | File uses `<YOUR_APP_NAME>` and example versions. | Fill from actual project before app harness use. |
| Whether `/scripts/agent/*.sh` exist in target project | File lists commands but this source folder only contains templates/reports. | Generate scripts in implementation phase. |
| Whether weak/strong model labels should mention specific model names | Model availability may change. | Keep roles capability-based in final version. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_004 | migration design defines AGENTS.md role |
| F_SUP_008 | STATE template referenced by AGENTS |
| F_SUP_009 | TASKS template referenced by AGENTS |
| F_SUP_011 | app-store-release skill referenced |
| F_SUP_012 | mobile-tdd skill referenced |
| F_SUP_013 | root-cause-debugging skill referenced |

## 13. Clean Summary for Codex

这份 AGENTS.md 是后续 iOS Harness 的入口模板。它应进入 v0.1，因为它能把项目身份、助手行为、skill 导航、状态文件、任务队列和验证脚本集中给 Codex。使用时要把占位符替换成真实项目参数，并把详细弱/强模型路由迁移到 `docs/agent/RISK_GATE.md`，避免 AGENTS 过长。清洗 Harness 自身也可借鉴它的任务开始检查清单：先读入口、再读状态、再检查 skill、记录任务、完成后更新状态。
