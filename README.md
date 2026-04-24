# Criação de Skills — Refatoração Arquitetural Automatizada

Este projeto apresenta a implementação da Skill **`refactor-arch`** para o Gemini CLI, desenvolvida para analisar, auditar e refatorar aplicações legadas para o padrão MVC em diferentes tecnologias.

---

## 🔍 A) Análise Manual

Abaixo estão os problemas identificados e documentados durante a fase de análise manual dos 3 projetos legados.

### 1. code-smells-project (Python/Flask)
- **AP-001 - SQL Injection (CRITICAL)**: Queries construídas via concatenação de strings.
  - *Justificativa*: Falha de segurança máxima que permite a invasão do banco de dados e vazamento de informações.
- **AP-002 - Lógica de Negócio em Modelos (MEDIUM)**: Cálculos de desconto dentro do `models.py`.
  - *Justificativa*: Viola o SRP (Single Responsibility Principle), dificultando a reutilização de regras de negócio em outras partes do sistema.
- **AP-003 - Tratamento de Erro Genérico (MEDIUM)**: Uso de `except Exception` retornando erros técnicos.
  - *Justificativa*: Compromete a experiência do usuário e pode vazar informações sensíveis do servidor em logs de erro.
- **AP-004 - Ausência de Type Hints (LOW)**: Falta de tipagem estática.
  - *Justificativa*: Reduz a previsibilidade do código e dificulta a manutenção por ferramentas de IDE/Lint.
- **AP-005 - Docstrings Ausentes (LOW)**: Funções sem documentação.
  - *Justificativa*: Aumenta o tempo de onboarding de novos desenvolvedores e a dificuldade de entendimento do propósito das funções.

### 2. ecommerce-api-legacy (Node.js/Express)
- **AP-001 - Hardcoded Credentials (CRITICAL)**: Senhas de DB e API Keys expostas.
  - *Justificativa*: Qualquer pessoa com acesso ao código-fonte pode comprometer o ambiente de produção e o gateway de pagamento.
- **AP-002 - God Object (MEDIUM)**: Classe `AppManager` centralizando todas as responsabilidades.
  - *Justificativa*: Torna o código impossível de testar unitariamente e extremamente frágil a mudanças.
- **AP-003 - Insecure Cryptography (MEDIUM)**: Uso de base64 repetido como hashing.
  - *Justificativa*: Oferece uma falsa sensação de segurança; senhas podem ser facilmente revertidas/quebradas.
- **AP-004 - Performance N+1 (LOW)**: Queries individuais dentro de loops.
  - *Justificativa*: Causa degradação linear de performance conforme o banco de dados cresce.
- **AP-005 - Falta de Validação de Entrada (LOW)**: Ausência de sanitização de inputs.
  - *Justificativa*: Permite a entrada de dados inconsistentes que podem quebrar a aplicação em camadas posteriores.

### 3. task-manager-api (Python/Flask)
- **AP-001 - SMTP Credentials Hardcoded (CRITICAL)**: Senha do Gmail exposta.
  - *Justificativa*: Risco de segurança que pode levar ao uso indevido da conta de e-mail da empresa para SPAM ou phishing.
- **AP-002 - Fat Routes (MEDIUM)**: Lógica de serialização manual dentro das rotas.
  - *Justificativa*: Aumenta a duplicação de código e dificulta a manutenção de padrões de resposta.
- **AP-003 - Performance N+1 em Relacionamentos (MEDIUM)**: Fetching de `User` e `Category` individualmente.
  - *Justificativa*: Gera tráfego excessivo entre a aplicação e o banco de dados.
- **AP-004 - SQLAlchemy Obsoleto (LOW)**: Uso de padrões depreciados (`query.get`).
  - *Justificativa*: Dificulta a migração futura para versões mais recentes do framework.
- **AP-005 - Inconsistência JSON (LOW)**: Retornos variados entre dicionários e `jsonify`.
  - *Justificativa*: Quebra a previsibilidade da API para clientes que esperam headers e formatos consistentes.

