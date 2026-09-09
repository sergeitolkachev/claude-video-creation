#!/usr/bin/env python3
"""Build the locked-off shots from their approved stills.

Seedance will not hold a frame — asked for a static shot it dollies forward
several metres, and saying so more firmly made it worse. Kling holds a frame
but costs $0.70 for a clip we would trim anyway. A still with a touch of lens
breathing is steadier than either, costs nothing, and comes out at exactly the
duration and exactly 1920x1080.

The breathing is 1.0 -> 1.006 across the shot: invisible as a move, enough
that the frame is not literally frozen. Grain, vignette and dropout are added
later, in the episode-wide grade.
"""
import os, sys, subprocess, pathlib, yaml

BREATH = 0.006      # locked-off: lens breathing only
DRIFT_ZOOM = 0.05   # drift: how far the push travels
DRIFT_PAN = 0.02    # drift: sideways travel, as a fraction of frame width
PUSH_ZOOM = 0.09    # push: a straight move in, no sideways travel

def main():
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    out_dir = ep / "takes"; out_dir.mkdir(exist_ok=True)
    built = 0
    for s in doc["shots"]:
        # A shot with `plates:` is a texture change over time — record 2's
        # drying ground — built as a cross-dissolve of its approved plates
        # rather than generated, because a model rewrites the patch instead
        # of drying it. Each plate holds, then dissolves into the next; the
        # whole thing gets the same lens breathing as any other locked shot.
        if s.get("plates"):
            plates = [ep / "approved" / f"{pid}.jpg" for pid in s["plates"]]
            missing = [f.name for f in plates if not f.exists()]
            if missing:
                print(f"  {s['id']:<5} SKIP — no {', '.join(missing)}"); continue
            secs, k = s["timeline_seconds"], len(plates)
            hold, xfade = secs / k, 1.2
            args = [ff, "-y", "-v", "error"]
            for f in plates:
                args += ["-loop", "1", "-t", f"{hold + xfade:.3f}", "-i", str(f)]
            fc = "".join(
                f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=increase,"
                f"crop=1920:1080,setsar=1,fps=24[p{i}];" for i in range(k))
            prev, off = "[p0]", hold
            for i in range(1, k):
                out = f"[x{i}]" if i < k - 1 else "[v]"
                fc += (f"{prev}[p{i}]xfade=transition=fade:duration={xfade}:"
                       f"offset={off:.3f}{out};")
                prev, off = out, off + hold
            fc = fc.rstrip(";")
            dst = out_dir / f"{s['id']}.mp4"
            subprocess.run(args + ["-filter_complex", fc, "-map", "[v]",
                                   "-t", str(secs), "-r", "24",
                                   "-c:v", "libx264", "-crf", "18",
                                   "-pix_fmt", "yuv420p", str(dst)], check=True)
            built += 1
            print(f"  {s['id']:<5} {secs}s  dissolve {k} plates "
                  f"{dst.stat().st_size // 1024:>6} KB")
            continue
        if s.get("source") != "ffmpeg_still":
            continue
        # A shot with a composited screen is built from that plate, so the
        # readout moves with the shot instead of being tracked onto it.
        screened = ep / "approved" / f"{s['id']}.screen.jpg"
        src = screened if screened.exists() else ep / "approved" / f"{s['id']}.jpg"
        dst = out_dir / f"{s['id']}.mp4"
        secs = s["timeline_seconds"]; frames = secs * 24
        n = frames - 1
        if s.get("local_motion") == "push":
            # A centred push, nothing sideways: this is the readout coming
            # closer, and the number has to stay square in the middle of it.
            z, x, y = (f"1+{PUSH_ZOOM}*on/{n}",
                       "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)")
        elif s.get("local_motion") == "drift":
            # A controlled push with a touch of sideways travel. Used where a
            # model was asked for a slow drift and trucked the subject out of
            # frame instead — here the subject cannot leave, because we say
            # exactly how far it goes.
            z = f"1+{DRIFT_ZOOM}*on/{n}"
            x = f"iw/2-(iw/zoom/2)+{DRIFT_PAN}*iw*on/{n}"
            y = f"ih/2-(ih/zoom/2)"
        else:
            z, x, y = (f"1+{BREATH}*on/{n}",
                       "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)")
        subprocess.run([
            ff, "-y", "-v", "error", "-loop", "1", "-i", str(src),
            "-t", str(secs), "-r", "24",
            "-vf", (f"scale=3840:-2,zoompan=z='{z}':d={frames}:"
                    f"x='{x}':y='{y}':s=1920x1080:fps=24,setsar=1"),
            "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", str(dst)],
            check=True)
        built += 1
        print(f"  {s['id']:<5} {secs}s  {s.get('local_motion', 'breathe'):<8} "
              f"{dst.stat().st_size // 1024:>6} KB")
    print(f"\n{built} locked-off shots built. $0.00.")

if __name__ == "__main__":
    main()
