# Framework Spec: Layered iOS App Development Harness

## 1. 为什么改成层级结构

平铺文件对机器可读没有问题，但对学员和新进入的 agent 不够直观。层级结构把框架变成一张执行地图：

```text
目标 -> 任务 -> 上下文 -> 文件范围 -> 角色/review -> 工具动作 -> 验证 -> 风险/release -> 状态记忆
```

每一层只回答一个问题：

| layer | question |
|---|---|
| 00_goal | 我们到底在做什么产品？ |
| 01_task | 当前任务是什么，边界是什么？ |
| 02_context | agent 应该读什么，不该读什么？ |
| 03_file_scope | agent 可以改什么，不能改什么？ |
| 04_roles_review | 谁负责，谁 review，什么模型能做？ |
| 05_action_aci | agent 如何安全地看、搜、改、跑命令？ |
| 06_verification | 如何证明任务完成？ |
| 07_risk_release | 什么动作必须升级或人工批准？ |
| 08_memory_state | 中断、失败、决策如何记录？ |
| 09_workflows | 端到端任务如何串起来？ |
| 10_examples | 新手如何照着做？ |

## 2. 设计决策

### D-001: 根目录只保留入口和地图

根目录用于导航，不承载大量细节。这样打开目录第一眼能看到：

```text
README.md
START_HERE.md
CALL_GRAPH.md
AGENTS.md
layers/
```

### D-002: 每一层独立成文件夹

层级文件夹降低认知负担。学员要学验证，只进 `06_verification`；agent 要检查风险，只进 `07_risk_release`。

### D-003: 调用链显式化

`CALL_GRAPH.md` 是核心文件。它告诉人和 agent 在正常任务、失败任务、高风险任务、release 任务中该如何跳转。

### D-004: 保留 AGENTS.md 在根目录

很多 coding agent 会默认寻找根目录的 `AGENTS.md`。因此根目录保留 agent 入口，但它只负责路由到 layers。

### D-005: scripts 不混入文档层

`scripts/validate_harness.py` 和 `scripts/install_into_repo.sh` 是运维入口；agent 动作脚本放在 `layers/05_action_aci/scripts/agent/`，因为它们属于 Action / ACI Layer。

## 3. 开发任务执行模型

```text
Human request
  -> task card
  -> context pack
  -> file scope check
  -> role/risk decision
  -> action/ACI
  -> verification
  -> review
  -> state update
```

这个模型的目标是防止：

- context pollution
- wrong file edit
- no test completion
- stuck loop
- weak model overreach
- release risk

## 4. 使用原则

- 新学员从 `START_HERE.md` 开始。
- Agent 从 `AGENTS.md` 开始。
- 设计讨论从 `FRAMEWORK_SPEC.md` 开始。
- 具体任务从 `layers/01_task/TASKS.md` 开始。
- 任何高风险动作必须经过 `07_risk_release`。
