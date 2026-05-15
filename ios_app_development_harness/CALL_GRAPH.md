# CALL GRAPH

这份文件描述 harness 的调用逻辑。把它当成系统执行图。

## 主调用链

```text
Human request
  -> 00_goal/DISCOVERY_GATE.md
  -> 00_goal/PRODUCT_SPEC.md
  -> 00_goal/PRODUCT_BRIEF.md
  -> 01_planning/SOLUTION_PLAN.md
  -> 01_planning/TASK_BREAKDOWN.md
  -> 01_planning/USER_CONFIRMATION.md
  -> 01_task/TASKS.md
  -> 02_context/CONTEXT_INDEX.md
  -> 03_file_scope/FILE_SCOPE_RULES.md
  -> 04_roles_review/ROLE_MATRIX.md
  -> 05_action_aci/ACI_TOOL_CONTRACTS.md
  -> 06_verification/VERIFICATION_MATRIX.md
  -> 06_verification/MODULE_VERIFICATION_POLICY.md
  -> 06_verification/SIMULATOR_TEST_POLICY.md
  -> 04_roles_review/REVIEW_MATRIX.md
  -> 08_memory_state/RUN_TRACE.md
  -> 08_memory_state/STATE.md
```

## 失败调用链

```text
verification failed
  -> 06_verification/DEBUG_GUIDE.md
  -> 08_memory_state/FAILURE_LOG.md
  -> 04_roles_review/MODEL_ROUTING.md
  -> 07_risk_release/RISK_CONTROL.md
  -> retry / escalate / block
```

## 高风险调用链

```text
high-risk file/action
  -> 03_file_scope/HIGH_RISK_FILES.md
  -> 07_risk_release/RISK_CONTROL.md
  -> 04_roles_review/REVIEW_MATRIX.md
  -> 07_risk_release/templates/manual_approval.md
```

## Release 调用链

```text
release task
  -> 07_risk_release/IOS_RELEASE_CHECKLIST.md
  -> 06_verification/VERIFICATION_MATRIX.md
  -> 04_roles_review/REVIEW_MATRIX.md
  -> manual approval
```

## Layer Responsibilities

| layer | responsibility | primary files |
|---|---|---|
| 00_goal | 定义项目目标、澄清门禁、产品确认 | `DISCOVERY_GATE.md`, `PRODUCT_SPEC.md`, `PRODUCT_BRIEF.md` |
| 01_planning | 控制方案、模块拆分、用户确认 | `SOLUTION_PLAN.md`, `TASK_BREAKDOWN.md`, `USER_CONFIRMATION.md` |
| 01_task | 把需求变成 bounded task | `TASKS.md`, `templates/task_card.md` |
| 02_context | 控制读什么 | `CONTEXT_INDEX.md`, `CONTEXT_RULES.md` |
| 03_file_scope | 控制能改什么 | `FILE_SCOPE_RULES.md`, `HIGH_RISK_FILES.md` |
| 04_roles_review | 控制谁负责和谁 review | `ROLE_MATRIX.md`, `REVIEW_MATRIX.md`, `MODEL_ROUTING.md` |
| 05_action_aci | 控制 agent 如何操作电脑 | `ACI_TOOL_CONTRACTS.md`, `scripts/agent/` |
| 06_verification | 控制怎么证明完成 | `VERIFICATION_MATRIX.md`, `MODULE_VERIFICATION_POLICY.md`, `SIMULATOR_TEST_POLICY.md`, `TESTING_GUIDE.md`, `DEBUG_GUIDE.md` |
| 07_risk_release | 控制隐私、发布和高风险动作 | `RISK_CONTROL.md`, `IOS_RELEASE_CHECKLIST.md` |
| 08_memory_state | 控制恢复、失败、执行轨迹和决策记录 | `STATE.md`, `FAILURE_LOG.md`, `DECISIONS.md`, `RUN_TRACE.md`, `RETROSPECTIVE.md` |
| 09_workflows | 提供端到端流程 | `WORKFLOW_CHAIN.md`, `BOOTSTRAP.md` |
| 10_examples | 提供可复制示例 | task examples, prompts |
