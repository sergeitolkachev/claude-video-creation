#!/usr/bin/env python3
"""Stage 7 — sound effects and room tone, from ElevenLabs.

Room tone is the one layer that must never be absent: absolute digital silence
under a found recording destroys the illusion that anything was recorded at
all. Everything here is listed in the episode's audio.yaml under `sfx:` so a
lost file is regenerable from the repository.

Usage: gen_sfx.py [episode dir] [--only wind]
"""
import json, os, pathlib, sys, urllib.request, yaml

print = __import__('functools').partial(print, flush=True)
API = "https://api.elevenlabs.io/v1/sound-generation"


def env():
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())


def main():
    env()
    args = sys.argv[1:]
    only = None
    if "--only" in args:
        i = args.index("--only"); only = args[i + 1]; del args[i:i + 2]
    ep = pathlib.Path(args[0] if args else "episodes/ep-02-sunrise-line")
    cfg = yaml.safe_load((ep / "audio.yaml").read_text())
    key = os.environ["ELEVENLABS_API_KEY"]

    for name, spec in (cfg.get("sfx") or {}).items():
        if only and name != only:
            continue
        dest = ep / "audio" / spec["file"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            print(f"  skip  {name} ({dest} already there)"); continue
        body = {"text": " ".join(spec["prompt"].split()),
                "duration_seconds": spec.get("seconds", 22),
                "prompt_influence": spec.get("influence", 0.6)}
        r = urllib.request.Request(
            API, data=json.dumps(body).encode(),
            headers={"xi-api-key": key, "Content-Type": "application/json"})
        dest.write_bytes(urllib.request.urlopen(r, timeout=300).read())
        print(f"  saved {name:<8} {dest}  ({dest.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
