#!/usr/bin/env python3
"""Stage 9 — the vertical cuts.

Each episode's cuts live in its own verticals.yaml, with the window, what the
cut lands on, and why it exists. This script only executes them.

Record 01 cropped from the finished master, cards and titles included. Record
02 does not: a data card is composed for the lower left of a 16:9 frame, and
a 9:16 crop takes 608 px of width out of 1920, so a card arrives with its
labels intact and its numbers gone. Verticals are cut from EPISODE-clean.mp4
— the same grade and the same grain, nothing laid over it — and carry only the
slug.

The crop is 608x1080 scaled to 1080x1920, a 1.78x upscale that CLAUDE.md
otherwise forbids. A 9:16 frame cannot come out of a 16:9 master any other
way, and cropping without scaling would deliver a 608-wide short.

Usage: build_verticals.py [episode dir] [--only fc9-002-b-the-line]
"""
import os, pathlib, subprocess, sys, yaml
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
print = __import__('functools').partial(print, flush=True)


def slug_plate(text, spec, dst):
    """The slug, in the channel's phosphor, with the same halo as a card.

    It does not type on. A card types because its arrival is an event in a
    four-minute record; a twenty-second short has no room for an event that is
    not the shot itself, and a slug is a mark of ownership, not information.
    """
    f = spec["font"]
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(f["face"], 34)
    x, y = 56, 96
    for ch in text:
        d.text((x, y), ch, font=font, fill=tuple(f["colour"]) + (f["alpha"],))
        x += d.textlength(ch, font=font) + f["tracking"]
    a = img.split()[3]
    halo = Image.new("RGBA", img.size, (0, 0, 0, 0))
    halo.putalpha(a.filter(ImageFilter.GaussianBlur(f.get("halo_radius", 9)))
                   .point(lambda v: int(v * f.get("halo_alpha", 170) / 255)))
    glow = img.filter(ImageFilter.GaussianBlur(f.get("glow_radius", 7)))
    glow.putalpha(glow.split()[3].point(
        lambda v: int(v * f.get("glow_alpha", 150) / 255)))
    Image.alpha_composite(Image.alpha_composite(halo, glow), img).save(dst)
    return dst


def main():
    args = sys.argv[1:]
    only = None
    if "--only" in args:
        i = args.index("--only"); only = args[i + 1]; del args[i:i + 2]
    ep = pathlib.Path(args[0] if args else "episodes/ep-02-sunrise-line")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    probe = str(pathlib.Path(ff).with_name("ffprobe"))

    cfg = yaml.safe_load((ep / "verticals.yaml").read_text())
    spec = yaml.safe_load(pathlib.Path("config/type.yaml").read_text())
    src = ep / cfg["source"]
    if not src.exists():
        sys.exit(f"no {src} — run grade.py --clean first")

    out = ep / "out" / "verticals"; out.mkdir(parents=True, exist_ok=True)
    plate = slug_plate(cfg["slug"], spec, out / "_slug.png")

    for cut in cfg["cuts"]:
        if only and cut["id"] != only:
            continue
        a, b = cut["from"], cut["to"]
        dst = out / f"{cut['id']}.mp4"
        span = b - a
        subprocess.run([
            ff, "-y", "-v", "error", "-ss", str(a), "-to", str(b), "-i", str(src),
            "-loop", "1", "-t", str(span), "-i", str(plate),
            "-filter_complex",
            "[0:v]crop=608:1080:(iw-608)/2:0,scale=1080:1920:flags=lanczos,"
            "setsar=1[v0];"
            # the slug fades in once and stays: it is furniture, not an event
            f"[1:v]format=rgba,fade=t=in:st=0.4:d=0.8:alpha=1[s];"
            f"[v0][s]overlay=0:0[v]",
            "-map", "[v]", "-map", "0:a",
            # A hard cut in the picture, never in the audio: a quarter-second
            # fade stops the last half-word sounding like a dropped connection.
            "-af", f"afade=t=out:st={span - 0.25:.2f}:d=0.25",
            "-c:v", "libx264", "-crf", "20", "-preset", "slow", "-tune", "grain",
            "-c:a", "aac", "-b:a", "160k", "-pix_fmt", "yuv420p", str(dst)],
            check=True)
        d = float(subprocess.run(
            [probe, "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(dst)],
            capture_output=True, text=True).stdout.strip())
        print(f"  {cut['id']:<26} {a:6.1f}-{b:<6.1f} {d:5.1f}s  "
              f"{dst.stat().st_size / 1048576:5.1f} MB   ends on "
              f"\"{cut['ends_on']}\"")


if __name__ == "__main__":
    main()
