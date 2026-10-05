# Cost — record 7

Prices from `config/models.yaml`, last verified against fal on 2026-09-18.
Re-check before stage 3 — it has been more than two weeks.

## Estimate

| Stage | Unit | Count | USD |
|---|---|---|---|
| Anchors, pass 1 | $0.03 / candidate | 5 anchors × 3 seeds | 0.45 |
| Anchors, further passes | $0.03 / candidate | budget two more passes on ~3 anchors | 0.54 |
| Stills | $0.0398 / image | 32 anchored shots × 2 | 2.55 |
| Stills, ref_shot (7.1 on 6.3, 8.2 on 1.2) | $0.0398 / image | 2 × 2 | 0.16 |
| Takes — Kling 10 s | $0.70 | 12 | 8.40 |
| Takes — Kling 5 s | $0.35 | 7 | 2.45 |
| Kling O3 Standard test | ~$0.084 / s | one 10 s shot | ~0.84 |
| Shots built in ffmpeg | — | 15 | 0.00 |
| Narration | ElevenLabs | 22 paragraphs × 3 seeded takes | ~0.30 |
| Beds (tone, pump), alignments | ElevenLabs | | ~0.20 |
| Teaser music | ElevenLabs music endpoint | 1 cue | ~0.30 |
| **Total, first rolls** | | | **~16.19** |

Rerolls are not in the total. Record 05 ran 19 rolls for 13 model shots; the
same ratio here is ~10 extra rolls, up to ~$6 more.

The cheapest video line on the channel since record 03, and not because
anything is frozen: 19 of 34 shots are Kling, no two ffmpeg shots touch, and
the record is short (4:27) because it says everything it has in that time.

## Kling O3 Standard test — run 2026-10-05, rejected (see Spend)

Raised 2026-10-05. fal lists Kling 3.0 (O3) Standard at about $0.084/s
without audio, billed per second from 3 to 15 s, against the workhorse's
$0.70 per 10 s. Price is not the argument for this record — every model shot
here is already 5 or 10 s, so per-second billing saves nothing and O3 costs
more. The question is whether it holds a locked frame and rigid geometry
better than 2.5 Turbo.

- One shot, rolled on both models from the same approved still, same
  prompt. Candidate: **3.2** (the meter disc — a rigid rotation with one
  stripe to track, so a wobble or a redrawn disc is obvious) or **6.4**.
- Before it runs: probe the endpoint id and the price live, add the tier to
  `config/models.yaml`, and `gen_takes.py --dry-run` the outgoing body.
- If O3 wins clearly, the 5-or-10 rule in CLAUDE.md and SCENARIO-AGENT.md
  is rewritten in the same change. Not before.

## Spend

