# MAM Galápagos — Pulso Semanal/Sprint

Este diretório contém o modelo versionado do relatório **MAM Galápagos — Pulso Semanal/Sprint**.

O objetivo é gerar uma leitura executiva semanal dos times, usando dados operacionais, critérios do MAM e regras claras de interpretação. O relatório não deve ser tratado como avaliação definitiva de maturidade. Ele é um **pulso operacional** para apoiar conversa, desbloqueio, previsibilidade e continuidade.

## Nome do relatório

**MAM Galápagos — Pulso Semanal/Sprint**

Para a visão mensal, usar:

**MAM Galápagos — Leitura Mensal de Maturidade Operacional**

## Regras centrais

1. Entrega de sprint considera somente **User Story** e **Bug** em **Closed**.
2. **Task**, **Bug Task** e **Blocker** entram como evidência de fluxo, decomposição, bloqueio e saúde operacional, mas não como entrega final.
3. **Resolved → Closed** deve ser tratado como **Deploy Time**.
4. Itens em **Resolved**, **Ready to Deploy**, **QA**, **Homologação** ou **Deployed** não contam como entregues, salvo regra explícita validada pela área.
5. **Aging** mede há quanto tempo o item está parado no status atual.
6. **Transbordo** mede itens planejados e não fechados no recorte.
7. Bloqueios fora da sprint devem influenciar o diagnóstico quando afetam previsibilidade do time.

## Regra visual

Este modelo deve priorizar clareza gerencial. O visual precisa ser limpo, consistente e sem sobreposição.

Regras obrigatórias:

- A visão global deve ter no máximo 4 times por página.
- Se houver 5 ou 6 times, gerar página adicional.
- A nota MAM deve ficar dentro do bloco de score.
- Nenhum número deve invadir texto, gráfico ou outro card.
- Comentários devem ser curtos.
- Diagnóstico profundo não entra na página global; entra na página detalhada por time.
- Texto longo deve ser reduzido ou truncado pelo gerador.

## Estrutura

```text
07_entregaveis/mam_pulso_semanal/
  README.md
  mam_pulso_layout.py
  mam_schema.json
  mam_blank.json
  mam_ficticio.json
```

## Uso

Gerar relatório fictício:

```bash
python mam_pulso_layout.py --data mam_ficticio.json --out output
```

Gerar modelo em branco:

```bash
python mam_pulso_layout.py --data mam_blank.json --out output_blank --blank
```

## Observação

A nota semanal ajuda a direcionar conversa e desbloqueio, mas não deve ser usada isoladamente como avaliação definitiva de maturidade do time.
