#!/usr/bin/env python3
"""Stage 8 — render the episode's data cards, and the sound of them arriving.

Every character on this channel is drawn here, in one font, and types itself
on with a click per glyph. The spec is config/type.yaml and it is channel
furniture: identical in every record, never varied for an episode. See the
On-Screen Text section of CLAUDE.md.

Output, per card in cards.yaml:

    cards/<id>.mov   RGBA overlay (QuickTime RLE), exactly the card's length
    cards/<id>.wav   the click track for that card, same length
    cards/manifest.json   where each overlay sits on the episode timeline

The overlays are composited before the grain pass, never after — a card that
sits on top of the grain reads as a caption printed onto the recording
instead of as part of it.

Usage:
    build_cards.py <episode dir> [--only aldren-card] [--preview]

--preview burns every card onto out/rough-cut.mp4 and writes
out/rough-cut-cards.mp4, which is the only way to judge whether a card sits
where the plate has room for it.
"""
import json, math, pathlib, random, struct, subprocess, sys, tempfile, wave
import yaml
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FPS = 24
W, H = 1920, 1080
SR = 48000                      # click track sample rate


# --- the channel's text spec ------------------------------------------------

def load_type_spec():
    return yaml.safe_load(pathlib.Path("config/type.yaml").read_text())


def font_at(spec, size):
    return ImageFont.truetype(spec["font"]["face"], size)


def draw_tracked(d, xy, text, font, fill, tracking, shadow=None):
    """Menlo with letter-spacing. drawtext cannot do this, which is why every
    character on the channel comes out of Pillow instead."""
    x, y = xy
    for ch in text:
        if shadow:
            off, sa = shadow
            d.text((x + off, y + off), ch, font=font, fill=(0, 0, 0, sa))
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking
    return x


def tracked_width(d, text, font, tracking):
    if not text:
        return 0
    return sum(d.textlength(c, font=font) for c in text) + tracking * (len(text) - 1)


# --- typing ------------------------------------------------------------------

def type_schedule(lines, start, spec):
    """When each character of each line appears, and when each click fires.

    Returns (per-line reveal schedule, click times). A space costs the same
    time as a glyph but makes no sound — a click on a space reads as a stutter.
    """
    cps = spec["typing"]["chars_per_second"]
    jitter = spec["typing"]["jitter"]
    pause = spec["typing"]["line_pause_seconds"]
    rng = random.Random(20260909)          # fixed: the same card types the same way
    t = start
    schedule, clicks = [], []
    for line in lines:
        reveal = []
        for ch in line:
            step = (1.0 / cps) * (1 + rng.uniform(-jitter, jitter))
            t += step
            reveal.append(t)
            if ch != " ":
                clicks.append(t)
        schedule.append(reveal)
        t += pause
    return schedule, clicks


def visible(line, reveal, t):
    """The part of a line that has arrived by time t."""
    n = sum(1 for r in reveal if r <= t)
    return line[:n]


# --- card renderers ----------------------------------------------------------
#
# Each returns a list of (line_text, x, y, font_size) plus any non-text
# drawing, given the card's own geometry. Text always goes through the typing
# schedule; rules, axes and bars are drawn as soon as their line exists.

def anchor_xy(pos, spec, box_w, box_h):
    mx, my = spec["margin"] if "margin" in spec else (96, 72)
    if pos == "lower-left":
        return mx, H - my - box_h
    if pos == "lower-band":
        return mx, H - my - box_h
    if pos == "right-half":
        return W // 2 + mx // 2, my + 120
    if pos == "centre":
        return (W - box_w) // 2, (H - box_h) // 2
    return mx, my


def extras_height(card, size, lh):
    """How much room a card needs below its text.

    The first build anchored the text block to the bottom margin and then drew
    the bar, the counter and the plot underneath it — off the bottom of the
    frame. A card is the text plus everything it carries, and that is what
    gets anchored.
    """
    h = 0
    if card.get("bar"):
        h += int(size * 1.2) + 28 + 10 + 16
    if card.get("counter"):
        h += 20 + lh + int(size * 1.7) + 16
    if card.get("type") == "plot":
        h += 200 + 24 + int(size * 2.2)      # plot, then the figure under it
    if card.get("type") == "stacked_bar":
        h += 22 + 24
    return h


