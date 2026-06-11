# Rotas de Consulta — Grimorio Versao Galapagos

Este arquivo orienta quais partes do Grimorio consultar conforme o tipo de pedido.

## Regra de entrada

Para qualquer pedido sobre Galapagos:

1. Ler `00_LEIA_PRIMEIRO.md`.
2. Verificar limites de acesso e uso.
3. Consultar `01_INDICE.md` para localizar a informacao.
4. Seguir a rota adequada abaixo.
5. Separar fato, hipotese, interpretacao e recomendacao.

## Rota 1 — Explicar o modelo operacional

Quando usar:

- explicar como a area trabalha;
- explicar fluxo de trabalho;
- explicar upstream/downstream;
- explicar boards;
- explicar hierarquia de demandas.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `01_documentacao_base/modelo_operacional_tecnologia.md`
3. `01_documentacao_base/artefatos_hierarquia_trabalho.md`
4. `01_documentacao_base/fluxos_de_trabalho_e_boards.md`
5. `01_documentacao_base/campos_politicas_dor_dod.md`

Saida esperada:

- explicacao clara;
- sem excesso de teoria;
- conectada ao contexto Galapagos.

## Rota 2 — Analisar um time

Quando usar:

- status de um time;
- leitura de maturidade;
- riscos do time;
- plano de melhoria;
- leitura de indicadores.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `04_times/README.md`
3. `04_times/modelo_time/perfil_do_time.md`
4. `04_times/modelo_time/fluxo_local.md`
5. `04_times/modelo_time/metricas_observadas.md`
6. `04_times/modelo_time/anotacoes.md`
7. `04_times/modelo_time/maturidade.md`
8. `04_times/modelo_time/riscos.md`
9. `04_times/modelo_time/plano_de_melhoria.md`
10. `07_entregaveis/mam_galapagos_v1_memoria_ia.md`, se a analise envolver maturidade, MAM, avaliacao por pilar ou evolucao trimestral

Saida esperada:

- leitura objetiva;
- evidencias usadas;
- pontos de atencao;
- recomendacoes;
- proximos passos.

## Rota 3 — Ler metricas ou indicadores

Quando usar:

- explicar uma metrica;
- interpretar dashboards;
- analisar fluxo;
- analisar previsibilidade;
- analisar qualidade ou estabilidade operacional.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `05_metricas_e_dados/metricas_principios_e_camadas.md`
3. `05_metricas_e_dados/catalogo_metricas_operacionais.md`
4. `05_metricas_e_dados/memoria_bases_azure_emulado_2026-06-11.md`, quando a pergunta envolver CSVs, Azure emulado, lead time, cycle time, throughput, bloqueios ou status por time
5. `07_entregaveis/mam_galapagos_v1_memoria_ia.md`, quando a pergunta envolver metricas dentro do MAM ou avaliacao de maturidade
6. `06_evidencias/README.md`, se houver evidencia fornecida
7. `06_evidencias/dashboards/README.md`, se o material vier de painel

Saida esperada:

- definicao da metrica;
- fonte ou recorte usado;
- interpretacao;
- limites;
- recomendacao.

## Rota 4 — Criar status report

Quando usar:

- status de iniciativa;
- status de frente de trabalho;
- atualizacao executiva;
- resumo para lideranca.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `07_entregaveis/status_report.md`
3. `08_comunicacao/README.md`
4. `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_regulatorias_validado_2026-06-11.md`, quando a pergunta envolver iniciativas regulatorias
5. `11_documentos_convertidos/05_diagnosticos/fontes_diagnostico_iniciativas_regulatorias_2026-06-11.md`, quando houver necessidade de hierarquia entre CSV, PPT, ODT e memoria operacional
6. `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_passadas_memoria_ia.md`, quando a pergunta envolver iniciativas passadas, cadastro de device ou diagnostico de projeto
7. Documentacao ou evidencias relacionadas ao tema

Saida esperada:

- contexto;
- status atual;
- avancos;
- pendencias;
- riscos;
- proximas acoes.

## Rota 5 — Criar relatorio periodico

Quando usar:

- fechamento de ciclo;
- leitura de periodo;
- resumo de evolucao;
- acompanhamento de time ou frente.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `07_entregaveis/relatorio_periodico.md`
3. `05_metricas_e_dados/`
4. `04_times/`, se for especifico de time
5. `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_regulatorias_validado_2026-06-11.md`, se o relatorio envolver iniciativas regulatorias
6. `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_passadas_memoria_ia.md`, se o relatorio envolver iniciativas passadas ou diagnosticos reconstruidos
7. `08_comunicacao/README.md`

Saida esperada:

- resumo;
- resultado;
- destaques;
- atencoes;
- recomendacoes;
- proximos passos.

## Rota 6 — Criar roadmap

Quando usar:

