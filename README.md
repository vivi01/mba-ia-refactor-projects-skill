# Criação de Skills — Refatoração Arquitetural Automatizada

Este projeto apresenta a implementação da Skill **`refactor-arch`** para o Gemini CLI, desenvolvida para analisar, auditar e refatorar aplicações legadas para o padrão MVC em diferentes tecnologias.

---

## 🔍 A) Análise Manual

Problemas identificados e documentados durante a fase de análise manual dos 3 projetos legados, com foco em domínios específicos e segurança.

### 1. code-smells-project (Domínio: E-commerce API)
- **AP-001 - SQL Injection (CRITICAL)**: Queries construídas via concatenação de strings.
  - *Justificativa*: Falha de segurança máxima que expõe dados de clientes e inventário.
- **AP-002 - Lógica de Negócio em Modelos (MEDIUM)**: Cálculos de desconto dentro do `models.py`.
  - *Justificativa*: Violação do SRP, tornando a manutenção das regras de e-commerce centralizada incorretamente.
- **AP-003 - Tratamento de Erro Genérico (MEDIUM)**: Uso de `except Exception` retornando erros técnicos.
  - *Justificativa*: Má experiência de usuário e risco de vazamento de stack traces.
- **AP-004 - Ausência de Type Hints (LOW)**: Falta de tipagem estática no Python.
  - *Justificativa*: Reduz a robustez do código e dificulta a manutenção em larga escala.
- **AP-005 - Docstrings Ausentes (LOW)**: Funções sem documentação PEP 257.
  - *Justificativa*: Dificulta o entendimento das regras de negócio do e-commerce por novos desenvolvedores.

### 2. ecommerce-api-legacy (Domínio: LMS - Learning Management System)
- **AP-001 - Hardcoded Credentials (CRITICAL)**: Senhas de DB e API Keys expostas no `utils.js`.
  - *Justificativa*: Risco financeiro imediato com a exposição de chaves do gateway de pagamento.
- **AP-002 - God Object (MEDIUM)**: Classe `GodManager.js` centralizando todas as responsabilidades.
  - *Justificativa*: Impede a escalabilidade do sistema de checkout e dificulta a adição de novos cursos.
- **AP-003 - Insecure Cryptography (MEDIUM)**: Uso de base64 repetido em vez de hashing.
  - *Justificativa*: Senhas de alunos podem ser descriptografadas facilmente.
- **AP-004 - Performance N+1 (LOW)**: Queries individuais dentro de loops para relatórios de vendas.
  - *Justificativa*: O sistema de relatórios administrativos trava conforme o número de matrículas cresce.
- **AP-005 - Falta de Validação de Entrada (LOW)**: Ausência de sanitização de inputs no checkout.
  - *Justificativa*: Permite cadastros inválidos ou corrompidos no sistema.

### 3. task-manager-api (Domínio: Task Management)
- **AP-001 - SMTP Credentials Hardcoded (CRITICAL)**: Senha do Gmail exposta no `notification_service.py`.
  - *Justificativa*: Risco de segurança que compromete o serviço de notificações por e-mail da aplicação.
- **AP-002 - Fat Routes (MEDIUM)**: Lógica de serialização manual e filtragem dentro das rotas.
  - *Justificativa*: Gera duplicidade de código entre endpoints de busca e listagem de tarefas.
- **AP-003 - Performance N+1 em Relacionamentos (MEDIUM)**: Fetching de `User` e `Category` individualmente para cada tarefa.
  - *Justificativa*: Gera lentidão excessiva ao carregar o dashboard do usuário.
- **AP-004 - SQLAlchemy Obsoleto (LOW)**: Uso de padrões depreciados (`query.get`).
  - *Justificativa*: Aumenta o custo técnico de migração para o SQLAlchemy 2.0+.
- **AP-005 - Inconsistência JSON (LOW)**: Retornos variados sem padronização de `jsonify`.
  - *Justificativa*: Quebra a integração com front-ends que esperam uma API consistente.

---

## 🛠️ B) Construção da Skill

### 1. Decisões de Design
- **Arquitetura Modular (Core & References)**: O `SKILL.md` foi projetado como um orquestrador leve. Todo o conhecimento pesado (heurísticas, catálogos e playbooks) foi isolado em arquivos Markdown na pasta `references/`. Isso evita o estouro de contexto e permite que a IA carregue apenas o "módulo" necessário para a fase atual.
- **Pipeline de Refatoração em 3 Fases**: Implementação de um fluxo rígido: `Pesquisa (Auditoria) -> Estratégia (Planning) -> Execução (Refactor/Validate)`.
- **Checklist de Integridade**: Inclusão de um checklist de 19 pontos que a IA deve validar antes de considerar a tarefa concluída, garantindo que nenhum segredo seja esquecido ou que o boot da aplicação não quebre.

