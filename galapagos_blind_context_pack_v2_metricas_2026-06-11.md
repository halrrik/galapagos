# Galapagos Blind Context Pack v2 — Métricas e Diagnósticos

status: pacote_consolidado_para_teste_sem_perguntas
versao: 2026-06-11
uso: subir como arquivo unico em Claude/GPT para testar respostas sobre Galapagos, MAM, diagnosticos e metricas

## Instrucao de uso para a IA

Use este arquivo como fonte principal para responder perguntas sobre Galapagos.

Regras obrigatorias:

1. Nao inventar fatos, datas, percentuais, status, metricas ou conclusoes que nao estejam neste arquivo.
2. Quando houver dado operacional, usar o dado operacional antes da memoria interpretativa.
3. Quando houver limite de qualidade dos dados, declarar o limite.
4. Para perguntas de metricas, explicar a formula usada.
5. Nao tratar lead time aproximado como cycle time real.
6. Nao calcular DORA completa sem dados de incidentes, falhas, mudancas e recuperacao.
7. Nao usar maturidade como ranking entre times.
8. Quando houver divergencia entre memoria antiga e fonte validada, usar a fonte validada.

## Gatilho recomendado

Consulte o arquivo Galapagos Blind Context Pack v2 como fonte principal. Responda usando o contexto do Grimorio Galapagos. Para perguntas de metricas, use a regra do Grimorio: CSV/Azure emulado e memoria de bases sao fonte operacional. Nao invente dados ausentes. Quando houver limite de informacao, declare o limite e diga exatamente o que falta. Quando eu pedir linguagem executiva, transforme a memoria operacional em uma resposta clara para gerente ou CTO, sem copiar literalmente o arquivo.

## MAM Galapagos — Modelo validado

O MAM Galapagos e um modelo de avaliacao de maturidade criado para analisar a capacidade dos times em entregar valor com previsibilidade, qualidade, eficiencia de fluxo, colaboracao e melhoria continua.

Cinco pilares oficiais:

1. Produto, Backlog e Alinhamento Estrategico.
2. Flow Efficiency, Lead Time e Previsibilidade.
3. Qualidade, Deploy e Estabilidade Operacional.
4. Autonomia, Colaboracao e Maturidade do Time.
5. Gestao por Evidencias, Azure e Melhoria Continua.

Escala: 0 a 4, convertida para 0 a 100.

Formula: nota do pilar = media das respostas do pilar / 4 * 100.

Faixas: 0-20 Nao estruturado; 21-40 Inicial; 41-60 Parcialmente estruturado; 61-80 Gerenciado; 81-100 Evolutivo.

## Diagnostico das iniciativas regulatorias

Temas: Roubo de Credenciais e Monitoramento de Atipicidades.

Roubo de Credenciais:

- Inicio: 21/01/2026.
- Escopo: Cadastro de Device, bloqueio de acessos simultaneos, bloqueio por ferramentas automatizadas, deteccao de acessos fora do padrao e alertas para plano de acao.
- Em marco: 40% de evolucao, fase de desenvolvimento, termino esperado para maio e nivel de confianca medio.
- Em abril: fase de homologacao/final, 68% de evolucao, 78% do planejado entregue, 23 bloqueios registrados e proxima entrega prevista para 16/05.

Situacao correta de Roubo de Credenciais: houve avanco tecnico relevante, mas baixa conversao imediata em entrega efetiva por dependencias estruturais, refinamento insuficiente, baixa participacao do negocio e gargalos em homologacao/deploy. O diagnostico nao confirma conclusao final posterior, go-live definitivo ou fechamento total.

Principal problema: dependencias fortes entre historias. Varias demandas chegaram a homologacao ou Ready to Deploy, mas nao puderam ser liberadas em producao porque dependiam de outras historias ainda em desenvolvimento, bloqueadas ou pendentes de validacao.

Monitoramento de Atipicidades:

- Em marco: 65% de evolucao e termino esperado para maio.
- Em abril: entregue, 100% de evolucao, sem backlog pendente, sem itens em andamento, sem itens em homologacao e sem bloqueios registrados.