def card_lines(card):
    """The text of a card, as flat lines, in the order they type on.

    A `figure:` is not in here: it resolves after the graphic, alone and on
    its own clock, which is the whole point of it in scene 2 — the chart
    explains the band, and then one number lands under it and does not
    explain anything."""
    if card.get("lines") and isinstance(card["lines"][0], str):
        return list(card["lines"])
    if card.get("lines"):
        return [l["text"] for l in card["lines"]]
    if card.get("rows") and card.get("type") == "stacked_bar":
        return [f"{r['label']:<18}{r['value']}" for r in card["rows"]]
    if card.get("type") == "cosine":
        v = card["equator_speed"]
        return [card["format"].format(lat=lat, v=v * math.cos(math.radians(lat)))
                for lat in card["rows"]]
    return []


def finish(layer, spec):
    """Halo, glow, glyphs — in that order.

    The halo is a blurred black silhouette of the card and is the only reason
    it survives a bright salt pan; the glow is a blurred copy of the card
    itself, which is the phosphor bloom off an analogue monitor. Neither is a
    scrim: both are the shape of the text, so the frame still shows through
    everywhere the text is not.
    """
    f = spec["font"]
    a = layer.split()[3]
    halo = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    halo.putalpha(a.filter(ImageFilter.GaussianBlur(f.get("halo_radius", 9)))
                   .point(lambda v: int(v * f.get("halo_alpha", 170) / 255)))
    glow = layer.filter(ImageFilter.GaussianBlur(f.get("glow_radius", 7)))
    glow.putalpha(glow.split()[3].point(
        lambda v: int(v * f.get("glow_alpha", 150) / 255)))
    out = Image.alpha_composite(halo, glow)
    return Image.alpha_composite(out, layer)


