# Cost — ep-01-tishina-9

Ceiling: **$30**. Prices verified 2026-09-08, see `config/models.yaml`.
Regenerate the plan column with `scripts/estimate.py`.

## Plan

| Item | Count | Sec | Planned | Actual |
|---|---:|---:|---:|---:|
| Filler video — Seedance Pro Fast 1080p | 18 | 139 | $6.76 | |
| Workhorse video — Kling 2.5 Turbo Pro | 11 | 110 | $7.70 | |
| Shot 6.1 — built in ffmpeg | 1 | — | $0.00 | |
| Shot stills — Nano Banana, 2-4 per shot | 87 | — | $3.46 | $4.28 (incl. reworks) |
| Anchors — Seedream V4, 3 per anchor | 12 | — | $0.36 | $1.08 (3 passes) |
| **Base, zero retakes** | | | **$18.28** | |
| Anchor overrun, 2 extra passes | | | +$0.72 | |
| Reserve, +30% on video | | | $4.33 | |
| **Expected** | | | **$22.61** | |

Narration, SFX and music come out of the ElevenLabs subscription, not this
budget. Episode 01 needs 1 793 characters of narration against a 35 903
character monthly allowance.

## Where the money actually goes

Two decisions account for most of the number.

**The filler tier is billed by the second, the workhorse tier is not.**
Seedance Pro Fast accepts any length from 2 to 12 seconds, so an 8 second
shot costs 8 seconds. Kling only makes 5 or 10 second clips, so a 7 second
shot is billed as 10 and trimmed. Six of the eleven workhorse shots are paid
at 10 seconds and cut shorter — about $1.20 of deliberate waste, spent on
the shots where the camera actually moves.

**Wan is not the cheap option at our resolution.** fal's pricing page lists
Wan 2.5 at $0.05/s, but that is the 480p tier; at 1080p it is $0.15/s, three
times Seedance Pro Fast. Reading the headline number would have put the
filler tier at $27 on its own and blown the ceiling before a single still.

## Headroom

$22.61 expected against a $30 ceiling leaves about $7.40, or roughly:

- 21 filler retakes, or
- 10 workhorse retakes, or
- 186 extra stills

Moving one shot from filler to workhorse costs $0.31 to $0.35. Moving the
whole filler tier there would cost $12.60 instead of $6.76 and put the
expected total at $30.36 — over the ceiling before any retakes. The
filler/workhorse split is the budget.

## Batches needing confirmation

Working Agreements require sign-off on any batch over ~50 generations.

- **87 shot stills** (29 shots x 3 candidates) — over the threshold, confirm
  before running. Splitting it per scene keeps every batch under 50 and gives
  an earlier read on whether the anchors are holding.
- 12 anchor candidates — under the threshold.

## Actual

Fill in after each batch. If the episode runs past the ceiling, stop and
diagnose before spending more — per CLAUDE.md it is almost always a prompt
problem, not a model problem.

