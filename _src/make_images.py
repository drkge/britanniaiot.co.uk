#!/usr/bin/env python3
"""
Generate the raster assets the site references: Open Graph card, logo PNG for
structured data, favicons and app icons.

    _src/venv/bin/python _src/make_images.py

Requires Pillow. Run once; the outputs are committed with the site.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
IMG.mkdir(parents=True, exist_ok=True)

NAVY = (10, 27, 48)
INK = (7, 19, 36)
GREEN = (14, 143, 88)
GREEN_HI = (34, 197, 94)
GOLD = (201, 162, 39)
WHITE = (255, 255, 255)
MUTED = (159, 182, 206)

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
BOLD = FONT_DIR / "Arial Bold.ttf"
REG = FONT_DIR / "Arial.ttf"


def font(path, size):
    return ImageFont.truetype(str(path), size)


def gradient_bg(w, h):
    """Navy field with two soft radial glows, matching the site hero."""
    base = Image.new("RGB", (w, h), NAVY)
    px = base.load()
    for y in range(h):
        for x in range(0, w, 2):
            # green glow, upper left
            dx, dy = (x - w * 0.10) / (w * 0.62), (y - h * -0.10) / (h * 0.85)
            g = max(0.0, 1.0 - (dx * dx + dy * dy)) ** 1.6
            # blue glow, upper right
            bx, by = (x - w * 0.95) / (w * 0.55), (y - h * 0.05) / (h * 0.80)
            b = max(0.0, 1.0 - (bx * bx + by * by)) ** 1.6
            r0, g0, b0 = NAVY
            c = (
                min(255, int(r0 + g * 12 + b * 14)),
                min(255, int(g0 + g * 58 + b * 46)),
                min(255, int(b0 + g * 30 + b * 88)),
            )
            px[x, y] = c
            if x + 1 < w:
                px[x + 1, y] = c
    return base


def draw_mark(d, x, y, s, bg_ring=False):
    """The Britannia IoT bin-and-signal mark, drawn at scale s (px per unit/40)."""
    u = s / 40.0
    if bg_ring:
        d.rounded_rectangle([x, y, x + s, y + s], radius=9 * u, fill=INK)
    # body
    d.rounded_rectangle(
        [x + 7 * u, y + 13 * u, x + 33 * u, y + 36 * u], radius=4.5 * u, fill=GREEN
    )
    # fill bar
    d.rounded_rectangle(
        [x + 10.5 * u, y + 25 * u, x + 29.5 * u, y + 32.5 * u], radius=2.2 * u, fill=GREEN_HI
    )
    # lid handle
    d.rounded_rectangle(
        [x + 13 * u, y + 8.5 * u, x + 27 * u, y + 14 * u], radius=2.5 * u,
        outline=GREEN, width=max(1, int(2.6 * u)),
    )
    d.rectangle([x + 13 * u, y + 12 * u, x + 27 * u, y + 15 * u], fill=GREEN)
    # signal arcs
    for r, wdt, col in ((11 * u, 2.4 * u, GOLD), (16 * u, 2.4 * u, (150, 124, 46))):
        cx, cy = x + 21 * u, y + 15 * u
        d.arc([cx - r, cy - r, cx + r, cy + r], start=-72, end=-8,
              fill=col, width=max(1, int(wdt)))


def make_og():
    W, H = 1200, 630
    img = gradient_bg(W, H)
    d = ImageDraw.Draw(img)

    # subtle grid
    for gx in range(0, W, 62):
        d.line([(gx, 0), (gx, H)], fill=(16, 36, 60), width=1)
    for gy in range(0, H, 62):
        d.line([(0, gy), (W, gy)], fill=(16, 36, 60), width=1)

    draw_mark(d, 80, 74, 76)

    d.text((176, 84), "BRITANNIA IOT", font=font(BOLD, 34), fill=WHITE)
    d.text((178, 124), "S O L U T I O N S", font=font(BOLD, 15), fill=MUTED)

    d.text((80, 216), "Collect the bins", font=font(BOLD, 76), fill=WHITE)
    d.text((80, 296), "that are full.", font=font(BOLD, 76), fill=WHITE)

    d.text((80, 402),
           "Radar fill-level sensors and dynamic round planning",
           font=font(REG, 27), fill=(178, 199, 220))
    d.text((80, 440), "for UK councils, contractors and large estates.",
           font=font(REG, 27), fill=(178, 199, 220))

    # stat strip
    y0 = 512
    d.line([(80, y0 - 26), (1120, y0 - 26)], fill=(30, 58, 92), width=2)
    stats = [("71%", "fewer collections"), ("54%", "fewer km driven"),
             ("<12 mo", "payback"), ("8 yrs", "battery life")]
    x = 80
    for num, label in stats:
        d.text((x, y0), num, font=font(BOLD, 38), fill=(110, 231, 165))
        d.text((x, y0 + 50), label, font=font(REG, 20), fill=MUTED)
        x += 268

    img.save(IMG / "og-default.png", "PNG", optimize=True)
    print("og-default.png")


def make_icons():
    # Square logo on ink, for schema.org and app icons.
    for size in (512, 192, 180):
        s = size
        img = Image.new("RGB", (s * 4, s * 4), INK)
        d = ImageDraw.Draw(img)
        pad = s * 4 * 0.16
        draw_mark(d, pad, pad, s * 4 - pad * 2)
        img = img.resize((s, s), Image.LANCZOS)
        name = {512: "logo.png", 192: "icon-192.png", 180: "apple-touch-icon.png"}[size]
        img.save(IMG / name, "PNG", optimize=True)
        if size == 512:
            img.save(IMG / "icon-512.png", "PNG", optimize=True)
        print(name)

    # Multi-resolution .ico
    big = Image.open(IMG / "logo.png").convert("RGB")
    big.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("favicon.ico")


if __name__ == "__main__":
    make_og()
    make_icons()
