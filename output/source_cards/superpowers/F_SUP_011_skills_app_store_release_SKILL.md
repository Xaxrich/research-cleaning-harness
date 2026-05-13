# Source Card: F_SUP_011 - app-store-release SKILL.md

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_011 |
| framework | superpowers |
| raw_path | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md |
| file_type | markdown |
| topic | app-store-release |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | high |

## 2. One-line Essence

这个文件本质上是在做：把 iOS App Store/TestFlight 发布拆成可验证的阶段性检查清单，确保发布、上传、审核、被拒处理和热修复都有证据链。

## 3. File Summary

- Skill frontmatter 定义触发条件：App Store 提交、TestFlight、版本号变更、发布构建、审核被拒。
- 核心原则是“发布是流程，不是事件”，没有完成检查清单就不能提交。
- 发布前检查分为代码质量、版本配置、iOS 配置、Firebase 配置、发布构建、App Store Connect、存档上传、提交审核、发布后验证九阶段。
- 它要求检查项结果明确为通过、失败或跳过并有理由。
- 它提供 TestFlight 内测/外测流程。
- 它列出常见审核被拒原因和处理步骤。
- 它定义热修复发布流程和发布检查清单模板。
- 它汇总测试、分析、格式、iOS release build、IPA、validate/upload 的验证命令。

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-067 | Release Checklist Gate | 没有完成检查清单就不能提交，每项必须有结果。 | E1, E2 | high |
| M-SUP-068 | Multi-stage App Store Pipeline | 将发布拆成代码质量、版本、iOS 配置、Firebase、构建、ASC、上传、提交、发布后验证。 | E3, E4, E5 | high |
| M-SUP-069 | iOS Metadata And Privacy Check | 检查 Info.plist、权限描述、图标、LaunchScreen、方向、加密声明等。 | E6 | high |
| M-SUP-070 | Firebase Production Readiness Check | 检查 GoogleService-Info、Bundle ID、生产项目、安全规则、Functions、Analytics。 | E7 | high |
| M-SUP-071 | Archive Upload And Validation | 支持 Xcode Archive 和命令行 IPA validate/upload。 | E8 | high |
| M-SUP-072 | Rejection Recovery Flow | 审核被拒后记录原因、修复、验证、递增构建号、回复审核员、重新提交。 | E10 | high |
| M-SUP-073 | Hotfix Release Flow | 紧急修复走 hotfix 分支、验证、递增构建号、上传和加急审核。 | E11 | medium |
| M-SUP-074 | Release Artifact Record | 每次发布创建版本化检查清单，记录执行者、阶段结果和备注。 | E12 | high |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| release_risk | 用发布检查清单和九阶段流程防止遗漏。 | E2, E3 |
| no_test_completion | 代码质量阶段要求 flutter test、analyze、format、debug log 与待办标记检查。 | E4 |
| version_mismatch | 版本配置阶段检查 pubspec、MARKETING_VERSION、CURRENT_PROJECT_VERSION。 | E5 |
| missing_privacy_permission | iOS 配置阶段列出 Info.plist 权限描述。 | E6 |
| firebase_prod_misconfig | Firebase 配置阶段检查生产环境、Bundle ID、安全规则和 Functions。 | E7 |
| upload_failure | 上传阶段包含 IPA validate/upload 和 ASC 可见性检查。 | E8 |
| review_rejection_loop | 被拒处理要求记录原因、复现/验证修复、回复审核员。 | E10 |
| post_release_blindness | 发布后验证检查 App Store 搜索、下载、Analytics、Crashlytics。 | E9 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 发布即流程 | 发布步骤多且易漏 | App Store 错误成本高，必须 checklist 化 | 流程较长 |
| 每项有结果 | 避免空勾选 | 跳过也要承担可追踪责任 | 需要人工判断跳过理由 |
| 分阶段检查 | 降低认知负担 | 按代码、配置、构建、平台、提交分离风险 | 阶段间依赖需要维护 |
| 被拒流程 | 审核失败不可临场处理 | 将拒绝信息变成 RCA/检查清单输入 | 仍需人工理解审核语境 |

## 7. 5 Why Analysis

### Mechanism: Release Checklist Gate