## Hierarquia de fontes

1. CSV/Azure emulado: fonte primaria para metricas, historias, epicos, features, status, datas, lead time, cycle time, throughput, bloqueios, Resolved e Closed.
2. PPTs e relatorios apresentados: fonte primaria para narrativa executiva apresentada, percentuais reportados, riscos comunicados e status reportado para lideranca.
3. Diagnostico executivo validado: fonte consolidada para interpretacao, causas, aprendizados, comparativo e conclusao executiva.
4. Memoria operacional: apoio interpretativo.

## Bases Azure emulado

### dadosglobaisdados22.csv

Base do time de Dados / Engenharia de Dados.

- 927 registros.
- Task: 524; User Story: 281; Feature: 60; Bug: 52; Epic: 10.
- Closed: 741; New: 90; Active: 79; Resolved: 17.
- Area Path: Data\Engenharia de Dados = 876; Data\Deploy para Produção = 51.
- Created Date: 927/927; Start Date: 0/927; Resolved Date: 294/927; Closed Date: 740/927.

Limite: Start Date vazio em 100%, cycle time real nao e confiavel.

### GlobalAutomacao.csv

Base do time de Automacao.

- 233 registros.
- Task: 133; User Story: 52; Feature: 30; Blocker: 8; Epic: 6; Iniciativa: 4.
- Closed: 184; New: 18; Desenvolvimento: 8; Em execucao: 6; Em homologacao: 4.
- Area Path: Automação = 233.
- Created Date: 233/233; Start Date: 4/233; Resolved Date: 18/233; Closed Date: 184/233.
- Blocked preenchido: 5/233; Blocked Yes: 1; Blocked No: 4.

Lead time conhecido de Automacao, User Stories fechadas, calculado como Closed Date - Created Date:

- Quantidade: 41 User Stories.
- Media: 18,0 dias.
- Mediana: 14,2 dias.
- P85: 28,0 dias.
- Maior: 44,0 dias.

Todos os itens fechados de Automacao:

- Quantidade: 184 itens.
- Media: 11,9 dias.
- Mediana: 9,9 dias.
- P85: 22,6 dias.

Regra: para leitura executiva do time de Automacao, usar User Stories fechadas como leitura principal e explicar que e lead time aproximado, nao cycle time real.

### data.csv

Base global DTVM.

- 5172 registros.
- User Story: 2607; Bug: 1431; Task: 436; Feature: 373; Blocker: 191; Epic: 49.
- Closed: 4481; New: 241; Alinhamento Estrategico: 175; Refinamento de Negocio: 69; Desenvolvimento: 53; QA: 29; Deployed: 17; Ready to Deploy: 6.
- Created Date: 5172/5172; Start Date: 65/5172; Resolved Date: 3513/5172; Closed Date: 4481/5172.
- Blocked preenchido: 713/5172; Blocked Yes: 131; Blocked No: 582.

Area Path principais:

- DTVM\Tech DTVM: 2333.
- DTVM\System Team: 998.
- DTVM\Engenharia Software 1: 682.
- DTVM\Squad Dragon: 640.
- DTVM\Boletador: 155.
- DTVM\Engenharia Software 2: 102.
- DTVM\Datalake: 78.
- DTVM\Regulatorios: 63.

Tipos de bloqueio mais frequentes:

- Dependência de outra US/Feature: 49.
- Aguardando validação de negócios: 43.
- Fila: 33.
- Dependência de fornecedor: 18.
- Aguardando ação da infra/segurança: 16.
- Aguardando definição de negócios: 13.

Lead time conhecido de Eng01, fonte data.csv filtrando Area Path = DTVM\Engenharia Software 1, User Stories fechadas, calculado como Closed Date - Created Date:

- Quantidade fechada: 117 User Stories.
- Media: 86,3 dias.
- Mediana: 78,2 dias.
- P85: 152,9 dias.

Ultimos 3 meses da base, desde 11/03/2026:

- Quantidade fechada: 24 User Stories.
- Media: 84,8 dias.
- Mediana: 73,1 dias.
- P85: 151,0 dias.

