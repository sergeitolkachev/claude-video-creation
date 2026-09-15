#!/usr/bin/env python3
"""Run the Validation Before Generation checks from CLAUDE.md against an
episode. Text is cheap, credits are not — this runs before anything spends."""
import sys, re, pathlib, yaml

# Record 1 carried its scene runtimes here, in the script. A second episode
# is where that stops working, so the numbers now live in the episode's own
# shots.yaml under scene_runtime; this is the fallback for record 1, which
# predates the key.
SCENE_RUNTIME_EP01 = {1: 22, 2: 43, 3: 45, 4: 55, 5: 65, 6: 20}

# Prompt-hygiene exceptions, per episode. Record 1 had these inline; they are
# episode facts, not pipeline facts. An episode may override either list in
# shots.yaml under hygiene:.
HYGIENE_EP01 = {"allow_grainy": ["5.2", "5.3"], "allow_hand": ["5.1"]}

WPM = 162   # measured, see config/voice.yaml
FLOOR = 1 / 3   # minimum share of runtime that stays silent, per CLAUDE.md
CEILING = 0.55  # above this an episode is dragging, per CLAUDE.md Runtime
# How far a card may sit from the line it answers to. Measured on record 3's
# working cards: -1.5 s to +3.8 s. A card may lead its line a little — it
# reads as the instrument getting there first — and may follow it by a few
# seconds. Fourteen seconds is what this exists to catch.
CARD_EARLY = 3.0
CARD_LATE  = 6.0
# A vertical is scrolled past, not started. The viewer decides inside the first
# second whether anything is here, so narration must be audible by then.
VERT_OPEN = 1.0
VERT_MAX_LINES = 2   # a caption block deeper than this eats the picture
# A word boundary is not the end of the sound. ElevenLabs marks a word as
# ending where the next one starts, and on this voice that can be 0.04 s later,
# so a cut placed just past the timestamp severs the word's decay. Record 03
# shipped two verticals that way and this file passed them, because it was
# reading the same timestamps. A cut needs real silence after it.
VERT_TAIL = 0.20

