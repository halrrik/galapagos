# DIAGNOSTICO DE INICIATIVAS PASSADAS — MEMORIA_IA

status: memoria_reconstruida
classe: diagnostico_iniciativas_galapagos
origem: conversas_projeto_galapagos
uso: apoiar_relatorios_executivos_e_leituras_de_fluxo
nao_usar_como: relatorio_final_textual_sem_reescrita

## Intencao

Registrar memoria operacional sobre diagnosticos de iniciativas analisadas no contexto Galapagos, incluindo iniciativa de cadastro de device e segunda iniciativa ainda nao totalmente especificada nesta memoria.

Esta memoria deve ajudar a IA a reconstruir relatorios graficos e textuais, leituras executivas, conclusoes e possiveis acoes, sem depender apenas do chat original.

## Iniciativa 1 — Cadastro de device

Identificacao: projeto/iniciativa de cadastro de device.

Estado da memoria: existe historico de analise em conversas anteriores, mas os dados finais completos, graficos e documento final nao estavam versionados no repositorio no momento desta atualizacao.

Leitura operacional geral:

- iniciativa acompanhada por metricas de fluxo e status;
- havia necessidade de relatorio grafico e textual para Arthur Oliveira;
- leitura deveria explicar o que aconteceu no projeto, nao apenas mostrar numeros;
- relatorio deveria ser executivo, com foco em fluxo, gargalos, eficiencia, riscos e proximas acoes;
- a analise deveria evitar conclusoes sem contexto dos dados.

Temas provaveis analisados:

- throughput / vazao;
- lead time;
- cycle time;
- bloqueios;
- idade em status;
- gargalos em homologacao / QA;
- gargalos em ready to deploy / deploy;
- dependencia de areas externas;
- impacto de priorizacao, refinamento e dependencias entre historias;
- diferenca entre conclusao tecnica e entrega efetiva em producao.

Regras para reconstituicao futura:

- nao inventar numeros;
- se houver prints ou CSVs no chat original, usar como fonte primaria;
- se nao houver dados, produzir leitura conceitual com limitacao explicita;
- separar gargalo interno do time de dependencia externa;
- explicar impactos em eficiencia sem culpabilizar pessoas;
- destacar quando outliers distorcem media;
- usar cycle time para leitura de execucao quando lead time for contaminado por backlog criado cedo demais.

## Iniciativa 2 — Outra iniciativa a levantar

Identificacao: segunda iniciativa mencionada como "o outro que vamos levantar".

Estado da memoria: insuficiente para diagnostico conclusivo.

Regra:

- tratar como iniciativa pendente de levantamento;
- nao assumir nome, escopo, status, metricas ou conclusoes;
- pedir ou usar evidencias quando fornecidas;
- estruturar diagnostico com o mesmo modelo da iniciativa de cadastro de device quando os dados existirem.

## Modelo de diagnostico usado nas iniciativas

Entrada minima:

- contexto da iniciativa;
- periodo analisado;
- time ou times envolvidos;
- fonte dos dados;
- status das demandas;
- datas relevantes;
- bloqueios;
- gargalos por etapa;
- riscos;
- decisoes ou dependencias externas.

Saida esperada:

1. Resumo executivo.
2. O que aconteceu no periodo.
3. Leitura de fluxo.
4. Gargalos e causas provaveis.
5. Impacto na eficiencia.
6. Riscos atuais.
7. Conclusoes.
8. Acoes recomendadas.
9. Limites da analise.

## Padroes de leitura ja consolidados

### Lead time vs cycle time

Lead time pode ser inadequado quando demandas sao criadas com muita antecedencia e ficam aguardando relevancia/priorizacao. Nesses casos, lead time mede tambem espera de backlog/upstream, nao apenas execucao.

Cycle time tende a ser melhor para analisar eficiencia de execucao, desde que o ponto de inicio esteja corretamente definido.

### Deploy frequency

Deploy frequency deve representar frequencia real de disponibilizacao em producao. Quando nao ha historico adequado, pode-se usar proxy, mas o proxy deve ser declarado.

Exemplo de proxy discutido: tempo entre resolved e closed pode indicar fila de deploy quando resolved representa pronto tecnico e closed representa efetiva disponibilizacao. Isso nao deve ser chamado de deploy frequency sem ressalva; pode ser melhor tratar como tempo em fila de deploy ou intervalo ate fechamento.

### QA / homologacao

QA/homologacao pode gerar gargalo por:

- capacidade limitada de pessoas testando;
- dependencia de area de negocio;
- validacao de fluxo;
- permissao ou ajuste de infraestrutura;
- espera por ambiente;
- criterio de aceite incompleto;
- demanda chegando com ambiguidade.

Regra: nao afirmar que todo gargalo em QA e falha do time. Identificar causa.

### Ready to deploy / deploy

Ready to deploy pode gerar fila por:

- cadencia de deploy semanal;
- dependencia de infraestrutura;
- dependencia de banco de dados;
- janela planejada de publicacao;
- politica interna de liberacao;
- acoplamento entre historias.

Regra: diferenciar fila planejada de atraso nao planejado. Mesmo quando planejada, a fila pode impactar eficiencia percebida e tempo total de entrega.

### Bloqueios

Bloqueios devem ser analisados por:

- quantidade;
- percentual de demandas afetadas;
- tempo bloqueado;
- tipo de bloqueio;
- origem do bloqueio;
- recorrencia;
- responsabilidade de tratamento;
- impacto no fluxo.

Bloqueio nao deve ser usado apenas como contagem. O tipo e a causa importam mais para decisao.

### Dependencias entre historias

Quando muitas historias pertencem a mesma feature ou fluxo, pode haver dependencia entre elas. Isso reduz paralelismo real, aumenta espera, gera bloqueios e distorce planejamento de sprint.

Acao recomendada: revisar quebra das historias, sequenciamento e criterios de prontidao antes de puxar para execucao.

## Linguagem executiva recomendada

Evitar:

- culpabilizar time;
- dizer que o time nao entrega sem contexto;
- usar metrica isolada como prova absoluta;
- transformar outlier em conclusao geral;
- esconder gargalos para parecer positivo.

Preferir:

- "A eficiencia foi impactada por gargalos nas etapas finais do fluxo";
- "O desenvolvimento demonstra capacidade de avancar, mas a conversao em entrega efetiva depende da reducao de filas posteriores";
- "Os dados indicam necessidade de separar gargalos internos de dependencias externas";
- "A proxima melhoria deve focar em reduzir espera, explicitar dependencias e melhorar previsibilidade de deploy/homologacao".

## Acoes recomendadas recorrentes

- Revisar criterios de prontidao das historias.
- Mapear dependencias antes da sprint/ciclo.
- Medir bloqueios por tipo e tempo.
- Separar tempo de desenvolvimento de tempo em homologacao/deploy.
- Reduzir filas entre pronto tecnico e producao.
- Definir cadencia de deploy compativel com criticidade e volume.
- Tratar outliers separadamente.
- Usar retrospectiva para causas recorrentes, nao apenas sintomas.
- Criar leitura executiva com dados e narrativa curta.
- Manter historico por time e iniciativa para comparacao futura.

## Limites desta memoria

Esta memoria nao contem todos os numeros, prints, graficos ou documentos finais das iniciativas. Deve ser usada para orientar recuperacao e reconstrucao. Quando os dados originais forem encontrados, criar patch complementar com evidencias, numeros e conclusoes finais.
