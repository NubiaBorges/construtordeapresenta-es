# Formato do plano de slides (`plano.md`)

O plano é o contrato entre o roteiro e o deck. As duas skills recebem o mesmo arquivo e precisam produzir exatamente um slide/bloco por item, na mesma ordem.

```markdown
# Plano de slides — [Título da apresentação]

## Contexto
- **Público:** [deduzido ou informado]
- **Objetivo:** [aprovar / informar / convencer / ensinar — e o que exatamente]
- **Duração:** [X min] · **Slides:** [N]
- **Saídas:** [HTML / PowerPoint / ambos] + roteiro em documento
- **Conteúdo-fonte:** [arquivo(s)]
- **Design:** [arquivo de referência] — fontes [..]; cores [..]; fundos [claro/escuro/alternado]; elementos [logo, formas decorativas, cards]
- **Suposições:** [o que foi deduzido e não estava explícito]

## Divergências e alertas
- [número/texto da referência de design que diverge do conteúdo-fonte, dado ausente, inconsistência interna do material]

## Sequência
| Nº | Tipo | Título | Mensagem-chave | Tempo |
|---|---|---|---|---|
| 01 | Título | ... | ... | 30 s |
| 02 | Estatísticas | ... | ... | 1 min |

## Slides

### Slide 01 — [Título]
- **Tipo:** [tipo do construtor: Título, Citação, Grade, Comparação, Problema/Solução, Etapas, Linha do tempo, Diagrama, Hub, Estatísticas, Screenshot, Divisor, FAQ, CTA — ou "Gráfico de barras"/"Barra empilhada" quando for dado]
- **Mensagem-chave:** [a frase que a plateia deve lembrar]
- **Na tela:** [exatamente o que aparece: títulos, números com a formatação final, itens]
- **Fonte:** [opcional — pág./seção/tabela do conteúdo-fonte para cada número ou fato; omita em roteiros sem dados]
- **Para a fala:** [contexto, ressalvas, comparações que NÃO vão na tela mas o apresentador deve dizer]
- **Design:** [opcional — fundo, destaque, elemento visual]
```

Regras:
- Se houver números, em **Na tela** já com a formatação final (ex.: `R$ 13,2 mi`, `6,77%`). O roteiro e o deck copiam daqui, então qualquer arredondamento é decidido uma vez só.
- Toda ressalva relevante do material vai em **Para a fala** do slide onde o assunto aparece.
- Em roteiros simples, sem dados, **Para a fala** guarda o que o apresentador conta (história, exemplo, explicação) e **Na tela** fica curto: uma frase, poucos itens ou uma imagem.
- A tabela **Sequência** e os blocos **Slides** têm a mesma quantidade e a mesma ordem.
