---
name: refactor-arch
description: Automates analysis, auditing, and refactoring of legacy codebases to the MVC pattern. Use when you need to modernize an application, improve its architecture, or fix code smells and security issues across different technologies.
---

# Refactor-Arch Skill

This skill automates the modernization of legacy applications into a clean MVC (Model-View-Controller) architecture.

## Mandatory Success Criteria
To consider the execution successful, you MUST follow and verify the checklist below:

### Phase 1 — Analysis (Verification)
- [ ] Detect language and framework accurately.
- [ ] **Describe application domain clearly (e.g., E-commerce, LMS, Task Management)**.
- [ ] Count analyzed source files correctly.

### Phase 2 — Audit (Verification)
- [ ] Follow `references/report_template.md` strictly.
- [ ] Provide exact file paths and line numbers for each finding.
- [ ] Order findings by severity: CRITICAL → LOW.
- [ ] **Identify and document at least 5 findings strictly following this distribution**:
    - At least **1 finding** of **CRITICAL** or **HIGH** severity.
    - At least **2 findings** of **MEDIUM** severity.
    - At least **2 findings** of **LOW** severity.
- [ ] **Save the report in the root `/reports` directory as `audit-project-x.md` (where x is 1, 2, or 3)**.
- [ ] Include deprecated API detection where applicable.
- [ ] **PAUSE**: Ask for explicit confirmation before Phase 3.

### Phase 3 — Refactoring (Verification)
- [ ] Implement target directory structure (Models, Controllers, Views/Routes).
- [ ] Extract hardcoded config to module/environment variables.
- [ ] Create Models for data abstraction.
- [ ] Separate Views/Routes for interface/routing.
- [ ] Use Controllers to orchestrate application flow.
- [ ] Centralize error handling globally.
- [ ] Maintain a clear entry point (e.g., `app.py`, `app.js`).
- [ ] Ensure application boots without errors.
- [ ] Verify all original endpoints respond correctly.

## Workflow Phases

### Phase 1: Analysis
Goal: Detect the stack and map project structure.
1. Use `references/analysis_heuristics.md`.
2. **Summarize purpose, stack, source file count, and clearly define the application domain**.

### Phase 2: Audit
Goal: Identify architectural and quality issues.
1. Use `references/anti_patterns_catalog.md`.
2. Generate report using `references/report_template.md` and **save it to the root `reports/` folder**.
3. **PAUSE FOR CONFIRMATION**: Present summary and wait for approval.

### Phase 3: Refactoring
Goal: Transform the codebase into an MVC structure.
1. Apply `references/mvc_guidelines.md` and `references/refactoring_playbook.md`.
2. **Mandatory Tasks**: Separate layers, move config to `.env`, and centralize errors.
3. **Validation**: Run boot and endpoint tests.
4. **Finalization**: Commit after successful validation.

## Guidelines
- **Technology Agnostic**: Adapt behavior based on detected stack.
- **Incremental Changes**: Make surgical edits to preserve functionality.
- **Security First**: Prioritize fixing CRITICAL vulnerabilities.
