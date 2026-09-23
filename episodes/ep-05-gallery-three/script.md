# FC9-005 // "THE OPERATOR WENT INTO GALLERY THREE ALONE"

**Slug:** FC9-LOG-005 // The Operator Went Into Gallery Three Alone
**Series:** 1 — The Last Operator
**Runtime:** 3:45 (225 s) — 26 shots, durations sum to 225 s exactly
**Per-scene seconds:** {1: 30, 2: 35, 3: 40, 4: 40, 5: 40, 6: 25, 7: 15} (sum 225)
**Format:** 16:9 horizontal, three vertical cuts assembled from it, one teaser
**Voice:** character (operator) only. No narrator: the recovery frame is
  delivered as text cards in the coda (Scene 7). Delivery: a tired technician
  reading a shift log into a suit recorder. Level, unhurried, no pauses for
  effect inside a sentence. Every number read like "shift complete".
**Word count:** 290. At 162 wpm that is 107.4 s of speech against 225 s of
  runtime — 52.3% silence overall; 48.9% across Scenes 1–6 (210 s) with the
  declared coda excluded.
**Motion split:** 8 static / 5 local / 13 model
**The barrier:** lunar night at a near-equatorial site lasts about 354 hours;
  the station battery covers 363.6 hours at survival draw — 9.3 hours of margin.
**The impossibility:** bus three draws 0.40 kW while every load on it is
  isolated.

### Per-scene silence

| Scene | Seconds | Words | Speech (s) | Silence |
|---|---|---|---|---|
| 1 | 30 | 41 | 15.2 | 49.4% |
| 2 | 35 | 49 | 18.1 | 48.3% |
| 3 | 40 | 51 | 18.9 | 52.8% |
| 4 | 40 | 59 | 21.9 | 45.4% |
| 5 | 40 | 55 | 20.4 | 49.1% |
| 6 | 25 | 35 | 13.0 | 48.1% |
| 7 (coda) | 15 | 0 | 0 | 100% — declared coda |
| **Total** | **225** | **290** | **107.4** | **52.3%** |

---

## Corrections on intake

The script was submitted as record **004**, which is a record that already
exists and is published. Everything below is the submitted draft with the
following changes, and nothing else. The words of the narration are unchanged,
every figure is unchanged, and the shot list is unchanged in content.

1. **Renumbered 004 → 005** throughout, including the slug, `publish.md` and
   the three vertical ids, which also move from `.a/.b/.c` as submitted to
   `.a/.b/.c` kept — record 04 used `.b/.c/.d` and the channel is going back
   to `.a/.b/.c` from here.

2. **Narration reformatted to the repository's own shape.** The draft used
   `**Narration**` and `OPERATOR:` line prefixes. `build_audio.py` — the one
   paragraph parser everything imports — reads `**Narration:**` followed by a
   block quote, and would have counted zero words and passed every silence
   check by measuring nothing. The speaker is named once, in `shots.yaml`
   under `voice: character`, which is the fix record 03 paid for when three
   scripts each carried their own idea of who was talking.

3. **The camera contradiction in 1.1 and 1.3.** Both were written as "camera
   locked" and "slow push" in the same sentence. That is two instructions to
   one model, and it is also the split `shots.yaml` exists to keep: the
   subject goes in `prompt`, the movement goes in `video_prompt` and
   `motion_tail`. Both shots are now locked, and the movement in them is the
   thing in the frame — the shadow edge in 1.1, the tether strap in 1.3.

4. **The console screens.** 4.1 and 6.1 asked for "one flat screen … with
   nothing displayed on it". Every noun in that clause is one record 04
   forbids outright, because the image models answer a screen with invented
   lettering. It is a flat glass panel lit evenly from behind now, with
   nothing behind it, and the word never reaches a prompt.

