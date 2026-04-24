# Audit Report: task-manager-api
**Date:** 2026-04-24
**Stack:** Python / Flask / SQLAlchemy
**Architecture:** MVC (Refactored)

---

## Detailed Findings

### AP-001 - SMTP Secrets Exposure
- **Severity:** **CRITICAL**
- **Location:** `services/notification_service.py` (Original state)
- **Description:** Gmail password hardcoded in class.
- **Recommendation:** Use environment variables (Implemented).

### AP-002 - Serialization Leak in Routes
- **Severity:** **MEDIUM**
- **Location:** `routes/task_routes.py`
- **Description:** JSON construction manual in endpoint handlers.
- **Recommendation:** Use Model `to_dict()` (Implemented).

### AP-003 - Performance N+1 in Task List
- **Severity:** **MEDIUM**
- **Location:** `routes/task_routes.py`
- **Description:** Querying users and categories inside a task loop.
- **Recommendation:** Use `joinedload` (Implemented).

### AP-004 - Deprecated ORM Methods
- **Severity:** **LOW**
- **Location:** CRUD routes.
- **Description:** Use of `query.get()` instead of `session.get()`.
- **Recommendation:** Update to SQLAlchemy 2.0 style (Implemented).

### AP-005 - JSON Response Inconsistency
- **Severity:** **LOW**
- **Location:** `app.py` vs `routes/`
- **Description:** Mixed usage of `jsonify` and raw dicts.
- **Recommendation:** Standardize all responses with `jsonify` (Implemented).

---

## Statistics
- **Total Issues:** 5 (1 Critical, 2 Medium, 2 Low)
