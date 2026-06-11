# MAM Galapagos — Modelo Validado 2026-06-11

status: modelo_validado_por_documento_odt
origem: Modelo de Avaliacao de Maturidade Galapagos.odt
uso: fonte principal para perguntas sobre MAM Galapagos

## Definicao

O MAM Galapagos e um modelo de avaliacao de maturidade criado para analisar, de forma estruturada, a capacidade dos times em entregar valor com previsibilidade, qualidade, eficiencia de fluxo, colaboracao e melhoria continua.

O objetivo nao e classificar times como bons ou ruins, nem criar competicao entre equipes. A proposta e identificar o nivel atual de maturidade do sistema de trabalho, evidenciar pontos fortes, lacunas, riscos e oportunidades de melhoria, permitindo que cada time evolua de forma objetiva e acompanhavel ao longo do tempo.

A avaliacao combina percepcao dos diferentes papeis envolvidos, evidencias objetivas extraidas das ferramentas de trabalho e analise orientada por dados.

## Principios

- Maturidade deve ser observavel por evidencias, nao apenas por percepcao.
- A avaliacao deve considerar diferentes pontos de vista: devs, lider tecnico, negocio, agilista e gerente.
- A nota final deve ser simples para comunicacao executiva, mas sustentada por analise operacional.
- O modelo nao deve estimular ranking entre times.
- A comparacao principal deve ser do time contra sua propria evolucao ao longo do tempo.
- Diagnostico sem plano de melhoria nao produz mudanca real.
- A ferramenta de trabalho deve refletir a realidade.
- Metricas devem ser interpretadas com contexto.

## Referencias conceituais

O MAM utiliza referencias de DORA, KMM / Kanban Maturity Model, Agile Fluency e estruturas de capacidade organizacional.

DORA e referencia executiva para desempenho de entrega de software, especialmente capacidade de entrega, frequencia de deploy, estabilidade e tempo de recuperacao. Entretanto, DORA nao explica sozinha as causas dos resultados.

KMM apoia a leitura de maturidade de fluxo, visualizacao do trabalho, gestao de bloqueios, melhoria evolucionaria e identificacao de gargalos.

## Cinco pilares oficiais

1. Produto, Backlog e Alinhamento Estrategico.
2. Flow Efficiency, Lead Time e Previsibilidade.
3. Qualidade, Deploy e Estabilidade Operacional.
4. Autonomia, Colaboracao e Maturidade do Time.
5. Gestao por Evidencias, Azure e Melhoria Continua.

Cada pilar recebe nota de 0 a 100. A nota geral tambem e apresentada em escala de 0 a 100.

## Pilar 1 — Produto, Backlog e Alinhamento Estrategico

Avalia se o time trabalha nas demandas certas, com clareza de valor, prioridade e preparacao suficiente antes da execucao.

Inclui entendimento do problema de negocio, qualidade do backlog, criterios de aceite, participacao do negocio, quebra das demandas, gestao de dependencias e alinhamento entre prioridade estrategica e execucao.

Pergunta executiva: estamos construindo as coisas certas, com clareza de valor, prioridade e preparacao adequada?

## Pilar 2 — Flow Efficiency, Lead Time e Previsibilidade

Avalia se o trabalho flui com eficiencia e se o time consegue prever entregas com base em dados e capacidade real.

Inclui visibilidade do fluxo, WIP, gargalos, bloqueios, aging, lead time, cycle time, throughput, estabilidade de escopo, planejamento e forecast.

Pergunta executiva: o trabalho flui com eficiencia e conseguimos prever entregas com base em capacidade real?

## Pilar 3 — Qualidade, Deploy e Estabilidade Operacional

Avalia se o time consegue entregar mudancas em producao com frequencia adequada, qualidade e baixo impacto operacional.

Inclui qualidade tecnica, prontidao para producao, homologacao, validacao, deploy frequency, change failure rate, MTTR quando aplicavel, retrabalho, defeitos, incidentes e dependencias de deploy, QA, negocio, infraestrutura ou seguranca.

Pergunta executiva: conseguimos entregar em producao com frequencia adequada, seguranca e baixo impacto operacional?

