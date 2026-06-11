# GALAPAGOS — CONTEXTO CONSOLIDADO PARA CLAUDE/GPT

status: pacote_consolidado_para_leitura_por_IA
versao: 2026-06-11
uso: subir como arquivo unico no Claude/GPT quando ZIP ou repositorio forem lidos de forma inconsistente
nao_usar_como: documento humano final

## COMO USAR ESTE ARQUIVO

Este arquivo consolida as partes mais importantes do Grimorio Galapagos para testes em Claude/GPT.

Use este arquivo quando a IA:

- diz que nao consegue ler o ZIP;
- enxerga nomes de arquivos, mas nao aplica o conteudo;
- responde de forma incompleta sobre MAM;
- responde genericamente sobre diagnosticos;
- nao encontra rotas, indice ou memorias operacionais.

Regra para a IA:

1. Use este arquivo como fonte principal de contexto.
2. Nao copie literalmente trechos marcados como MEMORIA_IA.
3. Transforme a memoria em linguagem humana quando responder para gerente, CTO ou apresentacao.
4. Separe fato, memoria reconstruida, limite, interpretacao e recomendacao.
5. Nao invente numero, data, percentual, quantidade de historias ou status quando nao estiver neste arquivo.

---

# 1. ENTRADA OBRIGATORIA DO GRIMORIO GALAPAGOS

Para qualquer pergunta sobre Galapagos, a IA deve seguir esta ordem conceitual:

1. Ler regras iniciais e limites.
2. Consultar indice.
3. Consultar rotas.
4. Escolher arquivos corretos.
5. Separar fato, hipotese, interpretacao e recomendacao.
6. Responder em linguagem humana adequada ao publico.

Arquivos conceituais de entrada no repositorio:

- `00_LEIA_PRIMEIRO.md`
- `README.md`
- `01_INDICE.md`
- `02_ROTAS.md`
- `PATCH_LOG.md`
- `AVISO_DE_PROPRIEDADE.md`

---

# 2. ROTAS PRINCIPAIS

## Rota MAM / Maturidade

Usar quando a pergunta envolver:

- MAM;
- Modelo de Avaliacao de Maturidade Agil Galapagos;
- perguntas de maturidade;
- avaliacao por pilar;
- avaliacao trimestral;
- visual de resultado por time;
- plano de evolucao do time.

Arquivos-base:

- `07_entregaveis/mam_galapagos_v1_memoria_ia.md`
- `07_entregaveis/diagnostico_de_maturidade.md`
- `04_times/modelo_time/maturidade.md`
- `05_metricas_e_dados/metricas_principios_e_camadas.md`
- `05_metricas_e_dados/catalogo_metricas_operacionais.md`

Saida esperada:

- dimensoes avaliadas;
- perguntas ou criterios;
- evidencias;
- leitura atual;
- metricas prioritarias de fluxo;
- riscos;
- recomendacoes;
- proximos passos;
- aviso de que maturidade e mapa de evolucao, nao ranking.

## Rota Diagnosticos de Iniciativas

Usar quando a pergunta envolver:

- diagnosticos feitos anteriormente;
- projeto de cadastro de device;
- iniciativa roubo de credenciais;
- relatorio grafico e textual de iniciativa;
- gargalos, bloqueios, QA, homologacao, deploy;
- recuperacao de conclusoes e acoes passadas.

Arquivos-base:

- `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_passadas_memoria_ia.md`
- `07_entregaveis/status_report.md`
- `07_entregaveis/relatorio_periodico.md`
- `05_metricas_e_dados/metricas_principios_e_camadas.md`
- `05_metricas_e_dados/catalogo_metricas_operacionais.md`

Saida esperada:

- deixar claro o que e memoria reconstruida e o que e dado confirmado;
- nao inventar numeros;
- separar evidencia, interpretacao, hipotese, risco e recomendacao;
- responder de modo executivo quando pedido;
- indicar limites quando dados originais nao estiverem presentes.

## Rota Papeis e Responsabilidades

Usar quando a pergunta envolver:

- papel do lider;
- papel do lider tecnico;
- papel do time;
- papel de analise de negocio;
- Scrum Master, PMO ou gestao de fluxo;
- ownership e accountability;
- responsabilidades em ceremonias ou no fluxo.

Arquivos-base:

- `11_documentos_convertidos/02_papeis_responsabilidades/README.md`
- `01_documentacao_base/modelo_operacional_tecnologia.md`
- `01_documentacao_base/artefatos_hierarquia_trabalho.md`
- `01_documentacao_base/fluxos_de_trabalho_e_boards.md`
- `08_comunicacao/README.md`

