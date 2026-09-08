#!/usr/bin/env python3
"""Stage 8, part two — grade the cut and burn in the titles.

Everything here is degradation the shot prompts were deliberately kept free of,
so that it is identical across all thirty shots instead of varying per
generation. Order matters: grade, then grain, then titles. Titles sit under the
grain, not on top of it — they are part of the recording, not a caption added
to it afterwards.
"""
import os, sys, subprocess, pathlib, yaml, random

# Locked for the channel. Compared 1:1 against grain 13 at CRF 20: the
# texture is indistinguishable at pixel level, and the master is nine times
# smaller (276 MB against 2.5 GB for four minutes). Do not change these per
# episode — different grain reads as a different source recording.
GRAIN      = 9       # noise strength
CRF        = 23
VIGNETTE   = "PI/4.5"
CHROMA     = 1       # rgbashift, pixels
SAT        = 0.86
CONTRAST   = 1.05
DROPOUTS   = 7       # brief tape dropouts across the episode

def main():
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    cards = yaml.safe_load((ep / "titles.yaml").read_text())["cards"]
    src = ep / "out" / "EPISODE-with-audio.mp4"

    random.seed(7)
    drops = sorted(random.uniform(8, 240) for _ in range(DROPOUTS))
    # lutyuv evaluates per pixel and has no notion of time; eq supports
    # timeline editing, so the dropouts are a timed brightness collapse.
    drop_expr = "+".join(f"between(t,{d:.2f},{d+0.06:.2f})" for d in drops)

    # A still PNG is a single frame at t=0. Without -loop the overlay has
    # nothing to draw once the timeline moves past zero and every title
    # silently fails to appear — which is exactly what happened on pass 1.
    ins = ["-i", str(src)]
    for c in cards:
        ins += ["-loop", "1", "-t", "250", "-r", "24",
                "-i", str(ep / "out" / "titles" / f"{c['id']}.png")]

    fc = [
        # grade first, so the grain sits on top of the final colour
        f"[0:v]eq=saturation={SAT}:contrast={CONTRAST},"
        f"rgbashift=rh=-{CHROMA}:bv={CHROMA},"
        f"vignette={VIGNETTE},"
        # dropouts: the picture collapses for about three frames
        f"eq=brightness=-0.42:contrast=0.5:enable='{drop_expr}'[base]"
    ]
    last = "base"
    for i, c in enumerate(cards, start=1):
        a, b = c["at"], c["at"] + c["hold"]
        fc.append(f"[{i}:v]format=rgba,"
                  f"fade=t=in:st={a}:d=0.6:alpha=1,"
                  f"fade=t=out:st={b-0.8}:d=0.8:alpha=1[t{i}]")
        fc.append(f"[{last}][t{i}]overlay=0:0:enable='between(t,{a-0.1},{b+0.1})'[o{i}]")
        last = f"o{i}"
    # grain last: it lies over the titles too, so they belong to the recording
    fc.append(f"[{last}]noise=alls={GRAIN}:allf=t+u,format=yuv420p[v]")

    out = ep / "out" / "EPISODE-final.mp4"
    subprocess.run([ff, "-y", "-v", "error", *ins,
                    "-filter_complex", ";".join(fc),
                    "-map", "[v]", "-map", "0:a",
                    # Grain is close to incompressible. Pass 1 used plain
                    # CRF 17 and produced 2.9 GB for four minutes; tune=grain
                    # tells x264 to keep the texture without spending a bit on
                    # every particle.
                    "-c:v", "libx264", "-crf", str(CRF), "-preset", "slow",
                    "-tune", "grain",
                    "-c:a", "copy", str(out)], check=True)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", str(out)],
                         capture_output=True, text=True).stdout.strip()
    print(f"  {len(cards)} titles, {DROPOUTS} dropouts at "
          + ", ".join(f"{d:.0f}s" for d in drops))
    print(f"  {out}  {float(dur):.2f}s")

if __name__ == "__main__":
    main()
