#!/usr/bin/env python3
"""Stage 6 gate — measure a Kling take before anyone watches it.

Two questions decide whether a clip is usable, and both are cheaper to answer
in numbers than by eye:

  Did anything move?   A shot running under silence must be a video clip, per
                       the Motion Policy, and a clip that does not move is a
                       frozen frame we paid $0.35 or $0.70 for.

  Did the camera move? Record 01 established that a model asked for a
                       locked-off frame will dolly anyway.

The first version of this script answered the second question with a proxy —
how much the pixels near the frame edge changed — and flagged ten takes out of
twelve, because film grain and compression noise alone move that number more
than a slow dolly does. A proxy with a guessed threshold is not a measurement.

What it does now is measure the thing itself: phase correlation between the
first frame and each later frame gives the translation between them, in
pixels, directly. A locked camera reads 0 or 1 px at this working width; a
dolly or a pan reads several and keeps growing through the clip. Noise cannot
fake a consistent displacement, which is exactly why this is the right test.

What this script is NOT is a verdict, and record 3 established that twice in
one sitting.

Correlating only a border band was tried, on the theory that the frame edge is
fixed geometry. It made the numbers worse: a band stitched from the top and
bottom strips has a seam through the middle of it, and phase correlation on a
discontinuity is noise. Whole-frame correlation stays.

That leaves a known confound, stated rather than hidden: a large object moving
across the middle of a locked shot inflates the reading, because it IS the
dominant translation in the picture. 4.1, a hatch swinging closed in a
perfectly locked frame, reads 33 px. 7.2, a star field drifting behind a
porthole, reads 4. Both are correct clips.

Brightness has the same shape of confound. The ramp catches 5.4, where the
work lamp bloomed until it flooded the corridor, and that is a real rejection;
it also catches 4.1 and 4.3 simply because a bright opening appeared or went
away.

So: STILL is decidable — a clip whose picture does not change is a frozen
frame nobody has to argue about, and it fails. CAMERA and LIGHT print as LOOK,
because the only instrument that settles them is a person watching the clip.
Record 3's two real rejections — a hatch that opened itself in 4.3, and 5.4's
flood — were both found by eye in a filmstrip, and the numbers had cleared one
of them.

`shift` is the largest displacement of the frame from where it started.
`motion` is mean absolute difference between consecutive frames inside the
border, 0-255 — how much is happening in the picture.
"""
import subprocess, sys, pathlib, tempfile
import numpy as np
import yaml
from PIL import Image

FF = "/usr/local/opt/ffmpeg-full/bin/ffmpeg"
WIDTH = 480          # working width; shifts are reported at this scale
BORDER = 0.08
STILL = 0.30         # below this, nothing in the frame is happening
DRIFT = 2.0          # px at 480 wide — about 0.4% of frame width
RAMP  = 6.0          # mean luminance may wander this far from frame one, 0-255

def frames(path, n, tmp, secs=None):
    """Sample the part of the clip that will actually be cut in.

    A take is trimmed to timeline_seconds from its head, so measuring the whole
    file measures footage nobody will see. Record 3's 5.4 is the case that
    forced this: the take is flat for four seconds and blows out in the fifth,
    the cut uses four, and reading the file end to end condemns a clip that is
    clean everywhere it matters.
    """
    out = pathlib.Path(tmp) / path.stem; out.mkdir(exist_ok=True)
    cmd = [FF, "-v", "error", "-i", str(path)]
    if secs: cmd += ["-t", str(secs)]
    cmd += ["-vf", f"fps={n}/10,scale={WIDTH}:-2", str(out / "f%03d.png")]
    subprocess.run(cmd, check=True)
    return sorted(out.glob("*.png"))

def shift(a, b):
    """Translation from a to b, in pixels, by phase correlation."""
    win = np.hanning(a.shape[0])[:, None] * np.hanning(a.shape[1])[None, :]
    A = np.fft.fft2((a - a.mean()) * win)
    B = np.fft.fft2((b - b.mean()) * win)
    R = A * np.conj(B)
    n = np.abs(R); n[n == 0] = 1e-9
    r = np.fft.ifft2(R / n).real
    dy, dx = np.unravel_index(np.argmax(r), r.shape)
    if dy > a.shape[0] // 2: dy -= a.shape[0]
    if dx > a.shape[1] // 2: dx -= a.shape[1]
    return float(np.hypot(dx, dy))

def main(ep, n=10):
    takes = sorted((pathlib.Path(ep) / "takes").glob("*.mp4"))
    if not takes:
        print("no takes yet"); return 1
    doc = yaml.safe_load((pathlib.Path(ep) / "shots.yaml").read_text())
    cut = {s["id"]: s["timeline_seconds"] for s in doc["shots"]}
    print(f"{'shot':>6} {'cut':>4}  {'shift px':>8} {'motion':>7} {'ramp':>6}   verdict")
    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        for t in takes:
            fs = frames(t, n, tmp, cut.get(t.stem))
            a = [np.asarray(Image.open(f).convert("L"), float) for f in fs]
            h, w = a[0].shape
            by, bx = int(h * BORDER), int(w * BORDER)
            mv = np.mean([np.abs(x - y)[by:-by, bx:-bx].mean()
                          for x, y in zip(a, a[1:])])
            sh = max(shift(a[0], f) for f in a[1:])
            ramp = max(abs(f.mean() - a[0].mean()) for f in a[1:])
            hard, look = [], []
            if mv < STILL: hard.append("STILL — nothing is moving")
            if sh > DRIFT: look.append(f"camera or a large object moves {sh:.0f} px")
            if ramp > RAMP: look.append(f"brightness wanders {ramp:.0f}")
            v = "; ".join(hard) or ("LOOK: " + "; ".join(look) if look else "ok")
            if hard: bad.append((t.stem, v))
            print(f"{t.stem:>6} {cut.get(t.stem,0):>3}s  {sh:8.1f} {mv:7.2f} {ramp:6.1f}   {v}")
    print()
    if bad:
        print("FAILED:"); [print("  -", s, ":", v) for s, v in bad]; return 1
    print("No frozen takes. Every LOOK line above still needs an eye on it.")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-03-carbon-balance"))
