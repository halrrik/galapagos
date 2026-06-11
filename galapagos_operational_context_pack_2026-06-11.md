# Galapagos Operational Context Pack — Compilado Honesto

status: contexto_operacional_compilado
versao: 2026-06-11
uso: fornecer a uma IA externa conteudo real minimo do Grimorio Galapagos para responder perguntas sem depender do repositorio completo
nao_usar_como: gabarito de perguntas especificas

## Por que este arquivo existe

O `Galapagos Universal Context Prompt` e um roteador. Ele ensina como consultar o Grimorio, mas sozinho nao contem os dados do Grimorio.

Se uma IA externa receber apenas o prompt universal, ela sabera como deveria consultar, mas nao tera conteudo suficiente para responder sobre iniciativas, metricas, MAM, diagnosticos ou times.

Este arquivo traz um compilado operacional de memorias, regras e dados ja registrados no Grimorio. Ele nao foi escrito para responder uma pergunta especifica; deve servir como contexto geral para qualquer pergunta cujo conteudo esteja registrado aqui.

## Regra principal

Use este arquivo como fonte de contexto operacional do Grimorio Galapagos.

Nao invente fatos, metricas, datas, percentuais, status, conclusoes ou decisoes.

Antes de declarar que nao ha informacao suficiente, aplique a escada de resposta:

1. Fonte direta.
2. Consolidacao de fontes.
3. Leitura derivada com limite declarado.
4. Framework aplicavel.
5. Lacuna real.

Se a informacao estiver neste arquivo, responda. Se estiver parcialmente, responda parcialmente e declare limite. Se nao estiver, diga que este contexto nao possui informacao suficiente.

## MAM Galapagos — modelo validado

O MAM Galapagos avalia a capacidade dos times em entregar valor com previsibilidade, qualidade, eficiencia de fluxo, colaboracao e melhoria continua. Nao e ranking de times.

Cinco pilares oficiais:

1. Produto, Backlog e Alinhamento Estrategico.
2. Flow Efficiency, Lead Time e Previsibilidade.
3. Qualidade, Deploy e Estabilidade Operacional.
4. Autonomia, Colaboracao e Maturidade do Time.
5. Gestao por Evidencias, Azure e Melhoria Continua.

Escala: 0 a 4, convertida para 0 a 100.

Formula: nota do pilar = media das respostas do pilar / 4 * 100.

Faixas: 0-20 Nao estruturado; 21-40 Inicial; 41-60 Parcialmente estruturado; 61-80 Gerenciado; 81-100 Evolutivo.

Fontes de avaliacao: devs, lider tecnico, negocio/analise de negocio, agilista, gerente e metricas objetivas dos ultimos tres meses quando disponiveis.

## Diagnostico das iniciativas regulatorias

Temas: Roubo de Credenciais e Monitoramento de Atipicidades.

### Roubo de Credenciais

Dados confirmados no diagnostico validado:

- Inicio: 21/01/2026.
- Escopo: Cadastro de Device, bloqueio de acessos simultaneos, bloqueio por ferramentas automatizadas, deteccao de acessos fora do padrao e alertas para plano de acao.
- Em marco: 40% de evolucao, fase de desenvolvimento, termino esperado para maio e nivel de confianca medio.
- Em abril: fase de homologacao/final, 68% de evolucao, 78% do planejado entregue, 23 bloqueios registrados e proxima entrega prevista para 16/05.

Leitura correta: houve avanco tecnico relevante, mas baixa conversao imediata em entrega efetiva. O principal problema foi dependencia forte entre historias. Varias demandas chegaram a homologacao ou Ready to Deploy, mas nao puderam ser liberadas porque dependiam de outras historias ainda em desenvolvimento, bloqueadas ou pendentes de validacao.

Resolved representa demanda tecnicamente pronta, em homologacao ou Ready to Deploy. Closed representa entrega efetivamente fechada. Olhar so Closed esconde progresso tecnico; olhar so Resolved pode exagerar entrega efetiva.

O diagnostico nao confirma conclusao final posterior, go-live definitivo ou fechamento total.

Principais problemas: prazo inicial incompativel com a complexidade; baixa participacao do negocio; dependencias excessivas entre historias; refinamento tardio e insuficiente; gargalos em QA, homologacao, Ready to Deploy e deploy; lideranca tecnica absorvida por demandas externas e bugs.

