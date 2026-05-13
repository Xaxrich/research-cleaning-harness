# Source Card: F_GSD_008 - report_stages_7_8_9

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_008 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/report_stages_7_8_9.md |
| file_type | markdown |
| topic | failure recovery, Git isolation, and verification gates |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把 GSD2 的卡住检测、失败恢复、Git/worktree 隔离和验证门机制迁移为 iOS Harness 的风险控制层。

## 3. File Summary

- Stage 7 定义 stuck loop 类型、重复尝试检测、根因分类、crash recovery 和 iOS failure handling。
- 文件强调两次失败后升级、blocker card 和 failure log 模板。
- Stage 8 讨论 work unit 对应 Git 隔离，比较 branch、worktree 和 none。
- 它定义并行 worktree、冲突避免、task-level commit、rollback、merge、弱模型 branch 和强模型 review branch。
- Stage 9 定义 verification gate、completion evidence、auto-fix retry、machine validation、status mapping 和 command constraints。
- 文件给出 iOS 脚本设计：doctor、analyze、test_fast、test_ui、build_ios_sim、build_ipa_check、firebase_check、privacy_check、release_candidate。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-055 | Stuck Loop Taxonomy | 将卡住分成多种类型，便于定位是环境、依赖、理解、工具还是验证问题。 | E1 | high |
| M-GSD-056 | Repeated Try Detection | 检测重复尝试，避免 agent 在同一错误上循环。 | E2 | high |
| M-GSD-057 | Failure Root Cause Classification | 对失败根因分类，驱动不同恢复策略。 | E3 | high |
| M-GSD-058 | Two-Failure Escalation and Blocker Card | 同类失败达到阈值后停止盲目重试并生成 blocker。 | E4 | high |
| M-GSD-059 | Work Unit Git Isolation | 根据任务风险选择 branch、worktree 或不隔离。 | E5 | high |
| M-GSD-060 | Task-Level Commit and Rollback | 以任务为粒度提交、回滚和合并。 | E6 | high |
| M-GSD-061 | Weak-Model Branch and Strong-Model Review | 让弱模型在隔离分支执行，强模型负责审查。 | E7 | medium |
| M-GSD-062 | Verification Evidence Gate | 完成状态必须有命令、日志或测试证据。 | E8 | high |
| M-GSD-063 | iOS Verification Script Matrix | 用一组 iOS 专用脚本覆盖环境、静态检查、测试、构建、发布和隐私风险。 | E9 | high |
| M-GSD-064 | Auto-Fix Retry Bound | 验证失败可自动修复，但重试次数必须受限。 | E10 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| stuck_loop | stuck taxonomy 和 repeated try detection 识别循环。 | E1 |
| blind_retry | 两次失败后升级 blocker，停止盲目修补。 | E4 |
| wrong_file_edit | Git/worktree 隔离降低误改主线风险。 | E5 |
| unrecoverable_change | task-level commit 和 rollback 提供恢复点。 | E6 |
| weak_model_damage | 弱模型隔离分支加上强模型 review 降低破坏面。 | E7 |
| false_completion | verification evidence gate 要求机器证据。 | E8 |
| release_risk | iOS 脚本矩阵覆盖发布与隐私检查。 | E9 |
| infinite_auto_fix | auto-fix retry bound 限制修复循环。 | E10 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 失败分类先于修复 | 避免乱改 | 不同失败类型需要不同处置路径 | 需要记录足够失败上下文 |
| Git 隔离按风险选择 | 降低主线污染 | 不是所有任务都值得开 worktree | 策略需要明确边界 |
| 验证矩阵脚本化 | 让完成可审计 | iOS 风险横跨测试、构建、发布和隐私 | 脚本维护成本较高 |

## 7. 5 Why Analysis

### Mechanism: Verification Evidence Gate