- organizar entregas;
- planejar marcos;
- explicar sequenciamento;
- mostrar evolucao esperada.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `07_entregaveis/roadmap.md`
3. `01_documentacao_base/`
4. `11_documentos_convertidos/04_roadmap_planejamento/`, quando houver documento convertido aplicavel
5. Evidencias ou materiais fornecidos pelo usuario

Saida esperada:

- objetivo;
- horizonte;
- marcos;
- dependencias;
- riscos;
- proximos passos.

## Rota 7 — Avaliar maturidade / MAM

Quando usar:

- diagnostico de maturidade;
- MAM;
- Modelo de Avaliacao de Maturidade Agil Galapagos;
- perguntas de maturidade;
- avaliacao por pilar;
- avaliacao trimestral;
- visual de resultado por time;
- plano de desenvolvimento de time.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `07_entregaveis/mam_galapagos_modelo_validado_2026-06-11.md`, como fonte principal validada
3. `07_entregaveis/mam_galapagos_v1_memoria_ia.md`, como memoria operacional anterior
4. `04_times/modelo_time/maturidade.md`
5. `07_entregaveis/diagnostico_de_maturidade.md`
6. `04_times/modelo_time/anotacoes.md`
7. `05_metricas_e_dados/metricas_principios_e_camadas.md`
8. `05_metricas_e_dados/catalogo_metricas_operacionais.md`
9. `11_documentos_convertidos/05_diagnosticos/`, quando houver diagnostico convertido aplicavel
10. Evidencias disponiveis

Saida esperada:

- dimensoes avaliadas;
- perguntas ou criterios, quando solicitados;
- evidencias;
- leitura atual;
- metricas prioritarias de fluxo;
- riscos;
- recomendacoes;
- proximos passos;
- aviso de que maturidade deve ser mapa de evolucao, nao ranking.

Regra especifica:

- Para MAM, usar `mam_galapagos_modelo_validado_2026-06-11.md` quando houver divergencia de pilares, escala ou estrutura.
- Para apresentacoes e relatorios, reescrever em linguagem executiva natural.

## Rota 8 — Trabalhar com evidencias

Quando usar:

- analisar imagem;
- analisar dashboard;
- analisar material de apoio;
- usar documento pontual como base.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `06_evidencias/README.md`
3. Subpasta correspondente ao tipo de material
4. Pasta de metricas, times ou entregaveis conforme a pergunta
5. `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_regulatorias_validado_2026-06-11.md`, se a evidencia estiver relacionada a diagnosticos regulatorios
6. `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_passadas_memoria_ia.md`, se a evidencia estiver relacionada a diagnosticos passados

Saida esperada:

- descricao da evidencia;
- leitura;
- limites;
- possiveis conclusoes;
- proximos passos.

## Rota 9 — Governanca, acesso e limites

Quando usar:

- duvida sobre uso de dados;
- uso com IA externa;
- uso com GPT corporativo;
- publicacao no Git;
- materiais sensiveis;
- uso de conectores;
- acesso a Azure, repositorios, documentos, codigo ou reunioes.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `09_governanca_compliance/README.md`
3. `AVISO_DE_PROPRIEDADE.md`
4. `10_historico_aprendizados/2026-06-11_visao_chegada_grimorio_contexto_vivo.md`, quando a pergunta envolver conectores, acesso a fontes reais ou evolucao futura
5. `11_documentos_convertidos/99_revisar_antes_de_publicar/`, quando o tema envolver documentos ainda nao revisados

Saida esperada:

- recomendacao prudente;
- limites claros;
- separacao entre publico, privado e corporativo;
- diferenciar visao estrategica de compromisso de MVP.

## Rota 10 — Consultar documentos convertidos

Quando usar:

- consultar um documento que veio de Word, PDF, apresentacao ou material consolidado;
- resumir documento convertido;
- comparar documento convertido com modelo operacional;
- usar documento convertido como fonte de contexto;
- decidir para qual pasta um documento convertido deve ir.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `11_documentos_convertidos/README.md`
3. Subpasta correspondente ao tema:
   - `01_refinamento/`
   - `02_papeis_responsabilidades/`
   - `03_transformacao_agil/`
   - `04_roadmap_planejamento/`
   - `05_diagnosticos/`
   - `06_processos_politicas/`
   - `99_revisar_antes_de_publicar/`
4. `09_governanca_compliance/README.md`, se houver risco de sensibilidade.

Saida esperada:

- origem do documento;
- resumo ou leitura;
- relacao com o Grimorio;
- limites de uso;
- indicacao se pode virar fonte oficial.

## Rota 12 — Diagnosticar iniciativas passadas

Quando usar:

