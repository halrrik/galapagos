---
origem: Documento de Processos Tecnologia.docx
status: convertido_para_markdown
classificacao_sugerida: revisar_antes_de_publicar
aplicacao: Grimorio Versao Galapagos
---

# Artefatos e Hierarquia de Trabalho

## 1. Objetivo desta Parte

Esta parte define **quais tipos de artefatos existem**, **quando cada um deve ser utilizado** e **como eles se relacionam hierarquicamente** dentro do sistema da área de tecnologia.

Seu objetivo é eliminar dúvidas recorrentes como:

- “Isso é épico ou feature?”

- “Posso abrir direto uma história?”

- “Quando usar solicitação?”

- “Bug é demanda ou incidente?”

Aqui não há julgamento de valor. Há **uso correto**.

## 2. Visão Geral da Hierarquia

A hierarquia de trabalho segue uma lógica de **redução progressiva de incerteza** e de **rastreabilidade total**:

**Iniciativa → Épico → Feature → Story / Solicitação → Task / Bug**

Todos os artefatos do sistema **devem obrigatoriamente possuir um relacionamento de pai–filho**, respeitando essa hierarquia.

Não pode existir nenhuma demanda órfã no sistema.

Isso garante:

- Clareza de contexto

- Rastreabilidade de decisão

- Leitura correta de impacto e prioridade

- Métricas confiáveis em todos os níveis

Criar um item sem pai é considerado **erro de uso do sistema**, não exceção operacional.

## 3. Iniciativa

**O que é**

Iniciativa representa um **direcionamento estratégico** ou um **problema relevante de negócio ou tecnologia** que precisa ser tratado.

Ela responde à pergunta:

*Por que isso deve existir?*

**Quando usar**

- Novos produtos

- Grandes mudanças estruturais

- Demandas regulatórias relevantes

- Iniciativas transversais entre times

**Quando não usar**

- Ajustes pontuais

- Correções técnicas isoladas

- Melhorias incrementais pequenas

**Responsabilidades**

- Criação: Liderança / Gestão

- Evolução: Produto + Tecnologia

- Encerramento: Liderança

A Iniciativa **não é item de execução**.

## 4. Épico

**O que é**

Épico é um **recorte estruturado de uma iniciativa**, ainda grande demais para execução direta, mas já delimitado em escopo.

Ele responde à pergunta:

*O que precisa ser feito para atender esta iniciativa?*

**Quando usar**

- Quebra de iniciativas em frentes lógicas

- Agrupamento de features relacionadas

- Para definir possíveis MVP

**Quando não usar**

- Para organizar tarefas

- Como substituto de feature

**Responsabilidades**

- Criação: Produto / Tecnologia

- Detalhamento: Produto

- Validação técnica: Tech Lead

## 5. Feature

**O que é**

Feature representa uma **capacidade funcional completa**, percebida pelo usuário ou sistema.

Ela responde à pergunta:

*Qual valor concreto será entregue?*

**Quando usar**

- Funcionalidades completas

- Entregas com valor mensurável

**Quando não usar**

- Para pequenas mudanças

- Para bugs

**Responsabilidades**

- Criação: Produto

- Viabilidade técnica: Tech Lead

- Priorização: Gestão

Feature **organiza trabalho**, não executa trabalho.

## 6. User Story

**O que é**

User Story é a **unidade padrão de entrega**.

Ela responde à pergunta:

*O que será desenvolvido agora?*

**Quando usar**

- Desenvolvimento de novas funcionalidades

- Melhorias funcionais

**Quando não usar**

- Para solicitações vagas

- Para bugs simples

**Responsabilidades**

- Criação: Produto

- Execução: Time

- Validação: Produto / Qualidade

## 7. Solicitação

**O que é**

Solicitação é uma **demanda estruturada**, mas que não nasce como história clássica.

Ela responde à pergunta:

*Há algo que precisa ser analisado, atendido, ajustado ou convertido?*

**Quando usar**

- Demandas externas

- Pedidos operacionais

- Ajustes que ainda exigem avaliação

**Quando não usar**

- Como atalho para execução

- Para substituir história refinada

Solicitação pode:

- Ser atendida diretamente

- Ser convertida em User Story

## 8. Bug

**O que é**

Bug representa um **desvio de comportamento esperado** em algo já entregue.

Ele responde à pergunta:

*O que quebrou ou não funciona como deveria?*

**Quando usar**

- Erros em produção

- Falhas identificadas em testes

**Quando não usar**

- Para novas funcionalidades

- Para mudanças de escopo

Bug pode ser filho de uma história ou existir de forma independente.

## 9. Task

**O que é**

Task representa uma **atividade técnica específica**.

Ela responde à pergunta:

*Qual ação concreta precisa ser feita?*

**Quando usar**

- Quebra técnica de histórias

- Atividades de apoio

**Quando não usar**

- Como item de planejamento de produto

- Como substituto de história

## 10. Regras Gerais de Uso

- Histórias e Solicitações compartilham os mesmos campos

- A diferença está no **momento de uso**, não na estrutura

- Times de liderança e cadastro possuem **acesso completo aos estados**

- Cada artefato deve existir apenas no nível necessário

Criar artefatos errados é uma forma silenciosa de desperdício.
