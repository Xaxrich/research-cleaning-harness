# Source Card: F_SUP_003 - Superpowers 框架设计逻辑深度分析报告

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_003 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md |
| file_type | markdown |
| topic | Superpowers 框架设计逻辑深度分析报告 |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：解释 Superpowers 为什么要用强制触发、隔离、验证、review 分离和质量门来对抗 LLM 的默认失效模式。

## 3. File Summary

- 文件把 Superpowers 定义为流程约束框架和软件工程纪律系统。
- 它将核心机制概括为强制触发、上下文隔离、验证闭环和审查分离。
- 它解释了三层流程约束：description 自动触发、Iron Law 禁止危险行为、理性化预防表封死借口。
- 它将任务拆成 Plan、Task、Step，并说明 2-5 分钟步骤粒度的理由。
- 它把 Worktree、Subagent、Reviewer 解释为三重隔离。
- 它把 TDD、Code Review、Verification Before Completion 解释为三级验证链。
- 它用 5 Why 说明 skills、plan-first、TDD、code review、worktree 和 subagent 的根因。
- 它把 Superpowers 放在流程编排层，位于具体执行工具之上。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-014 | Three-layer Process Constraint | 通过触发层、禁止层、认知层叠加约束 agent 行为。 | E2, E3 | high |
| M-SUP-015 | Plan Task Step Decomposition | 用 Plan→Task→Step 三层分解和 2-5 分钟步骤降低执行歧义。 | E4 | high |
| M-SUP-016 | Triple Isolation Strategy | 通过 worktree、subagent、reviewer 隔离保护文件系统、上下文窗口和评估视角。 | E5 | high |
| M-SUP-017 | Three-level Verification Chain | 用 TDD、两阶段 review、完成前验证覆盖实现、集成和交付三段风险。 | E7 | high |
| M-SUP-018 | Completion Gate Function | 完成声明必须经过 IDENTIFY→RUN→READ→VERIFY→THEN CLAIM。 | E8 | high |
| M-SUP-019 | Reviewer Implementer Separation | reviewer 不继承 implementer 的思考过程，只看描述、需求和 diff。 | E9 | high |
| M-SUP-020 | Process Orchestration Layer | Superpowers 不直接编码，而是决定何时做什么以及完成标准。 | E10 | medium |
| M-SUP-021 | Quality Gate Layering | 每一层都是质量门，前进必须通过当前层检查。 | E11 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| context_pollution | Fresh subagent、reviewer 隔离和 worktree 物理隔离减少上下文和文件污染。 | E5 |
| skipped_process | 三层约束和 1% 触发规则防止 agent 以“简单”为由绕过流程。 | E2, E3 |
| vague_task_execution | Plan→Task→Step 和执行者画像强迫消除隐含假设。 | E4 |
| no_test_completion | 完成门函数禁止无新鲜验证证据的完成声明。 | E8 |
| local_optimum_code | code review 被解释为对抗实现者局部最优的机制。 | E12 |
| hindsight_test_bias | TDD 被解释为期望和实现的认知解耦。 | E12 |
| weak_attention_decay | subagent/fresh context 被解释为长任务中保持流程约束注意力的策略。 | E12 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| Iron Law 句式 | 用绝对语言禁止危险行为 | 消除灰色地带和模型自我合理化空间 | 弱模型可能僵硬执行，需要 iOS 场景降级 |
| Plan-first | 先完成思考再行动 | 对抗自回归模型承诺升级和探索式开发 | 简单任务会增加前置成本 |
| TDD-first | 保证测试独立于实现 | 防止测试共享实现中的隐含假设 | 移动端测试启动慢时需要调整粒度 |
| Reviewer/Implementer 分离 | 引入独立评估视角 | 对抗确认偏见、锚定和沉没成本 | 需要 subagent 或等效 review 容器 |
| Fresh context | 每个任务重新构造上下文 | 对抗长上下文注意力稀释 | 需要 controller 维护跨任务知识 |

## 7. 5 Why Analysis

### Mechanism: Plan Task Step Decomposition

