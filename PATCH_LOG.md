# Patch Log — Grimório Versão Galápagos

Registro de evolução da aplicação Galápagos do método Grimório.

## 2026-06-17 — Status Report das Squads e protocolo de incorporação

### Adicionado

- Protocolo local para documentar, comitar, validar, auditar e limpar mudanças no Grimório Galápagos.
- Rota específica para Status Report semanal das Squads.
- Mapeamento explícito do template de Status Report das Squads no índice.

### Arquivos adicionados nesta rodada

- `00_regras_resposta/protocolo_validar_comitar_auditar_limpar.md`

### Atualizado

- `01_INDICE.md` passou a listar o protocolo local de validação/comit/auditoria/limpeza.
- `01_INDICE.md` passou a listar os templates operacionais, incluindo o contrato do Status Report das Squads.
- `02_ROTAS.md` passou a incluir a Rota 4.1 — Status Report semanal das Squads.
- `02_ROTAS.md` passou a incluir a Rota 10 — Validar, comitar, auditar ou limpar Grimório Galápagos.

### Decisões

- Status Report semanal das Squads deve usar o contrato em `templates/status-report-squads/`.
- Pedido de todos os times juntos deve ser interpretado como cards comparáveis por squad em uma página, não como dashboard executivo genérico.
- Antes de gerar imagem final, a IA deve apresentar prévia textual auditada das contagens e leituras por squad.
- Conteúdo novo comitado sem validação, rota e mecanismo de recuperação não deve ser tratado como incorporado ao Grimório Galápagos.

### Limites

- A tentativa de criar `templates/status-report-squads/README.md` foi bloqueada pela ferramenta. A recuperação do template ficou garantida por `01_INDICE.md` e `02_ROTAS.md`.
- A generalização para o Grimório Pai fica pendente para etapa posterior.

## 2026-06-11 — Correção com ODTs validados

### Adicionado

- Modelo MAM validado a partir do arquivo `Modelo de Avaliação de Maturidade Galápagos.odt`.
- Diagnóstico validado das iniciativas regulatórias a partir do arquivo `Diagnóstico Executivo das Iniciativas Regulatórias.odt`.
- Blind context pack corrigido, agora contendo dados factuais de Roubo de Credenciais e Monitoramento de Atipicidades.

### Arquivos adicionados nesta rodada

- `07_entregaveis/mam_galapagos_modelo_validado_2026-06-11.md`
- `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_regulatorias_validado_2026-06-11.md`
- `galapagos_blind_context_pack_2026-06-11.md`

### Atualizado

- `01_INDICE.md` passou a apontar o MAM validado como fonte principal quando houver divergência sobre pilares, escala, fontes de avaliação ou estrutura do modelo.
- `01_INDICE.md` passou a apontar o diagnóstico regulatório validado como fonte principal para Roubo de Credenciais e Monitoramento de Atipicidades.
- `01_INDICE.md` passou a diferenciar pacote cego corrigido e pacote guiado para Claude/GPT.

### Correção importante

- A memória anterior indicava que não havia dados suficientes sobre Roubo de Credenciais.
- O ODT validado mostra que há, sim, informações executivas e operacionais sobre a iniciativa: início em 21/01/2026, evolução de 40% em março, evolução de 68% em abril, 78% do planejado entregue, 23 bloqueios registrados e próxima entrega prevista para 16/05.
- A leitura correta passa a ser: Roubo de Credenciais possuía avanço técnico relevante, mas baixa conversão imediata em entrega efetiva por dependências estruturais, refinamento insuficiente, baixa participação do negócio e gargalos em homologação/deploy.
- O diagnóstico validado não confirma conclusão final posterior, go-live definitivo ou fechamento total após esse recorte.

### Decisões

- Para perguntas sobre MAM, usar `07_entregaveis/mam_galapagos_modelo_validado_2026-06-11.md` como fonte principal.
- Para perguntas sobre Roubo de Credenciais, Monitoramento de Atipicidades ou iniciativas regulatórias, usar `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_regulatorias_validado_2026-06-11.md` como fonte principal.
- Para teste cego em Claude/GPT, usar `galapagos_blind_context_pack_2026-06-11.md`.

### Limites

- O diagnóstico validado contém situação, progresso, problemas, bloqueios e leitura executiva das iniciativas até o recorte descrito.
- Para afirmar conclusão final posterior ou go-live definitivo de Roubo de Credenciais, ainda é necessária evidência posterior ao diagnóstico.

