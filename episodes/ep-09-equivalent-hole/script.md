# FC9-009 // "THE EQUIVALENT HOLE"

**Slug:** FC9-009 // THE EQUIVALENT HOLE
**Series:** 1 — The Last Operator
**Runtime:** 4:30 (270 s) — 32 shots, durations sum to 270 s exactly
**Per-scene seconds:** {1: 34, 2: 36, 3: 30, 4: 40, 5: 44, 6: 30, 7: 26, 8: 30} = 270
**Format:** 16:9 horizontal, three vertical cuts assembled out of it, one teaser
**Voice:** character (operator) — dry, procedural, first person. A technician
  reading a leak check back to himself. Every figure read like "shift
  complete". The last line of the record is the flattest one in it.
**Word count:** 381. At 162 wpm that is 141.1 s of speech against 240 s of
  body — 41.2% silence; scenes 1–3 at 36–40% (Serge, 2026-10-26: a little more
  voice, still above the one-third floor). The coda carries no voice.
**Motion split:** 10 static / 8 local / 14 model
**Interiors, plus two exteriors** (3.1, 6.2). They take their own spine and
  their own anchor; nothing is shared with the interior set.

### Per-scene silence

Measured at 162 wpm, stage directions stripped (`validate.py` recounts).

| Scene | Seconds | Words | Speech | Silence |
|---|---|---|---|---|
| 1 | 34 | 55 | 20.4 s | 40.1% |
| 2 | 36 | 62 | 23.0 s | 36.2% |
| 3 | 30 | 51 | 18.9 s | 37.0% |
| 4 | 40 | 63 | 23.3 s | 41.7% |
| 5 | 44 | 68 | 25.2 s | 42.8% |
| 6 | 30 | 46 | 17.0 s | 43.2% |
| 7 | 26 | 36 | 13.3 s | 48.7% |
| **Body 1–7** | **240** | **381** | **141.1 s** | **41.2%** |
| 8 (coda) | 30 | 0 | 0 | 100% — **declared coda**, exempt |

Scenes 1–3 sit at 36–40%, which is the new target. Scenes 4–7 run longer
silences on purpose: each one ends on a figure that needs air after it (see
Pacing), and scene 7's last shot is a silent push into the open module. If
the takes land slow, scenes 1–3 are the ones near the floor, and the fix is
picture, not a cut line.

---

## Disclaimer

> Work of fiction. All records, objects and events are invented. Any resemblance to real missions is coincidental. The leak physics in this record is real and the arithmetic checks: choked flow through an orifice into vacuum, pressure decay in a sealed volume, the equivalent-hole method used to size real station leaks. The station and everything in it do not exist.

---

## Synopsis

The sole operator of station PROSVET-4 finds the air makeup valve cycling in
the night. He shuts it, lets the cabin fall for four hours and turns the drop
into a hole: 1.4 mm equivalent, nineteen kilograms of air a day, fifteen days
of reserve. Closing the hatches one by one puts the leak in module C, behind a
panel he cannot open to the hull. Ground orders hatch three kept shut until an
inspection on day forty, and the station is safe.

Then the arithmetic starts disagreeing with the world. Corrected for the
falling pressure, the hole in module C is 1.1 mm on day three, 0.6 mm on day
five. Holes in a hull get larger or stay. The oxygen fraction inside the sealed
module drops, which a leak cannot do. On day six the pressure in C has not
moved for thirty-one hours. On day seven he equalises, opens hatch three, and
logs the problem as resolved. The log ends there.

The one invented thing: a hole that closes.

---

## Style spine (interiors)

> Bone-coloured fabric-covered panelling and brushed aluminium, worn soft and greyed along every edge that gets touched, faint scuffs and old adhesive marks, matte, nothing polished and nothing new. One palette throughout: bone, aluminium grey, cold blue. The light is flat, cool and diffuse with no visible source. Contrast is low, shadows soft and shallow, blacks lifted and never crushed. No lettering, no markings, no numerals, no people.

## Exterior spine (3.1, 6.2 only)

