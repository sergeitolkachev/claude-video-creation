#!/usr/bin/env python3
"""Stage 6 — animate approved stills.

Only approved/ is ever animated. This is the expensive stage: a clip costs
20-30x a still, so nothing here runs on a frame a human has not signed off.

Usage: gen_takes.py <scene> [--only 2.1] [episode dir]
"""
import os, sys, json, time, pathlib, urllib.request, urllib.error, yaml

print = __import__('functools').partial(print, flush=True)

# A queued request is money already spent. Record 04 lost $0.70 to a poll that
# hung on a clip whose request id existed only inside the running process: the
# job had to be killed, and with it went the only handle on a request fal had
# already accepted and was still working on. The id is written to disk the
# moment the request is accepted, and a rerun resumes from it instead of
# queueing — and paying for — the same clip twice. CLAUDE.md has warned about
# exactly this since record 01; the stills script was fixed and this one was
# not, which is the "count the copies" rule arriving late again.
POLL_CEILING_S = 1800     # wall clock, not an iteration count


def pending_load(ep):
    f = ep / "takes" / "pending.json"
    return (json.loads(f.read_text()) if f.exists() else {}), f


def pending_write(ep, data):
    (ep / "takes" / "pending.json").write_text(json.dumps(data, indent=2))

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
    # --dry-run prints the exact body that would be sent and spends nothing.
    #
    # Record 05 paid $0.70 to learn why this is needed. A shots.yaml edit
    # raised an error after its first substitution and before the file was
    # written, so nothing was saved; the generate command was on the next
    # shell line rather than chained to it and ran anyway, against the
    # unchanged prompt. The money bought a second copy of a take that had
    # already been rejected.
    #
    # What makes that impossible is not remembering to check. It is being able
    # to see the outgoing prompt without paying for it, which is what this is.
    # Run it after every prompt edit and before every generate.
    dry = "--dry-run" in args
    if dry: args.remove("--dry-run")
    scene = int(args[0])
    ep = pathlib.Path(args[1] if len(args) > 1 else "episodes/ep-01-tishina-9")
    cfg = yaml.safe_load(pathlib.Path("config/models.yaml").read_text())
    doc = yaml.safe_load((ep / "shots.yaml").read_text())

    def tail_for(s):
        """The constraint paragraph appended to a shot's motion prompt.

        Two tails were not enough. `motion_tail_moving` says the movement
        "covers only a very short distance across the whole shot", which is
        right for drifting dust and wrong for a hatch swinging closed — record
        3's 4.1 asked for a traverse and would have been told, in the same
        prompt, not to traverse. A shot may name its own tail key instead.
        """
        if s.get("motion_tail"):
            return " ".join(doc[s["motion_tail"]].split())
        # The two defaults are record 01 and 03's, and they are not channel
        # property: record 04 names a tail on every model shot and defines
        # neither. Reading them at the top of main() made that record crash
        # before it queued anything, on a key it has no use for. Looked up
        # only when a shot actually falls back to one, and loudly if missing.
        key = ("motion_tail_static" if s["motion"].strip() == "static"
               else "motion_tail_moving")
        if key not in doc:
            raise SystemExit(f"{s['id']} names no motion_tail and this episode "
                             f"has no {key}: give the shot its own tail key")
        return " ".join(doc[key].split())
    out = ep / "takes"; out.mkdir(exist_ok=True)
    cache = ep / "approved" / "urls.json"

    shots = [s for s in doc["shots"]
             if s["scene"] == scene and not s.get("source", "").startswith("ffmpeg")
             and (only is None or s["id"] == only)]

    pend, pend_f = pending_load(ep)

    jobs = []
    for s in shots:
        dest = out / f"{s['id']}.mp4"
        if dest.exists():
            print(f"  skip   {dest.name} (already there)"); continue
        if s["id"] in pend:
            # Already paid for on an earlier run that did not collect it.
            j = pend[s["id"]]
            print(f"  resume {s['id']:<5} id={j.get('request_id')}  "
                  f"(queued {int(time.time() - j['queued_at'])}s ago, "
                  f"${j['price']:.2f} already spent)")
            jobs.append((dest, j["status_url"], j["response_url"], 0.0, s))
            continue
        tier = cfg["video"][s["model"]]
        plate = ep / "approved" / f"{s['id']}.jpg"
        img = "<dry-run: not uploaded>" if dry else upload(plate, key, cache)
        gen = s["generate_seconds"]
        static = s["motion"].strip() == "static"
        motion = s.get("video_prompt") or (
            "Hold the frame exactly as it is." if static
            else f"A {s['motion']} on the scene already in frame.")
        prompt = " ".join(f"{motion} {tail_for(s)}".split())

        if s["model"] == "workhorse":
            body = {"image_url": img, "prompt": prompt, "duration": str(gen),
                    # Re-checked against fal's published schema 2026-09-14:
                    # this endpoint has NO generate_audio parameter at all. It
                    # exists on Kling v2.6 Pro and v3, not on v2.5 Turbo Pro,
                    # so the earlier note here — "Kling defaults this to true"
                    # — was simply wrong, and record 01 was never paying for
                    # native audio it then stripped. The field is left in
                    # because fal ignores unknown keys and because the day a
                    # tier here is swapped for one that does have it, the
                    # audio-off rule must already be in the body.
                    "generate_audio": False,
                    "negative_prompt":
                        # every item here is something a probe actually produced
                        "fast motion, camera shake, dolly, rapid push in, zoom, "
                        "water, wet floor, puddles, reflections on the floor, "
                        "morphing geometry, changing architecture, brightening, "
                        "blur, distortion, low quality, people, text, watermark"
                        + (", " + " ".join(s["negative_extra"].split())
                           if s.get("negative_extra") else "")}
            price = tier["price_10s_usd"] if gen == 10 else \
                    tier["price_base_usd"] + max(0, gen - 5) * tier["price_per_extra_second_usd"]
        else:
            body = {"image_url": img, "prompt": prompt, "duration": str(gen),
                    "resolution": tier["resolution"], "aspect_ratio": "16:9",
                    "seed": 11, "camera_fixed": s["motion"].strip() == "static"}
            price = gen * tier["price_per_second_usd"]

        if dry:
            print(f"\n  ---- {s['id']}  {s['model']}  {gen}s  ${price:.2f} "
                  f"{'(plate MISSING)' if not plate.exists() else ''}")
            print(f"  endpoint : {tier['id']}")
            print(f"  prompt   : {body['prompt']}")
            if body.get("negative_prompt"):
                print(f"  negative : {body['negative_prompt']}")
            for k in ("duration", "generate_audio", "camera_fixed", "resolution"):
                if k in body: print(f"  {k:<9}: {body[k]}")
            jobs.append((dest, None, None, price, s))
            continue

        r = req(f"https://queue.fal.run/{tier['id']}", key, body)
        # Written before anything is polled: from here on the request exists on
        # fal's side whatever happens to this process.
        pend[s["id"]] = {"request_id": r.get("request_id"),
                         "status_url": r["status_url"],
                         "response_url": r["response_url"],
                         "price": price, "queued_at": time.time()}
        pending_write(ep, pend)
        jobs.append((dest, r["status_url"], r["response_url"], price, s))
        print(f"  queued {s['id']:<5} {s['model']:<10} {gen}s  "
              f"camera_fixed={body.get('camera_fixed', '-')}  ${price:.2f}  "
              f"id={r.get('request_id')}")

    print(f"\nscene {scene}: {len(jobs)} clips, ${sum(j[3] for j in jobs):.2f}\n")
    if dry:
        print("DRY RUN — nothing was queued, nothing was uploaded, $0.00 spent.")
        return

    spent = 0.0
    for dest, status_url, response_url, price, s in jobs:
        # Wall clock, so a poll that answers slowly cannot quietly stretch the
        # ceiling: 300 iterations of a 60 s socket timeout is five hours, not
        # the fifteen minutes the number looked like.
        deadline = time.time() + POLL_CEILING_S
        st = None
        while time.time() < deadline:
            try:
                st = req(status_url, key)["status"]
            except Exception as e:          # a dropped poll is not a dead job
                print(f"  ... poll error on {s['id']}: {type(e).__name__}")
                time.sleep(5); continue
            if st == "COMPLETED": break
            time.sleep(3)
        if st != "COMPLETED":
            print(f"  TIMEOUT {dest.name}  — request kept in pending.json, "
                  f"rerun resumes it without paying again"); continue
        try:
            r = req(response_url, key)
        except urllib.error.HTTPError as e:
            print(f"  FAIL   {dest.name}  {e.read().decode()[:160]}"); continue
        # The download is the last place this can fail and it is not the model
        # failing: record 04 lost a completed 7.1 to a socket that stopped
        # feeding mid-file, and the traceback took the rest of the run with it.
        # The clip is paid for and finished either way, so this retries rather
        # than dying, and leaves the request in pending.json if it cannot.
        for attempt in range(3):
            try:
                dest.write_bytes(
                    urllib.request.urlopen(r["video"]["url"], timeout=300).read())
                break
            except Exception as e:
                print(f"  ... download failed for {s['id']} "
                      f"({type(e).__name__}), attempt {attempt + 1} of 3")
                time.sleep(5)
        else:
            print(f"  FAIL   {dest.name} — generated and paid for, still in "
                  f"pending.json; rerun downloads it again")
            continue
        spent += price
        pend.pop(s["id"], None); pending_write(ep, pend)
        print(f"  saved  {dest.name}  ({dest.stat().st_size // 1024} KB)")

    print(f"\nSpent ${spent:.2f}.")

if __name__ == "__main__":
    main()
