# Source Card: F_SUP_013 - root-cause-debugging SKILL.md

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_013 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md |
| file_type | markdown |
| topic | root-cause-debugging |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把系统化调试改造成移动端根因调查流程，要求先收集证据、形成假设、实验验证，再做最小修复和验证记录。

## 3. File Summary

- Skill frontmatter 指定遇到 Bug、测试失败、异常行为、构建失败、性能问题时触发。
- 核心原则是修复前必须找到根因，症状修复就是失败。
- 四阶段为信息收集、假设形成、假设验证、修复与验证。
- Phase 1 要创建调试会话文件，记录现象、期望/实际、环境、频率、首次出现、错误信息、复现步骤和已尝试修复。
- Phase 1 还收集 Flutter、iOS 原生、Firebase Crashlytics 日志，并判断范围。
- Phase 2 按 Flutter、Swift、Firebase、构建/工具链分类列出可能根因并按可能性排序。
- Phase 3 用代码审查、日志注入、最小复现、git bisect、对比测试、DevTools、Xcode Instruments 验证假设。
- Phase 4 做最小修复、运行相关/全部测试、flutter analyze、iOS simulator build，并记录根因、修复、验证和预防措施。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-084 | No-fix-before-root-cause Gate | 在完成根因调查前禁止提出修复。 | E1, E2 | high |
| M-SUP-085 | Debug Session Record | 为每次问题创建 `docs/agent/debug/debug-*.md` 记录事实和尝试。 | E3 | high |
| M-SUP-086 | Mobile Evidence Collection | 收集 Flutter verbose/logs、iOS 控制台/崩溃日志、Crashlytics。 | E4 | high |
| M-SUP-087 | Scope Classification Checklist | 判断问题属于 Flutter/Swift、debug/release、设备/iOS 版本、回归、用户/账户特定。 | E5 | high |
| M-SUP-088 | Layered Hypothesis Taxonomy | 按 Flutter、Swift、Firebase、构建/工具链列根因分类。 | E6 | high |
| M-SUP-089 | Hypothesis Experiment Library | 使用代码审查、日志注入、最小复现、bisect、对比测试、DevTools、Instruments 验证。 | E7 | high |
| M-SUP-090 | Fix Verification Record | 修复后运行相关测试、全量测试、复现验证、analyze、iOS build，并更新调试文件。 | E8 | high |
| M-SUP-091 | Debug Escalation Matrix | 阶段失败时请求人工/强模型，连续失败两次升级。 | E9 | high |
| M-SUP-092 | Mobile Debug Quick Reference | 为 Flutter build、iOS crash、Firestore、性能问题提供快速排查路径。 | E10 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| random_fix_loop | 铁律禁止未调查根因就修复。 | E2 |
| lost_debug_context | 调试会话文件记录现象、环境、日志、复现和尝试。 | E3 |
| incomplete_reproduction | Phase 1 出口要求至少 3 次复现和范围确定。 | E5 |
| single_hypothesis_bias | Phase 2 要至少列出 3 个假设并排序。 | E6 |
| unverified_fix | Phase 4 要运行测试、复现验证、analyze、iOS build。 | E8 |
| mobile_layer_confusion | 假设分类区分 Flutter、Swift、Firebase、构建工具链。 | E6 |
| weak_model_stuck | 降级路径和连续失败两次升级。 | E9 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 调试会话文件 | 保留证据链 | 防止长会话丢失已尝试内容 | 需要持续更新 |
| 先范围分类 | 快速定位问题层 | Flutter/iOS/Firebase 问题跨层，容易误修 | 需要多环境验证 |
| 假设排序 | 先验证最可能根因 | 避免随机尝试 | 初始评分可能不准 |
| 实验库 | 给模型可选验证方法 | 减少“试试看”修复 | 复杂工具如 Instruments 可能需要人工 |

## 7. 5 Why Analysis

### Mechanism: Debug Session Record

