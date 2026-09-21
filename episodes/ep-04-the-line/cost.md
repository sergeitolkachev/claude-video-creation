# Record 4 — "THE LINE": cost

Ceiling $30. Estimated before anything was spent, from `scripts/estimate.py`
against `shots.yaml`, at the prices in `config/models.yaml` (verified against
fal 2026-09-14 — re-check before stage 6).

## Estimate, stage 2

| Tier | Count | Seconds | USD |
|---|---|---|---|
| Video — workhorse (Kling) | 15 shots | 125 | 8.75 |
| Built in ffmpeg (static + local) | 16 shots | 145 | 0.00 |
| Shot stills (Nano Banana edit) | 64 | — | 2.55 |
| Anchors (Seedream t2i, 3 candidates × 5) | 15 | — | 0.45 |
| **Base, zero retakes** | | | **11.75** |
| With 30% video retakes | | | 14.37 |

Three of those fifteen Kling shots — 3.2, 4.4 and 5.3 — are the Motion Policy
correction made on intake: $1.75 of the video bill buys three shots that ran
under silence on a frozen frame in the submitted draft.

The 64-still batch is over the ~50 threshold and gets confirmed before it runs.

## Actual

| Stage | Date | USD | Note |
|---|---|---|---|
| Anchors, pass 1 | 2026-09-18 | 0.45 | 15 candidates, 5 anchors × 3 seeds. A1 usable; A2–A5 all failed |
| Anchors, pass 2 | 2026-09-18 | 0.36 | 12 candidates, A2–A5 reworked. A2 and A5 usable, A4 borderline, A3 failed twice |
| Anchors, pass 3 | 2026-09-18 | 0.09 | A3 only, geometry isolated from material. Approved, seed 33 |
| Stills | 2026-09-18 | 2.67 | 67 images: 59 candidates + 8 superseded by a prompt fix. 4 requests failed and produced nothing |
| Stills, ref_shot pair | 2026-09-18 | 0.16 | 5.1 and 7.2, generated against the approved 1.1 and 6.4 rather than an anchor |
| Takes | 2026-09-18 | 8.75 | 15 Kling clips, 125 s. 16 more shots built in ffmpeg for $0.00 |
| Takes, card plates | 2026-09-18 | 4.90 | 7 card plates moved from a frozen ffmpeg frame to Kling: snow frozen next to live snow reads as a stalled player |
| Takes, 6.1 retake | 2026-09-18 | 0.70 | first take grew a head on the animal by the tenth second |
| Takes, seven more | 2026-09-18 | 4.90 | five drift shots moved to Kling, 3.1 re-rolled, 4.3 re-rolled against a blooming light |
| Takes, 6.2 retake | 2026-09-18 | 0.70 | first take grew the beam into a comet with a bright core |
| Takes, coda plates | 2026-09-20 | 1.75 | 7.3, 7.4 and 7.5 moved to Kling: they were exempted from the suspended-particles rule by assertion, and the rough cut stopped dead for nineteen seconds |
| Takes, 5.4 paid twice | 2026-09-18 | 0.70 | a poll hung on a live request whose id existed only in the running process; killing the job lost the handle. gen_takes.py now writes the id to takes/pending.json before it polls and resumes from it. fal has no endpoint that lists recent requests, so the first payment is gone |
| Narration | | | |

Running total: $26.13 of the $11.75 estimate.

The $0.90 of anchors is the cheapest money in the record: every failure listed
against it would otherwise have been a reference image handed to 64 stills.
The $2.67 of stills includes two prompt faults found on scene 1 and fixed
before the other six scenes ran — eight images to save fifty-six.
