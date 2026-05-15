# Full Tutorial: 层级版 iOS App Development Harness 使用教程

## 1. 先看地图

打开 harness 后先看三个文件：

```text
START_HERE.md
CALL_GRAPH.md
FRAMEWORK_SPEC.md
```

不要先钻进所有细节。先理解层级：

```text
00_goal -> 01_planning -> 01_task -> 02_context -> 03_file_scope -> 04_roles_review -> 05_action_aci -> 06_verification -> 07_risk_release -> 08_memory_state
```

## 2. 安装到真实项目

推荐 sidecar 安装：

```bash
cp -R ios_app_development_harness /path/to/my-ios-app/agent_harness
cd /path/to/my-ios-app
python3 agent_harness/scripts/validate_harness.py
```

## 3. 第一次适配

按层适配：

| order | file | what to fill |
|---|---|---|
| 1 | `layers/00_goal/DISCOVERY_GATE.md` | 需求澄清问题和阻塞条件 |
| 2 | `layers/00_goal/PRODUCT_BRIEF.md` | 用户确认过的产品 brief |
| 3 | `layers/00_goal/PRODUCT_SPEC.md` | app 目标、用户、技术栈、风险 |
| 4 | `layers/01_planning/SOLUTION_PLAN.md` | 技术方案、模块计划、验证策略 |
| 5 | `layers/01_planning/TASK_BREAKDOWN.md` | 模块到任务卡的拆分 |
| 6 | `layers/02_context/CONTEXT_INDEX.md` | lib/ios/test/firebase 等真实路径 |
| 7 | `layers/03_file_scope/FILE_SCOPE_RULES.md` | allowed/read-only/forbidden 默认规则 |
| 8 | `layers/06_verification/VERIFICATION_MATRIX.md` | 项目真实验证命令 |
| 9 | `layers/06_verification/SIMULATOR_TEST_POLICY.md` | 什么时候必须跑模拟器/真机 |
| 10 | `layers/07_risk_release/IOS_RELEASE_CHECKLIST.md` | release、privacy、signing 流程 |

## 4. 第一个任务

在 `layers/01_task/TASKS.md` 写一个 docs-only task。不要一开始改业务代码。
实现类任务必须等 `PRODUCT_BRIEF.md`、`SOLUTION_PLAN.md` 和 `USER_CONFIRMATION.md` 确认后再创建。

```yaml
task_id: TASK-001
status: ready
task_type: docs
owner_role: orchestrator
risk_level: low
goal: Fill product spec for the app.
allowed_files:
  - agent_harness/layers/00_goal/PRODUCT_SPEC.md
read_only_files:
  - README.md
  - pubspec.yaml
forbidden_files:
  - .env*
  - "**/*.p12"
verification_commands:
  - git diff -- agent_harness/layers/00_goal/PRODUCT_SPEC.md
rollback_plan: revert product spec changes
```

## 5. 给 Codex 的工作提示

```text
你现在在一个 iOS app repo 中工作，必须使用 agent_harness。

当前任务是 TASK-001。

先读：
- agent_harness/AGENTS.md
- agent_harness/CALL_GRAPH.md
- agent_harness/layers/08_memory_state/STATE.md
- agent_harness/layers/01_task/TASKS.md
- agent_harness/layers/02_context/CONTEXT_INDEX.md
- agent_harness/layers/03_file_scope/FILE_SCOPE_RULES.md
- agent_harness/layers/06_verification/VERIFICATION_MATRIX.md

只允许修改当前任务的 allowed_files。
完成前运行 verification_commands。
用户可见 UI 改动需要按 SIMULATOR_TEST_POLICY.md 给出模拟器/真机证据。
完成后更新 RUN_TRACE.md。
```

## 6. 正常任务调用逻辑

```text
00_goal/DISCOVERY_GATE.md
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
  -> 08_memory_state/RUN_TRACE.md
  -> 08_memory_state/STATE.md
```

## 7. 失败任务调用逻辑

```text
06_verification/DEBUG_GUIDE.md
  -> 08_memory_state/FAILURE_LOG.md
  -> 04_roles_review/MODEL_ROUTING.md
  -> 07_risk_release/RISK_CONTROL.md
```

失败时不要盲目重试。先分类，再决定 retry、escalate 或 block。

## 8. 高风险任务调用逻辑

```text
03_file_scope/HIGH_RISK_FILES.md
  -> 07_risk_release/RISK_CONTROL.md
  -> 04_roles_review/REVIEW_MATRIX.md
  -> 07_risk_release/templates/manual_approval.md
```

release、signing、upload、production Firebase、privacy 权限都属于高风险。

## 9. 每层教学法

学员不要一次学完所有文件。按层练：

1. 00_goal：澄清需求，写产品目标。
2. 01_planning：写方案、拆模块、让用户确认。
3. 01_task：写任务卡。
4. 02_context：列出该读什么。
5. 03_file_scope：列出能改什么。
6. 04_roles_review：判断谁 review。
7. 05_action_aci：用 view/search/safe_edit/run。
8. 06_verification：跑验证，必要时跑模拟器/真机。
9. 07_risk_release：判断是否升级。
10. 08_memory_state：记录状态、失败和执行轨迹。

## 10. 判断学会的标准

学员能做到以下事情，才算真正会用：

- 解释每个 layer 的职责。
- 写一个合格 task card。
- 在实现前完成产品和方案确认。
- 正确区分 allowed/read-only/forbidden。
- 从 CALL_GRAPH 走完整任务流程。
- 为 Flutter/Swift/Firebase/release 任务选择不同验证。
- 判断何时必须开模拟器或真机测试。
- 失败时写 FAILURE_LOG 而不是盲改。
- 完成时写 RUN_TRACE。
- 知道 release_blocking 必须人工批准。
