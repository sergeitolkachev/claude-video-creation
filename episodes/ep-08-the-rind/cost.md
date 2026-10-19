# Cost — record 8

Prices from `config/models.yaml`, re-checked against fal on 2026-10-19:
Kling 2.5 Turbo Pro unchanged ($0.35 / 5 s, $0.07 each further second);
Seedream v4 raised to $0.04 in the config (fal's own article says $0.04, a
tracker still says $0.03 — budgeted at the higher); Nano Banana edit $0.04.

## Estimate

| Stage | Unit | Count | USD |
|---|---|---|---|
| Anchors, pass 1 | $0.04 / candidate | 4 anchors × 3 seeds | 0.48 |
| Anchors, further passes | $0.04 / candidate | pass 2 on 3 anchors, budget one more | 0.72 |
| Stills | $0.0398 / image | 30 anchored shots × 2 | 2.39 |
| Stills, ref_shot (6.1 on 4.1) | $0.0398 / image | 1 × 2 | 0.08 |
| Takes — Kling 10 s | $0.70 | 6 | 4.20 |
| Takes — Kling 5 s | $0.35 | 3 | 1.05 |
| Shots built in ffmpeg | — | 22 | 0.00 |
| Narration | ElevenLabs | 19 paragraphs × 3 seeded takes | ~0.30 |
| Music cue (261 s) | ElevenLabs music endpoint | 1, budget a second roll | ~0.60 |
| Spot effects, alignments | ElevenLabs | 4 effects | ~0.10 |
| Teaser music | ElevenLabs music endpoint | 1 cue | ~0.30 |
| **Total, first rolls** | | | **~10.22** |

Rerolls are not in the total. Record 05 ran 19 rolls for 13 model shots; the
same ratio here is ~4 extra rolls, up to ~$2.80 more.

The cheapest video line on the channel: 9 of 31 shots are Kling, and eight of
those nine move water or bubbles over rigid ice, which is the reliable class.
The risk is the opposite of cost — monotony — and it is judged at the stills.

## Spend

| Date | What | Count | USD |
|---|---|---|---|
| 2026-10-19 | Anchors pass 1 (A1, A2, A3, A5 × s11/s22/s33) | 12 | 0.48 |
| 2026-10-19 | Anchors pass 2 (A1, A3, A5 × s11/s22/s33) | 9 | 0.36 |
| 2026-10-19 | Stills scene 1 (4 shots × 2; 1.3_s11 returned nothing) | 8 | 0.28 |
| 2026-10-19 | Stills 1.3 pass 2 (dragonfly in pass 1) | 2 | 0.08 |
| 2026-10-19 | Stills scenes 2–3 | 16 | 0.64 |
| 2026-10-19 | Stills scene 4, first run — hung on a download with no timeout; 1 saved, the rest queued and lost with the process (est.) | 8 | ~0.32 |
| 2026-10-19 | Stills scenes 4–8, rerun (6.1 held for 4.1) | 35 | 1.40 |
| 2026-10-19 | Stills pass 2, text-only (2.2, 2.3, 4.4, 5.4, 5.5, 6.2 × 4 seeds) | 24 | 0.96 |
| 2026-10-19 | Stills 6.1 on 4.1, pass 1 (read as an eye) and pass 2 (mass off centre) | 4 | 0.16 |
| 2026-10-19 | Takes, Kling first rolls: 6 × 10 s, 3 × 5 s. Kept 2.3, 4.4, 6.1, 6.4, 8.2; 1.1 and 3.1 came back still, 4.1 slid the core along the bench, 5.3 breathes in and out | 9 | 5.25 |
| 2026-10-19 | Narration, ElevenLabs: 19 paragraphs × 3 seeds (character quota, ~7.4k chars) | 57 | ~0.30 |
| 2026-10-19 | Music cue 261 s (music endpoint) + 4 spot effects (sound endpoint) | 5 | ~0.40 |
| 2026-10-19 | Forced alignment (19 paragraphs) + teaser cue 30 s, ElevenLabs | 20 | ~0.15 |
| | **Running total** | | **~10.78** |
