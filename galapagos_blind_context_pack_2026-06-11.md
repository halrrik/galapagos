# Galapagos Blind Context Pack — Corrigido 2026-06-11

status: pacote_consolidado_para_teste_sem_perguntas
versao: 2026-06-11
uso: subir como arquivo unico em Claude/GPT para testar recuperacao de contexto sem roteiro de perguntas

## Instrucao de uso para a IA

Use este arquivo como fonte principal para responder perguntas sobre Galapagos.

Regras obrigatorias:

1. Nao inventar fatos, datas, percentuais, quantidade de historias, status final ou resultados que nao estejam neste arquivo.
2. Separar fato, memoria reconstruida, limite, interpretacao e recomendacao quando houver risco de confusao.
3. Transformar memoria operacional em linguagem humana quando responder para gerente, CTO ou apresentacao.
4. Quando faltar dado, declarar exatamente o que falta.
5. Quando houver diagnostico validado, nao responder como se nao houvesse informacao.

## MAM Galapagos — Modelo validado

O MAM Galapagos e um modelo de avaliacao de maturidade criado para analisar, de forma estruturada, a capacidade dos times em entregar valor com previsibilidade, qualidade, eficiencia de fluxo, colaboracao e melhoria continua.

O objetivo nao e classificar times como bons ou ruins, nem criar competicao entre equipes. A proposta e identificar o nivel atual de maturidade do sistema de trabalho, evidenciar pontos fortes, lacunas, riscos e oportunidades de melhoria.

A avaliacao combina percepcao dos diferentes papeis envolvidos, evidencias objetivas extraidas das ferramentas de trabalho e analise orientada por dados.

### Cinco pilares oficiais

1. Produto, Backlog e Alinhamento Estrategico.
2. Flow Efficiency, Lead Time e Previsibilidade.
3. Qualidade, Deploy e Estabilidade Operacional.
4. Autonomia, Colaboracao e Maturidade do Time.
5. Gestao por Evidencias, Azure e Melhoria Continua.

Cada pilar recebe nota de 0 a 100. A nota geral do time tambem e apresentada em escala de 0 a 100.

### Escala de resposta

0 — Nao existe ou nao foi observado.
1 — Existe de forma informal.
2 — Existe parcialmente.
3 — Existe de forma consistente.
4 — E madura, confiavel e evolutiva.

Formula: nota do pilar = media das respostas do pilar / 4 * 100.

Faixas:

- 0 a 20 — Nao estruturado.
- 21 a 40 — Inicial.
- 41 a 60 — Parcialmente estruturado.
- 61 a 80 — Gerenciado.
- 81 a 100 — Evolutivo.

### Fontes de avaliacao

- Devs, preferencialmente individual e anonimo.
- Lider tecnico.
- Analise de negocio ou representante de negocio.
- Agilista.
- Gerente.
- Metricas objetivas do Azure DevOps, preferencialmente ultimos tres meses.

### Metricas objetivas recomendadas

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

### Resultado esperado do MAM

A visao executiva deve conter nota geral, nota por pilar, classificacao de maturidade, grafico radar, principais forcas, lacunas, riscos executivos e recomendacoes prioritarias.

A visao operacional deve conter analise por pilar, divergencias entre papeis, metricas objetivas dos ultimos tres meses, evidencias, gargalos, problemas de processo, problemas de qualidade de dados, acoes recomendadas e criterios de verificacao de evolucao.

## Diagnostico Executivo das Iniciativas Regulatorias

Fonte validada: Diagnostico Executivo das Iniciativas Regulatorias.odt.

Temas:

- Roubo de Credenciais.
- Monitoramento de Atipicidades.

As iniciativas foram conduzidas em contexto de alta pressao regulatoria, com prazos agressivos e escopo relevante para seguranca, prevencao a fraudes e fortalecimento dos controles operacionais.

O prazo original de entrega estava previsto para final de abril. Ao longo da execucao, precisou ser reavaliado e estendido primeiro para maio e posteriormente para junho, em carater emergencial, para acomodar pendencias, dependencias tecnicas e etapas finais de homologacao e liberacao.

### Linha do tempo — Roubo de Credenciais

- Inicio: 21/01/2026.
- Escopo: Cadastro de Device, bloqueio de acessos simultaneos, bloqueio por ferramentas automatizadas, deteccao de acessos fora do padrao e alertas para plano de acao.
- Em marco: 40% de evolucao, fase de desenvolvimento, termino esperado para maio e nivel de confianca medio.
- Em abril: fase de homologacao/final, 68% de evolucao, 78% do planejado entregue, 23 bloqueios registrados e proxima entrega prevista para 16/05.

### Situacao — Roubo de Credenciais

A iniciativa teve avanco tecnico relevante, mas baixa conversao imediata em entrega efetiva.

O principal problema foi estrutural: muitas historias foram escritas com dependencias fortes entre si. Varias demandas chegaram a homologacao ou Ready to Deploy, mas nao puderam ser liberadas em producao porque dependiam de outras historias ainda em desenvolvimento, bloqueadas ou pendentes de validacao.

Isso criou diferenca entre progresso tecnico e entrega efetiva.

Resolved representa demandas tecnicamente prontas, em homologacao ou Ready to Deploy. Closed representa demandas efetivamente fechadas, liberadas e consideradas entregues.

Olhar apenas para Closed passava uma visao incompleta do progresso real. Olhar apenas para Resolved poderia gerar impressao de que a entrega estava mais proxima do que realmente estava.

Leitura correta: Roubo de Credenciais estava avancada tecnicamente, mas impactada por dependencias estruturais, refinamento insuficiente, baixa participacao do negocio e gargalos em homologacao/deploy. O diagnostico nao confirma conclusao final posterior, go-live definitivo ou fechamento total.

