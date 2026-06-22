# Pacote aditivo de protecao de repositorio v0.1.0

Este pacote foi criado para adicionar uma camada inicial de protecao documental aos repositorios do ecossistema ShadeVanSoul / Grimorio / Galapagos sem sobrescrever arquivos existentes.

## Regra principal

Nao copie estes arquivos por cima de arquivos existentes sem auditoria manual.

Os arquivos deste pacote usam nomes com sufixo `_DRAFT.md` justamente para evitar sobrescrita acidental de `LICENSE.md`, `NOTICE.md`, `README.md`, `SECURITY.md` ou politicas que ja existam no repositorio.

## Como usar

1. Descompactar este pacote fora do repositorio ou em uma pasta temporaria.
2. Comparar os arquivos `_DRAFT.md` com os arquivos ja existentes no repositorio.
3. Decidir, arquivo por arquivo, se o conteudo sera:
   - mantido apenas como referencia;
   - incorporado parcialmente em arquivo existente;
   - convertido em arquivo oficial na raiz do repositorio;
   - adaptado para um repositorio especifico.
4. Registrar no commit que esta e uma inclusao de protecao documental, nao uma mudanca funcional do produto.

## O que este pacote nao faz

- Nao substitui registro formal de marca, software ou obra intelectual.
- Nao substitui revisao juridica.
- Nao remove exposicoes anteriores de repositorios publicos.
- Nao protege automaticamente contra copia tecnica ou engenharia reversa.
- Nao deve ser tratado como licenca juridica final sem validacao.

## O que este pacote faz

- Declara autoria e titularidade pretendida.
- Reduz ambiguidade de uso, copia, distribuicao e derivacao.
- Cria material para auditoria futura.
- Ajuda a separar repositorio publico, privado, social, interno e comercial.
- Evita que a protecao seja apagada por parecer arquivo sem sentido.

## Data base operacional

Data base inicial usada neste pacote: 2026-06-03.

Essa data representa o marco operacional inicial do nucleo ShadeVanSoul / Grimorio conforme contexto do projeto. Antes de registro formal, validar se esta e a melhor data a declarar em documentos oficiais.
