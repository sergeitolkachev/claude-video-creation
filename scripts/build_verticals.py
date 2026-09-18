#!/usr/bin/env python3
"""Stage 9 — the vertical cuts, assembled.

Records 01 to 03 carved their cuts out of the finished master: one window,
`from` and `to`, the episode's own order, and a centre crop of 608 px out of
1920 that was not a choice but a constant in the source. It works and it
throws away the two things that decide whether a vertical is watched. The
record's order is paced for someone who has already chosen to watch; a cut has
four seconds to earn that. And the centre of a 16:9 frame is not where the
subject is — a hatch off to the left, a gauge in the right third, and the
centre crop delivers the wall between them.

From record 04 a cut is built the way the teaser is built: a shot list out of
takes/, in whatever order works, each shot framed where its subject is, and a
line list out of the paragraphs already in the record. What does NOT change:

  - Hard cuts only. A dissolve says a person edited this, which is the one
    thing a recovered recording cannot afford. The attention is bought with
    short shots, a subject that moves and a crop that frames it.
  - Nothing new is generated. Every shot is a take in takes/; every line is a
    paragraph already approved, already reproducible from its seed.
  - No data cards and no click bed. A card is composed for the lower left of a
    16:9 frame and the crop takes its numbers away; a typing sound over
    nothing typing is a fault. Every figure that matters is spoken.
  - No music, ever. The teaser is the only piece on this channel allowed a cue
    under it. A man reading numbers over music is an actor in a film.
  - A voice inside the first second, captions burned in from real word
    timings, the bottom 30% clear, and the channel's closing card at the end.

Schema, per cut in verticals.yaml:

    cuts:
      - id: fc9-004-b-the-measurement
        runtime_seconds: 34.0          # the whole cut, closing card included
        fan: off                       # optional: the gated layer, per cut
        shots:
          - {id: "3.2", at: 0.0, from: 2.0, seconds: 3.4}
          - {id: "3.5", at: 3.4, from: 1.0, seconds: 2.8, crop_x: 0.38}
          - {id: "3.1", at: 6.2, from: 0.0, seconds: 4.0, crop_x: 0.44,
             crop_to: 0.60}
        lines:
          - {pid: s3p1, at: 0.2}
          - {pid: s3p4, at: 12.3, trim: 3.60}
        ends_on: "I am not producing one point three nine."

`crop_x` is the window's centre as a fraction of the frame width, 0.5 being
the old centre crop and the default. `crop_to` makes it travel across the
shot. `trim` cuts a line short on a word boundary out of audio/alignment/ —
validate.py and this script read that through the same function.

Usage: build_verticals.py [episode dir] [--only fc9-004-b-the-measurement]
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
    only = None
    if "--only" in args:
        i = args.index("--only"); only = args[i + 1]; del args[i:i + 2]
    out_root, conf = None, None
    if "--out" in args:
        i = args.index("--out"); out_root = pathlib.Path(args[i + 1]); del args[i:i + 2]
    if "--config" in args:
        i = args.index("--config"); conf = pathlib.Path(args[i + 1]); del args[i:i + 2]
    ep = pathlib.Path(args[0] if args else "episodes/ep-03-carbon-balance")

    ff = V.ffmpeg()
    cfg = yaml.safe_load((conf or (ep / "verticals.yaml")).read_text())
    spec = yaml.safe_load(pathlib.Path("config/type.yaml").read_text())
    acfg = yaml.safe_load((ep / "audio.yaml").read_text())
    picks = yaml.safe_load((ep / "audio" / "narration.yaml").read_text())["picks"]

    # Levels come from the record's own mix unless a cut's file overrides them,
    # because a cut is the same recording and has to sound like it. A level
    # here is a trim applied to the file, not a target level in the mix.
    lv = dict(acfg.get("levels") or {})
    lv.update(cfg.get("levels") or {})
    lv.setdefault("voice", 0)

    out = (out_root or (ep / "out" / "verticals")); out.mkdir(parents=True, exist_ok=True)
    ec = spec["captions"]["end_card"]
    card_s = float(ec.get("seconds", 2.0))

    slug = V.text_plate([cfg["slug"]], spec, out / "_slug.png", size=34,
                        centre=False, x=44, y=88)

    for cut in cfg["cuts"]:
        if only and cut["id"] != only:
            continue
        # `runtime_seconds` is the whole cut, closing card included — the same
        # meaning it has in teaser.yaml. Two files describing the same kind of
        # object with the same key measuring different things is how a rule
        # drifts, and this one was written inconsistently on the first pass.
        total = float(cut["runtime_seconds"])
        body = total - card_s
        print(f"\n  {cut['id']}   {body:.1f}s picture + {card_s:.0f}s card")

        # The picture has to cover the runtime exactly. A gap is a frame of
        # black in the middle of a cut and an overrun is a shot that never
        # arrives; both are decidable here and neither is visible in a log.
        shot_sum = sum(float(s["seconds"]) for s in cut["shots"])
        if abs(shot_sum - body) > 0.05:
            sys.exit(f"{cut['id']}: shots sum to {shot_sum:.2f}s, "
                     f"runtime_seconds is {body:.2f}")

        tmp = out / f"_{cut['id']}"; tmp.mkdir(exist_ok=True)
        card = V.black_card(ec.get("lines") or ec["text"], spec, tmp, card_s,
                            size=ec.get("size", 46))
        joined = V.build_picture(ep, cut["shots"], tmp, tail_clip=card)

        cues = V.caption_cues(ep, cut["lines"], picks, bc)
        silent = V.overlay_type(joined, slug, cues, total, tmp,
                                tmp / "picture.mp4", bc, slug_until=body)

        # --- sound: the voice, the room tone, and the gated layer -----------
        #
        # The tone is the floor and it is not gated by anything, including
        # under the closing card. Record 03 gated its fan off and, because the
        # fan was also doing duty as the room tone, both fell to -90 dBFS —
        # not silence, but a file that has ended.
        ins, fc, mixed, idx = ["-i", str(silent)], [], [], 1

        def add(p):
            nonlocal idx
            ins.extend(["-i", str(p)]); idx += 1; return idx - 1

        tone = ep / "audio" / "sfx" / "tone.mp3"
        if tone.exists():
            i = add(tone)
            fc.append(f"[{i}:a]aloop=loop=-1:size=2e+09,volume={lv.get('tone', 0)}dB,"
                      f"apad,atrim=0:{total}[tone]")
            mixed.append("[tone]")
        else:
            print("  no audio/sfx/tone.mp3 — this cut has no floor under it")

        fan = ep / "audio" / "sfx" / "fan.mp3"
        fan_on = str(cut.get("fan", "on")).lower() not in ("off", "false", "no")
        if fan.exists() and fan_on:
            i = add(fan)
            fc.append(f"[{i}:a]aloop=loop=-1:size=2e+09,volume={lv.get('hum', 0)}dB,"
                      f"afade=t=out:st={body - 0.5:.2f}:d=0.6,"
                      f"apad,atrim=0:{total}[fan]")
            mixed.append("[fan]")
        elif fan.exists():
            print("  fan: off — declared for this cut, the tone still runs")

        vins, vfc, vlabels, idx = V.voice_chains(
            ep, cut["lines"], picks, total, lv["voice"], idx)
        ins += vins; fc += vfc; mixed += vlabels

        # A hard cut in the picture, never in the audio: a quarter-second fade
        # stops the last half-word sounding like a dropped connection.
        fc.append("".join(mixed) + f"amix=inputs={len(mixed)}:normalize=0:"
                  f"dropout_transition=0,alimiter=limit=0.95,"
                  f"afade=t=out:st={total - 0.5:.2f}:d=0.5,"
                  f"aformat=sample_rates=44100:channel_layouts=stereo[a]")

        dst = out / f"{cut['id']}.mp4"
        subprocess.run([ff, "-y", "-v", "error", *ins,
                        "-filter_complex", ";".join(fc),
                        "-map", "0:v", "-map", "[a]", "-t", str(total),
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        "-movflags", "+faststart", str(dst)], check=True)
        shutil.rmtree(tmp)
        print(f"  {dst.name:<34} {V.dur(dst):5.1f}s  "
              f"{dst.stat().st_size / 1048576:5.1f} MB   "
              f"{len(cut['shots'])} shots, ends on \"{cut['ends_on']}\"")


if __name__ == "__main__":
    main()
