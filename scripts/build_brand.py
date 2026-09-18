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
import sys, random, pathlib, yaml
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

FONT = "/System/Library/Fonts/Menlo.ttc"
INK = (232, 230, 224)

def spaced(draw, xy, text, font, tracking, fill):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking

def width_of(draw, text, font, tracking):
    return sum(draw.textlength(c, font=font) + tracking for c in text) - tracking

def ink_mask(w, h, seed, coarse=9, bias=118):
    """A rubber stamp does not print evenly — the ink sits in the paper's
    tooth and skips where it does not. Blurred noise thresholded into a
    patchy field, multiplied into the glyph alpha.

    Seeded, so a rebuild of the avatar is byte-identical to the last one. A
    stamp that is slightly different every build is a stamp the audience
    would notice changing and never be able to say why."""
    rnd = random.Random(seed)
    small = Image.frombytes("L", (max(1, w // coarse), max(1, h // coarse)),
                            bytes(rnd.randrange(256)
                                  for _ in range((w // coarse or 1) * (h // coarse or 1))))
    field = small.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(2))
    return field.point(lambda v: 255 if v > bias else int(v * 1.6))


def lighten(im, box, amount, feather=0.28):
    """Push a region of the plate back toward the paper around it, so a new
    stamp has somewhere to land. Used only where the plate already carries
    an ink blot the mark has to sit on top of."""
    x0, y0, x1, y1 = (int(v) for v in box)
    region = im.crop((x0, y0, x1, y1))
    # Sample the paper just outside the region. A guessed beige lands lighter
    # or cooler than the plate and the fill reads as a patch rather than as
    # paper — which is exactly what the first pass did.
    ring = im.crop((max(0, x0 - 60), max(0, y0 - 60), x1 + 60, y1 + 60)) \
             .resize((1, 1), Image.LANCZOS).getpixel((0, 0))
    paper = Image.new("RGB", region.size, ring)
    w, h = region.size
    px = bytearray(w * h)
    for y in range(h):
        fy = min(1.0, min(y, h - 1 - y) / (h * feather))
        for x in range(w):
            fx = min(1.0, min(x, w - 1 - x) / (w * feather))
            px[y * w + x] = int(255 * amount * fx * fy)
    region.paste(paper, (0, 0), Image.frombytes("L", (w, h), bytes(px)))
    im.paste(region, (x0, y0))
    return im


def clone_patch(im, cfg, W, H):
    """Cover a region with clean paper taken from elsewhere on the same plate.

    Filling with a sampled colour was the obvious move and it is wrong: flat
    colour has no grain, so the fill reads as a square of paint on a
    photograph no matter how well the hue is matched. Cloning carries the
    paper's own grain, specks and tone across, which is what makes the patch
    disappear."""
    x0, y0 = int(W * cfg["x0"]), int(H * cfg["y0"])
    x1, y1 = int(W * cfg["x1"]), int(H * cfg["y1"])
    w, h = x1 - x0, y1 - y0
    src = im.crop((x0 + int(W * cfg.get("dx", 0)), y0 + int(H * cfg.get("dy", 0)),
                   x1 + int(W * cfg.get("dx", 0)), y1 + int(H * cfg.get("dy", 0))))
    feather = cfg.get("feather", 0.22)
    px = bytearray(w * h)
    for y in range(h):
        fy = min(1.0, min(y, h - 1 - y) / (h * feather))
        for x in range(w):
            fx = min(1.0, min(x, w - 1 - x) / (w * feather))
            px[y * w + x] = int(255 * fx * fy)
    im.paste(src, (x0, y0), Image.frombytes("L", (w, h), bytes(px)))
    return im


def stamp(im, cfg, W, H):
    """Burn a Menlo mark onto the plate as ink.

    Not drawn straight onto the image: the glyphs are rendered on their own
    layer, distressed, rotated off the grid and multiplied down, so the
    paper's grain and the folder's shading come through the ink the way they
    do through the stamp already on the plate. Text drawn flat reads as a
    caption sitting on the photograph."""
    for c in cfg.get("clone", []):
        im = clone_patch(im, c, W, H)
    if "lighten" in cfg:
        l = cfg["lighten"]
        im = lighten(im, (W * l["x0"], H * l["y0"], W * l["x1"], H * l["y1"]),
                     l.get("amount", 0.5), l.get("feather", 0.28))

    f = ImageFont.truetype(FONT, cfg["size"])
    tr = cfg.get("tracking", 0)
    pad = cfg["size"]
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    tw = int(width_of(probe, cfg["text"], f, tr))
    layer = Image.new("L", (tw + pad * 2, int(cfg["size"] * 1.6) + pad * 2), 0)
    spaced(ImageDraw.Draw(layer), (pad, pad), cfg["text"], f, tr, 255)

    if cfg.get("box"):
        b = cfg["box"]
        d = ImageDraw.Draw(layer)
        m = int(cfg["size"] * b.get("margin", 0.45))
        d.rectangle((pad - m, pad - m * 0.6,
                     pad + tw + m, pad + cfg["size"] * 1.25 + m * 0.6),
                    outline=255, width=b.get("width", 5))

    layer = ImageChops.multiply(layer, ink_mask(*layer.size, seed=cfg.get("seed", 7),
                                                bias=cfg.get("ink", 118)))
    layer = layer.filter(ImageFilter.GaussianBlur(cfg.get("blur", 1.1)))
    layer = layer.rotate(cfg.get("rotate", 0), resample=Image.BICUBIC, expand=True)
    layer = layer.point(lambda v: int(v * cfg.get("alpha", 0.86)))

    x = int(W * cfg["x"] - layer.width / 2)
    y = int(H * cfg["y"] - layer.height / 2)
    im.paste(Image.new("RGB", layer.size, tuple(cfg.get("color", (38, 40, 42)))),
             (x, y), layer)
    return im


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

        marks = {m["id"]: m for m in brand.get("avatar_marks", [])}
        chosen = a.get("mark")
        if chosen:
            im = stamp(im, marks[chosen], w, h)

        dest = out / f"{a['id']}.png"
        im.save(dest)
        print(f"  built  {a['id']:<10} {w}x{h}  -> {dest}")

        if a["id"] == "avatar" and not a.get("mark"):
            for m in brand.get("avatar_marks", []):
                cand = stamp(im.copy(), m, w, h)
                cand.save(out / f"avatar-mark-{m['id']}.png")
            if brand.get("avatar_marks"):
                print("         + %d mark candidates (pick one into avatar.mark)"
                      % len(brand["avatar_marks"]))

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
