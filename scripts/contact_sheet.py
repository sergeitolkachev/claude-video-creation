#!/usr/bin/env python3
"""Look at the finished thing.

Every gate in this repository reads a file and scores it. None of them looks
at the picture, which is how record 02 shipped three cards cut off mid-word
and record 03 shipped a typewriter that made no sound and a fan 26 dB under
the floor — each one arithmetically defensible, each one obvious at a glance.
This builds that glance: a sheet of frames off the finished master, one per
shot, labelled with its time and its shot id, at a size where a smeared card
or a missing title is visible without hunting.

Two sheets, because they fail differently:

  16:9   one frame per shot, at a third and at two thirds of it, so a card
         that types past the end of its plate shows up as a half-typed line
         in the second frame. The shot id comes from shots.yaml, so a frame
         that looks wrong names the entry to go and fix.

  9:16   a vertical or the teaser, sampled evenly, with the two boundaries
         that matter drawn on it: `captions.bottom_clear` and
         `captions.safe_width` from config/type.yaml. validate.py computes
         those from font metrics and passes or fails; here they are lines
         across the picture, and a caption sitting on one is a caption that
         will be buried on some platform.

Judge these at the size they are built. A 320 px tile is roughly a phone held
at arm's length, which is where this channel is watched.

Usage:
  contact_sheet.py [episode dir]                 every master it can find
  contact_sheet.py [episode dir] --only verticals
  contact_sheet.py [episode dir] --file out/TEASER.mp4
  contact_sheet.py [episode dir] --every 3       9:16 sample interval
"""
import os, pathlib, subprocess, sys, yaml
from PIL import Image, ImageDraw, ImageFont

print = __import__('functools').partial(print, flush=True)

FONT = "/System/Library/Fonts/Menlo.ttc"
TILE_W_WIDE, COLS_WIDE = 320, 5      # 320x180 tiles, five across = 1600 px
TILE_H_TALL, COLS_TALL = 300, 8      # 169x300 tiles, eight across = 1352 px
LABEL_H = 18                         # a strip under each tile, not over it
PAD = 6
INK = (150, 255, 190)                # the channel's phosphor, for the labels
GUIDE = (255, 64, 64)                # not a channel colour: a guide is not art


def ffmpeg():
    return os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")


def duration(path):
    probe = str(pathlib.Path(ffmpeg()).with_name("ffprobe"))
    out = subprocess.run([probe, "-v", "error", "-show_entries",
                          "format=duration", "-of", "default=nw=1:nk=1",
                          str(path)], capture_output=True, text=True).stdout
    return float(out.strip())


