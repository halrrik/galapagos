---
origem: Documento de Processos Tecnologia.docx
status: convertido_para_markdown
classificacao_sugerida: revisar_antes_de_publicar
aplicacao: Grimorio Versao Galapagos
---

# Campos, Políticas, DoR e DoD

## 1. Objetivo desta Parte

Esta parte define **as regras mínimas de qualidade do sistema**.

Aqui não se discute fluxo nem hierarquia — isso já foi definido. Aqui se define **o que precisa estar verdadeiro para que o trabalho avance**.

Campos, políticas, DoR e DoD existem para **proteger o fluxo**, não para burocratizá-lo.

## 2. Campos como Contrato do Sistema

Campos não são informativos. São **contratos operacionais**.

Se um campo existe, ele existe porque:

- suporta decisão

- protege qualidade

- habilita métricas

Preencher campo “por preencher” é ruído. Não preencher campo obrigatório é quebra de contrato.

## 3. Campos Comuns a User Story e Solicitação

User Story e Solicitação compartilham exatamente os mesmos campos. A diferença entre elas é semântica e temporal, não estrutural.

Campos obrigatórios ao longo do fluxo:

- Título — claro, objetivo e verificável

- Descrição — contexto suficiente para entendimento (Se facilitara templates para agilizar a documentação )

- Critérios de Aceite — condição objetiva de validação

- Parent — relação pai obrigatória

- Área de Trabalho — classificação correta

- Origem — sistema, canal ou produto

- Prioridade — definida antes do downstream

- Bloqueado (Sim/Não)

- Tipo de Bloqueio (quando aplicável)

- Blocked Start / Blocked End  (Power automate)

- Due date / Target date / Start day

Sem esses campos, o item não avança de estado.

## 4. Campos Específicos por Tipo de Artefato

**Iniciativa**

- Objetivo

- Justificativa

- Indicadores de Sucesso

- Premissas

- Riscos

- Dependências

**Épico**

- Objetivo do Épico

- Escopo macro

- Dependências

**Feature**

- Valor de Negócio

- Time Criticality

- Effort

- Risco

**Bug**

- Severidade

- Passos para Reprodução

- Ambiente / Versão

- Impacto

**Task**

- Descrição técnica clara

Campos existem para clareza, não controle.

## 5. Políticas Explícitas do Sistema

### 5.1 Política de Bloqueio

- Consideramos este campo para bloqueios e/ou impedimentos.

- Bloqueio deve ser marcado imediatamente

- Todo bloqueio deve ter tipo definido

- Data de início e fim de bloqueio, será preenchido automaticamente

- Bloqueio sem motivo é inválido

Bloqueio visível protege o time e expõe o sistema.

### 5.2 Política de Avanço de Estado   [ainda em progresso esta parte]

- Item só avança se cumprir o objetivo do estado atual

- Estados não são pulados

- Avanços artificiais são considerados erro operacional

Mover cartão não é progresso. Progresso é redução de incerteza.

### 5.3 Política de Criação de Itens

- Nenhum item pode ser criado sem pai válido

- O tipo correto deve ser escolhido desde o início

- Conversões são permitidas (ex: Solicitação → Story)

Criar errado no início custa caro no final.

## 6. Definition of Ready (DoR)  [Ainda em progresso esta parte]

Um item está Ready quando pode entrar no downstream sem gerar retrabalho.

Critérios mínimos de DoR para Story / Solicitação:

- Objetivo claro

- Critérios de aceite definidos

- Dependências conhecidas

- Viabilidade técnica validada

- Prioridade definida

- Pai corretamente associado

Sem DoR, o item não entra em execução.

## 7. Definition of Done (DoD)  [Ainda em progresso esta parte]

Um item está Done quando entrega valor real e verificável.

Critérios mínimos de DoD:

- Desenvolvimento concluído

- Code review realizado

- Testes executados

- Critérios de aceite atendidos

- Deploy realizado (quando aplicável)

- Documentação mínima atualizada

Fechar item sem DoD é transferir problema para frente.

## 8. Responsabilidade e Governança

- Time é responsável por respeitar DoR e DoD

- Produto é responsável pela clareza funcional

- Tecnologia é responsável pela qualidade técnica

- Liderança é responsável por proteger o sistema

Quando DoR e DoD são ignorados, o problema não é o time é a governança.
