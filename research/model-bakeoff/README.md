# Video model bake-off — 2026-10-26

Three shots the workhorse (Kling 2.5 Turbo Pro) had already failed, rolled
once each on three candidates from the same approved still and the same
prompt. Prompts and request bodies are in `bakeoff.py`; takes in `takes/`
(not versioned), the Kling 2.5 originals copied into `takes/ref/`.
Spent: **$9.39** (9 clips).

| | Kling 2.5 Turbo (ref) | Kling 3.0 Pro | Veo 3.1 Fast | Seedance 2.0 Fast |
|---|---|---|---|---|
| Price | $0.07/s | $0.112/s | $0.10/s | $0.2419/s |
| Output | 1904×1088 | 1904×1088 | **1920×1080** | 1280×720 |
| Lengths | 5 / 10 s | 3–15 s | 4 / 6 / 8 s | 4–15 s |
| Seed | no | no | yes | no |
| Camera drift (max px @480) | 0–60 | 0–2 | 0–1 | 0 |

## Per shot

**A — ep-08 1.1, meltwater film down an ice bore** (Kling 2.5: came back
still). Every candidate moved the water this time and none moved the camera.
Seedance showed the strongest runs on the left wall, as asked; Kling 3 and Veo
moved the wall too, more weakly. A film is still the weakest motion of the
three; the rule "water as a bead, drip or thread" stays.

**B — ep-05 1.3, fabric strap beside an empty suit** (Kling 2.5: stretched into
a festoon, changed hooks on every roll). Kling 3.0 and Seedance kept the strap
on its hook, its length and its shape, swaying in a narrow arc — the first
clean rolls of this shot in four attempts. Veo swung it like a ribbon in a
wind, far out from the wall: it stays one strap, but the motion is wrong for a
still room. No figure appeared in the suit on any model.

**C — ep-08 4.1, meltwater off an ice core onto a bench** (Kling 2.5: slid the
core 60 px along the bench and back). Seedance: the core does not move, the
pool on the steel spreads and drips fall off the bench edge — exactly the
prompt. Kling 3.0: a single thread runs down the core's end face into the
pool, core steady to 2 px; good. Veo: invented a spray of droplets thrown up
over the core in the first second, then good drips — a fault an eye catches.

## Reading

- **Kling 3.0 Pro is the replacement workhorse.** It fixed both failure modes
  that cost money on records 05 and 08 (soft objects re-drawn, the subject
  sliding), held the camera on all three, and costs 1.6× Kling 2.5 — about
  $1.12 per 10 s shot. Durations are free from 3 to 15 s, so a 7 s shot is
  billed as 7, which takes back part of the difference.
- **Seedance 2.0 Fast was the best behaved** (best C, clean B, best A) but
  delivers only 720p and costs 3.5× Kling 2.5 ($1.21 per 5 s). 1080p Seedance is
  $0.682/s. Candidate for the hero tier on shots where behaviour matters more
  than resolution; the 720p is upscaled by ffmpeg and sits under grain.
  Record 01's ban was on Seedance 1; version 2 is a different model.
- **Veo 3.1 Fast**: native 1920×1080 (no crop), a seed, cheap — and the only
  one that invented something unasked (C's spray) and overplayed a motion
  (B). Not the workhorse.

One roll per cell. This is evidence for a switch, not proof: record 09's
first scene on Kling 3.0 is the confirmation, and the two-failures rule
applies as before.
