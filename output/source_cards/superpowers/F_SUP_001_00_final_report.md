# Source Card: F_SUP_001 - Superpowers 框架研究及 iOS Harness 迁移综合报告

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_001 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md |
| file_type | markdown |
| topic | Superpowers 框架研究及 iOS Harness 迁移综合报告 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 Superpowers 的工程纪律体系压缩成 iOS/Flutter 弱模型 Harness 的迁移判断、风险清单和落地结构总览。

## 3. File Summary

- 文件将 Superpowers 定义为面向 AI Agent 的软件工程纪律系统，而不是普通工具集。
- 文件认为原框架中大量机制依赖强模型元认知能力，在弱模型环境下需要降级或丢弃。
- 文件建议从“增加规则”转向“减少假设和依赖”，用外部工具和 CI 替代模型自律。
- 文件保留验证文化、YAGNI、小步快跑、文件级 todo 追踪等核心原则。
- 文件明确丢弃或延后 subagent 驱动、双阶段 review、Visual Companion、DOT 图和 Git Worktree。
- 文件给出 iOS Harness 的目标目录、移动端 skill 列表、任务分级和验证脚本设计。
- 文件特别指出 Flutter/iOS 的验证不能只看 `flutter test`，还需要 iOS release build 等平台验证。
- 文件用渐进阶段安排迁移：基础规则层、轻量工作流、质量门控、可选增强。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-001 | Engineering Discipline System | 用技能链、铁律和合理化预防把 agent 工作从聊天式编码转成工程流程。 | E1, E5, E6 | medium |
| M-SUP-002 | Weak-model Adaptation By Assumption Reduction | 不假设弱模型能自我监督、协调 subagent 或做稳定质量判断，改用更少机制和更外部的约束。 | E2, E3, E9 | high |
| M-SUP-003 | Externalized Verification Gate | 用 CI、验证脚本和 release build 把“完成声明”转成外部证据，而不是依赖模型说已验证。 | E4, E8, E12 | high |
| M-SUP-004 | Progressive Adoption Path | 将迁移拆成阶段 0-3，并明确永不采用项，降低一次性迁移风险。 | E10 | high |
| M-SUP-005 | iOS Harness File Placement Blueprint | 给出 AGENTS、skills、docs/agent、scripts/agent、CI workflow 的目标结构。 | E11 | medium |
| M-SUP-006 | Risk Escalation And Human Gate | 将架构、安全、发布、原生桥接等高风险任务升级到强模型或人工确认。 | E13 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| weak_model_self_supervision_failure | 将强模型依赖机制降级，避免把监督责任交给同一个不可靠 agent。 | E2, E3, E9 |
| subagent_orchestration_failure | 明确弱模型不稳定调用 subagent 时应改为 inline 执行或彻底丢弃。 | E9, E10 |
| no_test_completion | 用外部验证脚本和 CI 强制验证，减少“声称测试通过但未运行”的风险。 | E4, E8, E12 |
| ios_build_gap | 指出 `flutter test` 不等于 Xcode/iOS release 构建成功，要求增加 iOS release build gate。 | E8, E12 |
| worktree_ios_path_breakage | 识别 Xcode 工程路径对 worktree 的冲突，并建议禁用 worktree。 | E7 |
| over_engineering | 通过只保留 30% 核心原则、丢弃高 token/高复杂度机制来控制框架膨胀。 | E3, E10 |
| wrong_file_placement | 提供目标目录结构和脚本/文档位置，降低迁移时文件散落风险。 | E11 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 保留验证文化、小步快跑、YAGNI | 这些原则适合弱模型和移动开发 | 它们减少模型需要记忆和自我监督的内容 | 会牺牲 Superpowers 原框架的完整流程感 |
| 丢弃 subagent 驱动和双阶段 review | 弱模型无法稳定调用和审查 subagent | reviewer/implementer 隔离依赖强模型上下文管理 | 少了并行能力，需要更线性的执行节奏 |
| 用自动化验证替代模型自律 | 弱模型可能虚假声明验证通过 | 外部命令比自然语言承诺更可审计 | 需要维护脚本和 CI |
| 禁用 Git Worktree | iOS/Xcode 路径和签名环境脆弱 | 物理隔离可能破坏移动工程环境 | 降低隔离强度，需要更严格文件范围规则 |
| 分阶段引入 Harness | 一次迁移复杂度太高 | 先验证最小规则层，减少无效机制沉没成本 | 机制库成熟速度较慢 |

## 7. 5 Why Analysis

### Mechanism: Externalized Verification Gate