def is_tall(path):
    """Ask the file, not its name. The first version read the orientation off
    a filename prefix, which is a naming convention masquerading as a fact —
    it would have sheeted a 9:16 cut as 16:9 the first time one was called
    something else, and silently: the guides simply would not be drawn."""
    probe = str(pathlib.Path(ffmpeg()).with_name("ffprobe"))
    out = subprocess.run([probe, "-v", "error", "-select_streams", "v:0",
                          "-show_entries", "stream=width,height",
                          "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True).stdout.strip()
    w, h = (int(v) for v in out.split(",")[:2])
    return h > w


def grab(src, t, w, h, dst):
    """One frame at t, already scaled to the tile. Input-side -ss so a
    four-minute master does not get decoded forty times from the top."""
    subprocess.run([ffmpeg(), "-y", "-v", "error", "-ss", f"{t:.3f}",
                    "-i", str(src), "-frames:v", "1",
                    "-vf", f"scale={w}:{h}:flags=bilinear", str(dst)],
                   check=True)
    return Image.open(dst).convert("RGB")


def shot_windows(ep):
    """(start, end, id) per shot, summed off timeline_seconds — the same field
    validate.py sums, never a duration parsed out of prose."""
    f = ep / "shots.yaml"
    if not f.exists():
        return []
    acc, rows = 0.0, []
    for s in yaml.safe_load(f.read_text())["shots"]:
        d = float(s.get("timeline_seconds", s.get("generate_seconds", 0)))
        rows.append((acc, acc + d, str(s["id"])))
        acc += d
    return rows


def wide_samples(ep, total):
    """Two frames per shot. One is not enough: a card types on over several
    seconds, so the fault is in the second half of the plate, not the first."""
    rows = shot_windows(ep)
    if not rows:
        return [(t, "") for t in frange(0, total, 4.0)]
    out = []
    for a, b, sid in rows:
        if a >= total:
            break
        for frac in (0.33, 0.72):
            t = a + (b - a) * frac
            if t < total:
                out.append((t, sid))
    return out


def frange(a, b, step):
    t = a
    while t < b:
        yield t
        t += step


def label(d, x, y, text, size=13, tracking=1.0, fill=INK):
    font = ImageFont.truetype(FONT, size)
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking


def sheet(src, dst, samples, tile, cols, guides=None, title=""):
    tw, th = tile
    rows = (len(samples) + cols - 1) // cols
    W = PAD + cols * (tw + PAD)
    H = PAD + 26 + rows * (th + LABEL_H + PAD)
    sh = Image.new("RGB", (W, H), (16, 16, 18))
    d = ImageDraw.Draw(sh)
    label(d, PAD + 2, 6, title, size=15, tracking=1.5)

    tmp = dst.parent / "_frame.png"
    for n, (t, tag) in enumerate(samples):
        col, row = n % cols, n // cols
        x = PAD + col * (tw + PAD)
        y = PAD + 26 + row * (th + LABEL_H + PAD)
        im = grab(src, t, tw, th, tmp)
        if guides:
            g = ImageDraw.Draw(im)
            clear_y = int(th * (1.0 - guides["bottom_clear"]))
            g.line([(0, clear_y), (tw, clear_y)], fill=GUIDE, width=1)
            half = int(tw * guides["safe_width"] / 2)
            g.line([(tw // 2 - half, 0), (tw // 2 - half, clear_y)],
                   fill=GUIDE, width=1)
            g.line([(tw // 2 + half, 0), (tw // 2 + half, clear_y)],
                   fill=GUIDE, width=1)
        sh.paste(im, (x, y))
        mm, ss = divmod(t, 60)
        stamp = f"{int(mm):d}:{ss:05.2f}" + (f"  {tag}" if tag else "")
        label(d, x + 1, y + th + 3, stamp)
    if tmp.exists():
        tmp.unlink()
    sh.save(dst, quality=92)
    return sh.size


def main():
    args = sys.argv[1:]
    only, one_file, every = None, None, 2.5
    if "--only" in args:
        i = args.index("--only"); only = args[i + 1]; del args[i:i + 2]
    if "--file" in args:
        i = args.index("--file"); one_file = args[i + 1]; del args[i:i + 2]
    if "--every" in args:
        i = args.index("--every"); every = float(args[i + 1]); del args[i:i + 2]
    ep = pathlib.Path(args[0] if args else "episodes/ep-03-carbon-balance")
    if not ep.exists():
        sys.exit(f"no {ep}")

    spec = yaml.safe_load(pathlib.Path("config/type.yaml").read_text())
    cap = spec["captions"]
    guides = {"bottom_clear": float(cap["bottom_clear"]),
              "safe_width": float(cap["safe_width"]) / 1080.0}

    out = ep / "out" / "contact"; out.mkdir(parents=True, exist_ok=True)

    # What to sheet. The masters are 16:9 and get the per-shot sample; every
    # vertical and the teaser are 9:16 and get the safe-area guides.
    jobs = []
    if one_file:
        p = pathlib.Path(one_file)
        if not p.is_absolute():
            p = ep / one_file
        jobs.append((p, is_tall(p)))
    else:
        for name in ("EPISODE-final.mp4", "EPISODE-clean.mp4"):
            p = ep / "out" / name
            if p.exists() and only in (None, "master"):
                jobs.append((p, is_tall(p)))
        if only in (None, "teaser"):
            p = ep / "out" / "TEASER.mp4"
            if p.exists():
                jobs.append((p, is_tall(p)))
        if only in (None, "verticals"):
            for p in sorted((ep / "out" / "verticals").glob("*.mp4")):
                if not p.name.startswith("_"):
                    jobs.append((p, is_tall(p)))

    if not jobs:
        sys.exit("nothing to sheet — no masters found under out/")

    for src, tall in jobs:
        total = duration(src)
        if tall:
            samples = [(t, "") for t in frange(0.2, total, every)]
            tile, cols, g = (int(TILE_H_TALL * 9 / 16), TILE_H_TALL), COLS_TALL, guides
        else:
            samples = wide_samples(ep, total)
            tile, cols, g = (TILE_W_WIDE, int(TILE_W_WIDE * 9 / 16)), COLS_WIDE, None
        dst = out / f"{src.stem}.jpg"
        title = (f"{src.name}   {total:.2f}s   {len(samples)} frames"
                 + ("   guides: bottom_clear / safe_width" if g else
                    "   one frame at 1/3 and 2/3 of every shot"))
        size = sheet(src, dst, samples, tile, cols, g, title)
        print(f"  {dst.relative_to(ep)}   {size[0]}x{size[1]}   "
              f"{len(samples)} frames off {total:.1f}s")

    print(f"\n  {len(jobs)} sheet(s) in {out}")
    print("  Look at them before publishing. Cards typed past their plate, a "
          "title that\n  drew nothing, a caption on the red line — none of "
          "that fails a check.")


if __name__ == "__main__":
    main()
