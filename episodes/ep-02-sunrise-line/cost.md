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
| Workhorse video — Kling 2.5 Turbo Pro | 14 | 125 | $8.75 | |
| Local shots — drift or push, built in ffmpeg | 12 | — | $0.00 | |
| Static shots — card plates, lens breathing only | 8 | — | $0.00 | |
| Shot 3.3 — three-plate dissolve, ffmpeg | 1 | — | $0.00 | |
| Shot stills — Nano Banana | 88 | — | $3.50 | $6.19 |
| Anchors — Seedream V4, 5 passes | 15+ | — | $0.45 | $1.35 |
| **Base, zero retakes** | | | **$12.70** | |
| Reserve, +30% on video | | | $2.63 | |
| **Expected** | | | **$15.33** | |

The video line tripled after record 01's motion lesson was written into
CLAUDE.md: 26 of 30 shots locked off is a slideshow, and the saving came out
of the episode rather than out of the budget. Here 14 shots go to Kling — every
shot that runs under silence, and every shot where dust, water, frost or haze
should actually move — 12 get a local drift or push, and only 8 are frozen,
all of them carrying a data card the viewer is reading.

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

## The track problem

Scene 3 is the first scene whose subject is the animal's tracks, and both
ways of generating one failed on the same pass.

**With the A3 anchor**, 3.1 and 3.2 came back carrying A3's ribbed tread band
across the frame, and 3.1's "broad shallow track with a soft rounded rim"
became a two-metre raised ring. The anchor was approved with that tread band
known and recorded; scene 3 is where it stops being cosmetic.

**Without an anchor**, 3.3a defaulted to human and vehicle prints — a tyre
rut receding to the sun in one seed and a lug-soled boot print in another,
which is exactly the failure CLAUDE.md predicts for the word "footprint".

**Third route, text-to-image plus a written canon.** The canon did what it
was written to do — no boot soles, no tyre marks, no toes — and then
overshot: "a smooth oval depression with a rim of displaced soil" came back
as a moulded bowl set into the ground, too circular, too clean, and read at
the wrong scale because nothing in the frame gives one. A5 pass 5 of the
anchor failed separately: the added negations pushed the prompt long enough
that the nadir geometry was dropped and the tread survived anyway.

**Fourth route, canon v2: scale and texture, negations kept.** All four seeds
returned the imprint of a tracked vehicle — the deep lugged belt of an
excavator pressed into the clay. The canon says "no tread, no lugs, no ribs,
no grooves" and the model drew tread, lugs, ribs and grooves. This is record
1's "no signage" lesson at full strength: a negation list is a list of nouns,
and nouns in a prompt are things to draw.

There is a second suspect, which is the English word itself. "Track" is a
vehicle word — tyre track, tracked vehicle, track marks — and it has been in
every prompt in this family from the beginning, including the ones that
returned tyre ruts. "Print" and "impression" carry no machine sense.

What was tried and what it cost:

| Route | Result | Cost |
|---|---|---|
| A3 anchor as reference | anchor's ribbed tread band in every frame | $0.40 |
| A3 anchor reshot, pass 5 | negations cost the nadir, tread survived | $0.09 |
| text-to-image, canon v1 (shape) | moulded ceramic bowl in the ground | $0.36 |
| text-to-image, canon v2 (material) | excavator belt imprint, all four seeds | $0.12 |
| text-to-image, canon v3 (no negations, "print") | lugged boot print, all four seeds | $0.12 |

**Five routes, $1.09, and the conclusion is about the subject rather than the
prompt.** A single discrete mark in soft ground has exactly two strong
attractors in this model's training, a boot and a tyre, and every word
available to name the thing points at one of them: "track" returns a tracked
vehicle or a tyre rut, "print" returns a boot sole, describing the shape
returns a moulded bowl, and referencing the anchor returns the anchor's own
ribbed band. Naming what it must not be draws that thing instead.

What this world does render, reliably and on the first pass, is **bands**:
2.1, 2.4, 2.5 and 3.4 all landed immediately, and every one of them is a
stripe of one material against a stripe of another. So the animal's passage
is shown as a band of disturbed ground rather than as an imprint — which is
also the truer image, since an animal that never stops walking leaves a
continuous trail, not a row of separate marks.

