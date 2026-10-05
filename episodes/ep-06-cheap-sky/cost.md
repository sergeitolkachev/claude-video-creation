# Cost — record 6

Prices from `config/models.yaml`, verified against fal on 2026-09-18. Re-check
before stage 3.

## Estimate

| Stage | Unit | Count | USD |
|---|---|---|---|
| Anchors, pass 1 | $0.03 / candidate | 3 anchors × 3 seeds | 0.27 |
| Anchors, further passes | $0.03 / candidate | budget two more passes | 0.54 |
| Stills | $0.0398 / image | 32 anchored shots × 2 | 2.55 |
| Stills, text-to-image (5.1) | $0.03 / image | 3 seeds | 0.09 |
| Stills, ref_shot (4.4 on 2.2) | $0.0398 / image | 2 | 0.08 |
| Takes — Kling 10 s | $0.70 | 17 | 11.90 |
| Takes — Kling 5 s | $0.35 | 5 | 1.75 |
| Shots built in ffmpeg | — | 11 | 0.00 |
| Narration | ElevenLabs | 24 paragraphs × 3 seeded takes | ~0.30 |
| Beds, alignments | ElevenLabs | | ~0.20 |
| Teaser music | ElevenLabs music endpoint | 1 cue | ~0.30 |
| **Total, first rolls** | | | **~17.98** |

Rerolls are not in the total. Record 05 ran 19 rolls for 13 model shots;
the same ratio here is ~10 extra rolls, up to ~$7 more.

## Why the video line doubled

The draft was 11 model shots, $6.65. On intake eleven more moved to Kling
(script.md, correction 1): the draft ran ffmpeg shots in series up to 46 s
long, and four of them froze something that moves — two sets of distant
flyers, a particulate fall, a drifting fleck. Record 04 paid $1.75 to learn
what a frozen plate beside a moving one reads as, and then moved twelve
plates anyway. This record pays for it at the start instead.

## Spend

