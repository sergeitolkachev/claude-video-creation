#!/usr/bin/env python3
"""Stage 7 — lay the episode's audio bed.

Four layers, per the Audio section of script.md:
  narration  chosen takes, placed against the scene timeline
  hum        one unchanging note under the whole episode, cut at the end
  relay      one dry click every 4-5 seconds, deliberately uneven
  drone      a second barely-audible layer under scenes 4 and 5

The hum ducks to nothing for the 2.5 s before "It is not the station that is
moving away" — the one moment in the episode with no room tone at all, which
is what makes it land.
"""
import os, sys, json, subprocess, pathlib, random, yaml

SCENE_START = {1: 0, 2: 22, 3: 65, 4: 110, 5: 165, 6: 230}
SCENE_END   = {1: 22, 2: 65, 3: 110, 4: 165, 5: 230, 6: 250}
LEAD_IN     = 1.5    # silence before the first line of a scene
TAIL        = 3.0    # silence held at the end of a scene
MIN_GAP     = 1.2    # never closer than this
HOLD = {"s5p6": 2.5, "s5p8": 1.8}   # the two lines that need air before them
# Levels are relative to the source files, which arrive around -11 dB mean.
# The first mix used -26 dB for the hum, which put the bed at -37 dB in the
# master — inaudible on a laptop, and the gaps between paragraphs read as dead
# air rather than as a room. Room tone has to be quietly present, not absent.
HUM_DB, RELAY_DB, DRONE_DB = -19, -22, -28
# The hum cuts out for the 2.5 s before "It is not the station that is moving
# away" and comes back under the next line. Keep this aligned with s5p6's
# actual start — the placement above prints it. Currently s5p6 starts at
# 205.4 s, so the hum drops from 202.9 and returns as the line begins.
SILENCE_AT = (202.9, 2.5)

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries",
        "format=duration","-of","default=nw=1:nk=1",str(p)],
        capture_output=True, text=True).stdout)

def main():
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    A = ep / "audio"
    picks = yaml.safe_load((A / "narration.yaml").read_text())["picks"]

    # 1. Spread each scene's paragraphs across the scene rather than running
    # them off the top. Front-loading left one long dead stretch at the end of
    # every scene; spreading turns that into even, deliberate silences that
    # track the images.
    by_scene = {}
    for pid, seed in picks.items():
        by_scene.setdefault(int(pid[1]), []).append(
            (pid, A / "narration" / f"{pid}_s{seed}.mp3"))

    placed = []
    for scene, items in by_scene.items():
        span = SCENE_END[scene] - SCENE_START[scene] - LEAD_IN - TAIL
        speech = sum(dur(f) for _, f in items)
        holds = sum(HOLD.get(pid, 0) for pid, _ in items)
        gaps = max(len(items) - 1, 1)
        gap = max(MIN_GAP, (span - speech - holds) / gaps)
        t = SCENE_START[scene] + LEAD_IN
        for pid, f in items:
            t += HOLD.get(pid, 0)
            placed.append((pid, f, t))
            t += dur(f) + gap
        print(f"  scene {scene}: {len(items)} paragraphs, gap {gap:.1f}s")

    end = max(t + dur(f) for _, f, t in placed)
    print(f"  narration ends at {end:.1f}s of 250s")

    # 2. relay clicks, uneven on purpose so it never reads as a metronome
    random.seed(11)
    clicks, t = [], 3.0
    while t < 246:
        clicks.append(t); t += random.uniform(4.0, 5.0)

    ins, fc, idx = [], [], 0
    def add(path):
        nonlocal idx
        ins.extend(["-i", str(path)]); idx += 1; return idx - 1

    hum_i   = add(A / "music" / "hum-raw.mp3")
    drone_i = add(A / "music" / "drone.mp3")
    relay_i = add(A / "sfx" / "relay.mp3")
    narr = [(pid, add(f), t) for pid, f, t in placed]

    s0, d0 = SILENCE_AT
    # ElevenLabs fades its own output: the generated hum is flat until ~215 s
    # and is effectively silent by 246, which stripped the room tone out of the
    # entire close. So only the stable middle is used, looped over itself with
    # a crossfade to cover the full runtime, then levelled. Room tone has to be
    # the one thing in the mix that never moves, and the only fade at the end
    # is the one we ask for.
    fc.append(f"[{hum_i}:a]atrim=20:200,asetpts=N/SR/TB,asplit=2[h1][h2]")
    fc.append("[h1][h2]acrossfade=d=3:c1=tri:c2=tri[hloop]")
    fc.append(f"[hloop]dynaudnorm=f=500:g=31:p=0.9:m=3,"
              f"volume={HUM_DB}dB,"
              f"volume='if(between(t,{s0},{s0+d0}),0,1)':eval=frame,"
              f"afade=t=out:st=246:d=4,apad,atrim=0:250[hum]")
    fc.append(f"[{drone_i}:a]volume={DRONE_DB}dB,adelay=110000|110000,apad,atrim=0:250[drone]")
    for n, c in enumerate(clicks):
        fc.append(f"[{relay_i}:a]volume={RELAY_DB}dB,adelay={int(c*1000)}|{int(c*1000)},"
                  f"apad,atrim=0:250[r{n}]")
    for pid, i, t in narr:
        fc.append(f"[{i}:a]adelay={int(t*1000)}|{int(t*1000)},apad,atrim=0:250[n{i}]")

    mixed = "[hum][drone]" + "".join(f"[r{n}]" for n in range(len(clicks))) \
            + "".join(f"[n{i}]" for _, i, _ in narr)
    fc.append(f"{mixed}amix=inputs={2+len(clicks)+len(narr)}:normalize=0:dropout_transition=0,"
              f"alimiter=limit=0.95,aformat=sample_rates=44100:channel_layouts=stereo[out]")

    out = A / "episode-mix.mp3"
    subprocess.run([ff, "-y", "-v", "error", *ins,
                    "-filter_complex", ";".join(fc), "-map", "[out]",
                    "-c:a", "libmp3lame", "-b:a", "192k", str(out)], check=True)
    print(f"  {len(clicks)} relay clicks, {len(narr)} paragraphs")
    print(f"  {out}  {dur(out):.2f}s")

if __name__ == "__main__":
    main()
