# Protocolo Validar, Comitar, Auditar e Limpar — Galapagos

Status: Vigente  
Tipo: regra_operacional  
Escopo: Grimorio Galapagos  
Ultima atualizacao: 2026-06-17  
Responsavel: Richard / IA  
Origem: falha de recuperacao do template de Status Report das Squads  
Sensibilidade: interno

---

## Objetivo

Definir o protocolo minimo para criar, comitar, validar, auditar e limpar conteudo dentro do Grimorio Galapagos.

Este protocolo existe para evitar arquivos soltos, templates nao encontraveis, regras duplicadas, memoria morta e respostas futuras desalinhadas ao contexto Galapagos.

---

## Regra central

Conteudo novo comitado sem validacao, sem rota e sem mecanismo de recuperacao nao esta operacionalmente incorporado ao Grimorio Galapagos.

Ele pode existir como arquivo no repositorio, mas nao deve ser tratado como conhecimento funcional ate ser localizavel pelo fluxo padrao.

---

## Pilares respeitados

Este protocolo protege os tres pilares do Grimorio:

- Hipotese: o conteudo novo deve reforcar a continuidade e reduzir repeticao de contexto.
- Regras: o conteudo novo deve obedecer o fluxo de entrada, indice, rotas, fonte e validacao.
- Autoaprendizado: o conteudo novo deve virar conhecimento reutilizavel, encontravel e limpo, nao apenas arquivo acumulado.

---

## Entrada obrigatoria

Antes de qualquer execucao relevante no Grimorio Galapagos, a IA deve:

1. Ler `00_LEIA_PRIMEIRO.md`.
2. Consultar `01_INDICE.md`.
3. Seguir `02_ROTAS.md`.
4. Verificar regras locais aplicaveis.
5. Separar fato, evidencia, hipotese, interpretacao e recomendacao.

Se esse fluxo for pulado, o erro acontece antes da entrega. O que vier depois nao repara a falha.

---

## Documentar

Documentar e criar ou atualizar conteudo necessario.

Antes de documentar, verificar:

- qual problema operacional esta sendo resolvido;
- se o conteudo e regra, decisao, template, memoria, evidencia, aprendizado, entregavel ou rascunho;
- se ja existe arquivo equivalente;
- se deve ficar em Galapagos ou no Grimorio Pai;
- se contem informacao sensivel que nao deve ser persistida.

Documentar nao significa incorporar. A incorporacao so acontece quando o conteudo fica encontravel.

---

## Comitar

Comitar e registrar a mudanca no repositorio.

Antes de comitar, verificar:

- repositorio correto;
- caminho correto;
- nome de arquivo coerente;
- conteudo sem dados proibidos;
- mensagem de commit coerente com a mudanca.

Commit sozinho nao valida a mudanca.

---

## Validar

Validar e conferir a acao ou o ultimo commit feito. E o equivalente a um teste unitario.

A validacao deve verificar:

- arquivo criado ou alterado existe no caminho esperado;
- Markdown, JSON ou YAML esta legivel e minimamente bem formado;
- metadados minimos existem quando o arquivo for relevante;
- linguagem esta adequada ao papel do arquivo;
- indice, rota, README ou outro mecanismo de recuperacao foi atualizado quando necessario;
- patch log foi atualizado quando a mudanca for estrutural;
- uma IA futura consegue encontrar o conteudo a partir de um pedido curto.

Resultado esperado:

- OK;
- OK com avisos;
- Falhou;
- Bloqueado por falta de acesso, fonte ou contexto.

---

## Auditar

Auditar e revisar a integracao da mudanca com o repositorio. E o equivalente a um teste integrado.

A auditoria deve verificar:

- se a mudanca nao contradiz regras vigentes;
- se nao criou duplicidade ou sobreposicao de conteudo;
- se indice e rotas continuam apontando para os caminhos certos;
- se o novo conteudo nao ficou como memoria paralela nao roteada;
- se o conteudo novo reforca a hipotese do Grimorio Galapagos;
- se o conteudo permite continuidade em outro chat sem nova explicacao longa.

---

## Limpar

Limpar e reduzir ruido, redundancia e fragmentacao.

Usar limpeza quando houver:

- arquivos duplicados;
- regras equivalentes em locais diferentes;
- templates antigos substituidos;
- rascunhos que viraram fonte oficial;
- arquivos temporarios sem uso;
- memoria bruta que deve virar aprendizado processado.

A limpeza pode consolidar, arquivar, marcar obsoleto ou remover conteudo, sempre respeitando validacao e seguranca.

---

## Regra de parada

Se uma mudanca quebra entrada, regra, rota, indice, recuperacao ou validacao, parar.

Nao seguir explicando downstream.

Primeiro reparar o gate quebrado. Depois continuar.

---

## Criterio de incorporacao funcional

Um conteudo so esta funcionalmente incorporado ao Grimorio Galapagos quando:

- existe no caminho esperado;
- possui finalidade clara;
- esta referenciado por indice, rota, README ou arquivo de entrada;
- quando aplicavel, foi registrado no patch log;
- pode ser recuperado por uma IA futura sem depender da memoria do chat atual;
- nao contradiz regras locais ou limites de governanca.
