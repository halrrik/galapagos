# 04 — Times

Esta pasta organiza informações, diagnósticos, maturidade e planos de melhoria por time.

## Uso no piloto

A versão inicial deve começar com poucos times para reduzir complexidade e facilitar validação.

Cada time pode ter:

- perfil do time;
- fluxo local;
- métricas observadas;
- diagnóstico atual;
- maturidade;
- anotações;
- riscos;
- plano de melhoria.

## Regra sobre anotações

Anotações não substituem dados. Elas explicam, contextualizam, questionam ou complementam dados.

Quando uma anotação contradizer o dado, a IA deve declarar a divergência e tratar como hipótese a validar.

## Modelo de relação entre camadas

```text
Dados operacionais
+ Dashboards / prints
+ Documentação base
+ Anotações do time
= Diagnóstico do time
= Avaliação de maturidade
= Plano de melhoria
= Relatório executivo
```
