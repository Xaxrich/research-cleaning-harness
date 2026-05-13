# Source Card: F_SUP_005 - Superpowers 框架批判性审查报告

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_005 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md |
| file_type | markdown |
| topic | Superpowers 框架批判性审查报告 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：指出 Superpowers 的强模型假设在弱模型和 Flutter/iOS 场景中会失效，并给出保留、降级、替换和永不迁移清单。

## 3. File Summary

- 文件认为 Superpowers 是为 Claude 3.5 Sonnet+ 级强模型设计的高纪律框架。
- 它判断迁移到 Composer2 级弱模型时，约 60% 核心机制会失效或变形，约 40% 流程步骤过度设计。
- 它建议不整体迁移，只提取约 30% 核心原则：验证文化、YAGNI、文件级 todo 追踪。
- 它将 subagent 驱动、Visual Companion、DOT 流程图、subagent 双阶段 review、跨平台适配列为彻底丢弃。
- 它将 TDD、Brainstorming、Worktree、Verification、Writing Plans、Finishing、Skill 触发列为大幅简化。
- 它列出 Flutter/iOS 场景特有冲突：Xcode 路径、Flutter Widget 测试、pubspec 检测、iOS 构建验证。
- 它给出真实失败模式，如假装测试通过、伪 RED、review 幻觉、worktree 路径混乱和长任务上下文丢失。
- 它要求架构、安全、iOS 配置、发布、code review、测试覆盖判断和合并冲突必须人工兜底。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-030 | Selective Principle Extraction | 不整体迁移，只抽取验证文化、YAGNI、文件级 todo 等低依赖原则。 | E1, E2 | high |
| M-SUP-031 | Explicit Non-transfer List | 将 subagent、Visual Companion、DOT、subagent review、跨平台适配列为丢弃项。 | E8 | high |
| M-SUP-032 | Weak-model Checkpoint Simplification | 将 1% 自动触发、9 步 brainstorming、严格 TDD 等降级为明确检查点或指导原则。 | E3, E8 | high |
| M-SUP-033 | iOS-specific Verification Expansion | 将验证从测试扩展为 Flutter test、Flutter analyze、iOS release build 和发布检查。 | E4, E9, E13 | high |
| M-SUP-034 | External Tool Enforcement | 用 CI、linter、pre-commit hooks 替代模型自律。 | E6, E12, E15 | high |
| M-SUP-035 | Human Gate For High-risk Work | 高风险任务必须人工介入，包括架构、安全、签名、发布和 code review。 | E14 | high |
| M-SUP-036 | File-backed State Over Tool-backed Todo | 保留 todo 但改成文件级持久化，避免弱模型丢失工具状态。 | E3, E13 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| subagent_orchestration_failure | 彻底丢弃 subagent 驱动和 subagent review，改为主 session 顺序执行。 | E3, E6, E8 |
| tdd_waste_loop | 将“先写代码必须删除”从铁律降级为指导原则，避免弱模型重复删除重写。 | E3, E8 |
| skill_overtrigger_or_skip | 将 1% 规则替换为明确触发条件和 3-4 个检查点。 | E3, E8 |
| dot_context_noise | 删除 DOT 图，用简单有序列表替换。 | E3, E8 |
| worktree_ios_path_breakage | 在 iOS 场景禁用自动 worktree，改用 branch 或 in-place。 | E4, E6 |
| fake_verification | 用自动化工具强制验证，防止 agent 假装测试通过。 | E6, E12, E15 |
| pseudo_red_tdd | RED 阶段要求失败信息明确指向功能缺失，而不是 typo/import 错误。 | E6 |
| review_hallucination | 取消弱模型 subagent review，用 static analysis + 人工 review。 | E4, E6 |
| long_task_context_loss | 每 3 个 task 重新加载 plan 摘要，并使用文件级状态持久化。 | E6 |
| ios_build_gap | 增加 `flutter build ios --release`，避免 `flutter test` 通过但不可发布。 | E4 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 不整体迁移 | 强模型机制弱模型下失效 | 核心假设与执行者能力不匹配 | 会丢弃 Superpowers 的完整流程体系 |
| 外部验证替代自律 | 弱模型可能假装遵守规则 | 验证必须由不可伪造的命令/CI 提供 | 需要脚本和 CI 投入 |
| 串行执行替代 subagent | 弱模型协调 subagent 不可靠 | 减少跨上下文输入输出管理 | 降低并行效率 |
| 文件级 todo | 工具级 todo 在长会话中易丢失 | 文件更适合断点恢复和弱模型读取 | 手动更新成本更高 |
| 人工兜底高风险环节 | 弱模型质量判断不可靠 | 安全、发布、签名等错误成本高 | 人工介入增加等待时间 |

## 7. 5 Why Analysis

### Mechanism: External Tool Enforcement

