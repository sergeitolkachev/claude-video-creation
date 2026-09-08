#!/usr/bin/env python3
"""Stage 3 — generate anchor candidates.

Anchors define the location and the light for the whole episode. Everything
downstream references them, so they are generated first and approved by a
human before a single shot still is made.

Seeds are explicit and land in the filename. A candidate that gets picked can
then be reproduced exactly, the same way narration seeds work.
"""
import os, sys, json, time, pathlib, urllib.request, yaml

CANDIDATES = 3
SEEDS = [11, 22, 33]          # same three seeds for every anchor, so a
                              # difference between candidates is the prompt,
                              # not an unrecorded roll
IMAGE_SIZE = "landscape_16_9"

def env():
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def post(url, body, key):
    r = urllib.request.Request(url, data=json.dumps(body).encode(),
        headers={"Authorization": f"Key {key}", "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r))

def get(url, key):
    r = urllib.request.Request(url, headers={"Authorization": f"Key {key}"})
    return json.load(urllib.request.urlopen(r))

def main():
    env()
    key = os.environ["FAL_API_KEY"]
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9")
    cfg = yaml.safe_load(pathlib.Path("config/models.yaml").read_text())
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    model = cfg["image"]["anchor"]
    out = ep / "anchors"; out.mkdir(exist_ok=True)

    jobs = []
    for a in doc["anchors"]:
        for seed in SEEDS[:CANDIDATES]:
            dest = out / f"{a['id']}_s{seed}.jpg"
            if dest.exists():
                print(f"  skip  {dest.name} (already there)"); continue
            prompt = " ".join((a.get("spine", "") + " " + a["subject"]).split()) \
                     if "subject" in a else " ".join(a["prompt"].split())
            res = post(f"https://queue.fal.run/{model['id']}",
                       {"prompt": prompt,
                        "image_size": IMAGE_SIZE, "num_images": 1, "seed": seed}, key)
            jobs.append((dest, res["status_url"], res["response_url"]))
            print(f"  queued {dest.name}")

    print(f"\n{len(jobs)} queued, {len(jobs) * model['price_per_image_usd']:.2f} USD\n")

    done = 0
    for dest, status_url, response_url in jobs:
        for _ in range(90):
            if get(status_url, key)["status"] == "COMPLETED":
                break
            time.sleep(2)
        else:
            print(f"  TIMEOUT {dest.name}"); continue
        url = get(response_url, key)["images"][0]["url"]
        dest.write_bytes(urllib.request.urlopen(url).read())
        done += 1
        print(f"  saved  {dest.name}  ({dest.stat().st_size // 1024} KB)")

    spent = done * model["price_per_image_usd"]
    print(f"\n{done}/{len(jobs)} saved. Spent ${spent:.2f} on {model['id']}.")

if __name__ == "__main__":
    main()
