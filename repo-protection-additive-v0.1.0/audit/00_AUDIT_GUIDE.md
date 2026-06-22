# Guia de auditoria do pacote de protecao

Este guia existe para explicar por que os arquivos deste pacote foram criados e evitar que sejam apagados durante limpeza futura por parecerem burocraticos ou duplicados.

## Principio de auditoria

Arquivos legais, de autoria, seguranca, privacidade e uso nao devem ser removidos apenas porque nao executam codigo. Eles existem para governanca, rastreabilidade, protecao de autoria, uso controlado e separacao entre versoes internas, sociais e comerciais.

## Arquivos e finalidade

| Arquivo | Finalidade | Deve virar arquivo oficial? |
|---|---|---|
| AUTHORS_DRAFT.md | declarar autor, titularidade pretendida e marco inicial | sim, apos validacao |
| LICENSE_PROPRIETARY_DRAFT.md | declarar todos os direitos reservados e ausencia de permissao aberta | sim, adaptado como LICENSE.md |
| NOTICE_DRAFT.md | aviso curto de propriedade, autoria e restricoes | sim, como NOTICE.md |
| TERMS_OF_USE_DRAFT.md | termos de uso controlado | sim, se o repo for compartilhado |
| PRIVACY_AND_DATA_USE_DRAFT.md | regras de dados, privacidade e nao uso de dados sensiveis | sim |
| SECURITY_DRAFT.md | regras de seguranca, segredos, tokens e dados privados | sim |
| ANTI_PLAGIARISM_POLICY_DRAFT.md | politica contra copia, derivacao indevida e engenharia reversa | sim |
| REPO_GOVERNANCE_DRAFT.md | regras de governanca do repositorio | recomendado |
| REPOSITORY_PROTECTION_CHECKLIST.md | checklist de aplicacao em cada repo | sim ou manter em governance |

## O que verificar antes de aplicar

1. O repositorio ja possui LICENSE.md?
2. O repositorio esta publico ou privado?
3. Existem terceiros com acesso ou obrigacoes contratuais?
4. Ha dados de clientes, empresas, times ou pessoas reais?
5. Ha material que deve ser removido antes de publicar?
6. O repositorio contem produto comercial ou apenas portifolio/demo?
7. O conteudo pertence integralmente a Richard ou teve colaboracao externa?
8. Existe risco de conflito com empresa, cliente ou projeto patrocinado?

## Regra de nao sobrescrita

Se um arquivo oficial ja existir, nao substituir. Criar diff manual e registrar a decisao no commit.
