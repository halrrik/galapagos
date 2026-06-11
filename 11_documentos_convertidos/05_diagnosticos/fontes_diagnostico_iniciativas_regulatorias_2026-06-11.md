# Fontes do Diagnostico das Iniciativas Regulatorias — 2026-06-11

status: mapa_de_fontes_validado
uso: orientar recuperacao, analise e respostas sobre Roubo de Credenciais, Monitoramento de Atipicidades, Cadastro de Device e diagnosticos relacionados

## Objetivo

Este arquivo define quais fontes devem ser usadas quando houver perguntas sobre as iniciativas regulatorias, especialmente Roubo de Credenciais e Monitoramento de Atipicidades.

A regra principal e: o diagnostico nao deve depender apenas de memoria textual. Deve combinar dados operacionais, artefatos executivos apresentados e leitura consolidada.

## Hierarquia de fontes

### 1. CSV / dados extraidos do Azure DevOps ou emulacao do Azure

Prioridade: fonte primaria para metricas, historias, epicos, features, status e fluxo.

Usar para responder perguntas sobre:

- quantidade de historias;
- quantidade planejada;
- quantidade concluida;
- status das demandas;
- epicos e features associados;
- lead time;
- cycle time;
- throughput / vazao;
- aging por status;
- tempo em homologacao;
- tempo em ready to deploy;
- resolved versus closed;
- bloqueios;
- tipos de bloqueio;
- datas de inicio, resolved e closed;
- planejado versus finalizado;
- conversao de progresso tecnico em entrega efetiva.

Regra: quando o CSV estiver disponivel, nao responder apenas pela memoria. Usar o CSV para sustentar numeros e metricas.

### 2. PPTs e relatorios apresentados

Prioridade: fonte primaria para narrativa executiva apresentada, status report, mensagens comunicadas, marcos, percentuais divulgados, riscos apresentados e decisao gerencial.

Usar para responder perguntas sobre:

- o que foi apresentado para lideranca;
- leitura executiva usada nos slides;
- situacao comunicada em marco ou abril;
- percentuais reportados;
- nivel de confianca;
- data esperada de entrega;
- principais riscos comunicados;
- conclusoes apresentadas;
- narrativa para gerente ou CTO.

Regra: quando houver divergencia entre metricas do CSV e narrativa do PPT, explicitar a diferenca entre dado operacional e comunicacao executiva.

### 3. Diagnostico Executivo das Iniciativas Regulatorias.odt

Prioridade: fonte consolidada validada para leitura executiva e interpretacao dos problemas.

Usar para responder perguntas sobre:

- contexto regulatorio;
- comparativo entre Roubo de Credenciais e Monitoramento de Atipicidades;
- principais causas;
- diferenca entre progresso tecnico e entrega efetiva;
- problemas de refinamento;
- dependencias entre historias;
- participacao da area de negocio;
- gargalos em QA, homologacao, Ready to Deploy e deploy;
- aprendizados;
- recomendacoes;
- conclusao executiva.

Regra: o ODT e fonte validada, mas nao substitui o CSV quando a pergunta exigir numero granular por historia, epico ou status.

### 4. Memoria operacional anterior

Prioridade: apoio interpretativo e historico.

Usar para:

- lembrar regras de interpretacao;
- evitar conclusoes sem contexto;
- separar fato, memoria, hipotese, interpretacao e recomendacao;
- orientar linguagem executiva;
- orientar leitura de fluxo, bloqueios e dependencias.

Regra: memoria operacional nao deve prevalecer sobre CSV, PPT ou ODT validado.

## Regra especifica para Roubo de Credenciais

Nao responder que nao ha informacao sobre Roubo de Credenciais quando o diagnostico validado estiver disponivel.

Existe informacao validada sobre:

- inicio em 21/01/2026;
- 40% de evolucao em marco;
- fase de desenvolvimento em marco;
- termino esperado para maio em marco;
- nivel de confianca medio em marco;
- 68% de evolucao em abril;
- 78% do planejado entregue em abril;
- 23 bloqueios registrados;
- fase de homologacao/final em abril;
- proxima entrega prevista para 16/05;
- avanco tecnico relevante;
- dependencia entre historias;
- gargalos em homologacao, Ready to Deploy e deploy;
- diferenca entre Resolved e Closed;
- baixa conversao imediata de progresso tecnico em entrega efetiva.

O que o diagnostico validado nao confirma sozinho:

- conclusao final posterior ao recorte;
- go-live definitivo posterior;
- fechamento total da iniciativa apos a data analisada;
- lista completa granular de historias se o CSV nao estiver presente;
- metricas recalculadas se a base operacional nao estiver disponivel.

## Regra especifica para Monitoramento de Atipicidades

Existe informacao validada de que em abril a iniciativa constava como entregue, com 100% de evolucao, sem backlog pendente, sem itens em andamento, sem itens em homologacao e sem bloqueios registrados.

## Como responder perguntas executivas

Para perguntas de gerente ou CTO, a resposta deve combinar:

1. situacao executiva;
2. dado confirmado;
3. leitura de fluxo;
4. problemas principais;
5. impacto em prazo ou entrega;
6. limite da informacao;
7. proximo passo recomendado.

## Como responder perguntas metricas

Para perguntas de metricas, usar esta ordem:

1. localizar CSV ou base operacional;
2. identificar recorte de periodo;
3. calcular ou recuperar lead time, cycle time, throughput, bloqueios e status;
4. separar Resolved de Closed;
5. explicar o que cada metrica representa;
6. indicar limite se a base nao estiver presente.

## Decisao

O Grimorio Galapagos deve tratar o diagnostico das iniciativas regulatorias como um conjunto composto por dados, apresentacoes e consolidacao textual. A resposta ideal nao e apenas "ha ou nao ha dado", mas sim "qual fonte sustenta qual parte da resposta".