- Why 1: 为什么需要外部验证？因为弱模型可能声称测试已通过但实际未运行。
- Why 2: 为什么自然语言声明不够？因为完成状态需要可复验的命令输出，而不是 agent 自我报告。
- Why 3: 为什么移动端更需要它？因为 `flutter test` 通过仍可能在 iOS build、签名、pod、权限配置处失败。
- Why 4: 为什么不是让模型更严格执行 checklist？因为文件指出弱模型的自我监督能力本身不可靠。
- Why 5: 为什么这应进入 Harness？因为 Harness 的后续输出必须能被 Codex 稳定读取和执行，验证门应成为结构化文件和脚本，而不是临场提醒。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件将 Superpowers 定义为软件工程纪律系统，核心是技能链、铁律和合理化预防。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:15 | M-SUP-001 |
| E2 | 文件判断约 60% 核心机制在弱模型环境下会失效，特别是 subagent、TDD 铁律和双阶段 review。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:17 | M-SUP-002 |
| E3 | 文件建议减少假设和依赖，并用 CI/外部工具、顺序执行、自动化检查清单替代模型自律。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:21 | M-SUP-002, M-SUP-003 |
| E4 | 文件建议保留验证文化、YAGNI、小步快跑，并重新设计轻量级变体。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:23 | M-SUP-003, M-SUP-004 |
| E5 | 文件列出 Process Skills 链条和 Implementation Skills，说明流程技能与执行纪律的分层。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:86-108 | M-SUP-001 |
| E6 | 文件把流程约束概括为 description 触发、Iron Law 禁止和合理化预防三层。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:129-133 | M-SUP-001 |
| E7 | 文件指出 Git Worktree 与 Xcode 工程路径存在冲突，并建议禁用 worktree。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:207 | worktree_ios_path_breakage |
| E8 | 文件指出 `flutter test` 通过不等于 Xcode 构建成功，并要求增加 iOS release build。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:210 | M-SUP-003, ios_build_gap |
| E9 | 文件将 Subagent-Driven Development 标为弱模型下致命问题，并建议替换为 inline 执行。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:197 | M-SUP-002 |
| E10 | 文件给出阶段 0-3 和永不采用项，明确渐进采用边界。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:239-247 | M-SUP-004 |
| E11 | 文件提供 iOS Harness 目标目录结构，包括 `.agents/skills`、`docs/agent`、`scripts/agent` 和 CI。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:253-288 | M-SUP-005 |
| E12 | 文件设计验证脚本，并要求脚本单一职责、结构化输出、CI 中无修改运行。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:360-372 | M-SUP-003 |
| E13 | 文件定义弱模型、强模型、人工的任务升级路径。 | raw/Kimi_Agent_Superpowers 体系探究/00_final_report.md:358 | M-SUP-006 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Engineering Discipline System | Goal Layer | AGENTS.md | v0_1 | Convert into concise assistant contract and task start checklist |
| Weak-model Adaptation By Assumption Reduction | Context Layer | docs/agent/MODEL_LIMITS.md | v0_1 | Record what weak models may and may not do without escalation |
| Externalized Verification Gate | Feedback / Verification Layer | scripts/agent/verify-tests-pass.sh | v0_5 | Add command-based validation instead of relying on agent claims |
| Externalized Verification Gate | Feedback / Verification Layer | scripts/agent/verify-ios-build.sh | v0_5 | Require iOS release build evidence for mobile completion claims |
| Progressive Adoption Path | Task Layer | docs/agent/TASKS.md | v0_1 | Represent migration phases and current task status |
| iOS Harness File Placement Blueprint | Harness Maintenance Layer | docs/agent/FILE_PLACEMENT_MAP.md | v0_1 | Map Superpowers-derived concepts to iOS harness files |
| Risk Escalation And Human Gate | Risk / Release Layer | docs/agent/RISK_GATE.md | v0_1 | Define when to escalate to strong model or human review |
| Verification Scripts In CI | Action / ACI Layer | .github/workflows/ios-build.yml | v1_0 | Run the same local verification scripts in CI |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | Transfer principles and verification gates, not the full Superpowers workflow. |
| v0_1 | yes | Adopt AGENTS rules, task state, risk gate, file placement map, and minimal verification checklist. |
| v0_5 | yes | Add verification scripts, structured output, and Flutter/iOS build gates. |
| v1_0 | yes | Add CI enforcement and possibly runtime-safe task/file scope checks. |
| no_transfer | yes | Do not transfer Visual Companion, DOT diagrams, broad cross-platform support, subagent-driven development, or Git Worktree as default behavior. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether “60% failure” is empirical or analytical | This file states the number but does not show measurement data. | Check F_SUP_005 skeptic review and supporting raw reports. |
| Whether all listed generated deliverables exist and are internally consistent | This file is a final report and references multiple output files. | Process F_SUP_002-F_SUP_013 and compare claims. |
| Whether session-start hooks are impossible in the target Codex/iOS environment | This file says weak models do not support them well, but target runtime may differ. | Inspect actual Codex harness constraints and plugin/tool support later. |
| Whether Flutter is final target or iOS native/Swift-only is possible | File assumes Flutter + Firebase + Swift iOS. | Confirm actual app harness target stack before implementation. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_002 | expected detailed anatomy backing for framework structure and skills |
| F_SUP_003 | expected detailed design logic backing for mechanisms |
| F_SUP_004 | expected detailed iOS migration design backing for file placement |
| F_SUP_005 | expected skeptic review backing for weak-model risks |
| F_SUP_011 | expected concrete app-store-release skill source |
| F_SUP_012 | expected concrete mobile-tdd skill source |
| F_SUP_013 | expected concrete root-cause-debugging skill source |

## 13. Clean Summary for Codex

这份文件是 Superpowers 迁移研究的高层总览，价值在于给出“哪些原则可迁移、哪些机制应丢弃、为什么 iOS/Flutter 场景需要外部验证”的初始判断。后续 iOS Harness 不应直接照搬 Superpowers 的完整 skill 链，而应先落地轻量规则层：AGENTS 行为契约、TASKS/STATE 状态追踪、风险升级、人类确认点、验证脚本和 CI 门控。它也提醒 Codex：subagent、worktree、双阶段 review、Visual Companion 这些机制在弱模型和 iOS 工程里风险较高，需要通过后续 Source Card 逐项验证后再决定是否进入机制库。
