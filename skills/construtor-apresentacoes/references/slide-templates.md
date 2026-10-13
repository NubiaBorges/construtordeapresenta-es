# slide-templates.md

Padrões HTML para cada tipo de slide.
Use estes padrões como estruturas-base para criar apresentações de slides HTML em arquivo único.
Adapte o conteúdo e os nomes de classes conforme necessário, mas preserve a lógica estrutural e os limites de conteúdo.

Use este arquivo junto com:
- `references/design-system.md` para direção visual
- `assets/template.html` para o boilerplate da apresentação
- as regras da skill de apresentação para ajuste à viewport, navegação e animação

---

## Regras Globais

- Todo slide deve caber em `100vh`
- Nunca permita overflow vertical dentro de um slide
- Se o conteúdo não couber, divida em vários slides
- Prefira textos curtos e escaneáveis em vez de parágrafos
- Screenshots normalmente devem ter seu próprio slide dedicado
- Cada slide deve usar o wrapper `.slide`
- Use as classes `.animate` e `.delay-N` para revelações escalonadas
- Respeite o formato do contador de slides `NN / TOTAL`
- Use HTML semântico sempre que possível (`section`, `article`, `blockquote`, `figure`, `ol`, `ul`)

---

## Estrutura Comum

Use este padrão como wrapper base para a maioria dos slides.

```html
<section class="slide">
  <div class="slide-inner">
    <div class="slide-counter">01 / 10</div>

    <div class="slide-content">
      <!-- conteúdo do slide aqui -->
    </div>
  </div>
</section>
```

### Observações
- `slide-inner` deve controlar o padding e os limites do layout
- `slide-counter` fica no canto superior direito
- `slide-content` contém o layout real daquele slide
- Adicione classes específicas do tipo de slide ao elemento `<section>`, por exemplo:
  - `title-slide`
  - `grid-slide`
  - `stats-slide`

---

## 1. Slide de Título

### Use para
- gancho de abertura
- título da apresentação
- início de seção importante

### Limites de conteúdo
- Eyebrow: máximo de 4 palavras
- Título: máximo de 10 palavras
- Subtítulo: máximo de 20 palavras
- Badge/tag opcional: apenas 1

### Padrão

```html
<section class="slide title-slide">
  <div class="slide-inner">
    <div class="slide-counter">01 / 10</div>

    <div class="hero">
      <div class="eyebrow mono animate delay-1">SISTEMAS DE IA</div>
      <h1 class="animate delay-2">Crie Workflows de Agentes Mais Inteligentes</h1>
      <p class="subtitle animate delay-3">
        Um framework prático para sistemas de automação mais rápidos e limpos.
      </p>
    </div>
  </div>
</section>
```

### Observações
- Mantenha este slide visualmente forte e minimalista
- Evite múltiplos parágrafos
- Apenas um ponto focal dominante

---

## 2. Slide de Citação / Declaração

### Use para
- afirmação forte
- tese
- takeaway memorável
- frase de impacto emocional

### Limites de conteúdo
- Declaração principal: máximo de 20 palavras
- Atribuição: opcional, máximo de 4 palavras

### Padrão

```html
<section class="slide quote-slide">
  <div class="slide-inner">
    <div class="slide-counter">02 / 10</div>

    <blockquote class="statement animate delay-1">
      O melhor workflow de IA é aquele que as pessoas realmente usam.
    </blockquote>

    <div class="quote-meta mono animate delay-2">Princípio central</div>
  </div>
</section>
```

### Observações
- Use uma declaração muito grande
- Mantenha distrações mínimas
- Destaque 1 frase-chave se necessário

---

## 3. Grade de Conteúdo (Cards)

### Use para
- funcionalidades
- benefícios
- múltiplos itens com descrições curtas
- pontos categorizados

### Limites de conteúdo
- 3 a 6 cards
- Título do card: máximo de 5 palavras
- Descrição do card: máximo de 14 palavras
- Ícone/label opcional: 1 por card

### Padrão

