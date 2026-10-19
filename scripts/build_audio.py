#!/usr/bin/env python3
"""Stage 7 — lay the episode's audio bed.

Narration takes are placed against the scene timeline, then whatever layers
the episode declares are mixed under them. Everything that used to be a
constant in this file — scene boundaries, gaps, levels, which layers exist —
now lives in the episode's own audio.yaml, because record 01's constants were
record 01's, and the second episode had different scenes, a different room
tone and a runtime that moved after the narration was recorded.

Scene boundaries are never written down twice: they are summed from
shots.yaml, which is the only place a shot's duration is allowed to live.

Usage: build_audio.py [episode dir]
"""
import os, random, re, subprocess, sys, pathlib, yaml

print = __import__('functools').partial(print, flush=True)


def dur(p):
    return float(subprocess.run(
        ["/usr/local/opt/ffmpeg-full/bin/ffprobe", "-v", "error",
         "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(p)],
        capture_output=True, text=True).stdout)


def narration_paragraphs(script):
    """The narration, split into paragraphs, exactly as the voice says it.

    The canonical copy. There were three — here, in gen_narration.py and in
    build_captions.py — and they drifted: inline pause markers like *[2.5 s]*
    are directions to the assembly step and not words, and when that was
    found, two of the three copies were fixed. The third burned "*[2.5 s]*"
    into the captions of a finished vertical and shifted every word timing in
    that paragraph by four tenths of a second, because the alignment was asked
    for text the audio does not contain.

    One parser. Everything that needs paragraphs imports this.
    """
    order, paras = [], {}
    for sc, blk in enumerate(
            re.findall(r"\*\*Narration:\*\*\n+((?:>.*\n|\n(?=>))+)", script), 1):
        txt = re.sub(r"^> ?", "", blk, flags=re.M)
        txt = re.sub(r"\*\[[^\]]*\]\*", " ", txt)      # stage directions, not speech
        for i, para in enumerate([x.strip() for x in txt.split("\n\n") if x.strip()], 1):
            pid = f"s{sc}p{i}"
            order.append(pid); paras[pid] = " ".join(para.split())
    return order, paras


def scene_bounds(shots):
    """Where each scene starts and ends, summed from the shot list."""
    start, end, acc = {}, {}, 0
    for s in shots:
        sc = s["scene"]
        start.setdefault(sc, acc)
        acc += s["timeline_seconds"]
        end[sc] = acc
    return start, end


def card_anchors(ep, shots):
    """When each carded paragraph's card starts typing, in absolute seconds.

    A card is anchored to a plate and a line is anchored to a scene, and
    nothing connected the two: record 03 shipped a card fourteen seconds from
    its line and `with:` was added to *detect* that. This is the other half —
    the line waits for its card instead of drifting away from it.
    """
    f = ep / "cards.yaml"
    if not f.exists():
        return {}
    cards = (yaml.safe_load(f.read_text()) or {}).get("cards") or []
    at, acc = {}, 0
    for sh in shots:
        at[str(sh["id"])] = acc; acc += sh["timeline_seconds"]
    return {c["with"]: at[str(c["shot"])] + c.get("at", 0)
            for c in cards if c.get("with") and str(c.get("shot")) in at}


def place(picks, A, start, end, cfg, anchors=None):
    """Spread each scene's paragraphs across the scene rather than running them
    off the top. Front-loading leaves one long dead stretch at the end of every
    scene; spreading turns that into even, deliberate silences that track the
    images.

    A paragraph that owns a card never starts before that card does: the card
    is the instrument arriving, the line is the operator reading it, and the
    beat only exists when they land together. A card that sits *later* than its
    line cannot be fixed here — that is a shot order problem and validate.py
    says so."""
    lead, tail, min_gap = cfg["lead_in"], cfg["tail"], cfg["min_gap"]
    hold = cfg.get("hold") or {}
    anchors = anchors or {}
    by_scene = {}
    for pid, seed in picks.items():
        by_scene.setdefault(int(pid[1]), []).append(
            (pid, A / "narration" / f"{pid}_s{seed}.mp3"))

    placed = []
    for scene in sorted(by_scene):
        items = sorted(by_scene[scene], key=lambda x: int(x[0].split("p")[1]))
        # The gap is recomputed after every paragraph against what is left of
        # the scene, rather than once against the whole of it. With a fixed
        # gap, a paragraph that waits for its card pushes every later gap past
        # the end of the scene — the last line of scene 3 landed a second on
        # top of the first line of scene 4, two voices at once. Recomputing
        # spends the remaining time on the paragraphs that are still to come.
        t = start[scene] + lead
        gap = min_gap
        prev_end = None
        for idx, (pid, f) in enumerate(items):
            t += hold.get(pid, 0)
            if pid in anchors and anchors[pid] > t:
                t = anchors[pid]          # wait for the card to reach the screen
            # And the other direction, opt-in per episode. Spreading the scene
            # evenly pushed record 07's lines four to ten seconds past cards
            # that were timed for them, so a carded line is pulled back to
            # `card_pull` seconds after its card — never closer than min_gap
            # to the line before it, and never ahead of its card. Off unless
            # audio.yaml asks: records 04-06 were mixed without it, and this
            # function is also what validate.py checks them against.
            pull = cfg.get("card_pull")
            if pull is not None and pid in anchors and t > anchors[pid] + pull:
                floor = (prev_end + min_gap) if prev_end is not None else start[scene] + lead
                t = max(floor, anchors[pid] + pull, anchors[pid])
            placed.append((pid, f, t))
            t += dur(f)
            prev_end = t
            rest = items[idx + 1:]
            if rest:
                rem = sum(dur(f2) for _, f2 in rest)
                rem_holds = sum(hold.get(p2, 0) for p2, _ in rest)
                gap = max(min_gap,
                          (end[scene] - tail - t - rem - rem_holds) / len(rest))
                t += gap
        last = t
        print(f"  scene {scene}: {len(items)} paragraphs, gap {gap:4.1f}s, "
              f"ends {last:6.1f}s of {end[scene]}s"
              f"{'   OVERRUN' if last > end[scene] else ''}")
    return placed


# --- channel sound furniture (config/sound.yaml), from record 08 -------------
#
# One copy. build_verticals.py and build_teaser.py import these, for the same
# reason the paragraph parser lives here: a floor or a duck written twice is a
# floor or a duck that drifts.

def sound_spec():
    return yaml.safe_load(pathlib.Path("config/sound.yaml").read_text())


def ensure_floor(ep, ff=None):
    """The synthesised floor, rendered once into audio/sfx/floor.wav.

    Seeded, so it is byte-identical between builds and between records. It
    replaces the generated room beds of records 01-07, whose energy sat above
    3 kHz and read on YouTube as whine rather than as a room."""
    ff = ff or os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    f = ep / "audio" / "sfx" / "floor.wav"
    if f.exists():
        return f
    fl = sound_spec()["floor"]
    f.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([ff, "-y", "-v", "error", "-f", "lavfi", "-i",
                    f"anoisesrc=color={fl['color']}:amplitude=1:seed={fl['seed']}:"
                    f"d={fl['seconds']}:r=44100",
                    "-af", f"highpass=f={fl['highpass']},lowpass=f={fl['lowpass']},"
                           f"volume={fl['gain_db']}dB",
                    "-ac", "2", "-c:a", "pcm_s16le", str(f)], check=True)
    print(f"  floor: rendered {f}")
    return f


def duck_filter(spans, depth=None):
    """A volume filter: 0 dB in the silences, -depth dB under every span.

    `spans` are (start, end) of speech in the piece's own clock. Spans closer
    together than the ramps and margins merge — the cue stays down across an
    ordinary gap between paragraphs and only comes back in a real pause."""
    d = sound_spec()["duck"]
    depth = d["db"] if depth is None else depth
    r, pre, post = d["ramp"], d["pre"], d["post"]
    if not spans:
        return "anull"
    # Single-quoted, so the commas belong to the expression, not the graph.
    terms = [f"clip(min((t-({a - pre - r:.3f}))/{r},({b + post + r:.3f}-t)/{r}),0,1)"
             for a, b in spans]
    return f"volume='pow(10,-{depth}*clip({'+'.join(terms)},0,1)/20)':eval=frame"


def music_head():
    """What goes in front of a ducked cue: a high-pass for rumble only."""
    return f"highpass=f={sound_spec()['music']['highpass']}"


def event_times(cfg, shots, ep):
    """[(event, start, seconds, file)] for audio.yaml's `events:`.

    A spot effect is anchored to a shot and an offset inside it, the same way
    a card is, so a retimed shot list moves its sounds with it. Seconds are
    the event's own `seconds:`, else the whole file, never past the cap."""
    cap = sound_spec()["events"]["max_seconds"]
    at, acc = {}, 0
    for sh in shots:
        at[str(sh["id"])] = acc; acc += sh["timeline_seconds"]
    out = []
    for e in cfg.get("events") or []:
        f = ep / "audio" / (cfg.get("sfx") or {})[e["sfx"]]["file"]
        sec = float(e.get("seconds") or (dur(f) if f.exists() else cap))
        out.append((e, at[str(e["shot"])] + float(e.get("at", 0)), min(sec, cap), f))
    return out


def main():
    args = sys.argv[1:]
    # The verticals carry no cards, so they must not carry the sound of cards
    # typing — a click with nothing on screen is a fault, not a signature.
    no_clicks = "--no-clicks" in args
    if no_clicks:
        args.remove("--no-clicks")
    ep = pathlib.Path(args[0] if args else "episodes/ep-02-sunrise-line")
    ff = os.environ.get("FFMPEG_BIN", "/usr/local/opt/ffmpeg-full/bin/ffmpeg")
    A = ep / "audio"
    cfg = yaml.safe_load((ep / "audio.yaml").read_text())
    shots = yaml.safe_load((ep / "shots.yaml").read_text())["shots"]
    picks = yaml.safe_load((A / "narration.yaml").read_text())["picks"]
    start, end = scene_bounds(shots)
    total = cfg["runtime_seconds"]

    placed = place(picks, A, start, end, cfg, card_anchors(ep, shots))
    print(f"  narration ends at {max(t + dur(f) for _, f, t in placed):.1f}s "
          f"of {total}s")

    ins, fc, idx = [], [], 0

    def add(path):
        nonlocal idx
        ins.extend(["-i", str(path)]); idx += 1; return idx - 1

    levels = cfg.get("levels") or {}
    mixed = []

    for name, layer in (cfg.get("layers") or {}).items():
        if name == "relay":
            continue                      # placed as clicks, below
        # From record 08 the floor is synthesised, not generated: see
        # config/sound.yaml for why the old room beds came out of the mix.
        f = ensure_floor(ep, ff) if layer.get("synth") == "floor" else A / layer["file"]
        if not f.exists():
            print(f"  layer {name}: missing {f} — skipped")
            continue
        i = add(f)
        chain = [f"[{i}:a]"]
        if layer.get("trim"):
            a, b = layer["trim"]
            chain.append(f"atrim={a}:{b},asetpts=N/SR/TB,")
        if layer.get("loop_to_fill") or layer.get("synth") == "floor":
            # A 22-second bed under a 279-second record. aloop works in
            # samples, so the clip is looped past the runtime and trimmed
            # back — the seam is inaudible on a bed with no events in it,
            # which is exactly why room tone is generated eventless.
            chain.append(f"aloop=loop=-1:size=2e+09,")
        if layer.get("loop_crossfade"):
            # A generated bed fades itself at both ends, which strips the room
            # tone out of the close. Only the stable middle is used, looped
            # over itself, so the one fade in the mix is the one we ask for.
            fc.append("".join(chain) + f"asplit=2[{name}1][{name}2]")
            fc.append(f"[{name}1][{name}2]"
                      f"acrossfade=d={layer['loop_crossfade']}:c1=tri:c2=tri[{name}L]")
            chain = [f"[{name}L]"]
        if layer.get("filter"):
            # An episode-level EQ for a bed, written into audio.yaml so the
            # step lives in the repository. Record 06's generated beds put
            # nearly all their energy under 150 Hz, where a phone or a laptop
            # plays almost nothing, and the first draft read as voice and
            # clicks alone. A level is then a trim on what is audible.
            chain.append(f"{layer['filter']},")
        if layer.get("duck"):
            # The record's music cue, from record 08: under the whole record,
            # down by config/sound.yaml's duck wherever the voice is speaking.
            chain.append(f"{music_head()},")
        chain.append(f"volume={levels.get(name, -20)}dB,")
        if layer.get("duck"):
            spans = [(t, t + dur(pf)) for _, pf, t in placed]
            chain.append(f"{duck_filter(spans)},")
        if layer.get("delay"):
            d = int(layer["delay"] * 1000)
            chain.append(f"adelay={d}|{d},")
        # The window where this layer is deliberately absent. It belongs to the
        # layer, not to the episode: this read `name == "hum"` — record 03's
        # layer name, hard-coded — so record 04's pump was never gated at all.
        # The scene it is supposed to vanish from measured 0.25 dB quieter than
        # the scene before it, which is what a sound-design decision looks like
        # when it silently does not happen. The top-level key still works for
        # record 03, which is frozen and must keep building.
        s0 = layer.get("silence_at") or (cfg.get("silence_at")
                                         if name == "hum" else None)
        if s0:
            chain.append(f"volume='if(between(t,{s0[0]},{s0[0] + s0[1]}),0,1)':"
                         f"eval=frame,")
        if layer.get("fade_out"):
            st, d = layer["fade_out"]
            chain.append(f"afade=t=out:st={st}:d={d},")
        chain.append(f"apad,atrim=0:{total}[{name}]")
        fc.append("".join(chain))
        mixed.append(f"[{name}]")

    # Spot effects, from record 08: a handful of short natural sounds — ice
    # settling, a drip, a latch — placed in the pauses, not a bed under the
    # whole record. Band-limited so nothing reaches the whine the old beds
    # lived in, with a fade long enough at the tail that no event is cut off.
    ev_spec = sound_spec().get("events") or {}
    for n, (e, t, sec, f) in enumerate(event_times(cfg, shots, ep)):
        if not f.exists():
            print(f"  event {e['sfx']} at {t:.1f}s: missing {f} — skipped")
            continue
        i = add(f)
        d = int(t * 1000)
        fo = min(ev_spec["fade_out"], sec / 2)
        fc.append(f"[{i}:a]atrim={float(e.get('from', 0))}:"
                  f"{float(e.get('from', 0)) + sec},asetpts=N/SR/TB,"
                  f"highpass=f={ev_spec['highpass']},lowpass=f={ev_spec['lowpass']},"
                  f"afade=t=in:d={ev_spec['fade_in']},"
                  f"afade=t=out:st={sec - fo:.3f}:d={fo:.3f},"
                  f"volume={float(e.get('level', 0)) + levels.get('events', 0)}dB,"
                  f"adelay={d}|{d},apad,atrim=0:{total}[ev{n}]")
        mixed.append(f"[ev{n}]")
        print(f"  event {e['sfx']:<10} {t:6.1f}s  {sec:4.1f}s")

    # Uneven on purpose, so it never reads as a metronome. One input, split
    # into as many copies as there are clicks — a filter input cannot be
    # consumed twice.
    relay, rl = cfg.get("relay"), (cfg.get("layers") or {}).get("relay")
    if relay and rl and (A / rl["file"]).exists():
        random.seed(relay.get("seed", 11))
        times, t = [], relay["from"]
        while t < relay["until"]:
            times.append(t); t += random.uniform(*relay["every"])
        i = add(A / rl["file"])
        fc.append(f"[{i}:a]asplit={len(times)}" +
                  "".join(f"[rs{n}]" for n in range(len(times))))
        for n, c in enumerate(times):
            d = int(c * 1000)
            fc.append(f"[rs{n}]volume={levels.get('relay', -22)}dB,"
                      f"adelay={d}|{d},apad,atrim=0:{total}[rc{n}]")
            mixed.append(f"[rc{n}]")
        print(f"  relay: {len(times)} clicks")

    if not no_clicks and cfg.get("clicks_bed") and (ep / cfg["clicks_bed"]).exists():
        i = add(ep / cfg["clicks_bed"])
        fc.append(f"[{i}:a]volume={levels.get('clicks', 0)}dB,apad,"
                  f"atrim=0:{total}[clicks]")
        mixed.append("[clicks]")

    for pid, f, t in placed:
        i = add(f)
        d = int(t * 1000)
        fc.append(f"[{i}:a]adelay={d}|{d},apad,atrim=0:{total}[n{i}]")
        mixed.append(f"[n{i}]")

    fc.append("".join(mixed) +
              f"amix=inputs={len(mixed)}:normalize=0:dropout_transition=0,"
              f"alimiter=limit=0.95,aformat=sample_rates=44100:"
              f"channel_layouts=stereo[out]")

    out = A / ("episode-mix-noclicks.mp3" if no_clicks else "episode-mix.mp3")
    subprocess.run([ff, "-y", "-v", "error", *ins,
                    "-filter_complex", ";".join(fc), "-map", "[out]",
                    "-c:a", "libmp3lame", "-b:a", "192k", str(out)], check=True)
    print(f"\n  {len(placed)} paragraphs mixed")
    print(f"  {out}  {dur(out):.2f}s")


if __name__ == "__main__":
    main()
