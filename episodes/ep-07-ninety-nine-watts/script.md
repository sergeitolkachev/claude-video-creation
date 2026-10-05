# FC9-007 // "THE NINETY-NINE WATTS"

**Slug:** FC9-007 // THE NINETY-NINE WATTS
**Runtime:** 4:27 (267 s) — 34 shots, durations sum to 267 s exactly
**Per-scene seconds:** {1: 30, 2: 35, 3: 40, 4: 40, 5: 40, 6: 40, 7: 10, 8: 32} = 267
**Format:** 16:9 horizontal, three vertical cuts assembled out of it, one teaser
**Voice:** character (operator) — dry, procedural, first person. A man reading his own arithmetic back to himself. No performance. The fear is in the numbers, never in the delivery.
**Word count:** 376. At 162 wpm that is 139 s of speech against 267 s of runtime — 47.8% silence overall, 40.7% across Scenes 1–7 (235 s) with the declared coda excluded.
**Motion split:** 10 static / 10 local / 14 model
**Interiors only.** This record has no exterior shots. The radiator exists entirely as instrument readings, which is both the cheapest build on the channel and the correct one — the operator never sees it either.

### Per-scene silence

| Scene | Seconds | Words | Speech | Silence |
|---|---|---|---|---|
| 1 | 30 | 45 | 16.7 s | 44.3% |
| 2 | 35 | 52 | 19.3 s | 44.9% |
| 3 | 40 | 65 | 24.1 s | 39.8% |
| 4 | 40 | 71 | 26.3 s | 34.3% |
| 5 | 40 | 56 | 20.7 s | 48.1% |
| 6 | 40 | 70 | 25.9 s | 35.2% |
| 7 | 10 | 17 | 6.3 s | 37.0% |
| 8 (coda) | 32 | 0 | 0 | 100% — **declared coda**, exempt |

Scene 4 is the tight one at 34%. Record 02 came in slower than planned and
three scenes fell under the floor; if scene 4's takes land slow, the fix is
picture, not a cut line.

---

## Corrections on intake

The script was submitted by the scenario agent on 2026-10-05, without a
`publish.md`. Its arithmetic was checked end to end and the core holds:
4,483 W and 4,383 W from Stefan–Boltzmann, the design figure equal to bus
plus operator (4,384 W), 99 / 61.8 W/K = 1.60 K, a 3.2-day time constant that
reaches 94% in nine days, 2,150 kcal = 104.1 W. No two ffmpeg shots touch
anywhere. Everything below is the submitted draft with the following changes
and nothing else.

1. **Card 2 of the coda is gone; its plate carries the continuation hook.**
   `99 W IS WHAT IT COSTS TO HOLD 3.1 C BELOW AMBIENT` draws the conclusion
   for the viewer, and the channel does not explain its twist. The first coda
   card — a cooling device releases more heat than it removes — is the key;
   turning it is the viewer's job. Its 8 s plate now carries
   `KROMKA-6 / RECORD ENDS AT LOG 104`, the hook the agent could not fit. It
   is a line from the archive's own catalogue, not a promise of a sequel —
   the same distinction that keeps `SOON` off a vertical.

2. **The coda holds no voice.** The exemption covers a closing card block and
   a held silent shot, not a line (record 06, correction 8). The draft's 7.1
   is now scene 7 on its own — log ninety-eight, 10 s, 37% silent, and the
   pump returning on its cut exactly as the sound design asks. The coda is
   scene 8: the draft's 7.2–7.6 renumbered 8.1–8.5, 32 s of cards, no voice.

3. **The closer did not fit its plate.** The draft called it "tight but
   inside": `card_end` measures the three-line block at 6.27 s on a 6 s plate.
   Two lines, as record 06 shipped it (4.97 s); the fiction line goes in the
   description.

4. **Six days, twice.** Log 88 said the cabin had held for six days and log
   90 — two logs later, one a day by the record's own "yesterday" — said six
   again, with a card reading `STABLE 6 DAYS`. Log 88 now says **four**.
   One word.

5. **The calorimetric check in the appendix was wrong.** 0.22 × 3,400 × 5.99
   is 4,480, not 4,483; at the "six degrees" the voice says it is 4,488. The
   appendix now gives the honest figure and the agreement it buys (0.1%),
   which is what "agrees" in the narration claims. The narration is
   unchanged.

