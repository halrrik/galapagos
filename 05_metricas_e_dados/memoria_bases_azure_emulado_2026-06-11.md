# Memoria das Bases Azure Emulado — 2026-06-11

status: memoria_de_dados_operacionais
origem: CSVs fornecidos pelo usuario para emular conexao com Azure DevOps
uso: fonte de contexto para perguntas futuras sobre metricas, fluxo, historias, epicos, features, estados, bloqueios e diagnosticos por time/iniciativa

## Objetivo

Este arquivo registra a memoria operacional das bases CSV recebidas para emular uma conexao com Azure DevOps.

A finalidade nao e substituir o Azure real, mas permitir que a IA responda melhor perguntas sobre metricas, fluxo e diagnosticos usando uma estrutura parecida com a base de work items.

## Arquivos analisados

### 1. `dadosglobaisdados22.csv`

Uso esperado: base do time de Dados / Engenharia de Dados.

Volume:

- 927 registros.
- 20 colunas.

Work item types:

- Task: 524.
- User Story: 281.
- Feature: 60.
- Bug: 52.
- Epic: 10.

Estados principais:

- Closed: 741.
- New: 90.
- Active: 79.
- Resolved: 17.

Area Path:

- `Data\Engenharia de Dados`: 876 registros.
- `Data\Deploy para Produção`: 51 registros.

Cobertura de datas:

- Created Date: 927/927.
- Start Date: 0/927.
- Resolved Date: 294/927.
- Closed Date: 740/927.

Limite importante:

- Start Date esta vazio em 100% dos registros. Portanto, cycle time baseado em Start Date nao e confiavel nesta base.
- Story Points possui cobertura muito baixa: 7/927.
- Bloqueios praticamente nao estao registrados: apenas 1 registro com campo Blocked preenchido.

Uso recomendado:

- Throughput por Closed Date.
- Lead time aproximado Created Date -> Closed Date.
- Tempo Resolved -> Closed para itens com ambas as datas.
- Volume por status, work item type, area path e iteration path.

Nao usar sem ressalva:

- Cycle time real.
- Analise robusta de bloqueios.
- Capacidade por story points.

### 2. `GlobalAutomacao.csv`

Uso esperado: base do time de Automacao.

Volume:

- 233 registros.
- 24 colunas.

Work item types:

- Task: 133.
- User Story: 52.
- Feature: 30.
- Blocker: 8.
- Epic: 6.
- Iniciativa: 4.

Estados principais:

- Closed: 184.
- New: 18.
- Desenvolvimento: 8.
- Em execucao: 6.
- Em homologacao: 4.
- Alinhamento Estrategico: 3.
- Homologacao: 3.

Area Path:

- `Automação`: 233 registros.

Cobertura de datas:

- Created Date: 233/233.
- Start Date: 4/233.
- Resolved Date: 18/233.
- Closed Date: 184/233.

Limite importante:

- Start Date tem cobertura muito baixa: 4/233.
- Story Points nao possui cobertura.
- Resolved Date tem baixa cobertura: 18/233.
- Blocked tem baixa cobertura: 5/233.

Uso recomendado:

- Throughput por Closed Date.
- Estado atual por fluxo.
- Leitura de volume e distribuicao de trabalho por tipo.
- Analise simples de itens em desenvolvimento, homologacao e new.

Nao usar sem ressalva:

- Cycle time real.
- DORA.
- Capacidade por story points.
- Analise robusta de bloqueio por causa.

### 3. `data.csv`

Uso esperado: base global DTVM, incluindo Engenharia Software 1, Engenharia Software 2, System Team, Datalake, Regulatorios, Tech DTVM, Boletador, Dragon e outras areas.

Volume:

- 5172 registros.
- 24 colunas.

Work item types:

- User Story: 2607.
- Bug: 1431.
- Task: 436.
- Feature: 373.
- Blocker: 191.
- Epic: 49.
- Bug Task: 48.
- Spike: 19.
- Solicitacao: 7.
- Iniciativa: 6.
- Take Off: 5.

Estados principais:

- Closed: 4481.
- New: 241.
- Alinhamento Estrategico: 175.
- Refinamento de Negocio: 69.
- Desenvolvimento: 53.
- QA: 29.
- Deployed: 17.
- Feature Validation: 15.
- Em execucao: 14.
- Backlog: 13.
- Em Discovery: 12.
- Refinamento Tecnico: 11.
- Product Backlog: 10.
- Ready to Deploy: 6.

Area Path principais:

- `DTVM\Tech DTVM`: 2333 registros.
- `DTVM\System Team`: 998 registros.
- `DTVM\Engenharia Software 1`: 682 registros.
- `DTVM\Squad Dragon`: 640 registros.
- `DTVM\Boletador`: 155 registros.
- `DTVM\Engenharia Software 2`: 102 registros.
- `DTVM\Datalake`: 78 registros.
- `DTVM\Regulatorios`: 63 registros.
- `DTVM`: 59 registros.
- `DTVM\Debito Tecnico`: 26 registros.
- `DTVM\Sistemas`: 16 registros.
- `DTVM\Infraestrutura TI`: 15 registros.
- `DTVM\Cadastro MFO`: 5 registros.

