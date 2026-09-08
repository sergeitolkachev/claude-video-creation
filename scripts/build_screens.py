#!/usr/bin/env python3
"""Composite the delay readout onto the CRT plates.

The number is drawn onto the still, not onto the finished clip. Both shots that
show this screen are then built locally from the composited plate, so the
readout travels with the push exactly — there is nothing to track, because the
number is part of the frame before any motion is applied.

The screen rectangle was measured from the plates themselves (the phosphor glow
is the only strongly green region): x 300..922, y 103..626 on both, which is
also the proof that 1.2 and 4.3 really are the same screen.
"""
import pathlib, yaml
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/System/Library/Fonts/Menlo.ttc"
SCREEN = (300, 103, 922, 626)          # x0, y0, x1, y1
PHOSPHOR = (past := (150, 255, 190))   # slightly blue-green, like the plate

def draw_readout(plate: Image.Image, label: str, value: str) -> Image.Image:
    x0, y0, x1, y1 = SCREEN
    w, h = x1 - x0, y1 - y0
    layer = Image.new("RGBA", plate.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    f_small = ImageFont.truetype(FONT, int(h * 0.10))
    f_big   = ImageFont.truetype(FONT, int(h * 0.26))
    cx = x0 + w / 2
    lw = d.textlength(label, font=f_small)
    vw = d.textlength(value, font=f_big)
    d.text((cx - lw / 2, y0 + h * 0.30), label, font=f_small, fill=PHOSPHOR + (170,))
    d.text((cx - vw / 2, y0 + h * 0.44), value, font=f_big,   fill=PHOSPHOR + (215,))
    # phosphor bleeds: a blurred copy under the sharp one
    glow = layer.filter(ImageFilter.GaussianBlur(9))
    out = plate.convert("RGBA")
    out = Image.alpha_composite(out, glow)
    out = Image.alpha_composite(out, layer)
    return out.convert("RGB")

def main():
    ep = pathlib.Path("episodes/ep-01-tishina-9")
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    for s in doc["shots"]:
        txt = s.get("screen_text")
        if not txt:
            continue
        src = ep / "approved" / f"{s['id']}.jpg"
        dst = ep / "approved" / f"{s['id']}.screen.jpg"
        im = draw_readout(Image.open(src), txt["label"], txt["value"])
        im.save(dst, quality=95)
        print(f"  {s['id']}  {txt['label']} {txt['value']}  -> {dst.name}")

if __name__ == "__main__":
    main()