- Why 1: 因为 agent 常把“我修好了”当成完成。
- Why 2: iOS app 的正确性需要 build、test、analyze 或 release 检查证明。
- Why 3: 没有机器证据，review 无法区分真实完成和文本承诺。
- Why 4: 证据门迫使任务输出包含可复现命令。
- Why 5: 所以 iOS Harness 必须把验证证据作为状态转换条件。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Stage 7 列出多类 stuck loop。 | report_stages_7_8_9.md: stuck loop taxonomy | M-GSD-055 |
| E2 | Stage 7 讨论 repeated try detection。 | report_stages_7_8_9.md: repeated try detection section | M-GSD-056 |
| E3 | Stage 7 讨论 root cause classification。 | report_stages_7_8_9.md: root cause classification section | M-GSD-057 |
| E4 | Stage 7 包含两次失败升级和 blocker template。 | report_stages_7_8_9.md: escalation/blocker sections | M-GSD-058 |
| E5 | Stage 8 比较 branch、worktree 和 none。 | report_stages_7_8_9.md: Git isolation sections | M-GSD-059 |
| E6 | Stage 8 讨论 task-level commit、rollback 和 merge。 | report_stages_7_8_9.md: task commit/rollback sections | M-GSD-060 |
| E7 | Stage 8 讨论弱模型 branch 和强模型 review branch。 | report_stages_7_8_9.md: weak/strong model branch sections | M-GSD-061 |
| E8 | Stage 9 定义 verification evidence 和 completion gate。 | report_stages_7_8_9.md: verification gate sections | M-GSD-062 |
| E9 | Stage 9 列出 iOS verification scripts。 | report_stages_7_8_9.md: iOS script design sections | M-GSD-063 |
| E10 | Stage 9 讨论 auto-fix retry 和 command constraints。 | report_stages_7_8_9.md: auto-fix/constraints sections | M-GSD-064 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-055 | Feedback / Verification Layer | FAILURE_LOG.md | v0_1 | 记录 stuck 类型 |
| M-GSD-056 | Feedback / Verification Layer | scripts/agent/stuck_detector.sh | v0_5 | 检测重复错误和重复命令 |
| M-GSD-057 | Feedback / Verification Layer | FAILURE_LOG.md | v0_1 | 增加 root_cause 字段 |
| M-GSD-058 | Risk / Release Layer | BLOCKERS.md | v0_1 | 两次失败后升级 blocker |
| M-GSD-059 | Risk / Release Layer | GIT_WORKFLOW.md | v0_1 | 任务风险映射 branch/worktree/none |
| M-GSD-060 | Memory / State Layer | TASKS.md | v0_1 | 记录 task-level commit 和 rollback 点 |
| M-GSD-061 | Role / Review Layer | REVIEW_POLICY.md | v0_5 | 弱模型执行、强模型 review |
| M-GSD-062 | Feedback / Verification Layer | VERIFICATION_MATRIX.md | v0_1 | 完成状态必须有证据 |
| M-GSD-063 | Action / ACI Layer | scripts/agent/ios/ | v0_5 | 实现 iOS 验证脚本矩阵 |
| M-GSD-064 | Feedback / Verification Layer | FAILURE_LOG.md | v0_5 | 限制 auto-fix retry 次数 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | iOS Harness 必须具备失败、Git 和验证风险控制层 |
| v0_1 | yes | blocker、Git workflow 和验证证据门需要立即迁移 |
| v0_5 | yes | stuck detector 和 iOS 脚本矩阵可半自动化 |
| v1_0 | yes | 可作为 runtime 的任务状态转换和恢复策略 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| worktree 是否适合当前仓库 | 文件给的是策略，不知道用户 repo 分支工作流 | 查看当前 iOS 项目分支、CI 和依赖安装方式 |
| auto-fix retry 阈值是否固定为两次 | 源文档强调两次失败升级，但不同任务风险不同 | 在任务模板中允许 high-risk task 更早升级 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_011 | 失败恢复专项深入该文件 Stage 7 内容 |
| F_GSD_005 | 提供 failure log 和验证脚本模板 |
| F_GSD_004 | 将 Git/验证文件落入 iOS Harness 文件树 |
| F_SUP_011 | Superpowers verification-before-completion 可与验证门融合 |

## 13. Clean Summary for Codex

这个文件是 GSD2 风险控制层的主卡。它把失败恢复、Git 隔离和验证门连成一个闭环：先识别卡住和失败类型，再选择恢复或升级；高风险任务用 branch/worktree 隔离；完成前必须通过 iOS 验证脚本并保留证据。后续 iOS Harness v0.1 应迁移 `FAILURE_LOG.md`、`BLOCKERS.md`、`GIT_WORKFLOW.md` 和 `VERIFICATION_MATRIX.md`；v0.5 再实现 stuck detector 和 iOS 脚本矩阵。

