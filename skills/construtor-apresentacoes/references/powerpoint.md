# Saída em PowerPoint (.pptx)

Use quando o usuário pedir PowerPoint, .pptx, ou um arquivo para editar no Canva, Google Slides ou Keynote. O PowerPoint é a versão **editável** do mesmo deck: mesmos slides, mesma ordem, mesmos textos e números, mesmo design. Ele não substitui o HTML quando os dois forem pedidos; os dois saem do mesmo plano.

## Como construir

1. **Leia a skill de PowerPoint (`pptx`) antes de escrever código.** Ela traz as armadilhas do `pptxgenjs` (cores sem `#`, opções mutadas, sombras, notas) e o fluxo de "deck estruturado": tema → layouts → seções → slides preenchidos por placeholder → `applyTheme`. Siga esse fluxo.
2. **Formato:** `pres.layout = "LAYOUT_WIDE"` (13,333 × 7,5 pol, 16:9), o mesmo do Canva e do Google Slides.
3. **Tema = tokens do design.** As cores e fontes que o HTML usa no `:root` viram o `THEME` (`dk1` = tinta, `lt1` = branco, `accent1…6` = cores da marca, `headFontFace`/`bodyFontFace` = fontes do design). Mantenha a fonte do usuário mesmo que o preview local a substitua; deixe ~10% de folga nas caixas de texto.
4. **Layouts:** um por moldura de slide (ex.: capa, conteúdo claro, conteúdo sem título, slide de cor). Título como placeholder **alinhado à esquerda** (o padrão do placeholder é centralizado; passe `align: "left"`), número do slide no layout.
5. **O que o PowerPoint não faz bem, vira imagem:** gradientes de fundo, círculos com gradiente, anéis e espirais decorativas. Gere-os como PNG com `scripts/imagens_decorativas.py` (cores do design como argumento) e posicione com `addImage`. Texto **nunca** vira imagem.
6. **Gráficos simples como formas.** Barras horizontais, barras de proporção e destaques numéricos ficam como formas (`ROUNDED_RECTANGLE` para trilho e preenchimento) e caixas de texto. O Canva costuma converter gráficos nativos em imagem ao importar, e aí ninguém consegue editar. Use gráfico nativo (`addChart`) só para séries longas (linha do tempo com muitos pontos) e quando o destino não for o Canva.
7. **Ícones** do HTML (SVG) → PNG com `sharp` a 256 px.
8. **Notas do apresentador:** não escreva à mão. Depois do `writeFile` + `applyTheme`, grave as notas com o script da `roteiro-apresentacao`:
   ```bash
   python <roteiro-apresentacao>/scripts/notas_do_roteiro.py roteiro.md --pptx deck.pptx
   ```
   O script recusa se o número de slides divergir e lista título do slide × título do roteiro lado a lado.

## Verificação

- `python <pptx>/scripts/office/validate.py deck.pptx` → precisa passar.
- Renderize (`soffice.py --headless --convert-to pdf`, depois `pdftoppm`) e olhe **todos** os slides: texto cortado, sobreposição, título desalinhado entre slides do mesmo tipo, decoração saindo da borda. Compare com os screenshots do HTML: os dois devem parecer o mesmo deck.
- `markitdown deck.pptx` para conferir textos e números contra o plano.

## Entrega

Arquivo com o mesmo nome do HTML e extensão `.pptx`. Uma linha dizendo que é a versão editável (Canva: Criar design → Importar arquivo) e que as notas estão nas anotações do apresentador. Não prometa que as notas sobrevivem à importação em outra ferramenta: sugira conferir depois de importar e guardar o roteiro como reserva.
