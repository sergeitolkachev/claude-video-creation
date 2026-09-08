#!/usr/bin/env python3
"""Stage 6 — animate approved stills.

Only approved/ is ever animated. This is the expensive stage: a clip costs
20-30x a still, so nothing here runs on a frame a human has not signed off.

Usage: gen_takes.py <scene> [--only 2.1] [episode dir]
"""
import os, sys, json, time, pathlib, urllib.request, urllib.error, yaml

print = __import__('functools').partial(print, flush=True)

def env():
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def req(url, key, body=None, method=None):
    r = urllib.request.Request(
        url, data=json.dumps(body).encode() if body else None,
        headers={"Authorization": f"Key {key}", "Content-Type": "application/json"},
        method=method)
    return json.load(urllib.request.urlopen(r, timeout=60))

def upload(path, key, cache):
    c = json.loads(cache.read_text()) if cache.exists() else {}
    if path.name in c: return c[path.name]
    d = req("https://rest.alpha.fal.ai/storage/upload/initiate?storage_type=fal-cdn-v3",
            key, {"content_type": "image/jpeg", "file_name": path.name})
    urllib.request.urlopen(urllib.request.Request(
        d["upload_url"], data=path.read_bytes(),
        headers={"Content-Type": "image/jpeg"}, method="PUT"), timeout=120)
    c[path.name] = d["file_url"]; cache.write_text(json.dumps(c, indent=2))
    return d["file_url"]

def main():
    env(); key = os.environ["FAL_API_KEY"]
    args = [a for a in sys.argv[1:]]
    only = None
    if "--only" in args:
        i = args.index("--only"); only = args[i+1]; del args[i:i+2]
    scene = int(args[0])
    ep = pathlib.Path(args[1] if len(args) > 1 else "episodes/ep-01-tishina-9")
    cfg = yaml.safe_load(pathlib.Path("config/models.yaml").read_text())
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    tail_static = " ".join(doc["motion_tail_static"].split())
    tail_moving = " ".join(doc["motion_tail_moving"].split())
    out = ep / "takes"; out.mkdir(exist_ok=True)
    cache = ep / "approved" / "urls.json"

    shots = [s for s in doc["shots"]
             if s["scene"] == scene and s.get("source") != "ffmpeg"
             and (only is None or s["id"] == only)]

    jobs = []
    for s in shots:
        dest = out / f"{s['id']}.mp4"
        if dest.exists():
            print(f"  skip   {dest.name} (already there)"); continue
        tier = cfg["video"][s["model"]]
        img = upload(ep / "approved" / f"{s['id']}.jpg", key, cache)
        gen = s["generate_seconds"]
        static = s["motion"].strip() == "static"
        motion = s.get("video_prompt") or (
            "Hold the frame exactly as it is." if static
            else f"A {s['motion']} on the scene already in frame.")
        prompt = " ".join(f"{motion} {tail_static if static else tail_moving}".split())

        if s["model"] == "workhorse":
            body = {"image_url": img, "prompt": prompt, "duration": str(gen),
                    "negative_prompt":
                        # every item here is something a probe actually produced
                        "fast motion, camera shake, dolly, rapid push in, zoom, "
                        "water, wet floor, puddles, reflections on the floor, "
                        "morphing geometry, changing architecture, brightening, "
                        "blur, distortion, low quality, people, text, watermark"}
            price = tier["price_10s_usd"] if gen == 10 else \
                    tier["price_base_usd"] + max(0, gen - 5) * tier["price_per_extra_second_usd"]
        else:
            body = {"image_url": img, "prompt": prompt, "duration": str(gen),
                    "resolution": tier["resolution"], "aspect_ratio": "16:9",
                    "seed": 11, "camera_fixed": s["motion"].strip() == "static"}
            price = gen * tier["price_per_second_usd"]

        r = req(f"https://queue.fal.run/{tier['id']}", key, body)
        jobs.append((dest, r["status_url"], r["response_url"], price, s))
        print(f"  queued {s['id']:<5} {s['model']:<10} {gen}s  "
              f"camera_fixed={body.get('camera_fixed', '-')}  ${price:.2f}")

    print(f"\nscene {scene}: {len(jobs)} clips, ${sum(j[3] for j in jobs):.2f}\n")

    spent = 0.0
    for dest, status_url, response_url, price, s in jobs:
        for _ in range(300):
            try:
                st = req(status_url, key)["status"]
            except Exception as e:          # a dropped poll is not a dead job
                print(f"  ... poll error on {s['id']}: {type(e).__name__}")
                time.sleep(5); continue
            if st == "COMPLETED": break
            time.sleep(3)
        else:
            print(f"  TIMEOUT {dest.name}"); continue
        try:
            r = req(response_url, key)
        except urllib.error.HTTPError as e:
            print(f"  FAIL   {dest.name}  {e.read().decode()[:160]}"); continue
        dest.write_bytes(urllib.request.urlopen(r["video"]["url"], timeout=300).read())
        spent += price
        print(f"  saved  {dest.name}  ({dest.stat().st_size // 1024} KB)")

    print(f"\nSpent ${spent:.2f}.")

if __name__ == "__main__":
    main()
