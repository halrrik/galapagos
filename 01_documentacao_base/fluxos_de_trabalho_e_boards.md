---
origem: Documento de Processos Tecnologia.docx
status: convertido_para_markdown
classificacao_sugerida: revisar_antes_de_publicar
aplicacao: Grimorio Versao Galapagos
---

# Fluxos de Trabalho e Boards

## 1. Objetivo desta Parte

Esta parte descreve **como os artefatos se movem pelo sistema**, quais **fluxos existem**, por que há **boards diferentes** e como cada área interage com o trabalho sem gerar conflito, retrabalho ou perda de contexto.

Aqui não se define prioridade nem escopo. Aqui se define **movimento controlado do trabalho**.

## 2. Princípio Central do Fluxo

O sistema da área de tecnologia opera com um princípio claro:

**Trabalho muda de estado para reduzir incerteza — não para cumprir rito.**

Cada transição existe para responder uma pergunta objetiva. Se a pergunta não foi respondida, o item não deve avançar.

## 3. Separação Estrutural: Upstream e Downstream

### 3.1 Upstream - Preparação do Trabalho

O upstream concentra atividades de:

- Descoberta

- Análise

- Refinamento

- Validação de viabilidade

É onde ideias ainda podem mudar, morrer ou ser reestruturadas. Mover rápido aqui é saudável.

Estados típicos do upstream:

- Nova Demanda / Novo

- Refinamento de Negócio

- Refinamento Técnico

- Product Backlog

No upstream:

- Não há compromisso de entrega

- O custo do erro é baixo

- O foco é clareza, não velocidade

### 3.2 Downstream - Execução do Trabalho

O downstream concentra atividades de:

- Desenvolvimento

- Revisão

- Testes

- Entrega

Aqui o trabalho já foi decidido. O objetivo passa a ser entregar com qualidade e previsibilidade.

Estados típicos do downstream:

- Backlog

- Desenvolvimento

- Code Review

- QA

- Ready to Deploy

- Deployed

- Closed

No downstream:

- Mudanças de escopo são exceção

- Bloqueios devem ser explícitos

- Métricas passam a ser relevantes

## 4. Fluxos por Tipo de Artefato

### 4.1 Fluxo de Iniciativa

A Iniciativa percorre um fluxo estratégico, não técnico.

Fluxo típico:

- Discovery

- Em Andamento

- Validação

- Closed

- Suspenso (exceção)

A Iniciativa não entra em desenvolvimento. Ela orienta e governa os níveis abaixo.

### 4.2 Fluxo de Épico

O Épico traduz direção em frentes executáveis.

Fluxo típico:

- Novo

- Refinamento

- Aprovado

- Em Execução

- Encerrado

Um Épico pode ter múltiplas Features em execução simultânea.

### 4.3 Fluxo de Feature

A Feature organiza entregas de valor.

Fluxo típico:

- Novo

- Refinamento

- Priorizado

- Em Execução

- Entregue

Feature coordena histórias, mas não substitui o fluxo delas.

### 4.4 Fluxo de User Story e Solicitação

Histórias e Solicitações compartilham o mesmo fluxo operacional.

Fluxo típico:

- Product Backlog

- Backlog

- Desenvolvimento

- Code Review

- QA

- Ready to Deploy

- Deployed

- Closed

A diferença entre Story e Solicitação está na origem e maturidade, não no fluxo.

### 4.5 Fluxo de Bug

Bug segue fluxo próprio, com prioridade operacional.

Fluxo típico:

- Novo

- Em Análise

- Em Correção

- Testes

- Pronto para Deploy

- Closed

Bugs podem:

- Ser filhos de histórias ou solicitações

- Ser independentes, desde que tenham pai hierárquico válido

## 5. Boards e Seus Papéis

O sistema utiliza múltiplos boards, cada um com um objetivo específico.

**Board de Produto**

- Visualizar upstream

- Organizar prioridades

- Refinar demandas

**Board de Desenvolvimento**

- Executar trabalho

- Controlar WIP

- Visualizar bloqueios

**Board de Qualidade**

- Foco em validação

- Redução de retrabalho

**Board de Liderança**

- Visão sistêmica

- Acompanhamento de fluxo

- Identificação de gargalos

Boards não competem entre si. Cada um mostra o sistema sob uma lente diferente. Porém todos conseguem enxergar o backlog global, não se trata de esconder as demandas de um time para o outro, senão apresentar um board limpo e claro. E todos tem acesso aos outro boards.

## 6. Políticas Gerais de Movimento de cards no board

- Um item só avança se cumprir o objetivo do estado atual

- Bloqueios devem ser marcados explicitamente e o campo tipo de bloqueio/impedimento é obrigatório.

- Liderança e Cadastro possuem acesso completo aos estados

- Times não pulam estados para ganhar velocidade aparente

- Esta bloqueado voltar estados no board.

- Esta bloqueado apagar demandas, para isso se usara o estado cancelado.

Mover cartão sem reduzir incerteza é movimento ilusório.
