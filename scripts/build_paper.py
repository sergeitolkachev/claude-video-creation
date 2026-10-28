#!/usr/bin/env python3
"""Pencil marks on the paper in a plate — a plot, a schematic, a ringed point.

Record 09's desk plates showed blank sheets in a record about a man doing
arithmetic. The marks are drawn onto the approved still, not onto the clip:
the result is written as approved/<id>.screen.jpg, which build_static.py
already prefers over the plain still, so the drawing moves with the push or
pull exactly and there is nothing to track.

Handwriting is allowed (Serge, 2026-10-27): axis labels, a figure in the
margin, a date. It is the operator's pencil, part of the world in the frame,
so the one-renderer rule for the record's own Menlo layer does not reach it —
but every figure written here must agree with the narration and the cards,
and it is never set in Menlo: a typed face on a pencilled sheet reads as a
card that has fallen into the picture.

The marks are already on the paper when the shot starts. A sheet that draws
itself with no hand in frame reads as something writing — the one cause this
channel never shows.

Coordinates in paper.yaml are fractions of the sheet's own box, so a drawing
can be moved to another sheet by changing the box.

Usage: build_paper.py [episode dir]
"""
import sys, pathlib, yaml
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageFont

S = 4                     # supersample, so a 1 px stroke has a soft edge
GRAPHITE = 105            # default tone, 0 black .. 255 paper
HAND = "/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf"


class Sheet:
    def __init__(self, size, box, seed):
        self.W, self.H = size
        self.box = box
        self.rng = np.random.default_rng(seed)
        self.layer = Image.new("L", (self.W * S, self.H * S), 255)
        self.d = ImageDraw.Draw(self.layer)

    def xy(self, u, v):
        x0, y0, x1, y1 = self.box
        return x0 + u * (x1 - x0), y0 + v * (y1 - y0)

    def _jitter(self, pts, amp):
        pts = np.asarray(pts, float)
        k = min(9, len(pts))
        n = self.rng.normal(0, amp, pts.shape)
        n = np.column_stack([np.convolve(n[:, i], np.ones(k) / k, "same")
                             for i in range(2)])
        return pts + n

    def stroke(self, pts, w=1.2, tone=GRAPHITE, amp=0.5):
        """A pencil line: uneven pressure along it, a hand's slight wander."""
        p = self._jitter(pts, amp) * S
        m = len(p)
        press = 0.75 + 0.25 * np.sin(np.linspace(0, self.rng.uniform(2, 5), m)
                                     + self.rng.uniform(0, 6))
        for i, ((x0, y0), (x1, y1)) in enumerate(zip(p, p[1:])):
            tv = int(255 - (255 - tone) * press[i])
            self.d.line([(x0, y0), (x1, y1)], fill=tv,
                        width=max(1, int(w * S * press[i])))

    def line(self, a, b, n=60, **k):
        self.stroke(np.linspace(self.xy(*a), self.xy(*b), n), **k)

    def finish(self, plate):
        # Graphite breaks up where the paper's tooth shows through.
        grain = self.rng.uniform(0, 1, (self.H * S, self.W * S))
        arr = np.asarray(self.layer, float)
        arr = 255 - (255 - arr) * (0.55 + 0.45 * (grain > 0.35))
        g = Image.fromarray(arr.clip(0, 255).astype("uint8"))
        g = g.resize((self.W, self.H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.45))
        # Multiplied in, so the ruling shows through the pencil.
        return ImageChops.multiply(plate, Image.merge("RGB", [g, g, g]))


def decay(u0, u1, v_top, v_bottom, tau, n=140):
    t = np.linspace(0, 1, n)
    return t, u0 + t * (u1 - u0), v_top + (v_bottom - v_top) * (1 - np.exp(-t / tau))


