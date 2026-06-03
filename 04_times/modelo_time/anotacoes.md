# Anotações do Time

Use este arquivo para registrar contexto qualificado do time.

## Regra

Anotações não substituem dados. Elas servem para explicar, contextualizar, questionar ou complementar evidências.

## Modelo de anotação

```md
## AAAA-MM-DD — Título da anotação

- Data:
- Autor:
- Time:
- Tema:
- Fonte:
- Tipo:
  - fato
  - observação
  - hipótese
  - decisão
  - risco
  - impedimento
  - aprendizado
  - ação

### Descrição


### Relação com os dados existentes

A anotação:

- confirma um dado;
- explica um dado;
- contradiz um dado;
- complementa um dado;
- levanta hipótese sobre um dado;
- registra contexto que o dashboard não mostra.

### Impacto


### Validade

- Pontual
- Recorrente
- Temporária
- Ainda precisa validação

### Ação sugerida


```

## Exemplo

```md
## 2026-05-27 — Itens parados em homologação

- Data: 2026-05-27
- Autor: exemplo
- Time: exemplo
- Tema: homologação
- Fonte: observação do time + dashboard
- Tipo: hipótese

### Descrição

Há itens com aging alto em homologação. Parte deles pode estar aguardando validação do negócio, não atuação técnica de QA.

### Relação com os dados existentes

A anotação explica um dado observado no dashboard.

### Impacto

Evitar interpretar a fila como gargalo exclusivamente técnico.

### Validade

Ainda precisa validação.

### Ação sugerida

Separar aging de QA técnico e aging de validação de negócio nos próximos recortes.
```
