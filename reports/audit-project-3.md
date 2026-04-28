# Audit Report: task-manager-api
**Date:** 2026-04-24
**Stack:** Python / Flask / SQLAlchemy
**Architecture:** MVC (Refactored)

---

## Detailed Findings

### AP-001 - SMTP Secrets Exposure
- **Severity:** **CRITICAL**
- **Location:** `services/notification_service.py:7-11`
- **Description:** SMTP credentials defined directly in the class constructor. Range shows the fix using `os.getenv`.
- **Recommendation:** Use environment variables (Implemented).

### AP-002 - Serialization Leak in Routes
- **Severity:** **MEDIUM**
- **Location:** `routes/task_routes.py:11-14`
- **Description:** Manual JSON construction in endpoint handlers. Range shows the fix using `to_dict()`.
- **Recommendation:** Delegate serialization to Model `to_dict()` (Implemented).

### AP-003 - Performance N+1 in Task List
- **Severity:** **MEDIUM**
- **Location:** `routes/task_routes.py:12-13`
- **Description:** Querying related entities (users, categories) inside a loop. Range shows the fix using `joinedload`.
- **Recommendation:** Use Eager Loading with `joinedload` (Implemented).

### AP-004 - Deprecated ORM Methods
- **Severity:** **LOW**
- **Location:** `routes/task_routes.py:18-22`, `routes/task_routes.py:58-63`
- **Description:** Use of deprecated `query.get()` instead of `session.get()`.
- **Recommendation:** Update to SQLAlchemy 2.0 style using `session.get()` (Implemented).

### AP-005 - JSON Response Inconsistency
- **Severity:** **LOW**
- **Location:** `app.py:34-40`, `routes/task_routes.py:1-75`
- **Description:** Inconsistent usage of `jsonify` vs raw dictionaries for API responses.
- **Recommendation:** Standardize all responses with `jsonify` (Implemented).

---

## Statistics
- **Total Issues:** 5 (1 Critical, 2 Medium, 2 Low)