```html
<section class="slide grid-slide">
  <div class="slide-inner">
    <div class="slide-counter">03 / 10</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">FUNCIONALIDADES</div>
      <h2 class="animate delay-2">O que este sistema inclui</h2>
    </div>

    <div class="card-grid cols-3">
      <article class="card animate delay-1">
        <div class="card-label mono">01</div>
        <h3>Configuração rápida</h3>
        <p>Comece com uma base reutilizável em vez de um arquivo em branco.</p>
      </article>

      <article class="card animate delay-2">
        <div class="card-label mono">02</div>
        <h3>Estrutura clara</h3>
        <p>Cada tipo de slide tem um padrão explícito e limite de conteúdo.</p>
      </article>

      <article class="card animate delay-3">
        <div class="card-label mono">03</div>
        <h3>Mais consistência</h3>
        <p>Design e HTML permanecem alinhados em todo o deck.</p>
      </article>
    </div>
  </div>
</section>
```

### Observações
- Use 2, 3 ou 4 colunas dependendo da densidade
- Evite textos longos nos cards
- Se os cards ficarem apertados, reduza a quantidade ou divida em slides

---

## 4. Slide de Comparação (Duas Colunas)

### Use para
- antes vs depois
- antigo vs novo
- manual vs automatizado
- opção A vs opção B
- prós vs contras

### Limites de conteúdo
- apenas 2 colunas
- Título da coluna: máximo de 4 palavras
- Máximo de 5 bullets por coluna
- Cada bullet: máximo de 8 palavras

### Padrão

```html
<section class="slide comparison-slide">
  <div class="slide-inner">
    <div class="slide-counter">04 / 10</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">MUDANÇA</div>
      <h2 class="animate delay-2">Do trabalho manual aos workflows com agentes</h2>
    </div>

    <div class="comparison-grid">
      <div class="comparison-col muted animate delay-1">
        <h3>Antes</h3>
        <ul>
          <li>Copiar prompts manualmente</li>
          <li>Reconstruir layouts sempre</li>
          <li>Estrutura inconsistente</li>
          <li>Muita variação visual</li>
        </ul>
      </div>

      <div class="comparison-col accent animate delay-2">
        <h3>Depois</h3>
        <ul>
          <li>Padrões HTML reutilizáveis</li>
          <li>Limites de conteúdo definidos</li>
          <li>Consistência visual mais forte</li>
          <li>Output de apresentação mais rápido</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

### Observações
- Um lado pode ser visualmente suavizado, o outro enfatizado
- Mantenha os dois lados equilibrados em altura
- Evite parágrafos dentro das colunas

---

## 5. Slide de Árvore / Estrutura

### Use para
- hierarquias de arquivos
- estruturas de pastas
- camadas de sistema
- relações aninhadas

### Limites de conteúdo
- Máximo de 3 níveis de profundidade
- Máximo de 10 nós visíveis no total
- Labels: máximo de 5 palavras cada

### Padrão

```html
<section class="slide structure-slide">
  <div class="slide-inner">
    <div class="slide-counter">05 / 10</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">ESTRUTURA</div>
      <h2 class="animate delay-2">Arquivos de referência e responsabilidades</h2>
    </div>

    <div class="tree animate delay-3">
      <div class="tree-node root">references/</div>

      <div class="tree-children">
        <div class="tree-branch">
          <div class="tree-node">design-system.md</div>
          <div class="tree-note mono">direção visual</div>
        </div>

        <div class="tree-branch">
          <div class="tree-node">slide-templates.md</div>
          <div class="tree-note mono">padrões HTML</div>
        </div>

        <div class="tree-branch">
          <div class="tree-node">template.html</div>
          <div class="tree-note mono">estrutura base</div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Observações
- Prefira agrupamentos limpos e elegantes em vez de árvores literais de sistema operacional
- Mantenha labels curtos
- Use conectores de forma leve

---

## 6. Slide de Diagrama

### Use para
- workflows
- sistemas com partes conectadas
- arquitetura
- mapas de processo
- diagramas de relacionamento

### Limites de conteúdo
- Máximo de 6 nós
- Título do nó: máximo de 4 palavras
- Nota do nó: máximo de 10 palavras
- Mantenha conexões simples e legíveis

### Padrão

```html
<section class="slide diagram-slide">
  <div class="slide-inner">
    <div class="slide-counter">06 / 10</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">WORKFLOW</div>
      <h2 class="animate delay-2">Como o builder cria uma apresentação</h2>
    </div>

    <div class="diagram">
      <div class="diagram-node animate delay-1">
        <h3>Input</h3>
        <p>Roteiro, outline ou brief</p>
      </div>

      <div class="diagram-node animate delay-2">
        <h3>Mapeamento</h3>
        <p>Escolha os tipos de slide</p>
      </div>

      <div class="diagram-node animate delay-3">
        <h3>Design</h3>
        <p>Aplique o sistema visual</p>
      </div>

      <div class="diagram-node animate delay-4">
        <h3>Output</h3>
        <p>Deck HTML em arquivo único</p>
      </div>
    </div>
  </div>
</section>
```

