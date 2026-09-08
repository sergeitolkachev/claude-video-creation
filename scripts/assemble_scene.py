#!/usr/bin/env python3
"""Rough-cut one scene: trim each take to its timeline length, normalise to
1920x1080, concatenate in shot order. No grade, no titles, no audio — this is
for judging whether the shots sit together, nothing else.

Kling returns 1904x1088 and Seedance 1920x1088; neither is 16:9. Both are
centre-cropped to 1920x1080 rather than scaled, so nothing stretches.
"""
import os, sys, subprocess, pathlib, tempfile, yaml

def main():
    scene = int(sys.argv[1])
    ep = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "episodes/ep-01-tishina-9")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    shots = [s for s in doc["shots"] if s["scene"] == scene]

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
        if s.get("retime"):
            vf = f"setpts={s['retime']}*PTS," + vf
        subprocess.run([ff, "-y", "-v", "error", "-i", str(src), "-t", str(secs),
                        "-vf", vf, "-an", "-c:v", "libx264", "-crf", "18",
                        "-pix_fmt", "yuv420p", str(dst)], check=True)
        parts.append(dst)
        print(f"  {s['id']:<5} {secs}s")

    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    out = ep / "out" / f"scene-{scene}-rough.mp4"
    subprocess.run([ff, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c", "copy", str(out)], check=True)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration", "-of", "default=nw=1:nk=1", str(out)],
                         capture_output=True, text=True).stdout.strip()
    want = sum(s["timeline_seconds"] for s in shots)
    print(f"\n{out}  {float(dur):.2f}s (сценарий: {want}s)")
    if missing: print("нет клипов для:", ", ".join(missing))

if __name__ == "__main__":
    main()
