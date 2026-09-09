#!/usr/bin/env python3
"""
Britannia IoT Solutions — logo and icon generator.

Emits the canonical SVG mark plus every raster the site needs. Kept in the repo
so it is not lost again: the previous icon generator was deleted with _src/ and
had to be recovered from git history to recolour the brand.

    python3 _tools/make-logo.py

Requires Pillow. The `_tools` prefix means Jekyll ignores this directory.

Design: a circular badge tilted 45 degrees. The Union Jack fills one half, a navy
panel the other, with two bold signal arcs sweeping up-right. Drawn from geometry,
not traced from any existing artwork.
"""
from __future__ import annotations

import math
import pathlib

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"

RED   = "#CE2540"   # brand red, sampled from the business card
BLUE  = "#0B2A63"   # Union blue
NAVY  = "#0A1B30"   # matches the site's dark sections exactly
WHITE = "#FFFFFF"
INK   = "#071324"

TILT = -45          # SVG degrees; negative is anticlockwise on screen
RADII = (26.0, 40.0)
SPREAD = 62.0       # arc half-sweep, degrees either side of due east
WAVE_W = 8.5


def hx(c: str) -> tuple[int, int, int]:
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


# ---------------------------------------------------------------- SVG ------

def svg(prefix: str = "bm", ring: str = NAVY) -> str:
    """The mark as SVG. `prefix` namespaces the clipPath ids — the header and
    footer both render on every page, and duplicate ids would collide."""
    arcs = "".join(_svg_arc(50, 50, r, -SPREAD, SPREAD, WHITE, WAVE_W) for r in RADII)
    return f"""<svg class="logo-mark" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Britannia IoT Solutions">
  <defs>
    <clipPath id="{prefix}-o"><circle cx="50" cy="50" r="50"/></clipPath>
    <clipPath id="{prefix}-f"><rect width="50" height="100"/></clipPath>
  </defs>
  <g clip-path="url(#{prefix}-o)">
    <g transform="rotate({TILT} 50 50)">
      <rect x="50" width="50" height="100" fill="{NAVY}"/>
      <g clip-path="url(#{prefix}-f)">
        <rect width="100" height="100" fill="{BLUE}"/>
        <path d="M0 0 L100 100 M100 0 L0 100" stroke="{WHITE}" stroke-width="28"/>
        <g stroke="{RED}" stroke-width="9.5">
          <path d="M0 0 L50 50" transform="translate(0,4.8)"/>
          <path d="M50 50 L100 100" transform="translate(0,-4.8)"/>
          <path d="M100 0 L50 50" transform="translate(0,4.8)"/>
          <path d="M50 50 L0 100" transform="translate(0,-4.8)"/>
        </g>
        <path d="M50 0 V100 M0 50 H100" stroke="{WHITE}" stroke-width="33"/>
        <path d="M50 0 V100 M0 50 H100" stroke="{RED}" stroke-width="19.5"/>
      </g>
      {arcs}
    </g>
  </g>
  <circle cx="50" cy="50" r="48.5" fill="none" stroke="{ring}" stroke-width="3"/>
</svg>"""


def _svg_arc(cx, cy, r, a0, a1, colour, w):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    return (f'<path d="M {x0:.2f} {y0:.2f} A {r:.2f} {r:.2f} 0 0 1 {x1:.2f} {y1:.2f}" '
            f'fill="none" stroke="{colour}" stroke-width="{w}" stroke-linecap="round"/>')


# ------------------------------------------------------------- raster ------

def badge(size: int, ss: int = 8) -> Image.Image:
    """Render the badge as RGBA at `size` px, supersampled `ss` times.

    Composed unrotated, then rotated whole and masked to a circle — a circle is
    rotation-invariant, so this is equivalent to the SVG's rotated group.
    """
    S = size * ss
    u = S / 100.0                       # one SVG unit in device pixels
    def px(v): return v * u
    def w(v): return max(1, round(v * u))

    canvas = Image.new("RGBA", (S, S), (0, 0, 0, 0))

    # --- flag, drawn full-square then masked to its half ---
    flag = Image.new("RGBA", (S, S), hx(BLUE))
    fd = ImageDraw.Draw(flag)
    fd.line([(0, 0), (S, S)], fill=hx(WHITE), width=w(28))
    fd.line([(S, 0), (0, S)], fill=hx(WHITE), width=w(28))
    off = px(4.8)
    for (a, b), dy in ((((0, 0), (px(50), px(50))), off),
                       (((px(50), px(50)), (S, S)), -off),
                       (((S, 0), (px(50), px(50))), off),
                       (((px(50), px(50)), (0, S)), -off)):
        fd.line([(a[0], a[1] + dy), (b[0], b[1] + dy)], fill=hx(RED), width=w(9.5))
    fd.line([(px(50), 0), (px(50), S)], fill=hx(WHITE), width=w(33))
    fd.line([(0, px(50)), (S, px(50))], fill=hx(WHITE), width=w(33))
    fd.line([(px(50), 0), (px(50), S)], fill=hx(RED), width=w(19.5))
    fd.line([(0, px(50)), (S, px(50))], fill=hx(RED), width=w(19.5))

    half = Image.new("L", (S, S), 0)
    ImageDraw.Draw(half).rectangle([0, 0, px(50), S], fill=255)

    # navy panel on the other side, then the flag over its half
    ImageDraw.Draw(canvas).rectangle([px(50), 0, S, S], fill=hx(NAVY))
    canvas.paste(flag, (0, 0), half)

    # --- signal arcs, with round caps drawn in by hand ---
    d = ImageDraw.Draw(canvas)
    for r in RADII:
        # Pillow draws a thick arc inward from the bounding ellipse, so the box
        # has to sit at r + half the stroke for the centreline to land on r.
        rb = r + WAVE_W / 2
        bbox = [px(50 - rb), px(50 - rb), px(50 + rb), px(50 + rb)]
        d.arc(bbox, -SPREAD, SPREAD, fill=hx(WHITE), width=w(WAVE_W))
        for a in (-SPREAD, SPREAD):                     # Pillow arcs have no caps
            cx = px(50 + r * math.cos(math.radians(a)))
            cy = px(50 + r * math.sin(math.radians(a)))
            rr = px(WAVE_W / 2)
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=hx(WHITE))

    canvas = canvas.rotate(-TILT, resample=Image.BICUBIC, center=(S / 2, S / 2))

    # --- clip to the circle, then the ring ---
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, S - 1, S - 1], fill=255)
    out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    out.paste(canvas, (0, 0), mask)
    ImageDraw.Draw(out).ellipse([0, 0, S - 1, S - 1], outline=hx(NAVY), width=w(3))
    return out.resize((size, size), Image.LANCZOS)