5. **Nothing moves in a frame that will never be animated.** Thirteen of the
   twenty-six shots are built in ffmpeg from a single still. A still that
   contains dust in the air, a hanging strap, condensation or a lit indicator
   is a frozen picture of something that ought to be moving, and it reads as a
   stalled player — record 04 paid $1.75 re-rolling three coda plates for
   exactly that. Every static and local prompt now states that the air in
   front of the subject is clear and that nothing in the frame is loose, lit
   or suspended, and `shots.yaml` carries a hygiene rule whose exception list
   is, precisely, the shots that go to Kling.

6. **6.2 comes off the anchor, not off 3.1.** The draft referenced the
   approved still of 3.1 for the corridor on the way in. A reference makes two
   shots the same object down to the scratch in the glass, and it resists
   intended change just as hard — and the one thing that has to be different
   in 6.2 is the two steel bars being off the hatch, which is the beat of the
   scene. 5.3 keeps its reference to 3.1, where nothing changes at all.

7. **7.2 has no anchor at its distance.** A macro of regolith outside is
   neither the exterior wide (A1) nor the interior hardware macro (A3), and
   handing it either returns that anchor's distance. It goes text-to-image
   against a spine of its own, which is what record 04 did with its one
   tissue shot.

8. **The exterior appears in three lights** — low sun on the rim (1.1), full
   night under starlight (2.1), first light on the peaks (7.1). An anchor
   locks light as hard as it locks framing, so there are two exterior anchors:
   A1 for the two rim-lit shots and A1n for the night.

9. **A teaser was added.** It did not exist in the draft. Thirty seconds,
   vertical, out before the record, built from takes and from lines the record
   already contains. See "The teaser" below.

---

## Disclaimer

This record is fiction. Daedalus Two, its crew, its logs and every station
figure are invented. The length of the lunar night, the far side's lack of
line of sight to Earth and the energy arithmetic are real and can be checked
in the description.

## Synopsis

Daedalus Two is a six-person drill station in Daedalus crater on the lunar far
side. Sixty-four hours before nightfall the drill broke into a void at 41 m.
Four hours later five crew entered gallery three in suits and opened their own
purge valves within eleven seconds of each other. A revised protocol arrived:
no one enters gallery three alone, nothing from the void is touched, purge
valves stay clamped. The relay went silent at night minus forty hours.

The operator is alone for a 354-hour night with 9.3 hours of battery margin.
At night hour thirty the battery reads 12 kWh low. Bus three, whose loads are
all isolated, is drawing 400 W. That erases the margin: the battery now ends
about three and a half hours before dawn. The breaker is inside gallery three.
The operator goes in. The coda gives the battery's end at night hour 351 — the
hour it ends only if bus three was never isolated — and the number of suits in
gallery three at dawn.

---

## Style spine and anchors

Four sets, kept separate: exterior wide, exterior macro, interior, interior
macro. Interior and macro do not share a spine because room nouns in the
interior spine would build a room inside every macro frame.

**Exterior spine (A1, A1n).** Fine powdery pale-grey regolith. Hard black
shadow with a razor edge and no fill. No haze at any distance and nothing
softening anything. A black sky filled edge to edge with small, sharp,
unmoving stars. Hard white light or starlight only. Palette: monochrome grey
through black.

**Exterior macro spine (7.2 only).** A surface of fine pale grey dust, so fine
it has no visible grains, every part of the picture at the same distance from
the lens because the camera points straight down at it. No sky and no
distance anywhere in the picture. One hard white source from low on one side.
Palette: pale grey through black.

**Interior spine (A2, A4).** Scuffed brushed aluminium and off-grey composite
panelling, edges worn to bare metal, fine grey dust packed into every seam and
rivet line. Cold white-blue overhead light, low and even, falling off into
near-black within a few metres. Palette: desaturated blue-grey, graphite, dull
silver. No saturated colour.

**Interior macro spine (A3).** Worn brushed aluminium, grey woven suit fabric
with abrasion and pilling, fine grey dust caught in knurling and stitching.
Cold white-blue light from one side. Palette: desaturated blue-grey, graphite,
dull silver. No saturated colour.

**Anchors**

- **A1 — exterior wide, low sun.** Crater floor and rim, camera at ground
  level, wide lens, horizon in the upper third. Covers 1.1 and 7.1.