Na base `Regulatorios - Iniciativas.csv`, a linha da iniciativa Roubo de Credenciais tem: ID 46560; Work Item Type Iniciativa; State Em Andamento; Created Date 21/01/2026 13:42:10; Start Date 02/02/2026; Closed Date vazio; Resolved Date vazio.

### Monitoramento de Atipicidades

Conduzida por Engenharia Software 2. Principais entregas: tratamento de clientes com dados cadastrais compartilhados e controle de operacoes de mesma origem.

Dados confirmados: em marco estava com 65% de evolucao e termino esperado para maio. Em abril constava como entregue, 100% de evolucao, sem backlog pendente, sem itens em andamento, sem itens em homologacao e sem bloqueios registrados.

## Bases operacionais — Azure DevOps emulado

As bases CSV devem ser tratadas como fonte operacional, com limites. Parecem snapshots/exportacoes, nao historico completo de transicoes. Start Date tem baixa cobertura na maioria das bases. DORA completa nao e suportada.

### dadosglobaisdados22.csv

Uso: Dados / Engenharia de Dados.

- 927 registros.
- Work item types: Task 524; User Story 281; Feature 60; Bug 52; Epic 10.
- Estados: Closed 741; New 90; Active 79; Resolved 17.
- Area Path: Data\Engenharia de Dados 876; Data\Deploy para Produção 51.
- Datas: Created Date 927/927; Start Date 0/927; Resolved Date 294/927; Closed Date 740/927.
- Limite: Start Date vazio, entao cycle time real nao e confiavel.

### GlobalAutomacao.csv

Uso: time de Automacao.

- 233 registros.
- Work item types: Task 133; User Story 52; Feature 30; Blocker 8; Epic 6; Iniciativa 4.
- Estados: Closed 184; New 18; Desenvolvimento 8; Em execucao 6; Em homologacao 4; Alinhamento Estrategico 3; Homologacao 3; Em Desenvolvimento 2; Em Andamento 1; Em Discovery 1; Em Validacao 1; Quebra em historias 1; QA 1.
- Area Path: Automação 233.
- Datas: Created Date 233/233; Start Date 4/233; Resolved Date 18/233; Closed Date 184/233.
- Bloqueios: Blocked preenchido 5/233; Yes 1; No 4. Tipo de Bloqueio preenchido 8/233.

Lead time conhecido de Automacao, User Stories fechadas, formula Closed Date - Created Date:

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

Uso: base global DTVM.

- 5172 registros.
- Work item types: User Story 2607; Bug 1431; Task 436; Feature 373; Blocker 191; Epic 49; Bug Task 48; Spike 19; Solicitacao 7; Iniciativa 6; Take Off 5.
- Estados principais: Closed 4481; New 241; Alinhamento Estrategico 175; Refinamento de Negocio 69; Desenvolvimento 53; QA 29; Deployed 17; Ready to Deploy 6.
- Datas: Created Date 5172/5172; Start Date 65/5172; Resolved Date 3513/5172; Closed Date 4481/5172.
- Bloqueios: Blocked preenchido 713/5172; Yes 131; No 582; Tipo de Bloqueio preenchido 188/5172.

Area Paths principais:

- DTVM\Tech DTVM: 2333.
- DTVM\System Team: 998.
- DTVM\Engenharia Software 1: 682.
- DTVM\Squad Dragon: 640.
- DTVM\Boletador: 155.
- DTVM\Engenharia Software 2: 102.
- DTVM\Datalake: 78.
- DTVM\Regulatorios: 63.
- DTVM: 59.
- DTVM\Debito Tecnico: 26.
- DTVM\Sistemas: 16.
- DTVM\Infraestrutura TI: 15.
- DTVM\Cadastro MFO: 5.

Tipos de bloqueio mais frequentes: Dependencia de outra US/Feature 49; Aguardando validacao de negocios 43; Fila 33; Dependencia de fornecedor 18; Aguardando acao da infra/seguranca 16; Aguardando definicao de negocios 13.

Metricas conhecidas para Eng01 / Engenharia Software 1, filtro Area Path = DTVM\Engenharia Software 1, Work Item Type = User Story, Closed Date preenchido:

Historico fechado:

- Quantidade: 117 User Stories.
- Lead time medio: 86,3 dias.
- Mediana: 78,2 dias.
- P85: 152,9 dias.

Ultimos tres meses desde 11/03/2026:

- Quantidade: 24 User Stories.
- Media: 84,8 dias.
- Mediana: 73,1 dias.
- P85: 151,0 dias.

