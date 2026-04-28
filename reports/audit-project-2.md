# Audit Report: ecommerce-api-legacy
**Date:** 2026-04-24
**Stack:** Node.js / Express / SQLite3
**Architecture:** MVC (Refactored)

---

## Detailed Findings

### AP-001 - Hardcoded Secrets in Utils
- **Severity:** **CRITICAL**
- **Location:** `src/utils.js:1-7`
- **Description:** Payment Gateway Keys and DB passwords defined directly in source code.
- **Recommendation:** Move to `.env` (Implemented).

### AP-002 - God Object (SRP Violation)
- **Severity:** **MEDIUM**
- **Location:** `src/GodManager.js:4-150`
- **Description:** Single class `AppManager` handling DB, routing, and business logic.
- **Recommendation:** Separate into MVC layers (Implemented).

### AP-003 - Insecure Password Storage
- **Severity:** **MEDIUM**
- **Location:** `src/utils.js:18-24`
- **Description:** Weak custom "cryptography" function `badCrypto` using base64 loops.
- **Recommendation:** Use standard hashing libraries like `bcryptjs` (Implemented).

### AP-004 - Performance N+1 in Reports
- **Severity:** **LOW**
- **Location:** `src/GodManager.js:93-138`
- **Description:** Nested SQL queries inside loops for generating financial reports.
- **Recommendation:** Use SQL JOINs to consolidate queries (Implemented).

### AP-005 - Input Validation Gap
- **Severity:** **LOW**
- **Location:** `src/GodManager.js:43-85`
- **Description:** Missing email and card format validation in the checkout flow.
- **Recommendation:** Use validation middleware (Implemented basic checks).

---

## Statistics
- **Total Issues:** 5 (1 Critical, 2 Medium, 2 Low)
