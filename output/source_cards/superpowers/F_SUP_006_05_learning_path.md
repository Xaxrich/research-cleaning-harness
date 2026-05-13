# Source Card: F_SUP_006 - Superpowers 框架 3 天精通学习路径

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_006 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md |
| file_type | markdown |
| topic | Superpowers 框架 3 天精通学习路径 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 Superpowers 的机制理解、SKILL.md 编写和 iOS Harness 迁移拆成三天训练路径，并给出产出模板和自测题。

## 3. File Summary

- 文件面向有 Flutter/Firebase/iOS 经验、想设计 Agent 流程的开发者。
- Day 1 要求理解四大核心机制、完整工作流，并用费曼技巧向团队解释。
- Day 2 要求解剖 SKILL.md，实战编写 Flutter TDD 和 Firebase Rules TDD skill。
- Day 3 要求分析 Superpowers 可迁移性，设计 iOS Harness skill 集合，并产出 HARNESS.md 和迁移报告。
- 文件把学习任务设计为阅读材料、理解问题、结构图、产出文件和自测问题的组合。
- 文件强调 description 应描述“何时使用”，Iron Law 使用 `NO X WITHOUT Y FIRST` 格式。
- 文件提供了 Flutter/Firebase 专用 skill 示例模板。
- 文件把最终学习结果转为可执行 Harness 规范、CI 示例和下一步行动。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-037 | Training Path As Harness Adoption | 用三天学习路线降低团队理解和采用 Superpowers/iOS Harness 的门槛。 | E1, E2 | medium |
| M-SUP-038 | Learning Task Template | 每个学习任务固定包含阅读材料、理解问题、结构图、产出文件、自测问题。 | E3, E4 | high |
| M-SUP-039 | Feynman Explanation Gate | 要求学习者用 30 秒、FAQ、团队对比图解释 Superpowers，验证理解深度。 | E5 | medium |
| M-SUP-040 | Skill Authoring Practice | 通过解剖 SKILL.md 和编写 Flutter/Firebase skills 学习 skill 结构。 | E6, E7 | high |
| M-SUP-041 | Migration Exercise Pipeline | 将可迁移性分析、skill 集合设计、HARNESS.md 规范和迁移报告串成练习。 | E8, E9 | high |
| M-SUP-042 | Self-test Based Quality Gate | 每个任务后用自测问题检查学习者是否真正掌握。 | E3, E10 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| shallow_framework_adoption | 通过解释、画图、自测和产出文件迫使学习者理解机制而不是复制文本。 | E3, E5, E10 |
| poorly_written_skill | 用 SKILL.md 解剖、description 规则、Iron Law 模式和实战模板规范 skill 编写。 | E6, E7 |
| missing_ios_mapping | Day 3 要求把 Superpowers 概念映射到 iOS Harness 等价物。 | E8 |
| no_onboarding_path | 三天路线提供从理解到实践再到迁移的 onboarding 顺序。 | E1, E2 |
| unverified_training_completion | 每个任务包含自测问题和具体产出文件。 | E3, E10 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 三天分层学习 | 先理解，再编写，再迁移 | 避免直接写 Harness 时只复制形式不理解机制 | 学习路径不适合直接作为运行时规则 |
| 每任务固定模板 | 学习者知道每步要产出什么 | 将抽象方法论转成可检查资产 | 文档产出较多 |
| 费曼技巧 | 要求能向团队解释 | 语言复述暴露理解漏洞 | 依赖人工判断解释质量 |
| 实战写 skill | 从读转向做 | Skill 编写能力需要练习和自测 | 示例可能仍需真实项目验证 |

## 7. 5 Why Analysis

### Mechanism: Learning Task Template