### Observações
- Deve parecer arquitetura de produto, não gráfico de sala de aula
- Use espaçamento e alinhamento para sugerir fluxo
- Evite setas emaranhadas

---

## 7. Slide de Plugins / Cards de Funcionalidades

### Use para
- ferramentas
- plugins
- módulos
- capacidades
- componentes de um sistema

### Limites de conteúdo
- 3 a 5 cards de funcionalidades
- Nome da funcionalidade: máximo de 4 palavras
- Descrição: máximo de 12 palavras
- Status/tag opcional: 1 por card

### Padrão

```html
<section class="slide feature-slide">
  <div class="slide-inner">
    <div class="slide-counter">07 / 10</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">MÓDULOS</div>
      <h2 class="animate delay-2">Blocos centrais do sistema</h2>
    </div>

    <div class="feature-grid cols-3">
      <article class="feature-card animate delay-1">
        <div class="feature-tag mono">INPUT</div>
        <h3>Analisador</h3>
        <p>Interpreta a história e as principais transições.</p>
      </article>

      <article class="feature-card animate delay-2">
        <div class="feature-tag mono">LAYOUT</div>
        <h3>Mapeador</h3>
        <p>Atribui cada ideia ao tipo certo de slide.</p>
      </article>

      <article class="feature-card animate delay-3">
        <div class="feature-tag mono">OUTPUT</div>
        <h3>Builder</h3>
        <p>Cria HTML refinado com animação e navegação.</p>
      </article>
    </div>
  </div>
</section>
```

### Observações
- Semelhante à grade de conteúdo, mas com enquadramento mais de produto/módulo
- Tags funcionam bem aqui
- As descrições devem permanecer curtas

---

## 8. Slide de Estatísticas / Resultados

### Use para
- métricas
- KPIs
- melhorias de performance
- resultados
- prova numérica

### Limites de conteúdo
- 1 métrica hero OU 2 a 4 métricas menores
- Label da métrica: máximo de 4 palavras
- Linha de apoio: máximo de 10 palavras

### Padrão A: Métrica Hero

```html
<section class="slide stats-slide hero-stat">
  <div class="slide-inner">
    <div class="slide-counter">08 / 10</div>

    <div class="stat-block">
      <div class="stat-label mono animate delay-1">TEMPO ECONOMIZADO</div>
      <div class="stat-value animate delay-2">72%</div>
      <p class="stat-note animate delay-3">Menos trabalho de formatação por deck.</p>
    </div>
  </div>
</section>
```

### Padrão B: Grade Multiestatística

```html
<section class="slide stats-slide">
  <div class="slide-inner">
    <div class="slide-counter">08 / 10</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">RESULTADOS</div>
      <h2 class="animate delay-2">O que melhorou</h2>
    </div>

    <div class="stats-grid cols-3">
      <div class="stat-card animate delay-1">
        <div class="stat-value">3x</div>
        <div class="stat-label mono">VELOCIDADE</div>
      </div>

      <div class="stat-card animate delay-2">
        <div class="stat-value">10</div>
        <div class="stat-label mono">TIPOS DE SLIDE</div>
      </div>

      <div class="stat-card animate delay-3">
        <div class="stat-value">100vh</div>
        <div class="stat-label mono">AJUSTE À VIEWPORT</div>
      </div>
    </div>
  </div>
</section>
```

### Observações
- Use números muito grandes
- Mantenha o texto explicativo mínimo
- Não sobrecarregue com métricas demais

---

## 9. Slide de Etapas / Lista Numerada

### Use para
- instruções sequenciais
- slides de como fazer
- workflows passo a passo
- ordem de implementação

### Limites de conteúdo
- 3 a 5 etapas
- Título da etapa: máximo de 4 palavras
- Corpo da etapa: máximo de 10 palavras

### Padrão

