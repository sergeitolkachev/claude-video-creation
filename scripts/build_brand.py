#!/usr/bin/env python3
"""Channel art — crop the approved plates to spec and burn the text in.

Reads brand/approved/<id>.jpg, writes brand/out/<id>.png. Generation never
produces a character: models invent glyphs, and glyphs that drift between a
banner and a thumbnail are what makes a channel look assembled rather than
issued. Every character on this channel comes out of here, in the same Menlo
and with the same tracking as the burned-in episode titles.

    python3 scripts/build_brand.py
    python3 scripts/build_brand.py --record FC9-042   # per-episode thumbnail

Also writes two check plates that are never uploaded: the avatar masked to a
circle, and the banner with its safe area outlined. Both exist because the
crop is the thing that goes wrong and neither is visible in the export.
"""
import sys, pathlib, yaml
from PIL import Image, ImageDraw, ImageFont

FONT = "/System/Library/Fonts/Menlo.ttc"
INK = (232, 230, 224)

def spaced(draw, xy, text, font, tracking, fill):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking

def width_of(draw, text, font, tracking):
    return sum(draw.textlength(c, font=font) + tracking for c in text) - tracking

def zoom_in(im, cfg):
    """Punch in on the plate before cropping to spec. The avatar loses its
    corners to a circle and is shown at 32 px in a comment thread, where the
    only thing that survives is the largest dark shape — so the stamp has to
    be big in frame, and no prompt reliably makes a model put it there."""
    z = cfg["zoom"]
    s = round(min(im.width, im.height) * z)
    x = (im.width - s) // 2
    y = round((im.height - s) * cfg.get("bias_y", 0.5))
    return im.crop((x, y, x + s, y + s))


def cover(im, w, h):
    """Fill w x h without distorting: scale to cover, crop the overflow."""
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))

def scrim(im, box, strength=150):
    """Darken a band so light text holds on a plate that may be pale.
    Feathered on all four edges — a hard edge reads as a graphic element,
    and this has to look like uneven exposure, not like a lower third."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    px = bytearray(w * h)
    for y in range(h):
        v = min(y, h - 1 - y) / (h / 2)          # 0 at the edges, 1 in the middle
        vy = min(1.0, v * 1.6)
        for x in range(w):
            px[y * w + x] = int(strength * (1 - x / w) ** 1.5 * vy)
    mask = Image.frombytes("L", (w, h), bytes(px))
    im.paste(Image.new("RGB", (w, h), (0, 0, 0)), (x0, y0), mask)
    return im


def main():
    args = sys.argv[1:]
    record = args[args.index("--record") + 1] if "--record" in args else None

    brand = yaml.safe_load(pathlib.Path("config/brand.yaml").read_text())
    src = pathlib.Path("brand/approved")
    out = pathlib.Path("brand/out"); out.mkdir(parents=True, exist_ok=True)
    text_cfg = brand["text"]

    for a in brand["assets"]:
        p = src / f"{a['id']}.jpg"
        if not p.exists():
            print(f"  skip   {a['id']:<10} (no brand/approved/{a['id']}.jpg)")
            continue
        w, h = a["export"]["width"], a["export"]["height"]
        im = Image.open(p).convert("RGB")
        if "crop" in a:
            im = zoom_in(im, a["crop"])
        im = cover(im, w, h)
        d = ImageDraw.Draw(im)

        t = text_cfg.get(a["id"])
        if t:
            lines = [record] if record and a["id"] == "thumbnail" else t["lines"]
            f = ImageFont.truetype(FONT, t["size"])
            lh = int(t["size"] * 1.45)
            block_h = lh * len(lines)
            if a["id"] == "banner":
                # Centred in the safe area: everything outside it is cropped
                # away on some device, so the name has to live inside it.
                top = (h - block_h) // 2
                for i, line in enumerate(lines):
                    lw = width_of(d, line, f, t["tracking"])
                    spaced(d, ((w - lw) / 2, top + i * lh), line, f,
                           t["tracking"], INK)
            else:
                # Left third, where the plate was composed empty and dark.
                x, top = int(w * 0.07), int(h * 0.72)
                im = scrim(im, (0, top - 40, int(w * 0.55), top + block_h + 40))
                d = ImageDraw.Draw(im)
                for i, line in enumerate(lines):
                    spaced(d, (x, top + i * lh), line, f, t["tracking"], INK)

        dest = out / f"{a['id']}.png"
        im.save(dest)
        print(f"  built  {a['id']:<10} {w}x{h}  -> {dest}")

        if a["id"] == "avatar":
            mask = Image.new("L", (w, h), 0)
            ImageDraw.Draw(mask).ellipse((0, 0, w - 1, h - 1), fill=255)
            circ = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            circ.paste(im, (0, 0), mask)
            circ.save(out / "avatar-circle-check.png")
            circ.resize((32, 32), Image.LANCZOS).save(out / "avatar-32-check.png")
            print("         + circle and 32 px checks (do not upload)")

        if a["id"] == "banner" and "safe_area" in a:
            g = im.copy(); gd = ImageDraw.Draw(g)
            sw, sh = a["safe_area"]["width"], a["safe_area"]["height"]
            gd.rectangle(((w - sw) // 2, (h - sh) // 2,
                          (w + sw) // 2, (h + sh) // 2), outline=(255, 60, 60), width=4)
            g.save(out / "banner-safe-check.png")
            print(f"         + safe-area check {sw}x{sh} (do not upload)")

if __name__ == "__main__":
    main()
