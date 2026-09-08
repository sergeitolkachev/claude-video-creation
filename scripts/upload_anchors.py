#!/usr/bin/env python3
"""Upload the approved anchors to fal storage once and cache the URLs.

Every shot still passes anchors as references. Uploading them per request
would mean shipping the same 3 MB eighty-seven times; this uploads once and
the URLs are reused for the whole episode.
"""
import os, sys, json, pathlib, urllib.request, yaml

def env():
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def main():
    env(); key = os.environ["FAL_API_KEY"]
    ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9")
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    cache = ep / "anchors" / "urls.json"
    urls = json.loads(cache.read_text()) if cache.exists() else {}

    for a in doc["anchors"]:
        aid = a["id"]
        if aid in urls:
            print(f"  cached {aid}"); continue
        f = ep.parent.parent / a["approved_file"] if False else ep / "anchors" / f"{aid}.jpg"
        body = json.dumps({"content_type": "image/jpeg", "file_name": f.name}).encode()
        r = urllib.request.Request(
            "https://rest.alpha.fal.ai/storage/upload/initiate?storage_type=fal-cdn-v3",
            data=body, headers={"Authorization": f"Key {key}",
                                "Content-Type": "application/json"})
        d = json.load(urllib.request.urlopen(r))
        put = urllib.request.Request(d["upload_url"], data=f.read_bytes(),
                                     headers={"Content-Type": "image/jpeg"}, method="PUT")
        urllib.request.urlopen(put)
        urls[aid] = d["file_url"]
        print(f"  uploaded {aid}  ({f.stat().st_size // 1024} KB)")

    cache.write_text(json.dumps(urls, indent=2))
    print(f"\n{len(urls)} anchor URLs cached in {cache}")

if __name__ == "__main__":
    main()
