# FC9-011 // "THE MANIFEST"

**Slug:** FC9-011 // THE MANIFEST
**Series:** 1 — The Last Operator
**Runtime:** 5:00 (300 s) — 33 shots, durations sum to 300 s exactly
**Per-scene seconds:** {1: 36, 2: 38, 3: 40, 4: 44, 5: 36, 6: 40, 7: 36, 8: 30} = 300
**Format:** 16:9 horizontal, three vertical cuts assembled out of it, one teaser
**Voice:** character (operator) — dry, procedural, first person. The sole
  operator of a transfer ship reading his burn reports back to himself. Every
  mass is read like a fuel figure. The last line is the flattest one in the
  record.
**Word count:** 419 (body, scenes 1–7). At 162 wpm that is 155.2 s of speech
  against 270 s of body — 42.5% silence. The coda carries no voice.
**Motion split:** 10 static / 9 local / 14 model (of the 14, six are repeats
  built from an existing take — `reuse_take` — so eight are paid rolls).
  No floating pencil: cut on 2026-11-10 (Serge), it had been in five records.
**Interiors, plus one exterior** (2.1). It takes its own spine and its own
  anchor; nothing is shared with the interior set.

### Per-scene silence

Measured at 162 wpm, stage directions stripped (`validate.py` recounts).

| Scene | Seconds | Words | Speech | Silence |
|---|---|---|---|---|
| 1 | 36 | 55 | 20.4 s | 43.4% |
| 2 | 38 | 52 | 19.3 s | 49.3% |
| 3 | 40 | 60 | 22.2 s | 44.4% |
| 4 | 44 | 73 | 27.0 s | 38.6% |
| 5 | 36 | 57 | 21.1 s | 41.4% |
| 6 | 40 | 64 | 23.7 s | 40.7% |
| 7 | 36 | 58 | 21.5 s | 40.3% |
| **Body 1–7** | **270** | **419** | **155.2 s** | **42.5%** |
| 8 (coda) | 30 | 0 | 0 | 100% — **declared coda**, exempt |

Scene 2 runs the most air: its four lines are four separate checks, each
closed before the next one starts. Scene 4 is the densest and the floor is
there if the takes land slow — the fix is picture on 4.4, not a cut line.

---

## Disclaimer

> Work of fiction. All records, objects and events are invented. Any resemblance to real missions is coincidental. The physics in this record is real and the arithmetic checks: mass estimated in flight from thrust and measured acceleration, center-of-mass tracking by engine gimbal trim, and the rocket equation for the return burn. The ship and everything in it do not exist.

---

## Synopsis

The sole operator of the transfer ship SEVER-5 reads the mass estimate the
guidance computer makes on every burn: thrust divided by acceleration. On the
first trajectory correction the ship comes out 312 kg heavier than the manifest
and the flow meters allow. The engine is only rated to 1.5%, so he logs it as
engine error.

On the second correction it is 489 kg, outside the rating. Chamber pressure
says the thrust was identical, and two accelerometers agree, so whatever bias
the engine has cancels between the two burns: the ship gained 177 kg in six
days. The airlock has not cycled since launch. The engine's gimbal trim says
the center of mass moved forward, and the two figures together put the new
mass four and a half meters forward — in the habitat module, where every
locker holds exactly what the manifest says and where his bunk is.

On the third correction it is 671 kg, and the rate is rising. Run back, the
growth starts at launch. He works the rocket equation for the return burn: the
margin is gone at 1,250 kg, in eighteen days, on day forty-one. The return
burn is on day sixty-one. The log ends there. The coda shows the ship flew the
return burn anyway.

The one invented thing: mass accumulating inside a sealed ship.

---

## Style spine (interiors)

> Matte warm-gray painted aluminum and off-white padded paneling, worn soft and dull along every edge that gets touched, faint scuffs and old adhesive marks, nothing polished and nothing new. One palette throughout: warm gray, off-white, dull brass, cold blue. The light is flat, cool and diffuse with no visible source. Contrast is low, shadows soft and shallow, blacks lifted and never crushed. No lettering, no markings, no numerals, no people.

## Exterior spine (2.1 only)

> Open space. Dull gray aluminum and gold-brown thermal blanket weathered and creased, seams and fastener rows catching hard sunlight from one side, the shadow side falling to near black. Black sky with no planet in it. One palette: warm gray, gold-brown, black. No lettering, no markings, no numerals, no flags, no people.