def draw(sh, el):
    kind = el["kind"]
    tone = el.get("tone", GRAPHITE)
    if kind == "axes":
        (u0, v0), (u1, v1) = el["origin"], el["end"]
        sh.line((u0, v0 + 0.015), (u0 - 0.003, v1 - 0.02), tone=tone, w=1.4)
        sh.line((u0 - 0.02, v0), (u1 + 0.025, v0 + 0.002), tone=tone, w=1.4)
        for i in range(1, el.get("xticks", 0) + 1):
            u = u0 + i * (u1 - u0) / (el["xticks"] + 1)
            sh.line((u, v0 - 0.01), (u, v0 + 0.012), n=8, w=1.1, tone=tone)
        for i in range(1, el.get("yticks", 0) + 1):
            v = v0 - i * (v0 - v1) / (el["yticks"] + 1)
            sh.line((u0 - 0.015, v), (u0 + 0.012, v), n=8, w=1.1, tone=tone)
    elif kind == "decay":
        # A pressure fall: one curve per run, a hair apart.
        for du, dv, tn in el.get("runs", [[0, 0, tone]]):
            _, u, v = decay(el["u"][0], el["u"][1], el["v"][0], el["v"][1], el["tau"])
            pts = [sh.xy(a + du, b + dv) for a, b in zip(u, v)]
            sh.stroke(pts, w=1.2, tone=tn)
        for tt in el.get("rings", []):
            t, u, v = decay(el["u"][0], el["u"][1], el["v"][0], el["v"][1], el["tau"])
            i = int(tt * (len(t) - 1))
            cx, cy = sh.xy(u[i], v[i])
            a = np.linspace(0, 2 * np.pi, 40)
            r = el.get("ring_px", 6)
            sh.stroke(np.column_stack([cx + r * np.cos(a), cy + r * np.sin(a)]),
                      w=1.0, tone=tone, amp=0.4)
    elif kind == "line":
        sh.line(el["a"], el["b"], w=el.get("w", 1.2), tone=tone)
    elif kind == "box":
        (u0, v0), (u1, v1) = el["a"], el["b"]
        for a, b in (((u0, v0), (u1, v0)), ((u1, v0), (u1, v1)),
                     ((u1, v1), (u0, v1)), ((u0, v1), (u0, v0))):
            sh.line(a, b, n=40, w=el.get("w", 1.2), tone=tone)
    elif kind == "hatch":
        # Diagonal shading inside a box: the part that is shut off.
        (u0, v0), (u1, v1) = el["a"], el["b"]
        step = el.get("step", 0.03)
        k = u0 - (v1 - v0)
        while k < u1:
            a = (max(u0, k), v1 - max(0, u0 - k))
            b = (min(u1, k + (v1 - v0)), v1 - (min(u1, k + (v1 - v0)) - k))
            if b[0] > a[0]:
                sh.line(a, b, n=20, w=0.9, tone=el.get("tone", 140))
            k += step
    elif kind == "arrow":
        (u0, v0), (u1, v1) = el["a"], el["b"]
        sh.line((u0, v0), (u1, v1), n=30, w=1.2, tone=tone)
        ang = np.arctan2(v1 - v0, u1 - u0)
        for s in (+0.5, -0.5):
            sh.line((u1, v1), (u1 - 0.035 * np.cos(ang + s), v1 - 0.035 * np.sin(ang + s)),
                    n=10, w=1.2, tone=tone)
    elif kind == "text":
        # The operator's hand: each glyph set on its own, a little off the
        # line and off the vertical, pressure varying, so a word does not come
        # out as a font. `size` is the cap height as a fraction of the sheet.
        x, y = sh.xy(*el["at"])
        tone = el.get("tone", 60)        # writing is pressed harder than a ruled line
        px = int(el.get("size", 0.035) * (sh.box[3] - sh.box[1]) * S)
        font = ImageFont.truetype(HAND, px)
        cx = x * S
        for ch in el["text"]:
            if ch == " ":
                cx += px * 0.35; continue
            g = Image.new("L", (px * 2, px * 2), 0)
            ImageDraw.Draw(g).text((px // 2, px // 4), ch, font=font, fill=255)
            g = g.rotate(sh.rng.normal(0, 4) + el.get("angle", 0), resample=Image.BICUBIC)
            press = sh.rng.uniform(0.7, 1.0)
            ink = int((255 - tone) * press)
            dy = sh.rng.normal(0, px * 0.04)
            mask = g.point(lambda v: v * ink // 255)
            sh.layer.paste(255 - ink, (int(cx - px // 2), int(y * S - px // 4 + dy)), mask)
            cx += font.getlength(ch) * sh.rng.uniform(0.95, 1.08)
    else:
        raise SystemExit(f"unknown mark '{kind}'")


def main():
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    doc = yaml.safe_load((ep / "paper.yaml").read_text())
    for sid, spec in doc["sheets"].items():
        src = ep / "approved" / f"{sid}.jpg"
        plate = Image.open(src).convert("RGB")
        sh = Sheet(plate.size, spec["box"], spec.get("seed", 9))
        for el in spec["marks"]:
            draw(sh, el)
        dst = ep / "approved" / f"{sid}.screen.jpg"
        sh.finish(plate).save(dst, quality=95)
        print(f"  {sid:<5} {len(spec['marks'])} marks -> {dst.name}")


if __name__ == "__main__":
    main()
