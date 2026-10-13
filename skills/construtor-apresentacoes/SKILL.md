---
name: construtor-apresentacoes
description: Gera apresentações de slides em HTML de arquivo único (CSS e JS embutidos), com scroll-snap, navegação por teclado e por pontos, animações escalonadas, notas do apresentador e estética dark-tech premium ou o design enviado pelo usuário, a partir de qualquer conteúdo e assunto (roteiros simples ou de vídeo, tópicos, aulas, palestras, briefs de tema, relatórios executivos); e gera a mesma apresentação em PowerPoint (.pptx) editável, compatível com Canva, quando pedido. Use sempre que o usuário pedir slides, deck, apresentação, "transformar este roteiro/relatório em slides", deck em HTML ou uma versão em PowerPoint para editar no Canva, mesmo sem dizer "HTML", e quando enviar referências de design para uma apresentação. Para Google Slides nativo, não use.
---

# Construtor de Apresentações

Transforma conteúdo bruto de qualquer assunto (roteiro, tópicos, aula, brief, relatório) em um deck HTML pronto para produção, em um único arquivo, que pareça criado por um designer e não gerado.

O deck é sempre escrito em **português do Brasil**, mesmo que o material de entrada esteja em outro idioma (traduza e adapte, não translitere).

## Arquivos da skill

- `assets/template.html` — boilerplate completo: tokens, CSS de todos os tipos de slide, scroll-snap, pontos, teclado, barra de progresso, numeração automática e animações. **Sempre parta dele**; não reescreva a navegação do zero, porque é onde decks gerados à mão costumam quebrar.
- `references/design-system.md` — direção visual padrão (cores, tipografia, fundo, brilho, movimento). Leia antes de desenhar.
- `references/slide-templates.md` — padrão HTML e **limites de conteúdo** de cada tipo de slide (título, citação, grade, comparação, árvore, diagrama, módulos, estatísticas, etapas, screenshot, CTA, divisor, problema/solução, linha do tempo, FAQ, hub). Leia antes de mapear o conteúdo.
- `scripts/verificar_deck.py` — checagem automática do deck final.
- `references/powerpoint.md` — como gerar a versão em PowerPoint (.pptx) editável e compatível com Canva, e `scripts/imagens_decorativas.py`, que gera os fundos e formas decorativas em PNG a partir das cores do design.

## Hierarquia de design

1. **O design que o usuário enviar na conversa sempre vence.** Se ele mandar identidade visual, paleta, fontes, prints ou um deck de referência, extraia dali cores, tipografia, raio de borda, tom e densidade, e reescreva os tokens do `:root` do template para refleti-los — inclusive se for um design claro. Em caso de conflito com `design-system.md`, a referência do usuário prevalece.
   - **Como extrair o design de um .pptx de referência:** descompacte o arquivo e conte as fontes (`typeface=`) e cores (`srgbClr val=`) usadas em `ppt/slides/*.xml`; o tema (`theme1.xml`) costuma ter só valores padrão do Office e engana. Converta o .pptx para PDF (`soffice --headless --convert-to pdf`) e olhe as páginas para entender layout, alternância de fundos, formas decorativas e estilo dos cards. Logos e ícones ficam em `ppt/media/`; embuta em base64 os que forem da marca.
   - Use o design para **forma** (cores, fontes, raios, decoração, ritmo) e o material de conteúdo para os **fatos**. Se o deck de referência tiver textos de exemplo ou números divergentes do conteúdo, não os copie: use os do conteúdo e avise o usuário da divergência na entrega.
   - Para temas claros ou de marca, troque os tokens de superfície do `:root` (`--slide-bg`, `--card-bg`, `--card-border`, `--grid-line`, `--on-accent`) em vez de reescrever as regras de cada componente. Um bloco de CSS de tema adicionado ao fim do `<style>` é o caminho mais limpo; formas decorativas da marca (círculos, anéis) entram como elementos `.deco` posicionados dentro do `.slide`, fora do `.slide-inner`.
2. Sem referência do usuário, use `references/design-system.md` (dark-tech premium) como está.
3. O que nunca muda, qualquer que seja o design: as regras estruturais abaixo (100vh, navegação, numeração, arquivo único) e a qualidade editorial (um ponto focal por slide, nada genérico).

Por que essa ordem: a skill existe para servir à marca de quem pede. O dark-tech é um padrão bem resolvido, não uma imposição.

## Processo

### 1. Analise o input
Leia todo o material e extraia: a narrativa central (qual história o deck conta), as seções, as transições entre ideias e os elementos-chave (listas, comparações, citações fortes, etapas, números, visuais). Num roteiro de vídeo, ignore marcações de câmera/edição e fique com o que é dito e mostrado. Num relatório executivo, priorize conclusões e números sobre o texto de apoio. Num roteiro simples ou numa aula, sem dados, cada slide carrega uma ideia com uma frase forte, poucos itens, um ícone ou uma imagem; não invente números para preencher Estatísticas.

### 2. Monte o roteiro de slides
**Se você recebeu um plano de slides** (por exemplo, do `assistente-apresentacoes`), ele é a fonte da verdade: siga a ordem, a quantidade, o tipo e a mensagem de cada slide exatamente como estão, porque o roteiro de fala foi escrito sobre essa mesma numeração. Você ainda decide o desenho e a microcopy de cada slide. Se um slide do plano não couber numa tela, não divida por conta própria: avise quem pediu, porque dividir desalinha o roteiro.

Sem plano, antes de escrever HTML, faça mentalmente (ou em rascunho) a lista ordenada: `nº — tipo — conteúdo resumido`. Use o "Guia Final de Seleção" de `slide-templates.md`. Mapeamento rápido:

- abertura → Título · afirmação forte → Citação · vários itens curtos → Grade · antes/depois → Comparação · dor e resposta → Problema/Solução · processo → Etapas · cronologia → Linha do tempo · sistema conectado → Diagrama ou Hub · números → Estatísticas · imagem de UI → Screenshot · mudança de capítulo → Divisor · objeções → FAQ · fechamento → CTA

Respeite os limites de palavras e itens de cada tipo. Quando o conteúdo não couber, **divida em dois slides** ou condense o texto — nunca encolha a fonte para caber. Reescreva frases longas em microcopy forte; o slide não é o roteiro, é o apoio visual dele.

Varie os tipos: um deck com seis grades de cards seguidas parece gerado. Alterne densidade (slide denso → declaração respirada) para criar ritmo.

### 3. Imagens
Se o usuário anexar imagens (screenshots, logos, fotos), **embuta-as em base64** (`src="data:image/png;base64,..."`) para o arquivo continuar único e funcionar em qualquer lugar. Converta com script (ex.: `base64 -w0 arquivo.png`), não à mão. Cada screenshot ganha seu próprio slide. Se uma imagem for muito grande (> ~1,5 MB), reduza antes com Pillow mantendo a legibilidade. Sem imagens anexadas, não invente screenshots — use outro tipo de slide.

### 4. Construa o HTML
- Copie `assets/template.html`, preencha `<title>` e substitua o comentário `{{SLIDES}}` pelos `<section class="slide ...">`.
- Use as classes e estruturas de `slide-templates.md`. Pode criar classes novas quando o conteúdo pedir, sempre usando os tokens CSS.
- Deixe `<div class="slide-counter"></div>` vazio: o script do template numera `NN / TOTAL` automaticamente, o que evita erro de contagem quando você adiciona ou divide slides.
- No slide de Hub, deixe `<svg class="hub-connections"></svg>` vazio: o template desenha as linhas do nó central até cada nó periférico, sempre alinhadas em qualquer tamanho de tela.
- Valores em `.stat-value` nunca quebram linha; o template reduz a fonte até caber. Mesmo assim, prefira métricas curtas ("R$ 48,2 mi", não "R$ 48.200.000,00").
- Dê ênfase a 1–3 palavras por título com `<span class="hl">` (ou `hl-2` / `hl-glow`).
- Use `.animate delay-N` em sequência dentro de cada slide para a revelação escalonada.
- **Notas do apresentador:** quando houver roteiro ou notas, coloque em cada slide, como último filho do `<section>`, um `<aside class="notes">` com o conteúdo curto da nota (tempo, tópicos, fala). O template mostra essas notas num painel ao apertar **N** e esconde da plateia. Se um slide tem nota, todos devem ter.
- Fontes via Google Fonts, como no template (se o design do usuário pedir outras, troque o `<link>` e as variáveis `--font-*`).

### 5. Verifique
Rode:

```bash
python scripts/verificar_deck.py caminho/deck.html --screenshots /tmp/deck-shots
```

O script testa em 1440×900 e 1280×720: overflow de cada slide, contador, pontos sincronizados, teclado, animações, scroll-snap, imagens embutidas, fontes e, se houver, as notas do apresentador. Corrija tudo o que falhar e rode de novo. Depois **olhe os screenshots** de alguns slides (ao menos título, um denso e o CTA): o script pega erros mecânicos, mas não detecta um slide feio, desbalanceado ou genérico. Use a "Heurística Rápida" do `design-system.md` nessa revisão.

Se não houver Playwright no ambiente, faça a checagem manual da lista: tudo cabe em 100vh, sem rolagem interna, screenshots isolados, pontos e teclado funcionam, animações disparam, numeração correta, fontes carregadas.

### 6. Versão em PowerPoint (quando pedida)
Se o usuário pedir PowerPoint, .pptx ou um arquivo para editar no Canva, gere-o **depois** do HTML aprovado, seguindo `references/powerpoint.md`. O HTML é a referência visual: o .pptx repete os mesmos slides, textos, números e design, só que em formas e caixas de texto editáveis. Se só o PowerPoint for pedido, ainda assim decida o desenho de cada slide como faria no HTML (tipos, limites de conteúdo, hierarquia) e pule o arquivo .html.

## Regras inegociáveis

1. Um slide = uma viewport (`100vh`), sem rolagem interna. Conteúdo a mais vira outro slide.
2. Screenshot sempre em slide próprio.
3. Um único arquivo `.html`, com CSS e JS embutidos e imagens em base64.
4. Scroll-snap, navegação por teclado (setas, PageUp/PageDown, espaço, Home/End) e navegação por pontos sincronizada.
5. Animações suaves e escalonadas (0,5–0,8 s, ease-out), respeitando `prefers-reduced-motion`.
6. Numeração `NN / TOTAL` em todos os slides.
7. Nada de visual genérico: fontes padrão do navegador, Inter/Roboto/Arial, gradiente azul "de IA", slides lotados ou ênfase em tudo.

## Entrega

Quando houver versão em PowerPoint, entregue o `.pptx` com o mesmo nome base do `.html`.

Salve o deck como arquivo `.html` com nome descritivo em minúsculas e hífens (ex.: `lancamento-agentes-ia.html`) e entregue o arquivo ao usuário. Não cole o HTML no chat nem explique o código — no máximo uma linha dizendo quantos slides o deck tem e como navegar (setas ou pontos à direita; tecla N para as notas, quando houver).
