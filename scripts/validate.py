#!/usr/bin/env python3
"""Run the Validation Before Generation checks from CLAUDE.md against an
episode. Text is cheap, credits are not — this runs before anything spends."""
import sys, re, pathlib, yaml

SCENE_RUNTIME = {1: 22, 2: 43, 3: 45, 4: 55, 5: 65, 6: 20}

def main(ep):
    ep = pathlib.Path(ep)
    cfg = yaml.safe_load((pathlib.Path("config/models.yaml")).read_text())
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    script = (ep / "script.md").read_text()
    shots, fail = doc["shots"], []

    # 1. timeline_seconds sums to the runtime, per scene and overall.
    per = {}
    for s in shots:
        per.setdefault(s["scene"], 0)
        per[s["scene"]] += s["timeline_seconds"]
    for sc, want in SCENE_RUNTIME.items():
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
        if s.get("source") == "ffmpeg":
            if "generate_seconds" in s:
                fail.append(f"{s['id']}: source ffmpeg but has generate_seconds")
        elif "model" not in s:
            fail.append(f"{s['id']}: no model")

    # 3. No shot exceeds its tier's clip limits.
    for s in shots:
        if s.get("source") == "ffmpeg": continue
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
        if not r and s.get("source") != "ffmpeg":
            if s["timeline_seconds"] > s["generate_seconds"]:
                fail.append(f"{s['id']}: timeline longer than generated, no retime declared")

    # 5. Narration leaves at least a third of the runtime as silence.
    blocks = re.findall(r"\*\*Narration:\*\*\n((?:>.*\n)+)", script)
    words = sum(len(re.sub(r"^> ?", "", b, flags=re.M).split()) for b in blocks)
    WPM = 162   # measured, see config/voice.yaml
    speech = words / WPM * 60
    share = speech / doc["runtime_seconds"]
    print(f"\n  narration: {words} words, {speech:.0f} s at {WPM} wpm = "
          f"{share*100:.0f}% of runtime  {'ok' if share <= 2/3 else 'FAIL'}")
    if share > 2/3: fail.append(f"speech is {share*100:.0f}% of runtime")

    # 6. Prompt hygiene — the rules that cost credits when broken.
    ALLOWED_NOISE = {"5.2", "5.3"}
    for s in shots:
        p = s["prompt"].lower()
        if re.search(r"film grain|grain texture|scanline", p):
            fail.append(f"{s['id']}: degradation in prompt")
        if "grainy" in p and s["id"] not in ALLOWED_NOISE:
            fail.append(f"{s['id']}: grain in prompt")
        if re.search(r"\bhand\b", p) and s["id"] != "5.1":
            fail.append(f"{s['id']}: unexpected hand")

    print()
    if fail:
        print("FAILED:"); [print("  -", f) for f in fail]; return 1
    print("All checks passed."); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9"))
