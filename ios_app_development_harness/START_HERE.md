# START HERE

这份文件给第一次进入 harness 的人和 agent 使用。

## 你是学员

按这个顺序读：

1. `README.md`
2. `CALL_GRAPH.md`
3. `FRAMEWORK_SPEC.md`
4. `FULL_TUTORIAL.md`
5. `layers/01_task/TASKS.md`
6. `layers/03_file_scope/FILE_SCOPE_RULES.md`
7. `layers/06_verification/VERIFICATION_MATRIX.md`

## 你是 agent

按这个顺序读：

1. `AGENTS.md`
2. `layers/08_memory_state/STATE.md`
3. 当前任务：`layers/01_task/TASKS.md`
4. `layers/02_context/CONTEXT_INDEX.md`
5. `layers/03_file_scope/FILE_SCOPE_RULES.md`
6. `layers/06_verification/VERIFICATION_MATRIX.md`
7. `layers/07_risk_release/RISK_CONTROL.md`

## 你要接入真实项目

1. 复制目录为 `agent_harness/`。
2. 运行 `python3 agent_harness/scripts/validate_harness.py`。
3. 填写 `layers/00_goal/PRODUCT_SPEC.md`。
4. 适配项目路径和验证命令。
5. 在 `layers/01_task/TASKS.md` 写第一个任务卡。
