# Governanca do repositorio - rascunho

## Classificacao

Cada repositorio do ecossistema deve ser classificado antes de receber material sensivel:

- publico demonstrativo;
- privado operacional;
- privado sensivel;
- produto comercial;
- iniciativa social;
- laboratorio/experimento;
- arquivo historico.

## Regra de separacao

Nao misturar no mesmo pacote:

- nucleo privado do Grimorio;
- versao de aplicacao para terceiros;
- dados pessoais de Richard;
- dados de clientes;
- material comercial;
- material social gratuito;
- experimentos nao validados.

## Repositorios sensiveis

Repositorios que contenham arquitetura, metodo, prompts, scoring, scripts, governanca, estrategias, contexto privado ou produtos comercializaveis devem ser privados por padrao.

## Releases e zips

Zips distribuiveis devem conter apenas o necessario para uso autorizado. Nao incluir contexto administrativo, decisoes internas, historico privado ou dados sensiveis.

## Auditoria futura

Toda mudanca em arquivos de politica, licenca, autoria, seguranca, privacidade ou anti-plagio deve ser revisada antes de merge/commit final.

## Nao sobrescrita

Atualizacoes de protecao devem ser aditivas ate auditoria. Nao sobrescrever arquivos existentes sem comparar conteudo e registrar decisao.
