# Source Card: F_GSD_011 - research_failure_recovery

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_011 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/research_failure_recovery.md |
| file_type | markdown |
| topic | stuck loop detection, crash recovery, Git strategy, verification gates, and iOS recovery policies |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：系统化 GSD2 的失败恢复策略，覆盖卡住检测、crash recovery、Git 隔离、验证门和 iOS 失败类型处置。

## 3. File Summary

- 文件定义 stuck loop 类型和检测层级。
- 它讨论 Level 2 检测、artifact missing path、ADR-017 drift detection 和重试上限。
- 文件分析 crash recovery，包括 auto.lock、stale worker、unregistered milestone 以及持久化/不持久化边界。
- 它比较 Git worktree、branch 和 none，并覆盖并行 worktree、commit、rollback、merge。
- 文件强调 verification gate、must-haves、command execution、auto-fix 和 v2.82 verification blocking。
- 它提出 iOS failure recovery strategy，包含 11 类失败类型、两次失败升级、blocker card 和 Git strategy。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-081 | Multi-Level Stuck Detection | 按检测层级识别重复尝试和卡住状态。 | E1 | high |
| M-GSD-082 | Artifact Missing Path Detection | 把缺失产物路径作为失败信号。 | E2 | high |
| M-GSD-083 | Drift Detection | 使用 ADR-017 类型的 drift detection 识别任务偏离。 | E3 | medium |
| M-GSD-084 | Retry Cap Policy | 限制同类失败重试次数，避免无限循环。 | E4 | high |
| M-GSD-085 | Crash Recovery Boundary | 明确 auto.lock、stale worker、unregistered milestone 的恢复路径。 | E5 | high |
| M-GSD-086 | Persisted vs Non-Persisted State | 区分哪些状态必须持久化，哪些可以重建。 | E6 | high |
| M-GSD-087 | Git Isolation Decision Matrix | 用 worktree/branch/none 选择不同风险隔离方式。 | E7 | high |
| M-GSD-088 | Verification Blocking | 验证失败时阻止任务进入完成状态。 | E8 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| stuck_loop | 多层 stuck detection 和 retry cap 识别并限制循环。 | E1 |
| missing_artifact | artifact missing path detection 将“没有产物”作为失败。 | E2 |
| task_drift | drift detection 检查任务是否偏离原目标。 | E3 |
| crash_state_loss | crash recovery boundary 和持久化边界保证恢复。 | E5 |
| wrong_git_strategy | Git isolation decision matrix 防止过度或不足隔离。 | E7 |
| false_completion | verification blocking 阻止未验证任务完成。 | E8 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 检测层级 | 区分轻微失败和系统性卡住 | 不同层级对应不同升级动作 | 检测规则需要调参 |
| 持久化边界 | 支撑 crash recovery | 不是所有运行态都值得持久化 | 需要判断哪些状态可重建 |
| verification blocking | 保证完成可信 | 没有证据的完成会污染后续状态 | 可能让任务在环境问题上阻塞 |

## 7. 5 Why Analysis

### Mechanism: Verification Blocking

- Why 1: 因为失败任务如果被标记完成，会污染后续任务计划。
- Why 2: 后续 agent 会把错误完成状态当作事实。
- Why 3: iOS 构建和发布风险不能依赖自然语言确认。
- Why 4: verification blocking 将机器证据变成状态转换前置条件。
- Why 5: 所以 iOS Harness 应把验证失败保持为 blocked 或 review_needed，而不是 done。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件讨论 stuck loop types 和 detection levels。 | research_failure_recovery.md: stuck detection sections | M-GSD-081 |
| E2 | 文件包含 artifact missing path。 | research_failure_recovery.md: artifact missing path section | M-GSD-082 |
| E3 | 文件引用 ADR-017 drift detection。 | research_failure_recovery.md: drift detection section | M-GSD-083 |
| E4 | 文件讨论 cap=2 retry。 | research_failure_recovery.md: retry cap section | M-GSD-084 |
| E5 | 文件讨论 auto.lock、stale worker、unregistered milestone。 | research_failure_recovery.md: crash recovery sections | M-GSD-085 |
| E6 | 文件讨论 persistence include/exclude。 | research_failure_recovery.md: persistence boundary sections | M-GSD-086 |
| E7 | 文件比较 Git worktree、branch 和 none。 | research_failure_recovery.md: Git strategy sections | M-GSD-087 |
| E8 | 文件讨论 verification gate、must-haves 和 v2.82 verification blocking。 | research_failure_recovery.md: verification blocking sections | M-GSD-088 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-081 | Feedback / Verification Layer | scripts/agent/stuck_detector.sh | v0_5 | 根据重复错误和命令检测 stuck |
| M-GSD-082 | Feedback / Verification Layer | VERIFICATION_MATRIX.md | v0_1 | 将 expected_artifacts 写入验证条件 |
| M-GSD-083 | Risk / Release Layer | DECISIONS.md | v0_5 | 记录 task drift 检查规则 |
| M-GSD-084 | Feedback / Verification Layer | FAILURE_LOG.md | v0_1 | 每类失败记录 retry_count 和 cap |
| M-GSD-085 | Memory / State Layer | STATE.md | v0_5 | 记录 in_progress task 和恢复点 |
| M-GSD-086 | Memory / State Layer | STATE.md | v0_5 | 标注 persisted/rebuildable state |
| M-GSD-087 | Risk / Release Layer | GIT_WORKFLOW.md | v0_1 | 按风险选择 branch/worktree/none |
| M-GSD-088 | Feedback / Verification Layer | QUALITY_GATE.md | v0_1 | 验证失败禁止标记完成 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 失败恢复和验证阻断是 iOS Harness 稳定性的关键 |
| v0_1 | yes | retry cap、expected artifacts、Git strategy、verification blocking 立即迁移 |
| v0_5 | yes | stuck detector、crash recovery state 和 drift detection 可增强 |
| v1_0 | yes | 可与 runtime lease、command queue 结合 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Level 2 stuck detection 的具体阈值 | 源文件描述机制，实际阈值需项目校准 | 在清洗/开发任务中收集失败样本 |
| 11 类 iOS 失败类型是否完整 | 文件是迁移建议 | 与真实 iOS CI 和 App Store 失败记录对照 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_008 | Stage 7-9 概括同一失败/Git/验证机制 |
| F_GSD_009 | 架构层提供 worker/lease/crash recovery 支撑 |
| F_GSD_005 | 提供 failure log 和验证脚本模板 |
| F_SUP_012 | Superpowers verification-before-completion 可与 blocking 融合 |

## 13. Clean Summary for Codex

这个文件把 GSD2 的失败处理讲得最完整。对 iOS Harness 来说，最应该迁移的是 retry cap、expected artifacts、verification blocking、Git isolation matrix、stuck detector 和 blocker card。它还提醒后续 runtime 设计要区分“必须持久化的恢复状态”和“可重建的临时状态”。在与 SWE-agent 这种强调 tool/trajectory 的框架融合时，这张卡可以提供失败分类和状态转换策略。