- pergunta sobre diagnosticos feitos anteriormente;
- projeto de cadastro de device;
- segunda iniciativa pendente de levantamento;
- relatorio grafico e textual de iniciativa;
- recuperacao de conclusoes, gargalos ou acoes discutidas em conversas anteriores.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_regulatorias_validado_2026-06-11.md`, quando envolver Roubo de Credenciais ou Monitoramento de Atipicidades
3. `11_documentos_convertidos/05_diagnosticos/fontes_diagnostico_iniciativas_regulatorias_2026-06-11.md`, para definir hierarquia de fontes
4. `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_passadas_memoria_ia.md`
5. `07_entregaveis/relatorio_periodico.md`
6. `07_entregaveis/status_report.md`
7. `05_metricas_e_dados/metricas_principios_e_camadas.md`
8. `05_metricas_e_dados/catalogo_metricas_operacionais.md`
9. `05_metricas_e_dados/memoria_bases_azure_emulado_2026-06-11.md`, quando a pergunta exigir dados operacionais
10. Evidencias, prints, CSVs ou documentos fornecidos pelo usuario

Saida esperada:

- deixar claro o que e memoria reconstruida e o que e dado confirmado;
- separar evidencia, interpretacao, hipotese, risco e recomendacao;
- nao inventar numeros;
- reconstruir relatorio humano apenas quando houver pedido explicito;
- indicar limites quando os dados originais nao estiverem presentes.

## Rota 13 — Validar uso em GPT corporativo, Claude ou IA externa

Quando usar:

- testar se o Grimorio funciona em outra IA;
- preparar perguntas de validacao;
- comparar resposta de GPT/Claude com a memoria do repositorio;
- diagnosticar se uma resposta falhou por falta de dado, falta de rota ou comportamento do modelo;
- validar MAM, papeis, documentacao passada ou diagnosticos.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `01_INDICE.md`
3. `02_ROTAS.md`
4. `PATCH_LOG.md`
5. `10_historico_aprendizados/2026-06-11_roteiro_validacao_gpt_claude_memoria_ia.md`
6. Arquivos especificos da area testada:
   - MAM: `07_entregaveis/mam_galapagos_modelo_validado_2026-06-11.md`
   - Diagnosticos: `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_regulatorias_validado_2026-06-11.md`
   - Metricas e dados: `05_metricas_e_dados/memoria_bases_azure_emulado_2026-06-11.md`
   - Papeis: `11_documentos_convertidos/02_papeis_responsabilidades/README.md` e documentacao base
   - Documentacao convertida: `11_documentos_convertidos/README.md`
   - Visao de chegada: `10_historico_aprendizados/2026-06-11_visao_chegada_grimorio_contexto_vivo.md`

Saida esperada:

- roteiro de perguntas;
- criterio de avaliacao;
- resposta esperada ou sinais de resposta correta;
- identificacao de lacuna;
- recomendacao de patch quando necessario.

## Rota 14 — Visao de chegada do Grimorio / contexto vivo conectado

Quando usar:

- discutir futuro do Grimorio;
- explicar para onde o Grimorio deve evoluir;
- falar de memoria viva;
- conectar reunioes, Azure, Kiro, documentos, produto, codigo, repositorios, skills ou agentes;
- diferenciar visao estrategica de MVP;
- preparar conversa com CTO, gerente ou lideranca sobre conectores;
- discutir viabilidade, governanca e proximos passos para evolucao.

Consultar:

1. `00_LEIA_PRIMEIRO.md`
2. `01_INDICE.md`
3. `09_governanca_compliance/README.md`, quando envolver acesso, permissao ou dados sensiveis
4. `10_historico_aprendizados/2026-06-11_visao_chegada_grimorio_contexto_vivo.md`
5. `05_metricas_e_dados/memoria_bases_azure_emulado_2026-06-11.md`, quando a visao envolver Azure e metricas
6. Documentos ou evidencias relacionados ao conector/fonte discutida

Saida esperada:

- deixar claro que e visao de chegada, nao escopo fechado de MVP;
- explicar valor esperado;
- separar capacidade desejada de capacidade ja existente;
- apontar dependencias de governanca, conectores, permissoes e fontes oficiais;
- propor evolucao incremental;
- evitar prometer automacao total imediata.

## Rota 11 — Atualizar o Grimorio

Quando usar:

- adicionar novo documento;
- criar novo modelo;
- ajustar estrutura;
- registrar aprendizado.

Consultar:

1. `PATCH_LOG.md`
2. `01_INDICE.md`
3. `02_ROTAS.md`
4. `10_historico_aprendizados/README.md`
5. `11_documentos_convertidos/README.md`, se a atualizacao envolver documentos convertidos

Saida esperada:

- arquivo correto;
- pasta correta;
- classificacao de sensibilidade;
- atualizacao do patch log;
- ajuste do indice/rotas quando necessario.

Regra chave:

Sempre que novo conteudo relevante for adicionado ao Grimorio, verificar se `01_INDICE.md`, `02_ROTAS.md` e `PATCH_LOG.md` precisam ser atualizados. Se o conteudo criar uma nova forma de consulta, atualizar rotas. Se apenas adicionar material dentro de rota existente, atualizar indice e patch log.
