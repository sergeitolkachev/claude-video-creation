#!/usr/bin/env python3
"""Thumbnail variants for A/B, built from approved stills.

Nothing is generated here. The plate is a frame the episode actually contains,
cropped to 1280x720, and every character is burned in with the same Menlo and
tracking as the episode titles and the banner.

Variants exist to be swapped in YouTube Studio a week at a time, so they are
built together and named by variant id — the id is what a conversion number
later gets attached to.

    python3 scripts/build_thumbs.py episodes/ep-01-tishina-9
"""
import sys, pathlib, yaml
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/System/Library/Fonts/Menlo.ttc"
INK = (232, 230, 224)
SLUG_SIZE = 26
SLUG_TRACKING = 5

def spaced(draw, xy, text, font, tracking, fill):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking

def width_of(draw, text, font, tracking):
    return sum(draw.textlength(c, font=font) + tracking for c in text) - tracking

def zoom_in(im, cfg):
    """Punch in on the plate. A shot composed for 4 seconds of screen time is
    almost always too loose for a frame that has to land in a 210 px grid."""
    z = cfg["zoom"]
    w, h = round(im.width * z), round(im.height * z)
    # bias_x as well as bias_y: a subject that is centred in a 16:9 shot is
    # not necessarily what the crop should be built around. Record 02's animal
    # sits left of centre and disappears at grid size if the crop is centred.
    x = round((im.width - w) * cfg.get("bias_x", 0.5))
    y = round((im.height - h) * cfg.get("bias_y", 0.5))
    return im.crop((x, y, x + w, y + h))

def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))

def darken(im, box, strength=165):
    """Feathered darkening under a text block. Hard-edged boxes read as a
    lower third; this has to read as uneven exposure."""
    x0, y0, x1, y1 = (max(0, int(box[0])), max(0, int(box[1])),
                      min(im.width, int(box[2])), min(im.height, int(box[3])))
    w, h = x1 - x0, y1 - y0
    if w <= 0 or h <= 0:
        return im
    px = bytearray(w * h)
    for y in range(h):
        vy = min(1.0, (min(y, h - 1 - y) / (h / 2)) * 1.6)
        for x in range(w):
            px[y * w + x] = int(strength * (1 - x / w) ** 1.4 * vy)
    mask = Image.frombytes("L", (w, h), bytes(px))
    im.paste(Image.new("RGB", (w, h), (0, 0, 0)), (x0, y0), mask)
    return im

def dim_region(im, cfg, W, H):
    """Multiply a rectangle of the plate down, feathered at the edges.

    The CRT plate is a bright washed screen, and phosphor-green text on it
    disappears at the 210 px YouTube actually shows. A real tube is bright
    text on a dark screen, so the screen is dimmed first and the text put
    back on top — the same fix a colourist would make, not a text colour
    change that would break the in-world reading."""
    x0, y0 = int(W * cfg["x0"]), int(H * cfg["y0"])
    x1, y1 = int(W * cfg["x1"]), int(H * cfg["y1"])
    w, h = x1 - x0, y1 - y0
    k = cfg.get("strength", 0.55)          # 0 = untouched, 1 = black
    feather = cfg.get("feather", 0.18)
    px = bytearray(w * h)
    for y in range(h):
        fy = min(1.0, min(y, h - 1 - y) / (h * feather))
        for x in range(w):
            fx = min(1.0, min(x, w - 1 - x) / (w * feather))
            px[y * w + x] = int(255 * k * fx * fy)
    im.paste(Image.new("RGB", (w, h), (0, 0, 0)),
             (x0, y0), Image.frombytes("L", (w, h), bytes(px)))
    return im


def draw_block(im, b, W, H):
    f = ImageFont.truetype(FONT, b["size"])
    lines, tr = b["lines"], b.get("tracking", 6)
    lh = int(b["size"] * 1.28)
    d = ImageDraw.Draw(im)
    widest = max(width_of(d, l, f, tr) for l in lines)
    top = int(H * b["y"])
    left = int(W * b["x"])
    if b.get("anchor") == "centre":
        left = int(W * b["x"] - widest / 2)

    if b.get("scrim"):
        pad = int(b["size"] * 0.8)
        im = darken(im, (0 if b["x"] < 0.2 else left - pad, top - pad,
                         left + widest + pad * 2, top + lh * len(lines) + pad))

    colour = tuple(b.get("color", INK))
    if b.get("glow"):
        # Phosphor bleeds into the glass. Text sitting on a CRT without it
        # looks stuck on top of the photograph.
        halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        hd = ImageDraw.Draw(halo)
        for i, line in enumerate(lines):
            lx = int(W * b["x"] - width_of(hd, line, f, tr) / 2) \
                 if b.get("anchor") == "centre" else left
            spaced(hd, (lx, top + i * lh), line, f, tr, colour + (190,))
        halo = halo.filter(ImageFilter.GaussianBlur(b["glow"]))
        im = Image.alpha_composite(im.convert("RGBA"), halo).convert("RGB")

    d = ImageDraw.Draw(im)
    for i, line in enumerate(lines):
        lx = int(W * b["x"] - width_of(d, line, f, tr) / 2) \
             if b.get("anchor") == "centre" else left
        spaced(d, (lx, top + i * lh), line, f, tr, colour)
    return im

def main():
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1
                      else "episodes/ep-01-tishina-9")
    doc = yaml.safe_load((ep / "thumbnails.yaml").read_text())
    W, H = doc["export"]["width"], doc["export"]["height"]
    out = ep / "out" / "thumbs"; out.mkdir(parents=True, exist_ok=True)

    for v in doc["variants"]:
        plate = ep / "approved" / f"{v['plate']}.jpg"
        if not plate.exists():
            print(f"  skip  {v['id']:<12} (no {plate})"); continue
        im = Image.open(plate).convert("RGB")
        if "crop" in v:
            im = zoom_in(im, v["crop"])
        im = cover(im, W, H)
        if "dim" in v:
            im = dim_region(im, v["dim"], W, H)
        for b in v["blocks"]:
            im = draw_block(im, b, W, H)

        # The record slug is constant across variants — it is channel
        # furniture, not part of what is being tested.
        f = ImageFont.truetype(FONT, SLUG_SIZE)
        d = ImageDraw.Draw(im)
        sw = width_of(d, doc["slug"], f, SLUG_TRACKING)
        x, y = int(W * 0.05), int(H - SLUG_SIZE * 2.6)
        im = darken(im, (0, y - 18, int(x + sw + 60), y + SLUG_SIZE + 18), 150)
        d = ImageDraw.Draw(im)
        spaced(d, (x, y), doc["slug"], f, SLUG_TRACKING, INK)

        dest = out / f"{v['id']}.png"
        im.save(dest)
        print(f"  built {v['id']:<12} plate {v['plate']}  -> {dest}")

if __name__ == "__main__":
    main()
