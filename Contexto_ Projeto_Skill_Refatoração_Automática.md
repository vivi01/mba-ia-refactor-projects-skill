# Contexto do Projeto — Skill de Refatoração Automática MVC (Gemini CLI)

## 1. Visão Geral
O projeto consiste na criação de uma **Skill para o Gemini CLI** capaz de analisar, auditar e refatorar codebases legadas automaticamente, independentemente da tecnologia utilizada. A Skill deve detectar problemas arquiteturais, de segurança e qualidade de código, gerar um relatório estruturado e refatorar a aplicação para o padrão **MVC**, garantindo que o sistema continue funcional após as mudanças.

---

## 2. Problema
O projeto resolve problemas simultâneos em sistemas legados:
* Alto custo de análise manual de código.
* Arquiteturas inconsistentes ou inexistentes.
* Violações de boas práticas (MVC, SOLID).
* Vulnerabilidades de segurança.
* Baixa qualidade e manutenção difícil.

---

## 3. Objetivo
Criar uma Skill capaz de:
* Analisar automaticamente qualquer codebase.
* Detectar stack, framework e arquitetura atual.
* Identificar anti-patterns com severidade.
* Gerar relatório de auditoria estruturado.
* Refatorar para o padrão MVC.
* Validar o funcionamento da aplicação após as mudanças.
* Operar de forma agnóstica à tecnologia.

---

## 4. Escopo da Skill
A execução é dividida em três fases obrigatórias:

### Fase 1 — Análise
* Detectar linguagem, framework e arquitetura.
* Mapear a estrutura do projeto.
* Gerar um resumo da aplicação.

### Fase 2 — Auditoria
* Identificar anti-patterns e *code smells*.
* Classificar severidade (**CRITICAL, HIGH, MEDIUM, LOW**).
* Gerar relatório estruturado com localização exata (arquivo e linha).
* **Pausar para confirmação** antes de seguir para a Fase 3.

### Fase 3 — Refatoração
* Reestruturar para MVC (separar Models, Views/Routes e Controllers).
* Remover configurações *hardcoded*.
* Centralizar o tratamento de erros (*error handling*).
* Garantir o funcionamento da aplicação e validar endpoints.

---

## 5. Requisitos Técnicos
* **Ferramenta:** Gemini CLI.
* **Uso de Custom Skills:** Estrutura baseada em Markdown (`SKILL.md`).
* **Arquivos de referência:** Uso obrigatório.
* **Suporte:** Múltiplas linguagens.

---

# Technical Context & Severity Scale
To standardize auditing, the following severity levels must be used:
* **CRITICAL**: Severe architectural or security flaws (e.g., hardcoded credentials, SQL Injection, "God Classes" violating separation of concerns).
* **HIGH**: Strong violations of MVC or SOLID principles that hinder maintenance and testing (e.g., heavy business logic in Controllers, tight coupling).
* **MEDIUM**: Standardization issues, code duplication, or moderate performance bottlenecks (e.g., N+1 queries, missing route validations).
* **LOW**: Readability improvements, poor variable naming, or "magic numbers."

---

## 7. Catálogo e Playbook
* **Detecção:** Mínimo de 8 anti-patterns detectáveis, incluindo obrigatoriamente APIs *deprecated*.
* **Transformação:** Mínimo de 8 transformações de refatoração com exemplos de "antes/depois".
* **Cobertura:** Foco em MVC, SOLID e segurança.

* Os arquivos de referência devem cobrir obrigatoriamente as seguintes áreas de conhecimento:

* **Análise de projeto: Heurísticas para detecção de linguagem, framework, banco de dados e mapeamento de arquitetura
* **Catálogo de anti-patterns: Anti-patterns com sinais de detecção e classificação de severidade
* **Template de relatório: Formato padronizado do relatório de auditoria (Fase 2)
* **Guidelines de arquitetura: Regras do padrão MVC alvo (camadas Models, Views/Routes e Controllers)
* **Playbook de refatoração: Padrões concretos de transformação para cada anti-pattern (com exemplos de código)
---

## 8. Projetos de Teste
A validação será feita nos seguintes ambientes:
* **Python/Flask:** 2 projetos.
* **Node.js/Express:** 1 projeto.

---

## 9. Execução
* **Comando:** Skill invocada via `/refactor-arch` no Gemini CLI.
* **Fluxo:** Execução faseada obrigatória com pausa antes da refatoração.
* **Logs:** Relatórios salvos no diretório `/reports`.
* **Versionamento:** Commit automático após a conclusão de cada projeto.

---

## 10. Validação de Sucesso

| Fase | Critérios de Aceite |
| :--- | :--- |
| **Fase 1** | Stack correta, arquitetura identificada e resumo coerente. |
| **Fase 2** | No mínimo 5 achados, severidade correta e relatório estruturado. |
| **Fase 3** | Estrutura MVC aplicada, aplicação inicia sem erros e endpoints preservados. |

> **Resultado Final:** Skill capaz de automatizar auditoria e refatoração completa de sistemas legados com validação de qualidade e segurança.