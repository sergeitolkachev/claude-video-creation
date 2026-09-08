#!/usr/bin/env python3
"""Cost estimate from shots.yaml and config/models.yaml. Sums generate_seconds,
skips anything with source: ffmpeg."""
import sys, pathlib, yaml
from collections import defaultdict

CANDIDATES_PER_SHOT = 3
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
    c = tier["price_10s_usd"] if t == "workhorse" and g == 10 \
        else g * tier["price_per_second_usd"]
    by[t][0] += 1; by[t][1] += g; by[t][2] += c

print(f"{'tier':<12}{'shots':>7}{'sec':>7}{'usd':>9}   endpoint")
for t, (n, sec, c) in by.items():
    eid = "— built locally, no model" if t.startswith("ffmpeg") else cfg["video"][t]["id"]
    print(f"{t:<12}{n:>7}{sec:>7}{c:>9.2f}   {eid}")
    tot += c
video = tot

gen = [s for s in shots if not s.get("source", "").startswith("ffmpeg")]
stills_n = len(gen) * CANDIDATES_PER_SHOT
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
