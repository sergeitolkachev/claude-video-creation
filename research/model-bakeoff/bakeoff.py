#!/usr/bin/env python3
"""One-off bake-off: three shots Kling 2.5 Turbo failed, rolled on three
candidate models from the same approved still and the same prompt.

Not a pipeline script — a measurement. Takes land in takes/, findings in
README.md next to this file.

Usage: bakeoff.py [--dry-run] [--only A] [--model veo31fast]
"""
import sys, json, time, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import os; os.chdir(ROOT)
from gen_takes import env, req, fetch_ranges   # noqa: E402

print = __import__('functools').partial(print, flush=True)
HERE = pathlib.Path(__file__).resolve().parent
PENDING = HERE / "pending.json"

LOCK = ("The camera is locked off on a tripod and does not move at all: no "
        "dolly, no push in, no pull back, no pan, no tilt, no zoom. No cuts.")
NEG = ("camera movement, dolly, zoom, pan, handheld shake, morphing, objects "
       "changing shape, people, hands, faces, text, lettering, watermark")

SHOTS = {
    # ep-08 1.1 — Kling came back still: a film of water has no edge.
    "A": dict(src="ep-08-the-rind", file="1.1.jpg",
              prompt="Meltwater runs down the left wall of the ice bore: a thin "
                     "glistening film with small beads and rivulets sliding "
                     "steadily downward for the whole shot, catching the light "
                     "as they move. The ice itself is rigid and keeps exactly "
                     "its shape. " + LOCK,
              neg=NEG + ", ice melting away, ice reshaping"),
    # ep-08 4.1 — Kling slid the whole core 59 px along the bench and back.
    "C": dict(src="ep-08-the-rind", file="4.1.jpg",
              prompt="Meltwater tracks slowly down the side of the ice core "
                     "and drips off its lower edge onto the steel bench, one "
                     "drop at a time, and the small pool on the steel spreads "
                     "a little. The ice core does not move, slide or change "
                     "shape. " + LOCK,
              neg=NEG + ", the core sliding, the core rolling, ice reshaping"),
    # ep-05 1.3 — Kling stretched the strap into a festoon and moved it to
    # another hook on every roll.
    "B": dict(src="ep-05-gallery-three", file="1.3.jpg",
              prompt="The loose fabric strap hanging beside the empty suit "
                     "sways slowly from side to side in a faint draft, as one "
                     "piece, staying the same length and on the same hook for "
                     "the whole shot. The suit itself does not move and "
                     "nothing moves inside it. " + LOCK,
              neg=NEG + ", person, body filling the suit, head, helmet "
                        "turning, the strap lengthening, the strap moving to "
                        "another hook, the strap draping between hooks"),
}

MODELS = {
    "veo31fast": dict(id="fal-ai/veo3.1/fast/image-to-video", seconds=8, per_s=0.10,
                      body=lambda s, img: {"image_url": img, "prompt": s["prompt"],
                                           "negative_prompt": s["neg"], "duration": "8s",
                                           "resolution": "1080p", "aspect_ratio": "16:9",
                                           "generate_audio": False, "seed": 11}),
    "kling3pro": dict(id="fal-ai/kling-video/v3/pro/image-to-video", seconds=10, per_s=0.112,
                      body=lambda s, img: {"start_image_url": img, "prompt": s["prompt"],
                                           "negative_prompt": s["neg"], "duration": "10",
                                           "generate_audio": False}),
    # 720p is the ceiling on the fast tier; 1080p standard is $0.682/s.
    "seedance2fast": dict(id="bytedance/seedance-2.0/fast/image-to-video", seconds=5, per_s=0.2419,
                          body=lambda s, img: {"image_url": img, "prompt": s["prompt"],
                                               "duration": "5", "resolution": "720p",
                                               "aspect_ratio": "16:9", "generate_audio": False}),
}


def main():
    dry = "--dry-run" in sys.argv
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    mo = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else None
    env(); key = os.environ["FAL_API_KEY"]
    (HERE / "takes").mkdir(exist_ok=True)
    pend = json.loads(PENDING.read_text()) if PENDING.exists() else {}
    jobs, total = [], 0.0
    for sid, s in SHOTS.items():
        if only and sid != only: continue
        img = json.loads((ROOT / "episodes" / s["src"] / "approved" / "urls.json").read_text())[s["file"]]
        for mid, m in MODELS.items():
            if mo and mid != mo: continue
            dest = HERE / "takes" / f"{sid}-{mid}.mp4"
            price = m["seconds"] * m["per_s"]
            if dest.exists():
                print(f"  have {dest.name}"); continue
            body = m["body"](s, img)
            if dry:
                print(f"\n---- {sid} {mid}  {m['seconds']}s  ${price:.2f}\n  endpoint: {m['id']}")
                for k, v in body.items(): print(f"  {k}: {v}")
                total += price; continue
            k = f"{sid}-{mid}"
            if k not in pend:
                r = req(f"https://queue.fal.run/{m['id']}", key, body)
                pend[k] = {"status_url": r["status_url"], "response_url": r["response_url"],
                           "price": price, "request_id": r.get("request_id")}
                PENDING.write_text(json.dumps(pend, indent=2))
                print(f"  queued {k}  ${price:.2f}  id={r.get('request_id')}")
            total += price
            jobs.append((k, dest))
    print(f"\n{'DRY RUN — ' if dry else ''}{len(jobs) if not dry else ''} total ${total:.2f}")
    if dry: return
    t0 = time.time()
    while jobs and time.time() - t0 < 1800:
        for k, dest in list(jobs):
            try:
                st = req(pend[k]["status_url"], key)
            except Exception as e:
                print(f"  {k}: poll error {e}, retrying"); continue
            if st.get("status") == "COMPLETED":
                try:
                    out = req(pend[k]["response_url"], key)
                except urllib.error.HTTPError as e:
                    print(f"  {k}: FAILED {e.code} {e.read()[:300]}"); jobs.remove((k, dest)); continue
                url = out["video"]["url"]
                if fetch_ranges(url, dest):
                    print(f"  got {dest.name}"); jobs.remove((k, dest))
        time.sleep(10)
    print("done" if not jobs else f"still pending: {[j[0] for j in jobs]}")


if __name__ == "__main__":
    main()