> Open space. Aluminium and white thermal blanket weathered to a dull ivory, seams and fastener rows catching hard sunlight from one side, the shadow side falling to near black. Black sky, the Earth below in blue and white. One palette: ivory, aluminium grey, cold blue, black. No lettering, no markings, no numerals, no flags, no people.

**Spine notes.** Neither spine names an object or a camera distance. The
interior spine says "panelling", not "module" or "interior", so the macro
anchor (A2) is not dragged into a room. The station is weightless: everything
in a still is clipped, strapped or seated in a recess, and nothing "rests" on a
surface. Control surfaces imply indicator lamps, so `static` and `local`
prompts fill the row positively ("every switch in the row in the same position,
the metal around them dark") instead of saying "no lamp".

## Anchors

- **A1 — wide module.** Camera at chest height, wide field, the full depth of a
  cylindrical module in frame, everything in focus.
- **A2 — macro instrument.** Long lens, the subject filling the frame edge to
  edge, background two stops down and unresolvable.
- **A3 — object head-on.** Normal lens, flat frontal, subject centred, a plain
  panelled surface behind it. Hatch, valve, panel, porthole.
- **A4 — top-down surface.** Camera directly overhead, flat frontal plane, even
  coverage.
- **A5 — exterior.** Wide, hull in the foreground third, the Earth filling the
  lower half. Text-to-image, exterior spine; no interior anchor is passed.

**Repeat-subject rule.** Hatch three is generated once (2.1) and every later
hatch shot — 3.3, 5.4, 7.2 — references the approved 2.1. The gauge of 4.1
returns as 5.5 from the approved 4.1. The floating pencil of 3.4 returns as 6.3
and 8.2 from the approved 3.4. The fan of 2.4 returns as 8.4 from the approved
2.4.

## On-screen text conventions

All cards: **Menlo, phosphor green RGB 150 255 190, 40 px on 1080p**, halo and
glow, no box, no scrim, lower left. Type-on at 18 ch/s, 0.35 s between lines,
2 s hold after the last character. Every card sits on a `static` plate framed
with its lower left empty. No screen in this record is green in-fiction.

---

## SCENE 1 — COLD OPEN (0:00–0:34)

Image first. No logo, no ident. The slug types into the lower left of 1.1 and
is gone by 4.5 s.

**Card (shot 1.3 — answers paragraph 3):**
```
DECAY TEST         4 H
CABIN        -1.96 kPa
EQUIV HOLE      1.4 mm
RESERVE        15 DAYS
```
86 characters — 4.8 s typing, 1.05 s of line pauses, 2 s hold: 7.9 s on a 10 s
plate. The reserve line lands a few seconds before paragraph 4 says it, which
reads as the instrument getting there first.

**Shot 1.1** — model, 5 s, anchor A2
> Extreme close view of a small round indicator lamp set into a brushed aluminium valve panel beside a gas line union, the lamp lit a cold pale blue, flat cool light, background unresolvable. *Motion:* the lamp blinks off and on, steadily, three times.

**Shot 1.2** — model, 10 s, anchor A3
> A gas valve head-on on a bone-coloured panelled wall, a heavy aluminium handwheel with a plain ribbed rim and three spokes, a short braided line running from it into the panel, flat cool light from no visible source. *Motion:* the handwheel turns a quarter turn clockwise and stops.

**Shot 1.3** — static, 10 s, anchor A1
> A cylindrical station module seen wide at chest height down its full length, bone-coloured fabric panelling and brushed aluminium handrails, every stowage strap pulled flat and buckled, flat cool diffuse light, the air in front of the subject completely clear, nothing in the frame loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 1.4** — local (slow push), 9 s, anchor A4
> Directly overhead view of a small aluminium work surface with a closed logbook held flat under a steel clip bar and a pencil seated in a clip beside it, the cover worn pale at the corners, flat even cool light, the air above the surface completely clear, nothing loose or floating anywhere in frame

**Narration:**
> *[over 1.1]* Day one. Oh-three-forty. The makeup valve has opened eleven times since midnight.
>
> *[over 1.2]* I closed it at oh-three-fifty-two and let the cabin fall for four hours. One point nine six kilopascals.
>
> *[over 1.3, with the card]* The equivalent hole is one point four millimetres across.
>
> *[over 1.4]* Nineteen point seven kilograms of air a day. At that rate, the reserve lasts fifteen days.

---

## SCENE 2 — HATCH BY HATCH (0:34–1:10)

**Card (shot 2.2 — answers paragraph 2):**
```
MODULE A   0.00 kPa/h
MODULE B   0.00 kPa/h
MODULE C  -2.31 kPa/h
```
63 characters — 3.5 s typing, 0.7 s of pauses, 2 s hold: 6.2 s on an 8 s plate.

**Shot 2.1** — model, 10 s, anchor A3 — **master still for hatch three**
> A round pressure hatch head-on in a bone-coloured panelled bulkhead, a thick aluminium door on one heavy hinge on the left, a central handwheel with a plain ribbed rim, a dark rubber seal around the frame, the door standing half open into a dim aluminium module beyond, flat cool light. *Motion:* the door swings closed on its hinge as one rigid piece and seats in its frame.

**Shot 2.2** — static, 8 s, anchor A1
> A second cylindrical module seen wide at chest height, aluminium equipment racks along both sides with every latch closed and every handle in the same position, the metal around them dark, flat cool light, the air completely clear, nothing loose, floating or hanging in frame, the lower left of the frame a plain empty panel

**Shot 2.3** — local (slow push), 8 s, anchor A3
> An bone-coloured fabric-covered wall panel head-on, a square of panel framed by a neat row of flush aluminium fasteners on each side, the fabric scuffed grey along its lower edge, flat cool light, the air completely clear, nothing hanging from the panel or near it

**Shot 2.4** — model, 10 s, anchor A2 — **master still for the fan**
> Macro view through a round aluminium grille of a small five-bladed ventilation fan set into a duct, plain grey blades, flat cool light across the grille, background unresolvable. *Motion:* the fan turns steadily for the whole shot.

**Narration:**
> *[over 2.1]* Oh-nine-hundred. I closed the hatches one at a time and ran the same test on each module.
>
> *[over 2.2, with the card]* A and B hold. Module C loses two point three kilopascals an hour.
>
> *[over 2.3]* The ultrasonic detector finds it behind panel C-fourteen. A steady hiss at forty kilohertz.
>
> *[over 2.4]* Behind the panel there are forty millimetres of insulation, then the hull. From inside, I cannot reach it.

---

## SCENE 3 — THE RULE (1:10–1:40)

**Card (shot 3.2 — answers paragraph 2):**
```
HATCH 3    CLOSED
INSPECTION DAY 40
```
34 characters — 1.9 s typing, 0.35 s pause, 2 s hold: 4.3 s on an 8 s plate.

**Shot 3.1** — model, 10 s, anchor A5 (exterior)
> Exterior of an orbital station in hard sunlight, a short aluminium boom in the foreground carrying a boxy camera housing pointed away from the viewer towards a round docking port, the Earth filling the lower half of the frame with bands of white cloud over blue ocean, black sky above. *Motion:* the Earth's surface slides slowly and steadily beneath the station, clouds travelling left to right; the station and the boom do not move.

**Shot 3.2** — static, 8 s, anchor A4
> Directly overhead view of the same small aluminium work surface, a single sheet of ruled paper held flat under a steel clip bar, a pencil seated in a clip beside it, flat even cool light, the air above completely clear, nothing loose or floating, the lower left of the frame plain aluminium

*On the sheet* (`paper.yaml`, drawn onto the still): the station as three boxes in a row, the gap to C pressed shut with two hard strokes, C hatched, one arrow out through its wall; under it the first four-hour decay, a shallow fall with its end ringed. No letters, no numerals.

**Shot 3.3** — local (slow push), 7 s, from the approved still of 2.1
> The same round pressure hatch as in 2.1, now fully closed and seated in its frame, the handwheel at rest, flat cool light, nothing loose or hanging anywhere near it

**Shot 3.4** — model, 5 s, anchor A1 — **master still for the pencil**
> A cylindrical module seen wide at chest height, bone-coloured panelling and aluminium handrails, a single plain grey pencil floating free in the middle of the frame a metre from the camera, flat cool light. *Motion:* the pencil turns slowly end over end as it drifts a few centimetres to the right.

**Narration:**
> *[over 3.1]* The external camera is fixed on the docking port. Repointing it needs a walk outside.
>
> *[over 3.2, with the card]* Ground's instruction. Hatch three stays closed until the inspection on day forty.
>
> *[over 3.3]* Module C is sealed. The station holds. The reserve is no longer the problem.
>
> *[over 3.4]* I logged it as contained and slept for six hours.

---

## SCENE 4 — DAY THREE (1:40–2:20)

**Card (shot 4.2 — answers paragraph 2):**
```
DAY 3 / MODULE C
PRESSURE    42.3 kPa
HALF-LIFE       49 H
EQUIV HOLE    1.1 mm
```
76 characters — 4.2 s typing, 1.05 s of pauses, 2 s hold: 7.3 s on a 10 s plate.

**Shot 4.1** — model, 10 s, anchor A2 — **master still for the gauge**
> Extreme close view of a round pressure gauge in a brushed aluminium bezel, a short arc of five plain engraved ticks across the lower half of the face and nothing else on it, one fine black needle, scratched glass, flat cool light raking from the left, background unresolvable. *Motion:* the needle sinks steadily from the fourth tick towards the third.

**Shot 4.2** — static, 10 s, anchor A1
> The first module seen wide from its far end at chest height, looking back towards a closed round hatch, bone-coloured panelling, aluminium handrails, every strap flat and buckled, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 4.3** — local (slow pull back), 10 s, anchor A4
> Directly overhead view of the small aluminium work surface, three sheets of ruled paper overlapping under one steel clip bar, a pencil seated in a clip beside them, flat even cool light, the air completely clear, nothing loose or floating

*On the top sheet* (`paper.yaml`): the decay worked three times — three curves a hair apart, three measured points ringed, a hard underline pressed twice. No letters, no numerals.

**Shot 4.4** — model, 10 s, anchor A2
> Macro view of a small cylindrical pressure transducer threaded into an aluminium manifold, a braided line leaving it, one tiny round status lamp on its body lit cold pale blue, flat cool light, background unresolvable. *Motion:* the status lamp blinks steadily, once a second.

**Narration:**
> *[over 4.1]* Day three. Module C reads forty-two point three kilopascals.
>
> *[over 4.2, with the card]* Lower pressure means less flow, so I corrected for it. What is left is the hole. One point one millimetres.
>
> *[over 4.3]* I ran it three times. Then I fitted the spare transducer from B and ran it again.
>
> *[over 4.4]* One point one. Holes in a hull do not get smaller. They get larger, or they stay.

---

## SCENE 5 — DAY FIVE (2:20–3:04)

**Card (shot 5.1 — answers paragraph 1):** a labelled bar graphic, one bar per
measurement, the label and the figure inside each bar, bars drawn to scale
(1.4 mm = full width). Every bar says what it measures.
```
EQUIV HOLE, MODULE C
[DAY 1           1.4 mm]
[DAY 3      1.1 mm]
[DAY 5  0.6 mm]
```
Bars draw as their line types on. About 70 characters — 7.0 s with the hold, on
a 10 s plate.

**Card (shot 5.3 — answers paragraph 4):**
```
O2, MODULE C
DAY 1          20.9 %
DAY 5          19.8 %
```
63 characters — 6.2 s on a 9 s plate.

**Shot 5.1** — static, 10 s, anchor A3
> A round porthole head-on in a bone-coloured panelled wall, the glass seen at an angle so it shows only a dim cold reflection of the module and no view through it, a plain aluminium ring around it, flat cool light, nothing loose or hanging near it, the lower left of the frame plain panel

**Shot 5.2** — model, 10 s, anchor A3
> A round porthole head-on in a bone-coloured panelled wall, through it the Earth's surface far below with bands of white cloud over blue ocean, a plain aluminium ring around the glass, flat cool light in the module. *Motion:* the Earth slides slowly and steadily past the window, clouds travelling left to right.

**Shot 5.3** — static, 9 s, anchor A1
> The second module seen wide from the hatch end, aluminium equipment racks with every latch closed and every handle in the same position, the metal around them dark, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 5.4** — local (slow push), 5 s, from the approved still of 2.1
> The same round pressure hatch as in 2.1, fully closed and seated, the handwheel at rest, flat cool light, nothing loose or hanging near it

**Shot 5.5** — local (slow push), 10 s, from the approved still of 4.1
> The same round pressure gauge as in 4.1, the needle still. (Changed at stage 6: the Kling roll would not stop the needle and repeated 4.1's sweep; on day five the reading has all but stopped, so the needle holds and the camera moves.)

**Narration:**
> *[over 5.1, with the card]* Day five. Module C, twenty-seven point nine kilopascals. The hole is point six millimetres.
>
> *[over 5.2]* Ground calls it good news. Debris, they think, caught in the hole from outside and plugged it.
>
> *[over 5.2]* The flow runs outward. Anything in the hole is pushed out, not in.
>
> *[over 5.3, with the card]* Oxygen fraction in C, nineteen point eight percent. On day one it was twenty point nine.
>
> *[over 5.4]* A leak takes air as it finds it.

---

## SCENE 6 — DAY SIX (3:04–3:34)

**Card (shot 6.1 — answers paragraph 1):**
```
DAY 6 / 21:00 / MODULE C
PRESSURE      27.7 kPa
UNCHANGED         31 H
LEAK RATE   BELOW RES.
```
88 characters — 4.9 s typing, 1.05 s of pauses, 2 s hold: 8.0 s on a 10 s plate.

**Shot 6.1** — static, 10 s, anchor A1
> The first module seen wide at chest height down its full length, the round hatch at the far end closed, bone-coloured panelling, every strap flat and buckled, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Shot 6.2** — local (slow push), 10 s, anchor A5 (exterior)
> Exterior of one cylindrical station module seen from slightly above, its ivory thermal blanket and seam lines lit hard from one side and its far half in deep shadow, the Earth's limb a thin blue curve below, black sky, nothing attached to the hull moving or loose

**Shot 6.3** — model, 10 s, from the approved still of 3.4
> The same module and the same floating plain grey pencil as in 3.4. *Motion:* the pencil turns slowly end over end and drifts gently across the frame to the right.

**Narration:**
> *[over 6.1, with the card]* Day six, twenty-one hundred. Module C, twenty-seven point seven. Unchanged for thirty-one hours.
>
> *[over 6.2]* The leak rate is below what the transducer can resolve. Zero, as far as anything here can measure.
>
> *[over 6.2]* I reported it at twenty-one thirty. Ground is pleased. The inspection stays on day forty.

---

## SCENE 7 — RESOLVED (3:34–4:00)

No card. The voice ends on 7.2; 7.3 is silent. (Stage 6: 7.1 kept only its clean first 4 s, so paragraph 2 now runs over the first seconds of 7.2 while the hatch is still shut, and "Hatch three open" lands as the door starts to move.)

**Shot 7.1** — model, 5 s (first 4 s of the take, slowed 1.25x), anchor A2
> Macro view of a small equalisation valve set into the rim of a hatch frame, a flat aluminium lever on a round boss, the bone-coloured panelling around it scuffed grey, flat cool light, background unresolvable. *Motion:* the lever rotates a quarter turn from horizontal to vertical and stops.

**Shot 7.2** — model, 10 s, from the approved still of 2.1
> The same round pressure hatch as in 2.1, closed. *Motion:* the door swings slowly open on its hinge as one rigid piece, into the dim aluminium module beyond.

**Shot 7.3** — local (slow push), 11 s, anchor A1
> Looking through an open round hatch into a dim cylindrical module, bone-coloured panelling and aluminium racks beyond, the far end in shadow, flat cool light falling off with depth, the air completely clear, nothing loose, floating or hanging, every rack latch closed and every handle in the same position, the metal around them dark

**Narration:**
> *[over 7.1]* Day seven. Oh-five-forty. Equalisation valve open. The station settled at eighty-five point five.
>
> *[over 7.2]* Makeup brought it back to one-oh-one point three. Twenty-six kilograms from the reserve.
>
> *[over 7.2]* Hatch three open at oh-six-hundred. Problem resolved. Resuming normal schedule.

---

## SCENE 8 — CODA (4:00–4:30)

**Declared coda** (`coda: [8]`). Cards only, no voice. It carries what the
station's own record shows after the last entry, and the channel closer. The
two `model` shots between the plates are the empty station still running.

**Shot 8.1** — static, 7 s, anchor A1
> The first module seen wide at chest height, empty, every strap flat and buckled, bone-coloured panelling, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Card on 8.1:**
```
PROSVET-4
NO ENTRIES AFTER DAY 7
```
31 characters — 4.1 s on a 7 s plate.

**Shot 8.2** — model, 5 s, from the approved still of 3.4
> The same module and the same floating plain grey pencil as in 3.4. *Motion:* the pencil turns slowly end over end.

**Shot 8.3** — static, 7 s, anchor A4
> Directly overhead view of the small aluminium work surface, empty, the steel clip bar closed on nothing, a pencil clip with nothing in it, flat even cool light, the air completely clear, nothing loose or floating, the lower left of the frame plain aluminium

**Card on 8.3:**
```
INSPECTION, DAY 40
NOT PERFORMED
```
31 characters — 4.1 s on a 7 s plate.

**Shot 8.4** — model, 5 s, from the approved still of 2.4
> The same fan behind the same grille as in 2.4. *Motion:* the fan turns steadily.

**Shot 8.5** — static, 6 s, anchor A1
> A cylindrical module seen wide at chest height, bone-coloured panelling, every strap flat, flat cool light, the air completely clear, nothing loose, floating or hanging, the lower left of the frame a plain empty panel

**Card on 8.5 — channel closer:**
```
FILE CLASS NINE
FC9-009 // THE EQUIVALENT HOLE
```
45 characters — 4.9 s on a 6 s plate. The fiction line is in the description.

---

## Pacing (assembly)

Defaults: 1.2 s between paragraphs, 2.0 s across a scene cut. Speed pinned.

Non-default gaps, every one on a paragraph boundary:

- **2.0 s before "I logged it as contained…"** (Scene 3 ¶4). The record's last
  comfortable moment.
- **2.5 s before "One point one. Holes in a hull do not get smaller."** (Scene 4
  ¶4). The figure repeated after a silence is the first sign he has stopped
  believing his instrument.
- **2.5 s before "A leak takes air as it finds it."** (Scene 5 ¶5). The one line
  that says why the oxygen figure is wrong without saying anything else.
- **3.0 s before "Hatch three open at oh-six-hundred."** (Scene 7 ¶3). The rule
  from scene 3 is broken in this line. It arrives alone.

---

## Voice direction

- First person, present and past tense as a log uses them. He is filling in a
  form.
- Never describe what is on screen. Never explain the implication — not of the
  shrinking hole, not of the oxygen, not of opening the hatch.
- "Problem resolved" is read exactly like "shift complete". It is the flattest
  line in the record and must stay so.
- No rising inflection on any figure. "Point six millimetres" is a measurement,
  not a reveal.

---

## Sound design

Under the record: the channel floor and one cue, ducked 7 dB under the voice.
Nothing else runs under it.

**Music prompt** (ElevenLabs music, full runtime, 270 s):

> Slow ambient cue for a sealed orbital station. Sustained mid-register strings and soft glassy pads, roughly 200 Hz to 3 kHz, cold and even. No melody anyone could hum, no beat, no drums, no vocals, no swell, no resolution. Quiet enough to sit under a calm speaking voice throughout. One long shape: a faint pressure that thins very slowly towards the end and never resolves.

**Spot effects** — 7, each in a pause, each a natural event with a body:

1. `1.2 at 7.0 s` — a heavy aluminium valve wheel seating home, one dull clunk, recorded close, dry, short.
2. `2.1 at 7.5 s` — a heavy hatch door meeting its seal, one deep soft thud and a latch dropping, close, dry.
3. `3.3 at 5.0 s` — a single low creak of an aluminium module wall under load, close, dry, short.
4. `5.4 at 1.5 s` — the same low creak, deeper, once.
5. `6.3 at 5.0 s` — one soft muffled knock of a hull panel settling as it cools, close, with body, no ring.
6. `7.1 at 7.5 s` — a low muffled rush of air through a small valve settling to nothing, soft, no whistle, about 2 s.
7. `7.2 at 1.0 s` — a hatch latch releasing, one deep clunk, then the seal parting with a low soft thump.

No spot effects in verticals or the teaser.

---

## Verticals — three cuts

Line list plus shot list. Lines are paragraphs the record contains, trimmed
only from the head. Every figure is spoken. All shots named are `model`.

From record 09 (CLAUDE.md, verticals): each cut **opens on its strangest
figure**, its lines run **back to back** — the second within 0.3 s of the
first, every later gap at most 0.6 s — and it runs **15–25 s** of picture
before the closing card. Durations below are estimates at 162 wpm; the real
word timings decide `at:` and `validate.py` checks the gaps.

### FC9-009.a // "Holes In A Hull Do Not Shrink" (~17 s + card)

- **Lines:** S1 ¶3 → S4 ¶4 → S5 ¶1.
  "The equivalent hole is one point four millimetres across." /
  "One point one. Holes in a hull do not get smaller. They get larger, or they
  stay." / "Day five. Module C, twenty-seven point nine kilopascals. The hole is
  point six millimetres."
- **Shots:** 4.1, 2.3, 5.5, 2.4 — the needle first, so something moves in
  frame one.
- **In-point:** on "The equivalent hole" — voice at 0.2 s.
- **Framing:** all centred subjects; window centre throughout.
- **Out-point:** last word "millimetres", end of a paragraph.

### FC9-009.b // "A Leak Cannot Do That" (~16 s + card)

- **Lines:** S5 ¶4 → S5 ¶5 → S5 ¶3.
  "Oxygen fraction in C, nineteen point eight percent. On day one it was twenty
  point nine." / "A leak takes air as it finds it." / "The flow runs outward.
  Anything in the hole is pushed out, not in."
- **Shots:** 5.2, 3.3, 4.4, 2.1.
- **In-point:** on "Oxygen fraction" — voice at 0.2 s.
- **Framing:** 5.2 centred on the porthole; 2.1 window on the left third,
  where the door's hinge edge travels.
- **Out-point:** last word "in", end of a paragraph.

### FC9-009.c // "Problem Resolved" (~17 s + card)

- **Lines:** S6 ¶1 → S6 ¶2 → S7 ¶3 trimmed to its first two sentences.
  "Day six, twenty-one hundred. Module C, twenty-seven point seven. Unchanged
  for thirty-one hours." / "The leak rate is below what the transducer can
  resolve. Zero, as far as anything here can measure." / "Hatch three open at
  oh-six-hundred. Problem resolved."
- **Shots:** 6.3, 7.1, 7.2.
- **In-point:** on "Day six" — voice at 0.2 s.
- **Framing:** 7.2 window on the left third, on the opening edge of the door.
- **Out-point:** last word "resolved". Real silence follows it in the take
  (the sentence ends); confirm `VERT_TAIL` against the alignment.

---

## Teaser — five lines, in order

Lines back to back (same gap limits as a cut); the teaser keeps its 30 s.

1. "Day one. Oh-three-forty. The makeup valve has opened eleven times since midnight." (S1 ¶1)
2. "The equivalent hole is one point four millimetres across." (S1 ¶3)
3. "One point one. Holes in a hull do not get smaller." (S4 ¶4, first two sentences)
4. "Oxygen fraction in C, nineteen point eight percent. On day one it was twenty point nine." (S5 ¶4)
5. "Day six, twenty-one hundred. Module C, twenty-seven point seven. Unchanged for thirty-one hours." (S6 ¶1)

About 23 s of voice. Ends on `SOON`. Related video is set the day the record
goes public (see `publish.md`).

---

## Open production decisions

- **The video tier is pending the bake-off** (`research/model-bakeoff/`). The
  shots above are written to what Kling 2.5 already holds — rigid rotations,
  lamps blinking, a door on a hinge, a needle, clouds sliding — so they work on
  the workhorse either way. If a new tier wins, the shots most worth moving to
  it are 3.1 and 5.2 (the Earth) and 2.1 / 7.2 (the hatch).
- **The bar graphic on 5.1** is new to `build_cards.py` in this form (three
  labelled horizontal bars to scale). The stacked-bar renderer is the closest
  existing code.
- **Exteriors** go through text-to-image with the exterior spine (A5); no
  interior anchor is ever passed to 3.1 or 6.2.

---

## Appendix — what is real and what is invented

### Real, verifiable

**Choked flow into vacuum.** Air escaping through a small hole into vacuum is
choked: the flow is sonic at the hole and depends only on the upstream
pressure, not on the vacuum outside. Mass flow:
ṁ = C_d · A · p · √(γ / (R·T)) · (2/(γ+1))^((γ+1)/(2(γ−1))),
with γ = 1.4, R = 287 J·kg⁻¹·K⁻¹, T = 293 K, discharge coefficient C_d = 0.62
(sharp-edged orifice). The constant factor is 0.002361 s/m, so
ṁ = 0.62 × 0.002361 × A × p.

**An "equivalent hole" is how real station leaks are sized.** A measured
pressure decay is converted to the diameter of a single sharp-edged hole that
would produce it, without anyone having seen the hole.

**Day one, whole station (140 m³, 101.3 kPa).** Air mass = pV/(RT) = 168.7 kg.
At d = 1.4 mm, A = 1.539 × 10⁻⁶ m², ṁ = 2.283 × 10⁻⁴ kg/s = **19.7 kg/day**.
Time constant τ = m/ṁ = 8.55 days, so four hours of decay costs
101.3 × (1 − e^(−4/205.2)) = **1.96 kPa**. Reserve 300 kg / 19.7 kg/day =
**15.2 days**.

**Leak location by isolation.** Closing hatches and timing the decay in each
section is the standard method; it is how a real station's crew located a
leak in 2020. Module C alone (30 m³) at the same hole falls at
101.3 × 3600 / τ_C = **2.31 kPa/h** (τ_C = 1.83 days); A and B, sealed from
it, hold.

**Ultrasonic leak detection.** Gas escaping through a small orifice is loud
around 40 kHz, far above hearing; handheld detectors listen there and
heterodyne it down.

**Correcting for falling pressure.** In a sealed volume dp/dt = −p/τ with
τ = V/(R·T·C_d·A·0.002361): the rate falls with pressure, but τ — and the
pressure half-life τ·ln 2 — depends only on the hole. That is what the operator
"corrects for". In module C: d = 1.4 mm → half-life 30.5 h; 1.1 mm → **49 h**;
0.6 mm → 166 h.

**Module C pressure, integrated from isolation at day 1 09:00** with the hole
taken as 1.4 mm, 1.1 mm at day 3, 0.6 mm at day 5 (linear between): **42.3 kPa**
on day 3 at 09:00, **27.9 kPa** on day 5 at 09:00. Taking the hole to zero at
day 5 ~14:00, the pressure stops at **27.7 kPa**, and by day 6 at 21:00 it has
been flat for **31 hours**.

**Choked flow does not sort gases.** The orifice passes the mixture as it is,
so the oxygen fraction in a leaking sealed volume stays where it was: 20.9%.
A fall to 19.8% is not something a leak can produce.

**Equalisation.** Opening C (30 m³ at 27.7 kPa) to A + B (110 m³ at
101.3 kPa): (101.3 × 110 + 27.7 × 30) / 140 = **85.5 kPa**. Restoring 140 m³ to
101.3 kPa takes (101.3 − 85.5) / 101.3 × 168.7 = **26.2 kg** of makeup — the
same mass module C lost through the hole. Hatches between sections at
different pressures cannot be opened until an equalisation valve has brought
them level, which is why the valve comes first.

### Invented

Station PROSVET-4, its three modules and their volumes (A + B 110 m³, C 30 m³),
the 300 kg gas reserve, panel C-14 and its 40 mm of insulation, the external
camera's mounting, the day-40 inspection, every time of day. The oxygen
readings in module C.

**The one impossible thing:** a hole in a hull that closes — 1.4 mm, 1.1 mm,
0.6 mm, zero — while the module it drains loses oxygen faster than air.