- **A1n — exterior wide, night.** The same ground under starlight only, no
  sun anywhere in the picture. Covers 2.1.
- **A2 — corridor deep perspective.** Camera at eye height on the corridor
  axis, moderate wide lens, vanishing point centre frame.
- **A3 — macro hardware.** Camera 20–30 cm from subject, long lens, shallow
  depth of field.
- **A4 — object head-on, mid distance.** Camera 2–3 m from subject, normal
  lens, subject centred, lower left of frame kept dark and empty.

**Same-object references (use the approved still, not the anchor):**

- Shot 4.4 references the approved still of **Shot 1.3** (suit rack).
- Shot 4.2 references the approved still of **Shot 1.2** (purge valve).
- Shot 5.3 references the approved still of **Shot 3.1** (corridor and hatch).
- Shot 5.4 references the approved still of **Shot 2.3** (viewport frost).
- Shot 6.1 references the approved still of **Shot 4.1** (console).

5.1 is the same battery module as 2.2 and is deliberately **not** a reference:
the frost on it is thicker, and a reference resists an intended change as hard
as it holds an unintended one. 6.2 is the same corridor as 3.1 and is
deliberately not a reference either, for the same reason — the bars are off
the hatch.

---

## SCENE 1 — NIGHT HOUR ZERO (0:00–0:30)

No cards. Image first.

**Shot 1.1** — model, 10 s, anchor A1
> Ground-level wide view across a crater floor of pale grey regolith toward a
> distant mountainous crater rim. A low white sun sits exactly on the rim line
> at frame right. A hard black shadow edge lies across the regolith in the
> middle distance. Black sky with small sharp stars above the rim. Camera
> locked. The only movement in the shot is the shadow edge, creeping slowly
> toward the camera.

**Shot 1.2** — local, 10 s, anchor A3
> Macro of a round purge valve knob with coarse knurling, set into grey woven
> suit fabric. A heavy brushed-aluminium clamp bracket is bolted across the
> knob, locking it. Fine grey dust in the knurling and along the fabric
> stitching. Cold white-blue light raking from the left, deep shadow on the
> right. Long lens, shallow depth of field. Nothing in the frame is loose or
> hanging and the air in front of the subject is clear.

**Shot 1.3** — model, 10 s, anchor A4
> Head-on view of a wall-mounted suit rack with six heavy hooks in a row. Five
> hooks are bare. The last hook on the right holds one grey pressure suit, its
> empty helmet resting on the shelf above it. Worn aluminium panelling behind.
> Cold white-blue overhead light. A loose fabric tether strap hangs from the
> suit. Camera locked. The strap sways gently in a draft from an air vent and
> nothing else in the frame moves. Lower left of frame in shadow.

**Narration:**
> Operator log. Daedalus Two. Night hour zero.
>
> It is full moon on Earth tonight.
>
> Station crew, six. On shift, one.
>
> Clamps fitted to both purge valves on my suit. Per revised protocol seven.
>
> I checked them. Then I checked them again.

---

## SCENE 2 — THE BUDGET (0:30–1:05)

**Shot 2.1** — static, 10 s, anchor A1n
> Ground-level wide view across a crater floor at night. Pale grey regolith
> just visible under starlight, fading to black toward the camera. A dark
> crater rim silhouette against a black sky dense with small sharp stars.
> Camera locked. Nothing anywhere in the picture is lit except the ground and
> the stars. Lower left of frame near-black and empty.

**Card 2.1** (types on with "Night at this site…")
```
NIGHT     354.4 H
BATTERY   4000 KWH
```

**Shot 2.2** — static, 10 s, anchor A3
> Macro of the side of a battery module: ribbed brushed-aluminium cooling fins
> with a thin rime of frost along their outer edges, fine grey dust settled in
> the grooves. Cold white-blue light from above right. Camera locked. The air
> in front of the fins is completely clear and no lamp or indicator is lit
> anywhere in the frame. Lower left of frame in soft dark shadow and empty.

**Card 2.2** (types on with "Survival draw…")
```
DRAW      11.0 KW
RUNTIME   363.6 H
MARGIN    9.3 H
```

