#!/usr/bin/env python3
"""Stage 9b — the thirty-second teaser, assembled from teaser.yaml.

Not a cut of the record. The verticals are carved out of the finished episode
and keep its order; the teaser is built from scratch out of the shots where
something physically moves and the lines that escalate on their own, and it is
the one piece on this channel allowed a rising bed under it.

Three things it must not do, all of them enforced by what it is given rather
than by a check here:

  - speak a line the record does not contain. Every line is a take already in
    audio/narration/, already approved, already reproducible from its seed.
  - show a frame the record does not contain. Every shot is a take already in
    takes/, and the picture comes from EPISODE-clean.mp4's own source clips.
  - carry licensed music. The bed is generated (see teaser_sfx in audio.yaml);
    a Content ID claim on a channel built out of recovered recordings costs
    more than any track is worth.

Usage: build_teaser.py [episode dir]
"""
import importlib.util, json, os, pathlib, subprocess, sys, yaml
from PIL import Image, ImageDraw, ImageFilter, ImageFont

print = __import__('functools').partial(print, flush=True)

# 9:16. The teaser is a vertical because that is where a teaser is seen — it
# competes with a scrolling thumb, not with a subscription page. Which makes it
# a vertical in every other sense too: captions are mandatory, the bottom 30%
# stays clear, and it opens on a voice inside a second.
W, H = 1080, 1920
SRC_W, SRC_H = 1920, 1080
CROP_W = 608                     # of 1920, the same centre-safe crop as the cuts

_spec = importlib.util.spec_from_file_location("bc", "scripts/build_captions.py")
bc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(bc)


def dur(ff, p):
    probe = str(pathlib.Path(ff).with_name("ffprobe"))
    return float(subprocess.run(
        [probe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(p)], capture_output=True, text=True).stdout)