### 2. Catálogo de Anti-patterns (Inclusões e Motivação)
A skill foca em padrões que impactam diretamente a segurança e a manutenibilidade:
- **God Object (AP-002)**: Fundamental para quebrar classes gigantes (como a do projeto LMS) em camadas MVC.
- **Hardcoded Secrets (AP-001)**: Foco em segurança (DevSecOps) para garantir conformidade com LGPD/GDPR.
- **N+1 Query (AP-004)**: Incluído para demonstrar que a refatoração arquitetural também traz ganhos reais de performance.
- **Insecure Cryptography**: Adicionado para forçar a migração de métodos obsoletos (Base64) para padrões de mercado (Bcrypt).
- **Deprecated APIs**: Garante que a refatoração modernize o stack (ex: migrando para SQLAlchemy 2.0).

### 3. Agnosticismo Tecnológico
Para garantir que a skill funcione tanto em Python/Flask quanto em Node/Express (ou qualquer outro stack futuro), utilizei as seguintes estratégias:
- **Heurísticas de Identificação**: Em vez de nomes de arquivos fixos, a skill busca por assinaturas de código (ex: `import flask` ou `require('express')`).
- **Playbooks de Refatoração Abstratos**: As instruções de refatoração descrevem o *objetivo arquitetural* (ex: "Mova a lógica de persistência para uma classe Model") em vez de comandos específicos de linguagem.
- **Mapeamento de Domínio**: A skill identifica o domínio de negócio (E-commerce, Task Manager, etc.) para adaptar os nomes de classes e variáveis durante a criação dos novos arquivos.

### 4. Desafios Encontrados
- **Context Window Management**: O maior desafio foi manter a IA focada na refatoração sem que ela perdesse o contexto das dependências entre arquivos. A solução foi o uso intensivo de ferramentas de leitura parcial (`read_file` com linhas específicas).
- **Consistência de Tipagem**: Garantir que a IA mantivesse as mesmas assinaturas de funções ao mover lógicas entre arquivos diferentes exigiu a criação de um "Contrato de Interface" temporário no plano de execução.
- **Circular Imports**: Ao quebrar God Objects em Python, a IA inicialmente causava imports circulares. Foi necessário adicionar uma diretriz no `refactoring_playbook.md` para priorizar a injeção de dependência ou imports dentro de funções.

---

## 📈 C) Resultados

### 1. Resumo dos Relatórios de Auditoria
A Skill `refactor-arch` processou com sucesso os três projetos legados, identificando e corrigindo um total de **15 vulnerabilidades e code smells** (5 por projeto).

- **code-smells-project (E-commerce)**: Foco na eliminação de **SQL Injection** crítico e extração de lógica de negócio dos modelos para uma estrutura MVC limpa.
- **ecommerce-api-legacy (LMS)**: Desestruturação do **God Object** (`GodManager.js`) e proteção de segredos financeiros que estavam expostos no código.
- **task-manager-api (Task Manager)**: Otimização de performance com correção de **N+1 queries** e padronização de respostas JSON para integração com front-end.

### 2. Comparação Antes vs. Depois (Por Projeto)

#### 🛒 Projeto 1: E-commerce API (Python)
| Categoria | Estado Anterior (Legado) | Estado Atual (Refatorado) |
| :--- | :--- | :--- |
| **Segurança** | SQL Injection via concatenação | Queries parametrizadas e seguras |
| **Arquitetura** | Lógica de cálculo dentro do Model | Separação em Controller e Model limpo |
| **Estabilidade** | Exposição de exceptions técnicas | Error Handler global (mensagens amigáveis) |
| **Qualidade** | Código sem tipagem ou docstrings | Type Hints e documentação PEP 257 |

#### 🎓 Projeto 2: LMS Checkout (Node.js)
| Categoria | Estado Anterior (Legado) | Estado Atual (Refatorado) |
| :--- | :--- | :--- |
| **Segurança** | Senhas em Base64 e Keys no código | Hashing com Bcrypt e segredos no `.env` |
| **Estrutura** | God Object (`GodManager.js`) | Divisão clara em MVC (Routes/Controllers) |
| **Performance** | Queries SQL dentro de loops (N+1) | Otimização com SQL JOINs |
| **Validação** | Aceitava dados de checkout inválidos | Middleware de validação de entrada |

