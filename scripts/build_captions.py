#!/usr/bin/env python3
"""Captions for the vertical cuts, timed from the real audio.

Word timings come from ElevenLabs' with-timestamps endpoint, called with the
same seed AND the same previous_text as the take that is actually in the
episode. Both matter: with the seed alone a paragraph came back a full second
shorter, because previous_text changes the delivery. With both, the
regenerated audio matches the stored file to the millisecond, so the alignment
is valid for the file already in the mix.

Unless the model refuses previous_text, which eleven_v3 does — it rejects the
request outright. That is not a problem here, it is a requirement: the takes on
that voice were themselves generated without it, so an alignment call that sent
it would be describing a delivery the episode does not contain. The rule is the
same either way — ask for exactly what the stored take was asked for.

Alignments are cached — the API is only asked once per paragraph.
"""
import os, sys, json, base64, subprocess, pathlib, re, urllib.request, yaml
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, "scripts")
import importlib.util
_spec = importlib.util.spec_from_file_location("ba", "scripts/build_audio.py")
ba = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(ba)

VW, VH = 1080, 1920
MIN_TAIL = 18                 # a trailing cue shorter than this is an orphan
CFG = yaml.safe_load(pathlib.Path("config/type.yaml").read_text())
FONT_PATH  = CFG["font"]["face"]
C          = CFG["captions"]
SIZE, TRACK, LINE_H = C["size"], C["tracking"], C["line_height"]
LINE_CHARS, CUE_CHARS = C["line_chars"], C["cue_chars"]
SAFE_W = C["safe_width"]
INK = tuple(C["colour"])
# Kept clear at the bottom of every vertical, for the platform's own furniture.
BOTTOM_CLEAR = int(VH * C["bottom_clear"])

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
        "-of","default=nw=1:nk=1",str(p)], capture_output=True, text=True).stdout)

# The parser lives in build_audio.py and is shared. This file had its own copy
# and it was the copy that never learned to strip stage directions.
paragraphs = ba.narration_paragraphs

def alignment(pid, text, prev, seed, voice, key, cache_dir):
    cache = cache_dir / f"{pid}_s{seed}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    body = {"text": text, "model_id": voice["model_id"], "seed": seed}
    if voice.get("settings"):
        body["voice_settings"] = voice["settings"]
    if prev:
        body["previous_text"] = prev

    def send(b):
        r = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice['voice_id']}"
            f"/with-timestamps?output_format={voice['output_format']}",
            data=json.dumps(b).encode(),
            headers={"xi-api-key": key, "Content-Type": "application/json"})
        return json.load(urllib.request.urlopen(r, timeout=180))
    try:
        d = send(body)
    except urllib.error.HTTPError as e:
        detail = e.read()[:400].decode(errors="replace")
        if "previous_text" in detail and "previous_text" in body:
            body.pop("previous_text")
            d = send(body)          # the stored take was made this way too
        else:
            print(f"  HTTP {e.code} on {pid}\n    {detail}")
            raise
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

    # Rebalance a stranded tail — but a cue that is a whole sentence is not
    # stranded, it is a beat. "Nominal." standing alone is the point.
    #
    # And the rule may never create the problem it exists to solve: pulling a
    # word back out of the previous cue is only allowed if what is left is
    # still a readable cue. Without that guard, "There is no destination." /
    # "There never was." was rebalanced into "There is no" / "destination.
    # There never was." — the tail was fixed by orphaning the head.
    for i in range(1, len(out)):
        starts_sentence = out[i - 1][-1]["w"].endswith((".", "?", "!"))
        ends_sentence = out[i][-1]["w"].endswith((".", "?", "!"))
        if starts_sentence and ends_sentence:
            continue
        while (len(" ".join(x["w"] for x in out[i])) < MIN_TAIL
               and len(out[i - 1]) > 1):
            moved = out[i - 1][-1]
            rest = " ".join(x["w"] for x in out[i - 1][:-1])
            if len(rest) < MIN_TAIL:
                break
            if len(" ".join(x["w"] for x in [moved] + out[i])) > CUE_CHARS:
                break
            out[i - 1] = out[i - 1][:-1]
            out[i] = [moved] + out[i]

    # Whatever is still a short head with no sentence in it joins the cue after
    # it, if the two fit together.
    i = 0
    while i < len(out) - 1:
        head = " ".join(x["w"] for x in out[i])
        joined = len(head) + 1 + len(" ".join(x["w"] for x in out[i + 1]))
        if (len(head) < MIN_TAIL and not head.endswith((".", "?", "!"))
                and joined <= CUE_CHARS):
            out[i + 1] = out[i] + out[i + 1]
            del out[i]
            continue
        i += 1

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
        # The block grows upward, so the clear space below never shrinks — and
        # the scrim is part of the block, not an extra under it. The whole
        # thing is lifted by scrim_pad so the gradient's bottom edge lands on
        # the clear line instead of 28 px inside it, which is where the first
        # version put it.
        y0 = (VH - BOTTOM_CLEAR - C.get("scrim_pad", 0)
              - LINE_H * len(lines))
        for i, l in enumerate(lines):
            w = sum(d.textlength(c, font=f) + TRACK for c in l)
            x = (VW - w) / 2
            for ch in l:
                d.text((x, y0 + i * LINE_H), ch, font=f, fill=fill)
                x += d.textlength(ch, font=f) + TRACK

    im = Image.new("RGBA", (VW, VH), (0, 0, 0, 0)); paint(INK + (C["alpha"],), im)
    # a soft dark halo so the type holds over both dark metal and lit screens,
    # without a caption box, which would look like a player overlay
    halo = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    paint((0, 0, 0, C["halo_alpha"]), halo)
    halo = halo.filter(ImageFilter.GaussianBlur(C["halo_radius"]))

    # The scrim: a gradient, not a box. See config/type.yaml. It sits under
    # both the halo and the type, covers exactly the band the lines occupy,
    # and fades to nothing over `scrim_feather` px above them, so it has no
    # edge for the eye to find.
    a0, fade = C.get("scrim_alpha", 0), C.get("scrim_feather", 180)
    if a0:
        pad = C.get("scrim_pad", 28)
        top = VH - BOTTOM_CLEAR - pad - LINE_H * len(lines) - fade
        bot = VH - BOTTOM_CLEAR          # exactly the clear line, never past it
        col = np.zeros(VH, dtype=np.uint8)
        for y in range(max(0, top), min(VH, bot)):
            k = (y - top) / fade
            col[y] = int(a0 * min(1.0, k) ** 2 if k < 1 else a0)
        scrim = Image.fromarray(np.repeat(col[:, None], VW, axis=1), mode="L")
        layer = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
        layer.putalpha(scrim)
        return Image.alpha_composite(Image.alpha_composite(layer, halo), im)
    return Image.alpha_composite(halo, im)

