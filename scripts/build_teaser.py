#!/usr/bin/env python3
"""Stage 9b — the thirty-second teaser, assembled from teaser.yaml.

Out before the record exists, and the only piece on this channel allowed to
sound composed. It takes the shots where something physically moves and the
lines that escalate on their own, reorders them freely, and ends before the
answer.

Since record 04 the vertical cuts are assembled the same way, so the picture,
the type and the caption timings come out of scripts/vertical.py — one copy,
two callers. What stays here is the sound, and that is the whole difference:
the teaser gets a generated cue under it and a vertical cut never does. Two
mixes that must differ by rule do not belong behind one function.

Three things it must not do, all of them enforced by what it is given rather
than by a check here:

  - speak a line the record does not contain. Every line is a take already in
    audio/narration/, already approved, already reproducible from its seed.
  - show a frame the record does not contain. Every shot is a take already in
    takes/.
  - carry licensed music. The bed is generated (see teaser_sfx in audio.yaml);
    a Content ID claim on a channel built out of recovered recordings costs
    more than any track is worth.

And the closing card says SOON, not FULL RECORD. The two are not
interchangeable: a cut goes out after the record and its card is an
instruction, the teaser goes out before and a card promising something that
does not exist yet is the one promise a channel cannot take back.

Usage: build_teaser.py [episode dir] [--out path.mp4]
"""
import importlib.util, os, pathlib, shutil, subprocess, sys, yaml

print = __import__('functools').partial(print, flush=True)

_here = pathlib.Path(__file__).parent


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


V = _load("vertical", _here / "vertical.py")
bc = _load("bc", _here / "build_captions.py")


def main():
    args = sys.argv[1:]
    dest = None
    if "--out" in args:
        i = args.index("--out"); dest = pathlib.Path(args[i + 1]); del args[i:i + 2]
    ep = pathlib.Path(args[0] if args else "episodes/ep-03-carbon-balance")

    ff = V.ffmpeg()
    cfg = yaml.safe_load((ep / "teaser.yaml").read_text())
    spec = yaml.safe_load(pathlib.Path("config/type.yaml").read_text())
    picks = yaml.safe_load((ep / "audio" / "narration.yaml").read_text())["picks"]
    lv = cfg["levels"]
    total = float(cfg["runtime_seconds"])
    ec = cfg["end_card"]
    out = ep / "out"; out.mkdir(parents=True, exist_ok=True)
    tmp = out / "_teaser"; tmp.mkdir(exist_ok=True)
    dest = dest or (out / "TEASER.mp4")

    shot_sum = sum(float(s["seconds"]) for s in cfg["shots"])
    if abs(shot_sum + ec["seconds"] - total) > 0.05:
        sys.exit(f"shots sum to {shot_sum:.2f}s + {ec['seconds']}s card, "
                 f"runtime_seconds is {total:.2f}")

    # --- picture: each shot trimmed out of its own take, then the card ------
    card = V.black_card(ec["lines"], spec, tmp, ec["seconds"], size=64)
    joined = V.build_picture(ep, cfg["shots"], tmp, tail_clip=card)

    # --- captions, from the same word timings the cuts use -----------------
    cues = V.caption_cues(ep, cfg["lines"], picks, bc)
    slug = V.text_plate([cfg["slug"]], spec, tmp / "slug.png", size=34,
                        centre=False, x=44, y=88)
    silent = V.overlay_type(joined, slug, cues, total, tmp, tmp / "picture.mp4",
                            bc, slug_until=ec["at"])

    # --- sound: voice from the record, a rising bed, the scrubber fan -------
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

    vins, vfc, vlabels, idx = V.voice_chains(ep, cfg["lines"], picks, total,
                                             lv["voice"], idx)
    ins += vins; fc += vfc; mixed += vlabels

    fc.append("".join(mixed) + f"amix=inputs={len(mixed)}:normalize=0:"
              f"dropout_transition=0,alimiter=limit=0.95,"
              f"aformat=sample_rates=44100:channel_layouts=stereo[a]")

    subprocess.run([ff, "-y", "-v", "error", *ins,
                    "-filter_complex", ";".join(fc),
                    "-map", "0:v", "-map", "[a]", "-t", str(total),
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", str(dest)], check=True)
    shutil.rmtree(tmp)
    print(f"\n  {dest}  {V.dur(dest):.2f}s  "
          f"{dest.stat().st_size / 1048576:.1f} MB")


if __name__ == "__main__":
    main()
