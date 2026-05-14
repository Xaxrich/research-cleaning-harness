# Framework Spec: iOS App Development Harness

## 1. 设计目标

这套 harness 的目标是让一个 coding agent 在真实 iOS app repo 中稳定工作。稳定的含义不是“永远不出错”，而是：

- 每次只处理一个明确任务。
- 每个任务有明确文件范围。
- agent 不会随意读取和修改无关文件。
- 每次修改都有验证命令。
- 失败会被记录和分类，而不是盲目重试。
- release、privacy、signing、Firebase rules 等高风险动作不会被 agent 自动放行。

## 2. 为什么不是大而全 runtime

一上来做 runtime enforcement 很容易失败，因为真实 iOS 项目差异很大：

- Swift / SwiftUI / UIKit / Flutter / React Native 目录结构不同。
- 测试命令不同。
- Firebase、signing、privacy、CI 配置不同。
- App Store 发布路径高度敏感。

所以本框架采用 docs-first：

```text
v0.1 先稳定规则和任务纪律
v0.5 再把高频规则脚本化
v1.0 最后才做强制 runtime
```

## 3. 架构分层

| 层 | 文件 | 解决的问题 |
|---|---|---|
| Goal Layer | `PRODUCT_SPEC.md` | 项目目标、非目标、产品边界 |
| Task Layer | `TASKS.md`, `templates/task_card.md` | 每次只处理一个任务 |
| Context Layer | `CONTEXT_INDEX.md`, `CONTEXT_RULES.md` | 控制 agent 读取什么 |
| File Scope Layer | `FILE_SCOPE_RULES.md`, `HIGH_RISK_FILES.md` | 控制 agent 能改什么 |
| Role / Review Layer | `ROLE_MATRIX.md`, `REVIEW_MATRIX.md` | 控制谁负责、谁 review |
| Action / ACI Layer | `docs/agent/ACI_TOOL_CONTRACTS.md`, `scripts/agent/` | 控制工具调用 |
| Verification Layer | `VERIFICATION_MATRIX.md`, `docs/agent/TESTING_GUIDE.md` | 控制完成标准 |
| Risk / Release Layer | `RISK_CONTROL.md`, `IOS_RELEASE_CHECKLIST.md` | 控制高风险动作 |
| Memory Layer | `STATE.md`, `FAILURE_LOG.md`, `DECISIONS.md` | 控制恢复和决策记录 |

## 4. 关键设计决策

### D-001: 任务卡是执行入口

所有工作从 `TASKS.md` 的任务卡开始，而不是从一句自然语言需求直接开始。

原因：

- 自然语言需求容易遗漏文件范围。
- iOS 任务常常跨 Flutter、Swift、Firebase、release 多个风险域。
- 任务卡能让 agent、reviewer 和人类使用同一份约束。

### D-002: 文件范围必须显式声明

每个任务必须有：

```text
allowed_files
read_only_files
forbidden_files
```

原因：

- 防止 wrong_file_edit。
- 防止 context_pollution。
- 保护 signing、secrets、release metadata。

### D-003: 上下文按任务类型加载

不是每个任务都读全仓库。`CONTEXT_INDEX.md` 根据 task_type 决定要读哪些文件。

原因：

- 大上下文会让弱模型迷路。
- 过多无关文件会污染判断。
- iOS 项目里 release/privacy/native bridge 的上下文不能随便混入普通 UI 任务。

### D-004: 验证是完成条件，不是附加项

每个任务必须在 `VERIFICATION_MATRIX.md` 中找到对应验证。

原因：

- 没有验证的完成声明不可接受。
- iOS 任务常见“代码能编译但平台行为错”的问题。
- 测试失败必须进入 failure loop，而不是继续猜。

### D-005: 高风险动作默认不自动执行

release、signing、upload、production data、Firebase rules、privacy 权限属于高风险。

原因：

- 这些动作有外部副作用。
- 很多错误无法靠本地测试完全覆盖。
- 需要人工 approval 或强 review。

### D-006: ACI 工具是辅助，不是越权入口

脚本在 `scripts/agent/` 中，但它们只是把常用动作标准化。

原因：

- v0.5 脚本不能替代规则判断。
- safe command runner 不能覆盖所有项目命令。
- 真正强制拦截应放到 v1.0。

## 5. 框架融合思路

这套 harness 融合了五类能力：

| 能力 | 在本框架中的表现 |
|---|---|
| 工程纪律 | plan、test、debug、review、completion evidence |
| 状态机 | `STATE.md`, `TASKS.md`, `FAILURE_LOG.md` |
| repo context | `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md` |
| 角色治理 | `ROLE_MATRIX.md`, `REVIEW_MATRIX.md` |
| ACI 工具 | view/search/safe_edit/run/context_pack |

最终设计不是让某个框架统治全局，而是按职责分层。

## 6. 成功标准

一个 iOS task 只有同时满足以下条件，才算完成：

```text
1. 修改只发生在 allowed_files
2. read_only_files 没有被修改
3. forbidden_files 没有被读取或编辑
4. 验证命令已运行或明确说明为何无法运行
5. 失败记录在 FAILURE_LOG.md
6. 高风险动作有 review 或 manual approval
7. final answer 中写明变更、验证、风险、剩余问题
```