Limite atual:

- existe README e rota para papeis;
- ainda nao ha memoria detalhada convertida completa de papeis e responsabilidades;
- respostas sobre papel do lider podem usar MAM, fluxo, metricas e documentacao base, mas devem declarar limite se o usuario pedir documento oficial completo.

## Rota Documentos Convertidos

Usar quando a pergunta envolver:

- documentos passados;
- materiais convertidos de Word, PDF, apresentacao ou consolidado;
- refinamento;
- papeis e responsabilidades;
- transformacao agil;
- roadmap e planejamento;
- diagnosticos;
- processos e politicas.

Estrutura atual:

- `11_documentos_convertidos/01_refinamento/`
- `11_documentos_convertidos/02_papeis_responsabilidades/`
- `11_documentos_convertidos/03_transformacao_agil/`
- `11_documentos_convertidos/04_roadmap_planejamento/`
- `11_documentos_convertidos/05_diagnosticos/`
- `11_documentos_convertidos/06_processos_politicas/`
- `11_documentos_convertidos/99_revisar_antes_de_publicar/`

Regra:

- documentos convertidos devem indicar origem, data de conversao e status de revisao;
- materiais sensiveis ou ainda nao revisados devem permanecer em `99_revisar_antes_de_publicar`;
- nao assumir que todo pacote previsto ja contem documento completo.

---

# 3. MAM GALAPAGOS V1 — MEMORIA OPERACIONAL

## Definicao

MAM = Modelo de Avaliacao de Maturidade Agil Galapagos.

Objetivo principal: avaliar maturidade operacional e agil de times de tecnologia no contexto Galapagos, com foco em fluxo, qualidade, previsibilidade, bloqueios, colaboracao, governanca e melhoria continua.

Nao e ranking de times. Nao e instrumento punitivo. Nao mede valor humano. Nao substitui leitura contextual. Nao deve gerar comparacao simplista entre times com naturezas diferentes.

A avaliacao deve apoiar:

- entendimento do estado atual;
- identificacao de gargalos;
- definicao de planos de melhoria;
- leitura executiva de evolucao;
- acompanhamento trimestral;
- conexao entre comportamento operacional e metricas de fluxo.

## Periodicidade

Periodo padrao: ciclos de 3 meses.

Justificativa: maturidade nao deve ser avaliada em janela curta demais. Periodo trimestral reduz ruido de sprint isolada, outliers pontuais e eventos excepcionais.

## Unidade de avaliacao

Unidade primaria: time.

Aplicacao recomendada:

- resposta individual quando houver risco de pressao social ou vies de grupo;
- consolidacao por time;
- leitura qualitativa por lider/agilidade/facilitador;
- comparacao do time contra ele mesmo ao longo do tempo.

Evitar workshop onde pessoas se sintam pressionadas a responder de forma politicamente segura.

## Principios

- avaliar evidencia, nao percepcao solta;
- usar metricas como contexto, nao como sentenca;
- interpretar respostas com dados de fluxo;
- considerar tipo de time: projeto, sustentacao, automacao, plataforma, system team ou hibrido;
- distinguir problema do time de problema sistemico;
- observar gargalos fora do time quando impactarem eficiencia;
- evitar maturidade cosmetica baseada em cerimonias;
- preferir sinais de fluxo real, qualidade e decisao.

## Escala sugerida

Escala de 1 a 5 por item ou pilar.

1 = inexistente ou ad hoc. Pratica depende de esforco individual, nao ha previsibilidade, evidencias sao fracas.

2 = inicial. Existem praticas pontuais, mas inconsistentes, reativas ou pouco conectadas ao fluxo.

3 = em consolidacao. Praticas existem, sao reconhecidas pelo time e geram alguma previsibilidade, mas ainda ha fragilidade.

4 = consistente. Praticas estao integradas ao trabalho, sustentam decisoes e reduzem desperdicio.

5 = evolutivo. Time usa dados, aprendizado e feedback para melhorar continuamente o sistema de trabalho.

Regra: nota sem evidencia deve ser tratada como percepcao, nao como avaliacao fechada.

## Pilares

### Pilar 1 — Fluxo de trabalho

Pergunta central: o trabalho flui de forma visivel, gerenciavel e previsivel?

Sinais observaveis:

