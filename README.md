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

### Decisões de Design
- **Arquitetura Baseada em Referências**: O `SKILL.md` atua como orquestrador. O conhecimento específico foi isolado na pasta `references/`, permitindo que a IA carregue apenas as heurísticas e playbooks necessários.
- **Checklist de Validação Integrado**: Inclusão de um checklist obrigatório de 19 pontos no coração da Skill para garantir conformidade em todas as fases.

### Anti-patterns e Diferencial
- Foram incluídos 8 padrões no catálogo, com destaque para a detecção de **APIs Deprecated**, garantindo que a refatoração não apenas mude a estrutura, mas modernize as bibliotecas utilizadas.

### Garantia de Skill Agnóstica
- A skill utiliza **heurísticas de arquivo** e **identificação de domínio** para adaptar sua linguagem. Ela identifica o domínio (E-commerce, LMS ou Task Management) na Fase 1 e utiliza playbooks de refatoração poliglotas (Python/JS).

---

## 📈 C) Resultados

### Resumo de Auditoria e Melhorias
- **Project 1 (Python)**: Removido SQL Injection; Implementado Type Hints e Error Handler Global.
- **Project 2 (Node.js)**: Removido God Object; Implementado Bcryptjs e SQL JOIN.
- **Project 3 (Python)**: Otimizado performance N+1 com `joinedload`; Padronizado todas as respostas com `jsonify`.

### Checklist de Validação Final (3/3 projetos)
- [x] Linguagem/Framework detectados corretamente.
- [x] Domínio da aplicação (E-commerce, LMS, Task Management) descrito com precisão.
- [x] Mínimo de 5 findings identificados (1 Crit/High, 2 Med, 2 Low).
- [x] Estrutura MVC aplicada e segredos movidos para `.env`.
- [x] Aplicação inicia sem erros e endpoints validados.

---

## 🚀 D) Como Executar

### Pré-requisitos
- **Gemini CLI** e interpretadores **Python/Node.js**.

### Passos
1. Entre na pasta do projeto legatário.
2. Invoque a skill: `/refactor-arch`.
3. Verifique o relatório gerado em `reports/audit-project-x.md`.
4. Confirme a refatoração e valide o boot.

---
*Relatórios detalhados disponíveis na pasta `reports/` na raiz.*
