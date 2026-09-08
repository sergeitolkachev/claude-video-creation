#!/usr/bin/env python3
"""Stage 9 — the vertical cuts.

Centre-safe crop from the finished master, so the grade, grain and titles are
already in and a short can never drift from the episode it came from. Each one
stops mid-beat: the last thing heard is a line with no resolution after it.

The crop is 608x1080 out of 1920x1080, scaled to 1080x1920. That is a 1.78x
upscale, which CLAUDE.md otherwise forbids — but a 9:16 frame cannot be taken
from a 16:9 master any other way, and cropping without scaling would deliver a
608-wide short.
"""
import os, subprocess, pathlib, yaml

CUTS = [
    # id, start, end, what it ends on
    ("short-1-different-number", 50.2,  95.2,
     "They get a different number."),
    ("short-2-delay-climbing",  109.5, 144.5,
     "the three readings back to back"),
    ("short-3-not-the-station", 158.0, 208.0,
     "It is not the station that is moving away."),
]

def main():
    ep = pathlib.Path("episodes/ep-01-tishina-9")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    src = ep / "out" / "EPISODE-final.mp4"
    out = ep / "out" / "verticals"; out.mkdir(parents=True, exist_ok=True)

    for vid, a, b, ends_on in CUTS:
        dst = out / f"{vid}.mp4"
        subprocess.run([
            ff, "-y", "-v", "error", "-ss", str(a), "-to", str(b), "-i", str(src),
            "-vf", "crop=608:1080:(iw-608)/2:0,scale=1080:1920:flags=lanczos,setsar=1",
            # a hard cut at the end, but never a hard cut in the audio: a 0.25 s
            # fade stops the last word sounding like a dropped connection
            "-af", f"afade=t=out:st={b-a-0.25}:d=0.25",
            "-c:v", "libx264", "-crf", "20", "-preset", "slow", "-tune", "grain",
            "-c:a", "aac", "-b:a", "160k", "-pix_fmt", "yuv420p", str(dst)], check=True)
        d = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                            "-of","default=nw=1:nk=1",str(dst)],
                           capture_output=True, text=True).stdout.strip()
        mb = dst.stat().st_size / 1048576
        print(f"  {vid:<28} {a:6.1f}–{b:<6.1f} {float(d):5.1f}s  {mb:5.1f} МБ")
        print(f"      обрывается на: {ends_on}")

if __name__ == "__main__":
    main()
