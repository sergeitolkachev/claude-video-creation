#!/usr/bin/env python3
"""Cost estimate from shots.yaml and config/models.yaml. Sums generate_seconds,
skips anything with source: ffmpeg."""
import sys, pathlib, yaml
from collections import defaultdict

# What gen_stills.py actually does: a shot sitting on an anchor comes back
# nearly identical across seeds, so it gets two candidates; a shot with
# nothing holding it scatters, so it gets four.
CANDIDATES_ANCHORED = 2
CANDIDATES_FREE = 4
CANDIDATES_PER_ANCHOR = 3

ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "episodes/ep-01-tishina-9")
cfg = yaml.safe_load(pathlib.Path("config/models.yaml").read_text())
doc = yaml.safe_load((ep / "shots.yaml").read_text())
shots = doc["shots"]

rows, tot = [], 0.0
by = defaultdict(lambda: [0, 0, 0.0])   # tier -> [shots, seconds, usd]
for s in shots:
    if s.get("source", "").startswith("ffmpeg"):
        by[s["source"]][0] += 1
        continue
    t, g = s["model"], s["generate_seconds"]
    tier = cfg["video"][t]
    if t == "workhorse":
        # Kling is priced per clip, not per second: $0.35 covers the first
        # five, $0.70 buys ten. Record 1 only ever bought ten.
        c = tier["price_10s_usd"] if g == 10 else tier["price_base_usd"]
    else:
        c = g * tier["price_per_second_usd"]
    by[t][0] += 1; by[t][1] += g; by[t][2] += c

print(f"{'tier':<12}{'shots':>7}{'sec':>7}{'usd':>9}   endpoint")
for t, (n, sec, c) in by.items():
    eid = "— built locally, no model" if t.startswith("ffmpeg") else cfg["video"][t]["id"]
    print(f"{t:<12}{n:>7}{sec:>7}{c:>9.2f}   {eid}")
    tot += c
video = tot

# Every shot needs an approved still, including the ones built locally —
# a locked-off shot is a still with lens breathing on it, so it costs the
# same stills as a generated one. Counting only the video shots here
# understated record 1 by a factor of three.
needs_still = [s for s in shots if s.get("prompt")]
stills_n = sum(CANDIDATES_ANCHORED if s.get("anchors") or s.get("ref_shot")
               else CANDIDATES_FREE for s in needs_still)
stills_n += sum(len(s.get("plate_prompts", {})) * CANDIDATES_ANCHORED
                for s in shots)
stills = stills_n * cfg["image"]["still"]["price_per_image_usd"]
anch_n = len(doc["anchors"]) * CANDIDATES_PER_ANCHOR
anch = anch_n * cfg["image"]["anchor"]["price_per_image_usd"]

print(f"\n{'stills':<12}{stills_n:>7}{'':>7}{stills:>9.2f}   {cfg['image']['still']['id']}")
print(f"{'anchors':<12}{anch_n:>7}{'':>7}{anch:>9.2f}   {cfg['image']['anchor']['id']}")
base = video + stills + anch
print(f"\n  base, zero retakes      ${base:6.2f}")
print(f"  +30% video retakes      ${base + video*0.3:6.2f}")
print(f"  ceiling                 $30.00")
print(f"\n  largest single batch: {stills_n} stills "
      f"({'needs confirmation, over ~50' if stills_n > 50 else 'under the 50 threshold'})")
