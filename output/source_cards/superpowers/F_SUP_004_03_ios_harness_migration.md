# Source Card: F_SUP_004 - iOS App Harness: Superpowers 框架迁移设计

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_004 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md |
| file_type | markdown |
| topic | iOS App Harness: Superpowers 框架迁移设计 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把 Superpowers 的通用工程纪律改写成弱模型兼容的 Flutter/Firebase/Swift iOS Harness 文件结构、skills、验证脚本和任务分级体系。

## 3. File Summary

- 文件明确目标技术栈为 Flutter + Firebase + Swift iOS，目标模型包含弱模型 Composer2 和强模型 Claude 4 Sonnet。
- 它保留 skills 自动触发、移动端 TDD、系统化调试和完成前验证。
- 它移除 subagent 驱动、并行代理调度，并简化 Git Worktree 和双阶段 review。
- 它给出完整目标目录：`AGENTS.md`、`.agents/skills/`、`docs/agent/`、`scripts/agent/`、`.continue/`、`.mcp.json`、GitHub workflows。
- 它定义 10 个移动专用 skills，以及各自触发条件、输入输出、升级路径。
- 它定义 `docs/agent` 活文档体系和脚本规范。
- 它提供任务分级矩阵，明确哪些任务弱模型可做、哪些需要强模型或人工确认。
- 它设计多工具兼容、MCP 配置、实施路径和风险缓解。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-022 | Weak-model Lightweight Migration | 对强模型依赖机制做保留、简化、移除三类处理。 | E1, E2 | high |
| M-SUP-023 | iOS Harness Target Layout | 以 AGENTS、skills、docs/agent、scripts/agent、CI 组织 iOS Harness 文件。 | E3 | high |
| M-SUP-024 | Mobile Skill Set | 用 10 个移动专用 skill 替代 Superpowers 通用 skill 组。 | E4, E5 | high |
| M-SUP-025 | Live Agent Documents | 用 `STATE.md`、`TASKS.md`、specs、plans、decisions、checklists 维护运行状态。 | E6 | high |
| M-SUP-026 | Shared Verification Scripts | 将验证脚本作为模型无关、CI 可复用的执行工具。 | E7, E8 | high |
| M-SUP-027 | Task Capability Matrix | 用任务类型决定弱模型、强模型、人工和 review/升级要求。 | E9 | high |
| M-SUP-028 | Two-failure Escalation | 弱模型失败两次升级强模型，强模型失败两次升级人工。 | E10 | high |
| M-SUP-029 | File-convention Tool Compatibility | 用文件约定和 AGENTS/skills/docs/scripts 兼容多工具，而不是强依赖单一插件。 | E11 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| weak_model_subagent_failure | 移除 subagent 和并行代理，改为检查点式串行执行。 | E2 |
| state_loss | 用 `STATE.md`、`TASKS.md` 和状态更新格式保存进度。 | E6, E14 |
| no_test_completion | 所有验证脚本都有退出码，完成前用脚本证据验证。 | E7, E8 |
| ios_release_risk | App Store 发布 skill、release checklist 和 app-store-ready 脚本覆盖发布准备。 | E5, E8 |
| unsafe_firebase_change | Firebase 安全规则设计需要强模型和人工确认。 | E5, E9 |
| model_overreach | 任务分级矩阵限制弱模型处理架构、安全、Swift 原生和发布上传。 | E9 |
| tool_lock_in | 文件约定兼容 Codex、Claude Code、Cursor、OpenCode、Continue、Copilot。 | E11 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 弱模型轻量迁移 | Composer2 无法稳定管理复杂流程 | 减少认知负担和跨上下文依赖 | 牺牲 subagent 并行和强 review 隔离 |
| 10 个移动专用 skills | 原 skill 过于通用 | 移动端需要 Flutter、Firebase、Swift、App Store 专门流程 | 需要维护垂直领域技能 |
| 验证脚本共享 | 模型输出不可直接信任 | 命令和 CI 比自然语言声明更可复验 | 要维护本地/CI 环境一致性 |
| 任务能力矩阵 | 不同任务风险不同 | 弱模型只做低风险任务，高风险交给强模型/人工 | 需要每个任务先分类 |
| 文件约定兼容工具 | 各工具加载方式不同 | 以可读文件作为最低共同能力 | 高级插件能力需要后续适配 |

## 7. 5 Why Analysis

### Mechanism: Task Capability Matrix

