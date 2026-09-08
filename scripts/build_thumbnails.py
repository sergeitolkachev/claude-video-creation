#!/usr/bin/env python3
"""Three thumbnail variants, 1280x720.

Per script.md: the base is shot 5.3, the point among the stars, with the delay
figure large. No faces, no arrows. Two alternates are cut from other moments so
there is something to swap to if CTR sits under 4% on the first day.

Frames are pulled from the graded master, not from the approved stills, so the
thumbnail matches what a viewer actually sees when they click.
"""
import os, subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/System/Library/Fonts/Menlo.ttc"
W, H = 1280, 720
INK = (236, 233, 226)

# Times are checked against both the shot layout and the title windows, so no
# frame here carries a burned-in card that would double the thumbnail's own
# type. Shot 5.3 runs 183-195, 4.3 runs 127-136, 4.1 runs 110-119.
VARIANTS = [
    # id,          time,  headline,          sub,          pos
    ("a-point",   189.0, "DELAY: 00:04:17", "",           "centre"),
    # the readout is already on the screen in this frame — the thumbnail only
    # names the record, it does not repeat the number
    ("b-readout", 133.5, "LOG 047",         "TISHINA-9",  "lower-left"),
    ("c-porthole", 116.5, "DELAY: 00:04:17", "TISHINA-9", "lower-left"),
]

def spaced(d, xy, text, font, tracking, fill):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking

def width_of(d, text, font, tracking):
    return sum(d.textlength(c, font=font) + tracking for c in text)

def main():
    ep = pathlib.Path("episodes/ep-01-tishina-9")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    src = ep / "out" / "EPISODE-final.mp4"
    out = ep / "out" / "thumbnails"; out.mkdir(parents=True, exist_ok=True)

    for vid, t, head, sub, pos in VARIANTS:
        tmp = f"/tmp/thumb_{vid}.png"
        subprocess.run([ff, "-y", "-v", "error", "-ss", str(t), "-i", str(src),
                        "-frames:v", "1", "-vf", f"scale={W}:{H}", tmp], check=True)
        im = Image.open(tmp).convert("RGB")
        # darken slightly so type holds against the image
        im = Image.eval(im, lambda p: int(p * 0.88))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        fh = ImageFont.truetype(FONT, 72 if pos == "centre" else 58)
        fs = ImageFont.truetype(FONT, 26)
        tr = 5
        hw = width_of(d, head, fh, tr)
        if pos == "centre":
            hx, hy = (W - hw) / 2, H * 0.60
        else:
            hx, hy = 70, H - 190
        spaced(d, (hx, hy), head, fh, tr, INK + (245,))
        if sub:
            spaced(d, (hx + 4, hy + 82), sub, fs, 4, INK + (185,))
        glow = layer.filter(ImageFilter.GaussianBlur(14))
        base = im.convert("RGBA")
        base = Image.alpha_composite(base, glow)
        base = Image.alpha_composite(base, layer)
        p = out / f"thumb-{vid}.jpg"
        base.convert("RGB").save(p, quality=92)
        print(f"  {p.name:<20} кадр {t:6.1f}s   {head}")

if __name__ == "__main__":
    main()
