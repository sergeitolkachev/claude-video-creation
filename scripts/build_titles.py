#!/usr/bin/env python3
"""Stage 8, part one — render the burned-in titles as transparent PNGs.

Rendered in Pillow rather than with drawtext because these are monospace record
numbers and the letter-spacing matters; drawtext cannot set tracking. Each card
is a full-frame RGBA plate that ffmpeg then overlays on the graded footage.
"""
import pathlib, yaml
from PIL import Image, ImageDraw, ImageFont

FONT = "/System/Library/Fonts/Menlo.ttc"
W, H = 1920, 1080
INK = (232, 230, 224)

def spaced(draw, xy, text, font, tracking, fill):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking

def card(lines, size=34, tracking=2.5, pos="lower-left", alpha=225):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FONT, size)
    lh = int(size * 1.45)
    if pos == "lower-left":
        x, y = 120, H - 120 - lh * len(lines)
    else:                                  # centred block
        widest = max(sum(d.textlength(c, font=f) + tracking for c in l) for l in lines)
        x, y = (W - widest) / 2, (H - lh * len(lines)) / 2
    for i, line in enumerate(lines):
        if pos == "centre":
            wid = sum(d.textlength(c, font=f) + tracking for c in line)
            lx = (W - wid) / 2
        else:
            lx = x
        spaced(d, (lx, y + i * lh), line, f, tracking, INK + (alpha,))
    return im

def main():
    ep = pathlib.Path("episodes/ep-01-tishina-9")
    out = ep / "out" / "titles"; out.mkdir(parents=True, exist_ok=True)
    cards = yaml.safe_load((ep / "titles.yaml").read_text())["cards"]
    for c in cards:
        im = card(c["lines"], size=c.get("size", 34),
                  pos=c.get("pos", "lower-left"), alpha=c.get("alpha", 225))
        p = out / f"{c['id']}.png"; im.save(p)
        print(f"  {c['id']:<12} {c['at']:>6.1f}s +{c['hold']:.1f}s  {' / '.join(c['lines'])}")
    print(f"\n{len(cards)} cards -> {out}")

if __name__ == "__main__":
    main()