- Why 1: 为什么发布需要 gate？因为发布不是单个构建命令，而是代码、配置、元数据、上传和审核的组合。
- Why 2: 为什么每个检查项要有明确结果？因为空白或默认通过会掩盖风险。
- Why 3: 为什么 iOS 发布特别需要它？因为权限、图标、签名、TestFlight、ASC 元数据都会导致审核失败或上线问题。
- Why 4: 为什么被拒也要流程化？因为审核被拒后的修复、验证、构建号和回复都容易遗漏。
- Why 5: 为什么这适合 Harness？因为弱模型可以执行检查项，但提交/上传/审核决策仍由人工 gate 控制。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Frontmatter 定义发布相关触发、输入输出和升级条件。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:1-8 | M-SUP-067 |
| E2 | 核心原则称发布是流程，铁律要求没有完成检查清单就没有提交。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:10-27 | M-SUP-067 |
| E3 | 发布前检查清单从阶段 1 到阶段 9。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:35-319 | M-SUP-068 |
| E4 | 代码质量阶段运行 flutter test、flutter analyze、dart format、debug log 与待办标记检查。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:35-74 | M-SUP-068 |
| E5 | 版本配置阶段检查 pubspec 和 Xcode project 版本。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:76-113 | M-SUP-068 |
| E6 | iOS 特定配置阶段检查 Info.plist 权限描述和 AppIcon 尺寸。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:115-166 | M-SUP-069 |
| E7 | Firebase 阶段检查 GoogleService-Info、Bundle ID、生产环境、安全规则和 Cloud Functions。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:168-193 | M-SUP-070 |
| E8 | 存档上传阶段提供 Xcode 和命令行上传方法，以及 validate/upload 检查。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:260-295 | M-SUP-071 |
| E9 | 发布后验证要求检查审核状态、App Store 搜索、下载、Analytics、Crashlytics。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:314-328 | post-release |
| E10 | 审核被拒处理流程列出拒绝原因和 8 步处理。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:357-383 | M-SUP-072 |
| E11 | 热修复流程要求 hotfix 分支、mobile-tdd、验证、递增构建号和提交审核。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:386-398 | M-SUP-073 |
| E12 | 发布检查清单模板记录版本、构建号、发布类型、日期、执行者和阶段结果。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:400-459 | M-SUP-074 |
| E13 | 验证命令汇总列出 test、analyze、format、build ios、build ipa、validate/upload。 | raw/Kimi_Agent_Superpowers 体系探究/skills/app-store-release/SKILL.md:462-490 | commands |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Release Checklist Gate | Risk / Release Layer | .agents/skills/app-store-release/SKILL.md | v0_5 | Adopt as mobile release skill |
| Multi-stage App Store Pipeline | Risk / Release Layer | docs/agent/checklists/release-vX.Y.Z.md | v0_5 | Generate per-release checklist |
| iOS Metadata And Privacy Check | Feedback / Verification Layer | scripts/agent/verify-app-store-ready.sh | v0_5 | Convert checks into scriptable validations where possible |
| Firebase Production Readiness Check | Feedback / Verification Layer | scripts/agent/verify-firebase-config.sh | v0_5 | Validate production Firebase config |
| Archive Upload And Validation | Action / ACI Layer | docs/agent/RELEASE_UPLOAD.md | v1_0 | Document upload commands and human confirmation gates |
| Rejection Recovery Flow | Risk / Release Layer | docs/agent/checklists/rejection-vX.Y.Z.md | v0_5 | Create rejection records |
| Hotfix Release Flow | Task Layer | docs/agent/TASKS.md | v0_5 | Add hotfix task template |
| Release Artifact Record | Memory / State Layer | docs/agent/STATE.md | v0_5 | Update release status after each stage |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | App Store release is a high-risk iOS workflow that benefits from explicit checklist gates. |
| v0_1 | partial | Record release risk and human gate early, but full skill can wait. |
| v0_5 | yes | Add release skill, release checklist, firebase/app-store validation scripts. |
| v1_0 | yes | Add CI/upload validation and stronger release artifact tracking. |
| no_transfer | yes | Do not let weak models perform actual upload/submission without human confirmation. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| `xcrun altool` may be deprecated or replaced in current Apple tooling | Tooling changes over time. | Verify current Apple recommended upload command before implementation. |
| Some grep checks may produce false positives | `print(` or pending markers may be acceptable in non-critical paths. | Require manual review for found matches. |
| Full release skill may be too much for v0.1 | It is detailed and assumes real app project files exist. | Defer to v0.5 after app harness scaffold exists. |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| F_SUP_004 | migration design lists app-store-release as skill 8 |
| F_SUP_007 | AGENTS references app-store-release |
| F_SUP_008 | STATE release status should be updated by this skill |
| F_SUP_005 | skeptic review requires human gate for release |

## 13. Clean Summary for Codex

这份 skill 是 iOS Harness 中最适合保留为专用流程的文件之一。它把 App Store/TestFlight 发布从“最后一步”改造成九阶段检查清单，并把代码质量、版本、iOS 配置、Firebase、构建、上传、审核和发布后验证连接起来。后续 Codex 应把它迁移到 v0.5：先生成 release checklist 和 app-store/firbase 验证脚本，再加人工确认 gate。实际上传、提交审核、证书签名和审核回复不应由弱模型独立执行。