---

## 🛠️ B) Construção da Skill

### Decisões de Design
- **Arquitetura Baseada em Referências**: O `SKILL.md` atua como um orquestrador de alto nível. O conhecimento específico (como detectar uma stack Python vs JS) foi isolado em arquivos na pasta `references/` (ex: `analysis_heuristics.md`), garantindo que o SKILL.md permaneça conciso.
- **Progressive Disclosure**: A skill carrega apenas o contexto necessário para cada fase (Análise → Auditoria → Refatoração).

### Anti-patterns Incluídos
Foram incluídos 8 padrões no catálogo (`anti_patterns_catalog.md`), incluindo:
- **SQL Injection**: Foco em segurança.
- **N+1 Query**: Foco em performance.
- **Fat Controller/God Object**: Foco em arquitetura MVC.
- **Deprecated APIs**: Garantia de modernização de bibliotecas.

### Garantia de Skill Agnóstica
- A skill utiliza **heurísticas de arquivo** (presença de `package.json` vs `requirements.txt`) para adaptar os prompts de refatoração dinamicamente.
- Os playbooks de refatoração fornecem exemplos tanto em Python quanto em JavaScript, permitindo que a IA aplique o padrão correto baseada na linguagem detectada na Fase 1.

### Desafios Encontrados
- **Gestão de Processos Windows**: O maior desafio foi lidar com processos Flask/Node que ficavam "presos" nas portas 5000/3000. Resolvemos isso implementando comandos PowerShell na Skill para detectar e encerrar PIDs conflitantes antes da validação.

---

## 📈 C) Resultados

### Resumo de Auditoria
| Projeto | Critical/High | Medium | Low | Total |
| :--- | :---: | :---: | :---: | :---: |
| Project 1 | 1 | 2 | 2 | 5 |
| Project 2 | 1 | 2 | 2 | 5 |
| Project 3 | 1 | 2 | 2 | 5 |

### Comparação Antes vs Depois (MVC)
- **Antes**: Lógica misturada em arquivos únicos, segredos expostos, alto acoplamento.
- **Depois**: 
  - `models/`: Abstração de dados e lógica de negócio.
  - `controllers/`: Orquestração de requisições.
  - `routes/`: Definição limpa de endpoints.
  - `.env`: Segredos protegidos.

### Checklist de Validação (3/3 projetos)
- [x] Linguagem/Framework detectados corretamente.
- [x] Mínimo de 5 findings identificados (1 Crit, 2 Med, 2 Low).
- [x] Estrutura MVC aplicada com sucesso.
- [x] Error handling centralizado.
- [x] Aplicação inicia sem erros e endpoints respondem conforme logs abaixo.

### Logs de Validação Final
```powershell
# Project 1 Root Test
{"mensagem": "API da Loja Refatorada (MVC)", "status": "online"}
# Project 2 Root Test
{"mensagem": "Frankenstein LMS Refatorado (MVC)", "versao": "2.0.0"}
# Project 3 Root Test
{"message": "Task Manager API Refatorada (MVC)", "version": "2.0"}
```

---

## 🚀 D) Como Executar

### Pré-requisitos
- **Gemini CLI** instalado e configurado.
- **Interpretador Python** (acessível via `python` ou caminho absoluto).
- **Node.js** e **npm**.

### Passos para Execução
1. Navegue até a pasta do projeto (ex: `cd code-smells-project`).
2. Garanta que a skill local está vinculada: `gemini skills link ./.gemini/skills/refactor-arch --scope workspace`.
3. Invoque a skill: `/refactor-arch`.
4. Revise o relatório em `reports/` e confirme a refatoração quando solicitado.

### Validação de Funcionalidade
Para validar que a refatoração funcionou, execute:
- **Python**: `python app.py` (dentro da venv criada pela skill).
- **Node.js**: `npm start`.
- Teste o endpoint raiz via navegador ou `curl http://localhost:5000`.

---
*Relatórios detalhados disponíveis na pasta `reports/` na raiz deste repositório.*
