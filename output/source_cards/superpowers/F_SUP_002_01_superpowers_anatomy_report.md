# Source Card: F_SUP_002 - Superpowers 框架解剖报告

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_002 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md |
| file_type | markdown |
| topic | Superpowers 框架解剖报告 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把 Superpowers 仓库拆成目录、顶层上下文、skills、hooks、宿主适配和测试体系，说明哪些结构能迁移到 iOS Harness。

## 3. File Summary

- 文件基于 Superpowers v5.1.0，对顶层目录、14 个技能、宿主适配和辅助设施做结构分析。
- 它把 `skills/` 识别为最重要目录，每个 `SKILL.md` 是自包含行为规范。
- 它说明 skill frontmatter 的 `description` 是行为触发提示，而不是普通摘要。
- 它把 `hooks/session-start` 视为自动触发技能的核心基础设施。
- 它说明多宿主适配通过不同插件目录、符号链接、Gemini `@import` 和同步脚本完成。
- 它将 Process Skills 和 Implementation Skills 分层，强调不可跳过的流程链。
- 它总结了降低弱模型失控风险和减少上下文污染的机制体系。
- 它对 iOS Harness 提出 bootstrap、skill discovery、description matching、约定路径、subagent/降级方案等迁移建议。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-007 | Skill As Behavior Code | 将 `SKILL.md` 视为可触发的行为约束单元，而不只是文档。 | E1, E2, E8 | high |
| M-SUP-008 | Session Bootstrap Hook | 通过 session-start 在新会话注入引导技能，使技能触发机制真正生效。 | E3, E7 | high |
| M-SUP-009 | Host Adapter Layer | 为 Claude、Codex、Cursor、OpenCode、Gemini 等宿主保留不同 manifest/导入机制。 | E4, E5 | high |
| M-SUP-010 | Single Source Alias | 用 AGENTS.md 指向 CLAUDE.md，避免多上下文入口内容漂移。 | E5 | high |
| M-SUP-011 | Process And Implementation Skill Split | 将生命周期流程技能和执行纪律技能分层，形成不可跳过的链条。 | E6 | high |
| M-SUP-012 | Convention Path Memory | 通过 `docs/plans`、`docs/superpowers/specs` 等约定路径，让技能间通过文件系统传递状态。 | E7, E9 | medium |
| M-SUP-013 | Harness Integration Tests | 按宿主和功能验证 skill triggering、plugin sync、subagent 流程。 | E10 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| skill_not_triggered | 要求 Session Bootstrap 和 description-based matching，避免技能文件存在但不加载。 | E3, E11 |
| context_entry_drift | 使用 AGENTS.md/CLAUDE.md 单点真理别名，避免多个入口不一致。 | E5 |
| host_incompatibility | 把每个宿主适配拆成独立目录和 manifest，降低一个宿主格式影响其他宿主的风险。 | E4 |
| context_pollution | Fresh subagent、controller 构造上下文、约定路径和外部引用共同减少会话污染。 | E12 |
| weak_model_rationalization | 通过 Iron Law、Red Flags、人类审批、审查层和反馈层降低模型绕过流程的风险。 | E8, E12 |
| untested_bootstrap | 用 skill-triggering 测试验证新会话触发行为。 | E10, E11 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 每个 skill 独立目录 | 便于发现和加载 | 把注意力切成可触发的行为模块 | 需要宿主支持技能发现 |
| `description` 兼作文档和触发条件 | 减少重复配置 | 让行为触发与技能说明同源 | 描述质量会直接影响触发准确性 |
| session-start bootstrap | 会话开始即注入引导 | 解决“规则在磁盘但模型不知道”的问题 | 宿主必须支持会话钩子或等效机制 |
| 多宿主适配目录 | 每个平台格式不同 | 核心技能可复用，边缘 manifest 分离 | 增加同步和测试维护成本 |
| 约定路径通信 | 后续步骤可从文件恢复 | 减少依赖长对话历史 | 需要严格文件命名和目录纪律 |

## 7. 5 Why Analysis

### Mechanism: Session Bootstrap Hook

