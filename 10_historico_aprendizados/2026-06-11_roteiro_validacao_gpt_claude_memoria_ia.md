# ROTEIRO DE VALIDACAO GPT/CLOUDE — MEMORIA_IA

status: roteiro_teste_memoria
classe: validacao_grimorio_galapagos_em_ia_corporativa_ou_externa
data: 2026-06-11
uso: testar_se_modelo_consulta_rotas_e_memorias_corretas
nao_usar_como: documento_final_humano

## Objetivo

Orientar testes no GPT corporativo, Claude ou outra IA usando o pacote/repositorio Galapagos. Este roteiro ajuda a validar se a IA consegue localizar e aplicar informacoes existentes, reconhecer limites e nao inventar dados quando a memoria ainda nao contem detalhes factuais.

## Regra de avaliacao do teste

Uma resposta boa deve:

- consultar ou refletir as rotas corretas;
- citar ou mencionar os arquivos conceitualmente usados quando solicitado;
- separar dado confirmado de memoria reconstruida;
- transformar linguagem de IA em linguagem humana quando o pedido for executivo;
- nao copiar literalmente arquivos `memoria_ia`;
- nao inventar resultado, percentual, data, quantidade ou status quando nao existir evidencia;
- sinalizar lacunas com clareza;
- oferecer caminho de complementacao quando faltar dado.

Uma resposta ruim tende a:

- responder genericamente sem conectar ao Grimorio;
- tratar memoria operacional como relatorio final;
- inventar status de iniciativa;
- usar MAM como ranking;
- ignorar indice/rotas;
- dizer que nao ha nada quando existe memoria conceitual relevante;
- dar resposta longa, defensiva e pouco executiva quando o usuario pede leitura para gerente/CTO.

## Arquivos de entrada obrigatoria nos testes

Para qualquer teste, a IA deve considerar:

1. `00_LEIA_PRIMEIRO.md`
2. `README.md`
3. `01_INDICE.md`
4. `02_ROTAS.md`
5. `PATCH_LOG.md`

Depois deve usar a rota correspondente.

## Area 1 — Testes do MAM Galapagos

Arquivos esperados:

- `07_entregaveis/mam_galapagos_v1_memoria_ia.md`
- `07_entregaveis/diagnostico_de_maturidade.md`
- `04_times/modelo_time/maturidade.md`
- `05_metricas_e_dados/metricas_principios_e_camadas.md`
- `05_metricas_e_dados/catalogo_metricas_operacionais.md`

Perguntas de teste:

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

## Area 2 — Testes de diagnosticos de iniciativas passadas

Arquivos esperados:

- `11_documentos_convertidos/05_diagnosticos/diagnostico_iniciativas_passadas_memoria_ia.md`
- `07_entregaveis/status_report.md`
- `07_entregaveis/relatorio_periodico.md`
- `05_metricas_e_dados/metricas_principios_e_camadas.md`
- `05_metricas_e_dados/catalogo_metricas_operacionais.md`

Perguntas de teste:

1. O que existe de memoria sobre a iniciativa de cadastro de device?
2. O que pode ser afirmado com seguranca sobre os diagnosticos de iniciativas passadas?
3. Quais foram os gargalos recorrentes identificados nas analises passadas?
4. Como explicar para um gerente o impacto de QA/homologacao e deploy no fluxo?
5. Qual a diferenca entre conclusao tecnica e entrega efetiva em producao?
6. O que fazer quando lead time parece alto por causa de backlog criado muito antes?
7. Quais acoes recorrentes foram recomendadas para melhorar fluxo?
8. Qual foi o resultado da iniciativa roubo de credenciais?

Sinal esperado para pergunta 8:

- A resposta nao deve inventar resultado.
- A resposta deve dizer que o nome `roubo de credenciais` ainda nao esta registrado como iniciativa com resultado confirmado.
- A resposta pode levantar a hipotese de que seja uma iniciativa nao nomeada anteriormente, mas deve deixar claro que falta evidencia.
- A resposta ideal deve dizer que para responder percentual entregue, data de inicio, historias e status final e necessario adicionar memoria especifica da iniciativa.

## Area 3 — Testes de papeis e responsabilidades

Arquivos esperados:

- `11_documentos_convertidos/02_papeis_responsabilidades/README.md`
- `01_documentacao_base/modelo_operacional_tecnologia.md`
- `01_documentacao_base/artefatos_hierarquia_trabalho.md`
- `01_documentacao_base/fluxos_de_trabalho_e_boards.md`
- `08_comunicacao/README.md`

Perguntas de teste:

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
- nao inventa documento completo de papeis se a base estiver apenas estrutural;
- se faltar documento detalhado convertido, declara limite e usa documentacao base como apoio.

## Area 4 — Testes de documentacao passada / documentos convertidos

Arquivos esperados:

- `11_documentos_convertidos/README.md`
- subpastas de `11_documentos_convertidos/`
- `PATCH_LOG.md`
- `01_INDICE.md`
- `02_ROTAS.md`

Perguntas de teste:

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
- menciona que materiais sensiveis ou nao revisados devem permanecer em area apropriada;
- nao assume que todos os pacotes convertidos ja existem com conteudo completo.

## Area 5 — Testes de comportamento executivo

Perguntas de teste:

1. Resuma o MAM para um CTO em 5 bullets.
2. Explique o diagnostico de uma iniciativa com foco em decisao executiva.
3. Transforme a memoria IA em texto humano sem copiar literalmente.
4. Separe fato, limite, interpretacao e recomendacao sobre uma iniciativa sem dados completos.
5. Gere uma resposta curta para gerente quando nao ha dado suficiente.

Sinais de resposta correta:

- linguagem clara;
- resposta util;
- nao defensiva demais;
- nao inventa;
- oferece proximo passo objetivo;
- contextualiza impacto na eficiencia, fluxo e governanca.

## Resultado esperado do ciclo de testes

Ao testar no Claude/GPT corporativo, registrar:

- pergunta feita;
- resposta obtida;
- se encontrou a rota correta;
- se inventou informacao;
- se foi util para gestor;
- lacunas percebidas;
- necessidade de novo patch.

## Lacunas conhecidas antes do teste

- Ainda nao existe arquivo especifico com resultado factual da iniciativa `roubo de credenciais`.
- Ainda nao existe registro completo com percentual entregue, data de inicio, quantidade de historias e status final dessa iniciativa.
- Papeis e responsabilidades podem estar apenas estruturados em pasta, mas nao necessariamente convertidos em documento completo.
- Diagnosticos passados foram reconstruidos como memoria operacional, nao como relatorio final com dados.

## Proximo patch provavel

Criar um arquivo por iniciativa relevante, com campos:

- nome;
- aliases;
- contexto;
- data de inicio;
- periodo analisado;
- historias planejadas;
- historias entregues;
- percentual entregue;
- status final;
- principais problemas;
- gargalos;
- riscos;
- resultado executivo;
- evidencia usada;
- limites.
