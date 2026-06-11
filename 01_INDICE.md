# Indice — Grimorio Versao Galapagos

Este indice mostra onde procurar cada tipo de informacao dentro da aplicacao Galapagos.

## Entrada obrigatoria

- `00_LEIA_PRIMEIRO.md` — regras iniciais de uso, limites, ordem de consulta e criterios de resposta.
- `README.md` — visao geral da aplicacao Galapagos.
- `PATCH_LOG.md` — historico de mudancas, decisoes e pendencias.
- `AVISO_DE_PROPRIEDADE.md` — separacao entre metodo Grimorio, aplicacao Galapagos e materiais internos.

## Documentacao base

Pasta: `01_documentacao_base/`

Uso: entender o modelo operacional, fluxo de trabalho, hierarquia, politicas, campos e criterios de prontidao/conclusao.

Arquivos principais:

- `modelo_operacional_tecnologia.md`
- `artefatos_hierarquia_trabalho.md`
- `fluxos_de_trabalho_e_boards.md`
- `campos_politicas_dor_dod.md`

## Base conceitual

Pasta: `02_base_conceitual/`

Uso: guardar conceitos gerais usados como referencia. A aplicacao local deve sempre passar pelo de/para Galapagos antes de usar conceitos de forma direta.

## De/Para Galapagos

Pasta: `03_de_para_galapagos/`

Uso: explicar como conceitos de mercado, agilidade, gestao, fluxo e metricas sao adaptados ao contexto Galapagos.

## Times

Pasta: `04_times/`

Uso: registrar contexto, fluxo local, indicadores, anotacoes, maturidade, riscos e planos por time.

Modelo atual:

- `modelo_time/perfil_do_time.md`
- `modelo_time/fluxo_local.md`
- `modelo_time/metricas_observadas.md`
- `modelo_time/anotacoes.md`
- `modelo_time/maturidade.md`
- `modelo_time/riscos.md`
- `modelo_time/plano_de_melhoria.md`

## Metricas e dados

Pasta: `05_metricas_e_dados/`

Uso: consultar principios de metricas, catalogo operacional, qualidade dos dados e regras de interpretacao.

Arquivos principais:

- `metricas_principios_e_camadas.md`
- `catalogo_metricas_operacionais.md`

## Evidencias

Pasta: `06_evidencias/`

Uso: organizar materiais de apoio como dashboards, registros pontuais, documentos e recortes. Evidencias representam um momento e precisam de contexto.

Arquivos atuais:

- `README.md`
- `dashboards/README.md`

## Entregaveis

Pasta: `07_entregaveis/`

Uso: modelos para transformar contexto e evidencias em entregas reutilizaveis.

Arquivos atuais:

- `README.md`
- `relatorio_periodico.md`
- `status_report.md`
- `roadmap.md`
- `diagnostico_de_maturidade.md`
- `mam_galapagos_v1_memoria_ia.md` — memoria operacional do Modelo de Avaliacao de Maturidade Agil Galapagos. Usar como base de interpretacao, nao como texto final publicavel.

## Comunicacao

Pasta: `08_comunicacao/`

Uso: linguagem, narrativa, tom executivo, termos a usar/evitar e identidade comunicacional.

## Governanca e compliance

Pasta: `09_governanca_compliance/`

Uso: limites de uso, dados permitidos/restritos, acesso, seguranca, anonimizacao e uso com IA externa/corporativa.

## Historico e aprendizados

Pasta: `10_historico_aprendizados/`

Uso: registrar decisoes, aprendizados, problemas recorrentes, backlog do Grimorio e evolucao do modelo.

Arquivos atuais de memoria operacional:

- `2026-06-11_mam_e_diagnosticos_memoria_ia.md` — registro de controle da memoria reconstruida sobre MAM e diagnosticos de iniciativas passadas.
- `2026-06-11_roteiro_validacao_gpt_claude_memoria_ia.md` — roteiro de validacao para testar MAM, diagnosticos, papeis, documentos convertidos e comportamento executivo em GPT corporativo, Claude ou outra IA.

## Documentos convertidos

Pasta: `11_documentos_convertidos/`

Uso: organizar documentos originalmente recebidos em Word, PDF, apresentacoes ou materiais consolidados, convertidos para Markdown e preparados para consulta pelo Grimorio.

Subpastas atuais:

- `01_refinamento/`
- `02_papeis_responsabilidades/`
- `03_transformacao_agil/`
- `04_roadmap_planejamento/`
- `05_diagnosticos/`
- `06_processos_politicas/`
- `99_revisar_antes_de_publicar/`

Arquivos atuais em diagnosticos:

- `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_passadas_memoria_ia.md` — memoria operacional reconstruida sobre diagnosticos de iniciativas passadas, incluindo cadastro de device e segunda iniciativa pendente de levantamento.

Regra: documentos convertidos devem indicar origem, data de conversao e status de revisao. Materiais sensiveis ou ainda nao revisados devem permanecer em `99_revisar_antes_de_publicar/`.

## Roteiros de validacao

Usar `10_historico_aprendizados/2026-06-11_roteiro_validacao_gpt_claude_memoria_ia.md` quando o objetivo for testar se uma IA externa ou corporativa esta consultando o Grimorio corretamente.

Esse roteiro cobre perguntas sobre:

- MAM Galapagos;
- diagnosticos de iniciativas passadas;
- papeis e responsabilidades;
- documentacao convertida/passada;
- respostas executivas para gerente ou CTO;
- limites quando faltarem dados factuais.

## Area de trabalho

Pasta: `99_trabalho/`

Uso: guardar rascunhos e materiais ainda em preparacao. Nada nesta pasta deve ser tratado como versao oficial.

## Regra geral

Quando a pergunta envolver Galapagos, consultar primeiro `00_LEIA_PRIMEIRO.md`, depois usar este indice e `02_ROTAS.md` para escolher os arquivos corretos.

Quando a pergunta envolver MAM, maturidade, avaliacao trimestral, perguntas por pilar, visual de resultado por time ou diagnostico de iniciativas passadas, consultar tambem os arquivos de memoria operacional adicionados em 2026-06-11. Esses arquivos sao base para interpretacao por IA e nao devem ser copiados literalmente em comunicacoes humanas.

Quando a pergunta envolver validacao em GPT corporativo, Claude ou outra IA, usar o roteiro de validacao para diferenciar problema de conteudo, problema de rota e problema de comportamento do modelo.