```html
<section class="slide steps-slide">
  <div class="slide-inner">
    <div class="slide-counter">09 / 10</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">PROCESSO</div>
      <h2 class="animate delay-2">Construa o deck em quatro etapas</h2>
    </div>

    <ol class="steps-list">
      <li class="step animate delay-1">
        <div class="step-num mono">01</div>
        <div class="step-copy">
          <h3>Analise o input</h3>
          <p>Encontre a narrativa e as seções principais.</p>
        </div>
      </li>

      <li class="step animate delay-2">
        <div class="step-num mono">02</div>
        <div class="step-copy">
          <h3>Mapeie slides</h3>
          <p>Escolha o melhor padrão por bloco de conteúdo.</p>
        </div>
      </li>

      <li class="step animate delay-3">
        <div class="step-num mono">03</div>
        <div class="step-copy">
          <h3>Aplique design</h3>
          <p>Use tokens, hierarquia e regras de espaçamento.</p>
        </div>
      </li>

      <li class="step animate delay-4">
        <div class="step-num mono">04</div>
        <div class="step-copy">
          <h3>Verifique ajuste</h3>
          <p>Divida qualquer conteúdo que exceda uma viewport.</p>
        </div>
      </li>
    </ol>
  </div>
</section>
```

### Observações
- As etapas devem parecer rítmicas e fáceis de escanear
- Use contadores mono de forma consistente
- Se o texto ficar longo, divida em dois slides

---

## 10. Slide de Showcase de Screenshot

### Use para
- evidência de UI
- screenshots de produto
- showcase de página web
- walkthroughs de interface
- prova visual

### Limites de conteúdo
- Prefira 1 screenshot por slide
- Título: opcional, máximo de 6 palavras
- Legenda: opcional, máximo de 12 palavras

### Padrão A: Screenshot Completo

```html
<section class="slide screenshot-slide">
  <div class="slide-inner">
    <div class="slide-counter">10 / 10</div>

    <div class="section-heading compact">
      <div class="eyebrow mono animate delay-1">SHOWCASE</div>
      <h2 class="animate delay-2">Referência de landing page</h2>
    </div>

    <figure class="screenshot-frame animate delay-3">
      <img src="assets/reference-shot.jpg" alt="Screenshot da landing page" />
    </figure>
  </div>
</section>
```

### Padrão B: Screenshot com Legenda

```html
<section class="slide screenshot-slide">
  <div class="slide-inner">
    <div class="slide-counter">10 / 10</div>

    <figure class="screenshot-frame animate delay-1">
      <img src="assets/ui-example.jpg" alt="Showcase de UI" />
    </figure>

    <figcaption class="screenshot-caption mono animate delay-2">
      Contraste forte, acentos luminosos e superfícies premium em cards.
    </figcaption>
  </div>
</section>
```

### Observações
- Dê aos screenshots bastante respiro visual
- Não misture visuais pesados de screenshot com texto denso
- Use moldura ou container para refinamento

---

## 11. Slide de CTA / Encerramento

### Use para
- pitch final
- próximo passo
- links
- inscrever-se / entrar / contato
- mensagem de encerramento

### Limites de conteúdo
- Mensagem principal: máximo de 10 palavras
- Linha de apoio: máximo de 16 palavras
- 1 CTA primário
- 1 link secundário no máximo

### Padrão

```html
<section class="slide closing-slide">
  <div class="slide-inner">
    <div class="slide-counter">11 / 11</div>

    <div class="closing-content">
      <div class="eyebrow mono animate delay-1">PRÓXIMO PASSO</div>
      <h2 class="animate delay-2">Crie seu primeiro deck refinado hoje</h2>
      <p class="subtitle animate delay-3">
        Comece com o template, depois personalize a história e os visuais.
      </p>

      <div class="cta-row animate delay-4">
        <a href="#" class="btn btn-primary">Começar</a>
        <a href="#" class="btn btn-secondary">Ver referência</a>
      </div>
    </div>
  </div>
</section>
```

### Observações
- Mantenha o encerramento confiante e limpo
- Evite poluir com links demais
- Uma ação clara costuma ser melhor

---

## 12. Slide Divisor de Seção

### Use para
- quebra de capítulo
- transição importante
- introdução de nova seção

### Limites de conteúdo
- Eyebrow: máximo de 3 palavras
- Título da seção: máximo de 6 palavras
- Linha opcional: máximo de 10 palavras

### Padrão

```html
<section class="slide divider-slide">
  <div class="slide-inner">
    <div class="slide-counter">05 / 12</div>

    <div class="divider-content">
      <div class="eyebrow mono animate delay-1">SEÇÃO 02</div>
      <h2 class="animate delay-2">Sistema de Design</h2>
      <p class="subtitle animate delay-3">As regras visuais por trás do deck.</p>
    </div>
  </div>
</section>
```

