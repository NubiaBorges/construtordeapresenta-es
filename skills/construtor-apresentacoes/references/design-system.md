# design-system.md

Referência de design para apresentações de slides em HTML.
Use este arquivo como direção visual, não como um template rígido.
O objetivo é criar apresentações com uma estética dark-tech premium,
hierarquia forte, acentos neon e alto contraste.

---

## 1) Intenção de Design

Este estilo de apresentação deve transmitir:

- tecnologia
- premium
- precisão
- modernidade
- leve futurismo
- alto contraste
- intenção visual, nunca algo genérico

Evite:
- aparência genérica de “gradiente azul de IA”
- visuais planos de startup SaaS
- tipografia padrão do navegador
- contraste fraco
- slides cheios demais
- muitas cores de destaque ao mesmo tempo

A apresentação deve parecer um lançamento de produto / treinamento premium / showcase avançado de sistemas de IA.

---

## 2) DNA Visual Central

### Palavras-chave estéticas
- sala de controle escura
- laboratório neon
- dashboard premium
- educação futurista
- revelação de produto high-end

### Princípios visuais
- fundos escuros em primeiro lugar
- destaques brilhantes em palavras-chave, bordas, contadores e detalhes de UI
- títulos fortes e marcantes
- fonte mono apenas para contadores, labels, tags e pequenos metadados
- layouts espaçosos com vazio intencional
- cards devem parecer luminosos e premium, não planos

---

## 3) Sistema de Cores

Use apenas propriedades customizadas CSS.

```css
:root {
  --bg: #1C1B20;
  --bg-soft: #23222A;
  --surface: #2A2933;
  --surface-2: #312F3D;
  --text: #F5F7FB;
  --text-soft: #B8BCC8;
  --line: rgba(255,255,255,0.10);

  --accent: #28C2C4;
  --accent-2: #B0AFFA;
  --accent-3: #7BE7E8;

  --success: #6EE7B7;
  --warning: #F6C177;
  --danger: #FF7B9C;

  --shadow-soft: 0 10px 30px rgba(0,0,0,0.25);
  --shadow-glow: 0 0 0 1px rgba(40,194,196,0.16), 0 0 32px rgba(40,194,196,0.12);
}
```

### Regras de uso
- `--bg` é o fundo principal do slide
- `--surface` e `--surface-2` são usados para cards, painéis, diagramas e blocos de estatísticas
- `--accent` é o destaque principal
- `--accent-2` é usado como brilho de apoio / ênfase secundária
- use `--accent-3` com moderação para gradientes mais ricos ou destaques em camadas
- nunca use mais de 2 cores de destaque como dominantes no mesmo slide

### Equilíbrio de cores
Distribuição recomendada:
- 70% fundo/superfícies escuras
- 20% texto e linhas neutras
- 10% cor de destaque

---

## 4) Estilo de Fundo

Os fundos nunca devem ser preto puro.
Use superfícies escuras em camadas com brilho radial sutil.

Tratamento de fundo preferido:

```css
background:
  radial-gradient(circle at 20% 20%, rgba(176,175,250,0.10), transparent 30%),
  radial-gradient(circle at 80% 30%, rgba(40,194,196,0.10), transparent 28%),
  linear-gradient(180deg, #1C1B20 0%, #17161B 100%);
```

Opcional:
- textura de grade discreta
- ruído muito sutil
- brilho suave atrás do título hero ou diagrama principal

Não faça:
- usar ilustrações carregadas como fundo completo
- usar gradientes fortes que reduzem a legibilidade
- usar glassmorphism em tudo

---

## 5) Tipografia

### Combinação de fontes
Use uma fonte display para títulos e uma fonte mono para contadores/metadados.

Combinações recomendadas:
- Chakra Petch + JetBrains Mono
- Space Grotesk + JetBrains Mono
- Sora + IBM Plex Mono
- Outfit + Fira Code

