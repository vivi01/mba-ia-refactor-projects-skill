# Audit Report: code-smells-project
**Date:** 2026-04-24
**Stack:** Python / Flask / SQLite
**Architecture:** MVC (Refactored)

---

## Detailed Findings

### AP-001 - SQL Injection Vulnerability
- **Severity:** **CRITICAL**
- **Location:** `models.py` (Original state)
- **Description:** Queries were built using string concatenation.
- **Recommendation:** Use parameterized queries (Implemented).

### AP-002 - Business Logic in Data Layer
- **Severity:** **MEDIUM**
- **Location:** `models.py`
- **Description:** Discount and revenue calculations inside models.
- **Recommendation:** Extract to Service layer or maintain as constants (Implemented with constants).

### AP-003 - Technical Error Exposure
- **Severity:** **MEDIUM**
- **Location:** `controllers.py`
- **Description:** Raw exceptions returned to the user.
- **Recommendation:** Global Error Handler (Implemented).

### AP-004 - Missing Static Typing
- **Severity:** **LOW**
- **Location:** Project-wide.
- **Description:** Lack of Type Hints.
- **Recommendation:** Add Python 3 type annotations (Implemented).

### AP-005 - Lack of Internal Documentation
- **Severity:** **LOW**
- **Location:** Project-wide.
- **Description:** Functions without docstrings.
- **Recommendation:** Add PEP 257 compliant docstrings (Implemented).

---

## Statistics
- **Total Issues:** 5 (1 Critical, 2 Medium, 2 Low)
