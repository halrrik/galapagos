# Status Report das Squads — Template reutilizável

Versão canônica: **1.0**  
Base da versão: **v8_recontagem**  
Data de definição: **2026-06-17**

Este documento define o template do **Status Report das Squads** para que, nas próximas rodadas, seja possível receber os dados do Azure DevOps/Power BI, processar as regras e gerar a imagem/slide sem rediscutir estrutura, linguagem e critérios.

## Objetivo

Gerar uma capa executiva comparável por squad, com leitura curta sobre cerimônias, prioridades, entrega, impedimentos e risco de transbordo. A entrega deve responder ao que Jeremias pediu, usando linguagem direta e operacional, sem transformar a primeira página em diagnóstico amplo.

A superfície do slide deve ser curta e comparável. A camada causal pode orientar os textos, mas não deve dominar a apresentação.

## Linguagem aprovada

Título: **Status Report das Squads**  
Subtítulo: **Cerimônias, prioridades, entrega e impedimentos**

Usar como metadado no topo:

**Período analisado:** últimos 7 dias corridos  
**Escopo operacional:** demandas (User Stories/Bugs)  
**Base:** Azure DevOps / Power BI

Evitar como linguagem principal da capa: diagnóstico, maturidade, DORA, lead time, cycle time, throughput, governança de IA, modelo robusto, saúde do fluxo.

Esses conceitos podem orientar a análise por baixo, mas não devem aparecer como entrada principal da entrega.

## Estrutura visual

Formato: **16:9 horizontal**  
Render recomendado: **3840 x 2160 px**  
Preview recomendado: **1920 x 1080 px**

Estilo visual: fundo branco, azul institucional Galapagos, cards executivos, pouca ornamentação, visual limpo próximo aos decks de Comitê de Tecnologia.

Ordem dos cards:

1. Engenharia 1
2. Engenharia 2
3. Automação
4. Dados
5. System Team

Cada card deve conter:

1. Nome do time
2. Status
3. Demanda macro em foco
4. Cerimônias
5. Prioridade
6. Transbordo
7. Planejado ou Criado
8. Fechado
9. Bloqueios
10. Principal ponto de atenção
11. Próxima ação
12. Critério: **Fechado = entrega executiva**

## Campos do card

### Status

Valores possíveis:

- **Em dia**: operação controlada.
- **Atenção**: há ponto relevante a acompanhar.
- **Ação necessária**: há risco concreto para entrega ou alinhamento.
- **A definir**: dados insuficientes ou leitura não validada.

### Demanda macro em foco

Representa a demanda macro/iniciativa dominante em execução no período.

Quando houver dados suficientes, deve ser obtida por rastreabilidade:

**User Story/Bug → Feature → Epic → Initiative**

A rastreabilidade deve usar `Parent Work Item Id`. Se o export vier sem `Work Item Id` real e sem `Parent Work Item Id` real, não afirmar que houve rastreabilidade automática até iniciativa. Nesse caso, usar inferência textual com ressalva.

### Cerimônias

Valores: **Sim / Parcial / Não / A definir**.

Campo manual/observacional por enquanto, baseado em dailies e conversa com Jeremias.

### Prioridade

Valores: **Sim / Parcial / Não / A definir**.

Indica se está claro o que está sendo priorizado ou trabalhado. Pode ser parcialmente derivado dos dados, mas ainda depende de leitura do board e contexto.

### Transbordo

Valores: **Sim / Não / A definir**.

Indica risco de demandas planejadas/priorizadas não fecharem dentro do período/ciclo e transbordarem. Por enquanto é campo manual. Futuramente pode combinar percentual fechado, bloqueios, dias restantes, itens em homologação/deploy e dependências.

### Planejado / Criado

Para Engenharia 1, Engenharia 2, Automação e Dados, o campo aparece como **Planejado**.

Para System Team, o campo aparece como **Criado**, porque sustentação inicia contagem desde a criação da demanda.

### Fechado

Conta somente itens **User Story** ou **Bug** fechados. Para liderança, somente `Closed` conta como entrega executiva.

Itens em `Resolved`, `Waiting to Deploy`, `Homologação`, `QA` ou similares podem estar em etapa de entrega, mas **não contam como Fechado**.

### Bloqueios

Conta bloqueios ativos/atuais quando houver Work Item Type específico de bloqueio, ou campo confiável de bloqueio. Bloqueio não entra na contagem de demandas planejadas/criadas/fechadas.

### Principal ponto de atenção

Frase curta, executiva e orientada à decisão.

Não usar o rótulo “opinião”. Quando houver bloqueio concreto, pode ser mencionado dentro do texto.

### Próxima ação

Frase curta, prática e acionável. Deve ajudar Jeremias a conversar com o time ou com negócio.

## Regras de dados

### Regra fundamental de situação atual

`Is Current = TRUE/Yes` representa a situação atual real.

Linhas históricas servem para entender movimentação, mudança de status, entrada em In Progress, tempo bloqueado e eventos do período. Elas **não** devem ser contadas como situação atual.

### Tipos que entram nas contagens principais

Entram apenas:

- **User Story**
- **Bug**

Não entram nas contagens principais:

- Task
- Feature
- Epic
- Initiative
- Blocked / Blocker
- Qualquer outro tipo auxiliar

### Período

No slide, usar: **últimos 7 dias corridos**.

Na extração técnica, pode-se usar **últimos 8 dias** para evitar perda por horário/corte, mas a comunicação executiva continua sendo “últimos 7 dias corridos”.

