# PRODUCT SPEC

## Purpose

This harness coordinates coding agents working on an iOS app repo. It is optimized for bounded changes, traceable context, safe edits, verification evidence and release-risk control.

## Non-Goals

- It does not replace Xcode, Flutter, Firebase or App Store tooling.
- It does not grant autonomous release/upload authority.
- It does not make raw research files part of runtime context.

## v0.1 Scope

- Task cards with explicit file scope.
- Context index and context loading rules.
- Role/review/risk matrices.
- Verification matrix and failure log.
- Lightweight ACI tool contracts and optional scripts.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-GSD-021 | gsd2 | F_GSD_004 | v0_1 | Backward iOS Harness Design |
| M-GSD-037 | gsd2 | F_GSD_006 | v0_1 | Research Question Framing |
| M-GST-119 | gstack | F_GST_030 | v0_1 | Platform-Agnostic Agent Design |
| M-GST-127 | gstack | F_GST_032 | v0_1 | Product Context Preservation |
| M-GST-159 | gstack | F_GST_040 | v0_1 | Platform-Agnostic Agent Design |
| M-AID-003 | aider | F_AID_001 | v0_5 | Aider-to-iOS Transfer Agenda |