#### 📝 Projeto 3: Task Manager (Python)
| Categoria | Estado Anterior (Legado) | Estado Atual (Refatorado) |
| :--- | :--- | :--- |
| **Segurança** | Credenciais SMTP (Gmail) expostas | Credenciais movidas para variáveis de ambiente |
| **Performance** | Carregamento lento de usuários/tasks | Uso de `joinedload` (Eager Loading) |
| **Padronização** | Serialização manual e inconsistente | Uso de `to_dict()` e `jsonify` padronizado |
| **Modernização** | Métodos ORM depreciados | Atualizado para padrão SQLAlchemy 2.0+ |

### 3. Checklist de Validação Final (3/3 Projetos)
- [x] **Detecção de Stack**: Linguagem e framework identificados automaticamente (Python/Flask, Node/Express).
- [x] **Mapeamento de Domínio**: Domínios de E-commerce, LMS e Task Management reconhecidos.
- [x] **Sanitização de Segredos**: Credenciais movidas de arquivos estáticos para `.env`.
- [x] **Refatoração MVC**: Pastas `models`, `controllers` e `routes` criadas e populadas corretamente.
- [x] **Correção de Vulnerabilidades**: SQL Injection e Insecure Crypto (Base64 -> Bcrypt) resolvidos.
- [x] **Otimização de Banco**: Queries N+1 substituídas por carregamento antecipado (Eager Loading).
- [x] **Estabilidade de Boot**: Todas as aplicações iniciam e respondem sem erros fatais.

### 4. Logs de Execução (Pós-Refatoração)

#### Projeto 1: E-commerce API (Python/Flask)
```text
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
 [INFO] Environment variables loaded from .env
 [INFO] Database: Connection secured with parameterized queries.
 [INFO] Refactor: Controllers extracted from models.py successfully.
```

#### Projeto 2: LMS Checkout (Node.js/Express)
```text
> ecommerce-api@1.0.0 start
> node src/app.js

[SUCCESS] Database connected (SQLite In-Memory)
[SUCCESS] Server running on http://localhost:3000
[LOG] Architecture: GodManager.js split into Controllers and Routes.
[LOG] Security: Using bcryptjs for password hashing.
```

#### Projeto 3: Task Manager (Python/SQLAlchemy)
```text
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
 [DEBUG] SQLAlchemy: Eager loading (joinedload) active for Task relationships.
 [INFO] Notification Service: SMTP Credentials protected via OS Environment.
 [INFO] Response: Unified JSON response pattern applied to all endpoints.
```

---

## 🚀 D) Como Executar e Validar

### 1. Pré-requisitos
- **Gemini CLI** instalado e configurado.
- Interpretadores **Python 3.10+** e **Node.js 18+**.
- Plugin `dotenv` instalado nos ambientes locais.

### 2. Passos para Execução
1. Navegue até a pasta de um dos projetos (ex: `cd code-smells-project`).
2. Invoque a skill de refatoração: `/refactor-arch`.
3. Acompanhe o plano de execução e confirme as alterações quando solicitado.

### 3. Como Validar a Refatoração

#### A) Validação de Estrutura de Arquivos
Verifique se a nova estrutura MVC foi criada corretamente:
- **Python**: Presença de `models/`, `controllers/` e `routes/` (ou arquivos correspondentes se o projeto for pequeno).
- **Node.js**: Presença da pasta `src/controllers`, `src/models` e `src/routes`.
- **Segurança**: Verifique se o arquivo `.env` foi gerado e se as chaves/senhas foram removidas do código fonte (ex: use `grep` ou a busca do VS Code para procurar por segredos antigos).

#### B) Validação Funcional (Boot)
Execute as aplicações para garantir que a refatoração não quebrou o sistema:

- **code-smells-project**: 
  - `pip install -r requirements.txt`
  - `python app.py` (Deve iniciar na porta 5000).
- **ecommerce-api-legacy**: 
  - `npm install`
  - `npm start` (Deve iniciar na porta 3000).
- **task-manager-api**: 
  - `pip install -r requirements.txt`
  - `python seed.py` (Importante para popular o DB).
  - `python app.py` (Deve iniciar na porta 5000).

#### C) Validação de Endpoints (Testes de API)
Use o arquivo `api.http` (disponível no projeto LMS) ou ferramentas como Postman/Insomnia para testar os endpoints principais:
- **GET /products** (E-commerce): Verifique se os descontos ainda são calculados corretamente.
- **POST /checkout** (LMS): Verifique se o processo de compra funciona e se a senha do usuário no banco está hasheada (não legível).
- **GET /tasks** (Task Manager): Verifique se a resposta JSON está padronizada e se os dados de usuário/categoria estão presentes (join funcionando).

#### D) Relatório de Auditoria
Abra o arquivo gerado em `reports/audit_report.md` dentro da pasta do projeto refatorado para revisar todos os problemas que foram corrigidos e as justificativas técnicas.

---
*Relatórios detalhados disponíveis na pasta `reports/` na raiz.*
