#!/usr/bin/env python3
"""Stage 8, part two — grade the cut, lay the overlays under the grain, master.

Order matters and has not changed: grade, then overlays, then grain. Every
card and title sits *under* the grain, so it belongs to the recording rather
than being a caption added to it afterwards.

What did change is the dropout. Record 01 collapsed the picture to near-black
for 0.06 s, seven times, as a tape artefact. On a screen it does not read as
tape — it reads as a dropped frame in the player, and the viewer checks their
connection instead of watching the record. It is off by default now and any
episode that wants it has to ask for it by name in grade.yaml.

Usage: grade.py [episode dir]
"""
import json, os, pathlib, random, subprocess, sys, yaml

print = __import__('functools').partial(print, flush=True)

# Locked for the channel. Compared 1:1 against grain 13 at CRF 20: the texture
# is indistinguishable at pixel level and the master is nine times smaller.
# Never vary these between episodes — different grain reads as a different
# source recording.
GRAIN    = 9
CRF      = 23
VIGNETTE = "PI/4.5"
CHROMA   = 1        # rgbashift, pixels
SAT      = 0.86
CONTRAST = 1.05


def main():
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-02-sunrise-line")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    total = doc["runtime_seconds"]
    grade_cfg = {}
    if (ep / "grade.yaml").exists():
        grade_cfg = yaml.safe_load((ep / "grade.yaml").read_text()) or {}

    src = ep / "out" / "rough-cut.mp4"
    audio = ep / "audio" / "episode-mix.mp3"
    manifest = json.loads((ep / "cards" / "manifest.json").read_text())

    ins = ["-i", str(src), "-i", str(audio)]
    for m in manifest:
        ins += ["-i", str(ep / "cards" / m["mov"])]

    fc = [f"[0:v]eq=saturation={SAT}:contrast={CONTRAST},"
          f"rgbashift=rh=-{CHROMA}:bv={CHROMA},"
          f"vignette={VIGNETTE}[graded]"]
    last = "graded"

    drops = []
    n_drops = grade_cfg.get("dropouts", 0)
    if n_drops:
        random.seed(grade_cfg.get("dropout_seed", 7))
        drops = sorted(random.uniform(8, total - 30) for _ in range(n_drops))
        expr = "+".join(f"between(t,{d:.2f},{d + 0.06:.2f})" for d in drops)
        fc.append(f"[{last}]eq=brightness=-0.42:contrast=0.5:"
                  f"enable='{expr}'[dropped]")
        last = "dropped"

    # Every overlay is shorter than the record, so it is shifted into place
    # rather than enabled in place: an overlay filter with a short input holds
    # its last frame forever otherwise.
    for n, m in enumerate(manifest, start=2):
        fc.append(f"[{n}:v]setpts=PTS-STARTPTS+{m['at']}/TB[ov{n}]")
        fc.append(f"[{last}][ov{n}]overlay=0:0:eof_action=pass:"
                  f"enable='between(t,{m['at']},{m['at'] + m['duration']:.3f})'"
                  f"[c{n}]")
        last = f"c{n}"

    # Grain last, so it lies over the cards and the titles too.
    fc.append(f"[{last}]noise=alls={GRAIN}:allf=t+u,format=yuv420p[v]")

    out = ep / "out" / "EPISODE-final.mp4"
    subprocess.run([ff, "-y", "-v", "error", *ins,
                    "-filter_complex", ";".join(fc),
                    "-map", "[v]", "-map", "1:a",
                    # Grain is close to incompressible; tune=grain keeps the
                    # texture without spending a bit on every particle.
                    "-c:v", "libx264", "-crf", str(CRF), "-preset", "slow",
                    "-tune", "grain", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "192k", str(out)], check=True)

    probe = str(pathlib.Path(ff).with_name("ffprobe"))
    info = subprocess.run([probe, "-v", "error", "-select_streams", "v:0",
                           "-show_entries", "stream=width,height:format=duration",
                           "-of", "csv=p=0", str(out)],
                          capture_output=True, text=True).stdout.split()
    print(f"  {len(manifest)} overlays under the grain")
    print(f"  dropouts: {len(drops) or 'none — see the docstring'}")
    print(f"  {out}  {info[0]}  {float(info[1]):.2f}s  "
          f"{out.stat().st_size // 1024 // 1024} MB")


if __name__ == "__main__":
    main()