- etapas claras;
- WIP entendido;
- filas visiveis;
- bloqueios tratados;
- demandas nao ficam paradas sem explicacao;
- gargalos sao identificados por dados e conversas.

Perguntas possiveis:

- O time consegue enxergar onde cada demanda esta no fluxo?
- O time sabe onde o trabalho costuma travar?
- Existem limites ou acordos para evitar excesso de demandas simultaneas?
- Bloqueios sao registrados e tratados?
- O fluxo representa a realidade ou apenas o processo ideal?

### Pilar 2 — Qualidade da demanda e refinamento

Pergunta central: o trabalho entra no fluxo com clareza suficiente para ser executado sem retrabalho evitavel?

Sinais observaveis:

- historia/demanda com objetivo claro;
- criterios de aceite compreensiveis;
- dependencias identificadas cedo;
- refinamento evita descoberta tardia;
- negocio e tecnologia compartilham entendimento.

Perguntas possiveis:

- As demandas chegam com contexto suficiente?
- Os criterios de aceite ajudam a testar e validar?
- As dependencias sao conhecidas antes da execucao?
- O time frequentemente precisa parar para redescobrir o objetivo da demanda?
- O backlog ajuda ou atrapalha a execucao?

### Pilar 3 — Execucao tecnica e entrega

Pergunta central: o time consegue transformar demanda em entrega com estabilidade e qualidade?

Sinais observaveis:

- desenvolvimento avanca sem excesso de interrupcao;
- homologacao recebe itens testaveis;
- deploy nao vira gargalo invisivel;
- retrabalho e defeitos sao tratados como sinal de sistema;
- cycle time e idade em status sao usados na gestao.

Perguntas possiveis:

- O time consegue concluir desenvolvimento com estabilidade?
- A passagem para homologacao e clara?
- Existe fila relevante entre pronto tecnico e producao?
- O deploy ocorre em cadencia adequada ao tipo de demanda?
- O time aprende com retrabalho, falhas e atrasos?

### Pilar 4 — Metricas e leitura operacional

Pergunta central: o time usa metricas para aprender e decidir, nao para justificar ou punir?

Metricas prioritarias no MAM:

- vazao / throughput;
- lead time;
- cycle time;
- tempo bloqueado;
- percentual ou volume de demandas bloqueadas;
- tipo de bloqueio;
- idade em status;
- deploy frequency quando houver dado confiavel;
- DORA quando fizer sentido e houver contexto tecnico suficiente.

Regra de prioridade visual: metricas de fluxo devem aparecer antes de DORA quando o objetivo for maturidade operacional por time.

Perguntas possiveis:

- O time entende as metricas usadas?
- As metricas ajudam a tomar decisoes reais?
- Os gargalos aparecem nos indicadores?
- O time separa lead time de cycle time corretamente?
- Bloqueios sao analisados por tipo e causa?

### Pilar 5 — Colaboracao, lideranca e comunicacao

Pergunta central: o time possui conversas, acordos e lideranca suficientes para resolver problemas de sistema?

Sinais observaveis:

- lider atua removendo impedimentos e alinhando contexto;
- time entende prioridades;
- comunicacao com negocio e areas dependentes e clara;
- riscos sao escalados cedo;
- decisoes ficam registradas;
- reunioes existem para melhorar fluxo, nao para teatro agil.

Perguntas possiveis:

- O lider ajuda o time a destravar o fluxo?
- Prioridades sao claras e estaveis o suficiente?
- Dependencias externas sao acompanhadas?
- Conversas importantes viram acordos visiveis?
- O time consegue falar sobre problemas sem medo?

### Pilar 6 — Melhoria continua e maturidade sistemica

Pergunta central: o time melhora o sistema de trabalho ou apenas reage aos problemas?

Sinais observaveis:

- retrospectivas geram acoes;
- acoes sao acompanhadas;
- problemas recorrentes sao tratados na causa;
- melhoria nao depende apenas de boa vontade;
- maturidade e vista como evolucao, nao como nota.

Perguntas possiveis:

- O time transforma aprendizados em mudancas reais?
- As mesmas causas de bloqueio se repetem sem tratamento?
- Existe plano de melhoria por ciclo?
- A maturidade e acompanhada ao longo do tempo?
- O time consegue distinguir sintomas de causas?

## Resultado esperado por time

Cada avaliacao trimestral deve produzir uma folha/resumo por time contendo:

- nome do time;
- periodo avaliado;
- tipo de time ou contexto operacional;
- notas por pilar com destaque visual claro;
- principais metricas de fluxo;
- vazao;
- lead time;
- cycle time;
- bloqueios;
- tipos de bloqueio;
- principais gargalos;
- leitura executiva;
- riscos;
- recomendacoes;
- proximas acoes.