def render_frame(card, spec, t, schedule, lines, size):
    """One RGBA frame of a card at absolute time t."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font_at(spec, size)
    tracking = spec["font"]["tracking"]
    colour = tuple(spec["font"]["colour"])
    alpha = spec["font"]["alpha"]
    shadow = None                 # the halo does this now, see finish()
    lh = int(size * 1.55)

    box_w = max((tracked_width(d, l, f, tracking) for l in lines), default=0)
    text_h = lh * len(lines)
    box_h = text_h + extras_height(card, size, lh)
    x0, y0 = anchor_xy(card.get("pos", "lower-left"), spec, box_w, box_h)

    for i, line in enumerate(lines):
        shown = visible(line, schedule[i], t)
        if not shown:
            continue
        y = y0 + i * lh
        draw_tracked(d, (x0, y), shown, f, colour + (alpha,), tracking, shadow)
        # A heading gets a hairline under it once its line is complete.
        if i == 0 and len(shown) == len(line) and card.get("build") == "line":
            w = tracked_width(d, line, f, tracking)
            d.line([(x0, y + lh - 6), (x0 + w, y + lh - 6)],
                   fill=colour + (spec.get("rule_alpha", 90),), width=1)

    extra = card.get("bar") or {}
    if extra and t >= extra["at"]:
        # A margin bar draining once, in real time. It is the only element on
        # the channel that moves continuously, and it moves because the thing
        # it measures is running out while you watch.
        frac = min(1.0, (t - extra["at"]) / extra["drain_seconds"])
        bw, bh = extra.get("width", 640), 10
        bx, by = x0, y0 + text_h + 28 + int(size * 1.2)
        d.rectangle([bx, by, bx + bw, by + bh],
                    outline=colour + (spec.get("rule_alpha", 90),), width=1)
        d.rectangle([bx + 1, by + 1, bx + 1 + (bw - 2) * (1 - frac), by + bh - 1],
                    fill=colour + (alpha,))
        label_f = font_at(spec, int(size * 0.8))
        draw_tracked(d, (bx, by - int(size * 1.2)), extra["label"], label_f,
                     colour + (alpha,), tracking, shadow)

    counter = card.get("counter") or {}
    if counter and t >= card["at"]:
        # An odometer counts up fast and settles. It ticks per digit change,
        # not per frame — see the click track.
        frac = min(1.0, (t - card["at"]) / counter["count_seconds"])
        eased = 1 - (1 - frac) ** 3
        value = int(counter["from"] + (counter["to"] - counter["from"]) * eased)
        big = font_at(spec, int(size * 1.7))
        text = f"{value:,} {counter['unit']}"
        y = y0 + text_h + 20
        draw_tracked(d, (x0, y), counter["label"], f, colour + (alpha,), tracking,
                     shadow)
        draw_tracked(d, (x0, y + lh), text, big, colour + (alpha,), tracking, shadow)

    fig = card.get("figure") or {}
    if fig and t >= fig["at"]:
        fsch, _ = type_schedule([fig["text"]], fig["at"], spec)
        shown = visible(fig["text"], fsch[0], t)
        if shown:
            draw_tracked(d, (x0, H - spec["margin"][1] - int(size * 1.6)),
                         shown, f, colour + (alpha,), tracking, shadow)

    if card.get("type") == "plot":
        draw_plot(d, card, spec, t, x0, y0 + text_h, size)
    if card.get("type") == "cosine":
        draw_cosine(d, card, spec, t, x0 + box_w + 90, y0, size, text_h)
    if card.get("type") == "stacked_bar":
        draw_stack(d, card, spec, t, x0, y0 + text_h + 24, size)
    return finish(img, spec)


def draw_plot(d, card, spec, t, x0, y0, size):
    """Temperature across the band. The shaded window is measured against the
    axis, not eyeballed — the 60 km width is the whole point of the graphic."""
    colour = tuple(spec["font"]["colour"]); alpha = spec["font"]["alpha"]
    rule = spec.get("rule_alpha", 90)
    pw, ph = 900, 200
    draw_s = min(1.0, max(0.0, (t - card["at"]) / card.get("draw_seconds", 3.0)))
    if draw_s <= 0:
        return
    ax, ay = card["x_axis"], card["y_axis"]
    d.line([(x0, y0 + ph), (x0 + pw, y0 + ph)], fill=colour + (rule,), width=2)
    d.line([(x0, y0), (x0, y0 + ph)], fill=colour + (rule,), width=2)

    def px(v): return x0 + (v - ax["from"]) / (ax["to"] - ax["from"]) * pw
    def py(v): return y0 + ph - (v - ay["from"]) / (ay["to"] - ay["from"]) * ph

    sh = card.get("shade")
    if sh:
        x1, x2 = px(sh["from"]), px(sh["to"])
        if x2 <= x0 + pw * draw_s:
            d.rectangle([x1, y0, x2, y0 + ph], fill=colour + (40,))
            d.line([(x1, y0), (x1, y0 + ph)], fill=colour + (rule,), width=1)
            d.line([(x2, y0), (x2, y0 + ph)], fill=colour + (rule,), width=1)
    # A smooth fall from day side to night side across the band.
    pts = []
    steps = int(200 * draw_s)
    for i in range(max(steps, 2)):
        kx = ax["from"] + (ax["to"] - ax["from"]) * i / 199
        k = 1 / (1 + math.exp(kx / 26))
        pts.append((px(kx), py(ay["from"] + (ay["to"] - ay["from"]) * k)))
    if len(pts) > 1:
        d.line(pts, fill=colour + (alpha,), width=3)


def draw_cosine(d, card, spec, t, x0, y0, size, box_h):  # x0 is past the table
    """Required speed by latitude. The curve is drawn from the function, not
    traced: the table and the curve have to agree, because the narration reads
    two of the rows out loud."""
    colour = tuple(spec["font"]["colour"]); alpha = spec["font"]["alpha"]
    rule = spec.get("rule_alpha", 90)
    # The curve sits beside the table, not behind it: the table is read and
    # the curve is glanced at, and a curve under six lines of numbers is
    # neither. x0 already arrives offset past the table's width.
    cw, ch = 420, max(220, box_h)
    cx, cy = x0, y0
    d.line([(cx, cy + ch), (cx + cw, cy + ch)], fill=colour + (rule,), width=1)
    d.line([(cx, cy), (cx, cy + ch)], fill=colour + (rule,), width=1)
    n = max(2, int(90 * min(1.0, (t - card["at"]) / 2.0)))
    pts = [(cx + cw * lat / 90,
            cy + ch - ch * math.cos(math.radians(lat))) for lat in range(0, n + 1)]
    if len(pts) > 1:
        d.line(pts, fill=colour + (alpha,), width=3)


def draw_stack(d, card, spec, t, x0, y0, size):
    """Basal against locomotion, to scale, with each segment named inside it.

    The first build drew two unlabelled rectangles under the numbers and they
    read as a progress bar for nothing. A bar that does not say what it is
    measuring is decoration, and this channel does not do decoration.
    """
    colour = tuple(spec["font"]["colour"]); alpha = spec["font"]["alpha"]
    tracking = spec["font"]["tracking"]
    segs = [(r["label"], r["segment"], r["at"]) for r in card["rows"] if r.get("segment")]
    if not segs:
        return
    total = sum(s[1] for s in segs)
    bw, bh = 900, int(size * 1.1)
    lab = font_at(spec, int(size * 0.62))
    x = x0
    for label, value, at in segs:
        if t < at:
            break
        w = bw * value / total
        # Locomotion is the segment the scene is about, so it is the one that
        # is filled; basal is barely tinted. The two must not read as one bar.
        fill = int(alpha * 0.50) if "locomotion" in label else int(alpha * 0.10)
        d.rectangle([x, y0, x + w, y0 + bh], fill=colour + (fill,))
        d.rectangle([x, y0, x + w, y0 + bh], outline=colour + (alpha,), width=2)
        draw_tracked(d, (x + 10, y0 + (bh - int(size * 0.62)) / 2 - 2),
                     f"{label} {value}", lab, colour + (alpha,), tracking)
        x += w


# --- the click track ---------------------------------------------------------

def click_sample(spec):
    """One click, synthesised. Never sampled and never generated by a model, so
    it is byte-identical between episodes — a signature that drifts is worse
    than no signature."""
    c = spec["click"]
    n = int(SR * (c["attack_ms"] + c["decay_ms"]) / 1000)
    rng = random.Random(1178)
    centre, bw = c["centre_hz"], c["bandwidth_hz"]
    out, prev, prev2 = [], 0.0, 0.0
    # a two-pole resonator excited by noise: a band-passed burst without scipy
    r = math.exp(-math.pi * bw / SR)
    w0 = 2 * math.pi * centre / SR
    a1, a2 = 2 * r * math.cos(w0), -r * r
    for i in range(n):
        drive = rng.uniform(-1, 1) * math.exp(-i / (SR * c["decay_ms"] / 3000))
        y = drive + a1 * prev + a2 * prev2
        prev2, prev = prev, y
        out.append(y)
    peak = max(abs(v) for v in out) or 1.0
    gain = 10 ** (c["level_dbfs"] / 20)
    return [v / peak * gain for v in out]


def write_clicks(path, times, length_s, spec):
    c = spec["click"]
    base = click_sample(spec)
    buf = [0.0] * int(SR * length_s + len(base) + 1)
    rng = random.Random(4242)
    for t in times:
        # tiny pitch variation so a long line does not machine-gun
        step = 1 + rng.uniform(-c["pitch_jitter"], c["pitch_jitter"])
        start = int(t * SR)
        for i in range(int(len(base) / step)):
            src = base[min(int(i * step), len(base) - 1)]
            j = start + i
            if 0 <= j < len(buf):
                buf[j] += src
    with wave.open(str(path), "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(b"".join(
            struct.pack("<h", max(-32767, min(32767, int(v * 32767)))) for v in buf))


# --- main --------------------------------------------------------------------

def build_card(card, spec, ep, ff):
    lines = card_lines(card)
    start = card["at"]
    if card.get("build") == "line" and card.get("interval"):
        # A card that builds line by line still types each line; the interval
        # is the earliest a line may start.
        schedule, clicks = [], []
        t = start
        for i, line in enumerate(lines):
            sch, cl = type_schedule([line], max(t, start + i * card["interval"]), spec)
            schedule += sch; clicks += cl
            t = sch[0][-1] if sch[0] else t
    else:
        schedule, clicks = type_schedule(lines, start, spec)

    fig = card.get("figure") or {}
    if fig:
        _, fig_clicks = type_schedule([fig["text"]], fig["at"], spec)
        clicks += fig_clicks

    end = card.get("hold_until") or (max((r[-1] for r in schedule if r), default=start) + 3)
    for extra_key in ("bar", "counter", "figure"):
        e = card.get(extra_key) or {}
        if e.get("at"):
            end = max(end, e["at"] + e.get("drain_seconds", e.get("hold", 2)))
    if card.get("type") == "plot":
        end = max(end, card["at"] + card.get("draw_seconds", 3) + 1)
    dur = end - start
    frames = int(round(dur * FPS))
    size = card.get("size") or 26

    tmp = pathlib.Path(tempfile.mkdtemp())
    for i in range(frames):
        t = start + i / FPS
        render_frame(card, spec, t, schedule, lines, size).save(tmp / f"{i:05d}.png")

    out = ep / "cards"; out.mkdir(exist_ok=True)
    mov = out / f"{card['id']}.mov"
    subprocess.run([ff, "-y", "-v", "error", "-framerate", str(FPS),
                    "-i", str(tmp / "%05d.png"), "-c:v", "qtrle",
                    "-pix_fmt", "argb", str(mov)], check=True)
    wav = out / f"{card['id']}.wav"
    write_clicks(wav, [c - start for c in clicks], dur, spec)
    return {"id": card["id"], "shot": card.get("shot"), "at": start,
            "duration": round(dur, 3), "mov": mov.name, "wav": wav.name,
            "clicks": len(clicks)}


def main():
    args = [a for a in sys.argv[1:]]
    only = None
    if "--only" in args:
        i = args.index("--only"); only = args[i + 1]; del args[i:i + 2]
    preview = "--preview" in args
    if preview:
        args.remove("--preview")
    ep = pathlib.Path(args[0] if args else "episodes/ep-02-sunrise-line")
    ff = "/usr/local/opt/ffmpeg-full/bin/ffmpeg"
    spec = load_type_spec()
    doc = yaml.safe_load((ep / "cards.yaml").read_text())
    spec["margin"] = doc["style"].get("margin", [96, 72])
    spec["rule_alpha"] = doc["style"].get("rule_alpha", 90)

    manifest = []
    for card in doc["cards"]:
        if only and card["id"] != only:
            continue
        m = build_card(card, spec, ep, ff)
        manifest.append(m)
        print(f"  {m['id']:<20} at {m['at']:7.1f}s  {m['duration']:5.1f}s  "
              f"{m['clicks']:4d} clicks")
    (ep / "cards" / "manifest.json").write_text(json.dumps(manifest, indent=2))

    if preview:
        cut = ep / "out" / "rough-cut.mp4"
        dst = ep / "out" / "rough-cut-cards.mp4"
        args_ff = [ff, "-y", "-v", "error", "-i", str(cut)]
        for m in manifest:
            args_ff += ["-i", str(ep / "cards" / m["mov"])]
        fc, last = "", "[0:v]"
        for i, m in enumerate(manifest, start=1):
            out_l = f"[v{i}]" if i < len(manifest) else "[v]"
            fc += (f"{last}[{i}:v]overlay=0:0:enable='between(t,{m['at']},"
                   f"{m['at'] + m['duration']:.3f})':"
                   f"x=0:y=0:eof_action=pass{out_l};")
            last = out_l
        # each overlay is shorter than the cut, so it is delayed into place
        for i, m in enumerate(manifest, start=1):
            fc = fc.replace(f"[{i}:v]", f"[d{i}]", 1)
        pre = "".join(f"[{i}:v]setpts=PTS-STARTPTS+{m['at']}/TB[d{i}];"
                      for i, m in enumerate(manifest, start=1))
        subprocess.run(args_ff + ["-filter_complex", pre + fc.rstrip(";"),
                                  "-map", "[v]", "-c:v", "libx264", "-crf", "20",
                                  "-pix_fmt", "yuv420p", "-an", str(dst)], check=True)
        print(f"\npreview: {dst}")


if __name__ == "__main__":
    main()