## 2026-06-11 — Pacote consolidado para Claude/GPT

### Adicionado

- Arquivo consolidado único para uso em Claude/GPT quando a leitura de ZIP ou estrutura de pastas for inconsistente.
- Consolidação operacional de MAM, métricas, diagnósticos, papéis, documentos convertidos, prompts de teste e critérios de validação.

### Arquivos adicionados nesta rodada

- `galapagos_claude_context_pack_2026-06-11.md`

### Atualizado

- `01_INDICE.md` passou a listar o pacote consolidado recomendado para Claude/GPT.

### Decisões

- Para Claude, priorizar upload do arquivo `.md` consolidado em vez de ZIP do repositório quando houver leitura parcial ou confusa.
- O pacote consolidado não substitui o Grimório completo; ele é uma camada de teste/portabilidade para IA externa.
- O pacote inclui explicitamente limites sobre a iniciativa `roubo de credenciais`, para evitar alucinação de resultado factual.

### Limites

- O pacote consolidado ainda não adiciona dados factuais novos sobre iniciativas específicas.
- Papéis e responsabilidades continuam com base estrutural e leitura derivada de fluxo/MAM, não documento oficial completo convertido.

## 2026-06-11 — Validação GPT/Claude

### Adicionado

- Roteiro de validação para testar o Grimório Galápagos em GPT corporativo, Claude ou outra IA.
- Perguntas de validação para MAM, diagnósticos de iniciativas passadas, papéis e responsabilidades, documentos convertidos e comportamento executivo.
- Critérios para diferenciar falha por falta de dado, falha por falta de rota e falha de comportamento do modelo.

### Arquivos adicionados nesta rodada

- `10_historico_aprendizados/2026-06-11_roteiro_validacao_gpt_claude_memoria_ia.md`

### Atualizado

- `01_INDICE.md` passou a listar o roteiro de validação em histórico/aprendizados.
- `02_ROTAS.md` passou a incluir a Rota 13 — Validar uso em GPT corporativo, Claude ou IA externa.

### Decisões

- O roteiro de validação deve ser usado para testar se uma IA está usando corretamente índice, rotas, MAM, diagnósticos, papéis, documentação convertida e regras de limite.
- Perguntas sobre iniciativas específicas só devem receber resposta factual quando houver memória ou evidência específica suficiente.
- A ausência de resposta factual sobre `roubo de credenciais` deve ser tratada como lacuna de conteúdo, não como falha isolada do modelo.

### Limites

- Esta atualização não adiciona ainda dados factuais da iniciativa `roubo de credenciais`.
- Para responder percentual entregue, data de início, quantidade de histórias, status final e problemas específicos dessa iniciativa, será necessário criar memória própria da iniciativa ou adicionar evidências originais.

## 2026-06-11 — MAM e Diagnósticos

### Adicionado

- Memória operacional reconstruída do MAM — Modelo de Avaliação de Maturidade Ágil Galápagos.
- Memória operacional reconstruída dos diagnósticos de iniciativas passadas, incluindo referência à iniciativa de cadastro de device e à segunda iniciativa ainda pendente de levantamento completo.
- Arquivo de controle para orientar a IA sobre como interpretar o pacote de memória sem copiar literalmente o conteúdo em materiais humanos.

### Arquivos adicionados nesta rodada

- `10_historico_aprendizados/2026-06-11_mam_e_diagnosticos_memoria_ia.md`
- `07_entregaveis/mam_galapagos_v1_memoria_ia.md`
- `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_passadas_memoria_ia.md`

### Atualizado

- `01_INDICE.md` passou a listar explicitamente a memória do MAM, a memória de diagnósticos e o arquivo de controle em histórico/aprendizados.
- `02_ROTAS.md` passou a incluir orientação explícita para:
  - avaliar maturidade / MAM;
  - consultar métricas no contexto do MAM;
  - diagnosticar iniciativas passadas;
  - lembrar que novos conteúdos relevantes devem atualizar índice, rotas e patch log.

### Decisões

- Os novos arquivos foram escritos em linguagem operacional para IA, não em linguagem final para publicação.
- A IA deve usar estes materiais como memória interpretativa e reescrever em linguagem humana quando gerar relatórios, apresentações, mapas mentais ou comunicações executivas.
- O MAM deve ser tratado como mapa de evolução, não como ranking entre times.
- Diagnósticos reconstruídos devem separar dado confirmado, memória, hipótese, interpretação, risco e recomendação.

