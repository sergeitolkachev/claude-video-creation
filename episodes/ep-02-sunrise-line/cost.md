# Cost — ep-02-sunrise-line

Ceiling: **$30**, the same as record 1. Prices in `config/models.yaml` were
verified 2026-09-08 and re-read for this plan on 2026-09-09; nothing had
drifted in a day, so they were not re-probed. **Re-probe before stage 6** —
that is where the money is, and a stale price there is worth more than a
stale price anywhere else.

Regenerate the plan column with `scripts/estimate.py episodes/ep-02-sunrise-line`.

## Plan

| Item | Count | Sec | Planned | Actual |
|---|---:|---:|---:|---:|
| Workhorse video — Kling 2.5 Turbo Pro | 7 | 65 | $4.55 | |
| Locked-off shots — built in ffmpeg | 26 | — | $0.00 | |
| Shot 3.3 — three-plate dissolve, ffmpeg | 1 | — | $0.00 | |
| Shot stills — Nano Banana, 2 anchored / 4 free | 74 | — | $2.95 | |
| Anchors — Seedream V4, 3 per anchor, 5 anchors | 15 | — | $0.45 | |
| **Base, zero retakes** | | | **$7.95** | |
| Reserve, +30% on video | | | $1.37 | |
| Anchor reserve, 2 extra passes | | | $0.90 | |
| **Expected** | | | **$10.22** | |

Narration comes out of the ElevenLabs subscription, not this budget. 452
words is about 2 600 characters against a 35 903 character monthly allowance;
at three seeded takes per paragraph that is roughly 7 800, still comfortable.

## Why this is half of record 1

Record 1 spent $18.28. Two things changed, and neither is a cheaper model.

**Twenty-six of thirty-four shots are built locally.** Record 1 arrived at
that answer by paying for it — $2.42 of Seedance and Kling probes established
that no model holds a locked-off frame, and then seventeen shots were rebuilt
in ffmpeg anyway. Record 2 starts there. Only the seven shots with real
movement go to Kling, and one of those (7.2, the animal) buys a five-second
clip rather than ten, because the shot is four seconds long and Kling's
five-second tier is half the price of its ten.

**No exploration tier.** The world is one location seen at five distances.
Five anchors cover it, and every still references one of them.

The remaining risk is not the plan, it is 7.2. It is the only shot in the
record that has to contain a living animal, and it is the shot the whole
thing is built toward. Working Agreements cap it: two failed takes and we
stop, report, and fall back to the shape at the edge of frame.

## Headroom

$10.22 expected against a $30 ceiling leaves about $19.80, or roughly:

- 28 Kling ten-second retakes, or
- 497 extra stills, or
- 660 anchor candidates

Comfortable enough that the honest risk is the opposite one: with this much
headroom it is easy to stop killing bad ideas at the stills stage. The rule
stands regardless of the balance — a rejected still costs $0.04, a rejected
Kling clip costs $0.70, seventeen times more.

## Batches needing confirmation

Working Agreements require sign-off on any batch over ~50 generations.

- **74 shot stills** across seven scenes — over the threshold as one batch.
  Run it scene at a time, as record 1 did: every batch stays under 50, and a
  failing anchor shows up after one scene instead of after all of them.
- 15 anchor candidates — under the threshold.

## Before stage 4

One piece of tooling is missing and is cheaper to write than to discover:
`gen_stills.py` skips any shot with `source: ffmpeg`, which is correct for a
shot that needs no plate at all, but shot 3.3 needs three (`plate_prompts` in
`shots.yaml`). Add that branch before running scene 3, or 3.3 will silently
generate nothing.

`scripts/build_cards.py` does not exist yet either. It is stage 8 work and
does not block generation, but `cards.yaml` is written and the plates for it
are framed, so it should be built before the plates are graded rather than
after.

## Actual

Fill in after each batch. If the episode runs past the ceiling, stop and
diagnose before spending more — per CLAUDE.md it is almost always a prompt
problem, not a model problem.

| Date | Stage | Batch | Spent | Running total |
|---|---|---|---:|---:|
| 2026-09-09 | 1–2 — script, shot list | no spend | $0.00 | $0.00 |
