# MAM GALAPAGOS V1 — MEMORIA_IA

status: modelo_reconstruido_para_memoria
classe: modelo_avaliacao_maturidade_agil_galapagos
uso: orientar_analise_de_maturidade_por_time_area_ou_frente
nao_usar_como: questionario_final_publicavel_sem_reescrita

## Intencao do modelo

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

Evitar: workshop onde pessoas se sintam pressionadas a responder de forma politicamente segura.

## Principios de avaliacao

- avaliar evidencia, nao percepcao solta;
- usar metricas como contexto, nao como sentenca;
- interpretar respostas com dados de fluxo;
- considerar tipo de time: projeto, sustentacao, automacao, plataforma, system team ou hibrido;
- distinguir problema do time de problema sistemico;
- observar gargalos fora do time quando impactarem eficiencia;
- evitar maturidade cosmetica baseada em cerimorias;
- preferir sinais de fluxo real, qualidade e decisao.

## Escala sugerida

Escala de 1 a 5 por item ou pilar.

1 = inexistente ou ad hoc. Pratica depende de esforco individual, nao ha previsibilidade, evidencias sao fracas.
2 = inicial. Existem praticas pontuais, mas inconsistentes, reativas ou pouco conectadas ao fluxo.
3 = em consolidacao. Praticas existem, sao reconhecidas pelo time e geram alguma previsibilidade, mas ainda ha fragilidade.
4 = consistente. Praticas estao integradas ao trabalho, sustentam decisoes e reduzem desperdicio.
5 = evolutivo. Time usa dados, aprendizado e feedback para melhorar continuamente o sistema de trabalho.

Regra: nota sem evidencia deve ser tratada como percepcao, nao como avaliacao fechada.

## Pilares do MAM

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

Metricas prioritarias no contexto MAM:

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

## Linguagem para saidas humanas

Quando solicitado a produzir relatorio ou apresentacao, transformar esta memoria em linguagem executiva, clara e natural. Nao usar termos como MEMORIA_IA, status, classe, regra interna ou estrutura operacional, salvo se o usuario pedir explicitamente.