## Regras por squad

### Engenharia 1

Campo: **Planejado**.

Conta somente User Story/Bug atuais, com `Is Current = TRUE/Yes`, na iteration mais recente/confiável do time, com status mínimo de **Backlog** ou entrada real em **In Progress**.

Não contar:

- New
- Refinamento Técnico
- Refinamento de Negócio
- Product Backlog
- Histórico não atual
- Task, Feature, Epic, Initiative, Blocked

### Engenharia 2

Mesma regra da Engenharia 1.

Quando Iteration Path não for confiável, usar proxy temporário explícito. Não mascarar como precisão total.

### Automação

Mesma regra base de Engenharia 1 e 2.

Conta User Story/Bug atuais com status mínimo de Backlog ou entrada real em In Progress. Excluir New, refinamentos e Product Backlog.

A leitura qualitativa deve manter atenção à quebra das demandas e qualidade da escrita das histórias, mas isso é frente futura, não campo principal da capa atual.

### Dados

Campo: **Planejado**.

Usar **Iteration Path vigente** do time.

No corte validado nesta conversa, Dados deveria ter **18 itens planejados**, sendo:

- 16 em Active
- 2 em Backlog

Somente User Story/Bug. Itens em New não entram.

Se o número divergir desse corte, revisar arquivo/filtro antes de gerar o slide.

### System Team

Campo: **Criado**, não Planejado.

Como sustentação, desde a criação a demanda já inicia relógio/contador. Contar demandas criadas/abertas para atendimento, apenas User Story/Bug.

Sempre que possível, separar sustentação, GLPI, incidentes e demandas planejadas.

## Rastreabilidade até demanda macro

A rastreabilidade correta é:

`User Story/Bug` → `Feature` → `Epic` → `Initiative`

A demanda macro em foco deve ser a Initiative dominante quando houver dados suficientes.

Para funcionar, o arquivo precisa trazer linhas dos pais, mesmo que eles não tenham sido alterados no período. O mínimo para a hierarquia é:

- Work Item Id
- Title
- Work Item Type
- Parent Work Item Id
- Area Path
- State
- Is Current

Se o arquivo tiver apenas contagens agregadas, não há como fazer rastreabilidade segura.

## Area Path e squad

Nem todo `Area Path` representa squad. Alguns podem representar portfólio, regulatório ou agrupamento macro.

Antes de contar, confirmar mapa manual:

- Engenharia 1 = caminhos válidos a definir
- Engenharia 2 = caminhos válidos a definir
- Automação = caminhos válidos a definir
- Dados = caminhos válidos a definir
- System Team = caminhos válidos a definir

Não inferir squad apenas por qualquer Area Path sem validação.

## Campos esperados no próximo arquivo

Para Work Items:

- Work Item Id
- Title
- Work Item Type
- State
- State Category
- Board Column
- Assigned To
- Area Path
- Iteration Path
- Created Date
- Changed Date
- Resolved Date
- Closed Date
- Blocked
- Parent Work Item Id
- Is Current

Para bloqueios:

- Work Item Id
- Title
- Work Item Type
- State
- Parent Work Item Id
- Created Date
- Changed Date
- Closed Date
- Tipo de bloqueio
- Area Path
- Is Current

Evitar por enquanto:

- Tags, porque podem gerar ruído.
- Description, salvo quando a análise de qualidade da escrita das histórias virar objetivo do relatório.

## Critérios de leitura

**Card no board não é entrega.**

**Se não está fechado, não está entregue para liderança.**

**Muitas demandas em andamento não significam produtividade.**

**Bloqueio precisa estar registrado no board/campo correto.**

**Conversa relevante de daily precisa virar informação rastreável.**

**Demanda com dependência relevante não deve entrar no planejamento sem condição real de entrega.**

## Limitações conhecidas

1. Power BI pode exportar dados agregados sem Work Item Id real e Parent Work Item Id real. Nesse caso, a rastreabilidade até Initiative não é confiável.
2. A imagem funciona para envio rápido, mas a fonte ainda pode ficar pequena quando colada no PowerPoint. Próxima versão deve priorizar aumento de fonte ou migrar para PPT editável.
3. Quando os arquivos vierem quebrados por status/coluna, deduplicar por Work Item Id real.
4. Quando não houver Work Item Id real, tratar números como aproximação ou leitura agregada, não como verdade auditável.
5. System Team usa regra diferente porque opera como sustentação.

## Checklist da próxima execução

1. Receber os CSV/XLSX.
2. Conferir se há Work Item Id real e Parent Work Item Id real.
3. Confirmar mapa de Area Path → Squad.
4. Filtrar situação atual com `Is Current = TRUE/Yes` para contagens atuais.
5. Contar somente User Story/Bug para Planejado, Criado e Fechado.
6. Aplicar regra específica por squad.
7. Para Dados, validar se o corte/iteration esperado ainda bate com 18 quando for o mesmo período.
8. Gerar os campos dos cards.
9. Revisar Principal ponto de atenção e Próxima ação para não ficarem diagnósticos demais.
10. Gerar imagem 16:9 em alta resolução e preview.
11. Conferir legibilidade da fonte antes de enviar.

## Arquivos-base desta sessão

- Imagem final de referência: `status_report_squads_dados_v8_recontagem.png`
- Preview final de referência: `status_report_squads_dados_v8_recontagem_preview.png`
- Script protótipo: `generate_status_report_v8_recontagem.py`
- Contrato JSON desta definição: `status_report_squads_template_definition_v1.json`
