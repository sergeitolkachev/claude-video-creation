#!/usr/bin/env python3
"""Rough-cut one scene: trim each take to its timeline length, normalise to
1920x1080, concatenate in shot order. No grade, no titles, no audio — this is
for judging whether the shots sit together, nothing else.

Kling returns 1904x1088 and Seedance 1920x1088; neither is 16:9. Both are
centre-cropped to 1920x1080 rather than scaled, so nothing stretches.
"""
import os, sys, subprocess, pathlib, tempfile, yaml

def main():
    # "all" assembles the whole episode in shot order; a number does one scene.
    arg = sys.argv[1]
    scene = None if arg == "all" else int(arg)
    ep = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "episodes/ep-01-tishina-9")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    shots = [s for s in doc["shots"] if scene is None or s["scene"] == scene]

    tmp = pathlib.Path(tempfile.mkdtemp())
    parts, missing = [], []
    for s in shots:
        src = ep / "takes" / f"{s['id']}.mp4"
        if not src.exists():
            missing.append(s["id"]); continue
        dst = tmp / f"{s['id']}.mp4"
        secs = s["timeline_seconds"]
        vf = ("scale=1920:-2,crop=1920:1080:(iw-1920)/2:(ih-1080)/2,"
              "setsar=1,fps=24")
        src_t = []
        if s.get("retime"):
            r = s["retime"]
            # A plain setpts repeats frames, which is fine at 1.3x and reads
            # as a stutter well before 2x. Record 07's 1.2 is slowed 2x and
            # approved only as interpolated — repeated frames step the needle.
            # Only the source the shot actually uses is read: interpolating
            # the whole 10 s take to keep its first 5 is minutes for nothing.
            if s.get("retime_mode") == "interpolate":
                vf = (f"setpts={r}*PTS,minterpolate=fps=24:mi_mode=mci:"
                      f"mc_mode=aobmc:me_mode=bidir:vsbmc=1," + vf)
                src_t = ["-t", f"{secs / r + 0.1:.3f}"]
            else:
                vf = f"setpts={r}*PTS," + vf
        if s.get("post_motion") == "push":
            # A centred push laid over a take that came back too still to
            # hold the screen. Record 07's 3.4 asked Kling for a line that
            # "holds", got a near-frozen frame for $0.70, and was kept with
            # this instead of a reroll. Same travel as build_static.py's
            # `local_motion: push`, over the 3840 upscale that keeps zoompan
            # from stepping, so a pushed take and a pushed still move alike.
            from build_static import PUSH_ZOOM
            n = int(secs * 24) - 1
            vf += (f",scale=3840:-2,zoompan=z='1+{PUSH_ZOOM}*on/{n}':d=1:"
                   f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
                   f"s=1920x1080:fps=24,setsar=1")
        subprocess.run([ff, "-y", "-v", "error", *src_t, "-i", str(src), "-t", str(secs),
                        "-vf", vf, "-an", "-c:v", "libx264", "-crf", "18",
                        "-pix_fmt", "yuv420p", str(dst)], check=True)
        parts.append(dst)
        print(f"  {s['id']:<5} {secs}s")

    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    # mkdir, because a new episode has no out/ yet and the concat then fails
    # with a bare exit 254 that says nothing about a missing directory.
    (ep / "out").mkdir(exist_ok=True)
    out = ep / "out" / ("rough-cut.mp4" if scene is None
                        else f"scene-{scene}-rough.mp4")
    subprocess.run([ff, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c", "copy", str(out)], check=True)
    probe = str(pathlib.Path(ff).with_name("ffprobe"))
    dur = subprocess.run([probe, "-v", "error", "-show_entries",
                          "format=duration", "-of", "default=nw=1:nk=1", str(out)],
                         capture_output=True, text=True).stdout.strip()
    want = sum(s["timeline_seconds"] for s in shots)
    print(f"\n{out}  {float(dur):.2f}s (script says {want}s)")
    if missing: print("no take for:", ", ".join(missing))

if __name__ == "__main__":
    main()
