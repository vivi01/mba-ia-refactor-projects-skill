# Audit Report: code-smells-project
**Date:** 2026-04-24
**Stack:** Python / Flask / SQLite
**Architecture:** MVC (Refactored)

---

## Detailed Findings

### AP-001 - SQL Injection Vulnerability
- **Severity:** **CRITICAL**
- **Location:** `models.py:16-24`, `models.py:26-38`
- **Description:** Queries were originally built using string concatenation. Current lines show the refactored state with parameterized queries.
- **Recommendation:** Use parameterized queries (Implemented).

### AP-002 - Business Logic in Data Layer
- **Severity:** **MEDIUM**
- **Location:** `models.py:5-9`, `models.py:151-168`
- **Description:** Discount and revenue calculations located inside models instead of services/controllers.
- **Recommendation:** Extract to Service layer or maintain as constants (Implemented with constants).

### AP-003 - Technical Error Exposure
- **Severity:** **MEDIUM**
- **Location:** `app.py:31-45`
- **Description:** Raw exceptions were returned to the user. Current range shows the centralized error handler fix.
- **Recommendation:** Global Error Handler (Implemented).

### AP-004 - Missing Static Typing
- **Severity:** **LOW**
- **Location:** `models.py:1-168`, `controllers.py:1-125`
- **Description:** Lack of Type Hints throughout the source files.
- **Recommendation:** Add Python 3 type annotations (Implemented).

### AP-005 - Lack of Internal Documentation
- **Severity:** **LOW**
- **Location:** `models.py:1-168`, `controllers.py:1-125`
- **Description:** Functions and modules missing PEP 257 compliant docstrings.
- **Recommendation:** Add PEP 257 compliant docstrings (Implemented).

---

## Statistics
- **Total Issues:** 5 (1 Critical, 2 Medium, 2 Low)
