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
- agent_harness/layers/02_context/CONTEXT_INDEX.md
- agent_harness/layers/03_file_scope/FILE_SCOPE_RULES.md
- agent_harness/layers/06_verification/VERIFICATION_MATRIX.md
- agent_harness/layers/07_risk_release/RISK_CONTROL.md

只允许修改当前任务的 allowed_files。
完成前运行 verification_commands。
如果失败，更新 FAILURE_LOG.md。
```

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
