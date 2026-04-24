# task-manager-api

API de Task Manager em Python/Flask usada como entrada do desafio `refactor-arch`.

## Como rodar

```bash
pip install -r requirements.txt
python seed.py
python app.py
```

A aplicação sobe em `http://localhost:5000`. 

## Análise Manual

### Achados de Auditoria

1. **AP-001 - Credenciais de E-mail Hardcoded (CRITICAL)**
   - **Localização:** `services/notification_service.py`
   - **Problema:** Usuário e senha do SMTP expostos no código.
   - **Solução:** Migração para variáveis de ambiente via `.env`.

2. **AP-002 - Fat Routes e Vazamento de Lógica (MEDIUM)**
   - **Localização:** `routes/task_routes.py`
   - **Problema:** Rotas manipulando dicionários manualmente e calculando status.
   - **Solução:** Encapsulamento da lógica de serialização (`to_dict`) e regras de negócio no Model.

3. **AP-003 - Performance: Problema N+1 (MEDIUM)**
   - **Localização:** `routes/task_routes.py` (get_tasks)
   - **Problema:** Uma query SQL por task para buscar o usuário atribuído.
   - **Solução:** Uso de `joinedload` do SQLAlchemy para carregar relações em uma única query.

4. **AP-004 - Uso de Métodos Depreciados (LOW)**
   - **Localização:** Múltiplas rotas.
   - **Problema:** Uso de `Model.query.get()` em vez de `session.get()`.
   - **Solução:** Atualização para os métodos recomendados do SQLAlchemy 2.0+.

5. **AP-005 - Inconsistência na Resposta da API (LOW)**
   - **Localização:** `app.py` vs `routes/`
   - **Problema:** Retorno de dicionários simples misturado com `jsonify`.
   - **Solução:** Padronização global de respostas JSON e códigos de status.

---
*Relatório detalhado disponível em `reports/audit_report.md`.*
