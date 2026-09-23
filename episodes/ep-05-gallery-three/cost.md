# Cost — record 5

Prices from `config/models.yaml`, verified against fal on 2026-09-18. Re-check
before stage 3: this board moves and the drift is not announced.

## Estimate

| Stage | Unit | Count | USD |
|---|---|---|---|
| Anchors, pass 1 | $0.03 / candidate | 5 anchors × 3 seeds | 0.45 |
| Anchors, further passes | $0.03 / candidate | budget two more passes | 0.60 |
| Stills | $0.0398 / image | 26 shots × 2–3 candidates | 2.60 |
| Stills, ref_shot pairs | $0.0398 / image | 4.2, 4.4, 5.3, 5.4, 6.1 | 0.30 |
| Takes — Kling 10 s | $0.70 | 9 | 6.30 |
| Takes — Kling 5 s | $0.35 | 4 | 1.40 |
| Shots built in ffmpeg | — | 13 | 0.00 |
| Narration | ElevenLabs | 33 paragraphs × 2–3 seeded takes | ~1.00 |
| Teaser music | ElevenLabs music endpoint | 1 cue | ~0.30 |
| **Total** | | | **~12.95** |

## The number this estimate should be read against

Record 04 was estimated at $11.75 and came in at $26.13. Almost none of the
overrun was a bad prompt: it was seven card plates and five drift shots moving
off the free ffmpeg tier onto Kling after the rough cut, because a frozen
frame with snow suspended in it next to a clip of the same snow moving reads
as a stalled player.

That failure is designed out of this record rather than budgeted for. Every
one of the thirteen ffmpeg shots has a prompt that puts nothing in the air and
nothing loose in the frame, and `shots.yaml` carries a hygiene rule whose
exception list is exactly the thirteen shots that go to a model. The exposure
if it happens anyway is 13 × $0.70 = **$9.10**, and it would be visible at the
rough cut, not at publication.

The other known way to lose money here is the one record 04 paid twice for: a
poll hung on a live request whose id existed only in the running process.
`gen_takes.py` writes the id to `takes/pending.json` before it polls and
resumes from it. Do not kill a generation job without checking that file.

## Actual

| Stage | Date | USD | Note |
|---|---|---|---|
| Anchors, pass 1 | 2026-09-21 | 0.45 | 15 candidates, 5 anchors × 3 seeds. A1, A2, A3, A4 usable; A1n failed in all three seeds — sunlit ground and a horizon glow, both caused by the exterior spine offering "hard white light or starlight" |
| Anchors, pass 2 | 2026-09-21 | 0.09 | A1n only, against a night spine of its own. Light and vantage both fixed; the plain is still brighter than starlight |

| Stills, scene 1 batch 1 | 2026-09-21 | 0.24 | 3 shots × 2 seeds. 1.2 usable; 1.1 returned boot prints in one seed and a rift in the other, 1.3 returned a yellow hazard stripe and a second lit fixture in both |
| Stills, scene 1 batch 2 | 2026-09-21 | 0.16 | 1.1 and 1.3 re-rolled against the fixed prompts and hygiene rules 5 and 6. Both faults gone in all four candidates |

| Stills, scenes 2-7 | 2026-09-21 | 1.64 | 42 candidates, 21 shots. 3 shots held on refs by design. 5 shots rejected |
| Stills, batch 3 | 2026-09-21 | 0.40 | 2.4, 4.1, 4.2, 4.3, 7.1 re-rolled. All five usable |

| Stills, held shots | 2026-09-21 | 0.24 | 5.3, 5.4 and 6.1, generated against the approved frames they reference. All three usable on one seed of two |

| Takes, scene 1 | 2026-09-21 | 1.40 | 1.1 and 1.3, 10 s each. Camera locked in both (1 px over the clip, measured). 1.3's strap reshapes itself |

| Takes, 1.3 retake | 2026-09-21 | 0.70 | Take 1 animated the empty neck opening and turned the strap into a festoon on another hook. Take 2 holds both. Take 1 kept under takes/take-1/ |