## Pilar 4 — Autonomia, Colaboracao e Maturidade do Time

Avalia se o time consegue operar com responsabilidade, clareza de papeis, colaboracao efetiva e menor dependencia externa para resolver problemas recorrentes.

Autonomia nao significa ausencia de lideranca. Significa que o time entende seu fluxo, sabe escalar impedimentos, toma decisoes compativeis com sua responsabilidade e conhece seus acordos de trabalho.

Pergunta executiva: o time consegue operar com responsabilidade, clareza de papeis e colaboracao real?

## Pilar 5 — Gestao por Evidencias, Azure e Melhoria Continua

Avalia se o time possui dados confiaveis, utiliza corretamente o Azure DevOps, acompanha metricas relevantes e melhora o sistema de trabalho com base em evidencias.

Inclui qualidade dos registros no Azure, status, datas, relacionamentos entre epicos, features e user stories, bloqueios, dashboards, DORA, metricas de fluxo, retrospectivas, planos de acao e acompanhamento de melhorias.

Pergunta executiva: temos dados confiaveis, leitura correta das metricas e acoes reais de melhoria continua?

## Escala de resposta

As perguntas sao respondidas em escala de 0 a 4:

0 — Nao existe ou nao foi observado.
1 — Existe de forma informal.
2 — Existe parcialmente.
3 — Existe de forma consistente.
4 — E madura, confiavel e evolutiva.

A nota de cada pilar e calculada pela media das respostas do pilar, convertida para 0 a 100.

Formula: nota do pilar = media das respostas do pilar / 4 * 100.

Na versao inicial, todos os pilares possuem peso igual a 1.

## Faixas de maturidade

0 a 20 — Nao estruturado.
21 a 40 — Inicial.
41 a 60 — Parcialmente estruturado.
61 a 80 — Gerenciado.
81 a 100 — Evolutivo.

As faixas servem para orientar leitura, priorizacao e evolucao. Nao devem ser usadas como julgamento definitivo.

## Fontes de avaliacao

O MAM combina quatro fontes:

1. Percepcao dos devs, preferencialmente individual e anonima.
2. Avaliacao de papeis de referencia, como lider tecnico e negocio.
3. Avaliacao do agilista e gerente.
4. Metricas objetivas extraidas do Azure DevOps, preferencialmente dos ultimos tres meses.

## Papeis respondentes

- Devs.
- Lider tecnico.
- Analise de negocio ou representante de negocio.
- Agilista.
- Gerente.

O questionario e adaptado por papel. Algumas perguntas podem se repetir para comparar percepcoes.

## Metricas objetivas recomendadas

- Lead time.
- Cycle time.
- Throughput.
- Aging de demandas.
- Bloqueios: quantidade, tempo e recorrencia.
- WIP.
- Planejado versus concluido.
- Demandas reabertas ou com retrabalho.
- Tempo em homologacao ou validacao.
- Tempo em ready to deploy.
- Deploy frequency.
- Change failure rate, quando houver dado confiavel.
- MTTR, quando houver dado confiavel.
- Qualidade dos dados no Azure.

## Resultado esperado

A visao executiva deve conter nota geral, nota por pilar, classificacao de maturidade, grafico radar, principais forcas, lacunas, riscos executivos e recomendacoes prioritarias.

A visao operacional deve conter analise por pilar, divergencias entre papeis, metricas objetivas dos ultimos tres meses, evidencias, gargalos, problemas de processo, problemas de qualidade de dados, acoes recomendadas e criterios de verificacao de evolucao.

## Cadencia

A recomendacao inicial e avaliacao completa em ciclos trimestrais, com acompanhamento mensal das acoes definidas.

## Entregaveis

1. Documento explicativo do modelo.
2. Apresentacao executiva.
3. Instrumento de avaliacao com questionarios por papel, escala, evidencias, consolidacao e calculo de notas.

## Regra de uso

Este arquivo substitui a memoria reconstruida anterior quando houver divergencia sobre pilares, escala ou estrutura oficial do MAM. Para respostas humanas, reescrever em linguagem clara e executiva, sem copiar mecanicamente a memoria.