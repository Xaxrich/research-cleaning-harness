# Codex Prompts

## Execute Task

```text
你现在在一个 iOS app repo 中工作，必须使用 agent_harness。

当前任务是 <TASK_ID>。

先读：
- agent_harness/AGENTS.md
- agent_harness/CALL_GRAPH.md
- agent_harness/layers/08_memory_state/STATE.md
- agent_harness/layers/01_task/TASKS.md
- agent_harness/layers/00_goal/DISCOVERY_GATE.md
- agent_harness/layers/00_goal/PRODUCT_BRIEF.md
- agent_harness/layers/01_planning/SOLUTION_PLAN.md
- agent_harness/layers/01_planning/TASK_BREAKDOWN.md
- agent_harness/layers/01_planning/USER_CONFIRMATION.md
- agent_harness/layers/01_planning/GATE_OUTPUT_PROTOCOL.md
- agent_harness/layers/02_context/CONTEXT_INDEX.md
- agent_harness/layers/03_file_scope/FILE_SCOPE_RULES.md
- agent_harness/layers/06_verification/VERIFICATION_MATRIX.md
- agent_harness/layers/06_verification/MODULE_VERIFICATION_POLICY.md
- agent_harness/layers/06_verification/SIMULATOR_TEST_POLICY.md
- agent_harness/layers/07_risk_release/RISK_CONTROL.md

只允许修改当前任务的 allowed_files。
完成前运行 verification_commands。
如果失败，更新 FAILURE_LOG.md。
向用户请求确认时必须使用 GATE_OUTPUT_PROTOCOL.md：用中文说明当前阶段、你要看的文档、回答后会写入的文档、本次确认什么，并把 `需要你决定` 放在最后。
```

## Standard Gate Reply Example

Use this shape when asking the user to make a product, plan, task, verification, waiver, or risk decision. Keep the final `需要你决定` block as the last content in the reply.

```text
## 当前门禁：产品简报
当前阶段：开发前最小确认（00_goal）
当前状态：需要你做一个决定（needs_user_decision）

本次要解决：先确认 MVP 产品结构，之后才会请求你确认整份产品简报。

你要看的文档：`agent_harness/layers/00_goal/PRODUCT_BRIEF.md`
回答后会写入：`agent_harness/layers/00_goal/PRODUCT_BRIEF.md`
本次确认什么：MVP 产品结构。

### 已经确定
- 到岗 / 离岗机制：公司地址地理围栏进入 / 离开触发本地时间戳。
- 隐私边界：除非产品简报后续明确改动，否则每日考勤明细不上传。

### 还卡住什么
- MVP 产品结构还没有最终确认。

### 本次不处理
- 技术架构、权限实现、模块顺序、任务卡拆分。

### 文件变动
- `agent_harness/layers/00_goal/PRODUCT_BRIEF.md`
- `agent_harness/layers/08_memory_state/RUN_TRACE.md`

### 验证
- `python3 agent_harness/scripts/validate_harness.py`：通过。

### 确认后下一步
- 将产品简报状态推进到 `needs_user_confirmation`，再用单独一轮请求你确认整份产品简报。

## 需要你决定
请只做一件事：查看 `agent_harness/layers/00_goal/PRODUCT_BRIEF.md`，确认 MVP 产品结构是否采用“今日 / 首页、月度打工账单、补偿节点倒计时、设置”。
```

Do not add any text after `需要你决定`.

## Review Diff

```text
请按 agent_harness/layers/04_roles_review/REVIEW_MATRIX.md review 当前 diff。
Findings first，按 severity 排序。
重点检查 wrong_file_edit、missing verification、release/privacy/security risk、rollback gap。
```

## Debug Failure

```text
当前任务验证失败。
先读 agent_harness/layers/06_verification/DEBUG_GUIDE.md 和 agent_harness/layers/08_memory_state/FAILURE_LOG.md。
不要直接修。
先分类 failure mode，提出一个最小假设，再做一处修改。
```