def main():
    args = sys.argv[1:]
    only = None
    if "--only" in args:
        i = args.index("--only"); only = args[i + 1]; del args[i:i + 2]
    ep = pathlib.Path(args[0] if args else "episodes/ep-02-sunrise-line")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())
    key = os.environ["ELEVENLABS_API_KEY"]
    # Which voice is an episode fact — see gen_narration.py. Reading "narrator"
    # here regardless would have timed record 3's captions against a voice that
    # is not in the record.
    which = (yaml.safe_load((ep / "shots.yaml").read_text()).get("voice")
             or "narrator")
    voice = yaml.safe_load(pathlib.Path("config/voice.yaml").read_text())[which]
    picks = yaml.safe_load((ep / "audio" / "narration.yaml").read_text())["picks"]
    order, paras = paragraphs((ep / "script.md").read_text())
    prev_of = {order[i]: (paras[order[i-1]] if i else None) for i in range(len(order))}

    # Placement comes from the same function the mix uses, so a caption cannot
    # disagree with the audio it is transcribing. Record 01 kept a second copy
    # of the scene constants in sync_titles.py; there is only one copy now.
    cfg = yaml.safe_load((ep / "audio.yaml").read_text())
    shots = yaml.safe_load((ep / "shots.yaml").read_text())["shots"]
    start, end = ba.scene_bounds(shots)
    # The same anchors the mix was laid with — this was the third copy of the
    # placement call and the second one to be missing them, which would time
    # every caption against a mix nobody built. Count the copies before fixing
    # the bug: there were three, and two of them were wrong.
    pos = {pid: t for pid, _, t in
           ba.place(picks, ep / "audio", start, end, cfg,
                    ba.card_anchors(ep, shots))}
    cache_dir = ep / "audio" / "alignment"; cache_dir.mkdir(parents=True, exist_ok=True)

    # --align-only fetches and caches the word timings for every paragraph and
    # stops there, without needing verticals.yaml to exist.
    #
    # This exists because the pipeline had a circle in it. A cut's in and out
    # points come from the real word timings — the channel refuses an estimate,
    # because record 03 shipped two verticals cut inside a word — and those
    # timings live in audio/alignment/. But the only thing that ever filled
    # audio/alignment/ was this script, and this script reads verticals.yaml on
    # its way there. So the file whose contents depend on the alignments had to
    # exist before the alignments could be fetched, and record 04's cut points
    # were chosen against a set of timings someone had already produced by
    # running the script far enough to crash.
    #
    # Same API, same seeds, same previous_text, same cache. Nothing here is a
    # second copy of the alignment call; it is the same function, stopped early.
    align_only = "--align-only" in sys.argv
    for pid in order:
        if not align_only:
            break
        alignment(pid, paras[pid], prev_of[pid], picks[pid], voice, key, cache_dir)
        print(f"  aligned {pid}")
    if align_only:
        print(f"\n{len(order)} paragraphs aligned into {cache_dir}")
        return 0

    verticals = yaml.safe_load((ep / "verticals.yaml").read_text())

    # This stage burns captions into a cut that was carved out of the master as
    # one window — records 01 to 03. From record 04 a cut is assembled, and its
    # captions are laid on by build_verticals.py through the shared assembler
    # in scripts/vertical.py, off the same alignments. Running this over an
    # assembled cut would put a second set of captions on top of the first.
    #
    # What still lives here and is not duplicated anywhere: `alignment()`,
    # which is the one caller of the ElevenLabs with-timestamps endpoint and
    # the only thing that writes audio/alignment/, and `chunk()` and
    # `render()`, which the assembler imports rather than reimplements. This
    # module remains the owner of caption text and caption timing; it has
    # simply stopped being the thing that draws them onto a 9:16 file.
    assembled = [c["id"] for c in verticals["cuts"] if "to" not in c]
    if assembled:
        print(f"  {len(assembled)} assembled cut(s) — captions come out of "
              f"build_verticals.py, not from here")

    for cut in verticals["cuts"]:
        if only and cut["id"] != only:
            continue
        if "to" not in cut:
            continue
        vid, a, b = cut["id"], cut["from"], cut["to"]
        src = ep / "out" / "verticals" / f"{vid}.mp4"
        if not src.exists():
            print(f"  {vid}: no {src} — run build_verticals.py first"); continue
        out_dir = ep / "out" / "captions" / vid
        out_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n  {vid}  {a:.1f}-{b:.1f}s")

        cues = []
        for pid in order:
            if pid not in pos:
                continue
            t0 = pos[pid]
            d = dur(ep / "audio" / "narration" / f"{pid}_s{picks[pid]}.mp3")
            # A paragraph that starts inside the window counts, even if the cut
            # lands mid-word — that last half sentence is the point of the cut.
            if t0 + d < a - 0.01 or t0 > b - 0.2:
                continue
            words = alignment(pid, paras[pid], prev_of[pid], picks[pid],
                              voice, key, cache_dir)
            for grp in chunk(words):
                s_t = t0 - a + grp[0]["t"]
                e_t = t0 - a + grp[-1]["e"] + 0.18
                if e_t <= 0 or s_t >= b - a:
                    continue
                cues.append((max(0.0, s_t), min(b - a, e_t),
                             " ".join(w["w"] for w in grp)))

        # Never two captions on screen at once: a cue's tail is trimmed to the
        # next cue's head. The +0.18 hold reads well at the end of a sentence
        # and badly in the middle of one.
        for i in range(len(cues) - 1):
            s_t, e_t, txt = cues[i]
            cues[i] = (s_t, min(e_t, cues[i + 1][0] - 0.04), txt)

        for i, (s_t, e_t, text) in enumerate(cues):
            render(text).save(out_dir / f"c{i:02d}.png")
            print(f"    {s_t:6.2f}-{e_t:5.2f}  {text}")

        ins = ["-i", str(src)]
        for i in range(len(cues)):
            ins += ["-loop", "1", "-t", str(b - a), "-r", "24",
                    "-i", str(out_dir / f"c{i:02d}.png")]
        fc, last = [], "0:v"
        for i, (s_t, e_t, _) in enumerate(cues, start=1):
            fc.append(f"[{i}:v]format=rgba,fade=t=in:st={s_t:.2f}:d=0.18:alpha=1,"
                      f"fade=t=out:st={max(0, e_t - 0.18):.2f}:d=0.18:alpha=1[c{i}]")
            fc.append(f"[{last}][c{i}]overlay=0:0:"
                      f"enable='between(t,{max(0, s_t - 0.05):.2f},{e_t + 0.05:.2f})'"
                      f"[o{i}]")
            last = f"o{i}"
        dst = ep / "out" / "verticals" / f"{vid}-captioned.mp4"
        subprocess.run([ff, "-y", "-v", "error", *ins,
                        "-filter_complex", ";".join(fc),
                        "-map", f"[{last}]", "-map", "0:a",
                        "-c:v", "libx264", "-crf", "20", "-preset", "slow",
                        "-tune", "grain", "-c:a", "copy", "-pix_fmt", "yuv420p",
                        str(dst)], check=True)
        print(f"    {len(cues)} cues -> {dst.name}  "
              f"({dst.stat().st_size / 1048576:.1f} MB)")


if __name__ == "__main__":
    main()
