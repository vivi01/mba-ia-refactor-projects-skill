# Audit Report: code-smells-project (Revised)
**Date:** 2026-04-24
**Stack Detected:** Python / Flask / SQLite
**Architecture:** Monolithic (Legacy/Spaghetti)

---

## Detailed Findings

### AP-001 - SQL Injection Vulnerability
- **Severity:** **CRITICAL**
- **Location:** `models.py:27`, `models.py:46`, `models.py:100`
- **Description:** Multiple functions build SQL queries using direct string concatenation with user input, allowing attackers to manipulate or dump the database.
- **Evidence:** `cursor.execute("SELECT * FROM produtos WHERE id = " + str(id))`
- **Recommendation:** Use parameterized queries.

### AP-002 - N+1 Query Problem in Order Retrieval
- **Severity:** **MEDIUM**
- **Location:** `models.py:158` (get_pedidos_usuario)
- **Description:** Fetching items for each order inside a loop results in multiple database round-trips (N+1), which will significantly slow down the API as the number of orders grows.
- **Evidence:** A `cursor2.execute` call is nested within a `for row in rows` loop.
- **Recommendation:** Use a SQL `JOIN` or `IN` clause to fetch all items in one or two queries.

### AP-003 - Redundant Data Fetching in Health Check
- **Severity:** **MEDIUM**
- **Location:** `controllers.py:273` (health_check)
- **Description:** The health check endpoint performs multiple `SELECT COUNT(*)` queries on different tables sequentially rather than in a single batch or using a more optimized metadata check.
- **Evidence:** Three separate `cursor.execute("SELECT COUNT(*) FROM ...")` calls.
- **Recommendation:** Consolidate queries or cache counts if the database is large.

### AP-004 - Inconsistent Variable Naming (Snake_case vs CamelCase)
- **Severity:** **LOW**
- **Location:** `models.py:127` (criar_pedido)
- **Description:** The codebase uses `usuario_id` (snake_case) in some areas but inconsistently handles internal variables, drifting away from PEP 8 standards in some local contexts.
- **Evidence:** `usuario_id = dados.get("usuario_id")` mixed with logic that could be more pythonic.
- **Recommendation:** Standardize all variables to `snake_case` according to PEP 8.

### AP-005 - Use of Magic Numbers in Discount Logic
- **Severity:** **LOW**
- **Location:** `models.py:221` (relatorio_vendas)
- **Description:** The discount calculation uses numeric literals directly in the logic without naming them as constants, making the business rules harder to read and maintain.
- **Evidence:** `if faturamento > 10000: desconto = faturamento * 0.1`
- **Recommendation:** Define constants like `TIER_1_THRESHOLD = 10000` and `TIER_1_DISCOUNT = 0.1`.

---

## Statistics
- **Total Issues:** 5
- **Critical/High:** 1
- **Medium:** 2
- **Low:** 2