## Visual esperado

Formato sugerido: A4 horizontal, uma folha por time.

Preferencias registradas:

- cores suaves, nao saturadas;
- paleta alinhada a Galapagos Capital quando possivel;
- avaliacoes por pilar devem ser evidentes;
- nome do time deve estar claro;
- metricas de fluxo devem vir antes de DORA;
- evitar dashboard bonito sem leitura executiva;
- cada avaliacao representa 3 meses.

## Regras de interpretacao

- Nota baixa em pilar nao significa baixa competencia individual.
- Gargalo em QA, homologacao ou deploy pode estar fora do controle direto do time.
- Lead time pode ficar artificialmente alto quando backlog e criado com muita antecedencia; nesses casos cycle time pode representar melhor execucao.
- Deploy frequency so deve ser usada se a data de deploy for confiavel ou se houver proxy declarado.
- MTTR e change failure rate podem nao fazer sentido se nao houver dados adequados.
- Metrica sem contexto pode induzir decisao errada.
- Comparar times diferentes exige muito cuidado.

---

# 4. METRICAS — MEMORIA CONSOLIDADA

## Metricas prioritarias para leitura de fluxo

- Vazao / throughput: quantidade de demandas concluidas em determinado periodo.
- Lead time: tempo total desde entrada/criacao relevante ate conclusao/entrega, dependendo da definicao adotada.
- Cycle time: tempo desde inicio real da execucao ate conclusao.
- Tempo bloqueado: tempo em que demanda ficou impedida.
- Demandas bloqueadas: volume ou percentual de demandas que tiveram bloqueio.
- Tipo de bloqueio: origem do impedimento, como negocio, infraestrutura, dependencia tecnica, ambiente, decisao, acesso ou refinamento.
- Idade em status: tempo acumulado em uma etapa especifica do fluxo.
- Deploy frequency: frequencia real de deploy, quando houver dado confiavel.

## Lead time vs cycle time

Lead time pode ser inadequado quando demandas sao criadas com muita antecedencia e ficam aguardando relevancia/priorizacao. Nesses casos, lead time mede tambem espera de backlog/upstream, nao apenas execucao.

Cycle time tende a ser melhor para analisar eficiencia de execucao, desde que o ponto de inicio esteja corretamente definido.

## Deploy frequency

Deploy frequency deve representar frequencia real de disponibilizacao em producao. Quando nao ha historico adequado, pode-se usar proxy, mas o proxy deve ser declarado.

Exemplo de proxy discutido: tempo entre resolved e closed pode indicar fila de deploy quando resolved representa pronto tecnico e closed representa efetiva disponibilizacao. Isso nao deve ser chamado de deploy frequency sem ressalva; pode ser melhor tratar como tempo em fila de deploy ou intervalo ate fechamento.

## DORA

DORA pode fazer sentido quando houver dados confiaveis de deploy, falhas, incidentes e recuperacao. Em times de baixa maturidade de dados ou quando nao existe historico tecnico confiavel, DORA deve ser usada com cautela.

No resultado do MAM, metricas de fluxo devem aparecer antes de DORA.

---

# 5. DIAGNOSTICOS DE INICIATIVAS PASSADAS — MEMORIA OPERACIONAL

## Intencao

Registrar memoria operacional sobre diagnosticos de iniciativas analisadas no contexto Galapagos, incluindo iniciativa de cadastro de device e uma segunda iniciativa ainda nao totalmente especificada.

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

## Iniciativa roubo de credenciais

Estado atual da memoria: o nome `roubo de credenciais` pode ser perguntado pelo usuario como iniciativa conhecida, mas o repositorio ainda nao contem dados factuais suficientes para responder resultado final.

Nao ha, nesta memoria, confirmacao de:

- percentual entregue;
- data de inicio;
- data de fim;
- quantidade de historias planejadas;
- quantidade de historias entregues;
- status final;
- principais problemas especificos;
- evidencia de go-live;
- documento de fechamento.

Resposta esperada quando perguntarem resultado da iniciativa roubo de credenciais:

- nao inventar;
- responder de forma executiva;
- dizer que a memoria atual nao contem resultado confirmado;
- explicar exatamente quais dados faltam;
- sugerir criar memoria especifica da iniciativa com status, datas, historias, percentual, problemas e evidencias.

Exemplo de resposta executiva aceitavel:

