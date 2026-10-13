---
name: assistente-apresentacoes
description: Assistente que coordena a criação completa de uma apresentação a partir de qualquer conteúdo, sobre qualquer assunto (um roteiro simples, tópicos, aula, palestra, relatório, artigo, ideia descrita no chat) e de referências de design (PowerPoint, PDF de slides, imagens, design system). Separa conteúdo de design, monta um plano de slides para aprovação e depois pergunta duração e formato de saída (HTML, PowerPoint para editar no Canva, ou ambos) e depois aciona a skill roteiro-apresentacao (roteiro de fala por slide) e a construtor-apresentacoes (deck), entregando deck e roteiro alinhados slide a slide. Use sempre que o usuário enviar ou descrever um conteúdo, com ou sem referências de design, e pedir uma apresentação, ou pedir deck e roteiro juntos, "preparar a apresentação", "montar slides e o que falar", mesmo que não cite o assistente.
---

# Assistente de Apresentações

Coordena duas skills especialistas para entregar, a partir do mesmo material, um **deck HTML** e um **roteiro de fala** que contam a mesma história com a mesma numeração:

- `roteiro-apresentacao` → o que dizer em cada slide (documento + notas do apresentador).
- `construtor-apresentacoes` → o deck em HTML (notas na tecla N) e/ou em PowerPoint editável (notas nas anotações), conforme o formato pedido.

O papel do assistente é fazer o trabalho que nenhuma das duas faz bem sozinha: entender o material, decidir a história e fixar um **plano de slides** que as duas seguem à risca. Sem um plano comum, o roteiro e o deck divergem na numeração, nos números ou no que é dito em cada página.

Tudo em **português do Brasil**.

**O conteúdo pode ser de qualquer tipo.** Um roteiro de poucas linhas, uma lista de tópicos, uma aula, uma palestra motivacional, um treinamento, um relatório cheio de dados ou só um tema descrito no chat. Muitas apresentações não têm número nenhum. Adapte tudo abaixo ao que o material é: as regras sobre números e fontes só se aplicam quando houver números; num roteiro simples, o trabalho é organizar as ideias, dar ritmo e deixar cada slide visualmente forte. Se o usuário só descrever o tema, sem arquivo, use a descrição como conteúdo e não invente fatos: o que não estiver no pedido entra como sugestão marcada no plano.

## Fluxo

### 1. Triagem dos arquivos
Classifique cada arquivo recebido e diga a classificação no plano:

- **Conteúdo-fonte** — roteiro, tópicos, texto, aula, relatório, artigo, notas (PDF, DOCX, TXT, MD) ou o próprio texto do pedido no chat. Documento com muito texto corrido e páginas de formato retrato costuma ser conteúdo.
- **Referência de design** — PowerPoint, PDF de slides (páginas 16:9, pouco texto, muito visual), imagens de identidade visual, design system em MD/HTML.
- **Imagens para mostrar** — screenshots, fotos de produto, gráficos que o usuário quer na tela.

Um PowerPoint "começado" pelo usuário é referência de design: use os textos dele só como pista da intenção, nunca como fonte de fatos ou números (a menos que o usuário diga que o conteúdo está ali). Se um arquivo for ambíguo e a classificação mudar o resultado, pergunte; senão, decida e declare.

### 2. Contexto
Do material, deduza **público** e **objetivo** e declare como suposição. Duas coisas você pergunta, se não estiverem no pedido nem no material, **juntas e numa única mensagem** logo no início, enquanto começa a leitura:

- **Duração** — define quantos slides cabem e o tamanho de cada fala.
- **Formato de saída** — só HTML (apresentar no navegador, com notas na tecla N), só PowerPoint (editar no PowerPoint, Canva ou Google Slides), ou os dois. Deixe claro que o roteiro em documento sai em qualquer caso. Se a pessoa mencionar Canva, edição ou "um PowerPoint comum", isso já responde: inclua o PowerPoint.

Quantidade de slides: em torno de **1 slide por minuto** em apresentações executivas, de banca e de resultados (capa, divisores e encerramento contam como meio slide), mínimo 6. Treinamentos, aulas e palestras de roteiro simples toleram mais slides por minuto (slides de uma frase ou imagem passam rápido); pitches curtos, menos. Se o roteiro já vem dividido em partes ou cenas, essa divisão é o ponto de partida. Essa conta é um ponto de partida, não um corte automático:

- Se o usuário já tem um deck (feito antes nesta conversa ou enviado) ou citou uma quantidade de slides, **essa quantidade é o padrão**. A duração muda o tamanho das falas, não o número de slides.
- Se a conta por duração der bem menos slides do que o material pede (cerca de 30% a menos, ou mais), não corte por conta própria. No plano, ofereça as opções lado a lado e deixe o usuário escolher: (a) manter todos os slides com falas curtas, (b) manter todos com falas médias e aceitar passar do tempo, ou (c) reduzir para N slides, dizendo exatamente o que sai. Cortar conteúdo é decisão de quem apresenta, porque é a pessoa que sabe o que o público espera ver.