**Shot 2.3** — model, 10 s, anchor A3
> Macro of the inner edge of a thick round viewport set in worn aluminium.
> Beyond the glass, pure black. Fine feathered frost crystals grow slowly
> inward from the metal rim across the inner surface of the glass. Cold
> white-blue light grazing the frost from the left. Camera locked.

**Shot 2.4** — model, 5 s, anchor A2
> Eye-height view down a narrow station corridor of worn aluminium panels
> receding into darkness. A single shaft of cold white-blue overhead light
> halfway down. Fine grey dust motes drift slowly through the light shaft.
> Camera locked.

**Narration:**
> Night hour two.
>
> Night at this site lasts about three hundred and fifty-four hours.
>
> Battery at nightfall, four thousand kilowatt hours.
>
> Survival draw, eleven kilowatts. Heaters, scrubber, one occupant.
>
> That is about three hundred and sixty-three hours. About nine hours spare.
>
> Relay carrier lost at night minus forty hours.

---

## SCENE 3 — GALLERY THREE (1:05–1:45)

**Shot 3.1** — model, 10 s, anchor A2
> Eye-height view down a narrow corridor of worn aluminium panels toward a
> round pressure hatch at the far end. Two heavy steel bars are bolted across
> the hatch's twin handles. Cold white-blue overhead light in pools along the
> corridor. Fine grey dust drifts slowly through the light. Slow push forward
> along the corridor axis.

**Shot 3.2** — static, 10 s, anchor A3
> Macro of the face of a pressure hatch: thick worn grey paint chipped to bare
> steel around a heavy bolt head, fine grey dust settled along the seal
> groove. Cold white-blue light raking from the right. Camera locked. The air
> in front of the steel is completely clear, nothing hangs in the frame and no
> lamp or indicator is lit in it. Lower left of frame is flat dark painted
> steel, empty.

**Card 3.2** (types on with "Protocol seven.")
```
PROTOCOL 7  REVISED
NO ENTRY TO GALLERY 3 ALONE
NO CONTACT WITH VOID MATERIAL
PURGE VALVES CLAMPED
```

**Shot 3.3** — model, 10 s, anchor A3
> Macro of a row of transparent core sample tubes lying in a brushed-aluminium
> tray, each packed with dark grey regolith. A thin rime of frost coats the
> tubes. Faint cold vapour curls slowly off the frost and drifts upward. Cold
> white-blue light from the left. Long lens, shallow depth of field, camera
> locked.

**Shot 3.4** — model, 10 s, anchor A4
> Head-on view of the same round pressure hatch with two steel bars across its
> handles, set in a worn aluminium wall. Beside the hatch, a small round
> indicator lamp glows cold blue and slowly pulses brighter and dimmer. The
> hatch's small round viewport shows only black. Camera locked. Lower left in
> shadow.

**Narration:**
> Night hour fourteen.
>
> Five crew remain in gallery three.
>
> Recovery is not authorised under protocol seven.
>
> Protocol seven. No entry to gallery three alone. No contact with material
> from the void. Purge valves clamped at all times.
>
> The drill broke into the void at night minus sixty-four hours. Depth,
> forty-one metres.

---

## SCENE 4 — TELEMETRY (1:45–2:25)

**Shot 4.1** — local, 10 s, anchor A4
> Head-on view of a station operations console: a bank of worn aluminium
> panels with rows of physical toggle switches and one flat glass panel set
> into them, lit evenly from behind with a plain cold white-blue light and
> nothing behind it. Bundled grey cables run down into the floor. Low cold
> light. Every switch on the console is in the same position, nothing hangs
> loose anywhere in the frame, no lamp or indicator is lit on it and the air
> in front of it is clear.

**Shot 4.2** — static, 10 s, anchor A3 (reference approved still of Shot 1.2)
> Macro of a round purge valve knob with coarse knurling set into grey woven
> suit fabric, no clamp fitted, the knob turned fully out. Fine grey dust
> settled in the knurling. Cold white-blue light raking from the right.
> Camera locked. Nothing in the frame is loose or hanging and the air in front
> of the fabric is clear. Lower left of frame is soft out-of-focus grey
> fabric, empty.

