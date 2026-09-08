#!/usr/bin/env python3
"""Captions for the vertical cuts, timed from the real audio.

Word timings come from ElevenLabs' with-timestamps endpoint, called with the
same seed AND the same previous_text as the take that is actually in the
episode. Both are needed: with the seed alone a paragraph came back a full
second shorter, because previous_text changes the delivery. With both, the
regenerated audio matches the stored file to the millisecond, so the alignment
is valid for the file already in the mix.

Alignments are cached — the API is only asked once per paragraph.
"""
import os, sys, json, base64, subprocess, pathlib, re, urllib.request, yaml
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, "scripts")
from sync_titles import placement

FONT_PATH = "/System/Library/Fonts/Menlo.ttc"
VW, VH = 1080, 1920
SIZE, TRACK, LINE_H = 46, 1.5, 66
BOTTOM_LINES = 4              # empty lines kept clear under the captions
LINE_CHARS = 30               # per rendered line
CUE_CHARS  = 58               # per cue, i.e. up to two lines
MIN_TAIL   = 18               # a trailing cue shorter than this is an orphan
SAFE_W     = 900              # keep a real margin; the frame is 1080 wide
INK = (240, 238, 232)

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
        "-of","default=nw=1:nk=1",str(p)], capture_output=True, text=True).stdout)

def paragraphs(script):
    order, paras = [], {}
    for sc, blk in enumerate(re.findall(r"\*\*Narration:\*\*\n((?:>.*\n)+)", script), 1):
        txt = re.sub(r"^> ?", "", blk, flags=re.M)
        for i, p in enumerate([x.strip() for x in txt.split("\n\n") if x.strip()], 1):
            pid = f"s{sc}p{i}"; order.append(pid); paras[pid] = " ".join(p.split())
    return order, paras

def alignment(pid, text, prev, seed, voice, key, cache_dir):
    cache = cache_dir / f"{pid}_s{seed}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    body = {"text": text, "model_id": voice["model_id"],
            "voice_settings": voice["settings"], "seed": seed}
    if prev:
        body["previous_text"] = prev
    r = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice['voice_id']}"
        f"/with-timestamps?output_format={voice['output_format']}",
        data=json.dumps(body).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(r, timeout=180))
    a = d["alignment"]
    words, cur, t0 = [], "", None
    for c, s, e in zip(a["characters"], a["character_start_times_seconds"],
                       a["character_end_times_seconds"]):
        if c == " ":
            if cur: words.append({"w": cur, "t": t0, "e": last_e}); cur = ""; t0 = None
        else:
            if not cur: t0 = s
            cur += c; last_e = e
    if cur: words.append({"w": cur, "t": t0, "e": last_e})
    cache.write_text(json.dumps(words, indent=1))
    return words

def wrap(text):
    """Break one cue into at most two balanced lines."""
    if len(text) <= LINE_CHARS:
        return [text]
    words, best = text.split(), None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        if len(a) > LINE_CHARS or len(b) > LINE_CHARS:
            continue
        score = abs(len(a) - len(b))
        if best is None or score < best[0]:
            best = (score, [a, b])
    return best[1] if best else [text]

def chunk(words):
    """Group words into cues of at most two lines.

    A cue is allowed two lines so that a whole sentence can stay together —
    the first pass was one line per cue, which left the line the third short
    is named for split across two captions with "moving away." stranded on
    its own. Sentences break first, commas second, and a stranded tail is
    rebalanced against the cue before it.
    """
    out, cur = [], []
    for w in words:
        cand = " ".join(x["w"] for x in cur + [w])
        if cur and len(cand) > CUE_CHARS:
            out.append(cur); cur = [w]
        else:
            cur.append(w)
        if w["w"].endswith((".", "?", "!")):
            out.append(cur); cur = []
        elif w["w"].endswith(",") and len(" ".join(x["w"] for x in cur)) > 30:
            out.append(cur); cur = []
    if cur: out.append(cur)
    out = [c for c in out if c]

    # Rebalance a stranded tail — but a short cue that is a whole sentence is
    # not stranded, it is a beat. "Nominal." standing alone is the point;
    # pulling words back into it produced "Delay on their end, one point" /
    # "three one. Nominal." and split the reading across two captions.
    for i in range(1, len(out)):
        whole_sentence = (out[i][-1]["w"].endswith((".", "?", "!"))
                          and len(out[i]) <= 2)
        if whole_sentence:
            continue
        while (len(" ".join(x["w"] for x in out[i])) < MIN_TAIL
               and len(out[i - 1]) > 1):
            moved = out[i - 1][-1]
            if len(" ".join(x["w"] for x in [moved] + out[i])) > CUE_CHARS:
                break
            out[i - 1] = out[i - 1][:-1]
            out[i] = [moved] + out[i]
    return out

