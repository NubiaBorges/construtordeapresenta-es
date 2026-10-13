#!/usr/bin/env python3
"""
Verifica um deck HTML gerado pelo construtor-apresentacoes.

Uso:
    python verificar_deck.py caminho/deck.html [--screenshots pasta/]

Checa, em 1440x900 e 1280x720:
  - todo slide cabe na viewport (sem overflow)
  - contador NN / TOTAL correto em cada slide
  - um ponto de navegação por slide, e o ponto ativo acompanha o slide
  - teclado (ArrowDown / End / Home) muda de slide
  - animações recebem a classe in-view
  - scroll-snap ativo no container
  - imagens carregadas e embutidas (sem src externo/relativo)
  - fontes carregadas
  - notas do apresentador (se houver): presentes em todos os slides e abrindo com N
Sai com código 1 se houver falha. Com --screenshots, salva um PNG por slide.

Requer: pip install playwright && playwright install chromium
"""
import sys, re, argparse, pathlib
from playwright.sync_api import sync_playwright

VIEWPORTS = [(1440, 900), (1280, 720)]


def checar(page, w, h, falhas, avisos, shots_dir=None):
    tag = f"[{w}x{h}]"
    page.set_viewport_size({"width": w, "height": h})
    page.wait_for_timeout(400)

    info = page.evaluate("""() => {
      const deck = document.querySelector('.deck') || document.scrollingElement;
      const slides = [...document.querySelectorAll('.slide')];
      return {
        snap: getComputedStyle(deck).scrollSnapType,
        total: slides.length,
        counters: slides.map(s => (s.querySelector('.slide-counter')||{}).textContent || ''),
        overflow: slides.map((s,i) => {
          const inner = s.querySelector('.slide-inner') || s;
          const sr = s.getBoundingClientRect();
          let maxBottom = 0;
          inner.querySelectorAll('*').forEach(el => {
            const r = el.getBoundingClientRect();
            if (r.height > 0) maxBottom = Math.max(maxBottom, r.bottom - sr.top);
          });
          return { i: i+1, scroll: inner.scrollHeight, client: s.clientHeight, maxBottom: Math.round(maxBottom) };
        }),
        dots: document.querySelectorAll('.dots button, .dots a, [class*=dot] button').length,
        imgs: [...document.querySelectorAll('img')].map(im => ({src: im.getAttribute('src')||'', ok: im.complete && im.naturalWidth > 0})),
        fonts: document.fonts ? [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family) : [],
      };
    }""")

    total = info["total"]
    if total == 0:
        falhas.append(f"{tag} nenhum elemento .slide encontrado")
        return
    if "y" not in (info["snap"] or "") and "block" not in (info["snap"] or ""):
        falhas.append(f"{tag} scroll-snap não está ativo no container (.deck): '{info['snap']}'")

    for i, c in enumerate(info["counters"], 1):
        esperado = re.compile(rf"^\s*0?{i}\s*/\s*0?{total}\s*$")
        if not esperado.match(c):
            falhas.append(f"{tag} slide {i}: contador '{c.strip()}' ≠ '{i:02d} / {total:02d}'")

    for o in info["overflow"]:
        if o["scroll"] > o["client"] + 2 or o["maxBottom"] > o["client"] + 2:
            falhas.append(f"{tag} slide {o['i']} transborda: conteúdo {max(o['scroll'], o['maxBottom'])}px > viewport {o['client']}px")

    if info["dots"] != total:
        falhas.append(f"{tag} {info['dots']} pontos de navegação para {total} slides")

    for im in info["imgs"]:
        if not im["src"].startswith("data:"):
            falhas.append(f"{tag} imagem não embutida (src='{im['src'][:60]}') — use base64")
        elif not im["ok"]:
            falhas.append(f"{tag} imagem embutida não carregou")

    if w == VIEWPORTS[0][0]:
        if not info["fonts"]:
            avisos.append("nenhuma webfont carregada (sem rede? ou fonte não declarada)")
        # navegação por teclado + pontos + animação
        page.keyboard.press("Home"); page.wait_for_timeout(900)
        page.keyboard.press("ArrowDown"); page.wait_for_timeout(1100)
        estado = page.evaluate("""() => {
          const slides=[...document.querySelectorAll('.slide')];
          const top = (document.querySelector('.deck')||document.scrollingElement).scrollTop;
          const idx = slides.findIndex(s => Math.abs(s.offsetTop - top) < 5);
          const dots=[...document.querySelectorAll('.dots button, .dots a')];
          const ativo = dots.findIndex(d => d.classList.contains('active') || d.getAttribute('aria-current')==='true');
          const anim = slides[idx] ? slides[idx].querySelectorAll('.animate').length : 0;
          const animOk = slides[idx] ? [...slides[idx].querySelectorAll('.animate')].every(a => getComputedStyle(a).opacity > 0.5) : false;
          return {idx, ativo, anim, animOk};
        }""")
        if total > 1 and estado["idx"] != 1:
            falhas.append(f"teclado: ArrowDown a partir do slide 1 levou ao índice {estado['idx']+1}, esperado 2")
        if total > 1 and estado["ativo"] != 1:
            falhas.append(f"pontos: ponto ativo é {estado['ativo']+1}, esperado 2 (não sincroniza)")
        if estado["anim"] and not estado["animOk"]:
            falhas.append("animações: elementos .animate do slide 2 continuam invisíveis após entrar na tela")
        page.keyboard.press("End"); page.wait_for_timeout(1400)
        fim = page.evaluate("""() => { const d=document.querySelector('.deck')||document.scrollingElement; return Math.abs(d.scrollTop + d.clientHeight - d.scrollHeight) < 5; }""")
        if not fim:
            falhas.append("teclado: End não levou ao último slide")

        # notas do apresentador (opcional): se existirem, todo slide deve ter e a tecla N deve abrir o painel
        notas = page.evaluate("() => [...document.querySelectorAll('.slide')].map(s => !!s.querySelector('.notes'))")
        if any(notas):
            faltando = [str(i + 1) for i, tem in enumerate(notas) if not tem]
            if faltando:
                falhas.append(f"notas: slides sem <aside class=\"notes\">: {', '.join(faltando)}")
            page.keyboard.press("Home"); page.wait_for_timeout(700)
            page.keyboard.press("n"); page.wait_for_timeout(200)
            aberto = page.evaluate("() => { const p=document.getElementById('notesPanel'); return !!p && getComputedStyle(p).display !== 'none' && p.innerText.trim().length > 20; }")
            if not aberto:
                falhas.append("notas: a tecla N não abriu o painel de notas com conteúdo")
            page.keyboard.press("Escape"); page.wait_for_timeout(200)

        if shots_dir:
            shots_dir.mkdir(parents=True, exist_ok=True)
            for i in range(total):
                page.evaluate(f"document.querySelectorAll('.slide')[{i}].scrollIntoView({{behavior:'instant'}})")
                page.wait_for_timeout(1000)
                page.screenshot(path=str(shots_dir / f"slide-{i+1:02d}.png"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--screenshots")
    a = ap.parse_args()
    caminho = pathlib.Path(a.html).resolve()
    falhas, avisos = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        erros_js = []
        page.on("pageerror", lambda e: erros_js.append(str(e)))
        page.goto(caminho.as_uri(), wait_until="networkidle", timeout=30000)
        for w, h in VIEWPORTS:
            checar(page, w, h, falhas, avisos, pathlib.Path(a.screenshots) if (a.screenshots and w == VIEWPORTS[0][0]) else None)
        falhas += [f"erro de JavaScript: {e}" for e in erros_js]
        b.close()

    for x in avisos:
        print("AVISO:", x)
    if falhas:
        print(f"FALHOU ({len(falhas)}):")
        for f in falhas:
            print("  -", f)
        sys.exit(1)
    print("OK: todas as verificações passaram.")


if __name__ == "__main__":
    main()