**Card 4.2** (types on with "All five purge valves…")
```
PURGE VALVE OPEN  GALLERY 3
S2  -60:14:07
S3  -60:14:09
S4  -60:14:11
S5  -60:14:15
S6  -60:14:18
```

**Shot 4.3** — local, 5 s, anchor A4
> Head-on view of a single empty suit helmet resting on a worn aluminium
> bench. The dark smoked visor is down and reflects only a soft smear of cold
> overhead light. Fine grey dust settled on the bench. The helmet is empty and
> unoccupied, nothing is reflected in the visor but the light, and the air
> around it is clear. Lower left in shadow.

**Shot 4.4** — model, 10 s, anchor A4 (reference approved still of Shot 1.3)
> Head-on view of the wall-mounted suit rack with six hooks, five bare, one
> grey pressure suit hanging on the right. A loose fabric tether strap sways
> gently in the air vent draft. Cold white-blue overhead light. Camera locked.

**Shot 4.5** — model, 5 s, anchor A3
> Macro of a spare brushed-aluminium valve clamp hanging from a short steel
> lanyard against a worn aluminium panel, turning slowly on the lanyard. Cold
> white-blue light from the left. Long lens, shallow depth of field, camera
> locked.

**Narration:**
> Night hour twenty-two. I have read the suit telemetry.
>
> All five suits entered gallery three together.
>
> All five purge valves were opened by hand. First to last, eleven seconds.
>
> A purge valve takes four turns.
>
> No suit reported a fault. No alarm was raised on the channel.
>
> Heart rate on all five suits was normal until the valves opened.

---

## SCENE 5 — BUS THREE (2:25–3:05)

**Shot 5.1** — static, 10 s, anchor A3
> Macro of the side of a battery module: ribbed brushed-aluminium cooling fins
> with a thicker rime of frost along their edges, fine grey dust settled in
> the grooves. Cold white-blue light from above right. Camera locked. The air
> in front of the fins is completely clear and no lamp or indicator is lit
> anywhere in the frame. Lower left of frame in dark shadow and empty.

**Card 5.1** (types on with "Battery, three thousand…")
```
BATTERY   3658 KWH
EXPECTED  3670 KWH
```

**Shot 5.2** — static, 10 s, anchor A3
> Macro of a row of heavy black rotary breaker handles on a worn grey steel
> electrical cabinet, thick grey cables entering from above, fine grey dust
> settled on every ledge. Cold white-blue light raking from the right. Camera
> locked. Every handle in the row is identical and in the same position, the
> steel around them is dark and unlit with no lamp anywhere on it, and the air
> in front of the cabinet is clear. Lower left of frame is flat dark steel,
> empty.

**Card 5.2** (types on with "Bus three is drawing…")
```
BUS 3        0.40 KW
BUS 3 LOADS  ISOLATED
```

**Shot 5.3** — local, 5 s, anchor A2 (reference approved still of Shot 3.1)
> Eye-height view down the narrow corridor toward the round pressure hatch
> with two steel bars across its handles. Cold white-blue light in pools. The
> air in the corridor is completely clear with no dust in it, and nothing in
> the frame is lit but the overhead light.

**Shot 5.4** — model, 10 s, anchor A3 (reference approved still of Shot 2.3)
> Macro of the inner edge of the same thick round viewport. Beyond the glass,
> pure black. Feathered frost now covers a third of the glass and keeps
> growing slowly inward. Cold white-blue light grazing from the left. Camera
> locked.

**Shot 5.5** — model, 5 s, anchor A2
> Eye-height view along a corridor floor where a thick grey power cable runs
> away into darkness. On a steel junction box beside the cable, a small cold
> blue indicator light blinks slowly. Camera locked.