def on_bg(size: int, bg: str) -> Image.Image:
    im = Image.new("RGB", (size, size), hx(bg))
    b = badge(size)
    im.paste(b, (0, 0), b)
    return im


# ----------------------------------------------------------- OG card -------

FONT_DIR = pathlib.Path("/System/Library/Fonts/Supplemental")
BOLD, REG = FONT_DIR / "Arial Bold.ttf", FONT_DIR / "Arial.ttf"


def og_card() -> Image.Image:
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), hx(NAVY))
    px = img.load()
    for y in range(H):
        for x in range(0, W, 2):
            dx, dy = (x - W * .10) / (W * .62), (y + H * .10) / (H * .85)
            g = max(0.0, 1 - (dx * dx + dy * dy)) ** 1.6
            bx, by = (x - W * .95) / (W * .55), (y - H * .05) / (H * .80)
            b = max(0.0, 1 - (bx * bx + by * by)) ** 1.6
            r0, g0, b0 = hx(NAVY)
            c = (min(255, int(r0 + g * 10 + b * 14)),
                 min(255, int(g0 + g * 46 + b * 46)),
                 min(255, int(b0 + g * 86 + b * 88)))
            px[x, y] = c
            if x + 1 < W:
                px[x + 1, y] = c
    d = ImageDraw.Draw(img)
    for gx in range(0, W, 62):
        d.line([(gx, 0), (gx, H)], fill=(16, 36, 60))
    for gy in range(0, H, 62):
        d.line([(0, gy), (W, gy)], fill=(16, 36, 60))

    mark = badge(96)
    img.paste(mark, (80, 66), mark)
    f = lambda p, s: ImageFont.truetype(str(p), s)
    d.text((196, 78), "BRITANNIA IOT", font=f(BOLD, 34), fill=hx(WHITE))
    d.text((198, 118), "S O L U T I O N S", font=f(BOLD, 15), fill=(159, 182, 206))

    d.text((80, 216), "Collect the bins", font=f(BOLD, 76), fill=hx(WHITE))
    d.text((80, 296), "that are full.", font=f(BOLD, 76), fill=hx(WHITE))
    d.text((80, 402), "Radar fill-level sensors and dynamic round planning",
           font=f(REG, 27), fill=(178, 199, 220))
    d.text((80, 440), "for UK councils, contractors and large estates.",
           font=f(REG, 27), fill=(178, 199, 220))

    y0 = 512
    d.line([(80, y0 - 26), (1120, y0 - 26)], fill=(30, 58, 92), width=2)
    x = 80
    for num, label in [("71%", "fewer collections"), ("54%", "fewer km driven"),
                       ("<12 mo", "payback"), ("8 yrs", "battery life")]:
        d.text((x, y0), num, font=f(BOLD, 38), fill=(124, 197, 255))
        d.text((x, y0 + 50), label, font=f(REG, 20), fill=(159, 182, 206))
        x += 268
    return img


# --------------------------------------------------------------- main -----

def main() -> None:
    IMG.mkdir(parents=True, exist_ok=True)

    (IMG / "logo-mark.svg").write_text(svg("bm"), encoding="utf-8")
    (ROOT / "favicon.svg").write_text(svg("fv"), encoding="utf-8")
    print("  logo-mark.svg, favicon.svg")

    # Transparent-background PNGs for general use
    for name, size in [("logo.png", 512), ("icon-512.png", 512), ("icon-192.png", 192)]:
        badge(size).save(IMG / name, "PNG", optimize=True)
        print(f"  {name}")

    # Apple touch icons must be opaque — iOS composites them on a solid tile
    on_bg(180, WHITE).save(IMG / "apple-touch-icon.png", "PNG", optimize=True)
    print("  apple-touch-icon.png")

    ico = on_bg(256, WHITE)
    ico.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("  favicon.ico")

    og_card().save(IMG / "og-default.png", "PNG", optimize=True)
    print("  og-default.png")


if __name__ == "__main__":
    main()