- Why 1: 为什么要任务分级？因为弱模型、强模型和人工适合的任务边界不同。
- Why 2: 为什么不能只靠 skill 提醒？因为安全规则、架构、原生桥接和发布上传具有更高风险。
- Why 3: 为什么要失败两次升级？因为一次失败可能是偶发，连续失败说明当前执行者能力或上下文不足。
- Why 4: 为什么升级要写进 Harness？因为否则模型会在同一错误路径上反复尝试。
- Why 5: 为什么对 iOS 特别重要？因为 iOS 发布、签名、Firebase 安全和 Swift 桥接的错误成本高，必须提前限制执行者。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件目标模型包括 Composer2 弱模型和 Claude 4 Sonnet 强模型，设计原则是保留纪律、去除复杂度。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:1-7 | M-SUP-022 |
| E2 | 核心机制表说明保留/适配 TDD、调试、验证，移除 subagent、并行代理，简化 worktree/review。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:10-33 | M-SUP-022 |
| E3 | 目标目录结构列出 AGENTS、10 个 skills、docs/agent、scripts/agent、CI 等。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:35-87 | M-SUP-023 |
| E4 | `.agents/skills` 格式包含 level、trigger、input、output、escalation。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:108-134 | M-SUP-024 |
| E5 | Skill 总览列出 10 个移动专用 skills 及借鉴来源。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:236-253 | M-SUP-024 |
| E6 | `docs/agent` 被定义为运行时活文档，包含 STATE、TASKS、specs、plans、decisions、checklists。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:136-151 | M-SUP-025 |
| E7 | `scripts/agent` 设计为共享验证工具，脚本单一职责、退出码、结构化输出、CI 兼容。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:153-171,581-593 | M-SUP-026 |
| E8 | 文件列出 verify-flutter-build、verify-tests-pass、verify-ios-pod、verify-firebase-config、verify-app-store-ready、integration tests。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:593-700 | M-SUP-026 |
| E9 | 任务分级矩阵明确人工确认、弱模型可执行、强模型必须、二次 review 和失败升级。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:702-733 | M-SUP-027 |
| E10 | 升级规则定义弱模型失败两次到强模型，强模型失败两次到人工。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:735-754 | M-SUP-028 |
| E11 | 多工具兼容性设计采用文件约定而非工具特定插件。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:772-804 | M-SUP-029 |
| E12 | 实施路径按基础 harness、首次开发迭代、首次发布、持续进化推进。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:843-869 | M-SUP-022 |
| E13 | 风险表覆盖弱模型理解、状态遗漏、状态冲突、skill 不匹配、App Store 审核、脚本环境差异。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:909-919 | risks |
| E14 | 附录定义状态更新格式和任务格式。 | raw/Kimi_Agent_Superpowers 体系探究/03_ios_harness_migration.md:871-907 | M-SUP-025 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Weak-model Lightweight Migration | Goal Layer | AGENTS.md | v0_1 | State retained/simplified/removed Superpowers behaviors |
| iOS Harness Target Layout | Harness Maintenance Layer | docs/agent/FILE_PLACEMENT_MAP.md | v0_1 | Use as initial directory map |
| Mobile Skill Set | Context Layer | .agents/skills/*/SKILL.md | v0_5 | Create mobile-specific skill files incrementally |
| Live Agent Documents | Memory / State Layer | docs/agent/STATE.md | v0_1 | Persist current project state |
| Live Agent Documents | Task Layer | docs/agent/TASKS.md | v0_1 | Persist task queue, assignee, status, verification |
| Shared Verification Scripts | Feedback / Verification Layer | scripts/agent/verify-tests-pass.sh | v0_5 | Add model-independent validation command |
| Shared Verification Scripts | Feedback / Verification Layer | scripts/agent/verify-app-store-ready.sh | v0_5 | Add release readiness validation |
| Task Capability Matrix | Risk / Release Layer | docs/agent/RISK_GATE.md | v0_1 | Encode human/strong-model gates |
| Two-failure Escalation | Role / Review Layer | docs/agent/ESCALATION_RULES.md | v0_1 | Document escalation thresholds |
| File-convention Tool Compatibility | Action / ACI Layer | .mcp.json | v0_5 | Define external tool commands after file harness stabilizes |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | This is the most direct iOS migration blueprint in the superpowers folder. |
| v0_1 | yes | AGENTS, STATE, TASKS, FILE_PLACEMENT_MAP, RISK_GATE, ESCALATION_RULES should start immediately. |
| v0_5 | yes | Mobile skill files and validation scripts become useful after basic state/task flow works. |
| v1_0 | partial | CI workflows, MCP integration, Continue checks and full multi-tool compatibility belong later. |
| no_transfer | yes | Do not restore subagent, parallel dispatch, or complex worktree behavior as defaults. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether Composer2 is still the target weak model | The file names Composer2, but the actual model/runtime for the user's iOS harness may differ. | Confirm current model tiers before implementing runtime rules. |
| Whether Flutter + Firebase is fixed | File assumes this stack. | Confirm actual iOS app architecture before building scripts. |
| Whether `.continue` and `.mcp.json` are needed in v0.1 | They are listed in target structure but not essential to source-card cleaning. | Defer until app development harness phase. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_001 | final report summary aligns with this migration design |
| F_SUP_003 | design logic explains why these mechanisms exist |
| F_SUP_005 | skeptic review should validate or challenge this migration |
| F_SUP_011 | app-store-release detailed skill implementation |
| F_SUP_012 | mobile-tdd detailed skill implementation |
| F_SUP_013 | root-cause-debugging detailed skill implementation |

## 13. Clean Summary for Codex

这份文件是后续 iOS Harness 构建的直接蓝图。它已经把 Superpowers 的通用机制翻译成 iOS/Flutter/Firebase/Swift 场景下的目录、skill、文档、脚本和升级规则。Codex 后续应该优先读取其中的文件放置逻辑和任务分级，而不是直接照搬原 Superpowers：v0.1 先落地 AGENTS、STATE、TASKS、RISK_GATE 和 ESCALATION_RULES；v0.5 再补移动端 skills 和验证脚本；v1.0 再考虑 CI、MCP、Continue 和多工具适配。
