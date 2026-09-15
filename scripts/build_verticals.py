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


def slug_plate(text, spec, dst, size=34, tracking=None, centre=False):
    """The slug, in the channel's phosphor, with the same halo as a card.

    It does not type on. A card types because its arrival is an event in a
    four-minute record; a twenty-second short has no room for an event that is
    not the shot itself, and a slug is a mark of ownership, not information.

    The same renderer draws the closing card, because every character this
    channel puts on a screen comes out of one renderer in one font — the slug
    at the top of a vertical and the line asking for the full record at the end
    of it are the same furniture, and must not look like two decisions.
    """
    f = spec["font"]
    lines = text if isinstance(text, list) else [text]
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    trk = f["tracking"] if tracking is None else tracking
    safe = spec["captions"].get("safe_width", W - 120)

    # Shrink to fit rather than run off the frame. The closing card shipped
    # clipped at both ends once: 36 characters at size 46 is about 1100 px in a
    # 1080 px frame. Breaking the line is the real fix and lives in the config;
    # this is the guard that makes overflow impossible rather than unlikely.
    while size > 20:
        font = ImageFont.truetype(f["face"], size)
        widest = max(sum(d.textlength(c, font=font) + trk for c in l) - trk
                     for l in lines)
        if widest <= safe:
            break
        size -= 2
    font = ImageFont.truetype(f["face"], size)
    lh = int(size * 1.45)

    for i, line in enumerate(lines):
        w = sum(d.textlength(c, font=font) + trk for c in line) - trk
        if centre:
            x = (W - w) / 2
            y = H / 2 - (lh * len(lines)) / 2 + i * lh
        else:
            x, y = 56, 96 + i * lh
        for ch in line:
            d.text((x, y), ch, font=font, fill=tuple(f["colour"]) + (f["alpha"],))
            x += d.textlength(ch, font=font) + trk
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

    # The closing card. Channel furniture: same words, same length, every cut
    # and every episode, in the same Menlo and the same phosphor as every other
    # character the channel puts on a screen. It is also what lets a cut end on
    # a finished sentence — with a card after it, the last line no longer has
    # to be a cliffhanger to stop a thumb.
    ec = spec["captions"]["end_card"]
    card = slug_plate(ec.get("lines") or ec["text"], spec, out / "_endcard.png",
                      size=ec.get("size"), tracking=ec.get("tracking"),
                      centre=True)

    for cut in cfg["cuts"]:
        if only and cut["id"] != only:
            continue
        a, b = cut["from"], cut["to"]
        dst = out / f"{cut['id']}.mp4"
        span = b - a
        tail = float(ec.get("seconds", 2.0))
        body  = out / f"_{cut['id']}-body.mp4"
        tailf = out / f"_{cut['id']}-tail.mp4"
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
            "-c:a", "aac", "-b:a", "160k", "-pix_fmt", "yuv420p", str(body)],
            check=True)

        # the card, on black, with the room tone still under it so the cut does
        # not fall off a cliff into digital silence
        subprocess.run([
            ff, "-y", "-v", "error",
            "-f", "lavfi", "-i", f"color=c=black:s=1080x1920:r=24:d={tail}",
            "-loop", "1", "-t", str(tail), "-i", str(card),
            "-ss", str(b), "-t", str(tail), "-i", str(src),
            "-filter_complex",
            "[1:v]format=rgba,fade=t=in:st=0.15:d=0.45:alpha=1[c];"
            "[0:v][c]overlay=0:0,setsar=1[v];"
            f"[2:a]volume=-9dB,afade=t=out:st={tail - 0.5:.2f}:d=0.5[a]",
            "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-crf", "20", "-preset", "slow",
            "-c:a", "aac", "-b:a", "160k", "-pix_fmt", "yuv420p", str(tailf)],
            check=True)

        lst = out / f"_{cut['id']}.txt"
        lst.write_text(f"file '{body.name}'\nfile '{tailf.name}'\n")
        subprocess.run([ff, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                        "-i", str(lst), "-c", "copy", str(dst)], check=True)
        for f in (body, tailf, lst):
            f.unlink()
        d = float(subprocess.run(
            [probe, "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(dst)],
            capture_output=True, text=True).stdout.strip())
        print(f"  {cut['id']:<26} {a:6.1f}-{b:<6.1f} {d:5.1f}s  "
              f"{dst.stat().st_size / 1048576:5.1f} MB   ends on "
              f"\"{cut['ends_on']}\" + {tail:.0f}s card")


if __name__ == "__main__":
    main()
