# FC9-011 // THE MANIFEST — cost

Ceiling: $30.00.

## Estimate (stage 2, 2026-11-10, `scripts/estimate.py`)

| Item | Count | USD |
|---|---|---|
| Anchors, Seedream v4 (5 × 3 candidates) | 15 | 0.60 |
| Stills, Nano Banana edit | 66 | 2.63 |
| Video, Kling 3.0 Pro, audio off, $0.112/s | 8 shots, 73 s | 8.18 |
| **Base, zero retakes** | | **11.40** |
| +30% video retakes | | 13.86 |

Six model shots (3.1, 5.3, 6.1, 6.4, 8.2, 8.4) are `reuse_take` and never
generated. 3.1 was a paid pencil roll until 2026-11-10 — cut, see shots.yaml. Prices in `config/models.yaml` not yet re-checked against fal for
this record — do it before stage 6.

## Spend

| Date | Batch | USD |
|---|---|---|
| 2026-11-10 | Anchors pass 1, Seedream v4, 15 candidates | 0.60 |
| 2026-11-10 | Stills pass 1, Nano Banana edit, 30 saved (2.1 s22, 7.3 s22 refused by model) | 1.20 |
| 2026-11-10 | Stills reroll 1.1, 3.1 (new prompts; 3.1 moved to A3) | 0.16 |
| 2026-11-10 | Stills pass 2, 24 ref_shot dependents (7.3 s22 re-queued and refused again) | 0.96 |
| 2026-11-10 | Stills reroll 4.4, 6.2, 7.2, 8.1 (the word "strap" summoned straps) | 0.32 |
| 2026-11-10 | Takes, Kling 3.0 Pro audio off, 8 clips 73 s (+6 reuse cuts, free) | 8.18 |
| 2026-11-10 | Still reroll 2.3 pass 2 (hub at center, full-length needle) | 0.08 |
| 2026-11-10 | Take 2.3 roll 2 — WASTED: stale upload cache sent the rejected still (fixed: cache keys on content) | 0.90 |
| 2026-11-10 | Take 2.3 roll 2, from the new still | 0.90 |
| 2026-11-10 | Narration 27 paragraphs seed 11 + scene 2 on seed 22 (~2,700 chars); score 300 s, teaser cue 30 s, 5 spot effects — ElevenLabs subscription | 0.00 |
| 2026-11-10 | Spot effects reroll: cutoff (fixed, mid-band), knock (failed again: 35 Hz, -40 dBFS) — ElevenLabs subscription | 0.00 |