- Why 1: 为什么要写调试会话文件？因为 bug 调查容易跨多轮会话和多种工具。
- Why 2: 为什么要记录已尝试修复？因为重复尝试会浪费时间并制造新问题。
- Why 3: 为什么要记录环境和复现频率？因为移动端 bug 常与设备、iOS 版本、构建模式相关。
- Why 4: 为什么要记录证据链？因为根因必须可复现、可解释，不是猜测。
- Why 5: 为什么这对 Harness 有价值？因为弱模型调试最容易陷入随机修复，文件化记录能强迫它先收集事实。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Frontmatter 指定触发条件、输入输出和升级场景。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:1-8 | M-SUP-084 |
| E2 | 概述和铁律要求修复前找到根因，没有根因调查就没有修复方案。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:12-31 | M-SUP-084 |
| E3 | Phase 1 要创建 debug 文件，记录问题描述、错误信息、复现步骤、已尝试修复。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:51-93 | M-SUP-085 |
| E4 | Phase 1 收集 Flutter、iOS 原生、Firebase Crashlytics 日志。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:95-121 | M-SUP-086 |
| E5 | Phase 1 范围确定和出口标准要求判断层级、模式、设备、回归并确认复现。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:123-161 | M-SUP-087 |
| E6 | Phase 2 按 Flutter、Swift、Firebase、构建/工具链列根因分类，并要求至少 3 个假设。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:163-234 | M-SUP-088 |
| E7 | Phase 3 验证方法库包括代码审查、日志注入、最小复现、git bisect、对比测试、DevTools、Instruments。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:236-358 | M-SUP-089 |
| E8 | Phase 4 修复后运行相关测试、全量测试、复现验证、analyze、iOS simulator build，并更新记录。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:373-429 | M-SUP-090 |
| E9 | 降级路径定义每阶段失败处理和连续失败两次升级。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:433-448 | M-SUP-091 |
| E10 | 快速参考覆盖 Flutter 构建失败、iOS 崩溃、Firestore 读取失败、性能问题。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:450-489 | M-SUP-092 |
| E11 | 与原版差异说明移动版增加信息收集、分类、DevTools/Instruments、降级路径和快速参考。 | raw/Kimi_Agent_Superpowers 体系探究/skills/root-cause-debugging/SKILL.md:491-499 | transfer |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| No-fix-before-root-cause Gate | Goal Layer | .agents/skills/root-cause-debugging/SKILL.md | v0_5 | Adopt as debugging skill |
| Debug Session Record | Memory / State Layer | docs/agent/debug/debug-YYYY-MM-DD-issue.md | v0_5 | Store per-bug investigation state |
| Mobile Evidence Collection | Action / ACI Layer | scripts/agent/collect-debug-logs.sh | v1_0 | Automate log collection where possible |
| Scope Classification Checklist | Task Layer | templates/debug_session_template.md | v0_5 | Add scope checklist to debug template |
| Layered Hypothesis Taxonomy | Context Layer | docs/agent/DEBUG_GUIDE.md | v0_5 | Document Flutter/Swift/Firebase/build categories |
| Hypothesis Experiment Library | Action / ACI Layer | docs/agent/DEBUG_GUIDE.md | v0_5 | List validation methods and commands |
| Fix Verification Record | Feedback / Verification Layer | scripts/agent/verify-tests-pass.sh | v0_5 | Require post-fix verification commands |
| Debug Escalation Matrix | Risk / Release Layer | docs/agent/ESCALATION_RULES.md | v0_1 | Use failure thresholds for debug escalation |
| Mobile Debug Quick Reference | Context Layer | docs/agent/DEBUG_GUIDE.md | v0_5 | Add quick lookup paths for Flutter build, iOS crash, Firestore and performance issues |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | Root-cause debugging is directly useful for mobile app harness reliability. |
| v0_1 | partial | Keep escalation rule and no-random-fix principle in AGENTS/RISK_GATE. |
| v0_5 | yes | Add root-cause-debugging skill, debug templates, DEBUG_GUIDE and post-fix verification. |
| v1_0 | yes | Automate log collection and integrate DevTools/Instruments instructions as scripts/docs. |
| no_transfer | yes | Do not require weak models to operate Instruments/lldb without human or strong-model help. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Some commands may require local tools not always installed | `idevicesyslog`, Firebase CLI, DevTools, Instruments availability varies. | Add environment checks before script implementation. |
| Three reproductions may be unrealistic for flaky bugs | Some production crashes are rare. | Allow evidence gathering fallback for non-reproducible bugs. |
| Strong model vs human boundary for lldb/Instruments | File escalates but exact threshold may depend on team skill. | Define in RISK_GATE during app harness implementation. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_004 | migration design lists root-cause-debugging as skill 6 |
| F_SUP_005 | skeptic review supports systematic debug but warns about weak-model limits |
| F_SUP_007 | AGENTS references root-cause-debugging |
| F_SUP_012 | mobile-tdd complements debugging when tests fail |

## 13. Clean Summary for Codex

这份 skill 是 iOS Harness 中很适合迁移的调试流程资产。它的核心不是“调试命令清单”，而是禁止随机修复：先记录事实、收集日志、限定范围、列假设、验证假设，再做最小修复和完整验证。对后续 Codex 来说，v0.1 可先保留 no-fix-before-root-cause 和失败升级规则；v0.5 建立 `docs/agent/debug/`、debug template、DEBUG_GUIDE 和 root-cause-debugging skill；v1.0 再把日志收集和验证命令脚本化。
