# FC9-009 — cost

Prices checked 2026-10-26: Kling 3.0 Pro $0.112/s audio off (new workhorse,
`kling3`); Seedream v4 $0.04; Nano Banana edit $0.0398.

## Estimate (`scripts/estimate.py`)

| Item | Unit | Count | USD |
|---|---|---|---|
| Takes — Kling 3.0 Pro | $0.112 / s | 15 shots, 130 s | 14.56 |
| Stills | $0.0398 / image | 64 | 2.55 |
| Anchors | $0.04 / image | 15 | 0.60 |
| **Total, first rolls** | | | **17.71** |
| +30% video retakes | | | 22.08 |

The model-shot count is record 07's (15) at 1.6x the old per-second price,
which is where the record costs more than 08: the switch was bought for
behaviour (see `research/model-bakeoff/`), not for price.

## Spent

| Date | Stage | USD | Note |
|---|---|---|---|
| 2026-10-26 | Anchors, pass 1 | 0.60 | 5 anchors x 3 seeds. A4-topdown rejected in all three: a fold-down table seen from the front |
| 2026-10-26 | Anchors, A4 pass 2 | 0.12 | Flat-lay wording; reads as a flat plane |
| 2026-10-26 | Stills, scene 1 | 0.32 | 4 shots x 2 seeds. 1.4 s22 carries a readable nameplate |
| 2026-10-26 | Stills, scenes 2–8 | 1.84 | 46 images; 8 ref_shot stills held until their masters are approved |
| 2026-10-26 | Stills, 3.4 and 4.1 pass 2 | 0.16 | 3.4: wide anchor put the pencil at the far hatch; 4.1: no needle (s11), numbered scale (s22) |
| 2026-10-26 | Edit, flags off 3.1 / 6.2 | 0.08 | Nano Banana edit on the picked exteriors; the spine's "no flags" did not hold |
| 2026-10-26 | Stills, ref_shot repeats | 0.56 | 7 shots x 2 against approved 2.1, 2.4, 3.4, 4.1 |
| 2026-10-26 | Takes, scene 1 (Kling 3.0) | 1.68 | 1.1 5 s, 1.2 10 s. Both first roll, camera 0 px, both move as asked |
| 2026-10-26 | Takes, scene 2 (Kling 3.0) | 2.24 | 2.1 door closes and seats by ~6 s; 2.4 fan turns. First roll, camera 0–1 px |
| 2026-10-26 | Takes, scene 3 (Kling 3.0) | 1.68 | 3.1 Earth slides, boom still — ok. 3.4 pencil drifts right, but the hatch-three handwheel behind it turns ~45° unasked |
| 2026-10-26 | Take 3.4, roll 2 | 0.56 | Pencil now tumbles, but the wheel still re-draws between + and x, and the pencil grows a second point. Second failure: stopped |
| 2026-10-26 | Still 3.4, pass 3 | 0.08 | Pencil in front of a plain panel, hatch out of frame |
| 2026-10-26 | Take 3.4, roll 3 (plain panel) | 0.56 | Pencil drifts as one rigid object, no morph; it slides rather than tumbles |
| 2026-10-26 | Stills 6.3, 8.2 on the new 3.4 | 0.16 | s22 of both grew a drop of water on the pencil tip |
| 2026-10-26 | Takes, scene 4 (Kling 3.0) | 2.24 | 4.1 needle sweeps down to the ticks, ticks stay five; 4.4 lamp blinks. First roll, camera 0 px |
| 2026-10-26 | Takes, scene 5 (Kling 3.0) | 2.24 | 5.2 Earth slides past the window — ok. 5.5 needle never stops: sweeps all 10 s, past the last tick, the same move as 4.1 |
| 2026-10-26 | Take 6.3 (Kling 3.0) | 1.12 | Pencil tumbles end over end and drifts right; 183 px is the pencil, not the camera. 5.5 rebuilt as a free push |
| 2026-10-26 | Takes, scene 7 (Kling 3.0) | 2.24 | 7.2 door opens from ~6 s, wheel still — ok. 7.1 lever reaches vertical at ~4 s, then keeps spinning and turns double-ended |
| 2026-10-26 | Locked-off and local shots | 0.00 | 18 built by build_static.py |
| 2026-10-26 | Take 7.2, roll 2 | 1.12 | Start frame now 2.1's last frame — roll 1's generated still had the wheel shifted. Door opens from ~3 s. 3.3/5.4/5.5 re-based on take frames, rebuilt free |
| 2026-10-26 | Takes, scene 8 (Kling 3.0) | 1.12 | Started from take frames (6.3, 2.4 last frames). 8.2: background grows panel seams and a pale band. 8.4: frame drifts ~10 px and darkens. 7.1 kept as 4 s head x1.25, free |
| 2026-10-26 | 8.4 rebuilt from 2.4 | 0.00 | 2.4's take 5–10 s reused; the rolled 8.4 ($0.56) is in rejected. 8.2 kept as rolled |
| 2026-10-27 | Narration, ElevenLabs: 27 paragraphs x 3 seeds (character quota, ~6.7k chars) | ~0.30 | Median 167 wpm |
| 2026-10-27 | Alignment (27), music cue 270 s, 6 spot effects | ~0.80 | Cue mid-register, ~9 dB hotter than record 08's |
| 2026-10-27 | Teaser cue 30 s (music endpoint) | ~0.30 | Verticals, teaser, thumbnails built from existing takes and stills, free |
| | **Running total** | **~22.12** | |

The model bake-off ($9.39) is channel research, not this record's spend; it
is in `research/model-bakeoff/README.md`.

## Summary — record closed 2026-10-27

| Category | USD | Note |
|---|---|---|
| Anchors | 0.72 | 18 images, A4 in two passes |
| Stills and edits | 3.20 | 80 images incl. reworks and two flag edits |
| Video — Kling 3.0 Pro | 16.80 | 18 rolls, 13 kept; 8.4 reused from 2.4 |
| Audio — ElevenLabs | ~1.40 | 81 narration takes, alignment, cue, 6 effects, teaser cue |
| **Total** | **~22.12** | ceiling $30; estimate was 17.71 first-roll, 22.08 with retakes |

**Where the overrun went: $3.92 of rejected takes.** 3.4 rolls 1 and 2
($1.12 — a handwheel behind the pencil kept turning), 5.5 ($1.12 — the needle
would not stop), 7.2 roll 1 ($1.12 — started from a generated still whose
wheel had moved), 8.4 ($0.56 — started from a motion-blurred take frame).
Each one became a rule in CLAUDE.md the same day: still_from for an object at
rest, reuse_take for a repeated motion, Kling 3.0 does not stop a motion.

**What was free and worth it:** 18 locked-off and local shots, 5.5 as a push
on a take frame, 7.1 kept as its clean 4 s head, 8.4 cut from 2.4, the pencil
marks on 3.2 and 4.3, the verticals, the teaser picture and the thumbnails.

Model bake-off ($9.39) is channel research, not in this total
(`research/model-bakeoff/README.md`).