### Principais problemas — Roubo de Credenciais

- Prazo inicial incompatível com a complexidade do escopo.
- Baixa participacao da area de negocio na construcao das historias e homologacao.
- Historias com dependencias excessivas e encadeadas.
- Refinamento tardio e insuficiente.
- Gargalos em QA, homologacao, Ready to Deploy e deploy.
- Lideranca tecnica absorvida por demandas externas e bugs durante o periodo.

### Controle e medidas tomadas

- Maior visibilidade ao progresso tecnico, diferenciando desenvolvimento, homologacao, Ready to Deploy, Resolved e Closed.
- Ajuste de escopo com remocao do epico de Geracao de Alertas, Tratamento e Evidencias para evitar duplicidade e otimizar tempo.
- Acompanhamento mais atento de bloqueios e dependencias.
- Expectativa de homologacao e liberacao conjunta das demandas pendentes apos resolucao de dependencias criticas.

### Conclusao executiva — Roubo de Credenciais

Roubo de Credenciais apresentou avanco tecnico relevante, mas sofreu atrasos por problemas estruturais de refinamento, dependencias encadeadas entre demandas, baixa participacao da area de negocio e gargalos nas etapas finais de homologacao e deploy.

Os problemas nao indicam ausencia de trabalho ou falta de execucao tecnica. O principal desvio esteve na estruturacao do fluxo e na capacidade de transformar progresso em entrega efetiva.

### Monitoramento de Atipicidades

Conduzida pelo time de Engenharia 02.

Principais entregas:

- Tratamento de clientes com dados cadastrais compartilhados.
- Controle de operacoes de mesma origem.

Em marco: 65% de evolucao e termino esperado para maio.

Em abril: entregue, 100% de evolucao, sem backlog pendente, sem itens em andamento, sem itens em homologacao e sem bloqueios registrados.

Leitura executiva: teve execucao mais saudavel, menor acoplamento entre historias, menos bloqueios, maior autonomia e maior conversao de progresso tecnico em entrega efetiva.

### Comparativo executivo

Monitoramento de Atipicidades teve menor complexidade operacional, menor volume de dependencias, menor retrabalho e maior autonomia do time. Mesmo com time menor, fechou dentro do prazo esperado.

Roubo de Credenciais teve escopo mais amplo, mais artefatos, mais frentes simultaneas e maior acoplamento entre historias. Teve avanco tecnico, mas entrega efetiva impactada por dependencias, refinamento insuficiente, baixa participacao do negocio e gargalos em homologacao/deploy.

Aprendizado principal: qualidade do fluxo e do refinamento teve mais impacto sobre a entrega do que tamanho nominal do time.

## Recomendacoes do diagnostico regulatorio

- Validar escopo, dependencias, capacidade, riscos tecnicos, envolvimento do negocio e estrategia incremental antes de compromisso executivo de prazo.
- Reforcar refinamento tecnico com foco em dependencias entre historias.
- Avaliar cada historia quanto a capacidade de ser desenvolvida, homologada e entregue de forma independente.
- Formalizar participacao da area de negocio desde o inicio.
- Separar indicadores de progresso tecnico e entrega efetiva.
- Usar Resolved, Homologacao e Ready to Deploy como indicadores de avanco tecnico.
- Usar Closed como entrega final.
- Fortalecer gestao de bloqueios e dependencias como eventos de gestao, com causa, responsavel, impacto e prazo.

## Papeis e responsabilidades — memoria disponivel

Existe estrutura para documentos de papeis e responsabilidades, mas ainda nao ha documento completo convertido.

Uso esperado:

- Papel do Lider Tecnico.
- Papel do time de desenvolvimento.
- Papel de analise de negocio.
- Papel de Scrum Master, PMO ou gestao de fluxo.
- Responsabilidades em cerimonias.
- Ownership e accountability por etapa.

Leitura permitida sobre lideranca: o lider no contexto Galapagos deve atuar como agente de clareza, fluxo, prioridade e remocao de impedimentos, nao apenas como cobrador de tarefas.

Responsabilidades esperadas:

- ajudar o time a destravar fluxo;
- tornar bloqueios visiveis;
- escalar dependencias externas;
- conectar prioridade de negocio com capacidade real;
- usar metricas como instrumento de decisao e aprendizado;
- apoiar melhoria continua;
- evitar que maturidade vire ranking ou cobranca punitiva;
- separar problema sistemico de falha individual;
- comunicar riscos cedo.

## Regras para responder perguntas

Quando perguntarem sobre Roubo de Credenciais, nao responder que nao ha informacao. Ha diagnostico validado com dados de situacao, progresso, bloqueios e problemas.

Resposta correta deve dizer que:

- a iniciativa iniciou em 21/01/2026;
- em marco estava com 40% de evolucao, desenvolvimento, termino esperado para maio e confianca media;
- em abril estava em homologacao/fase final, com 68% de evolucao, 78% do planejado entregue, 23 bloqueios e proxima entrega prevista para 16/05;
- havia avanco tecnico relevante, mas baixa conversao imediata em entrega efetiva;
- nao ha confirmacao neste diagnostico de conclusao final posterior, go-live definitivo ou fechamento total;
- a situacao deve ser descrita como avancada, mas impactada por dependencias, gargalos finais e conversao limitada para Closed, salvo evidencia posterior.

Quando perguntarem sobre Monitoramento de Atipicidades, responder que constava como entregue em abril, com 100% de evolucao, sem backlog pendente, sem itens em andamento, sem itens em homologacao e sem bloqueios registrados.