| Stage | Date | USD | Notes |
|---|---|---|---|
| Anchors, pass 1 | 2026-10-05 | 0.45 | 5 anchors × seeds 11/22/33. All 15 came back saturated pastel blue and high-key instead of cold blue-grey and low. A1: no seed leaves the lower left empty, s22 grew small label plates. A2: s11 usable; s22 and s33 opened the top to a bright sky. A3: no numerals in any seed, but "scratched" came back as cracked glass and the 12-tick ring reads as a clock; s33 least so. A4: s11 grew a camera lens and a panel, s22 a tray in the card corner; s33 clean. A5: s22 has a panel in the card corner, s33's two ports read as eyes; s11 clean |
| Anchors, pass 2 | 2026-10-05 | 0.09 | A1 only, switches on the right side only and a plain wall on the left. The change worked in s22: left wall bare, floor bare, card corner empty. s11 put a sheet of labelled tags on the floor in the card corner; s33 turned the end of the compartment into an open empty cabinet |
| Stills, pass 1 | 2026-10-05 | 2.56 | 32 shots × seeds 11/22 (7.1 and 8.2 held for their ref_shot). The macro anchor locked composition hard: 2.5 s22 and 5.1 s22 came back as the A3 dial with the subject pasted on. The A5 housing returned as the body of 2.1, 3.1 and 4.2 alike. Lit blue indicators in 1.1 s11; fluorescent tubes in 4.4 s22; a lit control panel in 8.1 s22; a painted arrow in 8.5 s22 |
| Stills, 3.1 + 5.2 reroll | 2026-10-05 | 0.16 | Pass 1 of both rejected for lettering held on a static plate: "ON" printed on every breaker (3.1), a numbered scale on the slide rule (5.2). Prompts changed to a plain moulded handle and a plain straightedge; all four new seeds clean |
| Stills, ref_shot (7.1 on 6.3, 8.2 on 1.2) | 2026-10-05 | 0.16 | 7.1 s11 is the approved hatch, a shade darker; s22 rewrote the whole surface as a mottled frost-like texture. 8.2: both seeds are the approved dial, needle unchanged; s11 the closer match |
| Takes, scene 1 | 2026-10-05 | 1.40 | 1.3 kept: camera locked (0 px), dust drifts visibly the whole shot; the dark mass at the vanishing point from the still thins and thickens (brightness wander 11), reads as haze under grain. 1.2 REJECTED, $0.70 wasted: the needle swings from two o'clock to twelve and a second hand grows by 8 s, the dial becomes a clock; also a 7 px push. First 4 s clean, but the shot is 10 s |
| Takes, scene 2 | 2026-10-05 | 1.75 | 2.1 kept: camera 0 px, the wheel turns ~45° steadily over 10 s and does not stop — more than "a few degrees", still one rigid wheel. 2.5 kept: 0 px, dust drifts past the slats, nothing else moves. 2.3 REJECTED, $0.70 wasted: the paper advances, but from ~3 s the model writes on it — a double stroke mid-strip, then a closed scribbled outline like a map, and the strip swings back toward the slot by 10 s. Clean window ~2.5 s, too short to retime |
| Takes, scene 3 | 2026-10-05 | 1.40 | 3.4 kept: 0 px, the trace holds; its right end beads into dots in the last second. 3.2 provisional: 0 px, rigid, no morph — but the disc pivots like a coin turning on a cross-axis (edge-on, then face-on, then edge-on) instead of spinning in its own plane, so it reads as a butterfly valve, not a meter. The stripe never shows |
| Kling O3 Standard test, 3.2 | 2026-10-05 | 0.84 | A/B against the workhorse take, same approved still, same positive prompt, no negative (O3 has none). O3 LOST on every count: it returned 1268x724 — 720p, not 1080p, so it would have to be upscaled into the master; the camera drifts 58 px (about 88 px at 1080p) despite "the camera does not move at all"; and the disc stays edge-on and never visibly turns, so the one thing asked for does not happen. 88 s to generate. Workhorse 3.2 (0 px, rigid, wrong axis) stays |
| 3.2 and 3.4, decided without spend | 2026-10-05 | 0.00 | Serge: no rerolls. 3.2 keeps the workhorse take as rolled. 3.4 keeps its near-still take with a centred push (1.00→1.09, the local push constant) laid over it in assemble_scene.py. Lesson written into CLAUDE.md and SCENARIO-AGENT.md: a model shot must ask for visible motion, and must not be handed a pattern to continue |
| Takes, scene 4 | 2026-10-05 | 1.75 | None usable as rolled. 4.1: nothing moves (motion 1.31) — the shadow sweep was not drawn, even asked to start in the first second; a second near-still after 3.4. 4.3: the bubble crosses the glass as asked, then from ~5 s the camera pulls back (22 px, the window shrinks by a third). 4.5: the rotor turns, then at ~3.3 s the camera trucks right and a second window enters frame. Each has a clean head |
| Scene 4 repairs | 2026-10-05 | 0.00 | 4.1 push laid over; 4.3 first 5 s ×2 interpolated; 4.5 first 3.25 s ×1.54 interpolated. Serge on the pattern: stop paying for light, shadow and dust; a model shot is for an object that moves, everything else is an ffmpeg push or pull |
| Stills, 5.3 fan + 6.2 swivel lamp | 2026-10-05 | 0.16 | New subjects under the record-07 motion rule. 5.3: both seeds a five-blade fan behind a guard; s11 sparse rusty guard, blades read clearly through it; s22 a dense concentric guard over the blades. 6.2: both put the lamp high on the right with its oval on the back bulkhead; s11 has a thin cable hanging from the lamp down the wall (a soft thing, record 05); s22 has none |
| Takes, scene 5 | 2026-10-05 | 1.05 | Both kept as rolled — the first scene under the object rule, and the first with nothing to repair. 5.1: the pencil tumbles end over end with its shadow following, foreshortens as it turns toward the lens, camera 1 px. 5.3: the fan turns steadily for the full 10 s, guard and panel fixed, camera 0 px |
| Takes, scene 6 | 2026-10-05 | 1.05 | Both kept. 6.1: the lamp switches between lit and dark rather than pulsing, its hanging cable stays still; in the dark phases the ceiling at top left picks up a cream tint (taken out in the grade); 8 px of shift reads as the brightness change. 6.2: the lamp head turns and its oval slides across the back bulkhead from left to right, camera 0 px; in the last second the oval fades and a pale strip appears on the left wall. Last model shot of the record: 14 takes, $9.24 on video including $1.40 rejected and $0.84 on the O3 test |
| Rough cut | 2026-10-05 | 0.00 | build_static.py built the 20 ffmpeg shots (10 card plates, 10 pushes, pulls and drifts); assemble_scene.py all = 267.00 s, matching the script. Contact sheet in out/contact/ |
| 8.4 plate swap | 2026-10-05 | 0.00 | The dust in 8.4's first plate froze under the pull and read as specks on a photograph (Serge, on the rough cut). My error: I had noted it in shots.yaml and not told him. 8.4 now uses 5.5's clear-air plate, pulled instead of pushed |
| Narration | 2026-10-05 | ~0.25 | 22 paragraphs × seeds 11/22/33, plus 44/55/66 for scenes 1, 3, 5, 6, 7 (114 takes; eleven_v3 refuses previous_text). Median 176 wpm against the 162 planned; picks nearest the median, in audio/narration.yaml. Five paragraphs fast at every seed (s1p3 203-244, s3p2 183-213, s5p2 192-209, s6p1 181-197, s7p2 207-240). Speech 127.8 s against 139.3 planned; body 45.6% silent. Placement pulled to the cards with a new opt-in card_pull (audio.yaml); all seven carded lines now land 0.5-2.7 s after their card |
| Cards + graded preview | 2026-10-05 | 0.00 | build_cards.py --titles: 11 overlays, 384 clicks, bed at +23 dB as records 05-06. grade.py run against a provisional mix (voice + clicks, no beds) to judge card legibility under the real grade; the vignette and the 0.86 saturation take the pastel down and the green holds even on the bright floor plates (1.1, 5.4, 8.1). Preview only: out/test/graded-preview.mp4. audio/episode-mix.mp3 is provisional and is overwritten by build_audio.py |
| Beds + master | 2026-10-05 | ~0.10 | room and pump generated (22 s each), looped over their flat middles (the generator fades both ends; the pump's last second has a -1.4 dBFS knock). Levels against the 300 Hz band: tone 0 (≈-43), pump -6 (≈-40). Measured in the mix: -38.5 with the pump, -42.4 in scene 6 with it stopped, never below the floor. grade.py -> out/EPISODE-final.mp4, 267.00 s; check_flicker 0 dark frames. Serge approved the voice picks and the cards on the preview |
| Alignment, attempt 1 | 2026-10-05 | ~0.05 | with-timestamps regenerations of the 22 picked takes do NOT match the takes in the mix on eleven_v3 any more: last-word ends off by -0.80 to +1.44 s (records 03 and 05, same voice: within 0.16-0.40). Moved to audio/alignment-regen/, not used. build_captions.py now aligns the stored take itself through /v1/forced-alignment; the ElevenLabs key lacks the forced_alignment permission (401). Blocked on the key |
| Alignment, forced | 2026-10-05 | ~0.05 | Key given the forced_alignment permission by Serge. 22 paragraphs aligned on the takes in the mix: every last word ends inside its file (0.02-0.26 s before the end). The regenerated timings had put the pause after "drifting." in s2p2 at 0.13 s; the real one is 0.44 s, so the script's trim works and the teaser keeps all five lines |
| Verticals + teaser | 2026-10-05 | ~0.30 | Three cuts (22.4 / 27.6 / 19.7 s) and the teaser (30 s), built from takes/ only; all open on a voice by 0.34 s, s2p2 trimmed at 2.88 inside real silence. Slug at the new channel position (x 80, y 150). Teaser cue from the music endpoint, -35.4 above 300 Hz, no trim |
| Thumbnails | 2026-10-05 | 0.00 | a-the-number (6.3, "99 W / NO SOURCE"), b-the-patch (6.4, "11 cm / SINCE YESTERDAY"), c-the-drift (1.2, "+1.6 °C / THEN IT STOPPED"); judged at 210 px in out/thumbs/grid-210.png. Two blocks shrunk off their subject |
| **Total** | | **~13.57** | Against an estimate of ~16.19 for first rolls. Video $9.24 of it, including $1.40 rejected and $0.84 on the O3 test |
