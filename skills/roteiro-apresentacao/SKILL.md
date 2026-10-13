---
name: roteiro-apresentacao
description: Escreve o roteiro de fala de uma apresentação, slide por slide, alinhado 1:1 com o deck — objetivo de cada slide, tópicos obrigatórios, fala sugerida, dados citados com a fonte quando houver, tempo e transição — e gera as notas do apresentador para embutir no deck HTML (tecla N) e no PowerPoint. Use sempre que pedirem roteiro, script de fala, "o que falar em cada slide", notas do apresentador, ensaio ou preparação para apresentar, inclusive quando o assistente-apresentacoes encaminhar um plano de slides. Também serve para escrever notas para um deck HTML que já existe.
---

# Roteiro de Apresentação

Escreve o que a pessoa vai **dizer** enquanto o deck mostra o que a plateia **vê**. O roteiro e os slides contam a mesma história, com a mesma numeração, mas não repetem um ao outro: o slide tem a manchete (e o número, quando houver); a fala dá o contexto, a explicação ou a história, o porquê e a ponte para o próximo slide.

Sempre em **português do Brasil**.

## Entradas

Use a primeira que estiver disponível:

1. **Plano de slides** (vindo do `assistente-apresentacoes`): é a fonte da verdade da ordem e do conteúdo. Escreva exatamente um bloco por slide do plano, na mesma ordem.
2. **Deck HTML já pronto**: extraia os slides com `python scripts/notas_do_roteiro.py --listar-deck deck.html` e escreva um bloco por slide encontrado.
3. **Só o material bruto**: monte primeiro uma lista numerada de slides (tipo + mensagem) e confirme com o usuário antes de escrever, porque sem deck ou plano o alinhamento fica no ar. Se o usuário também quiser o deck, encaminhe para o `assistente-apresentacoes`.

Leia sempre o **material-fonte** (roteiro, tópicos, texto, relatório, PDF), não só o plano: a fala precisa de contexto, exemplos e detalhes que não cabem no slide. O material pode ser de qualquer assunto e não ter número nenhum; nesse caso, as regras sobre dados abaixo simplesmente não se aplicam. Se o usuário já escreveu a própria fala, preserve as palavras e o tom dele: divida por slide, ajuste só para o ouvido e para o tempo, e não reescreva do zero.

Contexto que muda o texto: **duração total**, **público** e **objetivo** (aprovar, informar, convencer, ensinar). Se vierem no plano, use. Se faltar a duração, pergunte. Público e objetivo, deduza do material e declare a suposição no cabeçalho do roteiro.

## Orçamento de tempo

Distribua a duração total entre os slides antes de escrever, e faça a soma fechar com até 10% de folga:

- capa: 20–40 s · divisor de seção: 10–20 s · encerramento/decisão: 45–90 s
- slide de dado único ou declaração: 30–60 s
- slide denso (gráfico, comparação, 3+ cards, linha do tempo): 60–120 s

Uma fala natural em português tem cerca de **130 palavras por minuto**. Use isso para dimensionar a fala sugerida de cada slide (um slide de 45 s → ~100 palavras, no máximo). Se o tempo não fecha nem com falas enxutas, diga ao usuário quais slides cortar ou fundir, em vez de espremer a fala.

## Formato do roteiro

Salve como `roteiro.md` seguindo `references/modelo-roteiro.md` à risca. Os títulos `## Slide NN — Título · ⏱ tempo` e os rótulos em negrito são lidos pelo script que gera as notas do deck, então não os renomeie.

Cada slide tem:

- **Objetivo** — uma frase: o que a plateia deve sair sabendo ou sentindo depois deste slide.
- **Abordar** — 2 a 4 tópicos obrigatórios, curtos, na ordem em que serão ditos. É o que a pessoa olha de relance enquanto fala.
- **Fala sugerida** — um parágrafo de fala natural, para apoiar, não para ler palavra por palavra.
- **Dados citados** — cada número dito, com a fonte exata (página do PDF, seção ou tabela). Omita se o slide não tem números.
- **Transição** — uma frase-ponte que puxa o próximo slide. O último slide fecha com o pedido ou a mensagem final, em vez de transição.
- **Se perguntarem** (opcional) — só em slides com números polêmicos, ressalvas metodológicas ou decisão: a pergunta provável e uma resposta curta.

No início vai um cabeçalho (título, público, objetivo, duração, tabela-resumo com tempo por slide) e, no fim, uma seção curta de **Preparação para perguntas** com 3 a 5 perguntas gerais e respostas.

## Como escrever a fala

- **Complemente o slide, não leia o slide.** Se o slide diz "6,77% de atraso", a fala diz o que isso significa e por que importa ("de cada 15 entregas, uma chega depois do prometido, e é justamente aí que a nota despenca").
- **Escreva para o ouvido:** frases curtas, verbos ativos, uma ideia por frase. Nada de parênteses, siglas não explicadas ou listas faladas com mais de três itens.
- **Números iguais aos do slide** (quando houver). Arredonde na fala só quando o slide também arredonda, ou diga os dois ("cerca de 96 mil pedidos, 96.478 para ser exato"). Um número diferente entre fala e tela destrói a credibilidade na hora.
- **Leve as ressalvas do material para a fala.** Se o material diz que uma relação é associação e não causa, ou que um valor não é perda comprovada, a fala precisa dizer isso no slide em que o número aparece. Diante de investidores, de uma banca ou de um cliente, é isso que protege quem apresenta.
- **Abra forte e feche com o pedido.** A primeira fala diz por que a plateia deve prestar atenção; a última diz claramente o que se espera dela (aprovar, decidir, agir).
- **Transições contam a história.** Use as transições para encadear causa e consequência ("…e se a entrega atrasa, o que acontece com a avaliação? É o que vem a seguir.").
- Ajuste o registro ao público: diretoria e investidores → direto, focado em impacto e decisão; banca acadêmica → método e limites explícitos; equipe → prático e próximo; aula → didático, com exemplos e perguntas à plateia; palestra → narrativo, com histórias e pausas.

## Notas do apresentador no deck

As notas são a versão de bolso do roteiro: tempo, tópicos do "Abordar" e a fala sugerida. Gere-as a partir do `roteiro.md` com o script, nunca reescrevendo à mão, para que documento e deck digam exatamente a mesma coisa:

```bash
# gera notas.json (para o construtor inserir ao montar o deck)
python scripts/notas_do_roteiro.py roteiro.md --json notas.json

# ou injeta direto num deck HTML existente
python scripts/notas_do_roteiro.py roteiro.md --deck deck.html --saida deck-com-notas.html

# ou grava nas anotações do apresentador de um PowerPoint
python scripts/notas_do_roteiro.py roteiro.md --pptx deck.pptx
```

O script recusa a injeção se o número de slides do roteiro for diferente do número de slides do deck (HTML ou PowerPoint), diz qual lado tem slides a mais e lista os títulos lado a lado para conferência. Corrija o desalinhamento antes de entregar.

## Entrega

- **Documento:** entregue o roteiro como documento editável. Use o tipo de documento do ambiente quando houver (ex.: um doc do Claude, que exporta para Word e PDF); senão gere `.docx` com a skill de Word. Mantenha a estrutura do modelo: título por slide, rótulos em negrito, tempo visível.
- **Notas:** `notas.json` para o construtor, ou o deck (HTML e/ou PowerPoint) já com as notas.
- No chat, só uma linha: duração total, número de slides e como abrir as notas no deck (tecla N).
