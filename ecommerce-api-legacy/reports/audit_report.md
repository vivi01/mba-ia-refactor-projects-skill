# Audit Report: ecommerce-api-legacy
**Date:** 2026-04-24
**Stack Detected:** Node.js / Express / SQLite3
**Architecture:** Monolithic ("Frankenstein" pattern)

---

## Detailed Findings

### AP-001 - Hardcoded Credentials & Sensitive Data
- **Severity:** **CRITICAL**
- **Location:** `src/utils.js:1`
- **Description:** O arquivo de utilitários contém credenciais de banco de dados e chaves de API de gateway de pagamento expostas diretamente no código.
- **Evidence:** `dbPass: "senha_super_secreta_prod_123"`, `paymentGatewayKey: "pk_live_1234567890abcdef"`
- **Recommendation:** Mover todas as configurações sensíveis para variáveis de ambiente (`process.env`).

### AP-002 - God Object / Frankenstein Manager
- **Severity:** **MEDIUM**
- **Location:** `src/AppManager.js`
- **Description:** A classe `AppManager` é responsável por tudo: inicializar o banco, definir rotas e executar toda a lógica de negócio (checkout, relatórios, auditoria). Isso viola o Princípio da Responsabilidade Única (SRP).
- **Evidence:** Uma única classe de 140 linhas cuidando de persistência, roteamento e fluxos de pagamento.
- **Recommendation:** Separar em `Routes`, `Controllers` e `Models`.

### AP-003 - Insecurity through custom/bad cryptography
- **Severity:** **MEDIUM**
- **Location:** `src/utils.js:20` (badCrypto)
- **Description:** O sistema utiliza uma função de "criptografia" customizada baseada em repetição de base64, que é insegura e previsível para armazenamento de senhas.
- **Evidence:** A função `badCrypto` que apenas transforma a senha em base64 repetidamente.
- **Recommendation:** Utilizar bibliotecas padrão como `bcrypt` ou `argon2` para hashing de senhas.

### AP-004 - Callback Hell & N+1 Queries em Relatórios
- **Severity:** **LOW**
- **Location:** `src/AppManager.js:93` (financial-report)
- **Description:** O endpoint de relatório financeiro utiliza múltiplos callbacks aninhados e executa queries individuais dentro de loops (N+1), o que impacta a performance.
- **Evidence:** `courses.forEach` contendo `this.db.all("SELECT * FROM enrollments...")` que contém mais queries aninhadas.
- **Recommendation:** Refatorar para usar `async/await` e utilizar `JOIN` SQL para consolidar as buscas.

### AP-005 - Falta de Validação de Entrada
- **Severity:** **LOW**
- **Location:** `src/AppManager.js:46` (api/checkout)
- **Description:** Embora haja uma verificação básica de presença de campos, não há validação de formato (ex: formato de email, tamanho de senha, validade do ID do curso).
- **Evidence:** `if (!u || !e || !cid || !cc) return res.status(400).send("Bad Request");`
- **Recommendation:** Utilizar um middleware de validação como `joi` ou `express-validator`.

---

## Statistics
- **Total Issues:** 5
- **Critical/High:** 1
- **Medium:** 2
- **Low:** 2
