# Patch Log — Grimório Versão Galápagos

Registro de evolução da aplicação Galápagos do método Grimório.

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