Mes calendario de maio/2026, Closed Date entre 01/05/2026 e 31/05/2026:

- Quantidade: 5 User Stories.
- Media: 29,2 dias.
- Mediana: 18,1 dias.
- P85: 52,3 dias.
- Maior: 78,2 dias.

Ultimos 30 dias em relacao a 11/06/2026, Closed Date entre 12/05/2026 e 11/06/2026:

- Quantidade: 2 User Stories.
- Media: 39,1 dias.
- Mediana: 39,1 dias.
- P85: 66,5 dias.
- Maior: 78,2 dias.

Regra: e lead time aproximado via Created Date -> Closed Date, inclui backlog, espera, refinamento e priorizacao. Nao e cycle time real.

### Regulatorios - Iniciativas.csv

Uso: iniciativas regulatorias.

- 91 registros.
- Work item types: User Story 63; Spike 12; Feature 8; Epic 5; Iniciativa 2; Bug 1.
- Estados: Closed 43; Desenvolvimento 22; Deployed 14; Em execucao 3; Em Desenvolvimento 2; Alinhamento Estrategico 2; Em Andamento 1; Removed 1; Feature Validation 1; Quebra em historias 1; Refinamento Tecnico 1.
- Datas: Created Date 91/91; Start Date 12/91; Resolved Date 50/91; Closed Date 43/91.
- Hierarquia: Roubo de Credenciais; Monitoramento de Atipicidades | Fraude.
- Frentes de Roubo: Geracao de Alertas, Tratamento e Evidencias; Bloqueio de Acessos atraves de ferramentas Automatizados (Captcha); Cadastro de Device Unificado.
- Frentes de Monitoramento: Clientes com dados cadastrais compartilhados; Controle de Operacoes de mesma origem.

## Times, areas e recortes identificados

Nao ha inventario oficial unico de times formais. Nas bases operacionais foram identificados 16 Area Paths / recortes operacionais:

Automação; Data\Engenharia de Dados; Data\Deploy para Produção; DTVM; DTVM\Boletador; DTVM\Cadastro MFO; DTVM\Datalake; DTVM\Debito Tecnico; DTVM\Engenharia Software 1; DTVM\Engenharia Software 2; DTVM\Infraestrutura TI; DTVM\Regulatorios; DTVM\Sistemas; DTVM\Squad Dragon; DTVM\System Team; DTVM\Tech DTVM.

Isso nao significa necessariamente 16 times formais. Para responder quantos times existem oficialmente, falta inventario organizacional.

## Regras de metricas

Lead time padrao: Closed Date - Created Date. Ressalva: inclui backlog, espera, refinamento, priorizacao e execucao.

Cycle time real exige data confiavel de inicio de execucao ou historico de transicao. Start Date tem baixa cobertura, entao nao usar cycle time real sem ressalva.

Throughput: usar Closed Date agrupado por dia, semana, sprint, mes, Area Path ou Iteration Path.

Resolved versus Closed: Resolved indica pronto tecnico/homologacao/Ready to Deploy; Closed indica entrega fechada.

DORA: bases atuais nao sustentam DORA completa. Nao calcular Change Failure Rate ou MTTR sem dados de falhas, incidentes e recuperacao.

## Regras por time / area

- Dados: usar dadosglobaisdados22.csv.
- Automacao: usar GlobalAutomacao.csv.
- Eng01: usar data.csv filtrando DTVM\Engenharia Software 1. Para Roubo, cruzar com Regulatorios - Iniciativas.csv e diagnostico validado.
- Eng02: usar data.csv filtrando DTVM\Engenharia Software 2. Para Monitoramento, cruzar com Regulatorios - Iniciativas.csv e diagnostico validado.
- System Team: usar data.csv filtrando DTVM\System Team.
- Regulatorios: usar Regulatorios - Iniciativas.csv para hierarquia e diagnostico validado para narrativa executiva.

## Papeis e responsabilidades

Nao ha neste contexto uma matriz oficial completa de papeis e responsabilidades.

Se houver documento oficial de papel, usar como fonte direta. Se nao houver documento oficial, nao declarar lacuna total automaticamente. Procurar MAM, fluxo, modelo operacional, DoR/DoD, metricas, diagnosticos e memoria operacional. Se houver material suficiente, responder como leitura derivada com limite declarado.

Formula recomendada: O Grimorio nao traz uma definicao oficial completa sobre este papel. Ainda assim, a partir do MAM, do fluxo e das regras de trabalho, e possivel fazer uma leitura derivada...
