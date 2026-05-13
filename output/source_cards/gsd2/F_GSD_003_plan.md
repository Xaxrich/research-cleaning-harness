# Source Card: F_GSD_003 - plan

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_003 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/plan.md |
| file_type | markdown |
| topic | staged research and delivery plan for GSD2 migration |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把 GSD2 到 iOS Harness 的研究任务拆成可执行阶段，并规定资料收集、深度研究、报告撰写、交付生成和质量标准。

## 3. File Summary

- 文件定义了 GSD2 深度研究到 iOS Harness 迁移的阶段化计划。
- Stage 1 聚焦资料收集和 Skill 加载。
- Stage 2 以 research_architecture、research_context、research_model_routing、research_failure_recovery 四类研究为核心。
- Stage 3 产出多段 report_stages 文件，逐步覆盖架构、任务、上下文、路由、恢复、Git、验证和迁移。
- Stage 4 生成 iOS Harness 迁移蓝图和可交付清单。
- Stage 5 格式化最终交付物。
- 文件给出了质量标准：理解 GSD2 核心、结合 Superpowers、产出可执行迁移方案。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-016 | Staged Research Pipeline | 将调研拆成资料收集、深度研究、报告撰写、交付物生成和格式化交付。 | E1 | high |
| M-GSD-017 | Research Topic Partition | 用 architecture/context/model_routing/failure_recovery 四个研究文件分离复杂主题。 | E2 | high |
| M-GSD-018 | Report Stage Projection | 把研究结果按 stage 投影为多份报告，降低单文件上下文压力。 | E3 | high |
| M-GSD-019 | Skill Loading Plan | 在研究阶段显式加载 Superpowers 相关 skill，保证比较基准稳定。 | E4 | high |
| M-GSD-020 | Quality Criteria Before Migration | 在计划中先定义理解、融合、方案完整性和质量要求，再进入生成。 | E5 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| unbounded_research | 用阶段和交付物约束研究范围。 | E1 |
| topic_mixing | 将架构、上下文、模型路由和失败恢复拆成独立研究文件。 | E2 |
| context_overload | 通过分 stage 报告承载结果，避免一次性生成超长报告。 | E3 |
| inconsistent_baseline | 明确加载 Superpowers skill，使 GSD2 比较基准可追溯。 | E4 |
| weak_final_output | 先定义质量标准，减少只堆材料没有迁移方案的风险。 | E5 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 分阶段研究 | 让任务可推进 | 把“调研一个框架”变成可审计流水线 | 需要维护多个中间文件 |
| 四类研究主题 | 覆盖 GSD2 核心能力 | 架构、上下文、路由和恢复是迁移 iOS Harness 的主要控制面 | 可能遗漏 UI/产品层信息 |
| stage 报告 | 避免报告生成过长 | 让后续 Source Card 可以按文件独立清洗 | 跨 stage 需要去重 |

## 7. 5 Why Analysis

### Mechanism: Staged Research Pipeline

- Why 1: 因为 GSD2 涉及 runtime、状态、上下文、模型和恢复多个系统面。
- Why 2: 单次总结容易混淆事实、推断和迁移建议。
- Why 3: 分阶段可以让每个输出承担一个明确角色。
- Why 4: 明确角色后，Source Card 能追溯到具体阶段产物。
- Why 5: 因此 iOS Harness 融合时可以按机制选择，而不是按整份报告照搬。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件列出 Stage 1 到 Stage 5 的研究流程。 | plan.md:3-35 | M-GSD-016 |
| E2 | Stage 2 明确产出四个 research_*.md 文件。 | plan.md:10-17 | M-GSD-017 |
| E3 | Stage 3 将报告拆成 report_stages_1_2_3、4_5_6、7_8_9、10_11、12_13_14。 | plan.md:18-27 | M-GSD-018 |
| E4 | Skill 加载计划包含 Superpowers 相关 skill。 | plan.md:37-42 | M-GSD-019 |
| E5 | 质量标准要求理解 GSD2、结合 Superpowers、产出完整迁移方案。 | plan.md:44-49 | M-GSD-020 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-016 | Task Layer | TASKS.md | v0_1 | 将 research、source_card、review、synthesis 作为分阶段任务 |
| M-GSD-017 | Context Layer | CONTEXT_RULES.md | v0_1 | 按研究主题限制每次读取的上下文 |
| M-GSD-018 | Memory / State Layer | output/frameworks/gsd2_summary.md | v0_5 | 用 stage 投影组织框架级合成 |
| M-GSD-019 | Role / Review Layer | AGENTS.md | v0_1 | 记录不同框架比较时必须加载的基准规则 |
| M-GSD-020 | Feedback / Verification Layer | QUALITY_GATE.md | v0_1 | 把质量标准转为验收条件 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 这是研究清洗和后续框架融合的流程骨架 |
| v0_1 | yes | 需要立即用于任务拆分和质量门 |
| v0_5 | yes | 可扩展为自动生成 stage summary |
| v1_0 | yes | 可成为 runtime 中 research pipeline 的状态机 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 计划是否完全按顺序执行 | plan 文件只描述计划，不证明执行结果 | 对照所有 report_stages 和 research 文件是否存在且内容匹配 |
| Skill 加载是否影响实际输出 | 文件只列出加载计划 | 查看生成报告中是否实际体现 Superpowers 对比 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_004 | 对应 Stage 10-11 报告产物 |
| F_GSD_005 | 对应 Stage 12-14 报告产物 |
| F_GSD_009 | 对应 architecture research 产物 |
| F_GSD_010 | 对应 context research 产物 |
| F_GSD_011 | 对应 failure recovery research 产物 |
| F_GSD_012 | 对应 model routing research 产物 |

## 13. Clean Summary for Codex

这个文件为 iOS Harness 后续融合提供了“研究任务也要被 harness 化”的证据。它把调研拆成可检查的阶段、主题文件和报告投影，正好对应当前 Research Cleaning Harness 的做法：先 inventory，再逐文件 card，再 review，再合成。后续 Codex 构建 iOS App Harness 时，可以把该机制迁移为 `TASKS.md` 中的阶段字段、`CONTEXT_RULES.md` 的主题隔离规则和 `QUALITY_GATE.md` 的验收标准，避免框架调研变成不可追溯的大段总结。

