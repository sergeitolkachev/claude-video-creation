# FC9-010 // THE CEILING — cost

Ceiling: $30.00.

## Estimate (stage 2, 2026-11-04, `scripts/estimate.py`)

| Item | Count | USD |
|---|---|---|
| Anchors, Seedream v4 (6 × 3 candidates) | 18 | 0.72 |
| Stills, Nano Banana edit | 64 | 2.55 |
| Video, Kling 3.0 Pro, audio off, $0.112/s | 11 shots, 88 s | 9.86 |
| **Base, zero retakes** | | **13.13** |
| +30% video retakes | | 16.09 |

`estimate.py` prints $13.80 / $16.95 because it counts 8.2 as a 6 s Kling
roll; 8.2 is `reuse_take` of 1.4 and is never generated ($0.67 less).

Prices checked 2026-11-04: Kling 3.0 Pro is listed by fal at $0.112/s with
audio off, matching `config/models.yaml`. The still and anchor rates in the
config ($0.04) sit at or slightly above fal's listed Nano Banana ($0.039) and
Seedream 4.0 ($0.03) prices, so the estimate is conservative there.

## Spend

| Date | Batch | Generations | USD | Running |
|---|---|---|---|---|
| 2026-11-04 | Anchors pass 1, Seedream v4, 6 × 3 | 18 + 5 | 0.92 | 0.92 |
| 2026-11-04 | Anchors pass 2, A1/A2/A4/A6 × 3 | 12 | 0.48 | 1.40 |
| 2026-11-04 | Stills wave 1, Nano Banana, 25 shots × 2 | 38 of 44 | 1.52 | 2.92 |
| 2026-11-04 | Stills pass 2 + wave 2 (2.4 3.2 4.4 5.1 5.2 5.4 6.4 7.2 7.3 8.4) | 24 | 0.96 | 3.88 |
| 2026-11-04 | Stills 5.3 (ref 4.4), 7.3 pass 2 (edit of 3.4) | 4 | 0.16 | 4.04 |
| 2026-11-04 | Stills 7.3 pass 3, Seedream text-only, overcast spine | 4 | 0.16 | 4.20 |
| 2026-11-04 | Takes scene 1, Kling 3.0 Pro: 1.1 (8 s), 1.4 (6 s) | 2 | 1.57 | 5.77 |
| 2026-11-05 | Takes scene 2, Kling 3.0 Pro: 2.3 (8 s) | 1 | 0.90 | 6.67 |
| 2026-11-05 | Takes scene 3, Kling 3.0 Pro: 3.2 (10 s, rejected), 3.4 (10 s) | 2 | 2.24 | 8.91 |
| 2026-11-05 | Take 5.4, Kling 3.0 Pro, pump pass 2 (6 s) | 1 | 0.67 | 9.58 |
| 2026-11-05 | Take 4.1, Kling 3.0 Pro, flight (8 s) | 1 | 0.90 | 10.48 |
| 2026-11-05 | Takes 5.1 (8 s), 6.1 (8 s), 6.4 (6 s), 7.3 (10 s) | 4 | 3.59 | 14.07 |
| 2026-11-05 | Still 8.2, Seedream text-only, overcast spine | 4 | 0.16 | 14.23 |

Pass 1 paid for 23 images to get 18: the first run died on a poll timeout
after 13 saves with five requests already queued and their ids lost, so the
five were queued again ($0.20 wasted). `gen_anchors.py` now retries a dropped
read instead of dying.

Wave 1: six requests came back 422 `no_media_generated` (1.3, 1.4, 2.1, 2.3,
4.4, 5.4 — one seed each), counted here as unbilled; not checked against
the fal dashboard. Every shot has at least one candidate.

Pass 2 / wave 2: `gen_stills.py` died twice on a status-poll TimeoutError —
its `get()` had no retry, the same fault fixed in `gen_anchors.py` an hour
earlier and not looked for elsewhere. 5.4 and 7.3 were recovered from the
request ids in the log at no cost. The first 7.2 run died while queueing and
printed no ids: if fal accepted those four requests, up to $0.16 more was
spent and cannot be collected. `get()` now retries a dropped read.

6.1 was first marked rejected (24 px push-in, marks on the drum strip);
Serge kept it as rolled on 2026-11-05.
