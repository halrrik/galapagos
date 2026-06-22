# Checklist de protecao por repositorio

Usar este checklist antes de commitar politicas de protecao em qualquer repositorio.

## Identidade do repositorio

- [ ] Nome do repositorio confirmado.
- [ ] Finalidade do repositorio documentada.
- [ ] Repositorio classificado como: interno, social, comercial, publico, privado ou misto.
- [ ] Dono/responsavel declarado.
- [ ] Relação com ShadeVanSoul / Grimorio / Galapagos descrita.

## Visibilidade e acesso

- [ ] Repositorio privado, se contiver arquitetura, metodo, prompts, scoring, scripts ou produto comercial.
- [ ] Acessos revisados.
- [ ] Terceiros removidos ou justificados.
- [ ] Branches e releases revisados.
- [ ] Forks/cópias publicas conhecidos mapeados, se houver.

## Arquivos de protecao

- [ ] AUTHORS.md ou equivalente.
- [ ] LICENSE.md proprietaria ou equivalente.
- [ ] NOTICE.md.
- [ ] TERMS_OF_USE.md.
- [ ] PRIVACY_AND_DATA_USE.md.
- [ ] SECURITY.md.
- [ ] ANTI_PLAGIARISM_POLICY.md.
- [ ] GOVERNANCE.md ou REPO_GOVERNANCE.md.

## Dados e privacidade

- [ ] Nenhum token, segredo ou credencial versionado.
- [ ] Nenhum dado sensivel desnecessario.
- [ ] Nenhum dado de cliente/time usado como amostra sem sanitizacao.
- [ ] Arquivos de exemplo revisados.
- [ ] Outputs de testes revisados.

## Produto e distribuicao

- [ ] Se houver skill/produto, ela esta em pasta propria.
- [ ] A skill/produto tambem possui seus proprios arquivos de protecao.
- [ ] O zip de distribuicao nao expoe mais do que o necessario.
- [ ] Arquitetura interna nao essencial foi removida do pacote publico/comercial.

## Commit recomendado

Mensagem sugerida:

`adicionar pacote documental de protecao sem sobrescrever arquivos existentes`