"Com base no Grimorio Galapagos atual, nao ha evidencia suficiente para afirmar o resultado final da iniciativa roubo de credenciais. Para uma resposta executiva completa, faltam percentual entregue, data de inicio, quantidade de historias planejadas e concluidas, status final, problemas principais e evidencia de conclusao ou go-live. A recomendacao e registrar uma memoria especifica da iniciativa antes de usar essa pergunta em contexto gerencial."

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

## Padroes consolidados de diagnostico

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

- "A eficiencia foi impactada por gargalos nas etapas finais do fluxo.";
- "O desenvolvimento demonstra capacidade de avancar, mas a conversao em entrega efetiva depende da reducao de filas posteriores.";
- "Os dados indicam necessidade de separar gargalos internos de dependencias externas.";
- "A proxima melhoria deve focar em reduzir espera, explicitar dependencias e melhorar previsibilidade de deploy/homologacao.".

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

---

# 6. PAPEIS E RESPONSABILIDADES — MEMORIA DISPONIVEL

Estado atual:

- existe estrutura para documentos de papeis e responsabilidades;
- existe README da pasta;
- ainda nao ha documento convertido completo de papeis e responsabilidades nesta memoria consolidada.

Uso esperado:

Consultar quando o pedido envolver:

- papel do Lider Tecnico;
- papel do time de desenvolvimento;
- papel de analise de negocio;
- papel de Scrum Master, PMO ou gestao de fluxo;
- responsabilidades em cerimonias;
- ownership e accountability por etapa.

Regra:

Documentos desta pasta devem apoiar alinhamento de expectativas, limites de atuacao e clareza de responsabilidades.

## Papel do lider no contexto Galapagos — leitura permitida a partir do MAM e fluxo

O lider no contexto Galapagos deve ser entendido como agente de clareza, fluxo, prioridade e remocao de impedimentos, nao apenas como cobrador de tarefas.

Responsabilidades esperadas:

- ajudar o time a destravar fluxo;
- tornar bloqueios visiveis;
- escalar dependencias externas quando necessario;
- conectar prioridade de negocio com capacidade real do time;
- usar metricas como instrumento de decisao e aprendizado;
- proteger a qualidade da conversa, nao esconder problemas;
- apoiar melhoria continua;
- evitar que maturidade vire ranking ou cobranca punitiva;
- separar problema sistemico de falha individual;
- garantir que riscos sejam comunicados cedo.

Mapa mental possivel para papel do lider:

- Lideranca operacional
  - clareza de prioridade
  - acompanhamento de fluxo
  - remocao de impedimentos
- Gestao de fluxo
  - WIP
  - gargalos
  - bloqueios
  - filas
- Metricas
  - vazao
  - lead time
  - cycle time
  - bloqueios
  - idade em status
- Comunicacao
  - negocio
  - tecnologia
  - areas dependentes
  - lideranca executiva
- Maturidade
  - melhoria continua
  - evidencias
  - plano de evolucao
  - seguranca psicologica
- Governanca
  - riscos
  - decisoes
  - acordos
  - limites

Limite:

Se o usuario pedir documento oficial completo de papeis e responsabilidades, responder que a estrutura existe, mas o documento detalhado ainda precisa ser convertido/adicionado.

---

# 7. ROTEIRO DE VALIDACAO PARA CLAUDE/GPT

## Testes MAM

Perguntas:

1. O que e o MAM Galapagos?
2. Quais pilares o MAM avalia?
3. Gere as perguntas do MAM por pilar.
4. Como aplicar o MAM trimestralmente por time?
5. Como interpretar resultado de maturidade sem transformar em ranking?
6. Monte uma leitura executiva de maturidade para um CTO.
7. Gere um modelo de resultado A4 horizontal por time para o MAM.
8. Quais metricas devem aparecer primeiro no resultado do MAM?
9. Explique por que vazao, lead time, cycle time e bloqueios sao importantes.
10. Quando DORA faz sentido e quando nao faz?

Sinais de resposta correta:

- menciona maturidade como mapa de evolucao, nao ranking;
- prioriza fluxo, vazao, lead time, cycle time, bloqueios e tipos de bloqueio;
- reconhece avaliacao trimestral;
- separa pilar, pergunta, evidencia e recomendacao;
- nao reduz maturidade a cerimonias ageis.

## Testes Diagnosticos

Perguntas:

