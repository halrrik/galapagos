# Grimório — Versão Galápagos

Esta pasta organiza a aplicação do método Grimório ao contexto Galápagos.

A Versão Galápagos é um piloto assistido para apoiar documentação operacional, análise de métricas, diagnóstico de times, geração de relatórios executivos, planos de melhoria e acompanhamento de maturidade.

## Entrada recomendada

Para usar esta aplicação, comece por:

1. `00_LEIA_PRIMEIRO.md` — regras iniciais, limites e ordem de consulta.
2. `01_INDICE.md` — mapa das pastas e arquivos da aplicação.
3. `02_ROTAS.md` — rotas de consulta por tipo de pedido.
4. `PATCH_LOG.md` — histórico de mudanças e pendências.

## Princípio central

O Grimório — Versão Galápagos não substitui sistemas corporativos como Azure DevOps, Power BI, Confluence, Box, SharePoint ou ferramentas internas.

Ele funciona como uma camada de contexto, interpretação, regras e comunicação para transformar informações autorizadas em análises e entregáveis úteis.

## Objetivo do piloto

Criar uma base estruturada para que pessoas e agentes de IA possam consultar:

- documentação operacional;
- fluxos de trabalho;
- adaptações locais de práticas ágeis e gestão de projetos;
- métricas e indicadores;
- evidências fornecidas;
- anotações qualificadas por time;
- diagnósticos;
- planos de melhoria;
- padrões de comunicação executiva.

## Princípios de uso

1. Guardar contexto, regras e interpretação; não massa bruta de dados.
2. Manter dados sensíveis, volumosos ou dinâmicos fora do repositório.
3. Tratar prints, exports e dashboards como snapshots datados.
4. Separar fato, hipótese, interpretação e recomendação.
5. Não assumir acesso a sistemas externos sem autorização explícita.
6. Respeitar segurança, confidencialidade, compliance e limites corporativos.
7. Preservar a diferença entre método Grimório e aplicação específica Galápagos.

## Estado atual

Versão conceitual para piloto assistido, com estrutura operacional inicial e primeiro pacote de documentação convertido.

Ainda não contém dados internos, métricas reais dos times, documentos confidenciais completos ou integrações automáticas.

## Estrutura desta aplicação

```text
01_aplicacoes/galapagos/
  README.md
  00_LEIA_PRIMEIRO.md
  01_INDICE.md
  02_ROTAS.md
  PATCH_LOG.md
  AVISO_DE_PROPRIEDADE.md
  01_documentacao_base/
  02_base_conceitual/
  03_de_para_galapagos/
  04_times/
  05_metricas_e_dados/
  06_evidencias/
  07_entregaveis/
  08_comunicacao/
  09_governanca_compliance/
  10_historico_aprendizados/
  99_trabalho/
```

## Uso esperado no piloto

1. Consultar documentação e contexto.
2. Inserir anotações qualificadas por time.
3. Analisar prints, recortes e evidências autorizadas.
4. Gerar diagnósticos, relatórios e planos de melhoria.
5. Registrar aprendizados no `PATCH_LOG.md` e em `10_historico_aprendizados/`.
6. Atualizar `01_INDICE.md` e `02_ROTAS.md` sempre que a estrutura mudar.