def render(text):
    lines = wrap(text)
    probe = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    size = SIZE
    while size > 30:
        f = ImageFont.truetype(FONT_PATH, size)
        widest = max(sum(probe.textlength(c, font=f) + TRACK for c in l) for l in lines)
        if widest <= SAFE_W:
            break
        size -= 2
    f = ImageFont.truetype(FONT_PATH, size)

    def paint(fill, layer):
        d = ImageDraw.Draw(layer)
        # the block grows upward, so the clear space below never shrinks
        y0 = VH - BOTTOM_LINES * LINE_H - LINE_H * len(lines)
        for i, l in enumerate(lines):
            w = sum(d.textlength(c, font=f) + TRACK for c in l)
            x = (VW - w) / 2
            for ch in l:
                d.text((x, y0 + i * LINE_H), ch, font=f, fill=fill)
                x += d.textlength(ch, font=f) + TRACK

    im = Image.new("RGBA", (VW, VH), (0, 0, 0, 0)); paint(INK + (250,), im)
    # a soft dark halo so the type holds over both dark metal and lit screens,
    # without a caption box, which would look like a player overlay
    halo = Image.new("RGBA", (VW, VH), (0, 0, 0, 0)); paint((0, 0, 0, 220), halo)
    halo = halo.filter(ImageFilter.GaussianBlur(10))
    return Image.alpha_composite(halo, im)

def main():
    ep = pathlib.Path("episodes/ep-01-tishina-9")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())
    key = os.environ["ELEVENLABS_API_KEY"]
    voice = yaml.safe_load(pathlib.Path("config/voice.yaml").read_text())["narrator"]
    picks = yaml.safe_load((ep / "audio" / "narration.yaml").read_text())["picks"]
    order, paras = paragraphs((ep / "script.md").read_text())
    prev_of = {order[i]: (paras[order[i-1]] if i else None) for i in range(len(order))}
    pos = placement(ep)
    cache_dir = ep / "audio" / "alignment"; cache_dir.mkdir(exist_ok=True)

    vid, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    src = ep / "out" / "verticals" / f"{vid}.mp4"
    out_dir = ep / "out" / "captions" / vid
    out_dir.mkdir(parents=True, exist_ok=True)

    cues = []
    for pid in order:
        t0 = pos[pid]
        d = dur(ep / "audio" / "narration" / f"{pid}_s{picks[pid]}.mp3")
        # Tolerance matters: the line the whole short is built to end on
        # finishes exactly at b, and a bare > comparison dropped it.
        if t0 < a - 0.01 or t0 + d > b + 0.05:
            continue
        words = alignment(pid, paras[pid], prev_of[pid], picks[pid], voice, key, cache_dir)
        for grp in chunk(words):
            text = " ".join(w["w"] for w in grp)
            cues.append((t0 - a + grp[0]["t"], t0 - a + grp[-1]["e"] + 0.18, text))

    # Never two captions on screen at once: a cue's tail is trimmed to the
    # next cue's head. The +0.18 hold reads well at the end of a sentence and
    # badly in the middle of one.
    for i in range(len(cues) - 1):
        s, e, txt = cues[i]
        cues[i] = (s, min(e, cues[i + 1][0] - 0.04), txt)

    for i, (s, e, text) in enumerate(cues):
        render(text).save(out_dir / f"c{i:02d}.png")
        print(f"  {s:6.2f}–{e:5.2f}  {text}")

    ins = ["-i", str(src)]
    for i in range(len(cues)):
        ins += ["-loop", "1", "-t", str(b - a), "-r", "24",
                "-i", str(out_dir / f"c{i:02d}.png")]
    fc, last = [], "0:v"
    for i, (s, e, _) in enumerate(cues, start=1):
        fc.append(f"[{i}:v]format=rgba,fade=t=in:st={s:.2f}:d=0.18:alpha=1,"
                  f"fade=t=out:st={e-0.18:.2f}:d=0.18:alpha=1[c{i}]")
        fc.append(f"[{last}][c{i}]overlay=0:0:enable='between(t,{s-0.05:.2f},{e+0.05:.2f})'[o{i}]")
        last = f"o{i}"
    dst = ep / "out" / "verticals" / f"{vid}-captioned.mp4"
    subprocess.run([ff, "-y", "-v", "error", *ins, "-filter_complex", ";".join(fc),
                    "-map", f"[{last}]", "-map", "0:a",
                    "-c:v", "libx264", "-crf", "20", "-preset", "slow", "-tune", "grain",
                    "-c:a", "copy", "-pix_fmt", "yuv420p", str(dst)], check=True)
    print(f"\n  {len(cues)} cues -> {dst}  ({dst.stat().st_size/1048576:.1f} МБ)")

if __name__ == "__main__":
    main()
