# Source Card: F_GSD_010 - research_context

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_GSD_010 |
| framework | gsd2 |
| raw_path | raw/Kimi_Agent_多 Agent GSD2/research_context.md |
| file_type | markdown |
| topic | context rot, fresh sessions, context injection, token profiles, and weak model context |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：解释 GSD2 如何对抗 context rot，并把上下文选择、压缩、排除和弱模型适配设计成任务级机制。

## 3. File Summary

- 文件分析 context rot 的表现、失败模式和根因。
- 它提出 one task per context window、fresh session、context reset 和 context injection。
- 它强调 pre-inlined injection 与 excluded contexts，避免污染。
- 文件讨论 summaries、projection 和 database 如何替代长聊天历史。
- 它给出 budget/balanced/quality token profiles、compression 和 complexity-based routing。
- 文件比较 GSD2 与 Aider Repo Map，并分析弱模型上下文管理。
- 它提出 iOS context injection 场景和 priority framework。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-GSD-073 | Context Rot Failure Taxonomy | 识别上下文腐烂的表现和根因。 | E1 | high |
| M-GSD-074 | One Task per Context Window | 每个任务使用独立上下文窗口，减少跨任务污染。 | E2 | high |
| M-GSD-075 | Fresh Session and Context Reset | 开新会话并重置旧上下文。 | E3 | high |
| M-GSD-076 | Pre-Inlined Context Injection | 在任务开始前预先注入必要材料。 | E4 | high |
| M-GSD-077 | Excluded Contexts | 明确不应注入的文件、历史或噪声。 | E5 | high |
| M-GSD-078 | Summary Projection over Chat History | 用 summary、projection 和 database 替代完整聊天历史。 | E6 | high |
| M-GSD-079 | Token Profiles | 通过 budget/balanced/quality profile 控制上下文长度与信息密度。 | E7 | high |
| M-GSD-080 | iOS Context Priority Framework | 将 iOS 场景映射到上下文注入优先级。 | E8 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| context_pollution | fresh session、context reset 和 excluded contexts 控制污染源。 | E3 |
| weak_model_confusion | one task per window 与 token profiles 降低噪声。 | E2 |
| stale_decision_reuse | summary/projection/database 替代旧聊天历史。 | E6 |
| token_overflow | token profiles 和 compression 控制上下文预算。 | E7 |
| missing_relevant_context | pre-inlined injection 确保任务开始前已有必要材料。 | E4 |
| poor_ios_task_context | iOS context priority framework 让不同开发场景读取不同材料。 | E8 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 一个任务一个上下文窗口 | 降低污染 | agent 的注意力应绑定当前任务，而不是整个项目历史 | 跨任务连续性需要 STATE/summary 承接 |
| excluded contexts | 防止噪声进入 | 明确“不读什么”与“读什么”同样重要 | 需要维护排除列表 |
| token profiles | 控制成本和质量 | 不同复杂度任务需要不同上下文密度 | 需要复杂度判断 |

## 7. 5 Why Analysis

### Mechanism: Excluded Contexts

- Why 1: 因为 agent 往往倾向多读文件。
- Why 2: 多读不相关材料会稀释任务注意力。
- Why 3: 被污染的上下文会导致旧方案、旧路径或错误假设被复用。
- Why 4: 只规定 allowed context 仍可能留下模糊边界。
- Why 5: 所以 iOS Harness 应同时维护 allowed_context 和 forbidden_context。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | 文件分析 context rot 的 failure modes 和 root causes。 | research_context.md: context rot sections | M-GSD-073 |
| E2 | 文件提出 one task per context window。 | research_context.md: context window section | M-GSD-074 |
| E3 | 文件讨论 fresh session 和 context reset。 | research_context.md: fresh/reset sections | M-GSD-075 |
| E4 | 文件讨论 pre-inlined injection。 | research_context.md: injection sections | M-GSD-076 |
| E5 | 文件讨论 excluded contexts。 | research_context.md: excluded context section | M-GSD-077 |
| E6 | 文件讨论 summaries、projection、database 替代 chat history。 | research_context.md: summary/projection/database sections | M-GSD-078 |
| E7 | 文件讨论 budget/balanced/quality token profiles 与 compression。 | research_context.md: token profile sections | M-GSD-079 |
| E8 | 文件讨论 iOS context injection scenarios 和 priority framework。 | research_context.md: iOS context sections | M-GSD-080 |

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| M-GSD-073 | Context Layer | docs/agent/CONTEXT_ROT.md | v0_5 | 记录上下文腐烂类型 |
| M-GSD-074 | Context Layer | CONTEXT_RULES.md | v0_1 | 每个 task 使用独立 context 包 |
| M-GSD-075 | Context Layer | AGENTS.md | v0_1 | 要求新任务先重建上下文 |
| M-GSD-076 | Context Layer | CONTEXT_INDEX.md | v0_1 | 任务开始前列出必须注入文件 |
| M-GSD-077 | Context Layer | CONTEXT_RULES.md | v0_1 | 增加 forbidden_context 字段 |
| M-GSD-078 | Memory / State Layer | STATE.md | v0_1 | 用 summary/state 承接跨任务信息 |
| M-GSD-079 | Role / Review Layer | MODEL_ROUTING.md | v0_5 | 按复杂度选择 token profile |
| M-GSD-080 | Context Layer | docs/agent/IOS_CONTEXT_PRIORITY.md | v0_5 | 为 SwiftUI、build、release、debug 等场景定义上下文优先级 |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 上下文治理是 GSD2 对 iOS Harness 最直接的提升点 |
| v0_1 | yes | fresh context、allowed/forbidden context、state summary 立即迁移 |
| v0_5 | yes | token profiles 和 iOS scenario priority 可增强 |
| v1_0 | yes | 可实现自动上下文打包和压缩 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| Aider Repo Map 对 iOS Harness 的融合方式 | 文件只做对比，Aider 尚未清洗 | 清洗 Aider 后合成 repo context mechanism |
| iOS 场景优先级是否覆盖全部任务 | 源文档是研究建议 | 在真实 iOS task 中补充缺失场景 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_GSD_007 | Stage 5 已概括上下文策略 |
| F_GSD_012 | 模型路由与 token profile 相关 |
| F_GSD_009 | database/projection 支撑上下文投影 |
| F_AID_QUEUED | Aider Repo Map 相关，待 Aider 清洗后链接具体 source_id |

## 13. Clean Summary for Codex

这个文件是 GSD2 上下文治理的专项证据。它最适合直接迁移到 iOS Harness 的内容是：一任务一上下文窗口、fresh session、pre-inlined context、forbidden context、summary/projection 替代长聊天历史，以及按 iOS 场景维护上下文优先级。后续与 Aider 融合时，应把 Aider 的 Repo Map 作为“如何发现相关文件”的机制，把 GSD2 的 context priority 作为“如何限制注入范围”的机制。