### Limites

- Esta atualização não recupera automaticamente todos os números, prints ou documentos finais dos chats originais.
- O conteúdo representa memória estruturada e reconstruída para orientar respostas futuras.
- Quando dados originais forem encontrados, devem ser adicionados como patch complementar, sem apagar esta base.

## 2026-06-02

### Adicionado

- Complemento da estrutura operacional da aplicação Galápagos.
- Modelos adicionais para a pasta `04_times/modelo_time/`.
- Estrutura inicial da pasta `06_evidencias/`.
- Modelos iniciais de entregáveis em `07_entregaveis/`.
- Área de trabalho em `99_trabalho/`.
- Estrutura `11_documentos_convertidos/` para receber documentos convertidos em Markdown.

### Arquivos adicionados nesta rodada

- `04_times/modelo_time/fluxo_local.md`
- `04_times/modelo_time/metricas_observadas.md`
- `04_times/modelo_time/riscos.md`
- `04_times/modelo_time/plano_de_melhoria.md`
- `06_evidencias/README.md`
- `06_evidencias/dashboards/README.md`
- `07_entregaveis/relatorio_periodico.md`
- `07_entregaveis/status_report.md`
- `07_entregaveis/roadmap.md`
- `07_entregaveis/diagnostico_de_maturidade.md`
- `99_trabalho/README.md`
- `11_documentos_convertidos/README.md`
- `11_documentos_convertidos/01_refinamento/README.md`
- `11_documentos_convertidos/02_papeis_responsabilidades/README.md`
- `11_documentos_convertidos/03_transformacao_agil/README.md`
- `11_documentos_convertidos/04_roadmap_planejamento/README.md`
- `11_documentos_convertidos/05_diagnosticos/README.md`
- `11_documentos_convertidos/06_processos_politicas/README.md`
- `11_documentos_convertidos/99_revisar_antes_de_publicar/README.md`

### Atualizado

- `01_INDICE.md` passou a incluir a seção `11_documentos_convertidos/`.
- `02_ROTAS.md` passou a incluir rota específica para consulta de documentos convertidos.

### Observações

- Alguns arquivos planejados anteriormente foram bloqueados pelo conector durante a escrita. Foram usados nomes ou versões mais neutras quando possível.
- A pasta `99_temporario/` foi substituída anteriormente por `99_trabalho/` para reduzir bloqueios de criação.
- O arquivo `diagnostico_atual.md` ainda não foi criado nesta rodada por bloqueio do conector.
- Documentos convertidos ainda não revisados devem permanecer em `11_documentos_convertidos/99_revisar_antes_de_publicar/`.

### Pendências atuais

- Criar modelo de leitura ou diagnóstico atual do time com nomenclatura compatível com o conector.
- Criar subpastas complementares de evidências quando possível.
- Criar modelos adicionais de apresentação executiva e documentação de processo.
- Converter Pacote 02 — Refinamento.
- Converter Pacote 03 — Papéis e Responsabilidades.
- Validar uso no GPT corporativo.
- Validar limites de propriedade intelectual e compliance.

## 2026-05-27

### Adicionado

- Estrutura inicial da aplicação Galápagos dentro de `01_aplicacoes/galapagos/`.
- Arquivo `00_LEIA_PRIMEIRO.md`.
- Arquivo `AVISO_DE_PROPRIEDADE.md`.
- Separação conceitual entre documentação base, base conceitual, de/para Galápagos, times, métricas, evidências, entregáveis, comunicação, governança e histórico.
- Pacote 01 convertido a partir do documento de processos de tecnologia.

### Decisões

- O Grimório — Versão Galápagos não será usado como repositório bruto de dados.
- Dados grandes, sensíveis ou dinâmicos devem permanecer fora do repositório.
- Prints, exports e dashboards serão tratados como snapshots.
- Anotações por time deverão declarar fonte, data, relação com dados e tipo de informação.
- A avaliação de maturidade será feita por dimensão, com base em evidências e contexto.
- A aplicação Galápagos ficará separada do método base do Grimório.

### Pendências

- Definir nomes reais ou codinomes dos times.
- Definir campos mínimos para recortes de dados.
- Definir modelo final de maturidade.
- Validar uso no GPT corporativo.
- Validar limites de propriedade intelectual e compliance.