### Combinação padrão preferida
- Títulos: `Chakra Petch`
- Corpo/UI: `Chakra Petch` ou `Space Grotesk`
- Labels/Contadores/Código: `JetBrains Mono`

### Carregamento de fontes
Exemplo:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
```

### Regras de tipografia
- títulos devem parecer fortes e levemente condensados
- corpo de texto deve permanecer altamente legível
- mono é reservado para:
  - números dos slides
  - tags
  - micro labels
  - métricas
  - detalhes de UI com aparência de código

Evite:
- Inter
- Roboto
- Arial
- fontes semelhantes a Times
- misturar mais de 2 famílias de fontes

---

## 6) Escala Tipográfica

Use clamp sempre que possível.

```css
--fs-display: clamp(56px, 7vw, 96px);
--fs-h1: clamp(40px, 5vw, 72px);
--fs-h2: clamp(28px, 3.6vw, 48px);
--fs-h3: clamp(22px, 2.4vw, 32px);
--fs-body-lg: clamp(18px, 1.5vw, 24px);
--fs-body: 18px;
--fs-small: 14px;
--fs-mono: 13px;
```

### Hierarquia
- slides hero/título: tamanho display bem grande
- slides de conteúdo: título grande + corpo contido
- labels/tags/metadados de estatísticas: sensação mono em small caps
- evite parágrafos longos; quebre o conteúdo em blocos

---

## 7) Princípios de Layout

### Grade
Use espaçamento interno consistente.
Padding recomendado para slides:

```css
padding: 56px 64px;
```

Estrutura desktop recomendada:
- lógica visual de 12 colunas
- layouts comparativos em 2 colunas
- layouts hero assimétricos são incentivados
- use espaços generosos entre blocos

### Alinhamento
- prefira texto alinhado à esquerda
- centralize apenas slides de título, citação e encerramento
- mantenha ritmo vertical forte
- cada slide deve ter um ponto focal dominante

### Densidade
Um slide deve parecer editorial, não lotado.
Se o conteúdo parecer apertado, divida em dois slides.

---

## 8) Estilo de Componentes

### Cards
Cards devem parecer premium e suavemente iluminados.

```css
.card {
  background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  box-shadow: var(--shadow-soft);
}
```

Card destacado opcional:

```css
.card--accent {
  border-color: rgba(40,194,196,0.30);
  box-shadow: var(--shadow-glow);
}
```

### Pills / tags
- totalmente arredondados
- fonte mono
- compactos
- borda sutil
- destaque apenas quando fizer sentido

### Linhas / divisores
- finos
- baixa opacidade
- usados para organizar, nunca dominar

### Botões / blocos de CTA
- fundo preenchido com a cor de destaque para CTA primário
- variante outline/glow para CTA secundário
- grandes o suficiente para leitura à distância

---

## 9) Tratamento de Títulos

Títulos devem frequentemente incluir ênfase em 1–3 palavras.

Estilos de ênfase permitidos:
- cor de destaque
- sublinhado com brilho sutil
- palavra-chave em caixa
- composição em linhas separadas

Exemplo:
- título neutro + palavra-chave destacada
- heading branco com palavra em ciano
- eyebrow roxo + heading branco + metadado mono

Não faça:
- texto arco-íris
- palavras demais enfatizadas
- efeitos de texto excessivamente decorativos

---

## 10) Estilo de Dados / Estatísticas

Para slides com números:
- número muito grande
- label curto
- frase de apoio opcional
- micro label mono acima ou abaixo

Estrutura de exemplo:
- pequeno label mono
- métrica gigante
- explicação em uma linha

Estatísticas podem usar:
- borda com destaque
- brilho sutil
- painéis divididos
- 2 a 4 métricas no máximo por slide

---

## 11) Slides de Diagrama / Sistema

Diagramas devem parecer arquitetura de produto, não gráficos de sala de aula.

Use:
- blocos arredondados
- linhas conectoras com acento em baixa opacidade
- superfícies em camadas
- labels contidos
- tags mono para termos técnicos

Sensação preferida:
- mapa de sistema limpo
- fluxo elegante
- arquitetura modular

Evite:
- setas bagunçadas por todos os lados
- cores demais
- aparência padrão de fluxograma

---

## 12) Slides de Screenshot

Screenshots recebem prioridade visual total.
Use:
- um screenshot por slide sempre que possível
- container emoldurado com borda suave
- label opcional acima
- legenda apenas se necessário

Sugestão de moldura para screenshot:

```css
.screenshot-frame {
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.10);
  box-shadow: 0 20px 60px rgba(0,0,0,0.35);
}
```

Adicione brilho externo discreto apenas se isso ajudar o slide.

---

## 13) Movimento

A animação deve parecer refinada e calma.

Use:
- fade-up
- leve scale-in
- revelação escalonada
- transições suaves de opacidade

Evite:
- movimento elástico
- elementos girando
- parallax exagerado
- transições chamativas demais

Tempo recomendado:
- 0,5s a 0,8s
- ease-out
- escalonamento de 80ms a 140ms

Exemplo:

```css
.animate {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
.animate.in {
  opacity: 1;
  transform: translateY(0);
}
```

---

## 14) Border Radius

Use cantos arredondados de forma generosa, mas consistente.

Escala sugerida:
- pequenos elementos de UI: 12px
- cards: 20px a 24px
- molduras grandes/screenshots: 24px a 28px
- pills/tags: 999px

Evite misturar valores demais de radius.

---

## 15) Sombras e Brilho

Use sombras para separar camadas.
Use brilho para enfatizar importância.

Regras:
- sombras são suaves, escuras e difusas
- brilho é sutil, nunca dominante
- brilho ciano para ênfase principal
- brilho roxo para atmosfera secundária

Bons casos de uso:
- palavra-chave hero
- card ativo
- CTA
- métrica destacada
- nó selecionado em diagrama

---

## 16) Tom do Conteúdo na UI

O texto dentro dos slides deve apoiar visualmente o tom da marca:
- direto
- premium
- confiante
- técnico sem ser frio

Padrões preferidos de microcopy:
- labels curtos
- afirmações fortes
- linhas de apoio concisas
- mínimo texto de enchimento

---

## 17) Direção Visual por Tipo de Slide

### Slide de título
- headline oversized
- brilho ou badge de destaque
- alto contraste
- no máximo uma frase de apoio

### Slide de citação/declaração
- declaração enorme
- distrações mínimas
- uma frase destacada

### Grade de conteúdo
- 3 a 6 cards no máximo
- ritmo visual equilibrado
- cada card com título curto + descrição curta

### Comparação
- layout dividido forte
- um lado suavizado, outro enfatizado
- use contraste para tornar a diferença óbvia

### Estatísticas/resultados
- números gigantes
- texto mínimo
- ritmo visual forte

### Etapas
- sequência numerada com contadores mono
- lógica de conexão ou ritmo vertical
- 3 a 5 etapas no máximo

### CTA/encerramento
- mensagem final forte
- área limpa para botão/link
- confiança visual, sem poluição

---

## 18) Regras de Implementação

- Sempre use variáveis CSS
- Prefira classes utilitárias reutilizáveis para espaçamento e ênfase
- Evite estilos inline, exceto quando forem dinâmicos
- Nunca deixe efeitos decorativos reduzirem a legibilidade
- O contraste deve permanecer forte em todos os slides
- Todo slide deve parecer consistente com o mesmo sistema visual

---

## 19) Heurística Rápida

Antes de finalizar um slide, verifique:

- Ele parece premium?
- Existe um ponto focal claro?
- A cor de destaque está sendo usada com intenção?
- A tipografia está forte o suficiente?
- Ele evita estética genérica de IA?
- Ele se encaixaria visualmente no lançamento de um curso avançado de IA?

Se qualquer resposta for “não”, simplifique e reestilize.