- Why 1: 为什么不用更多规则监督弱模型？因为弱模型连监督规则本身也可能假装遵守。
- Why 2: 为什么验证要外部化？因为测试、lint、build、CI 输出比模型声明更可复验。
- Why 3: 为什么 Flutter/iOS 特别需要外部验证？因为 `flutter test` 不能覆盖 Xcode 构建、签名、pod 和 App Store 约束。
- Why 4: 为什么人工仍然需要？因为架构、安全和发布判断不只是命令成功，还涉及风险取舍。
- Why 5: 为什么这应进入清洗 Harness？因为后续机制库需要明确哪些 Superpowers 机制不应迁移，避免 Codex 复用高风险流程。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | TL;DR 判断强模型框架迁移到弱模型时约 60% 核心机制会失效或变形。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:3-7 | M-SUP-030 |
| E2 | 文件建议不要整体迁移，只提取约 30% 核心原则。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:7 | M-SUP-030 |
| E3 | 弱模型稳定性表逐项批评 subagent、TDD 铁律、1% 规则、DOT、Rigid/Flexible、Red Flags、TodoWrite、9 步 Brainstorming。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:13-25 | M-SUP-032 |
| E4 | Flutter/Firebase/iOS 冲突表指出 worktree、widget 测试、pubspec 检测、baseline test、gh PR、review 和 iOS 构建问题。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:26-37 | M-SUP-033 |
| E5 | 过度设计表批评 Spec+Plan、双阶段 review、Visual Companion、Finishing 4 选项、跨平台适配等。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:38-50 | M-SUP-031 |
| E6 | 真实失败模式表列出绕过 brainstorming、假装测试、伪 RED、review 幻觉、worktree 混乱、长任务上下文丢失、subagent 通信开销。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:51-62 | failure modes |
| E7 | 不适合迁移部分总结彻底丢弃、大幅简化、需要替换项。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:63-84 | M-SUP-031 |
| E8 | 风险矩阵将 subagent、skill 绕过、TDD 铁律、假验证、长任务上下文丢失等列为红色风险。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:86-101 | risks |
| E9 | 最大风险部分指出框架核心假设与弱模型能力不匹配。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:103-111 | M-SUP-030 |
| E10 | 需要人工兜底的环节包括架构、Xcode/iOS 配置、Firebase 安全规则、发布前验证、code review、测试覆盖判断、合并冲突。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:113-123 | M-SUP-035 |
| E11 | 渐进采用路径建议阶段 0-3，并永不采用 Visual Companion、DOT、跨平台适配层。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:125-154 | M-SUP-030 |
| E12 | 核心矛盾总结指出用更多规则监督不可靠 agent 会陷入“谁监督监督者”。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:156-171 | M-SUP-034 |
| E13 | 渐进采用路径要求保留文件级 todo，并在质量门阶段加入 flutter test 与 flutter build ios release。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:129-146 | M-SUP-033, M-SUP-036 |
| E14 | 人工兜底清单明确架构、iOS 配置、Firebase 安全规则、发布验证、code review、覆盖率判断和合并冲突必须人工介入。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:113-123 | M-SUP-035 |
| E15 | 轻量工作流和核心矛盾总结都要求用自动化验证、CI、linter、pre-commit 替代模型自律。 | raw/Kimi_Agent_Superpowers 体系探究/04_skeptic_review.md:135-140,156-171 | M-SUP-034 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Selective Principle Extraction | Goal Layer | AGENTS.md | v0_1 | State retained principles and rejected heavyweight mechanisms |
| Explicit Non-transfer List | Risk / Release Layer | docs/agent/DO_NOT_TRANSFER.md | v0_1 | Record mechanisms that must not enter iOS Harness defaults |
| Weak-model Checkpoint Simplification | Task Layer | docs/agent/TASKS.md | v0_1 | Replace probabilistic skill triggers with explicit task checkpoints |
| iOS-specific Verification Expansion | Feedback / Verification Layer | scripts/agent/verify-ios-build.sh | v0_5 | Require `flutter build ios --release` evidence |
| External Tool Enforcement | Feedback / Verification Layer | .github/workflows/ios-build.yml | v1_0 | Run validation outside model control |
| Human Gate For High-risk Work | Risk / Release Layer | docs/agent/RISK_GATE.md | v0_1 | Define human-required decisions |
| File-backed State Over Tool-backed Todo | Memory / State Layer | docs/agent/STATE.md | v0_1 | Persist progress and context to disk |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | Transfer warnings, risk gates, validation culture, and simplification strategy. |
| v0_1 | yes | DO_NOT_TRANSFER, RISK_GATE, STATE/TASKS, basic verification culture are immediate. |
| v0_5 | yes | Add Flutter/iOS verification scripts, static analysis, and plan reload checkpoints. |
| v1_0 | yes | CI/pre-commit enforcement belongs in mature harness. |
| no_transfer | yes | Explicitly reject subagent-driven development, Visual Companion, DOT diagrams, subagent review, broad cross-platform adapters as defaults. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Numeric estimates such as 60%, 40%, 70%, 50% are not backed by measurement data in this file | They are useful judgments but may be analytical estimates. | Treat as qualitative risk signals unless later sources provide empirical data. |
| Whether target model is still Composer2-level weak | The file names Composer2; actual user environment may be stronger. | Confirm target model class before final iOS Harness design. |
| Whether all “never adopt” items remain invalid if runtime supports enforcement | Some items may become viable with stronger runtime or tool-level enforcement. | Reassess during v1.0 design, but keep out of v0.1 defaults. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_001 | final report repeats many of these risk judgments |
| F_SUP_003 | explains the original design logic being critiqued |
| F_SUP_004 | migration design already applies many simplifications |
| F_SUP_012 | mobile-tdd skill should be checked against TDD downgrade warning |
| F_SUP_013 | root-cause-debugging can preserve useful process without subagents |

## 13. Clean Summary for Codex

这份文件是 Superpowers 清洗中最重要的风险来源。后续 Codex 不能只看 Superpowers 的设计优点，还必须把这里的“不迁移/降级迁移”作为约束：不要默认使用 subagent、worktree、DOT、双阶段 review、Visual Companion 和跨平台适配；不要依赖弱模型自律完成验证；不要让弱模型独立处理架构、安全、iOS 签名、Firebase 规则和 App Store 发布。iOS Harness 的 v0.1 应以文件级状态、明确检查点、人工风险门和外部验证为核心。