### Observações
- Deve parecer mais leve que um slide de título
- Útil para decks longos
- Mantenha o texto mínimo

---

## 13. Slide de Problema / Solução

### Use para
- enquadramento de dor
- desafio e resposta
- por que isso importa

### Limites de conteúdo
- 2 painéis
- Título do problema: máximo de 4 palavras
- Título da solução: máximo de 4 palavras
- 3 bullets no máximo por painel

### Padrão

```html
<section class="slide problem-solution-slide">
  <div class="slide-inner">
    <div class="slide-counter">06 / 12</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">POR QUE EXISTE</div>
      <h2 class="animate delay-2">A lacuna que este sistema resolve</h2>
    </div>

    <div class="comparison-grid">
      <div class="comparison-col muted animate delay-1">
        <h3>Problema</h3>
        <ul>
          <li>Decks criados do zero</li>
          <li>Padrões HTML inconsistentes</li>
          <li>Overflow de conteúdo excessivo</li>
        </ul>
      </div>

      <div class="comparison-col accent animate delay-2">
        <h3>Solução</h3>
        <ul>
          <li>Templates de slide reutilizáveis</li>
          <li>Limites de conteúdo definidos</li>
          <li>Output estruturado mais rápido</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

---

## 14. Slide de Linha do Tempo

### Use para
- roadmap
- cronologia
- lançamento em fases
- sequência histórica

### Limites de conteúdo
- 3 a 5 pontos na linha do tempo
- Título do ponto: máximo de 4 palavras
- Descrição do ponto: máximo de 8 palavras

### Padrão

```html
<section class="slide timeline-slide">
  <div class="slide-inner">
    <div class="slide-counter">07 / 12</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">ROADMAP</div>
      <h2 class="animate delay-2">Como a skill evolui</h2>
    </div>

    <div class="timeline">
      <div class="timeline-item animate delay-1">
        <div class="timeline-dot"></div>
        <div class="timeline-copy">
          <div class="mono">FASE 01</div>
          <h3>Motor de slides</h3>
          <p>HTML base e navegação.</p>
        </div>
      </div>

      <div class="timeline-item animate delay-2">
        <div class="timeline-dot"></div>
        <div class="timeline-copy">
          <div class="mono">FASE 02</div>
          <h3>Tokens de design</h3>
          <p>Sistema visual alinhado à marca.</p>
        </div>
      </div>

      <div class="timeline-item animate delay-3">
        <div class="timeline-dot"></div>
        <div class="timeline-copy">
          <div class="mono">FASE 03</div>
          <h3>Mapeamento inteligente</h3>
          <p>Melhores escolhas de conteúdo para layout.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Observações
- Mantenha ritmo uniforme entre os itens
- Não sobrecarregue com datas ou parágrafos demais

---

## 15. Slide de FAQ / Perguntas e Respostas Curtas

### Use para
- objeções previstas
- FAQs
- esclarecimentos concisos

### Limites de conteúdo
- 3 a 4 blocos de P&R
- Pergunta: máximo de 8 palavras
- Resposta: máximo de 14 palavras

### Padrão

```html
<section class="slide faq-slide">
  <div class="slide-inner">
    <div class="slide-counter">08 / 12</div>

    <div class="section-heading">
      <div class="eyebrow mono animate delay-1">FAQ</div>
      <h2 class="animate delay-2">Perguntas comuns</h2>
    </div>

    <div class="faq-list">
      <article class="faq-item animate delay-1">
        <h3>Ele usa vários arquivos?</h3>
        <p>Não. O output fica em um único arquivo HTML.</p>
      </article>

      <article class="faq-item animate delay-2">
        <h3>Screenshots podem dividir slide?</h3>
        <p>Normalmente não. Dê a eles espaço visual dedicado.</p>
      </article>

      <article class="faq-item animate delay-3">
        <h3>E se o conteúdo transbordar?</h3>
        <p>Divida imediatamente em outro slide.</p>
      </article>
    </div>
  </div>
</section>
```

## 16. Slide de Hub / Rede de Conexões

### Use para
- mostrar como vários serviços, modelos ou tarefas periféricas se conectam a uma plataforma central
- arquiteturas hub-and-spoke
- representação visual de integrações irradiando a partir de um controlador central

### Limites de conteúdo
- Nó central: no máximo 1 título + ícone
- Nós periféricos: 4 a 6 no máximo
- Label do nó periférico: máximo de 3 palavras
- Linhas de conexão opcionais: SVG com fluxo de traço animado

