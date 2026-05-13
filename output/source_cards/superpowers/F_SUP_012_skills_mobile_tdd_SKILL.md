# Source Card: F_SUP_012 - mobile-tdd SKILL.md

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_012 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md |
| file_type | markdown |
| topic | mobile-tdd |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 Superpowers 的 TDD 铁律迁移到 Flutter/Dart、Widget、集成、Swift XCTest 和 Firebase Emulator 测试场景中。

## 3. File Summary

- Skill frontmatter 说明在实现功能、修复 Bug、重构前触发，适用于 Flutter Dart 和 Swift 原生代码。
- 核心原则是先写测试、看失败、再写最少代码通过。
- 铁律要求没有先失败的测试就没有生产代码，先写代码要删除重来。
- 它定义 RED、GREEN、REFACTOR 三阶段和提交时机。
- 它提供 Flutter 测试金字塔：大量单元测试、中等 Widget 测试、少量集成测试。
- 它提供 Swift 原生代码 XCTest 示例。
- 它定义 TDD 工作流检查清单和移动端测试反模式。
- 它提供 mock/fake、Firebase Emulator、验证命令和与原版 TDD 的差异。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-075 | Mobile TDD Trigger | 在功能、Bug 修复、重构和行为变更前触发测试先行流程。 | E1, E3 | high |
| M-SUP-076 | Failing-test-first Discipline | 要求先写失败测试，再写生产代码；先写实现则删除重来。 | E2, E3 | medium |
| M-SUP-077 | Red Green Refactor Loop | 定义 RED、GREEN、REFACTOR 的操作和提交时机。 | E4 | high |
| M-SUP-078 | Flutter Test Pyramid | 将测试分为单元、Widget、集成三层并给出适用范围。 | E5, E6, E7 | high |
| M-SUP-079 | Swift XCTest Coverage | 为 Flutter 平台通道/原生插件提供 XCTest 测试位置和示例。 | E8 | high |
| M-SUP-080 | Mobile Testing Anti-patterns | 列出测试实现、重复初始化、一个测试测太多、依赖外部服务、忽略 Widget 测试等反模式。 | E10 | high |
| M-SUP-081 | Test Double Guidance | 区分 mocktail mock 和 fake repository 示例。 | E11 | medium |
| M-SUP-082 | Firebase Emulator Test Guidance | 使用 Firebase Emulator 测试 Firestore/Auth 等集成。 | E12 | medium |
| M-SUP-083 | Mobile TDD Verification Commands | 完成 TDD 循环后运行 flutter test、指定测试、verbose、coverage，并设置覆盖率阈值。 | E13 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| tests_after_implementation | 铁律要求先失败测试，否则删除实现重来。 | E2, E3 |
| pseudo_test_coverage | 测试金字塔要求不同层次测试覆盖不同风险。 | E5 |
| widget_behavior_unverified | Widget 测试覆盖渲染、交互、页面布局和导航。 | E7 |
| native_bridge_unverified | Swift 原生代码使用 XCTest。 | E8 |
| bad_mobile_tests | 反模式区指出测试实现、测太多、外部服务依赖等问题。 | E10 |
| firebase_live_dependency | Firebase 测试建议使用 Emulator。 | E12 |
| no_test_completion | 验证步骤要求运行 flutter test/analyze 等测试命令。 | E9, E13 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 严格失败测试先行 | 确保测试验证真实期望 | 防止测试追认实现 | 与 F_SUP_005 的弱模型/Flutter 成本警告冲突 |
| Flutter 测试金字塔 | 不同测试速度和覆盖面不同 | 把大量验证放在快的单元层 | 集成问题仍需少量端到端测试 |
| Widget 测试示例 | UI 行为需要可观察验证 | 防止只靠热重载/肉眼检查 | 需要 MaterialApp/Scaffold 等包装样板 |
| Firebase Emulator | 避免真实外部服务依赖 | 保持测试可重复和 CI 友好 | Emulator setup 有环境成本 |

## 7. 5 Why Analysis

### Mechanism: Flutter Test Pyramid