Cobertura de datas:

- Created Date: 5172/5172.
- Start Date: 65/5172.
- Resolved Date: 3513/5172.
- Closed Date: 4481/5172.

Bloqueios:

- Blocked preenchido: 713/5172.
- Blocked = Yes: 131 registros.
- Blocked = No: 582 registros.
- Tipo de Bloqueio: 188/5172.

Limite importante:

- Start Date tem baixa cobertura: 65/5172. Cycle time baseado em Start Date deve ser usado com muita cautela.
- Story Points tem baixa cobertura: 207/5172.
- Tipo de Bloqueio tem baixa cobertura: 188/5172.
- A base parece ser snapshot/extração de work items atuais, nao historico completo de transicoes.

Uso recomendado:

- Throughput por Closed Date.
- Lead time aproximado Created Date -> Closed Date.
- Tempo Resolved -> Closed como proxy de fila final ou intervalo ate fechamento, quando ambas datas existirem.
- Analise de bloqueios por Blocked e Tipo de Bloqueio, com ressalva de cobertura.
- Distribuicao por Area Path, Iteration Path, Work Item Type e State.
- Leitura de itens em QA, Ready to Deploy, Deployed, Desenvolvimento, New e Closed.

Nao usar sem ressalva:

- Cycle time real, salvo registros com Start Date confiavel.
- DORA completa.
- Forecast por story points.
- Historico de bloqueio ao longo do tempo.

### 4. `Regulatorios - Iniciativas.csv`

Uso esperado: base especifica de iniciativas regulatorias, especialmente Roubo de Credenciais e Monitoramento de Atipicidades.

Volume:

- 91 registros.
- 16 colunas.

Work item types:

- User Story: 63.
- Spike: 12.
- Feature: 8.
- Epic: 5.
- Iniciativa: 2.
- Bug: 1.

Estados principais:

- Closed: 43.
- Desenvolvimento: 22.
- Deployed: 14.
- Em execucao: 3.
- Alinhamento Estrategico: 2.
- Em Desenvolvimento: 2.
- Em Andamento: 1.
- Removed: 1.
- Feature Validation: 1.
- Quebra em historias: 1.
- Refinamento Tecnico: 1.

Cobertura de datas:

- Created Date: 91/91.
- Start Date: 12/91.
- Resolved Date: 50/91.
- Closed Date: 43/91.

Hierarquia identificada:

- `Roubo de Credenciais` aparece como iniciativa.
- `Monitoramento de Atipicidades | Fraude` aparece como iniciativa.

Epicos / frentes identificadas em Roubo de Credenciais:

- Geracao de Alertas, Tratamento e Evidencias.
- Bloqueio de Acessos atraves de ferramentas Automatizados (Captcha).
- Cadastro de Device Unificado.

Frentes identificadas em Monitoramento de Atipicidades:

- Clientes com dados cadastrais compartilhados.
- Controle de Operacoes de mesma origem.

Limite importante:

- A base possui hierarquia de titulos (`Title 1` a `Title 5`), mas nao possui Area Path nem campos de bloqueio detalhados.
- Start Date tem cobertura parcial: 12/91.
- A base permite analisar situacao por iniciativa, epico, feature e historia, mas nao substitui historico completo do Azure.

Uso recomendado:

- Situacao atual por iniciativa.
- Contagem por Work Item Type.
- Contagem por State.
- Analise de Closed, Deployed, Desenvolvimento e demais status.
- Separacao entre Roubo de Credenciais e Monitoramento de Atipicidades.
- Analise de frentes/epicos e distribuicao de historias.

Nao usar sem ressalva:

- Cycle time real completo.
- Bloqueios por causa, pois nao ha campo de bloqueio nesta base.
- DORA.

## Regras gerais para metricas

### Throughput / Vazao

Preferir calcular throughput com base em `Closed Date`, agrupando por dia, semana, sprint, mes, Area Path ou Iteration Path.

Itens recomendados para throughput:

- User Story.
- Bug, se a pergunta envolver sustentacao ou qualidade.
- Spike, se a pergunta envolver descoberta/refinamento tecnico.

Evitar misturar Task com User Story em leitura executiva de entrega, salvo se o usuario pedir trabalho total.

### Lead time

Quando nao houver outra definicao, usar:

- Lead time aproximado = `Closed Date` - `Created Date`.

Ressalva obrigatoria:

- Esse lead time inclui tempo de backlog, espera, refinamento, priorizacao e execucao.
- Em times de projeto, pode parecer artificialmente alto quando demandas foram criadas muito antes de serem executadas.

### Cycle time

Cycle time real precisaria de data confiavel de inicio de execucao ou historico de transicao para desenvolvimento.

