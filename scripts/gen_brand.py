#!/usr/bin/env python3
"""Channel art — generate candidates for every asset in config/brand.yaml.

Same shape as gen_anchors.py: three seeds per asset, the seed in the filename,
a human picks. Different in two ways — each asset carries its own pixel size
rather than one shared aspect, and the candidates land in brand/ instead of
inside an episode, because channel art outlives episodes.

Every network call carries an explicit timeout and every print is flushed.
An unflushed log cost an hour on episode 01 and a lost request id costs the
price of the clip twice over.

    python3 scripts/gen_brand.py            # everything
    python3 scripts/gen_brand.py thumbnail  # one asset
"""
import os, sys, json, time, pathlib, urllib.request, urllib.error, yaml

TIMEOUT = 60          # seconds, on every socket
POLL_LIMIT = 90       # x 2 s = three minutes before giving up on a job

def say(*a):
    print(*a, flush=True)

def env():
    p = pathlib.Path(".env")
    if not p.exists():
        sys.exit("no .env — copy env.example and fill in FAL_API_KEY")
    for line in p.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def call(url, key, body=None, tries=3):
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Authorization": f"Key {key}"}
    if data:
        headers["Content-Type"] = "application/json"
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return json.load(r)
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == tries - 1:
                raise
            say(f"  retry {attempt + 1}/{tries - 1} after {e}")
            time.sleep(3)

def main():
    env()
    key = os.environ["FAL_API_KEY"]
    cfg = yaml.safe_load(pathlib.Path("config/models.yaml").read_text())
    brand = yaml.safe_load(pathlib.Path("config/brand.yaml").read_text())
    model = cfg["image"]["anchor"]        # text-to-image: there is nothing to
                                          # reference, the same as an anchor
    wanted = set(sys.argv[1:])
    out = pathlib.Path("brand"); out.mkdir(exist_ok=True)

    jobs = []
    for a in brand["assets"]:
        if wanted and a["id"] not in wanted:
            continue
        prompt = " ".join((brand["spine"] + " " + a["subject"]).split())
        for seed in brand["seeds"]:
            dest = out / f"{a['id']}_s{seed}.jpg"
            if dest.exists():
                say(f"  skip   {dest.name} (already there)"); continue
            res = call(f"https://queue.fal.run/{model['id']}", key,
                       {"prompt": prompt, "image_size": a["generate"],
                        "num_images": 1, "seed": seed})
            jobs.append((dest, res["status_url"], res["response_url"]))
            say(f"  queued {dest.name}  {res['request_id']}")

    if not jobs:
        say("nothing to do"); return

    # Priced at 1MP and scaling with area, so a 2560x1440 banner is not the
    # same money as a 1024 square. Quote the real number before waiting.
    def megapixels(a):
        return a["generate"]["width"] * a["generate"]["height"] / 1_000_000
    est = sum(megapixels(a) * model["price_per_image_usd"] * len(brand["seeds"])
              for a in brand["assets"] if not wanted or a["id"] in wanted)
    say(f"\n{len(jobs)} queued, about ${est:.2f}\n")

    done = 0
    for dest, status_url, response_url in jobs:
        for _ in range(POLL_LIMIT):
            if call(status_url, key)["status"] == "COMPLETED":
                break
            time.sleep(2)
        else:
            say(f"  TIMEOUT {dest.name}  {status_url}"); continue
        url = call(response_url, key)["images"][0]["url"]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            dest.write_bytes(r.read())
        done += 1
        say(f"  saved  {dest.name}  ({dest.stat().st_size // 1024} KB)")

    say(f"\n{done}/{len(jobs)} saved into brand/. "
        f"Pick one per asset and copy it to brand/approved/<id>.jpg.")

if __name__ == "__main__":
    main()
