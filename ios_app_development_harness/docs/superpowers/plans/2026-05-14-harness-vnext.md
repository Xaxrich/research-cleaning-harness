# Harness vNext Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the iOS app development harness into a product-confirmed, plan-confirmed, verification-backed development loop.

**Architecture:** Keep the existing layered harness, but add a planning layer between goal and task execution. Strengthen completion by binding each task to verification level, simulator policy, run trace, and retrospective evidence.

**Tech Stack:** Markdown harness documents, lightweight Python validation, iOS/Xcode verification policies.

---

### Task 1: Product Intake Gates

**Files:**
- Create: `layers/00_goal/DISCOVERY_GATE.md`
- Create: `layers/00_goal/PRODUCT_BRIEF.md`
- Modify: `START_HERE.md`

- [x] **Step 1: Define the discovery gate**

Create a checklist that prevents agents from writing task cards until product assumptions, non-goals, risks, and success criteria are explicit.

- [x] **Step 2: Define product brief format**

Create a compact product brief template that users can approve before planning.

- [x] **Step 3: Update startup guidance**

Update `START_HERE.md` so real project adoption starts with discovery and brief confirmation before task cards.

### Task 2: Planning and User Confirmation

**Files:**
- Create: `layers/01_planning/README.md`
- Create: `layers/01_planning/SOLUTION_PLAN.md`
- Create: `layers/01_planning/TASK_BREAKDOWN.md`
- Create: `layers/01_planning/USER_CONFIRMATION.md`
- Create: `layers/01_planning/templates/module_plan.md`
- Modify: `CALL_GRAPH.md`
- Modify: `FRAMEWORK_SPEC.md`

- [x] **Step 1: Add the planning layer**

Document solution planning, module breakdown, and user confirmation as mandatory gates.

- [x] **Step 2: Update the call graph**

Insert `01_planning` between `00_goal` and `01_task` in the normal development chain.

### Task 3: Task Card and Context Upgrade

**Files:**
- Modify: `layers/01_task/templates/task_card.md`
- Modify: `layers/01_task/TASKS.md`
- Modify: `layers/02_context/CONTEXT_INDEX.md`
- Modify: `layers/02_context/CONTEXT_RULES.md`
- Modify: `layers/03_file_scope/FILE_SCOPE_RULES.md`

- [x] **Step 1: Extend task card fields**

Add dependencies, user confirmation, acceptance criteria, verification level, simulator requirement, trace file, and done definition.

- [x] **Step 2: Update context and file-scope rules**

Require planning context before implementation and keep allowed/read-only/forbidden files explicit.

### Task 4: Verification and Simulator Policy

**Files:**
- Create: `layers/06_verification/MODULE_VERIFICATION_POLICY.md`
- Create: `layers/06_verification/SIMULATOR_TEST_POLICY.md`
- Create: `layers/06_verification/ACCEPTANCE_CHECKLIST.md`
- Modify: `layers/06_verification/VERIFICATION_MATRIX.md`

- [x] **Step 1: Define module verification levels**

Map module types to minimum verification: diff, unit, build, simulator, device, manual.

- [x] **Step 2: Define simulator rules**

Require simulator evidence for user-visible UI and system-permission flows unless explicitly waived.

### Task 5: Trace, Retrospective, and Validation

**Files:**
- Create: `layers/08_memory_state/RUN_TRACE.md`
- Create: `layers/08_memory_state/RETROSPECTIVE.md`
- Modify: `AGENTS.md`
- Modify: `README.md`
- Modify: `FULL_TUTORIAL.md`
- Modify: `layers/09_workflows/WORKFLOW_CHAIN.md`
- Modify: `scripts/validate_harness.py`

- [x] **Step 1: Add trace and retrospective evidence**

Document what agents must record after each module.

- [x] **Step 2: Update agent contract**

Make discovery, plan confirmation, task boundary, verification evidence, and trace evidence non-negotiable.

- [x] **Step 3: Validate new required files**

Extend `scripts/validate_harness.py` so the new gates remain part of the harness.

### Verification

- [ ] Run `python3 scripts/validate_harness.py`.
- [ ] Run `git diff -- ios_app_development_harness`.
- [ ] Confirm no forbidden files changed.
