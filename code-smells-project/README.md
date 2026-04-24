# code-smells-project

API de E-commerce em Python/Flask usada como entrada do desafio `refactor-arch`.

## Como rodar

```bash
pip install -r requirements.txt
python app.py
```

A aplicação sobe em `http://localhost:5000`. O banco SQLite (`loja.db`) é criado automaticamente no primeiro boot, já com produtos e usuários de exemplo.

## Análise Manual

### Achados de Auditoria

1. **AP-001 - Vulnerabilidade de SQL Injection (CRITICAL)**
   - **Localização:** `models.py`
   - **Problema:** Queries SQL construídas via concatenação de strings, permitindo ataques de injeção.
   - **Solução:** Implementação de queries parametrizadas.

2. **AP-002 - Lógica de Negócio em Modelos / Fat Models (MEDIUM)**
   - **Localização:** `models.py:relatorio_vendas`
   - **Problema:** Regras de negócio complexas (como cálculo de descontos) inseridas diretamente na camada de dados.
   - **Solução:** Centralização de constantes e separação de responsabilidades.

3. **AP-003 - Tratamento de Erro Genérico e Expositivo (MEDIUM)**
   - **Localização:** `controllers.py`
   - **Problema:** Captura genérica de exceções retornando mensagens técnicas brutas ao cliente.
   - **Solução:** Implementação de um Error Handler global no Flask.

4. **AP-004 - Ausência de Tipagem Sugerida / Type Hints (LOW)**
   - **Localização:** Múltiplos arquivos.
   - **Problema:** Falta de anotações de tipo, dificultando a manutenção e análise estática.
   - **Solução:** Adição de Type Hints em todas as assinaturas de funções.

5. **AP-005 - Falta de Documentação Interna / Docstrings (LOW)**
   - **Localização:** Todo o projeto.
   - **Problema:** Ausência de docstrings seguindo a PEP 257.
   - **Solução:** Documentação de todas as funções, parâmetros e retornos.

---
*Relatório detalhado disponível em `reports/audit_report_final.md`.*
