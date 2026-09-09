#!/usr/bin/env python3
"""Stage 7 — narration, one file per paragraph.

Per-request variance in ElevenLabs is large: the same text at the same
settings came back between 123 and 203 wpm across repeated runs. Generating
everything in one sitting does not help, because every paragraph is still its
own request. The seed does: the same seed reproduces the same delivery to four
decimal places.

So this generates several seeded candidates per paragraph and reports the pace
of each. A human picks the take whose pace sits with its neighbours, and the
winning seed goes into narration.yaml — after which the episode's audio is
reproducible from the repository.

Usage: gen_narration.py [--seeds 11,22,33] [episode dir]
"""
import os, sys, re, json, subprocess, pathlib, urllib.request, yaml

print = __import__('functools').partial(print, flush=True)

def env():
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def paragraphs(script):
    """Narration blocks, in scene order, split on blank quoted lines."""
    out = []
    for scene, blk in enumerate(
            # a blank line may sit between the heading and the quote — record
            # 02's script is written that way and record 01's is not
            re.findall(r"\*\*Narration:\*\*\n+((?:>.*\n|\n(?=>))+)", script),
            start=1):
        text = re.sub(r"^> ?", "", blk, flags=re.M)
        for i, para in enumerate([p.strip() for p in text.split("\n\n") if p.strip()], 1):
            out.append((f"s{scene}p{i}", " ".join(para.split())))
    return out

def main():
    env()
    args = sys.argv[1:]
    seeds = [11, 22, 33]
    scene = None
    if "--scene" in args:
        i = args.index("--scene"); scene = int(args[i+1]); del args[i:i+2]
    if "--seeds" in args:
        i = args.index("--seeds"); seeds = [int(x) for x in args[i+1].split(",")]
        del args[i:i+2]
    ep = pathlib.Path(args[0] if args else "episodes/ep-01-tishina-9")
    voice = yaml.safe_load(pathlib.Path("config/voice.yaml").read_text())
    n = voice["narrator"]
    key = os.environ["ELEVENLABS_API_KEY"]
    out = ep / "audio" / "narration"; out.mkdir(parents=True, exist_ok=True)

    paras = paragraphs((ep / "script.md").read_text())
    if scene is not None:
        paras = [(pid, txt) for pid, txt in paras if pid.startswith(f"s{scene}p")]
    print(f"{len(paras)} paragraphs, {len(seeds)} takes each\n")

    prev = None
    for pid, text in paras:
        for seed in seeds:
            dst = out / f"{pid}_s{seed}.mp3"
            if dst.exists():
                print(f"  skip  {dst.name}"); continue
            body = {"text": text, "model_id": n["model_id"],
                    "voice_settings": n["settings"], "seed": seed}
            if prev and voice.get("request", {}).get("use_previous_text"):
                body["previous_text"] = prev
            r = urllib.request.Request(
                f"https://api.elevenlabs.io/v1/text-to-speech/{n['voice_id']}"
                f"?output_format={n['output_format']}",
                data=json.dumps(body).encode(),
                headers={"xi-api-key": key, "Content-Type": "application/json"})
            dst.write_bytes(urllib.request.urlopen(r, timeout=180).read())
            dur = float(subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=nw=1:nk=1", str(dst)],
                capture_output=True, text=True).stdout)
            print(f"  {pid}_s{seed:<3}  {len(text.split()):3d} words  "
                  f"{dur:6.2f}s  {len(text.split())/dur*60:6.1f} wpm")
        prev = text
    print("\nPick one take per paragraph, then record its seed in narration.yaml.")

if __name__ == "__main__":
    main()