**Narration:**
> Night hour thirty.
>
> Battery, three thousand six hundred and fifty-eight kilowatt hours.
>
> At eleven kilowatts it should read three thousand six hundred and seventy.
>
> Bus three is drawing four hundred watts.
>
> Bus three feeds the lights and the drill head in gallery three. Both are
> isolated.
>
> The breaker for bus three is in gallery three.

---

## SCENE 6 — NIGHT HOUR THIRTY-ONE (3:05–3:30)

No cards. Every figure is spoken.

**Shot 6.1** — local, 10 s, anchor A4 (reference approved still of Shot 4.1)
> Head-on view of the station operations console: worn aluminium panels, rows
> of physical toggle switches, one flat glass panel lit evenly from behind
> with a plain cold white-blue light and nothing behind it. Bundled grey
> cables into the floor. Every switch is in the same position it was, nothing
> hangs loose in the frame, no lamp or indicator is lit and the air in front
> of the console is clear.

**Shot 6.2** — model, 10 s, anchor A2
> Eye-height view moving slowly down the narrow corridor toward the round
> pressure hatch. The two steel bars have been unbolted and lean against the
> wall beside it. A single white helmet-lamp beam leads the camera and lights
> fine grey dust drifting in the air. Slow steady forward movement along the
> corridor axis.

**Shot 6.3** — model, 5 s, anchor A4
> Head-on view inside a small cylindrical airlock of worn aluminium, the round
> inner hatch closed ahead. A thin white mist forms in the air and slowly
> thins away under one cold white-blue ceiling light. Camera locked.

**Narration:**
> Night hour thirty-one.
>
> About three hundred and twenty hours of battery. Dawn in about three hundred
> and twenty-three.
>
> Protocol seven does not allow entry to gallery three alone.
>
> Clamps checked. Both valves.
>
> Entering gallery three.

---

## SCENE 7 — CODA (3:30–3:45)

**Declared coda.** The recording has ended; this scene is the recovery frame
delivered as text, with no voice. It is exempt from the silence ceiling
because its only content is two cards the viewer must read, and the payoff of
the episode — the battery hour and the suit count — is deliberately withheld
from the voice.

**Shot 7.1** — static, 10 s, anchor A1
> Ground-level wide view across a crater floor still in deep black shadow
> toward a mountainous crater rim. The highest peaks of the rim catch the
> first hard white sunlight while everything below stays black. Black sky with
> small sharp stars. Camera locked. Nothing in the picture is lit but the
> peaks and the stars. Lower left of frame black and empty.

**Card 7.1**
```
RECORD ENDS  NIGHT HOUR 31
BATTERY 0 KWH  NIGHT HOUR 351
```

**Shot 7.2** — static, 5 s, text-to-image against the exterior macro spine
> Macro of fine pale grey regolith surface lit by low hard white light from
> the right, every grain casting a tiny black shadow. Camera locked. The
> surface is undisturbed with no track and no mark on it, and there is nothing
> above it or behind it. Lower left of frame in shadow and empty.

**Card 7.2**
```
SUITS IN GALLERY 3 AT DAWN: 6
```

---

## Pacing (assembly)

Defaults: 1.2 s between paragraphs, 2.0 s across scene cuts.

Card plate check (18 chars/s, 0.35 s between lines, 2 s hold):

| Card | Chars | Lines | Needs | Plate |
|---|---|---|---|---|
| 2.1 | 33 | 2 | 4.2 s | 10 s |
| 2.2 | 44 | 3 | 5.1 s | 10 s |
| 3.2 | 95 | 4 | 8.3 s | 10 s |
| 4.2 | 92 | 6 | 8.9 s | 10 s |
| 5.1 | 34 | 2 | 4.2 s | 10 s |
| 5.2 | 40 | 2 | 4.6 s | 10 s |
| 7.1 | 55 | 2 | 5.4 s | 10 s |
| 7.2 | 29 | 1 | 3.6 s | 5 s |

The figures above are the script's own arithmetic. The gate is `validate.py`,
which runs the real `card_end()` out of `build_cards.py`, so the table cannot
quietly disagree with the builder.

Non-default gaps:

