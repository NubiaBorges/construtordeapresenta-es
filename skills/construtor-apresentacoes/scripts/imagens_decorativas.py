#!/usr/bin/env python3
"""
Gera as imagens decorativas que o PowerPoint não desenha sozinho (gradientes, círculos, anéis),
a partir das cores do design. Saída em PNG, pronta para addImage no pptxgenjs.

Uso:
  python imagens_decorativas.py pasta/ \
      --claro EAF0F3 DCE6EE --brilho A9C1FF \
      --cor 5A82DA 3466E2 0A48E0 \
      --orb 1F57E6 7FA2FA --orb2 0A3FD6 2F62E8 \
      --anel FE431D:0.32 FF9B87:0.40 0246E3:0.28 \
      --anel2 FE431D:0.30 0246E3:0.70 \
      --espiral FA4B73

Gera (só o que for pedido):
  bg_claro.png    fundo claro com gradiente diagonal e brilho no canto superior direito (1920×1080)
  bg_cor.png      fundo de cor da marca em gradiente diagonal de 2 ou 3 cores (1920×1080)
  orb.png / orb2.png   círculo com gradiente, fundo transparente
  anel.png / anel2.png anel segmentado (cor:fração, frações somam 1)
  espiral.png     anéis concêntricos finos
Para um tema escuro, passe as cores escuras em --claro (o nome é só o do arquivo).
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 1080


def hx(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def gradiente(cores, peso_x=0.35):
    """Gradiente diagonal; cores = 2 ou 3 tons. Desenhado em baixa resolução e ampliado (rápido e suave)."""
    w, h = W // 8, H // 8
    im = Image.new("RGB", (w, h)); px = im.load(); cs = [hx(c) for c in cores]
    for y in range(h):
        for x in range(w):
            t = min(1, max(0, x / w * peso_x + y / h * (1 - peso_x)))
            if len(cs) == 2:
                px[x, y] = lerp(cs[0], cs[1], t)
            else:
                px[x, y] = lerp(cs[0], cs[1], t / .5) if t < .5 else lerp(cs[1], cs[2], (t - .5) / .5)
    return im.resize((W, H), Image.BICUBIC)


def orb(cores, S=1400):
    g = gradiente(cores, 0.5).resize((S, S))
    m = Image.new("L", (S * 2, S * 2), 0); ImageDraw.Draw(m).ellipse((0, 0, S * 2 - 1, S * 2 - 1), fill=255)
    out = Image.new("RGBA", (S, S), (0, 0, 0, 0)); out.paste(g, (0, 0), m.resize((S, S), Image.LANCZOS))
    return out


def anel(segmentos, S=800, interno=0.55, inicio=210):
    R = S * 2; big = Image.new("RGBA", (R, R), (0, 0, 0, 0)); d = ImageDraw.Draw(big); ang = inicio
    for cor, frac in segmentos:
        d.pieslice((0, 0, R - 1, R - 1), ang - 90, ang - 90 + frac * 360, fill=hx(cor) + (255,)); ang += frac * 360
    r = int(R * interno / 2); c = R // 2; d.ellipse((c - r, c - r, c + r, c + r), fill=(0, 0, 0, 0))
    return big.resize((S, S), Image.LANCZOS)


def espiral(cor, S=600):
    im = Image.new("RGBA", (S * 2, S * 2), (0, 0, 0, 0)); d = ImageDraw.Draw(im); c = S
    for r in range(60, c - 20, 84):
        d.ellipse((c - r, c - r, c + r, c + r), outline=hx(cor) + (150,), width=14)
    return im.resize((S, S), Image.LANCZOS)


def segs(lista):
    out = []
    for item in lista:
        cor, frac = item.split(":"); out.append((cor, float(frac)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta")
    ap.add_argument("--claro", nargs=2); ap.add_argument("--brilho")
    ap.add_argument("--cor", nargs="+")
    ap.add_argument("--orb", nargs=2); ap.add_argument("--orb2", nargs=2)
    ap.add_argument("--anel", nargs="+"); ap.add_argument("--anel2", nargs="+")
    ap.add_argument("--espiral")
    a = ap.parse_args(); os.makedirs(a.pasta, exist_ok=True); p = lambda f: os.path.join(a.pasta, f)
    if a.claro:
        bg = gradiente(a.claro)
        if a.brilho:
            m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse((W * .62, -H * .35, W * 1.15, H * .55), fill=70)
            bg = Image.composite(Image.new("RGB", (W, H), hx(a.brilho)), bg, m.filter(ImageFilter.GaussianBlur(160)))
        bg.save(p("bg_claro.png"))
    if a.cor: gradiente(a.cor, 0.8).save(p("bg_cor.png"))
    if a.orb: orb(a.orb).save(p("orb.png"))
    if a.orb2: orb(a.orb2).save(p("orb2.png"))
    if a.anel: anel(segs(a.anel)).save(p("anel.png"))
    if a.anel2: anel(segs(a.anel2), inicio=300).save(p("anel2.png"))
    if a.espiral: espiral(a.espiral).save(p("espiral.png"))
    print("imagens em", a.pasta, ":", sorted(os.listdir(a.pasta)))


if __name__ == "__main__":
    main()
