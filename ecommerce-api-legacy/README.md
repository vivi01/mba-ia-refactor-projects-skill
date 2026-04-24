# ecommerce-api-legacy

LMS API (com fluxo de checkout) em Node.js/Express usada como entrada do desafio `refactor-arch`.

## Como rodar

```bash
npm install
npm start
```

A aplicação sobe em `http://localhost:3000`. O banco SQLite é em memória e já carrega seeds automaticamente no boot.

Exemplos de requisições estão em `api.http`.

## Análise Manual

### Achados de Auditoria

1. **AP-001 - Credenciais e Dados Sensíveis Expostos (CRITICAL)**
   - **Localização:** `src/utils.js`
   - **Problema:** Senhas e chaves de API codificadas diretamente no código-fonte.
   - **Solução:** Uso de variáveis de ambiente (`.env`).

2. **AP-002 - God Object / Frankenstein Manager (MEDIUM)**
   - **Localização:** `src/AppManager.js`
   - **Problema:** Uma única classe centralizando persistência, rotas e lógica de negócio.
   - **Solução:** Refatoração para o padrão MVC.

3. **AP-003 - Criptografia Customizada Insegura (MEDIUM)**
   - **Localização:** `src/utils.js` (badCrypto)
   - **Problema:** Armazenamento de senhas usando um método previsível e fraco.
   - **Solução:** Implementação de `bcryptjs` para hashing de senhas.

4. **AP-004 - Callback Hell & Problema de Performance N+1 (LOW)**
   - **Localização:** `src/AppManager.js` (financial-report)
   - **Problema:** Queries SQL executadas dentro de loops e excesso de callbacks aninhados.
   - **Solução:** Uso de `async/await` e SQL `JOIN`.

5. **AP-005 - Ausência de Validação de Entrada (LOW)**
   - **Localização:** `src/AppManager.js` (api/checkout)
   - **Problema:** Falta de validação de formato para campos críticos como e-mail.
   - **Solução:** Implementação de camadas de validação nos controllers.

---
*Relatório detalhado disponível em `reports/audit_report.md`.*
