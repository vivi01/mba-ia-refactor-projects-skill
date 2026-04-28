# Audit Report: task-manager-api
**Date:** 2026-04-24
**Stack Detected:** Python / Flask / Flask-SQLAlchemy
**Architecture:** Layered (Partial MVC)

---

## Detailed Findings

### AP-001 - Credenciais de E-mail Hardcoded
- **Severity:** **CRITICAL**
- **Location:** `services/notification_service.py:7-11`
- **Description:** O serviço de notificação contém credenciais de login do Gmail codificadas diretamente.
- **Evidence:** `self.email_user = 'taskmanager@gmail.com'`, `self.email_password = 'senha123'`
- **Recommendation:** Mover credenciais para variáveis de ambiente (`.env`).

### AP-002 - Acoplamento e Vazamento de Responsabilidade (Fat Routes)
- **Severity:** **MEDIUM**
- **Location:** `routes/task_routes.py:11-14`
- **Description:** As rotas contêm lógica excessiva de manipulação de dados que deveria estar no Model ou Controller.
- **Evidence:** Loop `for` manual para reconstruir o JSON de cada task.
- **Recommendation:** Usar métodos do Model ou Controllers dedicados.

### AP-003 - Problema de Performance N+1 no Endpoint de Tasks
- **Severity:** **MEDIUM**
- **Location:** `routes/task_routes.py:12-13`
- **Description:** Queries individuais para relações dentro de um loop de listagem.
- **Evidence:** `User.query.get(t.user_id)` dentro do loop.
- **Recommendation:** Usar `joinedload` do SQLAlchemy.

### AP-004 - Uso de Métodos Deprecated do SQLAlchemy
- **Severity:** **LOW**
- **Location:** `routes/task_routes.py:18-22`, `routes/task_routes.py:58-63`
- **Description:** Uso de `query.get()`.
- **Evidence:** `task = Task.query.get(task_id)`
- **Recommendation:** Atualizar para `db.session.get()`.

### AP-005 - Inconsistência no Formato de Resposta JSON
- **Severity:** **LOW**
- **Location:** `app.py:34-40`, `routes/task_routes.py:1-75`
- **Description:** Uso inconsistente de `jsonify` vs retornos de dicionários simples.
- **Evidence:** `return {'status': 'ok'}` vs `return jsonify(data)`.
- **Recommendation:** Padronizar todas as respostas com `jsonify`.

---

## Statistics
- **Total Issues:** 5
- **Critical/High:** 1
- **Medium:** 2
- **Low:** 2
