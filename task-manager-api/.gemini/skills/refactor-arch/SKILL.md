---
name: refactor-arch
description: Automates analysis, auditing, and refactoring of legacy codebases to the MVC pattern. Use when you need to modernize an application, improve its architecture, or fix code smells and security issues across different technologies.
---

# Refactor-Arch Skill

This skill automates the modernization of legacy applications into a clean MVC (Model-View-Controller) architecture.

## Mandatory Success Criteria
To consider the execution successful, the following must be achieved:
1. **Phase 1**: Correctly detect the language, framework, and database (100% accuracy required).
2. **Phase 2**: Identify at least **5 findings** in the audit.
3. **Phase 2**: At least **1 finding** must be classified as **CRITICAL** or **HIGH**.
4. **Phase 3**: The application must be fully functional after refactoring, with all original endpoints preserved and validated.

## Workflow Phases

### Phase 1: Analysis
Goal: Detect the stack and map the project structure.
1. Use `references/analysis_heuristics.md` to identify the language, framework, database, and current architecture.
2. List the main components and entry points of the application.
3. Summarize the application's purpose and current state.

### Phase 2: Audit
Goal: Identify architectural and quality issues.
1. Use `references/anti_patterns_catalog.md` to detect at least 8 anti-patterns or code smells (minimum 5 required for success).
2. Classify each finding by severity (CRITICAL, HIGH, MEDIUM, LOW). Ensure at least one is CRITICAL or HIGH.
3. Generate a structured report using the template in `references/report_template.md`.
4. Save the report in the `/reports` directory of the project.
5. **PAUSE FOR CONFIRMATION**: Present the report summary to the user and wait for explicit approval before proceeding to Phase 3.

### Phase 3: Refactoring
Goal: Transform the codebase into an MVC structure.
1. Apply the target architecture defined in `references/mvc_guidelines.md`.
2. Follow the patterns in `references/refactoring_playbook.md` to fix the identified anti-patterns.
3. Specific tasks:
    - Separate logic into `Models`, `Views/Routes`, and `Controllers`.
    - Move hardcoded configurations to environment variables.
    - Centralize error handling.
4. **Validation**:
    - Ensure the application starts without errors.
    - Verify that endpoints are functional and preserve their original behavior.
5. **Finalization**: Commit the changes with a clear message describing the refactoring (after user confirmation of successful validation).

## Guidelines
- **Technology Agnostic**: Adapt your approach based on the detected stack.
- **Incremental Changes**: Make surgical edits to preserve functionality.
- **Security First**: Prioritize fixing CRITICAL security vulnerabilities like SQL injection or hardcoded secrets.
