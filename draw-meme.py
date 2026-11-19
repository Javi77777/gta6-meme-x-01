#!/usr/bin/env python3
"""Draw the gta6-meme-x-01 meme image (1024x1024 PNG) with Pillow.

The joke: 13 years waiting for GTA 6, and launch night is spent staring at a
download bar stuck at 99%. The make.fun ghost (official press-kit mark,
assets/makefun-mark.png) sits on the couch next to the gamer as a fellow
sufferer -- worked into the scene, not a sticker.

Run: python3 draw-meme.py   (writes meme.png next to this script)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def outlined_text(d, xy, text, fnt, fill, stroke, sw, anchor="mm"):
    d.text(xy, text, font=fnt, fill=fill, anchor=anchor,
           stroke_width=sw, stroke_fill=stroke)


def sunset_gradient(d, box):
    """Horizontal-band sunset: orange -> pink -> purple."""
    x0, y0, x1, y1 = box
    stops = [(255, 154, 61), (255, 94, 138), (123, 47, 190)]
    n = y1 - y0
    for i in range(n):
        t = i / max(n - 1, 1)
        if t < 0.5:
            a, b, u = stops[0], stops[1], t / 0.5
        else:
            a, b, u = stops[1], stops[2], (t - 0.5) / 0.5
        col = tuple(int(a[k] + (b[k] - a[k]) * u) for k in range(3))
        d.line([(x0, y0 + i), (x1, y0 + i)], fill=col)


def palm(d, bx, by, s, col):
    """A simple palm silhouette rooted at (bx, by), scale s."""
    # trunk: slightly curved thick line
    pts = []
    for i in range(9):
        t = i / 8
        pts.append((bx + 14 * s * t * t, by - 120 * s * t))
    d.line(pts, fill=col, width=max(3, int(10 * s)), joint="curve")
    tx, ty = pts[-1]
    # fronds: arcs drooping from the crown
    for ang in (-165, -125, -85, -45, -5):
        rad = math.radians(ang)
        ex = tx + 58 * s * math.cos(rad)
        ey = ty + 30 * s * math.sin(rad) + 62 * s
        mx = tx + 44 * s * math.cos(rad)
        my = ty + 8 * s * math.sin(rad) - 30 * s
        d.line([(tx, ty), (mx, my), (ex, ey)], fill=col,
               width=max(2, int(7 * s)), joint="curve")


def main():
    img = Image.new("RGB", (W, H), (18, 28, 52))
    d = ImageDraw.Draw(img, "RGBA")

    # ---- wall + floor -------------------------------------------------
    d.rectangle([0, 0, W, 860], fill=(22, 34, 63))
    d.rectangle([0, 860, W, H], fill=(38, 28, 24))
    # soft lamp glow, top right
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([620, -260, 1180, 300], fill=(255, 190, 90, 26))
    img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))
    d = ImageDraw.Draw(img, "RGBA")

    # ---- top caption --------------------------------------------------
    outlined_text(d, (512, 66), "WAITED 13 YEARS FOR GTA 6",
                  font(FONT_BOLD, 50), (255, 255, 255), (0, 0, 0), 7)

    # ---- TV -----------------------------------------------------------
    d.rounded_rectangle([118, 128, 906, 478], radius=26, fill=(8, 8, 12))
    sunset_gradient(d, (134, 144, 890, 462))
    # sun
    d.ellipse([452, 168, 572, 288], fill=(255, 236, 170))
    # palms
    palm(d, 190, 462, 1.0, (46, 16, 66))
    palm(d, 800, 462, 0.8, (46, 16, 66))
    # sea strip
    d.rectangle([134, 420, 890, 462], fill=(24, 60, 110))
    # title
    outlined_text(d, (512, 330), "GTA VI", font(FONT_BOLD, 92),
                  (255, 255, 255), (0, 0, 0), 10)
    outlined_text(d, (512, 402), "L E O N I D A", font(FONT_BOLD, 30),
                  (255, 214, 120), (0, 0, 0), 5)
    # download bar on the TV, at the bottom of the screen
    d.rounded_rectangle([214, 424, 810, 452], radius=10, fill=(10, 10, 16))
    d.rounded_rectangle([214, 424, 804, 452], radius=10, fill=(217, 0, 130))

    # ---- couch --------------------------------------------------------
    # backrest + base + cushions + armrests
    d.rounded_rectangle([96, 500, 928, 700], radius=30, fill=(164, 74, 52))
    d.rounded_rectangle([96, 640, 928, 852], radius=30, fill=(186, 92, 62))
    d.rounded_rectangle([150, 640, 520, 800], radius=22, fill=(204, 110, 74))
    d.rounded_rectangle([540, 640, 880, 800], radius=22, fill=(204, 110, 74))
    d.rounded_rectangle([96, 600, 168, 852], radius=24, fill=(164, 74, 52))
    d.rounded_rectangle([856, 600, 928, 852], radius=24, fill=(164, 74, 52))

    # ---- gamer (left cushion): slumped, controller in hand -----------
    # legs stretched forward
    d.rounded_rectangle([250, 800, 330, 852], radius=14, fill=(40, 52, 96))
    d.rounded_rectangle([360, 800, 440, 852], radius=14, fill=(40, 52, 96))
    # hoodie body
    d.rounded_rectangle([248, 640, 452, 816], radius=34, fill=(46, 127, 134))
    # arms to the controller
    d.line([(280, 700), (330, 780)], fill=(46, 127, 134), width=34)
    d.line([(420, 700), (372, 780)], fill=(46, 127, 134), width=34)
    # hands
    d.ellipse([312, 764, 344, 796], fill=(242, 199, 155))
    d.ellipse([356, 764, 388, 796], fill=(242, 199, 155))
    # controller
    d.rounded_rectangle([318, 772, 384, 806], radius=12, fill=(24, 24, 30))
    d.ellipse([330, 782, 340, 792], fill=(255, 255, 255))
    d.ellipse([360, 782, 370, 792], fill=(255, 214, 120))
    # head
    d.ellipse([292, 540, 408, 656], fill=(242, 199, 155))
    # cap: dome + brim sitting above the eyes
    d.pieslice([288, 524, 412, 640], 180, 360, fill=(24, 24, 30))
    d.rounded_rectangle([296, 582, 408, 600], radius=8, fill=(24, 24, 30))
    # tired eyes (half-closed lines) + flat mouth
    d.line([(318, 624), (344, 624)], fill=(20, 20, 20), width=5)
    d.line([(362, 624), (388, 624)], fill=(20, 20, 20), width=5)
    d.line([(336, 648), (370, 648)], fill=(20, 20, 20), width=4)

    # ---- make.fun ghost (official press-kit mark) on the right cushion
    mark = Image.open(os.path.join(HERE, "assets", "makefun-mark.png")).convert("RGBA")
    mark = mark.resize((236, 236), Image.LANCZOS).rotate(-5, expand=True, resample=Image.BICUBIC)
    img.paste(mark, (636, 566), mark)
    d = ImageDraw.Draw(img, "RGBA")
    # speech bubble from the ghost, on the couch backrest
    d.rounded_rectangle([498, 548, 668, 618], radius=18, fill=(255, 255, 255))
    d.polygon([(620, 618), (652, 618), (636, 652)], fill=(255, 255, 255))
    d.text((583, 583), "same.", font=font(FONT_BOLD, 34), fill=(20, 20, 20), anchor="mm")

    # ---- bottom caption ------------------------------------------------
    outlined_text(d, (512, 906), "DOWNLOAD: 99% — 2 HOURS LEFT",
                  font(FONT_BOLD, 42), (255, 255, 255), (0, 0, 0), 7)
    # make.fun wordmark, small, bottom centre
    d.text((512, 986), "make.fun", font=font(FONT_BOLD, 30),
           fill=(255, 64, 170), anchor="mm")

    out = os.path.join(HERE, "meme.png")
    img.save(out, "PNG")
    # 480px preview, as the judge will see it
    img.resize((480, 480), Image.LANCZOS).save(
        os.path.join(HERE, "meme-480-preview.png"), "PNG")
    print("wrote", out)


if __name__ == "__main__":
    main()