6. **"The same measurement three ways" was too strong.** The plate has to
   rise 1.60 K to reject 99 W more; the cabin sits upstream of it on the
   thermal path and rises at least that much. The narration never asserts the
   two are equal, so only the appendix sentence changed.

7. **No figures in any frame.** 5.3 asked for "the trailing digit of a figure
   stepping" — a request for lettering. It is now a single phosphor bar that
   steps once and holds. 3.2 was a register counter, which is a drum of
   numerals; it is now the turning disc of an induction meter, which is the
   bus being measured and has one dark stripe on its rim and nothing to read.
   The dials (1.2, 8.2), the column (4.1), the setpoint wheel (2.1) and the
   imager (6.4) forbade numerals in subjects that imply them; each is now
   filled positively — plain engraved ticks, a ribbed wheel, a thermal field
   running to every edge.

8. **"No card on this shot" was inside three prompts** (3.4, 5.3, 6.4). It is
   an instruction to assembly, and the model would read "card" as an object.
   Removed; the rule lives in `cards.yaml`, where those shots carry none.

9. **This station has no weight, and two shots forgot.** The bunk is strapped
   flat, the cup sits in a retaining ring, the seat webbing is pulled tight —
   then 2.5 asked a bead of condensation to run "down" a pipe and 5.1 a sheet
   of paper to lift and settle. Both are also soft shapes the model redraws
   every frame (record 05's strap). 2.5 is now dust carried past a ventilation
   grille; 5.1 is a pencil floating free and turning end over end — a rigid
   rotation, and the one shot that tells the viewer where this is. Objects in
   the plates are seated, clipped or held in foam rather than "resting".

10. **7.1 and 8.2 (was 7.3) reference approved stills.** The hatch is
    generated from the approved 6.3 and the dial from the approved 1.2, so
    each is the same object down to the scratch. "With the work lamp now
    off" is gone from the hatch: 6.3 has no lamp, and naming one puts it in
    frame.

11. **The spine named an object.** "Coming from wide recessed panels" is a
    light fixture, and the model would put it into every macro. The light is
    described without a source.

12. **Card wording.** `LENGTH 0.42 m` becomes `ACROSS 0.42 m` (the voice says
    "across"); `m2` becomes `m²`.

13. **Verticals and teaser.** .a and .c both ended on "I have checked it four
    times"; .c now ends on "…is not drawing current." .b opened "Except the
    forward hold bulkhead" with the sentence it excepts left out; S6 ¶2 is
    back in. Teaser line 3 was the second sentence of a paragraph, which
    `vertical.py` cannot cut to — trims run from the head only. It is now
    S3 ¶3, whole.

14. **Planned test, not a change.** One `model` shot will be rolled on Kling
    O3 Standard as well as the workhorse, same approved still, to see whether
    it holds a frame better. See `cost.md`.

## Changes after intake (stages 4–6)

15. **Motion, re-planned after scenes 1–4 were animated.** Two shots asking
    Kling to move only light (3.4's glow, 4.1's shadow) came back as stills,
    and the draft leaned on dust wherever nothing else moved. Rule from here
    (CLAUDE.md, Motion Policy): a model shot is for an object that moves.
    5.3 is now a cooling fan (new still); 6.2 is the work lamp turning on its
    swivel clamp (new still); 5.5, 6.4, 7.1 and 8.2 are ffmpeg pushes; 8.4 is
    an ffmpeg pull back down the passage. Split is 10 static / 10 local /
    14 model.
16. **Repairs on rolled takes, no rerolls.** 1.2, 2.3 and 4.3 keep the clean
    head of their take slowed 2x by interpolation; 4.5 the same at 1.54x. 3.4
    and 4.1 have a push laid over a near-still take. Kling O3 Standard was
    tried on 3.2 and lost (720p, camera drift, no rotation).

---

## Disclaimer

> Work of fiction. All records, objects and events are invented. Any resemblance to real missions is coincidental. The thermal physics in this record is real and the arithmetic checks; the station and everything in it do not exist.

---

## Synopsis

The sole operator of a station notices the cabin has settled one point six degrees above its setpoint and stopped there. A fault drifts; this balanced. He rules out the bus — electrical load is unchanged to within a watt over a month. He measures what the radiator is actually rejecting, twice, by two independent methods that do not depend on each other. Out: 4,483 watts. In: 4,280 on the bus plus 104 from his own body, which he can state because he logs his food. The difference is ninety-nine watts that draw no current. He sweeps the station with a thermal camera looking for a warm surface and finds none. The only deviation anywhere is a cold patch on the forward hold bulkhead — and it is not where it was yesterday.

---

## Style spine

> Painted steel and anodised aluminium, worn through to bare metal along every edge that gets touched. Matte, faintly oxidised, nothing polished and nothing new. One palette throughout: cold blue-grey. The light is flat, blue-white, low and diffuse, with no visible source anywhere. Contrast is low, shadows are soft and shallow, blacks are lifted and never crushed. No lettering, no markings, no numerals, no people.

**Spine notes for the shot writer.** The spine names no objects and contains no camera words — distance, lens and framing belong to the anchors and to each shot line. There is no warm light anywhere in this record; the one practical lamp the record allows is named in shots 6.1 and 6.2 and nowhere else, and it is cold white. Control surfaces imply indicator lamps, so `static` and `local` prompts never say "no lamp" — they fill the row positively instead ("every switch in the row in the same position, the metal around them dark").

## Anchors

- **A1 — wide compartment.** Camera at chest height, wide field, the full depth of the space in frame, everything in focus.
- **A2 — deep perspective.** Camera centred in a long narrow passage, vanishing point inside the frame, strong recession.
- **A3 — macro instrument.** Long lens, the subject filling the frame edge to edge, background two stops down and unresolvable.
- **A4 — top-down surface.** Camera directly overhead, flat frontal plane, even coverage.
- **A5 — object head-on.** Normal lens, flat frontal, subject centred, a plain surface one metre behind it.

**Repeat-subject rule:** shots 6.3 and 7.1 are the same hatch seen twice, and 1.2 and 8.2 are the same dial. Generate 7.1 from the approved still of 6.3 and 8.2 from the approved still of 1.2, not from the anchor.

## On-screen text conventions

All cards: **Menlo, phosphor green RGB 150 255 190, 40 px on 1080p**, halo and glow, no box, no scrim. Composed for the **lower left** of the frame; every plate below is framed with that corner empty. Characters type on at 18 ch/s, 0.35 s between lines, card holds at least 2 s after its last character. Nothing fades or slides. No card sits over a screen that is green in-fiction — shots 3.4, 5.3 and 6.4 carry glowing readouts and carry no card.

---

## SCENE 1 — COLD OPEN (0:00–0:30)

Image first. No logo, no ident.

**Card (shot 1.1 — answers paragraph 2):**
```
LOG 088 / KROMKA-6
CABIN 22.8 C / NOMINAL 21.2 C
```
47 characters — 2.6 s typing, 0.35 s between lines, 2 s hold. The slug types into the same corner first and is gone by 4.5 s; the card follows it.

**Shot 1.1** — static, 10 s, anchor A1
> A cramped equipment compartment of painted steel seen wide at chest height, a bank of identical grey toggle switches along the right wall with every switch in the same position and the metal around them dark, flat blue-white light, the air in front of the subject completely clear, nothing in the frame loose or hanging, the lower left of the frame an empty bare floor panel

**Shot 1.2** — model, 10 s, anchor A3
> Extreme close view of a round instrument set into a steel panel, a ring of plain engraved tick marks under a scratched glass cover, one fine black needle, flat cold light raking across the bezel from the left, background unresolvable. *Motion:* the needle creeps a fraction of a tick and settles.

**Shot 1.3** — model, 10 s, anchor A2
> A long narrow passage of painted steel seen straight down its length, vanishing point centred, fine dust drifting slowly through the flat blue-white light halfway along, cold low contrast, no people

**Narration:**
> Log eighty-eight. Shift complete. Nothing to report.
>
> Cabin temperature, twenty-two point eight. Nominal is twenty-one point two.
>
> The log flagged it. I would not have noticed one point six degrees.
>
> It has been twenty-two point eight for four days. It was climbing before that.

---

## SCENE 2 — THE DRIFT STOPPED (0:30–1:05)

**Card (shot 2.2 — answers paragraph 2, which lands about 10.7 s into the scene; the plate is on screen 10–15 s):**
```
LOG 090 / +1.6 C STABLE 6 DAYS
```
30 characters — 1.7 s typing, 2 s hold, inside the 5 s plate.

**Shot 2.1** — model, 10 s, anchor A5
> A small grey controller housing head-on against a plain steel surface a metre behind it, a knurled setpoint wheel with a plain ribbed edge set into its blank worn faceplate, normal lens, flat frontal composition, cold blue-white light. *Motion:* the wheel turns a few degrees and stops.

**Shot 2.2** — static, 5 s, anchor A4
> Directly overhead view of a plain steel desk surface with a closed logbook held flat under a steel clip bar and squared to the edge of the frame, matte cover worn through at the corners, flat even blue-white light, the air above the surface completely clear, nothing loose or hanging anywhere in frame, the lower left of the frame empty bare steel

**Shot 2.3** — model, 10 s, anchor A3
> Macro view of a strip of pale paper with a plain ruled grid emerging from a narrow slot in a steel recorder housing, one continuous ink trace along it, flat cold light, background unresolvable. *Motion:* the paper advances steadily out of the slot and the trace travels with it.

**Shot 2.4** — local (drift right), 5 s, anchor A1
> Wide view of a narrow sleeping alcove, bunk strapped flat to the bulkhead and empty, restraint webbing pulled tight and flush to the mattress, flat blue-white light, the air completely clear, nothing hanging or suspended anywhere in frame

**Shot 2.5** — model, 5 s, anchor A3
> Macro view of a ventilation grille of thin steel slats set into a bulkhead beside a coolant line union, fine dust drifting past the slats on the airflow, flat cold light, background unresolvable

**Narration:**
> Log ninety. I checked the setpoint. The loop controller is asking for twenty-one point two and the loop is delivering twenty-two point eight.
>
> A fault drifts. This is not drifting. It rose for nine days and then it stopped, and it has held for six.
>
> Something that stops is something that balanced.

---

## SCENE 3 — THE BUS (1:05–1:45)

**Card (shot 3.1 — answers paragraph 1, spoken 0–9.6 s into the scene):**
```
LOG 092 / BUS LOAD
NOW      4280 W
D-14     4280 W
D-30     4281 W
```
63 characters — 3.5 s typing, 1.05 s of line pauses, 2 s hold. Fits the 10 s plate.

**Shot 3.1** — static, 10 s, anchor A5
> A flat steel distribution panel head-on, a row of identical black breaker handles all in the same position, the steel around them dark and unlit, plain bulkhead one metre behind, flat blue-white light, the air in front of the panel completely clear, nothing loose or hanging, the lower left of the frame empty painted steel

**Shot 3.2** — model, 10 s, anchor A3
> Macro view through a scratched glass window of a thin aluminium disc seen edge-on on its spindle inside a steel meter housing, one dark painted stripe on its rim, flat cold light across the glass, background unresolvable. *Motion:* the disc turns slowly and the stripe passes once.

**Shot 3.3** — local (slow push), 5 s, anchor A2
> A service passage lined with insulated pipe runs clipped tight to the wall, vanishing point centred, flat blue-white light from the near end only, the air completely clear, every line clipped flush with nothing hanging or slack anywhere in frame

**Shot 3.4** — model, 10 s, anchor A3
> Macro view of a small round phosphor screen in a steel bezel, one flat horizontal trace across its middle with a coarse phosphor glow, the rest of the screen dark, dark surroundings. *Motion:* the trace jitters by a hair and holds.

**Shot 3.5** — local (drift), 5 s, anchor A4
> Overhead view of a steel workbench, a spanner and a flow fitting seated in fitted cut-outs of a grey foam tray, squared to the surface, flat even light, the air above completely clear, nothing loose or hanging in frame

**Narration:**
> Log ninety-two. Bus load, four thousand two hundred eighty watts. Two weeks ago, four thousand two hundred eighty. A month ago, four thousand two hundred eighty-one.
>
> Everything electrical on this station turns into heat eventually. If the load has not changed, the electrical heat has not changed.
>
> Nothing has been added. Nothing has been switched on. Whatever is making the difference is not drawing current.

---

## SCENE 4 — THE RADIATOR (1:45–2:25)

**Card (shot 4.2 — answers paragraph 2, which runs about 12.9–21 s into the scene; the plate is on screen 10–20 s):**
```
RADIATOR A   14.0 m²
PLATE       285.5 K
DESIGN      283.9 K
REJECTING    4483 W
```
80 characters — 4.4 s typing, 1.05 s of line pauses, 2 s hold. Fits the 10 s plate.

**Shot 4.1** — model, 10 s, anchor A3
> Macro view of a glass capillary column with a thin silver thread set into a steel panel beside a strip of plain evenly spaced engraved lines, flat cold light, background unresolvable. *Motion:* the thread stands still while a slow shadow edge travels up the column from below.

**Shot 4.2** — static, 10 s, anchor A5
> A plain instrument housing head-on against a painted steel bulkhead a metre behind, blank matte faceplate with two recessed ports and a worn grey finish, flat blue-white light, the air in front of it completely clear, nothing loose or hanging anywhere in frame, the lower left of the frame empty bulkhead

**Shot 4.3** — model, 10 s, anchor A3
> Macro view of a sight glass in a coolant line with clear fluid moving steadily through it, flat cold light, background unresolvable. *Motion:* a single bubble crosses the glass left to right.

**Shot 4.4** — local (slow push), 5 s, anchor A1
> Wide view of a pump bay, two identical steel pump bodies bolted to the deck, every pipe clipped flush to the frame, flat blue-white light, the air completely clear, nothing hanging or suspended anywhere in frame

**Shot 4.5** — model, 5 s, anchor A3
> Macro view of a small vaned flow-meter rotor behind a scratched round window in a coolant line, flat cold light, background unresolvable. *Motion:* the rotor turns at a steady slow rate.

**Narration:**
> Log ninety-four. If the station is warmer, the radiator is warmer. I pulled the plate temperature: two hundred eighty-five point five kelvin. Design is two hundred eighty-three point nine.
>
> Fourteen square meters at emissivity zero point eight five. That panel is throwing four thousand four hundred eighty-three watts into the dark.
>
> The flow meter agrees without trusting the coating. Zero point two two kilograms a second, six degrees across the panel.

---

## SCENE 5 — THE NUMBER (2:25–3:05)

**Card A (shot 5.2 — answers paragraph 2; "one hundred four watts" lands about 13 s into the scene, the plate is on screen 5–15 s):**
```
OUT        4483 W
BUS        4280 W
OPERATOR    104 W
```

**Card B (shot 5.4 — answers paragraph 3; the plate is on screen 25–35 s):**
```
UNACCOUNTED  99 W
```
One line, 17 characters. It types in under a second and then holds for nine. That hold is the scene.

**Shot 5.1** — model, 5 s, anchor A3
> Macro view of a plain wooden pencil floating free in the air in front of a soft dark painted steel background, flat raking light from the left, background unresolvable. *Motion:* the pencil turns slowly end over end.

**Shot 5.2** — static, 10 s, anchor A4
> Directly overhead view of a plain steel desk surface with a sheet of paper bearing only printed ruled lines held flat under a steel clip bar and squared to the frame, a slide rule seated in a slot beside it, flat even blue-white light, the air above the surface completely clear, nothing loose or hanging in frame, the lower left of the frame empty bare steel

**Shot 5.3** — model, 10 s, anchor A3
> Macro view of a small round phosphor screen in a steel bezel, a single short bright horizontal bar glowing near its middle with a coarse phosphor glow, the rest of the screen dark, dark surroundings. *Motion:* the bar lengthens by one step and holds.

**Shot 5.4** — static, 10 s, anchor A1
> Wide view at chest height of a narrow galley recess, a single steel cup seated in its retaining ring on a bare shelf, flat blue-white light, nothing else on any surface, the air completely clear, nothing loose or hanging anywhere in frame, the lower left of the frame empty painted steel

**Shot 5.5** — model, 5 s, anchor A2
> A long narrow passage seen straight down its length, vanishing point centred, flat blue-white light, cold low contrast. *Motion:* a slow shadow edge travels along the right wall toward the camera.

**Narration:**
> Log ninety-six. Four thousand four hundred eighty-three out. Four thousand two hundred eighty in, on the bus.
>
> I am the rest of it. Two thousand one hundred fifty kilocalories a day is one hundred four watts. I logged the food, so I can log the watts.
>
> That leaves ninety-nine watts. I have checked it four times.

---

## SCENE 6 — THE SWEEP (3:05–3:45)

**Card (shot 6.3 — answers paragraph 3, which runs about 17.9–26.4 s into the scene; the plate is on screen 15–25 s):**
```
IR SWEEP / FORWARD HOLD
WALL     296.0 K
PATCH    292.9 K
ACROSS     0.42 m
```
75 characters — 4.2 s typing, 1.05 s of line pauses, 2 s hold. Fits the 10 s plate.

**Shot 6.1** — model, 10 s, anchor A2
> A long narrow passage seen straight down its length with a single cold-white work lamp clamped to the right wall halfway along, vanishing point centred, cold blue-grey surfaces, no people. *Motion:* the lamp pulses slowly between two brightnesses.

**Shot 6.2** — model, 5 s, anchor A1
> Wide view at chest height of a steel bulkhead with cold-white light from a work lamp out of frame left raking hard across it, fine dust drifting slowly through the beam, the surface worn through to bare metal along one edge, no people

**Shot 6.3** — static, 10 s, anchor A5
> A heavy steel hatch head-on filling the frame, six identical latches around its rim all in the same position, worn paint across the face, plain bulkhead to each side, flat blue-white light, the air in front of it completely clear, nothing loose or hanging anywhere in frame, the lower left of the frame empty painted steel

**Shot 6.4** — model, 10 s, anchor A3
> Macro view of the screen of a handheld thermal imager in a worn rubber housing, a coarse monochrome grey thermal field running to every edge of the screen with one dark ellipse low in the picture, dark surroundings. *Motion:* the field shimmers slightly frame to frame.

**Shot 6.5** — local (drift), 5 s, anchor A4
> Overhead view of a bare steel deck panel, the thermal imager seated face down in a fitted cut-out of a grey foam tray, flat even blue-white light, the air above completely clear, nothing loose or hanging in frame

**Narration:**
> Log ninety-seven. Ninety-nine watts of heat has to come out of a surface. I took the thermal camera through every compartment.
>
> There is no warm surface anywhere on this station. Everything is uniform to two tenths of a degree.
>
> Except the forward hold bulkhead. There is a patch there, forty-two centimeters across, three point one degrees colder than the wall around it.
>
> It was eleven centimeters to the left yesterday.

---

## SCENE 7 — LOG NINETY-EIGHT (3:45–3:55)

The pump comes back on this cut.

**Shot 7.1** — model, 10 s, from the approved still of 6.3
> The same heavy steel hatch head-on as in shot 6.3, flat blue-white light, no people. *Motion:* a slow shadow edge creeps across the lower third of the face.

**Narration:**
> Log ninety-eight. Shift complete. Cabin temperature, twenty-two point eight.
>
> I am not going into the forward hold.

If the takes run long, the second line may finish over the first coda plate; its card waits for it.

---

## SCENE 8 — CODA (3:55–4:27)

**Declared coda.** Scene 8, cards only, no voice. It carries what the voice withholds — the principle the operator never says — and the record's own catalogue line, then the channel closer. Its silence is the delivery mechanism, not slack.

**Shot 8.1** — static, 8 s, anchor A1
> Wide view at chest height of the operator's station, an empty seat with its restraint webbing pulled tight and flush, bare steel surfaces around it, flat blue-white light, the air completely clear, nothing loose or hanging anywhere in frame, the lower left of the frame empty bare deck

**Shot 8.2** — model, 5 s, from the approved still of 1.2
> The same round instrument as in shot 1.2, flat cold light. *Motion:* the needle stays completely still while a slow shadow edge crosses the glass.

**Shot 8.3** — static, 8 s, anchor A4
> Directly overhead view of a plain steel desk surface, empty, a single flat-headed fastener seated in a threaded hole off centre, flat even blue-white light, the air above completely clear, nothing loose or hanging in frame, the lower left of the frame empty bare steel

**Shot 8.4** — model, 5 s, anchor A2
> A long narrow passage seen straight down its length, vanishing point centred, fine dust drifting slowly through the flat blue-white light at the far end, cold low contrast, no people

**Shot 8.5** — static, 6 s, anchor A4
> Directly overhead view of a bare painted steel deck panel filling the frame, matte, worn through along one seam, flat even blue-white light, the air above completely clear, nothing loose or hanging in frame, the lower left of the frame empty painted steel

**Coda plates.** Each card has its own plate; none shares one. Measured with `card_end`.

**Card on 8.1 (8 s plate):**
```
A COOLING DEVICE RELEASES MORE HEAT
THAN IT REMOVES
```
50 characters — 5.1 s from first character to the end of the hold.

**Card on 8.3 (8 s plate) — the continuation hook:**
```
KROMKA-6
RECORD ENDS AT LOG 104
```

**Card on 8.5 (6 s plate) — channel closer:**
```
FILE CLASS NINE
FC9-007 // THE NINETY-NINE WATTS
```
4.97 s. The fiction line is in the description.

---

## Pacing (assembly)

Defaults: 1.2 s between paragraphs, 2.0 s across a scene cut. The voice speed parameter is pinned at the synthesis default and never touched.

Non-default gaps — every one of them falls on a paragraph boundary:

- **2.5 s before "That leaves ninety-nine watts."** (Scene 5, start of paragraph 3.) The figure is the spine of the record and arrives on its own.
- **2.5 s before "It was eleven centimeters to the left yesterday."** (Scene 6, start of paragraph 4.) The coolant pump is already out of the bed here — see Sound design — so this gap is close to true silence under room tone.
- **2.5 s before "I am not going into the forward hold."** (Scene 7, start of paragraph 2.) This is why that sentence is its own paragraph rather than the tail of the one above it; a gap inside a paragraph cannot be cut.

---

## Voice direction

- First person, present tense, procedural. He is filling in a form.
- Never describe what is already on screen.
- Never explain the implication. The whole thermodynamic point of the record is in the coda card and is never spoken.
- The numbers are read exactly like "shift complete". No rising inflection anywhere, least of all on ninety-nine.
- The flattest line in the episode is "I have checked it four times." Keep it the flattest.

---

## Sound design

Room tone runs under the entire episode; there is never digital silence. It is its own ungated bed, separate from the pump.

One recurring element: **the coolant circulation pump**, a low cycling hum with a beat about every eleven seconds. Establish it in Scene 1 and carry it through Scenes 2–5. **Remove it entirely at the top of Scene 6** — in fiction he stops circulation so the walls settle before the thermal sweep, which is why the sweep is possible at all. **Bring it back on the cut into Scene 7**, at the same level it had in Scene 1. The return is the only comfortable sound in the record and the coda takes it away again: the hum is cut on the last plate, 8.5. The room tone stays.

Video models are generated with audio off. No sound is written into any shot prompt.

---

## Verticals — three cuts

Each is a line list plus a shot list. Lines are paragraphs the record already contains, trimmed only to their first sentences where noted. Nothing is generated for a cut. Order is for the cut, not the record. All shots named are `model`. Every figure in every cut is spoken aloud, never card-only.

### FC9-007.a // "The Ninety-Nine Watts" (~33 s)

- **Lines:** Scene 5 ¶1 → Scene 5 ¶2 → Scene 5 ¶3.
- **Shots:** 5.1, 5.3, 4.1, 5.5, 6.4.
- **In-point:** on "Log ninety-six" — voice inside the first second, no held frame.
- **Framing:** 5.3 and 6.4 are macro and centred, so the 608 px window sits dead centre. 5.5 wants the window on the right third, where the shadow edge travels.
- **Out-point:** last word "times", end of a paragraph.

### FC9-007.b // "The Patch" (~32 s)

- **Lines:** Scene 6 ¶1 → Scene 6 ¶2 → Scene 6 ¶3 → Scene 6 ¶4.
- **Shots:** 6.1, 6.2, 6.4, 3.4.
- **In-point:** on "Log ninety-seven".
- **Framing:** 6.2 wants the window on the left, where the lamp rakes the wall. 6.4 centred.
- **Out-point:** last word "yesterday". Paragraph end — safe cut.

### FC9-007.c // "A Fault Drifts" (~25 s)

- **Lines:** Scene 1 ¶2 → Scene 2 ¶2 trimmed to its first two sentences ("A fault drifts. This is not drifting.") → Scene 2 ¶3 → Scene 3 ¶3.
- **Shots:** 1.2, 2.1, 2.3, 3.2.
- **In-point:** on "Cabin temperature".
- **Framing:** all four are centred subjects; window centre throughout.
- **Out-point:** last word "current". Paragraph end.

Captions are burned in from real word timings, kept out of the bottom 30% and off the right edge. Hard cuts only; no music.

---

## Teaser — five lines, in order

All five already exist in the record. No connective tissue between them, nothing explains anything, and the last one does not resolve.

1. "Cabin temperature, twenty-two point eight. Nominal is twenty-one point two." (Scene 1 ¶2)
2. "A fault drifts. This is not drifting." (Scene 2 ¶2, first two sentences)
3. "Nothing has been added. Nothing has been switched on. Whatever is making the difference is not drawing current." (Scene 3 ¶3)
4. "That leaves ninety-nine watts. I have checked it four times." (Scene 5 ¶3)
5. "It was eleven centimeters to the left yesterday." (Scene 6 ¶4)

Ends on `SOON`.

---

## Appendix — what is real and what is invented

### Real, verifiable

**Radiation is the only heat rejection path in vacuum.** No conduction, no convection. A spacecraft's thermal balance is therefore a radiator problem, which is why vacuum is a thermal insulator and not a cold sink.

**Stefan–Boltzmann:** P = ε σ A T⁴, with σ = 5.670 × 10⁻⁸ W·m⁻²·K⁻⁴.
- At the measured plate temperature: 0.85 × 5.670e-8 × 14.0 × 285.5⁴. 285.5⁴ = 6.6439 × 10⁹, so P = 4,483 W.
- At the design plate temperature: 0.85 × 5.670e-8 × 14.0 × 283.9⁴ = 4,383 W (283.9⁴ = 6.4962 × 10⁹) — which is the design load, 4,280 W of bus and 104 W of operator.
- Difference: 99.6 W. The balance below, done in whole watts, gives 99.

**Calorimetric cross-check, independent of emissivity:** Q = ṁ·c_p·ΔT = 0.22 kg/s × 3,400 J·kg⁻¹·K⁻¹ × 6.0 K = 4,488 W, within 5 W — a tenth of a percent — of the radiative figure. This is why the operator says the flow meter agrees "without trusting the coating": a degraded coating would corrupt the radiative figure and leave this one untouched. The two methods agreeing is what rules out radiator degradation.

**Radiative sensitivity:** dP/dT = 4P/T = 4 × 4,383 / 283.9 = 61.8 W/K. Rejecting 99 W more therefore needs the plate 99 / 61.8 = 1.60 K warmer — exactly the 285.5 against 283.9 the operator reads. The cabin sits upstream of the plate on the same thermal path and moves with it.

**Thermal time constant:** C / (dP/dT) ≈ 1.7 × 10⁷ J/K ÷ 61.8 W/K ≈ 2.8 × 10⁵ s ≈ 3.2 days. A step input settles to 94% after nine days, which is why the temperature climbed for nine days and then held.

**All electrical power in a closed compartment becomes heat.** Nothing leaves as work; the bus load is a direct heat-input figure.

**Metabolic heat:** 2,150 kcal/day × 4,184 J/kcal ÷ 86,400 s = 104.1 W. In steady state essentially all metabolic energy leaves the body as heat, which is why a resting adult is quoted as roughly a hundred watts.

**A cooling device heats its surroundings.** Any refrigeration process rejects the heat it removes *plus* the work done to remove it, so the net heat released into a closed compartment equals the device's input power. A cold surface is therefore not evidence against a heat source in the same volume. This is the entire coda and the operator never says it.

**Thermal balance:** 4,483 W out − 4,280 W bus − 104 W operator = 99 W unaccounted.

### Invented

Station KROMKA-6 and every log number, including log 104. Radiator area 14.0 m² and emissivity 0.85. Bus load 4,280 W. Coolant mass flow 0.22 kg/s and specific heat 3,400 J·kg⁻¹·K⁻¹. Station effective heat capacity 1.7 × 10⁷ J/K. Setpoint 21.2 °C. The operator's 2,150 kcal diet and the fact that he logs it. The forward hold, the 0.42 m patch, its 3.1 K depression, and its 11 cm displacement overnight.

**The one impossible thing:** a 99 W heat source drawing no current. Everything else in this record is ordinary engineering.
