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

    # 5. Narration leaves at least a third of the runtime as silence.
    blocks = re.findall(r"\*\*Narration:\*\*\n+((?:>.*\n|\n(?=>))+)", script)
    words = sum(len(re.sub(r"^> ?", "", b, flags=re.M).split()) for b in blocks)
    WPM = 162   # measured, see config/voice.yaml
    speech = words / WPM * 60
    share = speech / doc["runtime_seconds"]
    print(f"\n  narration: {words} words, {speech:.0f} s at {WPM} wpm = "
          f"{share*100:.0f}% of runtime  {'ok' if share <= 2/3 else 'FAIL'}")
    if share > 2/3: fail.append(f"speech is {share*100:.0f}% of runtime")

    # 5b. And it leaves a third per scene, not only overall. Record 2 was
    # submitted at 30% overall and 8% in scene 5 — the average hid a scene
    # with no room for the paragraph gaps it already needed.
    for m in re.finditer(r"^##+ +(?:SCENE +)?(\d+)\b.*?(?=^##+ |\Z)",
                         script, re.M | re.S):
        sc = int(m.group(1))
        if sc not in scene_runtime:
            continue
        b = re.findall(r"\*\*Narration:\*\*\n((?:>.*\n|\n(?=>))+)", m.group(0))
        w = sum(len(re.sub(r"^> ?", "", x, flags=re.M).split()) for x in b)
        sp = w / WPM * 60
        sil = (scene_runtime[sc] - sp) / scene_runtime[sc]
        waived = sc in (doc.get("silence_waiver") or {})
        ok = sil >= FLOOR or waived
        print(f"  scene {sc}: {w:4d} words, {sp:5.1f} s speech / "
              f"{scene_runtime[sc]:3d} s = {sil*100:4.0f}% silent  "
              f"{'ok' if sil >= FLOOR else 'waived' if waived else 'FAIL'}")
        if not ok:
            fail.append(f"scene {sc}: {sil*100:.0f}% silence, floor is 33%")

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

    print()
    if fail:
        print("FAILED:"); [print("  -", f) for f in fail]; return 1
    print("All checks passed."); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9"))