| Stage | Date | USD | Notes |
|---|---|---|---|
| Anchors, pass 1 | 2026-09-25 | 0.27 | 3 anchors × seeds 11/22/33. A1: every seed grew a dark band along the bottom that reads as ground, s22 a sun-like hotspot. A2: s33 usable; s11 has a shadow wedge and marks like footprints, s22 glassy blue-white ice. A3: no seed is top-down — all three are low oblique views with depth, and the cobbles came back as clear glassy ice |
| Anchors, pass 2 | 2026-09-25 | 0.18 | A1 and A3 only. A1: the vertical-gradient change worked in s11 — no band, no horizon, lower left deep rust; s22 still has a thin dark line at the bottom and the hotspot, s33 still grows ground. A3: geometry fixed in s11 and s22 (near top-down, sharp across the frame), s33 still oblique. The glass cobbles survived in all three, and the sand splits into bright dry gold on the left and dark wet on the right — a fault pass 1 had too |
| Anchors, pass 3 | 2026-09-25 | 0.09 | A3 only. The glass is gone in all three: opaque matte cream pebbles. The sand split survived in s11 and s22 (gold left, dark right); s33 has uniform dark sand but went oblique again. s22 is the only true top-down frame |
| Stills, batch 1 | 2026-09-25 | 2.52 | 66 of 66 saved: 62 on nano-banana against the three anchors, 4 text-to-image for 5.1. 4.4 held until 2.2 is approved. Faults: A2 locks composition hard, so 1.2 and 1.3 came back as the same frame; 5.1 sits on a flat yellow backdrop in all four seeds; 6.1 returned a bird and a fruit bat, one with feet; 2.2 s22 has legs on its specks; 5.5 s22 and 6.4 s22 have marks like tracks |
| Stills, retakes + 4.4 | 2026-09-25 | 0.36 | 1.3 (framing), 5.1 (background), 6.1 (body shape) and 4.4 off the approved 2.2. All three fixes landed on at least one seed: 1.3 s11 is a different frame from 1.2, 5.1 now stands on a plain in haze, 6.1 s22 is a crescent membrane with no head, tail or legs. 5.1 s11/s33 grew a screen-like panel again |
| Takes, scene 1 | 2026-09-25 | 1.75 | 1.4 accepted: a puff of dust runs across the sand, pebbles hold. 1.3: a sun disc rises out of the haze above the horizon from ~2 s and is plain by 7 s, with "sun, sun disc" already in negative_extra. 1.1: the particulate is barely visible and mostly gone after 2 s; what moves is the gradient itself, drifting and darkening ~10% (YAVG 114 -> 103). check_takes reads it as an 89 px shift |
| Takes, scene 2 | 2026-09-25 | 1.40 | Both accepted. 2.2: the three domes drift left together, keeping shape and spacing, nothing resolves. 2.4: a sheet of fine dust streams low across the foreground, cobbles hold, camera holds. Scene 1's three takes are kept as they came, marked provisional for the rough cut (take_note in shots.yaml) |
| Takes, scene 3 | 2026-09-25 | 2.80 | All four accepted. 3.1: particulate clearly visible and drifting — the approved still had visible specks and 1.1's did not, so particle visibility is set at the still, not in the video prompt. 3.2: vapour lifts off the wet cobble twice. 3.4: drops land, one ring spreads, the pool holds — first drizzle on this channel, first roll. 3.5: bands of haze roll across the frame. No money lost, but ~70 min lost to downloads: the fal CDN throttles each connection to ~30 KB/s on some clips. Fixed in gen_takes.py with parallel byte-range downloads (3.5: 40 min -> 15 s) |
| Takes, scene 4 | 2026-09-25 | 2.45 | Downloads fine this time (parallel ranges). 4.4, 4.5 accepted; 4.1 kept provisional (faint particulate, like 1.1 — the still carried few specks). 4.2 rejected: the "particulate settling" became a column pouring from above and a white heap growing into a mound by 2.4 s — a sugar pour. "deposit growing into crystals" was in negative_extra |
| Takes, 4.2 roll 2 | 2026-09-26 | 0.70 | **Rejected — second failure, stopped.** Motion changed to a dust drift (the class that held on 1.4 and 2.4); the deposit grew anyway, a white blob swelling into a large smooth oval by 4 s. Both rolls grew the pale band, so the still invites it. Also: the command ran generation after `validate.py \| tail`, and the pipe swallowed a validation failure ("shape" in the video prompt tripped rule 4). Harmless here, a wrong chain all the same |
| 4.2 to ffmpeg | 2026-09-26 | 0.00 | After two rejected rolls: a 9% centred push on the approved still, built by build_static.py with the other eleven ffmpeg shots. Split is now 21 model / 3 local / 9 static; the first-roll video estimate drops by $0.70 |
| Takes, scene 5 | 2026-09-26 | 1.75 | 5.3 and 5.5 accepted. 5.1 kept provisional: the housing holds, but the pale sand at its foot heaps up against it by 4.8 s and settles — a wind drift piling sand, plausible, but the same growing-pale-mass habit as 4.2 |
| Takes, scene 6 | 2026-09-26 | 2.80 | 6.2, 6.5 accepted; 6.4 provisional (the haze roll barely registers, motion 1.07). 6.1, roll 1: the flyer glides right to left and holds for ~2.5 s; from ~3 s a small nub grows at the trailing tip and by 5 s it is a bulb — record 04's tail-bulb completion again — and at 8-9 s it banks and flattens into something like an aircraft hull. It never leaves frame |
| Takes, scene 7 | 2026-09-26 | 0.70 | Both accepted: 7.1 two dark flecks drift across, 7.3 one pale fleck crosses the top of frame. Stage 6 closed: 21 model shots, 23 rolls, $14.70 of Kling (4.2 rejected twice and moved to ffmpeg; 6.1 undecided) |
| Narration | 2026-09-27 | ~0.40 | 24 paragraphs × seeds 11/22/33, plus 44/55/66 for scenes 1, 2 and 5 (114 requests), then 24 alignments. Billed as characters against the subscription; converted at the plan rate, not an observed charge. This text ran fast on this voice: six paragraphs stayed above 180 wpm across six seeds |
| Sound beds | 2026-09-27 | ~0.05 | wind (22 s), wingbeat (22 s), wingbeat-close (3 s) at the sound-effect endpoint, prompts written as what is there with no listed absences. Measured -37.2 / -28.6 / -34.4 dBFS — 9 dB of spread, against 40 on record 05 |
| Rough cut | 2026-09-27 | 0.00 | rough-cut.mp4, 12 card overlays + slug + closer, 412 clicks, mix, grade, grain 9 / CRF 23. check_flicker: 0 dark frames. out/EPISODE-final.mp4, 300.00 s |
| Sound beds, pass 2 + draft 2 | 2026-09-27 | ~0.05 | **Draft 1 had no audible background** on Serge's playback: the pass 1 beds carried nearly all their energy under 150 Hz (above 300 Hz: -52 to -57 dBFS before trims, -60 to -70 in the mix), and a phone or laptop plays almost nothing down there. Levels had been set against full-band means. Pass 2 prompts described hiss, rustle and flap and still came back low-heavy. Fix: a `filter:` key in build_audio.py (250 Hz high-pass per bed, in audio.yaml) and trims set against the band above 300 Hz. Beds now sit 13-25 dB under the voice in that band. Master regraded |
| Verticals | 2026-09-27 | 0.00 | Three cuts from takes/: 22.4 / 28.0 / 20.8 s. build_verticals.py hard-coded audio/sfx/tone.mp3 and build_teaser.py guessed sfx/<level>.mp3 — neither would have found this record's floor (wind.mp3) or applied its high-pass. Both now read the layer through vertical.layer_source(). Four crops moved onto their subjects |
| Teaser cue + teaser | 2026-09-27 | ~0.30 | Music endpoint, 30 s. -21.3 dBFS mean, -29.7 above 300 Hz; trim -6. One caption rendered as a single overflowing line: a 58-character cue with no two-line split under 30 characters made wrap() give up. Fixed in build_captions.py — the most balanced split is used and render() sizes the font |
| Thumbnails | 2026-09-27 | 0.00 | Three variants from approved stills: a-the-flyer (6.1), b-the-human (1.3), c-the-budget (2.2). Judged at 210 px; C re-cropped onto the domes after they vanished at grid size |

Running total: ~$18.57