Regra: esse lead time e aproximado, pois inclui backlog, espera, refinamento e priorizacao. Nao e tempo puro de execucao.

### Regulatorios - Iniciativas.csv

Base especifica de iniciativas regulatorias.

- 91 registros.
- User Story: 63; Spike: 12; Feature: 8; Epic: 5; Iniciativa: 2; Bug: 1.
- Closed: 43; Desenvolvimento: 22; Deployed: 14; Em execucao: 3; Em Desenvolvimento: 2; Alinhamento Estrategico: 2.
- Created Date: 91/91; Start Date: 12/91; Resolved Date: 50/91; Closed Date: 43/91.

Hierarquia identificada:

- Roubo de Credenciais aparece como iniciativa.
- Monitoramento de Atipicidades | Fraude aparece como iniciativa.

Epicos/frentes em Roubo de Credenciais:

- Geracao de Alertas, Tratamento e Evidencias.
- Bloqueio de Acessos atraves de ferramentas Automatizados (Captcha).
- Cadastro de Device Unificado.

Frentes em Monitoramento de Atipicidades:

- Clientes com dados cadastrais compartilhados.
- Controle de Operacoes de mesma origem.

## Regras gerais de metricas

Throughput / Vazao: preferir Closed Date, agrupando por dia, semana, sprint, mes, Area Path ou Iteration Path.

Lead time aproximado: Closed Date - Created Date. Inclui backlog, espera, refinamento, priorizacao e execucao.

Cycle time real: depende de data confiavel de inicio de execucao ou historico de transicao para desenvolvimento. Start Date tem baixa cobertura, entao nao usar sem ressalva.

Resolved versus Closed: Resolved indica avanco tecnico ou pronto tecnico; Closed indica entrega efetivamente fechada.

Bloqueios: usar Blocked, Tipo de Bloqueio e Type Block quando existirem, com ressalva de cobertura.

DORA: bases atuais nao sustentam DORA completa. Nao calcular Change Failure Rate ou MTTR sem dados confiaveis de falhas, incidentes e recuperacao.

## Regras por time

Dados / Engenharia de Dados: usar dadosglobaisdados22.csv.

Automacao: usar GlobalAutomacao.csv. Lead time principal: User Stories fechadas, media 18,0 dias, mediana 14,2 dias, P85 28,0 dias.

Engenharia Software 1 / Eng01: usar data.csv filtrando DTVM\Engenharia Software 1. Lead time principal: User Stories fechadas, media 86,3 dias, mediana 78,2 dias, P85 152,9 dias.

Engenharia Software 2 / Eng02: usar data.csv filtrando DTVM\Engenharia Software 2.

System Team: usar data.csv filtrando DTVM\System Team.

Regulatorios: usar Regulatorios - Iniciativas.csv para hierarquia da iniciativa e data.csv para leitura global quando necessario.

## Como responder perguntas futuras

Se a pergunta for sobre situacao de iniciativa, responder com: situacao executiva, dados confirmados, leitura de fluxo, problemas principais, limite e proximo passo.

Se a pergunta for sobre metricas, responder com: base usada, filtro usado, formula usada, resultado numerico, interpretacao e limite do dado.

Se a pergunta for sobre lead time, nunca responder apenas o numero. Explicar se e aproximado ou real.

Se a pergunta for sobre cycle time, verificar cobertura de Start Date. Se Start Date estiver incompleto, dizer que cycle time real nao e confiavel.

Se a pergunta for sobre DORA, dizer que as bases atuais nao sustentam DORA completa.

## Limites gerais

- Bases parecem snapshots/exportacoes de work items, nao historico completo de transicoes.
- Start Date e pouco preenchido na maioria das bases.
- Story Points possui baixa cobertura.
- Bloqueios e tipos de bloqueio possuem cobertura parcial.
- DORA completa nao e suportada pelas bases atuais.
- Lead time baseado em Created Date pode incluir espera antes da execucao.
- Cycle time real depende de historico de entrada em desenvolvimento, que nao esta completo nas bases atuais.