Nas bases analisadas, `Start Date` possui baixa cobertura:

- Dados: 0%.
- Automacao: 1,7%.
- DTVM global: 1,3%.
- Regulatorios: 13,2%.

Portanto, nao usar cycle time real sem ressalva.

Alternativas possiveis:

- usar `Resolved Date` - `Created Date` como tempo ate pronto tecnico, com ressalva;
- usar `Closed Date` - `Resolved Date` como tempo de fila final/intervalo ate fechamento, quando ambas as datas existirem;
- se houver historico de transicoes no futuro, recalcular cycle time a partir da primeira entrada em Desenvolvimento ate Resolved/Closed.

### Resolved versus Closed

Regra importante para diagnosticos:

- `Resolved` representa demanda tecnicamente pronta, em homologacao ou Ready to Deploy, dependendo do fluxo.
- `Closed` representa entrega efetivamente fechada.

Para iniciativas como Roubo de Credenciais, analisar Resolved e Closed separadamente para evitar duas distorcoes:

- olhar apenas Closed pode esconder progresso tecnico;
- olhar apenas Resolved pode exagerar entrega efetiva.

### Bloqueios

Usar `Blocked`, `Tipo de Bloqueio` e `Type Block` quando existirem.

Limite:

- Muitas bases possuem baixa cobertura de bloqueio ou campos vazios.
- Se o usuario perguntar sobre bloqueios historicos, verificar se existe historico de transicoes ou apenas snapshot atual.

### DORA

As bases atuais nao sustentam DORA completa de forma confiavel.

Possivel analisar parcialmente:

- Deploy frequency, se `Closed Date`, `Deployed`, `Ready to Deploy` ou datas de deploy forem bem definidas no recorte.

Nao calcular sem evidencia:

- Change Failure Rate.
- MTTR.

Essas metricas exigem dados confiaveis de falhas, incidentes, recuperacao e mudancas.

## Regras por time / area

### Dados / Engenharia de Dados

Fonte principal: `dadosglobaisdados22.csv`.

Usar para leitura de fluxo e throughput do time de Dados. Ter cuidado com cycle time, bloqueios e story points por baixa cobertura.

### Automacao

Fonte principal: `GlobalAutomacao.csv`.

Usar para leitura de volume, estados e throughput. Considerar que o time iniciou recentemente sprints formais e que Start Date, Resolved Date, Story Points e bloqueios possuem baixa cobertura.

### Engenharia Software 1

Fonte principal: `data.csv`, filtrando `Area Path = DTVM\Engenharia Software 1`.

Usar para perguntas sobre Eng01, incluindo iniciativas regulatorias quando relacionadas ao time. Para Roubo de Credenciais, cruzar tambem com `Regulatorios - Iniciativas.csv` e diagnostico validado.

### Engenharia Software 2

Fonte principal: `data.csv`, filtrando `Area Path = DTVM\Engenharia Software 2`.

Usar para perguntas sobre Eng02 e Monitoramento de Atipicidades quando aplicavel. Cruzar com `Regulatorios - Iniciativas.csv` para iniciativas regulatorias.

### System Team

Fonte principal: `data.csv`, filtrando `Area Path = DTVM\System Team`.

Usar para leitura de fluxo, status, QA, Ready to Deploy, bloqueios, demandas fechadas e sustentacao/apoio tecnico.

### Regulatorios

Fonte principal: `Regulatorios - Iniciativas.csv` para hierarquia da iniciativa e `data.csv` para leitura global quando necessario.

Para narrativa executiva, usar tambem o ODT validado do diagnostico regulatorio.

## Ordem correta quando o usuario pedir metricas

1. Identificar qual time, iniciativa ou recorte foi pedido.
2. Identificar a base correta.
3. Verificar se a pergunta pede numero, tendencia, explicacao ou diagnostico.
4. Para numeros, usar CSV/Azure emulado.
5. Para narrativa executiva ja apresentada, usar PPT/relatorio/ODT.
6. Para interpretacao, usar memoria operacional.
7. Declarar limites da base quando a metrica nao for confiavel.

## Limites gerais das bases

- As bases parecem snapshots/exportacoes de work items, nao historico completo de transicoes.
- Start Date e pouco preenchido na maioria das bases.
- Story Points possui baixa cobertura.
- Bloqueios e tipos de bloqueio possuem cobertura parcial.
- DORA completa nao e suportada pelas bases atuais.
- Lead time baseado em Created Date pode incluir espera antes da execucao.
- Cycle time real depende de historico de entrada em desenvolvimento, que nao esta completo nas bases atuais.

## Decisao operacional

Quando o usuario pedir metricas, a IA deve tratar estas bases como emulacao de Azure DevOps, mas nao como Azure completo.

A resposta deve ser util, calculavel e honesta: mostrar o que da para medir, o que e proxy e o que nao pode ser afirmado sem dados adicionais.