### 3. Leitura do conteúdo
Leia o conteúdo-fonte inteiro, não só o resumo. Identifique a ideia central, as partes, os exemplos, as frases fortes e o tom (formal, inspirador, didático, descontraído). **Se houver números**, anote para cada um: o valor exato, a página/tabela de origem e qualquer ressalva (recorte, exclusões, "associação, não causa", "não é perda comprovada"). Quando o material tiver tabelas validadas e gráficos com recortes diferentes, use as tabelas validadas e mencione a diferença em **Divergências**.

### 4. Leitura do design
Siga as instruções de extração de design da `construtor-apresentacoes` (seção "Hierarquia de design"): fontes e cores reais dos slides, render do arquivo para ver layout e decoração, logo e ícones de marca. Resuma no plano em uma linha: fontes, cores, tipo de fundo e elementos característicos.

Ao comparar referência e conteúdo, procure divergências: número ou fato no PowerPoint diferente do conteúdo, rótulo trocado, texto de modelo esquecido ("Lorem ipsum", "$12M", países que não aparecem no estudo), erros de digitação. Liste todas em **Divergências e alertas**.

### 5. Plano de slides → aprovação
Escreva `plano.md` seguindo `references/formato-plano.md`. Pense na história antes dos slides e escolha o arco que combina com o material. Alguns exemplos: resultados/negócio → abertura que diz por que importa, diagnóstico com os dados, proposta, pedido; aula ou treinamento → o que vamos aprender, conceitos em ordem, exemplo, recapitulação; palestra ou roteiro narrativo → gancho, desenvolvimento, virada, mensagem final; institucional → quem somos, o que fazemos, como, contato. Se o roteiro do usuário já tem uma ordem, siga-a. Em material sem dados, o campo **Fonte** do plano é opcional e **Para a fala** guarda o que o apresentador conta (história, exemplo, explicação), enquanto **Na tela** fica curto: uma frase, poucos itens ou uma imagem. Cada slide tem uma mensagem-chave; se dois slides dizem a mesma coisa, funda.

Mostre ao usuário **no chat** uma versão compacta para aprovação: a tabela Sequência (nº, tipo, título, mensagem-chave, tempo), a soma do tempo, as suposições e as divergências. Se algum conteúdo do material ficou de fora, liste o que saiu e por quê, em destaque, junto com as opções de quantidade descritas no passo 2. Termine perguntando se aprova ou o que mudar. **Pare aqui e espere a resposta**: refazer deck e roteiro inteiros por causa de uma ordem errada custa muito mais que essa pausa.

Se o usuário pedir ajustes, atualize o `plano.md` e mostre só o que mudou.

### 6. Roteiro
Com o plano aprovado, carregue a skill `roteiro-apresentacao` e siga-a, passando o `plano.md` e o conteúdo-fonte. Ela produz `roteiro.md` e, pelo script dela, `notas.json`.

O roteiro vem antes do deck de propósito: escrever a fala revela slides que não se sustentam (sem o que dizer) ou que estão densos demais (muito o que dizer). Se isso acontecer, ajuste o plano e avise o usuário em uma linha antes de construir o deck.

### 7. Deck
Carregue a skill `construtor-apresentacoes` e siga-a, passando o `plano.md` (ordem, tipos e textos de tela), as referências de design e os **formatos pedidos**. Quando forem os dois, faça o HTML primeiro e o PowerPoint a partir dele (seção "Versão em PowerPoint" do construtor). Depois grave as notas em cada formato com o script da `roteiro-apresentacao`:

```bash
python <roteiro-apresentacao>/scripts/notas_do_roteiro.py roteiro.md --deck deck.html
python <roteiro-apresentacao>/scripts/notas_do_roteiro.py roteiro.md --pptx deck.pptx
```

### 8. Conferência final
Antes de entregar:
- HTML: `verificar_deck.py` da `construtor-apresentacoes` passa (inclui notas em todos os slides e tecla N).
- PowerPoint: o `validate.py` da skill de PowerPoint passa, os slides renderizados não têm texto cortado nem sobreposto, e o deck parece o mesmo do HTML.
- O script de notas não acusa desalinhamento e a lista lado a lado mostra o mesmo assunto em cada número.
- Se houver números, os que aparecem nos slides são iguais aos citados no roteiro (o plano é a fonte de ambos; confira os que mudaram em ajustes).
- A soma dos tempos do roteiro fecha com a duração pedida (±10%), quando houver duração.

### 9. Entrega
- O **deck** nos formatos pedidos: `.html` (com notas, tecla N) e/ou `.pptx` (texto editável, notas nas anotações do apresentador).
- O **roteiro** como documento editável (conforme a `roteiro-apresentacao`).
- No chat, poucas linhas: quantos slides, duração total, como abrir as notas, e as divergências que o usuário precisa resolver na fonte (se houver).

Não entregue o `plano.md` como produto final, a menos que o usuário peça; ele é ferramenta de trabalho. Mas mantenha-o na pasta de trabalho para ajustes posteriores: quando o usuário pedir uma mudança depois da entrega, altere o plano primeiro e propague para roteiro e deck, para que continuem alinhados.