- Why 1: 为什么需要 bootstrap？因为只把 skills 放在磁盘上不会让模型自动使用它们。
- Why 2: 为什么必须在会话开始注入？因为引导技能定义了后续所有技能选择规则。
- Why 3: 为什么不能依赖用户每次提醒？因为 Harness 的目标是稳定复现流程，而不是靠人工记忆。
- Why 4: 为什么 iOS Harness 也要设计等效机制？因为移动端 agent 同样会遇到上下文入口和技能触发问题。
- Why 5: 为什么要测试 bootstrap？因为文件指出新 harness PR 必须证明干净会话中技能能自动触发。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件说明分析范围覆盖完整目录结构、14 个技能、宿主适配机制和辅助设施。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:3-6 | scope |
| E2 | `skills/` 被标记为核心目录，每个 skill 是自包含行为规范，使用 YAML frontmatter。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:31-33,151-166 | M-SUP-007 |
| E3 | `hooks/` 与 `session-start` 被描述为技能自动触发的关键基础设施。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:27,627-645 | M-SUP-008 |
| E4 | 文件列出 Claude、Codex、Cursor、OpenCode、Gemini 等不同宿主适配方式。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:581-594 | M-SUP-009 |
| E5 | AGENTS.md 作为 CLAUDE.md 符号链接，被解释为文件名兼容和单点真理策略。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:102-114,595-603 | M-SUP-010 |
| E6 | 文件将 Process Skills 和 Implementation Skills 分类，并说明流程链不可跳过。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:535-578 | M-SUP-011 |
| E7 | docs、hooks、scripts 目录被解释为计划/规格约定路径、会话钩子和维护自动化。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:647-714 | M-SUP-012 |
| E8 | 文件总结“技能即代码”“不可理性化”“强制链条”“验证即诚实”等设计哲学。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:717-735 | M-SUP-007 |
| E9 | 文件列出减少上下文污染的机制，包括 fresh subagent、controller 构造上下文、约定路径、外部引用。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:752-763 | M-SUP-012 |
| E10 | tests 目录按宿主/功能组织，包含 skill-triggering、codex-plugin-sync、subagent-driven-dev。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:695-714 | M-SUP-013 |
| E11 | iOS Harness 必须实现 Session Bootstrap、Skill Discovery、Description-based Matching。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:765-775 | M-SUP-008 |
| E12 | 文件列出多层防御和上下文污染防护体系。 | raw/Kimi_Agent_Superpowers 体系探究/01_superpowers_anatomy_report.md:737-763 | failure modes |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Skill As Behavior Code | Goal Layer | .agents/skills/<skill>/SKILL.md | v0_1 | Define each iOS workflow as a self-contained skill file |
| Session Bootstrap Hook | Context Layer | docs/agent/BOOTSTRAP.md | v0_1 | Specify how Codex/iOS session should load the harness entry rules |
| Session Bootstrap Hook | Action / ACI Layer | scripts/agent/check-bootstrap.sh | v0_5 | Add a check that required harness files are present before execution |
| Host Adapter Layer | Harness Maintenance Layer | docs/agent/HOST_ADAPTERS.md | v0_5 | Track per-host context entry conventions without duplicating rules |
| Single Source Alias | Context Layer | AGENTS.md | v0_1 | Keep AGENTS as the canonical entry or documented alias |
| Process And Implementation Skill Split | Task Layer | docs/agent/WORKFLOW_CHAIN.md | v0_1 | Separate planning/review/verification rules from implementation-specific rules |
| Convention Path Memory | Memory / State Layer | docs/agent/STATE.md | v0_1 | Use files, not chat history, for persistent state |
| Harness Integration Tests | Feedback / Verification Layer | tests/harness/test_skill_triggering.md | v0_5 | Define transcript-based or scripted checks for skill loading |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | Transfer file/skill architecture and bootstrap principle; do not blindly transfer all strong-model workflows. |
| v0_1 | yes | Canonical AGENTS entry, skills directory, state/tasks docs, bootstrap notes, workflow chain. |
| v0_5 | yes | Add bootstrap checks, host adapter docs, and harness integration tests. |
| v1_0 | yes | Runtime skill discovery and description matching can be added once the basic file harness is stable. |
| no_transfer | yes | Do not transfer broad multi-host support before the target iOS/Codex runtime is clear. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether iOS Harness can support true session-start hooks | This file recommends it, but target runtime capabilities are not proven here. | Check actual Codex/iOS harness runtime APIs. |
| Whether subagent dispatch should be P1 in weak-model iOS scenario | This anatomy file lists it as migration requirement, but F_SUP_001 warns against it for weak models. | Compare F_SUP_005 skeptic review and final mapping decisions. |
| Whether all 14 skills should be copied | File documents all skills, but does not filter by iOS suitability. | Process F_SUP_003-F_SUP_005 before deciding. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_001 | summary-level migration judgment |
| F_SUP_003 | expected deeper design logic for the mechanisms in this anatomy |
| F_SUP_004 | expected iOS-specific file placement and skill list |
| F_SUP_005 | expected critique of weak-model risks |

## 13. Clean Summary for Codex

这份文件是理解 Superpowers 文件结构和运行方式的主要依据。它告诉后续 iOS Harness：真正需要迁移的不是某个单一提示词，而是一组可发现的 skill 文件、一个会话 bootstrap 入口、一套约定路径、宿主适配层和验证测试。对 Codex 来说，最重要的落点是先稳定 `AGENTS.md`、`.agents/skills/`、`docs/agent/STATE.md`、`docs/agent/TASKS.md` 和 bootstrap/skill-triggering 检查；至于 subagent、多宿主和 worktree 等能力，应等后续风险卡确认后再决定是否进入 v0.5 或 v1.0。
