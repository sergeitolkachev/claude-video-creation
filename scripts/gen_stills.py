#!/usr/bin/env python3
"""Stage 4 — generate candidate first frames for a scene.

Anchors are always passed as references, which is the whole point of stage 3.
Shots with no anchor listed are object studies that carry no location; they
get the spine as text instead, so they still read as the same station.

Usage: gen_stills.py <scene number> [episode dir]
Scene at a time on purpose: 87 stills in one go is over the batch threshold in
CLAUDE.md, and a bad anchor would only show up after all of it had been paid for.
"""
import os, sys, json, time, pathlib, urllib.request, yaml

# Candidates per shot. A shot sitting on an anchor comes back nearly
# identical across seeds — the anchor has already fixed the frame, so a third
# candidate buys nothing. A shot with no anchor has nothing holding it and
# scatters, so it gets more. Scene 2 measured this: the three porthole
# candidates were interchangeable, the three antenna candidates were three
# different objects.
SEEDS_ANCHORED = [11, 22]
SEEDS_FREE     = [11, 22, 33, 44]

def env():
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def post(url, body, key):
    r = urllib.request.Request(url, data=json.dumps(body).encode(),
        headers={"Authorization": f"Key {key}", "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r))

def get(url, key):
    return json.load(urllib.request.urlopen(
        urllib.request.Request(url, headers={"Authorization": f"Key {key}"})))

def upload(path, key, cache):
    """Put an approved still into fal storage so a later shot can reference it.
    Cached by filename — an approved image never changes."""
    c = json.loads(cache.read_text()) if cache.exists() else {}
    if path.name in c:
        return c[path.name]
    r = urllib.request.Request(
        "https://rest.alpha.fal.ai/storage/upload/initiate?storage_type=fal-cdn-v3",
        data=json.dumps({"content_type": "image/jpeg",
                         "file_name": path.name}).encode(),
        headers={"Authorization": f"Key {key}", "Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(r))
    urllib.request.urlopen(urllib.request.Request(
        d["upload_url"], data=path.read_bytes(),
        headers={"Content-Type": "image/jpeg"}, method="PUT"))
    c[path.name] = d["file_url"]; cache.write_text(json.dumps(c, indent=2))
    return d["file_url"]


def main():
    env(); key = os.environ["FAL_API_KEY"]
    scene = int(sys.argv[1])
    ep = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "episodes/ep-01-tishina-9")
    cfg = yaml.safe_load(pathlib.Path("config/models.yaml").read_text())
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    still_model = cfg["image"]["still"]
    ext_model  = cfg["image"]["exterior"]
    anchor_urls = json.loads((ep / "anchors" / "urls.json").read_text())
    spine = " ".join(doc["anchors"][0]["spine"].split())
    ext_spine = " ".join(doc["exterior_spine"].split())
    out = ep / "stills"; out.mkdir(exist_ok=True)

    shots = [s for s in doc["shots"]
             if s["scene"] == scene and s.get("source") != "ffmpeg"]

    # A shot with `plates:` is not generated as video at all, but it still
    # needs stills — record 2's shot 3.3 is one patch of ground photographed
    # three times as it dries out. The first plate is generated against the
    # anchor like any other still; the later ones reference the *approved*
    # first plate, because the whole point is that it is the same square metre.
    # So they only queue once 3.3a has been picked, and say so until then.
    for s0 in doc["shots"]:
        if s0["scene"] != scene or not s0.get("plates"):
            continue
        base = s0["plates"][0]
        shots.append({**s0, "id": base, "plate_prompts": None})
        for pid, pprompt in (s0.get("plate_prompts") or {}).items():
            if (ep / "approved" / f"{base}.jpg").exists():
                shots.append({**s0, "id": pid, "prompt": pprompt,
                              "anchors": [], "ref_shot": base,
                              "plate_prompts": None})
            else:
                print(f"  hold   {pid}: waiting on approved/{base}.jpg")
    if not shots:
        print(f"scene {scene}: nothing to generate"); return

    jobs = []
    for s in shots:
        prompt = " ".join(s["prompt"].split())
        # A shot that shows where the animal has passed carries the canonical
        # description of the trail. It goes after the framing, because the framing
        # is what the reference image argues with and the mark is what the
        # enhancer would otherwise invent.
        if s.get("trail_canon"):
            prompt = f"{prompt}. {' '.join(s['trail_canon'].split())}"
        if s.get("ref_shot"):
            # Two shots in this episode are the same physical plate seen twice
            # in the story (1.2/4.3 the delay readout, 1.3/4.1 the porthole).
            # An anchor would only make them the same kind of thing; the
            # approved still makes them the same object.
            src = ep / "approved" / f"{s['ref_shot']}.jpg"
            model = still_model
            refs = [upload(src, key, ep / "approved" / "urls.json")]
            kind, seeds = f"shot {s['ref_shot']}", SEEDS_ANCHORED
        elif s.get("exterior"):
            # No reference at all: style goes in as text and the endpoint is
            # text-to-image. Record 1 used this where every anchor was an
            # interior and would have leaked a bulkhead into open space.
            # Record 2 uses it where the anchor is the thing doing the damage
            # — A3 injected a band of tyre tread into every ground shot that
            # referenced it, through five passes.
            #
            # Which text spine is per shot: the default is the episode's
            # exterior_spine, but a shot can name another key, because "seen
            # from three thousand metres" is the wrong opening sentence for a
            # macro of wet soil.
            spine_key = s.get("spine_key", "exterior_spine")
            model, refs, kind = ext_model, None, f"text-only/{spine_key}"
            seeds = SEEDS_FREE
            prompt = f"{' '.join(doc[spine_key].split())} {prompt}"
        elif s.get("anchors"):
            model = still_model
            refs = [anchor_urls[a] for a in s["anchors"]]
            kind = "+".join(a.split("-")[0] for a in s["anchors"])
            seeds = SEEDS_ANCHORED
        else:
            # An interior object study: no anchor of its own, but the station
            # still has to be recognisable behind it, so A1 goes in as a
            # style reference and the spine goes in as text.
            model = still_model
            # Whatever the episode's first anchor is — record 1 hardcoded
            # its own control room here, which is not a fact about the
            # pipeline.
            refs = [anchor_urls[doc["anchors"][0]["id"]]]
            kind, seeds = "style-ref", SEEDS_FREE
            prompt = f"{spine} {prompt}"

        for seed in seeds:
            dest = out / f"{s['id']}_s{seed}.jpg"
            if dest.exists():
                print(f"  skip   {dest.name}"); continue
            body = {"prompt": prompt, "num_images": 1, "seed": seed}
            if refs:
                body |= {"image_urls": refs, "aspect_ratio": "16:9",
                         "output_format": "jpeg"}
            else:
                body |= {"image_size": "landscape_16_9"}
            res = post(f"https://queue.fal.run/{model['id']}", body, key)
            jobs.append((dest, res["status_url"], res["response_url"],
                         model["price_per_image_usd"]))
            print(f"  queued {dest.name:<16} refs: {kind}")

    cost = sum(j[3] for j in jobs)
    print(f"\nscene {scene}: {len(shots)} shots, {len(jobs)} generations, "
          f"${cost:.2f}\n")

    done = 0
    spent = 0.0
    for dest, status_url, response_url, price in jobs:
        for _ in range(120):
            st = get(status_url, key)["status"]
            if st == "COMPLETED": break
            time.sleep(2)
        else:
            print(f"  TIMEOUT {dest.name}"); continue
        r = get(response_url, key)
        if not r.get("images"):
            print(f"  EMPTY   {dest.name}  {str(r)[:120]}"); continue
        dest.write_bytes(urllib.request.urlopen(r["images"][0]["url"]).read())
        done += 1; spent += price
        print(f"  saved  {dest.name}  ({dest.stat().st_size // 1024} KB)")

    print(f"\n{done}/{len(jobs)} saved. Spent ${spent:.2f}.")

if __name__ == "__main__":
    main()
