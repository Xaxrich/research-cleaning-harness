# iOS App Development Harness

这是一套按层级组织的 iOS app 开发 harness。它可以直接复制到真实项目中作为 `agent_harness/` 使用。

## 一眼看懂目录

```text
agent_harness/
  README.md
  START_HERE.md
  AGENTS.md
  CALL_GRAPH.md
  FRAMEWORK_SPEC.md
  FULL_TUTORIAL.md

  layers/
    00_goal/            # 项目目标、产品边界
    01_task/            # 任务卡、任务入口
    02_context/         # 上下文读取规则
    03_file_scope/      # allowed/read-only/forbidden 文件范围
    04_roles_review/    # 角色、review、模型路由
    05_action_aci/      # agent 工具契约和脚本
    06_verification/    # 测试、验证、debug
    07_risk_release/    # 风险、隐私、发布、人工批准
    08_memory_state/    # 状态、失败日志、决策、Git
    09_workflows/       # 工作流、启动步骤
    10_examples/        # 示例任务和 Codex prompts
```

## 调用顺序

```text
00_goal
  -> 01_task
  -> 02_context
  -> 03_file_scope
  -> 04_roles_review
  -> 05_action_aci
  -> 06_verification
  -> 07_risk_release
  -> 08_memory_state
```

人类先读 `START_HERE.md`。Agent 先读 `AGENTS.md`。想理解为什么这样设计，读 `FRAMEWORK_SPEC.md`。要完整教学版，读 `FULL_TUTORIAL.md`。

## 最短使用路径

```bash
cp -R ios_app_development_harness /path/to/my-ios-app/agent_harness
cd /path/to/my-ios-app
python3 agent_harness/scripts/validate_harness.py
```

然后按顺序适配：

```text
layers/00_goal/PRODUCT_SPEC.md
layers/02_context/CONTEXT_INDEX.md
layers/03_file_scope/FILE_SCOPE_RULES.md
layers/06_verification/VERIFICATION_MATRIX.md
layers/07_risk_release/IOS_RELEASE_CHECKLIST.md
```

## 设计原则

- v0.1 是文档规则和任务纪律。
- v0.5 是脚本辅助。
- v1.0 才是 runtime enforcement。
- 任何任务都必须有文件范围、验证命令和恢复路径。
