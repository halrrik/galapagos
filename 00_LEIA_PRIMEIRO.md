# 00 — Leia Primeiro

Este arquivo define como o **Grimório — Versão Galápagos** deve ser utilizado.

Antes de responder qualquer pedido relacionado ao contexto Galápagos, a IA ou pessoa usuária deve considerar:

1. Qual é o tipo de pedido?
2. Qual camada do Grimório deve ser consultada?
3. Existe dado ou evidência fornecida?
4. O dado é permitido, anonimizado e adequado para análise?
5. Há limitação de acesso?
6. A resposta separa fato, hipótese, interpretação e recomendação?
7. A saída está adequada ao público-alvo?

## Tipos de pedido suportados

- análise de sprint;
- diagnóstico de time;
- leitura de dashboard;
- documentação de processo;
- plano de melhoria;
- relatório executivo;
- status report;
- roadmap;
- resposta de e-mail;
- avaliação de maturidade;
- explicação de fluxo ou métrica.

## Ordem de consulta recomendada

1. `00_LEIA_PRIMEIRO.md`
2. `09_governanca_compliance/`
3. `01_documentacao_base/`
4. `03_de_para_galapagos/`
5. `05_metricas_e_dados/`
6. `04_times/`, quando o pedido for específico de um time
7. `07_entregaveis/`, quando houver saída esperada
8. `08_comunicacao/`, quando a resposta for executiva ou formal
9. `10_historico_aprendizados/`, quando houver necessidade de contexto evolutivo

## Regra de acesso

O Grimório não concede acesso automático a Azure DevOps, Power BI, Confluence, Box, SharePoint, e-mails ou qualquer outro sistema corporativo.

Se os dados não foram fornecidos ou se não houver integração autorizada, a IA deve declarar limitação.

## Regra de interpretação

Toda análise deve separar:

- fato;
- evidência;
- hipótese;
- interpretação;
- risco;
- recomendação.

## Regra de segurança

Não inserir neste repositório:

- dados pessoais;
- credenciais;
- tokens;
- contratos;
- dados financeiros sensíveis;
- informações estratégicas confidenciais;
- exportações completas sem necessidade;
- documentos internos não autorizados.

## Regra de uso

Este repositório deve ser usado como camada de contexto e orientação, não como repositório bruto de dados operacionais.