- **Scene 1, after "On shift, one." — 2.0 s.** The headcount is the cost
  before the cause; it needs to land before the clamps line explains nothing.
- **Scene 4, before "Heart rate on all five suits…" — 2.0 s.** The flattest
  line in the scene; the gap is what makes it flat rather than rushed.
- **Scene 6, before "Entering gallery three." — 2.5 s.** Last words of the
  record. Nothing follows them but picture.
- **Scene 6 → Scene 7 — hard cut, 0 s gap.** The recording stops; the coda
  arrives without a transition. Room tone continues across the cut.

Every one of these falls on a paragraph boundary, which is the only place a
pause can be cut: the voice is generated one file per paragraph and the gaps
are inserted between those files.

Card-to-line alignment: every card plate starts within 2 s of the line it
answers to (2.1 with the night line, 2.2 with the draw line, 3.2 with
"Protocol seven.", 4.2 with "All five purge valves…", 5.1 with "Battery…",
5.2 with "Bus three is drawing…").

## Voice direction

One voice, the operator. Adult, American accent, a technician at the end of a
long shift — not frightened, not heroic. Reads the log as a form. Numbers are
spoken in full words and at exactly the pace of the words around them. No
emphasis on "by hand", "four turns", "normal" or "alone". The last line is
delivered exactly like the first: "Entering gallery three" sounds the same as
"Operator log".

## Sound design

- **Room tone** under the whole episode: station interior, a low steady air
  handler.
- **Recurring element — the air handler.** Established from Scene 1. In
  Scene 5, from "Bus three is drawing four hundred watts", a second, very
  faint steady electrical tone sits under the air handler and stays through
  Scene 6. On Shot 6.3 the air handler is gone and only the airlock pump and
  the faint tone remain. In the coda both are gone: only a thin exterior
  recorder hiss.
- **The air handler is the effect, not the floor.** A second, ungated bed runs
  under it for the whole record, including through 6.3 and the coda where the
  handler is off. Record 03 gated its only bed and two scenes fell to
  -90 dBFS: not silence, a file that has ended.
- Every level in `audio.yaml` is a trim on a measured file, never a target.
  Measure the bed first, then choose the sign.
- **Card clicks:** dry per glyph, under the narration level. Mixed by
  `build_cards.py`, never by hand.
- **Suit recorder texture:** narration carries a slight close-mic helmet
  character throughout (production choice of EQ).
- No music under the record. The teaser is the only piece allowed a cue.

## Verticals — three cuts, assembled

Assembled from `takes/`, not carved out of the master: a shot list in whatever
order works, each shot framed where its subject is, and a line list out of the
paragraphs the record already contains. Nothing is generated. Every figure in
every cut is spoken aloud; none of them depends on a card.

**V .a — The clamps.** Lines s1p3, s1p4, s1p5.
- Opens on "Station crew, six. On shift, one." Voice on the first frame.
- Ends on **"again."** Paragraph end, real silence after it.
- Picture: 1.3 (the five bare hooks), 1.2, 4.5, 4.3.
- Payload: six crew, one on shift, clamps on the valves, checked twice.

**V .b — Eleven seconds.** Lines s4p3, s4p4, s4p5, s4p6.
- Opens on "All five purge valves were opened by hand."
- Ends on **"opened."** End of the scene's narration.
- Picture: 4.2, 4.5, 3.4, 4.4, 3.3.
- Payload: five valves, by hand, eleven seconds, four turns, normal heart rate.

**V .c — Four hundred watts.** Lines s5p4, s5p5, s5p6, s6p2, s6p3.
- Opens on "Bus three is drawing four hundred watts."
- Ends on **"alone."** Real silence follows.
- Picture: 5.5, 5.2, 3.1, 5.4, 6.2, 3.4.
- Payload: the load, the isolated bus, the breaker in gallery three, three
  hundred and twenty hours against three hundred and twenty-three.

All three close on the channel's card, `WATCH THE FULL RECORD ON THE CHANNEL`.
Trim points come from `audio/alignment/`, and every one of them is checked for
real silence after the last word before it is written down.

## The teaser

