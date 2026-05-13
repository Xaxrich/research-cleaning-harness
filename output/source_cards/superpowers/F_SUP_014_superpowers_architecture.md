# Source Card: F_SUP_014 - superpowers_architecture.png

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_014 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/superpowers_architecture.png |
| file_type | image |
| topic | architecture diagram |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：用分层架构图展示 Superpowers 如何把用户目标逐层推进到需求澄清、计划、任务拆解、TDD、实现、调试、review、完成验证和规则沉淀。

## 3. File Summary

- 图片标题是 “Superpowers 框架分层架构图”，副标题描述从聊天到工程流程的完整设计逻辑。
- 图中从第 0 层到第 9 层纵向排列，蓝色箭头表示从上一层进入下一层。
- 每一层左侧是阶段名称和问题/做法，右侧绿色框是 Superpowers 机制或对应 skill。
- 第 0 层是用户目标，强调自然语言模糊和隐含假设。
- 第 1-3 层是 brainstorming、writing-plans、bite-sized tasks。
- 第 4-8 层覆盖 TDD、实现、systematic debugging、code review、verification/completion。
- 第 9 层是 meta-level 规则沉淀，包含 skill 自动触发、指令优先级和 1% 调用规则。
- 底部总结核心设计哲学：流程约束大于 agent 自由意志、上下文隔离、长会话、验证闭环、信任声明、自动触发等。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-093 | Layered Workflow Diagram | 用 0-9 层展示 Superpowers 从目标到交付再到规则沉淀的质量门链条。 | E1, E2 | high |
| M-SUP-094 | Skill-triggered Stage Transitions | 每层右侧标出 description 触发或对应 skill，说明阶段推进由机制触发。 | E3 | high |
| M-SUP-095 | Quality Gate Ladder | 每一层都包含禁止项或铁律，将下一步行动限制在通过当前门后。 | E4 | high |
| M-SUP-096 | Meta-level Rule Consolidation | 第 9 层把自动触发、指令优先级和 1% 规则作为规则沉淀层。 | E5 | high |
| M-SUP-097 | Visual Mechanism Map | 将抽象机制与具体 skill 名称对齐，便于团队沟通。 | E6 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| process_order_confusion | 用纵向层级和箭头说明从需求到完成的顺序。 | E1, E2 |
| skipped_gate | 多层绿色机制框标注禁止直接编码、禁止无测试、禁止无根因、禁止无验证。 | E4 |
| unclear_skill_mapping | 每层右侧写明关联 skill，例如 brainstorming、writing-plans、test-driven-development、systematic-debugging。 | E3 |
| weak_team_understanding | 视觉图把文字机制转成一页结构图，帮助解释复杂流程。 | E6 |
| context_pollution | 图中明确 subagent 不继承会话历史、reviewer subagent 隔离等机制。 | E3, E4 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 纵向层级图 | 表示流程推进方向 | 把每个阶段看成质量门 | 图很高，移动端阅读不便 |
| 左侧阶段/右侧机制 | 同时展示工作内容和约束机制 | 让“做什么”和“为何不能跳过”对齐 | 右侧文字部分较密 |
| 底部哲学总结 | 提炼全图主旨 | 让读者记住设计原则而非单个 skill | 不提供具体执行模板 |

## 7. 5 Why Analysis

### Mechanism: Layered Workflow Diagram

- Why 1: 为什么需要图？因为 Superpowers 的流程链比单个 skill 更重要。
- Why 2: 为什么要分层？因为每个阶段解决不同失败模式。
- Why 3: 为什么要标 skill？因为团队需要知道每一层由哪个机制触发。
- Why 4: 为什么要显示禁止项？因为 Superpowers 的价值来自防止跳过质量门。
- Why 5: 为什么这对 iOS Harness 有价值？因为后续可以把图转成 `WORKFLOW_CHAIN.md`，帮助 Codex 和人类理解执行顺序。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 图片标题为 Superpowers 框架分层架构图，展示从聊天到工程流程的设计逻辑。 | raw/Kimi_Agent_Superpowers 体系探究/superpowers_architecture.png: title area | M-SUP-093 |
| E2 | 图中纵向列出第 0 层用户目标到第 9 层 Harness 规则沉淀。 | raw/Kimi_Agent_Superpowers 体系探究/superpowers_architecture.png: full vertical layers | M-SUP-093 |
| E3 | 右侧绿色机制框标注 brainstorming、writing-plans、test-driven-development、systematic-debugging、review、verification 等 skill。 | raw/Kimi_Agent_Superpowers 体系探究/superpowers_architecture.png: right mechanism boxes | M-SUP-094 |
| E4 | 图中多处写明禁止直接跳到代码、禁止写代码/搭建项目/采取实现、没有测试失败则删除重写、禁止无根因修复、禁止未验证声明。 | raw/Kimi_Agent_Superpowers 体系探究/superpowers_architecture.png: layers 1-8 | M-SUP-095 |
| E5 | 第 9 层列出 skills 自动触发、指令优先级和 1% 可能也必须调用 skill。 | raw/Kimi_Agent_Superpowers 体系探究/superpowers_architecture.png: layer 9 | M-SUP-096 |
| E6 | 底部总结核心设计哲学，包括流程约束大于自由意志、上下文隔离、验证闭环、自动触发等。 | raw/Kimi_Agent_Superpowers 体系探究/superpowers_architecture.png: bottom summary | M-SUP-097 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Layered Workflow Diagram | Harness Maintenance Layer | docs/agent/WORKFLOW_CHAIN.md | v0_5 | Convert image into text workflow for Codex-readable handoff |
| Skill-triggered Stage Transitions | Context Layer | AGENTS.md | v0_5 | Summarize stage-to-skill mapping |
| Quality Gate Ladder | Feedback / Verification Layer | QUALITY_GATE.md | v0_5 | Align each phase with a gate |
| Meta-level Rule Consolidation | Goal Layer | AGENTS.md | v0_1 | Preserve rule priority and entry discipline |
| Visual Mechanism Map | Harness Maintenance Layer | output/ios_harness_mapping/codex_handoff.md | v1_0 | Include as optional human-facing appendix |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | partial | Use diagram to derive workflow docs; do not rely on image as primary Codex input. |
| v0_1 | partial | Preserve only core stage order and rule priority in AGENTS. |
| v0_5 | yes | Convert to text `WORKFLOW_CHAIN.md` after source cards are reviewed. |
| v1_0 | yes | Include visual appendix in handoff pack for humans. |
| no_transfer | yes | Do not require Codex to inspect image during normal execution. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Some right-side text is visually dense | Image text is readable but not as robust as raw Markdown. | Prefer F_SUP_003 as authoritative text source for layer details. |
| Diagram reflects original Superpowers strict flow | F_SUP_005 says strict flow may not transfer to weak-model iOS. | Use diagram as conceptual map, not final iOS workflow. |
| Image should not be primary model context | Models may parse images inconsistently. | Convert important content to text synthesis. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_003 | text version of layered design logic |
| F_SUP_002 | structural anatomy supporting skill mapping |
| F_SUP_005 | critique constraining strict transfer |

## 13. Clean Summary for Codex

这张图是 Superpowers 工作流的视觉索引。它把用户目标、需求澄清、计划、任务拆解、TDD、实现、调试、review、完成验证和规则沉淀放在一条纵向质量门链上。它的价值在于帮助后续 synthesis 生成 `WORKFLOW_CHAIN.md`，但不应要求 Codex 在执行时依赖图片理解机制。真正的机制细节应以 F_SUP_003 等文本 Source Card 为准，F_SUP_014 主要作为人类沟通和交叉验证材料。