def dur_of(path):
    import subprocess
    return float(subprocess.run(
        ["/usr/local/opt/ffmpeg-full/bin/ffprobe", "-v", "error", "-show_entries",
         "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True).stdout or 0)


def narration_words(block):
    """Words the voice actually says.

    `.split()` counted a standalone em-dash as a word, and counted the
    inline pause markers (`*[2.5 s]*`) as two more each. Record 3 measured
    265 words against a real 260 — a 2% error in the direction that makes an
    episode look busier than it is, which is the wrong direction for a check
    whose whole job is to catch an episode with no room to breathe.
    """
    text = re.sub(r"^> ?", "", block, flags=re.M)
    text = re.sub(r"\*\[[^\]]*\]\*", " ", text)          # *[2.5 s]* stage directions
    return sum(1 for t in text.split() if re.search(r"[\w]", t))

def main(ep):
    ep = pathlib.Path(ep)
    cfg = yaml.safe_load((pathlib.Path("config/models.yaml")).read_text())
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    script = (ep / "script.md").read_text()
    shots, fail = doc["shots"], []
    scene_runtime = {int(k): v for k, v in
                     (doc.get("scene_runtime") or SCENE_RUNTIME_EP01).items()}
    hyg = {**HYGIENE_EP01, **(doc.get("hygiene") or {})}

    # 1. timeline_seconds sums to the runtime, per scene and overall.
    per = {}
    for s in shots:
        per.setdefault(s["scene"], 0)
        per[s["scene"]] += s["timeline_seconds"]
    for sc, want in scene_runtime.items():
        got = per.get(sc, 0)
        mark = "ok" if got == want else "FAIL"
        if got != want: fail.append(f"scene {sc}: {got}s vs {want}s")
        print(f"  scene {sc}: {got:3d} s / {want:3d} s  {mark}")
    total = sum(per.values())
    if total != doc["runtime_seconds"]:
        fail.append(f"total {total}s vs {doc['runtime_seconds']}s")
    print(f"  TOTAL:   {total} s / {doc['runtime_seconds']} s  "
          f"{'ok' if total == doc['runtime_seconds'] else 'FAIL'}")

    # 2. Every shot has a model, unless it is not generated at all.
    for s in shots:
        if s.get("source", "").startswith("ffmpeg"):
            if "generate_seconds" in s:
                fail.append(f"{s['id']}: {s['source']} but has generate_seconds")
        elif "model" not in s:
            fail.append(f"{s['id']}: no model")

    # 3. Every ffmpeg_still shot must have the approved still it is built from.
    # Before selection has run there is nothing to check yet — this is a stage
    # 6 gate, and failing it at stage 2 would mean the shot list can never be
    # validated on the day it is written.
    locked = [s for s in shots if s.get("source") == "ffmpeg_still"]
    missing = [s["id"] for s in locked
               if not (ep / "approved" / f"{s['id']}.jpg").exists()]
    if missing:
        # Selection is a human step that runs over days; an incomplete
        # approved/ is the normal state of an episode in stage 4, not a
        # failure. build_static.py is the gate that actually needs the file.
        print(f"\n  plates: {len(locked) - len(missing)} / {len(locked)} "
              f"approved — {len(missing)} still to pick")
    else:
        print(f"\n  plates: {len(locked)} / {len(locked)} approved  ok")

    # 4. No shot exceeds its tier's clip limits.
    for s in shots:
        if s.get("source", "").startswith("ffmpeg"): continue
        tier = cfg["video"][s["model"]]
        g, d = s["generate_seconds"], tier["duration_seconds"]
        if tier.get("has_seed") is False or s["model"] == "workhorse":
            if g not in d:
                fail.append(f"{s['id']}: {g}s not in allowed {d} for {s['model']}")
        elif not (d[0] <= g <= d[1]):
            fail.append(f"{s['id']}: {g}s outside range {d} for {s['model']}")

    # 4. Retiming stays under 1.3x.
    for s in shots:
        r = s.get("retime")
        if r and r > 1.3: fail.append(f"{s['id']}: retime {r} exceeds 1.3x")
        if r and abs(s["timeline_seconds"] / s["generate_seconds"] - r) > 0.01:
            fail.append(f"{s['id']}: retime {r} disagrees with the durations")
        if not r and not s.get("source", "").startswith("ffmpeg"):
            if s["timeline_seconds"] > s["generate_seconds"]:
                fail.append(f"{s['id']}: timeline longer than generated, no retime declared")

    # 4c. Motion policy, per CLAUDE.md. A still frame is allowed only where
    # the viewer is reading something.
    TIERS = {"static", "local", "model"}
    for s in shots:
        tier = s.get("motion_tier")
        if tier not in TIERS:
            fail.append(f"{s['id']}: motion_tier missing or unknown ({tier})")
            continue
        if tier == "static" and not s.get("card") and not s.get("static_exception"):
            fail.append(f"{s['id']}: static with no card and no static_exception")
        if tier == "model" and "model" not in s:
            fail.append(f"{s['id']}: motion_tier model but no model tier named")
        if tier == "local" and not s.get("source", "").startswith("ffmpeg"):
            fail.append(f"{s['id']}: motion_tier local but not built locally")
    n = {t: sum(1 for s in shots if s.get("motion_tier") == t) for t in TIERS}
    moving = n["model"] + n["local"]
    print(f"\n  motion: {n['model']} model, {n['local']} local, {n['static']} static "
          f"— {moving * 100 // len(shots)}% of shots move")

    # 5. Narration leaves at least a third of the runtime as silence.
    blocks = re.findall(r"\*\*Narration:\*\*\n+((?:>.*\n|\n(?=>))+)", script)
    words = sum(narration_words(b) for b in blocks)
    WPM = 162   # measured, see config/voice.yaml
    speech = words / WPM * 60
    share = speech / doc["runtime_seconds"]
    print(f"\n  narration: {words} words, {speech:.0f} s at {WPM} wpm = "
          f"{share*100:.0f}% of runtime  {'ok' if share <= 2/3 else 'FAIL'}")
    if share > 2/3: fail.append(f"speech is {share*100:.0f}% of runtime")

    # 5b. And it leaves a third per scene, not only overall. Record 2 was
    # submitted at 30% overall and 8% in scene 5 — the average hid a scene
    # with no room for the paragraph gaps it already needed.
    body = []
    for m in re.finditer(r"^##+ +(?:SCENE +)?(\d+)\b.*?(?=^##+ |\Z)",
                         script, re.M | re.S):
        sc = int(m.group(1))
        if sc not in scene_runtime:
            continue
        b = re.findall(r"\*\*Narration:\*\*\n((?:>.*\n|\n(?=>))+)", m.group(0))
        w = sum(narration_words(x) for x in b)
        sp = w / WPM * 60
        sil = (scene_runtime[sc] - sp) / scene_runtime[sc]
        coda = sc in (doc.get("coda") or [])
        body.append((sc, w, scene_runtime[sc])) if not coda else None
        waived = sc in (doc.get("silence_waiver") or {})
        ok = sil >= FLOOR or waived
        print(f"  scene {sc}: {w:4d} words, {sp:5.1f} s speech / "
              f"{scene_runtime[sc]:3d} s = {sil*100:4.0f}% silent  "
              f"{'coda' if coda else 'ok' if sil >= FLOOR else 'waived' if waived else 'FAIL'}")
        if not ok and not coda:
            fail.append(f"scene {sc}: {sil*100:.0f}% silence, floor is 33%")

    # 5c. And the ceiling. Silence is the format; dead air is not the same
    # thing. Record 3 was submitted at 60% — half a minute of it on frozen
    # frames, which under the Motion Policy is also the most expensive kind of
    # second there is. Scenes listed under `coda:` are exempt by declaration:
    # a closing card block and a held silent shot are not dead air.
    if body:
        bw = sum(w for _, w, _ in body)
        bs = sum(sec for _, _, sec in body)
        sil = (bs - bw / WPM * 60) / bs
        tag = " (excluding coda)" if len(body) < len(scene_runtime) else ""
        print(f"\n  body{tag}: {bw} words / {bs} s = {sil*100:.0f}% silent  "
              f"{'ok' if sil <= CEILING else 'FAIL'}")
        if sil > CEILING:
            fail.append(f"body is {sil*100:.0f}% silent, ceiling is {CEILING*100:.0f}%")

    # 6. Prompt hygiene — the rules that cost credits when broken.
    for s in shots:
        p = s["prompt"].lower()
        if re.search(r"film grain|grain texture|scanline", p):
            fail.append(f"{s['id']}: degradation in prompt")
        if "grainy" in p and s["id"] not in hyg["allow_grainy"]:
            fail.append(f"{s['id']}: grain in prompt")
        if re.search(r"\bhand\b", p) and s["id"] not in hyg["allow_hand"]:
            fail.append(f"{s['id']}: unexpected hand")

    for rule in (doc.get("hygiene") or {}).get("forbid", []):
        pat, allowed = rule["pattern"], set(rule.get("except", []))
        for s in shots:
            body = " ".join(str(s.get(k, "")) for k in ("prompt", "video_prompt"))
            if re.search(pat, body, re.I) and s["id"] not in allowed:
                fail.append(f"{s['id']}: matches forbidden /{pat}/ ({rule.get('why','')})")

    # 7. A card lands with the line it answers to.
    #
    # Record 3 shipped a master where the card reading LOG 114 typed 14 s after
    # the voice said "Log one fourteen". Nothing was wrong with either file:
    # the card was correctly placed on its plate and the line was correctly
    # placed in its scene, and no check looked at both. A card names its
    # paragraph with `with:` and this measures the gap.
    #
    # It needs the narration picks, so before stage 7 it reports and passes.
    # Narration placement, computed once. It was computed inside the card
    # check and reused by the vertical check, which meant an episode with no
    # `with:` fields skipped the card block, left the timeline empty, and was
    # told every one of its verticals opens on silence. Record 02 was failed by
    # that and record 02 is fine. A value two checks depend on is not a local
    # of the first one.
    at_full, at = [], {}
    picks_f = ep / "audio" / "narration.yaml"
    if picks_f.exists() and (ep / "audio.yaml").exists():
        sys.path.insert(0, str(pathlib.Path(__file__).parent))
        from build_audio import place, scene_bounds
        acfg = yaml.safe_load((ep / "audio.yaml").read_text())
        pk = yaml.safe_load(picks_f.read_text())["picks"]
        st, en = scene_bounds(shots)
        at_full = place(pk, ep / "audio", st, en, acfg)
        at = {pid: t for pid, _, t in at_full}

    cards_f = ep / "cards.yaml"
    if cards_f.exists():
        cards = (yaml.safe_load(cards_f.read_text()) or {}).get("cards") or []
        want = [c for c in cards if c.get("with")]
        if not want:
            pass
        elif not at_full:
            print(f"\n  card sync: {len(want)} cards declare a line — "
                  f"needs narration.yaml, checked at stage 7")
        else:
            shot_start, acc = {}, 0
            for sh in shots:
                shot_start[sh["id"]] = acc; acc += sh["timeline_seconds"]
            print()
            for c in want:
                t_card = shot_start.get(c["shot"], 0) + c.get("at", 0)
                t_line = at.get(c["with"])
                if t_line is None:
                    fail.append(f"card {c['id']}: no paragraph {c['with']}"); continue
                d = t_card - t_line
                ok = -CARD_EARLY <= d <= CARD_LATE
                print(f"  card {c['id']:<12} {t_card:6.1f}s vs {c['with']} "
                      f"{t_line:6.1f}s  = {d:+5.1f}s  {'ok' if ok else 'FAIL'}")
                if not ok:
                    fail.append(f"card {c['id']}: {d:+.1f}s from {c['with']}, "
                                f"allowed -{CARD_EARLY} to +{CARD_LATE}")

    # 8b. Stage directions are not speech. They are stripped by one shared
    # parser now, but the check is two lines and the fault it catches — a
    # marker burned into a caption and every word timing in that paragraph
    # shifted — cost a finished set of verticals.
    for pid, text in (locals().get("_paras") or {}).items():
        if "*[" in text:
            fail.append(f"{pid}: stage direction left in narration text")

    # 8. The verticals: they open on a voice, and their captions clear the
    # platform furniture. Both are channel rules and both are decidable here,
    # before anything is rendered.
    vf = ep / "verticals.yaml"
    if vf.exists() and at_full:
        vcfg = yaml.safe_load(vf.read_text())
        tspec = yaml.safe_load(pathlib.Path("config/type.yaml").read_text())
        cap = tspec["captions"]
        H, W = 1920, 1080
        clear = H * cap["bottom_clear"]
        block = cap["line_height"] * VERT_MAX_LINES
        top = H - clear - block
        print()
        print(f"  captions: {VERT_MAX_LINES} lines of {cap['line_height']}px grow up "
              f"from {clear:.0f}px clear — block sits {top:.0f}-{H - clear:.0f}px of {H}")
        if cap["safe_width"] > W:
            fail.append(f"captions.safe_width {cap['safe_width']} exceeds the {W}px frame")
        if top < H * 0.25:
            fail.append(f"a {VERT_MAX_LINES}-line caption reaches {top:.0f}px, "
                        f"into the upper quarter of the frame")
        # a cut may stop mid-sentence; it may not stop mid-word. Record 3
        # shipped three verticals severed inside a word — "I am not produc—" —
        # which reads as a broken file and not as a withheld ending.
        align = ep / "audio" / "alignment"
        pk_seed = yaml.safe_load(picks_f.read_text())["picks"]
        import json as _json
        words = []
        for pid, _f, t0 in at_full:
            j = align / f"{pid}_s{pk_seed[pid]}.json"
            if j.exists():
                words += [(t0 + w["t"], t0 + w["e"], w["w"])
                          for w in _json.loads(j.read_text())]
        for c in vcfg.get("cuts", []):
            t1 = float(c["to"])
            # No tolerance. A 0.02 s margin was tried and it passed a cut that
            # clipped the last 20 ms off "open" — a tolerance of the same order
            # as the error it is meant to catch is not a check.
            inside = [w for a_, b_, w in words if a_ < t1 < b_]
            if inside:
                print(f"  {c['id']:<22} ends at {t1:7.1f}s  inside \"{inside[0]}\"  FAIL")
                fail.append(f"{c['id']}: `to: {t1}` falls inside the word "
                            f"\"{inside[0]}\" — cut between words")
            elif words:
                before = [(b_, w) for a_, b_, w in words if b_ <= t1]
                last_e, last = before[-1] if before else (0, "?")
                after = [a_ for a_, _, _ in words if a_ > t1]
                # silence available at the cut: to the next word, or to the end
                gap = (min(after) - last_e) if after else 99.0
                ok = gap >= VERT_TAIL
                print(f"  {c['id']:<22} ends at {t1:7.1f}s  after \"{last}\"  "
                      f"silence {gap:4.2f}s  {'ok' if ok else 'FAIL'}")
                if not ok:
                    fail.append(f"{c['id']}: only {gap:.2f}s of silence after "
                                f"\"{last}\" — needs {VERT_TAIL}s, or the word "
                                f"is heard being cut")

        # narration has to be running inside the first second of every cut
        spans = [(t, t + dur_of(f)) for _, f, t in at_full]
        for c in vcfg.get("cuts", []):
            t0 = float(c["from"])
            live = [s_ for s_, e_ in spans if s_ < t0 + VERT_OPEN and e_ > t0]
            if live:
                d = max(0.0, min(s_ for s_ in live) - t0)
                print(f"  {c['id']:<22} opens at {t0:7.1f}s  voice in {d:4.1f}s  ok")
            else:
                nxt = min((s_ for s_, _ in spans if s_ >= t0), default=None)
                gap = f"{nxt - t0:.1f}s" if nxt else "never"
                print(f"  {c['id']:<22} opens at {t0:7.1f}s  voice in {gap:>5}  FAIL")
                fail.append(f"{c['id']}: no narration inside the first "
                            f"{VERT_OPEN}s — first voice {gap} in")

    # 9. Thumbnails: a text block may not land in the slug's band.
    #
    # The slug is drawn last, at H - 26*2.6, with a darkened box around it. A
    # block placed under that reads as a smear at the 210 px YouTube actually
    # renders — which is the only size that decides anything, and the size
    # nobody looks at while building a 1280 px plate.
    tf = ep / "thumbnails.yaml"
    if tf.exists():
        tdoc = yaml.safe_load(tf.read_text())
        TH = tdoc["export"]["height"]
        slug_top = TH - 26 * 2.6 - 18          # the darkened box, not the type
        print()
        for v in tdoc.get("variants", []):
            for b in v.get("blocks", []):
                top = b["y"] * TH
                bot = top + int(b["size"] * 1.28) * len(b["lines"])
                ok = bot <= slug_top
                print(f"  thumb {v['id']:<14} block ends {bot:5.0f}px  "
                      f"slug band from {slug_top:.0f}px  {'ok' if ok else 'FAIL'}")
                if not ok:
                    fail.append(f"thumbnail {v['id']}: a block reaches {bot:.0f}px, "
                                f"into the slug band at {slug_top:.0f}px")

    print()
    if fail:
        print("FAILED:"); [print("  -", f) for f in fail]; return 1
    print("All checks passed."); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9"))
