# Cost — ep-03-carbon-balance

Ceiling: **$30**, the same as records 1 and 2.

Prices in `config/models.yaml` were verified against fal on 2026-09-08 and
have not been re-probed since. **Re-probe before stage 6** — that is where the
money is, and a stale price there is worth more than a stale price anywhere
else. Everything before stage 6 is cents.

Regenerate the plan column with `scripts/estimate.py episodes/ep-03-carbon-balance`.

## Plan

| Item | Count | Sec | Planned | Actual |
|---|---:|---:|---:|---:|
| Workhorse video — Kling 2.5 Turbo Pro | 12 + 2 retakes | 85 | $5.95 | **$6.65** |
| Local shots — drift or push, built in ffmpeg | 8 | — | $0.00 | |
| Static shots — card plates, lens breathing only | 7 | — | $0.00 | |
| Closing card block — composed on black | 1 | — | $0.00 | |
| Shot stills — Nano Banana | 80 | — | $2.31 | **$3.16** |
| Anchors — Seedream V4, three passes | 33 | — | $0.45 | **$0.99** |
| **Base, zero retakes** | | | **$8.71** | |
| **Actual, stages 3–6 complete** | | | | **$10.80** |
| Reserve, +30% on video | | | $1.78 | |
| **Expected** | | | **$10.49** | |

The Kling line splits five ten-second clips ($0.70 each) against seven
five-second ($0.35). Nothing is billed at a length it does not use: the model
tier prices 5 s and 10 s only, so every `model` shot in `shots.yaml` is exactly
5 or 10 seconds of timeline and there is no trimmed remainder being paid for.
Record 02 bought one five-second clip for a four-second shot and noted it;
record 03 has none of those.

Narration comes out of the ElevenLabs subscription, not this budget. 260 words
is about 1 500 characters against a 35 903 character monthly allowance; at
three seeded takes per paragraph that is roughly 4 500, comfortable.

## Where this sits against the first two records

Record 1 spent $18.28. Record 2 planned $15.33 and put fourteen shots through
Kling after record 1's motion lesson was written into CLAUDE.md. Record 3
plans $10.49 with twelve, and the difference is not a cheaper model and not
more frozen frames — 71% of shots move here against record 2's 76%, which is
the same record.

It is shorter. 220 s against 279 s, for the same kind of episode, because the
draft's 4:20 was 60% silence and the Motion Policy prices silence at Kling
rates. Forty seconds came out of the body and no narration was cut.

The exploration tier is unused, as in record 2. One location at five distances;
five anchors cover it and every still references one of them.

## The batch that needs confirming

**58 stills in one run is over the ~50 threshold in Working Agreements and gets
confirmed before it goes.** It is $2.31, so the confirmation is not about the
money — it is about not discovering a systematic prompt fault 58 images in.
Run scene 1 first (3 shots, 6 stills, $0.24), look at what comes back, and only
then release the rest.

The specific thing to look for in that first scene: the three paper shots
(2.3, 5.1, 6.1) are prompted as texture precisely so that no model invents
lettering, and 1.3 is the first plate that shares their top-down anchor. If A4
comes back with writing on the bench, the anchor is wrong and every card plate
in the record is wrong with it.

## Risks, in the order they cost money

**The anchors — settled, $0.99 against a planned $0.45.** Three passes. Pass 1
lost A3 and A4 to the spine: "Interior of an orbital relay station" built a
room inside both close distances, and naming the work lamp — in a sentence
whose whole purpose was to restrict where it appeared — put the lamp in eight
of fifteen candidates. Pass 2 fixed A1, A2, A3 and A5 with a second spine that
contains no room noun. Pass 3 was A4 alone and failed a third time: Seedream
does not render an orthographic top-down texture study, and every negation in
that prompt came back as its own object — the forbidden grit banked along the
edges, the forbidden rim drawn in, a background invented behind it. A4 is
retired rather than paid for a fourth time. See the note on the anchor.

Record 2 spent four passes and $1.35 on five anchors. This is $0.99 on four,
which is the same shape: anchors are the cheapest place in the pipeline to be
wrong, and the only place where being wrong three times still costs under a
dollar.

**Shot 6.3.** Ten seconds of a dark hatch with dust moving in a thin spill of
light, no voice and no card — the centre of the record. It is the shot most
likely to come back either dead (nothing visibly moving, which makes it a
frozen frame that cost $0.70) or alive in the wrong way (the hatch opening,
light changing, something entering frame). Its `video_prompt` says the hatch
does not move and nothing opens, and `motion_tail_moving` says it again.
Working Agreements cap it: two failed takes and we stop and report.

**Shots 3.3 and 5.2,** the phosphor monitors. A model asked for a line on a
screen will happily animate a different line, or letter the axes. Both are
five-second clips, so a retake is $0.35 and the fallback is cheap: build them
as `local` from the approved still with the line already in the right place,
and lose nothing but four seconds of motion.

## Headroom

$10.49 expected against a $30 ceiling leaves about $19.50, or roughly:

- 27 Kling ten-second retakes, or
- 55 Kling five-second retakes, or
- 490 shot stills, or
- four complete re-runs of every anchor at five seeds.

Which is to say the budget is not the constraint on this record. Selection time
is.


## Actual — stages 3 to 6 closed

**$10.80 against a planned $10.49.** Three per cent over, and the overrun is
entirely in the two places the plan named as risks: anchors took three passes
instead of one, and stills took 80 generations instead of 58.

Where the extra went, in order of size:

- **$0.85 of stills** on rerouting. Four shots had to leave the anchor set
  entirely — three paper shots and the porthole — and four more were
  regenerated after the first pass returned lettering, a terrestrial workshop,
  or a product render with no wear on it. Every one of those was a wrong
  distance or a wrong word in a prompt, not a bad roll.
- **$0.54 of anchors** on two extra passes, both of them the same lesson: a
  spine that opens "Interior of an orbital relay station" builds a room in
  every frame, and a spine that names an object puts the object in every frame.
- **$0.70 of Kling** on two retakes, one of which was not needed. 4.3 opened a
  hatch that had to stay shut and was fixed on the second roll. 5.4 bloomed its
  work lamp, was rerolled, came back worse — and then luminance sampling showed
  the *first* take was flat for four full seconds and only blew out in the
  fifth. The shot is cut to four. That $0.35 buys the rule: measure where a
  fault starts before paying for another roll of a clip that has no seed.

**Video came in on plan.** Twelve clips, no shot billed at a length it does not
use, and the two retakes were the entire variance. The $1.78 reserve covered
them twice over.

$19.20 of the $30 ceiling is unspent, and nothing costed remains — narration
runs off the ElevenLabs subscription and everything after it is ffmpeg.
