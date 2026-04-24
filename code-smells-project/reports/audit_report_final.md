# Audit Report: code-smells-project (Final Criteria)
**Date:** 2026-04-24
**Stack Detected:** Python / Flask / SQLite
**Architecture:** Monolithic (Spaghetti)

---

## Detailed Findings

### AP-001 - SQL Injection Vulnerability
- **Severity:** **CRITICAL**
- **Location:** `models.py`
- **Description:** Uso de concatenação de strings para montar queries SQL.
- **Evidence:** `cursor.execute("SELECT * FROM produtos WHERE id = " + str(id))`
- **Recommendation:** Utilizar queries parametrizadas.

### AP-002 - Lógica de Negócio em Modelos (Fat Models)
- **Severity:** **MEDIUM**
- **Location:** `models.py:relatorio_vendas`
- **Description:** O modelo contém regras de cálculo de desconto.
- **Evidence:** Cálculos de `desconto` baseados em faixas de faturamento.
- **Recommendation:** Mover cálculos de negócio para a camada de Controller ou Service.

### AP-003 - Tratamento de Erro Genérico
- **Severity:** **MEDIUM**
- **Location:** `controllers.py`
- **Description:** Uso excessivo de `try...except Exception` retornando erros brutos.
- **Evidence:** `except Exception as e: return jsonify({"erro": str(e)}), 500`
- **Recommendation:** Implementar handler global de erros.

### AP-004 - Ausência de Tipagem Sugerida (Type Hints)
- **Severity:** **LOW**
- **Location:** `models.py` / `controllers.py`
- **Description:** Falta de Type Hints do Python 3.
- **Evidence:** `def buscar_produto(id):`
- **Recommendation:** Adicionar Type Hints.

### AP-005 - Docstrings Ausentes
- **Severity:** **LOW**
- **Location:** Todo o projeto.
- **Description:** Funções e módulos sem documentação interna.
- **Evidence:** Falta de PEP 257.
- **Recommendation:** Adicionar docstrings.

---

## Statistics
- **Total Issues:** 5
- **Critical/High:** 1
- **Medium:** 2
- **Low:** 2