| Takes, scene 2 | 2026-09-21 | 1.05 | 2.3 and 2.4. Frost growth and dust both correct; the frame drifts in both |

| Takes, 2.3 retake | 2026-09-21 | 0.70 | Frame locked to 0.0 px. The fix was naming the drift as the subject moving, not as a camera instruction; carried to the seven locked model shots not yet generated |

| Takes, scene 3 | 2026-09-21 | 2.10 | 3.1 and 3.4 usable. 3.3 animated the wrong thing: no vapour, and the regolith inside the sealed tubes churns |

| Takes, 3.3 retake | 2026-09-22 | 0.70 | The vapour arrived and the frame locked to 0.0 px. The regolith inside the sealed tubes still churns — second failure on that fault, so no third roll |

| Takes, scene 4 | 2026-09-22 | 1.05 | 4.5 usable — its 18 px reading is the rotating clamp, the confound check_takes documents, and the wall behind it is static. 4.4's collar held but its strap became a festoon between two hooks |

| Takes, 4.4 roll 2 | 2026-09-22 | 0.70 | **Wasted.** The shots.yaml edit raised an AssertionError after its first substitution and before the file was written, so nothing was saved; the generate command was on the next line rather than chained to it and ran anyway, against the unchanged prompt. Same strap fault, twice paid for. A file edit and the run that depends on it belong in one command, and the edit is verified by reloading the file before anything is queued |

| Takes, 4.4 roll 3 | 2026-09-22 | 0.70 | First roll to actually carry the fixed wording, verified with the new `--dry-run` before it was sent. The collar held; the strap broke again. Three rolls, three strap failures — stop. Roll 3 accepted as it is |

| Takes, scene 5 | 2026-09-22 | 1.05 | Both frames locked. 5.4's frost carries on correctly from 2.3. 5.5's indicator fades out once at 3.4 s and stays out instead of blinking repeatedly |

| Takes, scene 6 | 2026-09-22 | 1.05 | Both accepted. 6.2's camera travels as intended, the two bars stay two and stay leaning, the hatch stays closed; 6.3's mist forms and thins away |

| Narration | 2026-09-22 | ~0.30 | 33 paragraphs x 3 seeds = 99 requests, 5,211 characters. ElevenLabs bills characters against the subscription and returns no per-request price, so this is the character count converted at the plan rate rather than an observed charge |

| Sound beds | 2026-09-22 | ~0.10 | Four 22 s beds: tone, fan, hum, pump. Measured -63.0, -68.6, -28.3 and -33.9 dBFS — 40 dB of spread from four prompts at one endpoint on one day, which is worse than the 15-20 dB CLAUDE.md records for record 04 |

| Word alignments | 2026-09-22 | ~0.10 | 33 paragraphs through the with-timestamps endpoint, same voice, same seeds, same previous_text as the takes in the mix. Cached in audio/alignment/ |
| Verticals | 2026-09-22 | 0.00 | Three cuts assembled from takes/ and from paragraphs already in the record. Nothing generated |

| Teaser cue | 2026-09-22 | ~0.30 | One 30 s piece at the MUSIC endpoint, not the sound-effect one. Measured -16.1 dBFS against voice at -17.2, so the trim is -13; record 04's -16 would have put it 4 dB quieter than intended |
| Teaser | 2026-09-22 | 0.00 | Assembled from takes/ and from paragraphs already in the record |

Running total: ~$15.22 of the $12.95 estimate. Stage 6 closed: 13 model shots,
19 rolls, 110 s of Kling. Narration generated; picks provisional until heard.

Stills are closed: 26 of 26 approved, 60 candidates generated. The stage
estimated at $2.90 came in at $2.68.

Four images spent on scene 1 to find two prompt faults and two missing
hygiene rules, before the other six scenes ran. Record 04 did the same
arithmetic: eight images to save fifty-six. The boot prints are the one worth
the money — rule 5 now covers 2.1, 7.1 and 7.2 as well, and none of those
three has been generated yet.
