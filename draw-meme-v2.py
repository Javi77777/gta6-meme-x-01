#!/usr/bin/env python3
"""Draw the fresh GTA 6 meme for gta6-meme-x-01 (v2, new joke).

Concept: a Vice City sunset. The make.fun ghost IS the player's AI agent:
it has already beaten GTA 6 and is chilling on the beach with its magenta
coin, while the player is still stuck on the title screen.

Top text:    MY AI AGENT BEAT GTA 6
Bottom text: I'M STILL ON THE / TITLE SCREEN

Deterministic: no randomness, no network, no downloaded images.
Everything is drawn with PIL primitives.
"""
import hashlib
import math

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
HORIZON = 700

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


# ---- sky: sunset gradient ----
stops = [
    (0.00, (26, 10, 60)),     # deep purple
    (0.35, (96, 16, 88)),     # magenta-purple
    (0.60, (198, 38, 92)),    # hot pink
    (0.78, (255, 110, 70)),   # orange
    (1.00, (255, 186, 90)),   # warm horizon
]
for y in range(HORIZON):
    t = y / HORIZON
    col = stops[-1][1]
    for i in range(len(stops) - 1):
        t0, c0 = stops[i]
        t1, c1 = stops[i + 1]
        if t0 <= t <= t1:
            col = lerp(c0, c1, (t - t0) / (t1 - t0))
            break
    d.line([(0, y), (W, y)], fill=col)

# ---- sun (halo + disc) ----
d.ellipse([512 - 150, 330 - 150, 512 + 150, 330 + 150], fill=(255, 150, 80))
d.ellipse([512 - 115, 330 - 115, 512 + 115, 330 + 115], fill=(255, 222, 140))
d.ellipse([512 - 95, 330 - 95, 512 + 95, 330 + 95], fill=(255, 240, 180))

# ---- buildings (dark silhouettes with lit windows) ----
BLDG = (16, 6, 34)


def building(x, w, h):
    d.rectangle([x, HORIZON - h, x + w, HORIZON], fill=BLDG)
    for wy in range(HORIZON - h + 14, HORIZON - 10, 26):
        for wx in range(x + 10, x + w - 8, 22):
            if (wx // 22 + wy // 26) % 3 == 0:
                d.rectangle([wx, wy, wx + 7, wy + 9], fill=(255, 214, 120))


for (x, w, h) in [(0, 90, 90), (95, 70, 130), (170, 80, 80), (255, 60, 110),
                  (760, 70, 100), (835, 80, 140), (920, 104, 85)]:
    building(x, w, h)

# ---- ground ----
d.rectangle([0, HORIZON, W, H], fill=(18, 7, 32))
d.rectangle([0, HORIZON, W, HORIZON + 10], fill=(60, 20, 60))

# ---- billboard: make.fun, worked into the scene ----
d.rectangle([100, 575, 120, HORIZON], fill=BLDG)
d.rectangle([300, 575, 320, HORIZON], fill=BLDG)
d.rectangle([60, 480, 340, 575], fill=(20, 10, 40), outline=(230, 0, 126), width=6)
f_bill = ImageFont.truetype(BOLD, 40)
d.text((200, 527), "make.fun", font=f_bill, fill=(255, 255, 255), anchor="mm",
       stroke_width=2, stroke_fill=(230, 0, 126))

# ---- palm tree (right edge) ----
def palm(cx, top_y, base_y):
    pts = []
    for i in range(9):
        t = i / 8
        x = cx + int(40 * t * t) - int(10 * t)
        y = top_y + int((base_y - top_y) * t)
        pts.append((x, y))
    d.line(pts, fill=BLDG, width=20)
    for ang in [-165, -140, -115, -90, -65, -40, -15, 5]:
        r = math.radians(ang)
        x2 = cx + int(170 * math.cos(r))
        y2 = top_y + int(100 * math.sin(r)) + 78
        d.line([(cx, top_y), ((cx + x2) // 2, (top_y + y2) // 2 - 26), (x2, y2)],
               fill=BLDG, width=14)


palm(880, 400, HORIZON)

# ---- beach towel under the ghost ----
for i, col in enumerate([(230, 0, 126), (255, 255, 255),
                         (230, 0, 126), (255, 255, 255)]):
    d.rectangle([380, 762 + i * 16, 644, 762 + (i + 1) * 16], fill=col)
d.rectangle([380, 762, 644, 826], outline=(0, 0, 0), width=4)


# ---- helpers: stars ----
def star(cx, cy, ro, ri, npoints, fill):
    pts = []
    for i in range(npoints * 2):
        a = math.pi / 2 + i * math.pi / npoints
        r = ro if i % 2 == 0 else ri
        pts.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    d.polygon(pts, fill=fill)


# ---- the make.fun ghost (mascot): white body, black outline, sparkle eyes,
#      one round hand holding a magenta coin with a white star ----
cx, cy, r = 512, 540, 170
body = []
for deg in range(180, 361, 6):  # dome, left -> top -> right (through 270 = top)
    a = math.radians(deg)
    body.append((cx + r * math.cos(a), cy + r * math.sin(a)))
body.append((cx + r, 700))  # right side down
for bx in (639.5, 554.5, 469.5, 384.5):  # wavy bottom, right -> left
    for deg in range(0, 181, 12):
        a = math.radians(deg)
        body.append((bx + 42.5 * math.cos(a), 700 + 42.5 * math.sin(a)))
body.append((cx - r, cy))  # left side up
# black outline: same shape scaled 1.06 about (512, 560)
ox, oy = 512, 560
outline = [(ox + (x - ox) * 1.06, oy + (y - oy) * 1.06) for (x, y) in body]
d.polygon(outline, fill=(0, 0, 0))
d.polygon(body, fill=(255, 255, 255))
# sparkle eyes
star(455, 480, 32, 9, 4, (0, 0, 0))
star(570, 480, 32, 9, 4, (0, 0, 0))
# magenta coin with white star (held out to the side)
d.ellipse([660 - 58, 630 - 58, 660 + 58, 630 + 58], fill=(230, 0, 126),
          outline=(0, 0, 0), width=5)
star(660, 630, 34, 14, 5, (255, 255, 255))
# round little hand holding the coin
d.ellipse([612 - 26, 672 - 26, 612 + 26, 672 + 26], fill=(255, 255, 255),
          outline=(0, 0, 0), width=4)

# ---- meme text: big white with black stroke ----
def fit_font(text, start, max_w):
    size = start
    while size > 20:
        f = ImageFont.truetype(BOLD, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(BOLD, size)


top = "MY AI AGENT BEAT GTA 6"
f_top = fit_font(top, 84, 940)
d.text((512, 55), top, font=f_top, fill=(255, 255, 255), anchor="mt",
       stroke_width=7, stroke_fill=(0, 0, 0))

f_bot = ImageFont.truetype(BOLD, 62)
d.text((512, 855), "I'M STILL ON THE", font=f_bot, fill=(255, 255, 255),
       anchor="mt", stroke_width=6, stroke_fill=(0, 0, 0))
d.text((512, 925), "TITLE SCREEN", font=f_bot, fill=(255, 255, 255),
       anchor="mt", stroke_width=6, stroke_fill=(0, 0, 0))

img.save("meme.png")
prev = img.resize((480, 480), Image.LANCZOS)
prev.save("meme-480-preview.png")

raw = open("meme.png", "rb").read()
print("meme.png:", img.size, len(raw), "bytes, sha256",
      hashlib.sha256(raw).hexdigest()[:16])
print("top font size:", f_top.size)