### Padrão

```html
<section class="slide hub-slide">
  <div class="slide-inner">
    <div class="slide-counter">01 / 10</div>
    
    <div class="hero">
      <div class="hero-badge animate delay-1">HUB DE INTEGRAÇÃO</div>
      <h1 class="animate delay-2">Conexão com Plataforma Central</h1>
    </div>

    <div class="hub-showcase animate delay-3">
      <!-- SVG de linhas de conexão animadas -->
      <svg class="hub-connections" viewBox="0 0 960 380" preserveAspectRatio="none">
        <!-- Linhas do centro (50%, 50%) até os nós -->
        <line x1="50%" y1="50%" x2="11.5%" y2="19%" stroke="url(#grad-1)" class="pulsing-line" />
        <line x1="50%" y1="50%" x2="11.5%" y2="81%" stroke="url(#grad-2)" class="pulsing-line" />
        <line x1="50%" y1="50%" x2="88.5%" y2="19%" stroke="url(#grad-3)" class="pulsing-line" />
        <line x1="50%" y1="50%" x2="88.5%" y2="81%" stroke="url(#grad-4)" class="pulsing-line" />
      </svg>

      <!-- Nós laterais da coluna esquerda -->
      <div class="hub-col-side">
        <div class="hub-small-node node-accent-1">
          <span class="node-icon">💻</span>
          <span class="node-text">Serviço A</span>
        </div>
        <div class="hub-small-node node-accent-2">
          <span class="node-icon">✍️</span>
          <span class="node-text">Serviço B</span>
        </div>
      </div>

      <!-- Nó central -->
      <div class="hub-center-node">
        <span class="hub-center-badge">CORE</span>
        <div class="hub-center-icon">🤖</div>
        <div class="hub-center-title">HUB PRINCIPAL</div>
      </div>

      <!-- Nós laterais da coluna direita -->
      <div class="hub-col-side">
        <div class="hub-small-node node-accent-3">
          <span class="node-icon">🔍</span>
          <span class="node-text">Serviço C</span>
        </div>
        <div class="hub-small-node node-accent-4">
          <span class="node-icon">⚡</span>
          <span class="node-text">Serviço D</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Sugestões de Classes Utilitárias

Estes são padrões opcionais de nomenclatura para incentivar consistência.

```html
.animate
.delay-1
.delay-2
.delay-3
.delay-4
.delay-5

.mono
.eyebrow
.subtitle
.section-heading
.card
.card-grid
.stats-grid
.btn
.btn-primary
.btn-secondary
.muted
.accent
.cols-2
.cols-3
.cols-4
```

---

## Heurísticas de Limite de Conteúdo

Use estas regras rápidas em caso de dúvida:

- Se um slide tiver mais de 1 parágrafo, considere dividir
- Se uma grade tiver mais de 6 cards, divida
- Se uma comparação tiver mais de 5 bullets por lado, divida
- Se um slide de etapas tiver mais de 5 etapas, divida
- Se labels ficarem multilinha com frequência, reduza o conteúdo
- Se screenshot + texto parecerem apertados, mova o screenshot para seu próprio slide
- Se o título quebrar linhas demais, encurte

---

## Anti-Padrões

Não faça o seguinte:

- Não coloque parágrafos longos em cards
- Não adicione screenshots ao lado de texto denso
- Não coloque 8+ itens em uma única grade
- Não crie um slide com múltiplos pontos focais competindo
- Não use linha do tempo para conceitos sem relação
- Não use diagrama se uma comparação simples funcionar melhor
- Não mantenha conteúdo transbordando “só porque quase cabe”

---

## Guia Final de Seleção

Use este mapeamento rápido:

- Gancho / abertura → Slide de Título
- Grande afirmação → Citação / Declaração
- Muitos itens curtos → Grade de Conteúdo
- Antigo vs novo → Comparação
- Arquivo ou hierarquia → Árvore / Estrutura
- Sistema conectado → Diagrama
- Módulos / ferramentas → Plugins / Cards de Funcionalidades
- Números / prova → Estatísticas / Resultados
- Processo / instruções → Etapas / Lista Numerada
- Prova de UI → Showcase de Screenshot
- Ação final → CTA / Encerramento

Se dois tipos de conteúdo competirem, prefira o tipo de slide que torna o conteúdo mais fácil de escanear em 3 segundos.