- Why 1: 为什么要先 plan？因为直接写代码会导致探索式开发和混乱产出。
- Why 2: 为什么探索式开发对 LLM 更危险？因为一旦生成代码，自回归模型会倾向维护先前假设。
- Why 3: 为什么 task 还要拆成 step？因为 2-5 分钟步骤能让进度可追踪、错误可定位。
- Why 4: 为什么要假设执行者没有上下文和判断？因为这迫使 plan 消除隐含前提。
- Why 5: 为什么这对 iOS Harness 有价值？因为后续弱模型可以只执行窄任务，不需要在大上下文里自行恢复目标。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件核心结论称 Superpowers 是面向 AI Agent 的软件工程纪律系统。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:1-7 | essence |
| E2 | 文件列出四个核心机制：强制触发、上下文隔离、验证闭环、审查分离。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:9-24 | M-SUP-014 |
| E3 | 流程约束被拆成 skill trigger、Iron Law、理性化预防三层。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:31-80 | M-SUP-014 |
| E4 | 任务分解被定义为 Plan、Task、Step 三级，步骤粒度为 2-5 分钟。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:83-127 | M-SUP-015 |
| E5 | 上下文节省使用 Worktree、Subagent、Reviewer 三重隔离。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:129-187 | M-SUP-016 |
| E6 | 行为触发被定义为声明式触发，description 即 trigger。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:189-233 | M-SUP-014 |
| E7 | 验证闭环被定义为 TDD、Code Review、Verification Before Completion 三级链。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:235-282 | M-SUP-017 |
| E8 | 完成声明门函数为 IDENTIFY、RUN、READ、VERIFY、THEN CLAIM。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:331-374 | M-SUP-018 |
| E9 | reviewer/implementer 分离依赖 subagent 边界、精确上下文注入和多角色模板。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:376-439 | M-SUP-019 |
| E10 | Superpowers 被定位为流程编排层，位于执行工具和代码操作工具之上。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:491-539 | M-SUP-020 |
| E11 | 分层架构把每一层定义为质量门，前进必须通过检查。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:733-818 | M-SUP-021 |
| E12 | 5 Why 部分解释了 skills、plan-first、TDD、code review、worktree、subagent 的根因。 | raw/Kimi_Agent_Superpowers 体系探究/02_superpowers_design_logic.md:541-731 | design logic |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Three-layer Process Constraint | Goal Layer | AGENTS.md | v0_1 | Add concise non-negotiable rules and rationalization-prevention checks |
| Plan Task Step Decomposition | Task Layer | docs/agent/TASKS.md | v0_1 | Require each task to name source_id, allowed_read, allowed_write, acceptance |
| Triple Isolation Strategy | Context Layer | docs/agent/CONTEXT_RULES.md | v0_1 | Replace worktree/subagent assumptions with one-file-at-a-time context constraints |
| Three-level Verification Chain | Feedback / Verification Layer | QUALITY_GATE.md | v0_1 | Encode card/review/synthesis gates |
| Completion Gate Function | Feedback / Verification Layer | scripts/agent/verify-harness-output.sh | v0_5 | Require validators before claiming cleaning completion |
| Reviewer Implementer Separation | Role / Review Layer | templates/review_template.md | v0_1 | Separate Source Reader output from Reviewer judgment |
| Process Orchestration Layer | Harness Maintenance Layer | docs/agent/WORKFLOW_CHAIN.md | v0_5 | Document how cleaning phases progress |
| Quality Gate Layering | Risk / Release Layer | docs/agent/RISK_GATE.md | v0_5 | Define which outputs can feed synthesis |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | This file explains reusable design mechanisms for the cleaning harness itself. |
| v0_1 | yes | One-file tasks, source card review, quality gates, and context rules are immediate. |
| v0_5 | yes | Add automated validators and workflow-chain docs. |
| v1_0 | partial | Runtime enforcement of allowed_read/allowed_write is useful but can wait. |
| no_transfer | yes | Do not transfer rigid worktree/subagent assumptions directly to weak-model iOS workflow. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Whether all Iron Law rigidity transfers to Flutter/iOS work | This design logic file argues for rigidity generally, but does not specialize mobile constraints. | Compare F_SUP_004 and F_SUP_005. |
| Whether subagent separation is available in the target harness runtime | File assumes subagent architecture as key mechanism. | Confirm Codex/iOS runtime capabilities and weak-model policy. |
| Whether worktree isolation is safe for Xcode/iOS projects | File defends worktree generally, but iOS path/signing constraints may differ. | Check F_SUP_005 and later iOS mapping. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_001 | summary report that downgrades some mechanisms for weak models |
| F_SUP_002 | structural anatomy for the mechanisms explained here |
| F_SUP_004 | iOS migration design that should adapt these mechanisms |
| F_SUP_005 | skeptic review that should challenge transfer assumptions |

## 13. Clean Summary for Codex

这份文件给后续 iOS Harness 的最大价值，是把 Superpowers 的“为什么”讲清楚：skills 是注意力管理系统，plan-first 是对抗自回归承诺升级，TDD 是认知解耦，review 是对抗局部最优，verification 是完成声明的证据门。清洗 Harness 自身已经可以直接采用这些机制：一文件一任务、Source Reader/Reviewer 分离、质量门、状态文件和验证脚本。迁移到 iOS App Harness 时，应保留这些机制背后的目标，但对 worktree、subagent 和严格 TDD 做移动端适配。