1. O que existe de memoria sobre a iniciativa de cadastro de device?
2. O que pode ser afirmado com seguranca sobre os diagnosticos de iniciativas passadas?
3. Quais foram os gargalos recorrentes identificados nas analises passadas?
4. Como explicar para um gerente o impacto de QA/homologacao e deploy no fluxo?
5. Qual a diferenca entre conclusao tecnica e entrega efetiva em producao?
6. O que fazer quando lead time parece alto por causa de backlog criado muito antes?
7. Quais acoes recorrentes foram recomendadas para melhorar fluxo?
8. Qual foi o resultado da iniciativa roubo de credenciais?

Sinal esperado para pergunta 8:

- nao inventar resultado;
- dizer que `roubo de credenciais` ainda nao tem resultado confirmado;
- explicar o que falta: percentual entregue, data de inicio, historias, status final, evidencias;
- responder de forma executiva, nao apenas defensiva.

## Testes Papeis

Perguntas:

1. Qual e o papel do lider no contexto Galapagos?
2. Gere um mapa mental do papel do lider no fluxo de trabalho.
3. Explique a diferenca entre lideranca operacional, facilitacao e gestao de fluxo.
4. Como o lider deve atuar diante de bloqueios recorrentes?
5. Como o lider deve usar metricas sem transformar isso em cobranca punitiva?
6. Quais responsabilidades precisam ficar claras entre time, lider, negocio e areas dependentes?
7. Crie uma versao executiva sobre papel do lider para apresentacao.

Sinais de resposta correta:

- conecta lideranca com fluxo, bloqueios, clareza, prioridades, dependencia e melhoria continua;
- nao reduz lider a cobrador de tarefa;
- se faltar documento detalhado convertido, declara limite e usa documentacao base como apoio.

## Testes Documentacao Convertida

Perguntas:

1. Que tipos de documentos convertidos existem no Grimorio Galapagos?
2. Onde procurar documentos sobre refinamento?
3. Onde procurar documentos sobre papeis e responsabilidades?
4. Onde procurar diagnosticos?
5. O que significa um documento estar em `99_revisar_antes_de_publicar`?
6. O que ainda esta pendente de conversao?
7. Como decidir se um documento convertido pode virar fonte oficial?

Sinais de resposta correta:

- reconhece a estrutura de documentos convertidos;
- diferencia documento oficial, memoria operacional, rascunho e material pendente de revisao;
- nao assume que todos os pacotes previstos ja existem com conteudo completo.

---

# 8. PROMPTS SUGERIDOS PARA TESTE NO CLAUDE

## Prompt base

Consulte o arquivo Galapagos consolidado. Responda usando o Grimorio Galapagos. Nao copie literalmente trechos de MEMORIA_IA; transforme em linguagem humana. Separe fato, memoria, limite, interpretacao e recomendacao quando houver risco de confusao.

## Prompt MAM

Explique o que e o MAM Galapagos, quais pilares ele avalia, como deve ser aplicado trimestralmente por time e quais metricas devem aparecer primeiro no resultado. Responda em linguagem executiva para gerente/CTO.

## Prompt Diagnostico

O que existe de memoria sobre os diagnosticos de iniciativas passadas no Galapagos? Explique os principais gargalos recorrentes, limites dos dados e proximas acoes recomendadas.

## Prompt Roubo de Credenciais

Qual foi o resultado da iniciativa roubo de credenciais? Responda de forma executiva. Se nao houver dados suficientes, explique exatamente o que falta para responder percentual entregue, data de inicio, quantidade de historias, status final e principais problemas.

## Prompt Papeis

Qual e o papel do lider no contexto Galapagos? Gere uma leitura executiva e depois um mapa mental textual do papel do lider no fluxo de trabalho, metricas, bloqueios, comunicacao e maturidade.

---

# 9. CRITERIO DE DIAGNOSTICO DO TESTE

Se Claude/GPT responder incompleto sobre MAM, problema provavel: nao leu o trecho consolidado ou ignorou a rota MAM.

Se responder que nao pode falar nada sobre diagnosticos, problema provavel: ignorou a memoria de diagnosticos. Resposta correta deve dizer que ha memoria operacional, mas faltam dados finais completos.

Se inventar resultado de roubo de credenciais, problema grave: alucinacao.

Se disser que roubo de credenciais nao tem dados suficientes e explicar o que falta, comportamento correto.

Se responder sobre papeis com muita certeza documental, problema: a base de papeis ainda e limitada. Resposta correta deve usar MAM/fluxo como apoio e declarar que o documento detalhado de papeis ainda nao foi convertido.