| Date | Stage | Batch | Spent | Running total |
|---|---|---|---:|---:|
| 2026-09-08 | 3 — anchors | 12 candidates, Seedream V4, pass 1 | $0.36 | $0.36 |
| 2026-09-08 | 3 — anchors | 12 candidates, pass 2, shared style spine | $0.36 | $0.72 |
| 2026-09-08 | 3 — anchors | 12 candidates, pass 3, spine split from camera | $0.36 | $1.08 |
| 2026-09-08 | 3 — anchors | **approved:** A1 s33, A2 s33, A3 s33, A4 s11 | — | $1.08 |
| 2026-09-08 | 4 — stills | scene 2, 18 generations (3 failed on 2.6) | $0.72 | $1.80 |
| 2026-09-08 | 4 — stills | debugging the 2.6 failure, 8 probes | $0.32 | $2.12 |
| 2026-09-08 | 4 — stills | scene 2 shot 2.6 regenerated, 3 | $0.12 | $2.24 |
| 2026-09-08 | 4 — stills | **approved:** 2.1 s22, 2.2 s33, 2.4 s33, 2.5 s11, 2.6 s22 | — | $2.24 |
| 2026-09-08 | 4 — stills | shot 2.3 reworked to the dish alone, 4 | $0.16 | $2.40 |
| 2026-09-08 | 4 — stills | **approved:** 2.3 s44 — scene 2 complete | — | $2.40 |
| 2026-09-08 | 4 — stills | scene 5, 18 generations | $0.68 | $3.08 |
| 2026-09-08 | 4 — stills | **approved:** 5.1 s11, 5.4 s11, 5.5 s33 | — | $3.08 |
| 2026-09-08 | 4 — stills | 5.2/5.6 rewired to A2, 5.3 exterior spine, 5.7 silhouette | $0.36 | $3.44 |
| 2026-09-08 | 4 — stills | 5.6 reworked to raking light, 2 | $0.08 | $3.52 |
| 2026-09-08 | 4 — stills | scene 3, 16 generations | $0.64 | $4.16 |
| 2026-09-08 | 4 — stills | 3.3 reworked with pencil crossings, 4 | $0.16 | $4.32 |
| 2026-09-08 | 4 — stills | scene 1, 6 generations | $0.24 | $4.56 |
| 2026-09-08 | 4 — stills | **approved:** 13 stills, scenes 1/3/5 | — | $4.56 |
| 2026-09-08 | 4 — stills | scene 4, 14 generations | $0.56 | $5.12 |
| 2026-09-08 | 4 — stills | scene 6, 4 generations | $0.16 | $5.28 |
| 2026-09-08 | 4 — stills | 4.3 reworked to a clean plate, 2 | $0.08 | $5.36 |
| 2026-09-08 | 4 — stills | **stage 4 closed — 29/29 approved** | — | $5.36 |
| 2026-09-08 | 6 — takes | 2.1 probe, camera_fixed ignored | $0.34 | $5.70 |
| 2026-09-08 | 6 — takes | 2.1 retry, explicit locked-off wording, worse | $0.34 | $6.04 |
| 2026-09-08 | 6 — takes | 2.1 Kling probe, 10 s | $0.70 | $6.74 |
| 2026-09-08 | 6 — takes | duplicate Kling submit, cancelled locally after the API accepted it — assume billed | $0.70 | $7.44 |
| 2026-09-08 | 6 — takes | 2.1 built in ffmpeg from the approved still | $0.00 | $7.44 |
| 2026-09-08 | 6 — takes | 2.5 Seedance drift probe | $0.34 | $7.78 |
| 2026-09-08 | 6 — takes | **16 locked-off shots built in ffmpeg** | $0.00 | $7.78 |
| 2026-09-08 | 6 — takes | 2.5/3.6/4.6 moved to Kling; Seedance dropped from the episode | — | $7.78 |
| 2026-09-08 | 6 — takes | scene 2: 2.2 and 2.5 on Kling | $1.40 | $9.18 |
| 2026-09-08 | 6 — takes | scenes 1/3/4: 1.2, 3.1, 3.2, 3.6, 4.3, 4.5, 4.6 | $4.90 | $14.08 |
| 2026-09-08 | 6 — takes | scene 5: 5.2, 5.3, 5.5 | $2.10 | $16.18 |
| 2026-09-08 | 6 — takes | 5.7 first submit — poll hung on a socket with no timeout, request id lost with the unflushed log; assume billed | $0.70 | $16.88 |
| 2026-09-08 | 6 — takes | 5.7 resubmitted after the script was fixed | $0.70 | $17.58 |
| 2026-09-08 | 6 — takes | 6.1 built in ffmpeg, blink keyframed | $0.00 | $17.58 |
| 2026-09-08 | 6 — takes | 4.3 rebuilt locally with a controlled drift | $0.00 | $17.58 |
| 2026-09-08 | 6 — takes | 5.1 moved to Kling — a frozen hand read as a freeze-frame | $0.70 | $18.28 |
| 2026-09-08 | 6 — takes | **stage 6 closed — 30/30 shots, 250.00 s** | — | $18.28 |
| 2026-09-08 | 7 — audio | narration 24 paragraphs x3 takes, hum, relay, drone | $0.00 | $18.28 |
| 2026-09-08 | 8 — post | grade, grain, titles, screen readouts | $0.00 | $18.28 |
| 2026-09-08 | 8 — post | **master rendered — 279 MB, 1920x1080, 250.00 s** | — | $18.28 |
