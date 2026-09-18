#!/usr/bin/env python3
"""The 9:16 assembler — one copy, imported by build_verticals.py and
build_teaser.py.

Both pieces are verticals in every sense the channel cares about: captions
burned in from real word timings, the bottom 30% clear, a voice inside the
first second. They were also two separate implementations of the same four
operations — render channel type onto transparency, trim shots out of takes
and crop them to 9:16, turn alignments into caption cues, and lay the type
over the picture. Record 03 lost a finished vertical to a paragraph parser
that existed in three places and was fixed in two, and this was the same
shape of fault waiting to happen: the slug plate had a shrink-to-fit guard in
one copy and not the other.

What is NOT shared is the sound bed, and that is deliberate. The teaser is
the one piece on this channel allowed a generated cue under it; a vertical cut
never is. Two mixes that must differ by rule do not belong behind one
function — the difference is the rule.

Also here: the word-timing helpers that decide where a cut may stop. The
builder and validate.py read cut points through the same two functions, so a
cut cannot be placed by one rule and checked by another.
"""
import functools, json, os, pathlib, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

print = functools.partial(print, flush=True)

W, H = 1080, 1920
SRC_W, SRC_H = 1920, 1080
CROP_W = 608                     # of 1920 — the only window that gives 9:16
FPS = 24


def ffmpeg():
    return os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")


