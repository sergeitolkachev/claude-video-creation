#!/usr/bin/env python3
"""Look for single dark frames in a master — the thing a viewer reads as a
dropped frame in their player rather than as an artefact of the recording.

A cut to a darker shot is not a flicker, so frames within an eighth of a
second of any shot boundary are skipped; boundaries come from shots.yaml.
Anything left that is more than 12 luma below the median of its neighbours is
reported with its time and depth.

Record 01 scores 9. They are its seven deliberate tape dropouts, each one or
two frames deep by 18 to 63 luma. Record 02 scores 0.

Usage: check_flicker.py [episode dir] [--threshold 12]
"""
import statistics, subprocess, sys, pathlib, yaml

FF = "/usr/local/opt/ffmpeg-full/bin"


def luma(path):
    out = subprocess.run([f"{FF}/ffprobe", "-v", "error", "-f", "lavfi",
                          f"movie={path},signalstats", "-show_entries",
                          "frame_tags=lavfi.signalstats.YAVG", "-of", "csv=p=0"],
                         capture_output=True, text=True).stdout
    vals = []
    for tok in out.replace(",", " ").split():
        try:
            vals.append(float(tok))
        except ValueError:
            pass
    return vals


def main():
    args = sys.argv[1:]
    thr = 12.0
    if "--threshold" in args:
        i = args.index("--threshold"); thr = float(args[i + 1]); del args[i:i + 2]
    ep = pathlib.Path(args[0] if args else "episodes/ep-02-sunrise-line")
    master = ep / "out" / "EPISODE-final.mp4"
    shots = yaml.safe_load((ep / "shots.yaml").read_text())["shots"]

    cuts, acc = set(), 0
    for s in shots:
        acc += s["timeline_seconds"]
        cuts.update(range(int(acc * 24) - 3, int(acc * 24) + 4))

    v = luma(master)
    hits = []
    for i in range(3, len(v) - 3):
        if i in cuts:
            continue
        nb = statistics.median([v[i - 3], v[i - 2], v[i - 1],
                                v[i + 1], v[i + 2], v[i + 3]])
        if nb - v[i] > thr:
            hits.append((i / 24, nb - v[i]))

    print(f"  {len(v)} frames, {len(cuts) // 7} cuts skipped")
    for t, d in hits:
        print(f"  DARK  {t:7.2f}s  {d:.1f} luma below its neighbours")
    print(f"  {len(hits)} dark frames away from any cut")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