The rewrite landed on the first pass: twelve candidates, no boot, no tyre, no
bowl, and three of the four seeds usable on every shot. $1.09 was spent
finding out that the subject was wrong, and $0.52 fixing it.

The dissolve plates are the other thing that worked exactly as record 1 said
they would. 3.3b and 3.3c were generated against the **approved** 3.3a rather
than against an anchor, and came back as the same band in the same frame with
only the moisture changed — which is the whole point of `ref_shot:`, and the
reason the drying sequence reads as one patch of ground instead of three.

What is left to try is scale and texture rather than shape — the print floored
with the same soil and the same cracks as everything around it, edges
crumbled and asymmetric, shot from directly above with no horizon in frame to
argue about size.

Both point at the same gap: nothing in this repository has ever said what
this animal's track actually looks like. It is described by what it is not.
The fix is a positive description reused verbatim in every shot that shows
one — a smooth oval depression the size of a dinner plate, soft rounded rim,
no toes, no claws, no tread, no ridges — plus a clean A3.

## The animal has no legs

Found while reviewing 7.2, after five prompt routes had been spent on
the trail: **a legged animal cannot leave a continuous band.** It leaves
separate prints. Every failure in scene 3 was the model correctly drawing the
animal the storyboard had described, into a world whose ground said something
else.

The body plan was the part that had never actually been decided, so it was
decided last and by the evidence: one long low body lying flat against the
ground, no limbs, moving on its underside, leaving a band exactly as wide as
itself. It renders for the same reason every landed shot in this episode
renders — it is a stripe. The animal has the same shape as its own trail.

It also settles the 7.2 problem permanently. There is no familiar silhouette
to fall into, so the horned cow of the first pass and the near-wildebeest of
the second cannot recur.

Two words of narration changed: "keeps the legs going" became "keeps it
moving", and "as their stride lengthens" became "as they lengthen" — which is
now literal, since a longer body leaves a wider band, and the aerial 5.1 shows
a broad trail and a thin one side by side.

Taylor's cost-of-transport allometry is measured on legged runners. A body
moving on its underside pays more per metre, not less, so the 24 MJ/day figure
is now stated as a conservative floor rather than an estimate. The narration
says "about" and never totals anything beyond 40, so no number on screen
changed.

## Actual

Fill in after each batch. If the episode runs past the ceiling, stop and
diagnose before spending more — per CLAUDE.md it is almost always a prompt
problem, not a model problem.