def dur(path):
    probe = str(pathlib.Path(ffmpeg()).with_name("ffprobe"))
    return float(subprocess.run(
        [probe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True).stdout.strip())


# --- type ----------------------------------------------------------------

def text_plate(lines, spec, dst, size, tracking=None, centre=True,
               x=None, y=None):
    """Channel type on transparency: Menlo, phosphor green, halo and glow.

    Every character this channel puts on a screen comes out of one renderer in
    one font. The slug at the top of a cut and the line asking for the full
    record at the end of it are the same furniture and must not look like two
    decisions, which is why there is one function and not one per caller.

    Shrinks rather than overflowing. The closing card shipped clipped at both
    ends once — 36 characters at size 46 is about 1100 px in a 1080 px frame.
    Breaking the line is the real fix and lives in the config; this is the
    guard that makes overflow impossible rather than unlikely.
    """
    f = spec["font"]
    lines = lines if isinstance(lines, list) else [lines]
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    trk = f["tracking"] if tracking is None else tracking
    safe = spec["captions"].get("safe_width", W - 120)

    while size > 20:
        font = ImageFont.truetype(f["face"], size)
        widest = max(sum(d.textlength(c, font=font) + trk for c in l) - trk
                     for l in lines)
        if widest <= safe:
            break
        size -= 2
    font = ImageFont.truetype(f["face"], size)
    # 1.5, and it is worth saying why the number is written down here. The two
    # copies this function replaces disagreed: the teaser's used 1.5 and the
    # verticals' used 1.45, so the SOON card and the FULL RECORD card — the
    # same furniture, in the same font, two seconds apart in a viewer's feed —
    # were set to different leading, and nothing could have caught it because
    # each file was correct on its own. 1.5 is the one that shipped.
    lh = int(size * 1.5)

    for i, line in enumerate(lines):
        w = sum(d.textlength(c, font=font) + trk for c in line) - trk
        px = (W - w) / 2 if x is None else x
        py = (H / 2 - lh * len(lines) / 2 + i * lh) if centre else y + i * lh
        for ch in line:
            d.text((px, py), ch, font=font, fill=tuple(f["colour"]) + (f["alpha"],))
            px += d.textlength(ch, font=font) + trk

    a = img.split()[3]
    halo = Image.new("RGBA", img.size, (0, 0, 0, 0))
    halo.putalpha(a.filter(ImageFilter.GaussianBlur(f.get("halo_radius", 9)))
                   .point(lambda v: int(v * f.get("halo_alpha", 170) / 255)))
    glow = img.filter(ImageFilter.GaussianBlur(f.get("glow_radius", 7)))
    glow.putalpha(glow.split()[3].point(
        lambda v: int(v * f.get("glow_alpha", 150) / 255)))
    Image.alpha_composite(Image.alpha_composite(halo, glow), img).save(dst)
    return dst


# --- picture -------------------------------------------------------------

def crop_x_px(frac):
    """Window left edge in pixels from a centre given as a fraction of the
    frame width. 0.5 is the centre crop, which is the default and was the only
    option until record 04. Clamped so the window cannot leave the frame."""
    left = float(frac) * SRC_W - CROP_W / 2
    left = max(0.0, min(SRC_W - CROP_W, left))
    return int(left // 2 * 2)          # even, or the chroma planes disagree


def crop_expr(shot):
    """The x argument for the crop filter.

    A fixed number when the frame does not move, which is most shots. When
    `crop_to` is given the window travels from `crop_x` to `crop_to` across
    the shot — a pan inside a photograph, the same trick build_static.py uses
    on 16:9, and the only camera move a cut is allowed. Commas inside a filter
    expression are escaped, because ffmpeg reads a bare one as the end of the
    filter and not as an argument separator.
    """
    x0 = crop_x_px(shot.get("crop_x", 0.5))
    if shot.get("crop_to") is None:
        return str(x0)
    x1 = crop_x_px(shot["crop_to"])
    d = float(shot["seconds"])
    return f"trunc(({x0}+({x1 - x0})*min(t/{d:.3f}\\,1))/2)*2"


def build_picture(ep, shots, tmp, tail_clip=None):
    """Each shot trimmed out of its own take and cropped to 9:16.

    The picture comes from takes/, not from a window into the master, so the
    shots may be reordered and a shot may be used twice. Hard cuts only: a
    dissolve says a person edited this, which is the one thing the format
    cannot afford. What buys the attention instead is short shots, a subject
    that moves, and a crop that frames it — never a transition.
    """
    ff = ffmpeg()
    parts = []
    for s in shots:
        src = ep / "takes" / f"{s['id']}.mp4"
        if not src.exists():
            sys.exit(f"no take for shot {s['id']} — {src}")
        dst = tmp / f"p{len(parts):02d}.mp4"
        subprocess.run([
            ff, "-y", "-v", "error", "-ss", str(s.get("from", 0)), "-i", str(src),
            "-t", str(s["seconds"]),
            "-vf", (f"scale={SRC_W}:-2,"
                    f"crop={SRC_W}:{SRC_H}:(iw-{SRC_W})/2:(ih-{SRC_H})/2,"
                    f"crop={CROP_W}:{SRC_H}:{crop_expr(s)}:0,"
                    f"scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS}"),
            "-an", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
            str(dst)], check=True)
        parts.append(dst)
        move = (f"  crop {s.get('crop_x', 0.5):.2f}"
                + (f" -> {s['crop_to']:.2f}" if s.get("crop_to") is not None
                   else ""))
        print(f"  {s['id']:<5} {s['seconds']:4.1f}s from {s.get('from', 0):4.1f}s"
              f"{move}")
    if tail_clip:
        parts.append(tail_clip)

    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p.name}'\n" for p in parts))
    joined = tmp / "joined.mp4"
    subprocess.run([ff, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c", "copy", str(joined)], check=True)
    return joined


def black_card(lines, spec, tmp, seconds, size=64, name="card"):
    """The closing card, on black, silent. The caller puts sound under it —
    the room tone never stops, including here."""
    ff = ffmpeg()
    png = text_plate(lines, spec, tmp / f"{name}.png", size=size)
    dst = tmp / f"p99-{name}.mp4"
    subprocess.run([
        ff, "-y", "-v", "error",
        "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={seconds}",
        "-loop", "1", "-t", str(seconds), "-i", str(png),
        "-filter_complex", "[1:v]format=rgba,fade=t=in:st=0.2:d=0.5:alpha=1[c];"
                           "[0:v][c]overlay=0:0,setsar=1[v]",
        "-map", "[v]", "-c:v", "libx264", "-crf", "18",
        "-pix_fmt", "yuv420p", str(dst)], check=True)
    return dst


# --- word timings --------------------------------------------------------

def word_spans(ep, pid, picks):
    """(start, end, word) for a paragraph's chosen take, in the take's own
    time. The one reader of audio/alignment/, used by the builder and by
    validate.py, so a cut cannot be placed by one rule and checked by
    another."""
    j = ep / "audio" / "alignment" / f"{pid}_s{picks[pid]}.json"
    if not j.exists():
        return []
    return [(w["t"], w["e"], w["w"]) for w in json.loads(j.read_text())]


def line_words(ep, ln, picks):
    """A line's words, cut to `trim` when it gives only its first sentences."""
    words = word_spans(ep, ln["pid"], picks)
    if ln.get("trim"):
        words = [w for w in words if w[1] <= float(ln["trim"]) + 0.01]
    return words


def trim_fault(ep, ln, picks, tail):
    """Why this trim point is not a legal place to stop, or None.

    A cut stops mid-sentence, on a word boundary, never inside a word — a
    severed word is not a withheld ending, it is a file that broke. Checked
    with no tolerance at all: a first version allowed 0.02 s either side and
    passed a cut that clipped the last twenty milliseconds off "open", and a
    margin the size of the fault is not a check.

    And a word boundary is not the end of the sound. ElevenLabs marks a word
    as ending where the next one begins, which on this voice can be forty
    milliseconds later, so the point also needs real silence after it: `tail`
    seconds to the next word, or the end of the paragraph.
    """
    if not ln.get("trim"):
        return None                     # runs to the end of the take
    t = float(ln["trim"])
    words = word_spans(ep, ln["pid"], picks)
    if not words:
        return f"no alignment for {ln['pid']}"
    inside = [w for a, b, w in words if a < t < b]
    if inside:
        return (f"trim {t} falls inside the word \"{inside[0]}\" — "
                f"cut between words")
    before = [(b, w) for a, b, w in words if b <= t]
    last_e, last = before[-1] if before else (0.0, "?")
    after = [a for a, _, _ in words if a > t]
    gap = (min(after) - last_e) if after else 99.0
    if gap < tail:
        return (f"only {gap:.2f}s of silence after \"{last}\" — needs {tail}s, "
                f"or the word is heard being cut")
    return None


# --- captions ------------------------------------------------------------

def caption_cues(ep, lines, picks, bc):
    """(start, end, text) on the cut's own timeline.

    Mandatory on anything 9:16: it is watched muted first and read second.
    Built from the real word timings, offset by where each line sits, so they
    cannot drift from the voice. `bc` is build_captions, passed in rather than
    imported here so there is still one owner of the chunking rules.
    """
    cues = []
    for ln in lines:
        words = line_words(ep, ln, picks)
        if not words:
            print(f"  no alignment for {ln['pid']} — run build_captions.py first")
            continue
        for c in bc.chunk([{"t": a, "e": b, "w": w} for a, b, w in words]):
            if c:
                cues.append((float(ln["at"]) + c[0]["t"],
                             float(ln["at"]) + c[-1]["e"] + 0.25,
                             " ".join(x["w"] for x in c)))
    # A cue holds 0.25 s past its last word so a short line does not blink —
    # but never past the next cue's first word, or two captions draw at once.
    cues.sort()
    for n in range(len(cues) - 1):
        a, b, t = cues[n]
        cues[n] = (a, min(b, cues[n + 1][0] - 0.02), t)
    return cues


def overlay_type(joined, slug_png, cues, total, tmp, dst, bc,
                 slug_until=None):
    """Slug and captions over the picture. One ffmpeg pass, one overlay per
    cue, enabled over its own window."""
    ff = ffmpeg()
    ins = ["-i", str(joined), "-loop", "1", "-t", str(total), "-i", str(slug_png)]
    gate = f":enable='lt(t,{slug_until:.2f})'" if slug_until else ""
    chain = [f"[0:v][1:v]overlay=0:0{gate}[b0]"]
    for n, (a, b, text) in enumerate(cues):
        png = tmp / f"cue{n:02d}.png"
        bc.render(text).save(png)
        ins += ["-loop", "1", "-t", str(total), "-i", str(png)]
        chain.append(f"[b{n}][{n + 2}:v]overlay=0:0:"
                     f"enable='between(t,{a:.2f},{b:.2f})'[b{n + 1}]")
        print(f"  cue {a:5.1f}-{b:5.1f}s  {text}")
    subprocess.run([ff, "-y", "-v", "error", *ins,
                    "-filter_complex", ";".join(chain),
                    "-map", f"[b{len(cues)}]", "-t", str(total),
                    "-c:v", "libx264", "-crf", "19", "-preset", "slow",
                    "-pix_fmt", "yuv420p", str(dst)], check=True)
    return dst


# --- sound ---------------------------------------------------------------

def voice_chains(ep, lines, picks, total, level, start_idx):
    """The narration legs of a filter_complex: each take delayed to its place
    on the cut's timeline, trimmed where the line gives only its opening.

    Returns (inputs, chains, labels). The beds are the caller's business: the
    teaser gets a generated cue under it and a vertical cut never does, and
    that difference is a channel rule, not a parameter.
    """
    ins, fc, labels, i = [], [], [], start_idx
    for n, ln in enumerate(lines):
        f = ep / "audio" / "narration" / f"{ln['pid']}_s{picks[ln['pid']]}.mp3"
        if not f.exists():
            sys.exit(f"no take for {ln['pid']} — {f}")
        ins += ["-i", str(f)]
        d = int(float(ln["at"]) * 1000)
        trim = f"atrim=0:{ln['trim']},asetpts=N/SR/TB," if ln.get("trim") else ""
        fc.append(f"[{i}:a]{trim}volume={level}dB,adelay={d}|{d},"
                  f"apad,atrim=0:{total}[v{n}]")
        labels.append(f"[v{n}]")
        print(f"  {ln['pid']:<6} at {ln['at']:5.1f}s"
              + (f"  first {ln['trim']}s" if ln.get("trim") else ""))
        i += 1
    return ins, fc, labels, i