- Why 1: 为什么学习任务要固定结构？因为学习者需要明确输入、问题、图示、产出和自测。
- Why 2: 为什么要有产出文件？因为只阅读无法成为可复用团队资产。
- Why 3: 为什么要画结构图？因为 Superpowers 是流程/机制系统，单纯文字容易误解连接关系。
- Why 4: 为什么要自测？因为学习完成声明需要可检查信号。
- Why 5: 为什么这对 iOS Harness 有价值？因为后续团队需要 onboarding 文档来理解为何要遵守 Harness，而不是只看到一堆规则。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件目标是理解 Superpowers 设计哲学、独立编写 SKILL.md、迁移到 Flutter + Firebase iOS Harness。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:1-5 | M-SUP-037 |
| E2 | Day 1 目标是解释四大核心机制并画完整工作流图。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:9-17 | M-SUP-037 |
| E3 | Day 1 Task 1 包含阅读材料、理解问题、结构图、产出文件、自测问题。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:17-79 | M-SUP-038 |
| E4 | Day 1 Task 2 使用同样结构拆解完整工作流。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:81-154 | M-SUP-038 |
| E5 | Day 1 Task 3 要求用费曼技巧、30 秒电梯演讲、FAQ、团队风险评估解释。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:156-233 | M-SUP-039 |
| E6 | Day 2 Task 4 解剖 SKILL.md 标准结构、frontmatter、Iron Law 和 CSO。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:241-341 | M-SUP-040 |
| E7 | Day 2 Task 5/6 要求编写 Flutter TDD 和 Firebase Rules TDD skill。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:343-612 | M-SUP-040 |
| E8 | Day 3 Task 7 要求分析 Superpowers 到 iOS Harness 的迁移映射。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:621-702 | M-SUP-041 |
| E9 | Day 3 Task 8/9 要求设计 iOS skill 集合、HARNESS.md 和迁移报告。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:704-927 | M-SUP-041 |
| E10 | 文件几乎每个任务都提供自测问题，作为学习质量检查。 | raw/Kimi_Agent_Superpowers 体系探究/05_learning_path.md:65-79,140-154,919-927 | M-SUP-042 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Training Path As Harness Adoption | Harness Maintenance Layer | docs/agent/ONBOARDING.md | v0_5 | Turn the three-day learning path into team onboarding |
| Learning Task Template | Task Layer | templates/training_task_template.md | v0_5 | Reuse structure for future harness training exercises |
| Feynman Explanation Gate | Role / Review Layer | docs/agent/REVIEW_GUIDE.md | v0_5 | Ask reviewers to check whether contributors can explain mechanism intent |
| Skill Authoring Practice | Harness Maintenance Layer | docs/agent/SKILL_AUTHORING.md | v0_5 | Capture SKILL.md structure and description/Iron Law rules |
| Migration Exercise Pipeline | Harness Maintenance Layer | output/ios_harness_mapping/codex_handoff.md | v1_0 | Use as later handoff training section |
| Self-test Based Quality Gate | Feedback / Verification Layer | templates/review_template.md | v0_5 | Add self-test prompts for training artifacts |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | Valuable for onboarding and skill-authoring, not for runtime execution. |
| v0_1 | no | Current harness needs source cards first; onboarding can wait. |
| v0_5 | yes | Add ONBOARDING, SKILL_AUTHORING, and training templates after mechanism library stabilizes. |
| v1_0 | yes | Include training path in Codex handoff pack for team adoption. |
| no_transfer | yes | Do not treat the learning exercises as authoritative source evidence for runtime mechanisms. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether the three-day workload is realistic | The file proposes time estimates but gives no learning outcome data. | Pilot with a developer and record completion time. |
| Whether sample skills are production-ready | They are learning outputs, not reviewed runtime skills. | Compare with actual F_SUP_011-F_SUP_013 skill files and run review. |
| Whether team onboarding belongs in v0.5 or v1.0 | Depends on whether the immediate goal is solo research cleaning or team rollout. | Decide after source-card and synthesis phases. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_002 | anatomy report supplies learning content for Day 1 |
| F_SUP_003 | design logic supplies 5 Why and mechanism explanations |
| F_SUP_004 | migration design overlaps with Day 3 outputs |
| F_SUP_011 | app-store-release real skill should be compared to learning templates |
| F_SUP_012 | mobile-tdd real skill should be compared to learning templates |

## 13. Clean Summary for Codex

这份文件不应直接决定 iOS Harness 的运行机制，但它对后续团队采用非常有价值。它提供了一个从“理解机制”到“编写 skill”再到“迁移 Harness”的训练生产线。Codex 后续可以把它转成 `docs/agent/ONBOARDING.md`、`docs/agent/SKILL_AUTHORING.md` 和训练任务模板，帮助团队理解为什么 Harness 要有 source cards、质量门、验证证据和迁移映射。当前清洗阶段只需保留其学习机制，不把示例 skill 当作最终实现。
