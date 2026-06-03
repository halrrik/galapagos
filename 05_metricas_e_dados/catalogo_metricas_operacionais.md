---
origem: Documento de Processos Tecnologia.docx
status: convertido_para_markdown_parcial
classificacao_sugerida: revisar_antes_de_publicar
aplicacao: Grimorio Versao Galapagos
---

# Catálogo de Métricas Operacionais

Este arquivo reúne métricas usadas para leitura do fluxo, previsibilidade, qualidade e estabilidade operacional.

## 1. Lead Time

Mede o tempo total que uma demanda permanece no sistema, do ingresso à conclusão.

Uso principal:

- avaliar eficiência ponta a ponta;
- entender tempo total percebido pelo negócio;
- identificar longas esperas no fluxo.

Regra de interpretação:

- declarar marco inicial e marco final usados no cálculo;
- preferir leitura por percentis quando houver histórico suficiente;
- não comparar times sem verificar fluxo, tipo de trabalho e critérios de fechamento.

## 2. Cycle Time

Mede o tempo efetivo de execução no downstream, do início real do trabalho até a entrega ou conclusão definida.

Uso principal:

- avaliar estabilidade da execução;
- apoiar previsibilidade operacional;
- identificar variação entre demandas semelhantes.

Regra de interpretação:

- declarar se o cálculo usa Desenvolvimento, In Progress, Resolved, Closed ou outro marco equivalente;
- separar tempo de execução de tempo de espera sempre que possível.

## 3. Aging

Mede o tempo que uma demanda permanece em determinado estado do fluxo.

Uso principal:

- identificar itens envelhecendo;
- localizar gargalos;
- apoiar atuação sobre WIP parado.

Regra de interpretação:

- aging alto indica necessidade de investigação, não culpa individual;
- diferenciar espera, bloqueio, validação, desenvolvimento e deploy.

## 4. Throughput

Mede a quantidade de itens concluídos por período.

Uso principal:

- compreender capacidade histórica;
- apoiar planejamento;
- avaliar estabilidade de entrega.

Regra de interpretação:

- analisar por tipo de item;
- não misturar bugs, histórias, tarefas e iniciativas sem critério;
- usar tendência, não apenas ponto isolado.

## 5. Bloqueios

Mede ocorrência, duração e tipo de bloqueio no fluxo.

Uso principal:

- identificar restrições sistêmicas;
- evidenciar dependências;
- apoiar melhoria de fluxo.

Regra de interpretação:

- todo bloqueio precisa ter motivo;
- bloqueios recorrentes devem virar problema estrutural a ser tratado;
- tempo bloqueado deve ser separado do tempo de execução.

## 6. Previsibilidade

Mede a relação entre o que foi planejado e o que foi efetivamente entregue.

Uso principal:

- avaliar consistência de planejamento;
- apoiar conversas de capacidade;
- identificar impacto de não planejados e transbordo.

Regra de interpretação:

- não confundir baixa previsibilidade com baixa produtividade automaticamente;
- investigar mudanças de prioridade, bloqueios, dependências e urgências.

## 7. Retrabalho

Mede itens reabertos, correções repetidas, bugs derivados ou ajustes após validação.

Uso principal:

- avaliar qualidade do refinamento;
- avaliar qualidade de execução;
- identificar desperdício.

Regra de interpretação:

- retrabalho pode nascer no discovery, refinamento, desenvolvimento, QA ou validação de negócio;
- evitar tratar como falha isolada de desenvolvimento sem evidência.

## 8. Bugs pós-entrega

Mede falhas identificadas após entrega ou publicação.

Uso principal:

- avaliar qualidade da entrega;
- identificar fragilidades de teste;
- avaliar impacto de mudanças em produção.

Regra de interpretação:

- diferenciar severidade, recorrência e impacto;
- relacionar com mudanças recentes, cobertura de teste e critérios de aceite.

## 9. Frequência de deploy ou release

Mede com que frequência mudanças chegam efetivamente ao ambiente final definido.

Uso principal:

- avaliar fluidez da entrega final;
- identificar filas em ready to deploy;
- analisar estabilidade da cadência de publicação.

Regra de interpretação:

- diferenciar item pronto de item publicado;
- considerar janelas de deploy, dependências e governança de mudança.

## 10. Tempo de recuperação

Mede quanto tempo o sistema ou serviço leva para voltar a um estado aceitável após incidente ou falha relevante.

Uso principal:

- avaliar resiliência operacional;
- apoiar gestão de incidentes;
- identificar riscos de continuidade.

Regra de interpretação:

- separar tempo de detecção, tempo de resposta e tempo de recuperação quando houver dados.

## 11. Indisponibilidade

Mede tempo em que serviço, aplicação ou capacidade ficou indisponível ou degradada.

Uso principal:

- avaliar estabilidade percebida;
- apoiar governança de risco;
- conectar qualidade técnica ao impacto no negócio.

Regra de interpretação:

- diferenciar indisponibilidade total, parcial e degradação;
- registrar impacto ao cliente ou operação quando aplicável.