- Why 1: 为什么移动端 TDD 需要测试金字塔？因为 Flutter app 同时有业务逻辑、Widget 行为、跨页面和 Firebase 集成。
- Why 2: 为什么不能只写集成测试？因为集成测试慢且定位问题成本高。
- Why 3: 为什么不能只写单元测试？因为 UI 渲染、交互和导航需要 Widget/integration 测试。
- Why 4: 为什么 Swift 还要单独覆盖？因为平台通道和原生插件不一定被 Dart 测试覆盖。
- Why 5: 为什么这对 iOS Harness 有价值？因为后续验证脚本和任务验收需要知道不同代码类型对应哪类测试。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Frontmatter 指定触发条件、输入、输出和升级场景。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:1-8 | M-SUP-075 |
| E2 | 概述要求先写测试，看失败，再写最少代码通过。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:12-24 | M-SUP-076 |
| E3 | 铁律要求没有先失败测试就没有生产代码，先写代码要删除重来。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:27-38 | M-SUP-076 |
| E4 | RED-GREEN-REFACTOR 定义测试、实现、重构和提交时机。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:55-79 | M-SUP-077 |
| E5 | Flutter 测试金字塔列出集成、Widget、单元测试层次。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:81-91 | M-SUP-078 |
| E6 | 单元测试适用于业务逻辑、状态管理、数据转换和工具函数。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:93-137 | M-SUP-078 |
| E7 | Widget 测试适用于渲染、页面布局、交互和导航。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:139-212 | M-SUP-078 |
| E8 | Swift 原生代码使用 XCTest，测试位置为 ios/RunnerTests。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:260-290 | M-SUP-079 |
| E9 | TDD 工作流检查清单覆盖开始前、RED、GREEN、REFACTOR、提交前。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:292-317 | M-SUP-083 |
| E10 | 移动端测试反模式列出测试实现、重复 setup、单测试过多、外部服务依赖、忽略 Widget 测试。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:319-374 | M-SUP-080 |
| E11 | Mock/Fake 部分给出 mocktail 和 FakeAuthRepository 示例。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:376-422 | M-SUP-081 |
| E12 | Firebase 测试特别指南使用 Firebase Emulator Suite。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:424-460 | M-SUP-082 |
| E13 | 验证步骤列出 flutter test、指定测试、verbose、coverage 和覆盖率最低要求。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:463-485 | M-SUP-083 |
| E14 | 与原版差异说明本 skill 增加 Flutter 测试金字塔、移动端反模式、Firebase Emulator、Widget 和 Swift XCTest。 | raw/Kimi_Agent_Superpowers 体系探究/skills/mobile-tdd/SKILL.md:488-496 | transfer |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Mobile TDD Trigger | Context Layer | .agents/skills/mobile-tdd/SKILL.md | v0_5 | Adopt with weak-model downgrade notes |
| Failing-test-first Discipline | Feedback / Verification Layer | docs/agent/TESTING_GUIDE.md | v0_5 | Convert strict iron law to guidance or tiered rule based on risk |
| Red Green Refactor Loop | Task Layer | docs/agent/TASKS.md | v0_5 | Add test-first task checklist |
| Flutter Test Pyramid | Feedback / Verification Layer | docs/agent/TESTING_GUIDE.md | v0_5 | Map code types to test types |
| Swift XCTest Coverage | Feedback / Verification Layer | docs/agent/TESTING_GUIDE.md | v0_5 | Add native bridge test expectations |
| Mobile Testing Anti-patterns | Role / Review Layer | docs/agent/REVIEW_GUIDE.md | v0_5 | Add mobile test review checklist |
| Test Double Guidance | Feedback / Verification Layer | docs/agent/TESTING_GUIDE.md | v0_5 | Add mock/fake selection guidance for mobile tests |
| Firebase Emulator Test Guidance | Feedback / Verification Layer | scripts/agent/run-integration-tests.sh | v1_0 | Add emulator-backed integration tests |
| Mobile TDD Verification Commands | Feedback / Verification Layer | scripts/agent/verify-tests-pass.sh | v0_5 | Run flutter test/analyze/coverage checks |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | Transfer testing taxonomy and verification commands; strict delete-and-restart rule conflicts with weak-model critique. |
| v0_1 | no | Current app harness should start with verification culture, not strict mobile TDD. |
| v0_5 | yes | Add mobile-tdd skill, testing guide, review anti-patterns and verify-tests script. |
| v1_0 | yes | Add Firebase emulator and coverage enforcement in CI. |
| no_transfer | yes | Do not apply “delete prior code and restart” rigidly for weak models without human confirmation. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Strict TDD may be too costly for Flutter weak-model workflow | F_SUP_005 argues Flutter Widget tests have setup cost and weak models produce pseudo RED. | Reconcile during mechanism synthesis; likely downgrade to validation-oriented development. |
| Coverage thresholds may not fit all projects | File states unit coverage >= 70% and Widget coverage all pages. | Confirm team quality bar and CI capacity. |
| Firebase emulator setup is only sketched | The file says full auth setup needs Firebase documentation. | Design concrete emulator script later. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_004 | migration design lists mobile-tdd as skill 5 |
| F_SUP_005 | skeptic review challenges strict TDD transfer |
| F_SUP_007 | AGENTS references mobile-tdd |
| F_SUP_013 | root-cause-debugging complements TDD when tests fail |

## 13. Clean Summary for Codex

这份 skill 提供了移动端测试体系的具体内容：Flutter 单元测试、Widget 测试、集成测试、Swift XCTest、测试替身、Firebase Emulator 和验证命令。它对后续 iOS Harness 很有价值，但必须和 F_SUP_005 的弱模型批判合并使用：不要把“先写代码就删除重来”的铁律直接给弱模型执行，而应保留测试先行文化、测试金字塔、反模式和验证脚本。v0.5 可以引入 `mobile-tdd`，v1.0 再做 coverage/Emulator/CI 强制。