**Spine notes.** Neither spine names an object or a camera distance. The
interior spine says "paneling", not "module" or "cabin", so the macro anchor
(A2) is not dragged into a room. A different palette from record 09's station
(warm gray and dull brass, not bone and cold aluminum) — a different vessel.
The ship is weightless between burns: everything in a still is clipped,
strapped or seated in a recess. Under thrust, loose things hang aft; only the
shots that name a burn show that. Control surfaces imply indicator lamps, so
`static` and `local` prompts fill the row positively ("every switch in the row
in the same position, the metal around them dark") instead of saying "no
lamp".

## Anchors

- **A1 — wide module.** Camera at chest height, wide field, the full depth of a
  cylindrical module in frame, everything in focus.
- **A2 — macro instrument.** Long lens, the subject filling the frame edge to
  edge, background two stops down and unresolvable.
- **A3 — object head-on.** Normal lens, flat frontal, subject centered, a plain
  paneled surface behind it. Hatch, locker, porthole, bunk.
- **A4 — top-down surface.** Camera directly overhead, flat frontal plane, even
  coverage.
- **A5 — exterior.** The aft end of the ship, engine bell in the center third,
  black sky. Text-to-image, exterior spine; no interior anchor is passed.

**Repeat-subject rule.** The clamp on its lanyard (1.1) returns as 6.1 and 8.2
— the same swing, so both are `reuse_take` of `takes/1.1.mp4`. The flow meter
(1.4) returns as 6.4 (`reuse_take`). The chamber-pressure gauge (2.3) returns as 3.1
(`reuse_take`) — the same error on both burns, the same needle climbing the
same way. The nozzle on its gimbal (2.1) returns as 5.3 (`reuse_take`) under
"no scale on this ship but the engine". The gimbal actuator (4.1) returns as 8.4 (`reuse_take`). The
habitat module wide (1.2) is the master for 4.4, 6.2 and 8.1 (`ref_shot: 1.2`).
The work surface (1.3) is the master for every top-down sheet.

## On-screen text conventions

All cards: **Menlo, phosphor green RGB 150 255 190, 40 px on 1080p**, halo and
glow, no box, no scrim, lower left. Type-on at 18 ch/s, 0.35 s between lines,
2 s hold after the last character. Every card sits on a `static` plate framed
with its lower left empty. No screen in this record is green in-fiction. The
channel closer (8.5) is `pos: centre-high`.

---

## SCENE 1 — CORRECTION ONE (0:00–0:36)

Image first. No logo, no ident. The slug types into the lower left of 1.1 and
is gone by 4.5 s.

**Card (shot 1.2 — answers paragraph 2):**
```
TCM-1 / DAY 11
MASS, MEASURED  25,577 KG
MASS, EXPECTED  25,265 KG
TOLERANCE         ±379 KG
```
83 characters — 4.6 s typing, 1.05 s of line pauses, 2 s hold: 7.7 s on an
11 s plate. The tolerance line is still on screen when paragraph 3 names it.

**Shot 1.1** — model, 8 s, anchor A3 — **master take for the clamp**
> A steel spring clamp hanging from a short braided lanyard clipped to an aluminum handrail on a warm-gray paneled wall, the lanyard drawn straight toward the aft end of the module by the burn, flat cool light. *Motion:* the clamp swings slowly back and forth on its lanyard as one rigid piece, steadily, for the whole shot.

**Shot 1.2** — static, 11 s, anchor A1 — **master still for the habitat module**
> A cylindrical habitat module seen wide at chest height down its full length, off-white padded paneling and warm-gray aluminum handrails, every stowage strap pulled flat and buckled, a row of small locker doors along the right side all closed, flat cool diffuse light, the air in front of the subject completely clear, nothing in the frame loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 1.3** — local (slow push), 9 s, anchor A4 — **master still for the work surface**
> Directly overhead view of a small warm-gray aluminum work surface, a single sheet of ruled paper held flat under a steel clip bar and a pencil seated in a clip beside it, flat even cool light, the air above the surface completely clear, nothing loose or floating anywhere in frame

*On the sheet* (`paper.yaml`): one division worked in the margin —
`24,000 ÷ 0.9383 = 25,577`, the result ringed, `−25,265` under it, `+312`
underlined once, and beside it `ENGINE ±1.5%` with a tick.

**Shot 1.4** — model, 8 s, anchor A2 — **master take for the flow meter**
> Macro view through the round glass window of a propellant flow meter set into a brass-colored line, a small four-bladed turbine rotor inside it, flat cool light raking across the glass, background unresolvable. *Motion:* the rotor turns steadily and quickly for the whole shot.

**Narration:**
> *[over 1.1]* Day eleven. Trajectory correction one. The ship came out three hundred and twelve kilograms heavier than the manifest.
>
> *[over 1.2, with the card]* Thrust divided by acceleration is the mass of the ship. The computer works it out on every burn.
>
> *[over 1.3]* The engine is rated to one and a half percent. That covers it. I logged it as engine error.

---

## SCENE 2 — CORRECTION TWO (0:36–1:14)

**Card (shot 2.2 — answers paragraph 2):**
```
TCM-2 / DAY 17
MASS, MEASURED  25,448 KG
MASS, EXPECTED  24,959 KG
OFFSET   +489   ±374 KG
```
81 characters — 4.5 s typing, 1.05 s of pauses, 2 s hold: 7.6 s on a 10 s plate.

**Shot 2.1** — model, 10 s, anchor A5 (exterior)
> Exterior of the aft end of a ship in open space, a single dark bell-shaped rocket nozzle on a gimbal mount at the center of the frame, gold-brown thermal blanket and gray aluminum struts around its base lit hard from one side, black sky, no flame and no plume visible. *Motion:* the nozzle tilts slowly a few degrees to one side on its gimbal and back, as one rigid piece, steadily for the whole shot; the ship around it does not move.

**Shot 2.2** — static, 10 s, anchor A1
> A narrow cylindrical access tunnel seen wide at chest height looking aft, warm-gray aluminum ribs and off-white padded paneling, a closed round hatch at the far end, every cable run clipped flat into its tray, every switch in the side panel in the same position and the metal around them dark, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 2.3** — model, 8 s, anchor A2
> Extreme close view of a round pressure gauge in a dull brass bezel, a short arc of five plain engraved ticks across the lower half of the face and nothing else on it, one fine black needle, scratched glass, flat cool light from the left, background unresolvable. *Motion:* the needle climbs steadily from the first tick toward the third for the whole shot.

**Shot 2.4** — local (slow push), 10 s, anchor A3
> Two identical small gray instrument boxes bolted side by side to one aluminum bracket on a warm-gray paneled wall, a braided cable leaving each into the same conduit, both boxes plain and scuffed at the corners, every surface on them dark and unlit, flat cool light, the air completely clear, nothing hanging from the bracket or near it

**Narration:**
> *[over 2.1]* Day seventeen. Correction two. Four hundred and eighty-nine kilograms heavy.
>
> *[over 2.2, with the card]* That is outside the rating. Ground reads it as the engine losing thrust, or the accelerometer drifting.
>
> *[over 2.3]* Chamber pressure matches the first burn to point oh five percent. Same pressure, same thrust.
>
> *[over 2.4]* Both accelerometers agree with each other to point oh two.

---

## SCENE 3 — THE DIFFERENCE (1:14–1:54)

**Card (shot 3.2 — answers paragraph 2):**
```
DAY 11 TO DAY 17
MASS GAINED     177 KG
RATE     29.5 KG / DAY
```
60 characters — 3.3 s typing, 0.7 s of pauses, 2 s hold: 6.0 s on a 10 s plate.

**Shot 3.1** — model, 8 s, `reuse_take: {take: 2.3, from: 0.0}`
> The chamber-pressure gauge of 2.3, its needle climbing exactly as it did on correction two. No new roll. Fallback if 2.3 fails twice: a local push on the approved still of 2.4, the two identical IMUs.

**Shot 3.2** — static, 10 s, from the approved still of 1.3
> The same work surface as in 1.3, two sheets of ruled paper overlapping under the steel clip bar, the pencil seated in its clip, flat even cool light, the air above completely clear, nothing loose or floating, the lower left of the frame plain aluminum

*On the top sheet* (`paper.yaml`): `25,577` and `25,448` written one above
the other with their expected figures beside them, the two offsets `+312`
and `+489`, the difference `177` ringed, `÷ 6 = 29.5` under it.

**Shot 3.3** — local (slow push), 12 s, anchor A3
> A round airlock hatch head-on in a warm-gray paneled bulkhead, a thick aluminum door seated fully closed in its frame on one heavy hinge on the left, a central handwheel with a plain ribbed rim at rest, a dark rubber seal all the way around, flat cool light, nothing loose or hanging anywhere near it

**Shot 3.4** — model, 10 s, anchor A2 — **master take for the fan**
> Macro view through a round aluminum grille of a small five-bladed ventilation fan set into a duct, plain gray blades, flat cool light across the grille, background unresolvable. *Motion:* the fan turns steadily for the whole shot.

**Narration:**
> *[over 3.1]* Whatever the engine's error is, it is the same error on both burns. It cancels in the difference.
>
> *[over 3.2, with the card]* Between day eleven and day seventeen the ship gained one hundred and seventy-seven kilograms. Twenty-nine and a half a day.
>
> *[over 3.3]* The airlock has not cycled since launch. Nothing has docked.
>
> *[over 3.4]* Mass in a sealed ship goes one way. Out, through the engine.

---

## SCENE 4 — WHERE (1:54–2:38)

**Card (shot 4.2 — answers paragraph 2):**
```
TCM-2 / GIMBAL TRIM
OFF PREDICTION   0.55°
ARM                9 M
CG SHIFT    8.6 CM FWD
```
82 characters — 4.6 s typing, 1.05 s of pauses, 2 s hold: 7.6 s on an 11 s
plate.

**Shot 4.1** — model, 10 s, anchor A2 — **master take for the actuator**
> Macro view of a heavy gimbal actuator in an engine bay, a polished steel push rod emerging from a thick gray hydraulic cylinder, braided lines leaving the cylinder, flat cool light raking along the rod, background unresolvable. *Motion:* the rod slides slowly and steadily out of its cylinder for the whole shot, as one rigid piece.

**Shot 4.2** — static, 11 s, from the approved still of 2.2
> The same access tunnel as in 2.2, looking aft, the far hatch closed, every cable clipped flat, every switch in the same position, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 4.3** — local (slow push), 11 s, from the approved still of 1.3
> The same work surface as in 1.3, one fresh sheet of ruled paper under the clip bar, the pencil seated in its clip, flat even cool light, the air completely clear, nothing loose or floating

*On the sheet* (`paper.yaml`): the ship drawn side-on as a long box with the
engine at the left, a small cross for the center of mass, an arrow `8.6 cm`
pointing right, and the moment worked below it:
`489 × r = 25,448 × 0.086` — `r = 4.48 m`, ringed, with a second arrow
reaching from the cross into the forward end of the box.

**Shot 4.4** — local (slow push toward the far end), 12 s, from the approved
still of 1.2
> The same habitat module as in 1.2, the same closed lockers, every strap flat, flat cool light, the air completely clear, nothing loose, floating or hanging

**Narration:**
> *[over 4.1]* The engine sits on a gimbal and steers its thrust through the center of mass. On correction two it trimmed point five five degrees off the prediction.
>
> *[over 4.2, with the card]* Nine meters from the gimbal, that is eight point six centimeters. The center of mass moved forward.
>
> *[over 4.3]* Four hundred and eighty-nine kilograms, eight point six centimeters. I solved for where it sits.
>
> *[over 4.4]* Four and a half meters forward of the center of mass. The habitat module.

---

## SCENE 5 — THE LOCKERS (2:38–3:14)

**Card (shot 5.2 — answers paragraph 2):**
```
WATER     81 L   LOGGED
FOOD    142 KG   LOGGED
WASTE    38 KG   LOGGED
ITEMS  206 OF 206
```
83 characters — 4.6 s typing, 1.05 s of pauses, 2 s hold: 7.7 s on a 9 s plate.

**Shot 5.1** — model, 10 s, anchor A3
> A small square locker door head-on in a row of identical closed lockers set into off-white padded paneling, plain aluminum frame, a recessed flat latch, flat cool light. *Motion:* the door swings slowly open on its hinge as one rigid piece, steadily for the whole shot, into a shallow dark compartment.

**Shot 5.2** — static, 9 s, anchor A3
> A row of small square locker doors head-on in off-white padded paneling, every one of them closed and latched, every latch in the same position, plain aluminum frames, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 5.3** — model, 8 s, `reuse_take: {take: 2.1, from: 1.0}`
> The nozzle of 2.1 tilting on its gimbal, under "no scale on this ship but the engine". No new roll.

**Shot 5.4** — local (slow push), 9 s, anchor A3
> A sleeping alcove head-on in off-white padded paneling, a sleeping bag strapped flat against the back wall under two buckled straps, its zip closed, a small round reading lamp above it switched off and dark, flat cool light, the air completely clear, nothing loose, floating or hanging

**Narration:**
> *[over 5.1]* Day eighteen. I opened every locker in the habitat module. Two hundred and six items. Every one is on the manifest.
>
> *[over 5.2, with the card]* Water, food, waste, as logged. What moves inside the ship does not change its mass.
>
> *[over 5.3]* Between burns nothing weighs anything. There is no scale on this ship but the engine.
>
> *[over 5.4]* The bunk is in this module.

---

## SCENE 6 — CORRECTION THREE (3:14–3:54)

**Card (shot 6.2 — answers paragraph 2):**
```
TCM-3 / DAY 23
OFFSET        +671 KG
GIMBAL TRIM     0.76°
POSITION    4.5 M FWD
```
78 characters — 4.3 s typing, 1.05 s of pauses, 2 s hold: 7.4 s on an 11 s
plate.

**Shot 6.1** — model, 8 s, `reuse_take: {take: 1.1, from: 0.0}`
> The clamp of 1.1, swinging on its lanyard under the burn. No new roll.

**Shot 6.2** — static, 11 s, from the approved still of 1.2
> The same habitat module as in 1.2, seen from the same height, every locker closed, every strap flat, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 6.3** — local (slow pull back), 13 s, from the approved still of 1.3
> The same work surface as in 1.3, three sheets overlapping under the clip bar, the pencil seated in its clip, flat even cool light, the air completely clear, nothing loose or floating

*On the top sheet* (`paper.yaml`): a plot, `DAY` along the bottom and `KG`
up the side, three points ringed at 11, 17 and 23 and labelled `312`, `489`,
`671`, a line through them bending very slightly upward, and the same line
carried back as a dashed stroke to the corner at `0`.

**Shot 6.4** — model, 8 s, `reuse_take: {take: 1.4, from: 0.0}`
> The flow meter of 1.4, its rotor turning. No new roll.

**Narration:**
> *[over 6.1]* Day twenty-three. Correction three. Six hundred and seventy-one kilograms heavy.
>
> *[over 6.2, with the card]* Gimbal trim point seven six degrees. The same place, four and a half meters forward.
>
> *[over 6.3]* One hundred and eighty-two kilograms in six days. Thirty point three a day. The rate is rising.
>
> *[over 6.4]* Run the line back and it reaches zero on the day of launch. The three hundred and twelve was not the engine.

---

## SCENE 7 — THE RETURN BURN (3:54–4:30)

**Card (shot 7.2 — answers paragraph 2):**
```
RETURN BURN / DAY 61
REQUIRED   1,644 M/S
MANIFEST   1,756 M/S
DAY 23     1,694 M/S
```
80 characters — 4.4 s typing, 1.05 s of pauses, 2 s hold: 7.5 s on a 10 s plate.

**Shot 7.1** — local (slow push), 9 s, from the approved still of 1.3
> The same work surface as in 1.3, one fresh sheet under the clip bar, the pencil seated in its clip, flat even cool light, the air completely clear, nothing loose or floating

*On the sheet* (`paper.yaml`): the rocket equation written out at the top,
`Δv = 3138 · ln(m0 / m1)`, then three lines under it —
`14,000 → 1,756`, `14,671 → 1,694`, `15,250 → 1,644` — the last one ringed.

**Shot 7.2** — static, 10 s, from the approved still of 1.2
> The same habitat module as in 1.2, every locker closed, every strap flat, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 7.3** — model, 9 s, anchor A3
> A round porthole head-on in off-white padded paneling, a plain aluminum ring around the glass, through it black space with a field of small sharp stars, flat cool light inside the module. *Motion:* the star field turns slowly and steadily across the window as the ship rotates, every star keeping its place relative to the others.

**Shot 7.4** — local (slow push), 8 s, from the approved still of 1.3
> The same work surface as in 1.3, the sheet from 7.1 on top, the pencil seated in its clip, flat even cool light, the air completely clear, nothing loose or floating

*On the sheet* (`paper.yaml`): the sheet of 7.1 with one more line under the
ringed one — `1,250 − 671 = 579`, `579 ÷ 30.3 ≈ 19`, the `19` struck through
and `18` written beside it, and below everything `DAY 41` underlined twice.

**Narration:**
> *[over 7.1]* The return burn needs one thousand six hundred and forty-four meters per second.
>
> *[over 7.2, with the card]* At manifest mass the tanks give one thousand seven hundred and fifty-six. Today, one thousand six hundred and ninety-four.
>
> *[over 7.3]* The margin is gone at twelve hundred and fifty kilograms. At the rising rate, in eighteen days.
>
> *[over 7.4]* Day forty-one. The return burn is on day sixty-one.

---

## SCENE 8 — CODA (4:30–5:00)

**Declared coda** (`coda: [8]`). Cards only, no voice. It carries what the
ship's own telemetry shows after the last entry, and the channel closer. The
two `model` shots between the plates are the ship flying its return burn with
nobody logging it: the clamp hangs aft again, the actuator steers.

**Shot 8.1** — static, 7 s, from the approved still of 1.2
> The same habitat module as in 1.2, empty, every strap flat and buckled, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Card on 8.1:**
```
SEVER-5
NO LOG ENTRIES AFTER DAY 23
```
34 characters — 4.2 s on a 7 s plate.

**Shot 8.2** — model, 5 s, `reuse_take: {take: 1.1, from: 2.0}`
> The clamp of 1.1, swinging on its lanyard under a burn. No new roll.

**Shot 8.3** — static, 8 s, from the approved still of 1.3
> The same work surface as in 1.3, empty, the steel clip bar closed on nothing, a pencil clip with nothing in it, flat even cool light, the air completely clear, nothing loose or floating, the lower left of the frame plain aluminum

**Card on 8.3:**
```
RETURN BURN, DAY 61
MASS         +1,936 KG
DELTA-V  1,588 OF 1,644
```
63 characters — 6.2 s on an 8 s plate.

**Shot 8.4** — model, 4 s, `reuse_take: {take: 4.1, from: 3.0}`
> The actuator of 4.1, its rod sliding. No new roll.

**Shot 8.5** — static, 6 s, from the approved still of 2.2
> The same access tunnel as in 2.2, the far hatch closed, flat cool light, the air completely clear, nothing loose, floating or hanging, the center of the frame a plain empty panel

**Card on 8.5 — channel closer** (`pos: centre-high`):
```
FILE CLASS NINE
FC9-011 // THE MANIFEST
```
38 characters — 4.5 s on a 6 s plate. The fiction line is in the description.

---

## Pacing (assembly)

Defaults: 1.2 s between paragraphs, 2.0 s across a scene cut. Speed pinned.

Non-default gaps, every one on a paragraph boundary:

- **2.0 s before "Mass in a sealed ship goes one way."** (Scene 3 ¶4). The rule
  of the record, stated once; it needs to arrive by itself.
- **2.5 s before "Four and a half meters forward of the center of mass."**
  (Scene 4 ¶4). The answer to a sum he has just said he did.
- **2.5 s before "The bunk is in this module."** (Scene 5 ¶4). The flattest
  line before the last one. Nothing after it in the scene.
- **2.0 s before "Run the line back…"** (Scene 6 ¶4).
- **3.0 s before "Day forty-one. The return burn is on day sixty-one."**
  (Scene 7 ¶4). The last line of the record arrives alone.

---

## Voice direction

- First person, the tense of a log. He is filling in a burn report.
- Never describe what is on screen. Never explain the implication — not of the
  growth, not of where it sits, not of the bunk, not of the dates.
- Every mass is read like a propellant figure. "Six hundred and seventy-one
  kilograms heavy" has the weight of "nominal".
- "The bunk is in this module" is a location, not a confession.
- The last line is two dates. No rising inflection on either.

---

## Sound design

Under the record: the channel floor and one cue, ducked 7 dB under the voice.
Nothing else runs under it.

**Music prompt** (ElevenLabs music, full runtime, 300 s):

> Slow ambient cue for a small sealed ship in deep space. Sustained mid-register strings and soft glassy pads, roughly 200 Hz to 3 kHz, cold and even. No melody anyone could hum, no beat, no drums, no vocals, no swell, no resolution. Quiet enough to sit under a calm speaking voice throughout. One long shape: a faint weight that thickens very slowly and never resolves.

**Spot effects** — 8, each in a pause, each a natural event with a body.
Offsets are first estimates; they are placed against the real takes so each
sits at least 0.3 s clear of a word.

1. `1.4 at 2.0 s` — a low muffled shudder through a metal hull as an engine burn cuts off, one soft deep thump, close, dry, about 1 s.
2. `2.1 at 8.5 s` — a single low creak of an aluminum frame taking load, close, dry, short.
3. `3.3 at 6.0 s` — a heavy hatch seal settling in its frame, one deep soft thud, close, dry.
4. `4.4 at 9.0 s` — one soft muffled knock of a panel settling, close, with body, no ring.
5. `5.1 at 6.5 s` — a small locker latch releasing, one dull plastic-and-metal clack, close, dry.
6. `5.4 at 6.0 s` — the same low creak as 2, deeper, once.
7. `6.4 at 5.5 s` — the same low hull shudder as 1, a burn ending.
8. `7.3 at 6.0 s` — one soft muffled knock of a hull panel as it cools, close, with body.

No spot effects in verticals or the teaser.

---

## Verticals — three cuts

Line list plus shot list. Lines are paragraphs the record contains, trimmed
only from the head. Every figure is spoken. All shots named are `model`.

Each cut **opens on its strangest figure**, its lines run **back to back** —
the second within 0.3 s of the first, every later gap at most 0.6 s — and it
runs **15–25 s** of picture before the closing card. Durations are estimates
at 162 wpm; the real word timings decide `at:` and `validate.py` checks the
gaps.

### FC9-011.a // "312 kg. Then 489. The Airlock Never Opened" (~18 s + card)

- **Lines:** S1 ¶1 → S2 ¶1 → S3 ¶3 → S3 ¶4.
  "Day eleven. Trajectory correction one. The ship came out three hundred and
  twelve kilograms heavier than the manifest." / "Day seventeen. Correction
  two. Four hundred and eighty-nine kilograms heavy." / "The airlock has not
  cycled since launch. Nothing has docked." / "Mass in a sealed ship goes one
  way. Out, through the engine."
- **Shots:** 1.1, 2.1, 1.4, 3.4 — the swinging clamp first, so something moves
  in frame one.
- **In-point:** on "Day eleven" — voice at 0.2 s.
- **Framing:** 1.1 window on the clamp; 2.1 centered on the nozzle.
- **Out-point:** last word "engine", end of a paragraph.

### FC9-011.b // "The Extra 671 kg Sits 4.5 Meters Forward" (~17 s + card)

- **Lines:** S6 ¶1 → S6 ¶2 → S4 ¶4 → S5 ¶4.
  "Day twenty-three. Correction three. Six hundred and seventy-one kilograms
  heavy." / "Gimbal trim point seven six degrees. The same place, four and a
  half meters forward." / "Four and a half meters forward of the center of
  mass. The habitat module." / "The bunk is in this module."
- **Shots:** 4.1, 2.1, 5.1, 1.4.
- **In-point:** on "Day twenty-three" — voice at 0.2 s.
- **Framing:** 5.1 window on the hinge side, where the door's edge travels.
- **Out-point:** last word "module", end of a paragraph.
- **Note:** ¶2 and S4 ¶4 both say "four and a half meters forward" back to
  back. Read on the takes; if it sounds like a stutter, drop S6 ¶2 and the
  cut runs ~13 s, under the floor — then add S3 ¶4 at the head instead.

### FC9-011.c // "The Margin Is Gone In 18 Days. The Burn Is In 38" (~21 s + card)

- **Lines:** S6 ¶3 → S7 ¶1 → S7 ¶3 → S7 ¶4.
  "One hundred and eighty-two kilograms in six days. Thirty point three a day.
  The rate is rising." / "The return burn needs one thousand six hundred and
  forty-four meters per second." / "The margin is gone at twelve hundred and
  fifty kilograms. At the rising rate, in eighteen days." / "Day forty-one.
  The return burn is on day sixty-one."
- **Shots:** 1.4, 7.3, 4.1, 1.1.
- **In-point:** on "One hundred" — voice at 0.2 s.
- **Framing:** 7.3 centered on the porthole.
- **Out-point:** last word "sixty-one", end of a paragraph and of the record's
  voice.

---

## Teaser — five lines, in order

Lines back to back (same gap limits as a cut); the teaser keeps its 30 s.

1. "Day eleven. Trajectory correction one. The ship came out three hundred and twelve kilograms heavier than the manifest." (S1 ¶1)
2. "Mass in a sealed ship goes one way. Out, through the engine." (S3 ¶4)
3. "Day seventeen. Correction two. Four hundred and eighty-nine kilograms heavy." (S2 ¶1)
4. "Four and a half meters forward of the center of mass. The habitat module." (S4 ¶4)
5. "Day twenty-three. Correction three. Six hundred and seventy-one kilograms heavy." (S6 ¶1)

About 24 s of voice. Ends on `SOON`. Related video is set the day the record
goes public (see `publish.md`).

---

## Open production decisions

- **The exterior (2.1)** is the only shot outside. If the nozzle comes back
  with a flame, a plume or the ship drifting, it is rebuilt as a `local` push
  on the approved still — the gimbal motion is also carried by 4.1.
- **The star field (7.3)** is new on this channel: a rigid field turning is
  the same class of motion as clouds sliding under the station in record 09,
  but untested. If the stars smear or multiply, 7.3 becomes a `local` push on
  the approved still and the motion of scene 7 is the push.
- **Reuse takes** (3.1, 5.3, 6.1, 6.4, 8.2, 8.4) depend on the master takes having
  a clean stretch long enough at the stated `from`. Check at stage 6.

---

## Appendix — what is real and what is invented

### Real, verifiable

**Mass from thrust and acceleration.** Guidance computers estimate vehicle
mass in flight from m = F / a, using the commanded thrust and the measured
acceleration; it is how a propellant budget is cross-checked during a burn.

**The engine.** Thrust F = 24.0 kN, specific impulse 320 s, so exhaust velocity
v_e = 320 × 9.80665 = **3,138 m/s** and mass flow ṁ = F / v_e = **7.65 kg/s**.
A 40 s correction burn uses **306 kg**; the mid-burn mass is the pre-burn mass
less 153 kg.

**Propellant and expected mass.** Dry mass by manifest 14,000 kg. Propellant
before TCM-1 11,418 kg; after each 40 s burn 306 kg less — 11,112, 10,806, and
**10,500 kg** after TCM-3. Expected mid-burn mass: TCM-1 14,000 + 11,265 =
**25,265 kg**; TCM-2 **24,959 kg**; TCM-3 **24,653 kg**.

**The three estimates.** Measured accelerations 0.93834, 0.94310 and
0.94772 m/s² give 24,000 / a = **25,577**, **25,448** and **25,324 kg** —
offsets of **+312**, **+489** and **+671 kg**.

**Tolerance.** A ±1.5% thrust uncertainty is a ±1.5% mass uncertainty:
±379 kg at TCM-1 (312 inside it), ±374 kg at TCM-2 (489 outside it).

**Why the difference is real.** Thrust is set by chamber pressure through the
nozzle's thrust coefficient and throat area: F = C_F · p_c · A_t. Same engine,
same throat, chamber pressure equal to 0.05%, so the thrust of both burns is
equal to 0.05% whatever its absolute error. The bias divides out of the
comparison and the change in offset, 489 − 312 = **177 kg** in six days
(**29.5 kg/day**), stands at about ±13 kg. Two independent IMUs agreeing to
0.02% rules out an accelerometer scale drift of that size.

**A sealed ship's mass is constant except for what leaves it.** Consumables
moved, eaten or stored change where mass sits, not how much there is; the
airlock and docking ports are the only ways in. Micrometeoroid accretion is
grams per year.

**Center of mass by gimbal trim.** The engine is gimbaled so its thrust line
passes through the center of mass; any offset of the CG from prediction shows
up as a steady trim angle. With the gimbal pivot 9.0 m aft of the CG, a trim
θ means a lateral CG offset d = 9.0 × tan θ: **0.55° → 8.6 cm**,
**0.76° → 11.9 cm**. (Simplified: the operator reads the axis the ship was
pointed on that burn as the ship's long axis. Invented geometry, real method.)

**Locating the added mass.** An added mass X at distance r from the CG shifts
it by d = X · r / M. At TCM-2: r = 0.086 × 25,448 / 489 = **4.48 m**. At TCM-3:
d = 671 × 4.48 / 25,324 = 0.119 m, which is a trim of **0.76°** — the same
place.

**Weightlessness.** Between burns the ship and everything in it fall together;
no scale on board reads anything. Mass is only visible while the engine
accelerates the ship.

**The growth.** Offsets +312, +489, +671 at days 11, 17, 23. Rates
28.4 (days 0–11), 29.5 (11–17), **30.3 kg/day** (17–23). A rate rising
linearly, r(t) = 27.67 + 0.133 t kg/day, reproduces all three: 312.4, 489.6,
671.2 kg — and gives zero at t = 0, the day of launch.

**The rocket equation.** Δv = v_e · ln(m₀ / m₁), with 10,500 kg of propellant:
- manifest mass (14,000 dry): 3,138 × ln(24,500 / 14,000) = **1,756 m/s**;
- day 23 (14,671 dry): 3,138 × ln(25,171 / 14,671) = **1,694 m/s**;
- the return burn needs **1,644 m/s**, which is reached at a dry mass of
  **15,250 kg** — an added **1,250 kg**.

**Days to the limit.** 1,250 − 671 = 579 kg. At a constant 30.3 kg/day:
19.1 days. At the rising rate (30.73 kg/day at day 23, +0.133 per day):
30.73 t + 0.0667 t² = 579 → t = **18.1 days**, **day 41**. The return burn is
scheduled for **day 61**.

**The coda.** At day 61 the same law gives 27.67 × 61 + 0.0667 × 61² =
**1,936 kg** added; 3,138 × ln(26,436 / 15,936) = **1,588 m/s** against the
1,644 required.

### Invented

The ship SEVER-5, its engine (24 kN, 320 s), its dry mass and propellant load,
the gimbal arm, the habitat module's position, the burn schedule (days 11, 17,
23, 61), the locker count and consumables figures, the accelerometer
agreement. Every measured acceleration.

**The one impossible thing:** mass accumulating inside a sealed ship — about
thirty kilograms a day, rising, since launch, four and a half meters forward
of the center of mass.