Thirty seconds, vertical, out **before** the record. Assembled from takes in
which something physically moves, and from lines the record already contains.
It closes on `SOON`, not on the cuts' card: the record does not exist yet.

- Picture: 1.3, 3.4, 4.5, 3.3, 5.5, 2.3, 6.2.
- Lines: s1p3 ("Station crew, six. On shift, one."), s3p2 ("Five crew remain
  in gallery three."), s4p3 ("All five purge valves were opened by hand. First
  to last, eleven seconds."), s4p4 ("A purge valve takes four turns."), s4p6
  ("Heart rate on all five suits was normal until the valves opened."), s6p5
  ("Entering gallery three.").
- Nothing here explains anything else. The teaser never says what was in the
  void, and it never says what the battery does.
- Music is generated at ElevenLabs' music endpoint, never the sound-effect one
  and never licensed, and it stays in the teaser.

---

## Appendix — what is real and what is invented

### Real, verifiable

1. **Length of the lunar night.** The Moon is tidally locked, so a lunar day
   equals the synodic month, 29.530589 days. At a site near the lunar equator
   day and night are each about half of that:
   29.530589 / 2 = 14.765 days × 24 = **354.37 hours**, read as "about three
   hundred and fifty-four". Local topography shifts this by hours at a real
   site; the episode uses the half-synodic figure.
2. **Full moon on Earth is night on the far side.** At full moon the Sun is on
   the opposite side of the Moon from Earth, so the Earth-facing hemisphere is
   lit and the far side is dark.
3. **No line of sight to Earth from the far side.** Because of tidal locking
   the far side never faces Earth (apart from small libration effects at the
   limb), so a far-side station needs a relay for communication. Daedalus
   crater is a real far-side crater near the equator (about 6° S, 179° E).
4. **No atmosphere, hard shadows.** No air to scatter light: shadows have hard
   edges, there is no haze at distance, and the sky is black.
5. **Mist in a depressurising airlock.** Rapid pressure drop cools the
   remaining air; water vapour in it condenses into visible fog.
6. **Energy arithmetic** (E = P × t), all on the invented figures below:
   - Runtime at nightfall: 4000 kWh / 11.0 kW = **363.64 h**; margin
     363.64 − 354.37 = **9.27 h** (card: 9.3 H).
   - Expected at night hour 30: 4000 − 30 × 11.0 = **3670 kWh**.
   - Measured 3658 kWh: shortfall 12 kWh over 30 h = **0.40 kW** extra draw.
   - Total draw 11.4 kW. At night hour 31: 3658 − 11.4 = 3646.6 kWh;
     3646.6 / 11.4 = **319.9 h** of battery ("about three hundred and
     twenty"); dawn in 354.37 − 31 = **323.4 h** ("about three hundred and
     twenty-three"). Shortfall **about 3.5 h**.
   - Battery empty at 30 + 3658 / 11.4 = 30 + 320.9 = **350.9 h** — card
     "NIGHT HOUR 351".
   - If bus three had been isolated at night hour 31: 3646.6 / 11.0 =
     331.5 h → battery lasts to night hour **362.5**, past dawn. The coda's
     hour 351 therefore means the 0.40 kW load was still running.
7. **Timeline consistency:** drill breach at −64 h, purge valves opened at
   −60 h 14 min, relay lost at −40 h, nightfall at 0 h. Telemetry spread
   −60:14:07 to −60:14:18 = **11 s**, as spoken.

### Invented

- Daedalus Two station, its six-person crew and gallery three.
- Battery usable capacity 4000 kWh; survival draw 11.0 kW.
- Drill breach into a void at 41 m depth, at night minus 64 hours.
- Revised protocol seven and its three rules.
- Suit telemetry, suit numbering S1–S6, purge valve needing four turns,
  heart-rate data, valve clamps.
- Relay carrier loss at night minus 40 hours.
- Bus three topology (lights and drill head in gallery three, breaker inside
  gallery three).
- **The impossibility:** a steady 0.40 kW draw on bus three with every load
  on it isolated.
- Suit count in gallery three at dawn.
