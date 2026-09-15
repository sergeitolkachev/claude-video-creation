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

Which voice is an episode fact, not a channel one. Records 1 and 2 are told by
the channel narrator; record 3 is told by its own operator and uses the
character voice. The episode names it in shots.yaml under `voice:`, and the
default stays narrator.

Usage: gen_narration.py [--scene N] [--seeds 11,22,33] [episode dir]
"""
import os, sys, re, json, subprocess, pathlib, urllib.request, yaml

print = __import__('functools').partial(print, flush=True)

def env():
    for line in pathlib.Path(".env").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

# Shared with build_audio.py and build_captions.py, so a fix to it cannot
# reach two scripts out of three.
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_audio import narration_paragraphs


def paragraphs(script):
    order, paras = narration_paragraphs(script)
    return [(pid, paras[pid]) for pid in order]


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
    doc = yaml.safe_load((ep / "shots.yaml").read_text())
    which = doc.get("voice", "narrator")
    if which not in voice:
        print(f"shots.yaml asks for voice '{which}', which config/voice.yaml "
              f"does not define"); return 1
    n = voice[which]
    key = os.environ["ELEVENLABS_API_KEY"]
    out = ep / "audio" / "narration"; out.mkdir(parents=True, exist_ok=True)

    paras = paragraphs((ep / "script.md").read_text())
    if scene is not None:
        paras = [(pid, txt) for pid, txt in paras if pid.startswith(f"s{scene}p")]
    print(f"{len(paras)} paragraphs, {len(seeds)} takes each, "
          f"voice: {which} ({n['model_id']})\n")

    prev = None
    for pid, text in paras:
        for seed in seeds:
            dst = out / f"{pid}_s{seed}.mp3"
            if dst.exists():
                print(f"  skip  {dst.name}"); continue
            body = {"text": text, "model_id": n["model_id"], "seed": seed}
            # The character entry carries no settings block, deliberately:
            # nothing has been measured about stability or style on that voice,
            # and an unmeasured number written down reads as a decision.
            if n.get("settings"):
                body["voice_settings"] = n["settings"]
            if prev and voice.get("request", {}).get("use_previous_text"):
                body["previous_text"] = prev
            def send(b):
                rq = urllib.request.Request(
                    f"https://api.elevenlabs.io/v1/text-to-speech/{n['voice_id']}"
                    f"?output_format={n['output_format']}",
                    data=json.dumps(b).encode(),
                    headers={"xi-api-key": key, "Content-Type": "application/json"})
                return urllib.request.urlopen(rq, timeout=180).read()
            try:
                dst.write_bytes(send(body))
            except urllib.error.HTTPError as e:
                detail = e.read()[:500].decode(errors="replace")
                # eleven_v3 rejects previous_text outright. Handing prosody
                # across a paragraph boundary is worth having and costs
                # nothing, so it is attempted; when the model refuses, the
                # request goes again without it rather than failing the run.
                # Record 3 is the first episode on the character voice and the
                # first to hit this.
                if "previous_text" in detail and "previous_text" in body:
                    body.pop("previous_text")
                    print(f"  {pid}_s{seed}: model refuses previous_text, "
                          f"sending without it")
                    dst.write_bytes(send(body))
                else:
                # A bare "HTTP Error 400: Bad Request" in a traceback says
                # nothing about which field the API rejected, and this script
                # spends subscription characters. gen_stills.py learned the
                # same thing against fal.
                    print(f"  HTTP {e.code} on {pid}_s{seed}\n    {detail}")
                    raise
            dur = float(subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=nw=1:nk=1", str(dst)],
                capture_output=True, text=True).stdout)
            print(f"  {pid}_s{seed:<3}  {len(text.split()):3d} words  "
                  f"{dur:6.2f}s  {len(text.split())/dur*60:6.1f} wpm")
        prev = text
    print("\nPick one take per paragraph, then record its seed in narration.yaml.")
    return 0

if __name__ == "__main__":
    sys.exit(main() or 0)
