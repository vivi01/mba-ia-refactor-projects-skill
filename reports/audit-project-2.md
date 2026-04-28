# Audit Report: ecommerce-api-legacy
**Date:** 2026-04-24
**Stack:** Node.js / Express / SQLite3
**Architecture:** MVC (Refactored)

---

## Detailed Findings

### AP-001 - Hardcoded Secrets in Utils
- **Severity:** **CRITICAL**
- **Location:** `src/utils.js:1-7` (Original state)
- **Description:** Payment Gateway Keys and DB passwords in source code.
- **Recommendation:** Move to `.env` (Implemented).

### AP-002 - God Object (SRP Violation)
- **Severity:** **MEDIUM**
- **Location:** `src/GodManager.js:4-150`
- **Description:** Single class handling DB, routing, and logic.
- **Recommendation:** Separate into MVC layers (Implemented).

### AP-003 - Insecure Password Storage
- **Severity:** **MEDIUM**
- **Location:** `src/utils.js:19-26` (badCrypto)
- **Description:** Base64 transformation used as security.
- **Recommendation:** Use `bcryptjs` (Implemented).

### AP-004 - Performance N+1 in Reports
- **Severity:** **LOW**
- **Location:** `src/GodManager.js:92-135`
- **Description:** SQL queries inside loops for financial reports.
- **Recommendation:** Use SQL JOINs (Implemented).

### AP-005 - Input Validation Gap
- **Severity:** **LOW**
- **Location:** `src/GodManager.js:41-47` (Checkout flow)
- **Description:** Missing e-mail and card format validation.
- **Recommendation:** Use validation middleware (Implemented basic checks).

---

## Statistics
- **Total Issues:** 5 (1 Critical, 2 Medium, 2 Low)