| Date | Stage | Batch | Spent | Running total |
|---|---|---|---:|---:|
| 2026-09-09 | 1–2 — script, shot list | no spend | $0.00 | $0.00 |
| 2026-09-09 | 3 — anchors | 15 candidates, pass 1 | $0.45 | $0.45 |
| 2026-09-09 | 3 — anchors | 15 candidates, pass 2, sky and infrastructure fixed | $0.45 | $0.90 |
| 2026-09-09 | 3 — anchors | 9 candidates, pass 3, A1/A2/A3 only | $0.27 | $1.17 |
| 2026-09-09 | 3 — anchors | 6 candidates, pass 4, A3/A4 nadir geometry | $0.18 | $1.35 |
| 2026-09-09 | 3 — anchors | **approved:** A1 p3 s11, A2 p3 s33, A3 p4 s22, A4 p4 s22, A5 p2 s33 | — | $1.35 |
| 2026-09-09 | 4 — stills | scene 1, 8 generations | $0.32 | $1.67 |
| 2026-09-09 | 4 — stills | 1.2 reworked, dust brought close to camera, 2 | $0.08 | $1.75 |
| 2026-09-09 | 4 — stills | **approved:** 1.1 s11, 1.2 s11, 1.3 s22, 1.4 s22 — scene 1 complete | — | $1.75 |
| 2026-09-09 | 4 — stills | scene 2, 10 generations | $0.40 | $2.15 |
| 2026-09-09 | 4 — stills | 2.5 reworked, causeway and people removed, 2 | $0.08 | $2.23 |
| 2026-09-09 | 4 — stills | **approved:** 2.1 s11, 2.2 s11, 2.3 s11, 2.4 s11 — 2.5 held | — | $2.23 |
| 2026-09-09 | 4 — stills | 2.5 rewired to the aerial anchor, 2 | $0.08 | $2.31 |
| 2026-09-09 | 4 — stills | **approved:** 2.5 s22 — scene 2 complete | — | $2.31 |
| 2026-09-09 | 4 — stills | scene 3, 10 generations | $0.40 | $2.71 |
| 2026-09-09 | 4 — stills | **approved:** 3.4 s22. 3.1, 3.2, 3.3a rejected — see below | — | $2.71 |
| 2026-09-09 | 3 — anchors | A3 pass 5, failed: negations cost the nadir, tread stayed | $0.09 | $2.80 |
| 2026-09-09 | 4 — stills | 3.1/3.2/3.3a on text-to-image with the track canon, 12 | $0.36 | $3.16 |
| 2026-09-09 | 4 — stills | 3.1 with canon v2, failed: four tracked-vehicle prints | $0.12 | $3.28 |
| 2026-09-09 | 4 — stills | 3.1 with canon v3, failed: four boot prints | $0.12 | $3.40 |
| 2026-09-09 | 4 — stills | storyboard changed to bands; 3.1/3.2/3.3a, 12 | $0.36 | $3.76 |
| 2026-09-09 | 4 — stills | 3.3b/3.3c against the approved 3.3a, 4 | $0.16 | $3.92 |
| 2026-09-09 | 4 — stills | **approved:** 3.1 s44, 3.2 s11, 3.3a s11, 3.3b s22, 3.3c s11 — scene 3 complete | — | $3.92 |
| 2026-09-09 | 4 — stills | scene 4, 16 generations (4.1/4.5 routed off A3) | $0.56 | $4.48 |
| 2026-09-09 | 4 — stills | 4.2 and 4.6 reworked, 4 | $0.16 | $4.64 |
| 2026-09-09 | 4 — stills | **approved:** 4.1 s11, 4.2 s22, 4.3 s22, 4.4 s11, 4.5 s44, 4.6 s11 — scene 4 complete | — | $4.64 |
| 2026-09-09 | 4 — stills | scene 5, 16 generations | $0.56 | $5.20 |
| 2026-09-09 | 4 — stills | 5.5/5.6 re-pitched by distance, 5.2 against approved 5.1, 10 | $0.32 | $5.52 |
| 2026-09-09 | 4 — stills | **approved:** 5.1 s22, 5.2 s11, 5.3 s44, 5.4 s22, 5.5 s11, 5.6 s22, 5.7 s11 — scene 5 complete | — | $5.52 |
| 2026-09-09 | 4 — stills | scenes 6 and 7, 14 generations | $0.52 | $6.04 |
| 2026-09-09 | 4 — stills | 7.2 re-pitched off the bovine silhouette; 6.3 and 7.3 against approved plates, 6 | $0.24 | $6.28 |
| 2026-09-09 | 4 — stills | **approved:** 6.1 s22, 6.2 s11, 6.3 s11, 6.4 s22, 7.1 s11, 7.2 s22, 7.3 s11, 7.4 s11 | — | $6.28 |
| 2026-09-09 | 4 — stills | **stage 4 closed — 36/36 plates approved, 34 shots** | — | $6.28 |
| 2026-09-09 | 4 — stills | 7 debug probes chasing a 401 that was a local variable shadowing the API key | $0.28 | $6.56 |
| 2026-09-09 | 4 — stills | 7.2 regenerated on the creature canon, 2 | $0.08 | $6.64 |
| 2026-09-09 | 4 — stills | **approved:** 7.2 s22 — the legless body | — | $6.64 |
| 2026-09-09 | 6 — takes | 20 local shots built in ffmpeg, incl. the 3.3 dissolve | $0.00 | $6.64 |
| 2026-09-09 | 6 — takes | scene 1: 1.2, 1.4 | $1.40 | $8.04 |
| 2026-09-09 | 6 — takes | scenes 2, 4, 5: 2.1, 2.2, 2.5, 4.3, 4.4, 4.6, 5.2, 5.3, 5.7 | $6.30 | $14.34 |
| 2026-09-09 | 6 — takes | scenes 6, 7: 6.4, 7.1, 7.2 | $1.05 | $15.39 |
| 2026-09-09 | 6 — takes | 5.3 retaken — first take drifted orange and grew a blue sky | $0.70 | $16.09 |
| 2026-09-09 | 6 — takes | **stage 6 closed — 34/34 shots, 272.00 s** | — | $16.09 |