def text_plate(lines, spec, dst, size, y_centre=True, x=None, y=None):
    """Channel type on transparency — the same renderer as every other
    character this channel puts on a screen, so the teaser's card and the
    record's cards cannot drift apart."""
    f = spec["font"]
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(f["face"], size)
    trk = f["tracking"]
    lh = int(size * 1.5)
    for i, line in enumerate(lines):
        w = sum(d.textlength(c, font=font) + trk for c in line) - trk
        px = (W - w) / 2 if x is None else x
        py = (H / 2 - lh * len(lines) / 2 + i * lh) if y_centre else y + i * lh
        for ch in line:
            d.text((px, py), ch, font=font, fill=tuple(f["colour"]) + (f["alpha"],))
            px += d.textlength(ch, font=font) + trk
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
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1
                      else "episodes/ep-03-carbon-balance")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    cfg = yaml.safe_load((ep / "teaser.yaml").read_text())
    spec = yaml.safe_load(pathlib.Path("config/type.yaml").read_text())
    picks = yaml.safe_load((ep / "audio" / "narration.yaml").read_text())["picks"]
    lv = cfg["levels"]
    total = float(cfg["runtime_seconds"])
    out = ep / "out"; out.mkdir(parents=True, exist_ok=True)
    tmp = out / "_teaser"; tmp.mkdir(exist_ok=True)

    # --- picture: each shot trimmed out of its own take ---------------------
    parts = []
    for s in cfg["shots"]:
        src = ep / "takes" / f"{s['id']}.mp4"
        if not src.exists():
            sys.exit(f"no take for shot {s['id']}")
        dst = tmp / f"p{len(parts):02d}.mp4"
        subprocess.run([
            ff, "-y", "-v", "error", "-ss", str(s["from"]), "-i", str(src),
            "-t", str(s["seconds"]),
            "-vf", (f"scale={SRC_W}:-2,crop={SRC_W}:{SRC_H}:(iw-{SRC_W})/2:(ih-{SRC_H})/2,"
                    f"crop={CROP_W}:{SRC_H}:(iw-{CROP_W})/2:0,"
                    f"scale={W}:{H}:flags=lanczos,setsar=1,fps=24"),
            "-an", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", str(dst)],
            check=True)
        parts.append(dst)
        print(f"  {s['id']:<5} {s['seconds']:4.1f}s from {s['from']:4.1f}s")

    # the closing card, on black, same length as it is given
    ec = cfg["end_card"]
    card = text_plate(ec["lines"], spec, tmp / "card.png", size=64)
    cdst = tmp / "p99.mp4"
    subprocess.run([
        ff, "-y", "-v", "error",
        "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r=24:d={ec['seconds']}",
        "-loop", "1", "-t", str(ec["seconds"]), "-i", str(card),
        "-filter_complex", "[1:v]format=rgba,fade=t=in:st=0.2:d=0.5:alpha=1[c];"
                           "[0:v][c]overlay=0:0,setsar=1[v]",
        "-map", "[v]", "-c:v", "libx264", "-crf", "18",
        "-pix_fmt", "yuv420p", str(cdst)], check=True)
    parts.append(cdst)

    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p.name}'\n" for p in parts))
    joined = tmp / "joined.mp4"
    subprocess.run([ff, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c", "copy", str(joined)], check=True)

    # --- captions, from the same word timings the record's cuts use ---------
    # Mandatory, because this is a vertical: it is watched muted first and read
    # second. They are built from audio/alignment/, offset by where each line
    # sits on the teaser's own timeline, so they cannot drift from the voice.
    align = ep / "audio" / "alignment"
    cues, ov, fc0, idx0 = [], [], [], 1
    for ln in cfg["lines"]:
        j = align / f"{ln['pid']}_s{picks[ln['pid']]}.json"
        if not j.exists():
            print(f"  no alignment for {ln['pid']} — run build_captions.py first")
            continue
        words = json.loads(j.read_text())
        if ln.get("trim"):
            words = [w for w in words if w["e"] <= float(ln["trim"]) + 0.01]
        for c in bc.chunk(words):
            if not c:
                continue
            cues.append((float(ln["at"]) + c[0]["t"],
                         float(ln["at"]) + c[-1]["e"] + 0.25,
                         " ".join(x["w"] for x in c)))
    # A cue holds 0.25 s past its last word so a short line does not blink —
    # but never past the next cue's first word, or two captions draw at once.
    cues.sort()
    for n in range(len(cues) - 1):
        a, b, t = cues[n]
        cues[n] = (a, min(b, cues[n + 1][0] - 0.02), t)

    slug = text_plate([cfg["slug"]], spec, tmp / "slug.png", size=34,
                      y_centre=False, x=44, y=88)
    ins_v = ["-i", str(joined), "-loop", "1", "-t", str(total), "-i", str(slug)]
    chain = ["[0:v][1:v]overlay=0:0:enable='lt(t,%.2f)'[b0]" % ec["at"]]
    for n, (a, b, text) in enumerate(cues):
        png = tmp / f"cue{n:02d}.png"
        bc.render(text).save(png)
        ins_v += ["-loop", "1", "-t", str(total), "-i", str(png)]
        chain.append(f"[b{n}][{n + 2}:v]overlay=0:0:"
                     f"enable='between(t,{a:.2f},{b:.2f})'[b{n + 1}]")
        print(f"  cue {a:5.1f}-{b:5.1f}s  {text}")
    silent = tmp / "picture.mp4"
    subprocess.run([ff, "-y", "-v", "error", *ins_v,
                    "-filter_complex", ";".join(chain),
                    "-map", f"[b{len(cues)}]", "-t", str(total),
                    "-c:v", "libx264", "-crf", "19", "-preset", "slow",
                    "-pix_fmt", "yuv420p", str(silent)], check=True)

    # --- sound: voice from the record, a rising drone, the scrubber fan -----
    ins, fc, mixed, idx = ["-i", str(silent)], [], [], 1

    def add(p):
        nonlocal idx
        ins.extend(["-i", str(p)]); idx += 1; return idx - 1

    bed = ep / (cfg.get("music") and f"audio/{cfg['music']}" or "audio/sfx/drone.mp3")
    if bed.exists() and "music" in lv:
        i = add(bed)
        # The cue already carries its own build and its own tail, which is what
        # a music generator is for and what a sound-effect generator could not
        # be talked into. No ramp is applied over it: two shapes fighting is
        # how a bed starts sounding designed.
        fc.append(f"[{i}:a]volume={lv['music']}dB,apad,atrim=0:{total}[bed]")
        mixed.append("[bed]")
    elif bed.exists():
        i = add(bed)
        # The whole point of the bed: a level that climbs for thirty seconds.
        # No melody does the work, the rise does. It starts 18 dB under where
        # it ends, so the first line lands almost dry.
        #
        # The ramp is written in decibels and converted here, because `volume`
        # with eval=frame wants a plain multiplier — a dB suffix inside an
        # expression is a parse error, not a conversion, and the first version
        # of this line died on it.
        lo, hi = lv["drone"] - 18, lv["drone"]
        rate = (hi - lo) / total
        # dynaudnorm first, because the generated bed is not flat and cannot be
        # asked to be. Two prompts tried: one said "with a slow swell in it"
        # and returned 15 dB of variation across 22 s, the rewrite forbade the
        # swell in six different ways and returned 20. A sound-effect model
        # makes material, not beds. Flattening is deterministic, free, and
        # belongs here — the rise is supposed to be the mix's decision, and it
        # cannot be if the material is louder and quieter than the ramp.
        fc.append(f"[{i}:a]aloop=loop=-1:size=2e+09,"
                  f"dynaudnorm=f=200:g=21:p=0.9:m=12,"
                  f"volume='pow(10\\,({lo}+{rate:.4f}*t)/20)':eval=frame,"
                  f"apad,atrim=0:{total}[drone]")
        mixed.append("[drone]")

    fan = ep / "audio" / "sfx" / "fan.mp3"
    if fan.exists():
        i = add(fan)
        fc.append(f"[{i}:a]aloop=loop=-1:size=2e+09,volume={lv['hum']}dB,"
                  f"afade=t=out:st={ec['at'] - 0.5:.2f}:d=0.6,"
                  f"apad,atrim=0:{total}[fan]")
        mixed.append("[fan]")

    for n, ln in enumerate(cfg["lines"]):
        f = ep / "audio" / "narration" / f"{ln['pid']}_s{picks[ln['pid']]}.mp3"
        i = add(f)
        d = int(float(ln["at"]) * 1000)
        trim = f"atrim=0:{ln['trim']},asetpts=N/SR/TB," if ln.get("trim") else ""
        fc.append(f"[{i}:a]{trim}volume={lv['voice']}dB,adelay={d}|{d},"
                  f"apad,atrim=0:{total}[v{n}]")
        mixed.append(f"[v{n}]")
        print(f"  {ln['pid']:<5} at {ln['at']:5.1f}s"
              + (f"  first {ln['trim']}s" if ln.get("trim") else ""))

    fc.append("".join(mixed) + f"amix=inputs={len(mixed)}:normalize=0:"
              f"dropout_transition=0,alimiter=limit=0.95,"
              f"aformat=sample_rates=44100:channel_layouts=stereo[a]")

    dest = out / "TEASER.mp4"
    subprocess.run([ff, "-y", "-v", "error", *ins,
                    "-filter_complex", ";".join(fc),
                    "-map", "0:v", "-map", "[a]", "-t", str(total),
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", str(dest)], check=True)
    for p in tmp.glob("*"):
        p.unlink()
    tmp.rmdir()
    print(f"\n  {dest}  {dur(ff, dest):.2f}s  "
          f"{dest.stat().st_size / 1048576:.1f} MB")


if __name__ == "__main__":
    main()
