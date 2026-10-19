# FC9-008 // "THE RIND"

**Slug:** FC9-008 // THE RIND
**Runtime:** 4:21 (261 s) — 31 shots, durations sum to 261 s exactly
**Per-scene seconds:** {1: 34, 2: 38, 3: 40, 4: 40, 5: 40, 6: 35, 7: 10, 8: 24} = 261
**Format:** 16:9 horizontal, three vertical cuts assembled out of it
**Voice:** narrator — unhurried, third person, present tense. The record builds
  one ledger and balances it in scene 5. Nothing in the delivery marks that the
  ledger does not balance.
**Word count:** 385. At 162 wpm that is 142.6 s of speech against 261 s of
  runtime — 45% silence; 40% in the body without the coda. Per-scene table below.
**Motion split:** 11 static / 15 local / 5 model (after stage 6; 9 model at intake)

**Per-scene silence** (measured by `validate.py`)

| Scene | Seconds | Words | Speech | Silence |
|---|---|---|---|---|
| 1 | 34 | 57 | 21.1 s | 38% |
| 2 | 38 | 67 | 24.8 s | 35% |
| 3 | 40 | 68 | 25.2 s | 37% |
| 4 | 40 | 62 | 23.0 s | 43% |
| 5 | 40 | 71 | 26.3 s | 34% |
| 6 | 35 | 44 | 16.3 s | 53% |
| 7 | 10 | 16 | 5.9 s | 41% |
| 8 | 24 | 0 | — | coda, declared |
| **Total** | **261** | **385** | **142.6 s** | **45%** |

**Coda declaration.** Scene 8 is the coda: two text cards over near-black ice,
the melting shot between them, and the channel closer. No voice.

**Scene 6 is at 53%,** inside the ceiling with two points of room. If any line
is cut there the scene must be shortened with it.

**The payoff is on the cards, not in the voice.** The record speaks seven years
once, in scene 6, as the output of an integral. It never says what seven years
means next to fifteen million. That juxtaposition exists only as two lines of
text in the coda, and the last real fact in the file — that no clean sample of
this lake has ever been recovered — is never spoken at all.

---

## Corrections on intake

The script was submitted by the scenario agent on 2026-10-19 with a
`publish.md`. Its arithmetic was checked end to end and holds: 96.3% shield by
volume, 871 g of rind, 8.6 nmol/s through the shell, 0.271 mol a year, 37
years at the starting rate against 7.09 integrated, 76 mmol/L needed against
7.2 µmol/L measured (10,600×), 760× on the generous figure, 350 bar depressing
the melting point 2.6 K. Everything below is the submitted draft with the
following changes and nothing else. `shots.yaml` carries the cleaned prompts.

1. **Narration format.** Submitted as `**Narration**` with `*(over 1.2)*` lines
   between separate quote blocks; the parser found no narration at all. Now one
   `**Narration:**` block per scene with `*[over N.N]*` inside each paragraph.
   SCENARIO-AGENT.md now shows the exact form.

2. **The coda held a voice.** The exemption covers a card block and a held
   silent shot, not a line (record 06, correction 8; record 07, correction 2).
   The draft's 7.1 is scene 7 on its own, lengthened from 8 s to 10 s so it
   stays above the silence floor (41%). The coda is scene 8.

3. **Three static plates in a row in the coda, two in scene 5.** Two
   locked-off frames in a row is twenty seconds with nothing moving
   (CLAUDE.md, Motion Policy). Coda: the melting shot moves between the two
   cards, which also gives `NO CLEAN SAMPLE EXISTS` the air before it that the
   Pacing section asked for, and a slow pull goes before the closer — static,
   model, static, local, static. Scene 5: the silent bore shot moves between
   the two cards; 5.3 is the draft's 5.4 and 5.4 the draft's 5.3. Runtime
   4:15 → 4:21.

4. **A card on a drift.** The gas card sat on 2.2, a local move, and its
   neighbour 2.3 was the static plate. 2.2 is now the static plate for the gas
   card, the silent bubble shot follows it — the cages opening, right after
   the line about them — and the 730 card takes the draft's 2.3 plate, now
   2.4. Every card in the record sits on a static plate.

5. **3.4 moved only light.** "A slow travel of the light along it as the
   source shifts" is a still at $0.70 (record 07, 3.4 and 4.1). It is a
   `local` push along the fracture plane now.

6. **Static plates said what moved in them.** "Only a bead of meltwater
   moves", "only frost sublimating", "almost nothing moves" — a plate is never
   animated, and a frozen bead reads as a stalled player. Every plate now says
   the face is "wet, glassy and perfectly still".

7. **No A4.** It covered only 6.1, and 6.1 references the approved 4.1 as the
   script itself asks. Four anchors.

8. **3.2 said "no display".** The noun is enough to summon one. The hardware
   is "every face plain and blank".

9. **Sound design** is a music cue and eight spot effects (CLAUDE.md, Audio
   Rules, from record 08). The ice arc survives as events; nothing runs under
   the record but the floor and the cue.

10. **Not changed, flagged:** the script nominates no teaser lines (brief
    §10b). They are chosen at stage 9 from the record's own paragraphs. And
    eight of the nine model shots are meltwater or bubbles on ice — right for
    this record, but the batch is judged for monotony at the stills stage.

11. **Stage 6: four water shots became local moves.** 1.1, 3.1 and 5.3 asked
    for a film of meltwater running down the bore walls, 4.1 for a run of
    water down the side of the core. The stills held a wet sheen and nothing
    with an edge; Kling returned two stills, one slid the core along the
    bench and one zoomed in and out ($2.45). Rebuilt as push, drift, push and
    pull from the approved stills. The five water shots that held — 2.3, 4.4,
    6.1, 6.4, 8.2 — all had a bead, a drip or a thread in the still.
    CLAUDE.md and SCENARIO-AGENT.md carry the rule now.

---

## Disclaimer

This record is fiction. The lake, its depth, pressure, temperature, isolation
time, gas supersaturation and measured organic carbon are real and published.
The dissolved oxygen figure is an estimate derived from the published
supersaturation, not a measurement — the lake has never been cleanly sampled.
The animal and every figure attached to it are invented. Details in the
appendix.

---

## Synopsis

Four kilometres under the East Antarctic ice sheet there is a lake 250 km long,
sealed for roughly fifteen million years. The ice above it presses at about 350
bar, which depresses the melting point enough to keep the water liquid at −3 °C.

The ice also carries air locked in clathrates, and when it melts into the lake
the cages open. The water is estimated to hold about 2.5 litres of nitrogen and
oxygen per kilogram — roughly fifty times an ordinary freshwater lake, or around
730 mg of oxygen per litre against about 15 at the surface.

For everything that lives in water, oxygen is the limiting resource, and
low-oxygen animals go flat and thin to gather more of it. Here the gradient runs
backwards, so the geometry inverts: surface area is the liability and volume is
the defence. The specimen is a 120 mm sphere that is 96% shield by volume, with
a 40 mm living core. Oxygen reaches that core at about 8.6 nanomoles a second.

Scene 5 is the ledger. Neutralising one O₂ takes four electrons; oxidising one
carbon atom yields four. One for one. So the water would have to carry at least
as much dissolved carbon as oxygen — and carbon diffuses about three times
slower, so 76 millimoles a litre. Measured organic carbon in the accretion ice
is 86 micrograms a litre. Seven micromoles.

The animal does not feed. The rind is both the shield and the reductant, and the
core eats it from the inside. As the rind thins the diffusion path shortens, so
the arrival rate climbs: at the starting rate the store lasts 37 years;
integrated properly, 7.1.

---

## Style spine

Deep glacial ice under one hard white source held close, so that the ice glows
from within where the beam enters it and everything beyond about a metre is
black. The ice is pale blue-grey and very dense, shot through with flattened
bubbles and fine crystal planes, and every cut face is wet with a thin film of
meltwater. Surfaces that are not ice are scuffed cold steel holding frost. The
palette is one narrow range: pale blue-grey, bone white, black, dull steel. No
warm light, no colour, no lettering, no markings, no people.

**One set, and the lake is never in it.** Every shot is ice, meltwater, or cold
steel. The record never reaches the water it is about — nobody has — so there is
no underwater photography anywhere in this file and no shot looking into open
water. This is the structural reason the single appearance in scene 6 works: the
specimen is *in* ice, held still, and the only thing moving in that shot is
meltwater.

**Distinct from FC9-003.** That record was black water and a hard beam. This one
must not look like it. The dominant texture here is ice itself — bubbles,
fracture planes, cut faces — and the frames are close. If a batch comes back
reading as open water, the anchors have drifted.

## Anchors

- **A1 — ice in deep perspective.** A cylindrical bore of pale blue-grey ice
  receding away, the beam falling off down it into black, the walls wet.
- **A2 — core section head-on, close.** A cylinder of ice lying on cold steel,
  lit across its cut face, frost at the contact line.
- **A3 — macro into ice.** Flattened bubbles and crystal planes backlit at close
  range, shallow depth of field, the ice glowing where the beam enters.
- **A4 — the mass in ice.** A dark form behind cloudy ice at close range, seen
  side-on, its edges diffused by the ice in front of it and never resolved.
- **A5 — cold steel close, head-on.** Scuffed stainless and anodised grey,
  frosted, worn at every edge, the beam raking low across it.

**Repeat reference.** Shot 6.1 is the only view of the specimen. Shot 4.1 shows
the same core section before the camera is close enough to see anything in it —
generate 6.1 against the approved 4.1 still, not A4, so it reads as the same
piece of ice twice and the second look is a discovery rather than a new object.

---

## SCENE 1 — THE SEAL (0:00–0:34)

**Cards**

- On 1.3:

```
ICE ABOVE        ~4,000 m
PRESSURE            350 bar
WATER                -3 C
SEALED            ~15 Myr
```

**Shots**

**Shot 1.1** — local (push), 10 s, anchor A1 — *silent* — *was model; see correction 11*
> A cylindrical bore of pale blue-grey ice receding away from camera, lit by one
> hard white source close behind the lens so the near walls glow from within and
> the far end is black. A thin film of meltwater runs steadily down one wall.
> The camera holds still and the water moves.

**Shot 1.2** — local, 10 s, anchor A3
> Macro into pale blue-grey ice, backlit so it glows, filled with flattened
> lens-shaped bubbles lying in parallel planes, the nearest in focus and the
> rest falling off into soft blue. Very slow push in.

**Shot 1.3** — static, 10 s, anchor A2
> A cylinder of pale ice lying on scuffed cold steel, lit across its wet cut
> face, frost gathered along the line where ice meets metal. Locked off, framed
> with the lower left of frame empty steel. Only a bead of meltwater moves.

**Shot 1.4** — local, 4 s, anchor A3
> Macro into dense ice with no bubbles at all, only faint crystal planes
> crossing frame, glowing where the beam enters. Slow drift right.

**Narration:**
> *[over 1.2]* Four kilometres under the Antarctic ice there is a lake two
> hundred and fifty kilometres long. It has been sealed for about fifteen
> million years.
>
> *[over 1.3, with the card]* The ice above it weighs three hundred and fifty
> bar. At that pressure water stays liquid at minus three degrees, and the lake
> does.
>
> *[over 1.4]* No sunlight has reached it since the Miocene.

---

## SCENE 2 — THE CAGES (0:34–1:12)

**Cards**

- On 2.2:

```
DISSOLVED GAS    2.5 L/kg
VS FRESHWATER         50x
```

- On 2.4:

```
O2, LAKE (EST.)     730 mg/L
O2, SURFACE AT 0 C  14.6 mg/L
```

**Shots**

**Shot 2.1** — local, 10 s, anchor A3
> Macro into ice packed with small rounded gas inclusions at high density, each
> one catching the backlight as a bright point, the ice between them glowing
> pale blue. Slow push in.

**Shot 2.2** — static, 10 s, anchor A2
> A cut face of pale ice on cold steel seen close and slightly oblique, the face
> wet and glassy, with fine open pits across it where inclusions have opened at
> the surface. The lower left of frame is empty wet steel. Locked off.

**Shot 2.3** — model, 10 s, anchor A3 — *silent*
> Macro into ice at a cut edge where it is melting, with a steady stream of fine
> gas bubbles breaking out of the face and rising through the film of water on
> it. Camera static.

**Shot 2.4** — static, 8 s, anchor A2
> A core section on cold steel, locked off, lit across the cut face, wet, glassy
> and perfectly still, the cylinder set right of centre and the lower left of
> frame empty frosted steel.

**Narration:**
> *[over 2.1]* The ice carries air trapped in clathrates — gas locked into cages
> of water under pressure. When that ice melts into the lake, the cages open.
>
> *[over 2.2, with the card]* The water is estimated to hold about two and a
> half litres of nitrogen and oxygen per kilogram. Fifty times an ordinary
> freshwater lake.
>
> *[over 2.4, with the card]* Around seven hundred and thirty milligrams of
> oxygen per litre. Surface water at this temperature holds about fifteen.

---

## SCENE 3 — NOTHING IS THIN (1:12–1:52)

**Cards**

- On 3.3:

```
LOW O2  ->  THIN, HIGH AREA
HIGH O2 ->  COMPACT, LOW AREA
THIN FORMS RECORDED       0
```

**Shots**

**Shot 3.1** — local (drift), 10 s, anchor A1 — *was model; see correction 11*
> A bore of pale ice receding into black, lit from close behind the lens, with
> meltwater running down the walls in several thin threads and a slow drift of
> vapour near the lens where cold air meets the beam. Camera static.

**Shot 3.2** — local, 10 s, anchor A5
> Close head-on on scuffed stainless and anodised grey hardware standing on ice,
> frosted along every edge, the beam raking low across it, worn through to bare
> metal at the corners. No display and no marking on it. Slow drift right.

**Shot 3.3** — static, 10 s, anchor A2
> A core section on cold steel, locked off, lit across its wet cut face, the
> cylinder high and right in frame and the lower left of frame empty frosted
> steel. Only frost sublimating at the edge moves.

**Shot 3.4** — local, 10 s, anchor A3 — *silent*
> Macro into pale ice, backlit and glowing, with a single long fracture plane
> set diagonally across frame like a sheet of frozen glass. Slow push in along
> the plane.

**Narration:**
> *[over 3.1]* For everything that lives in water, oxygen is the limiting
> resource. Animals in low-oxygen water go flat and thin to take in more of it.
>
> *[over 3.2]* The gradient here runs the other way. Oxygen is an oxidiser at
> fifty times the usual concentration, arriving whether it is wanted or not.
>
> *[over 3.3, with the card]* So the geometry inverts. Surface area becomes the
> liability and volume becomes the defence. Nothing down here is thin.

---

## SCENE 4 — THE SPECIMEN (1:52–2:32)

**Cards**

- On 4.3:

```
OUTER DIAMETER     120 mm
LIVING CORE         40 mm
SHIELD BY VOLUME     96%
O2 TO CORE      8.6 nmol/s
```

**Shots**

**Shot 4.1** — local (push), 10 s, anchor A2 — *was model; see correction 11*
> A long cylinder of pale blue-grey ice lying on cold steel, lit along its
> length, wet all over, with a steady run of meltwater tracking down its side
> and pooling on the metal. Nothing visible inside it at this distance. Camera
> static.

**Shot 4.2** — local, 10 s, anchor A3
> Macro into cloudy ice where the clarity breaks down into a dense white
> scattering, the beam entering from the left and dying out within a few
> centimetres. Slow push in.

**Shot 4.3** — static, 10 s, anchor A2
> A core section on cold steel, locked off, lit across the cut face, the cylinder
> running across the upper half of frame and the lower left of frame empty wet
> steel. Only a meltwater bead moves.

**Shot 4.4** — model, 10 s, anchor A3 — *silent*
> Macro into ice with the beam behind it, the glow uneven, and a slow continuous
> rise of meltwater film across the cut face as it thaws. Camera static.

**Narration:**
> *[over 4.1]* The specimen recovered from the accretion ice is a sphere a
> hundred and twenty millimetres across.
>
> *[over 4.2]* Almost all of it is a dense reducing rind. The living tissue is a
> core forty millimetres wide at the centre.
>
> *[over 4.3, with the card]* Ninety-six per cent of the animal by volume is
> shield. Oxygen crossing it reaches the core at about eight and a half
> nanomoles a second.

---

## SCENE 5 — THE LEDGER (2:32–3:12)

**Cards**

- On 5.2:

```
PER O2              4 e-
PER CARBON          4 e-
EXCHANGE           1 : 1
CARBON NEEDED  76 mmol/L
```

- On 5.4:

```
CARBON MEASURED    86 ug/L
                0.007 mmol/L
DEFICIT           10,600x
```

**Shots**

**Shot 5.1** — local, 10 s, anchor A5
> Close head-on on frosted anodised grey hardware on ice, the light low and
> raking, every edge worn and the surface finely scratched, with frost crystals
> standing on the colder faces. Slow drift left.

**Shot 5.2** — static, 10 s, anchor A2
> A core section on cold steel, locked off, lit across the cut face, wet, glassy
> and perfectly still, the cylinder right of centre and the lower left of frame
> empty frosted steel.

**Shot 5.3** — local (pull), 5 s, anchor A1 — *silent* — *was model; see correction 11*
> A bore of pale ice receding into black with meltwater running down one wall in
> a continuous thread. Camera static.

**Shot 5.4** — static, 10 s, anchor A3
> Macro into pale backlit ice, locked off, bubbles sparse and the glow even,
> glassy and perfectly still, the lower left of frame nearly clear ice going to
> black.

**Shot 5.5** — local, 5 s, anchor A3
> Macro into cloudy white ice, the light dying within a short distance, nothing
> resolved inside it. Very slow push in.

**Narration:**
> *[over 5.1]* Neutralising one oxygen molecule costs four electrons. Oxidising
> one carbon atom yields four. The exchange is one to one.
>
> *[over 5.2, with the card]* So the water would need at least as much dissolved
> carbon as oxygen, and carbon diffuses about three times slower. Seventy-six
> millimoles a litre.
>
> *[over 5.4, with the card]* Measured dissolved organic carbon in the accretion
> ice is eighty-six micrograms a litre. Seven micromoles.
>
> *[over 5.5]* The barrier that keeps the oxygen out keeps the carbon out with
> it.

---

## SCENE 6 — SEVEN YEARS (3:12–3:47)

**Cards**

- On 6.3:

```
OXIDISABLE CARBON   10 mol
AT INITIAL RATE       37 y
INTEGRATED           7.1 y
```

**Shots**

**Shot 6.1** — model, 10 s, ref_shot 4.1 — **the only appearance. Silent.**
> *Reference the approved still from 4.1.* The same core section on cold steel,
> now close, with a dark rounded mass held inside the ice a few centimetres
> behind the cut face, its edge diffused by the cloudy ice in front of it and
> never resolving into an outline. A single bead of meltwater runs down the face
> across it and off the bottom of frame. Nothing inside the ice moves. The camera
> holds still.

**Shot 6.2** — local, 10 s, anchor A3
> Macro into the cut face of the same ice, the beam entering low, the white
> scattering dense enough that depth reads only as dimming. Slow drift right.

**Shot 6.3** — static, 10 s, anchor A2
> A core section on cold steel, locked off, lit across the face, the cylinder set
> high in frame, wet, glassy and perfectly still, and the lower left of frame
> empty wet steel.

**Shot 6.4** — model, 5 s, anchor A3 — *silent*
> Macro into pale ice with the meltwater film thickening and beginning to run,
> carrying fine bubbles across the frame with it. Camera static.

**Narration:**
> *[over 6.2]* It does not feed. The rind is both the shield and the reductant,
> and the core consumes it from the inside.
>
> *[over 6.3, with the card]* As the rind thins, the path shortens and the
> oxygen arrives faster. At the starting rate the store lasts thirty-seven
> years. Integrated, seven.

---

## SCENE 7 — THE LAST LINE (3:47–3:57)

**Shots**

**Shot 7.1** — local, 10 s, anchor A2
> A core section on cold steel seen from further back, lit flat across it, the
> steel wet, the ice dull and softened at its edges. Very slow push forward.

**Narration:**
> *[over 7.1]* The lake is fifteen million years old. Its water turns over every
> thirteen thousand three hundred.

---

## SCENE 8 — CODA (3:57–4:21)

**Cards**

- On 8.1:

```
ISOLATION    15,000,000 y
SHIELD LIFE          7.1 y
```

- On 8.3:

```
NO CLEAN SAMPLE EXISTS
```

- On 8.5 (the channel closer, titles.yaml):

```
FILE CLASS NINE
FC9-008 // THE RIND
```

**Shots**

**Shot 8.1** — static, 6 s, anchor A3
> Macro into dark, nearly clear ice with the light almost out of frame, graded
> to black at the lower left of frame. Locked off.

**Shot 8.2** — model, 5 s, anchor A3 — *silent*
> Macro into ice that is visibly melting, the cut face wet and soft at its edges
> and the meltwater film running continuously across frame. Camera static.

**Shot 8.3** — static, 4 s, anchor A3
> Macro into dark ice, dimmer still, almost a single tone, one bubble catching a
> trace of light near the top of frame. Locked off.

**Shot 8.4** — local, 4 s, anchor A3
> Macro into dark ice, a few flattened bubbles faintly lit near the centre, the
> rest falling to black. Slow pull back.

**Shot 8.5** — static, 5 s, anchor A3
> Dark ice at its dimmest, near a flat tone across the whole frame. Locked off.

*(No narration. The two figures the record is actually about sit next to each
other on card 8.1 and are never spoken together.)*

---

## Pacing (assembly)

Defaults: 1.2 s between paragraphs, 2.0 s across a scene cut.

| Where | Gap | Reason |
|---|---|---|
| Before the first line of scene 1 | 3.0 s | Cold open is image first. Shot 1.1 runs 10 s with no card and no voice. |
| Scene 2, before "Around seven hundred and thirty milligrams of oxygen per litre." | 2.0 s | The card types the two numbers in the same beat the voice reaches them. |
| Scene 3, before "Nothing down here is thin." | 1.8 s | The card finishes on `THIN FORMS RECORDED 0` at the same moment. Voice and card land together or the line is wasted. |
| Scene 4 → 5 cut | 2.5 s | Out of description and into arithmetic. |
| Scene 5, before "The barrier that keeps the oxygen out keeps the carbon out with it." | 2.5 s | Flattest line in the record and the hinge of the whole file. Silence on both sides. |
| Scene 5 → 6 cut | 3.0 s | Into shot 6.1, silent for its full 10 s. |
| Scene 6, shot 6.1 entire | silent | The only appearance. No voice for the full 10 s, so the cue sits at full level under it — the one long stretch where nothing but the music speaks. |
| Scene 6 → 7 cut | 3.0 s | Already longer: 6.4 is 5 s with no voice. |
| Between cards 8.1 and 8.3 | 5 s (8.2) | 8.3 is the last real fact in the record and it is never spoken. It needs to arrive alone. |

## Voice direction

Narrator. Unhurried, third person, present tense.

- **No reverb in the delivery, and none added.** Four kilometres of ice is
  anechoic. If the voice sounds like it is in a space, the record is wrong.
- Scenes 1 through 4 are description and scene 5 is a balance sheet that does not
  balance. Read identically.
- "The exchange is one to one" is read as a bookkeeping statement, because it is
  one.
- "The barrier that keeps the oxygen out keeps the carbon out with it" is the
  flattest line in the episode. No weight on either half.
- "Integrated, seven." — two words, dropped, no emphasis. The narrator does not
  know that number is small.
- Chemical and unit names are read plainly and at the same speed as everything
  else. Micromoles is not a special word.
- There is no closing thought and the narrator never addresses the viewer.

## Sound design (music prompt + spot effects)

*Rewritten in production on 2026-10-19 for the channel's new bed (CLAUDE.md,
Audio Rules): a synthesised floor and one music cue under the whole record,
ducked 7 dB under the voice, plus a few spot effects in the pauses. The
submitted version ran room tone and a meltwater trickle under the whole
record; the ice arc is kept, as events.*

**Music** — one cue, generated at the full runtime (255 s):

> Slow, cold, sparse ambient music for a documentary about a lake sealed under
> four kilometres of Antarctic ice. Sustained mid-register strings and a soft
> glassy pad, faint crystalline high tones drifting over them, very little
> bass. No melody, no beat, no drums, no vocals, no swell. One gradual thinning
> across the whole piece, ending almost bare. Quiet enough to sit under a calm
> speaking voice the whole way through.

**Spot effects — the ice.** Eight events, all in pauses, all on silent shots.
The arc of the submitted script survives in where they sit: established in
the cold open, present once per scene through 2–4, **absent for the whole of
scene 5** (the arithmetic is dry), back on 6.1 closer than before, then gone —
except the meltwater, which is the only sound of the coda.

| Shot | At | Effect | Note |
|---|---|---|---|
| 1.1 | 2.5 s | ice creak A | cold open, first sound after the music |
| 1.1 | 6.5 s | ice groan B | |
| 2.3 | 7.5 s | ice creak A | −3 dB, end of the silent bubble shot |
| 3.4 | 7.5 s | ice groan B | −3 dB |
| 4.4 | 7.5 s | ice creak A | −3 dB |
| 6.1 | 2.0 s | ice crack, close | +2 dB — closer than it has been |
| 6.1 | 6.5 s | ice groan B | |
| 8.2 | 0.5 s | meltwater drops, 8 s | runs on under card 8.3 |

Prompts are in `audio.yaml` under `sfx:`. Each is one dry close event with a
body — a creak, a groan, a muffled crack, round drops — and none of them is a
tick, a squeak or anything high.

- The voice stays dry — no reverb in the delivery and none added. The cue may
  have air in it; the narrator may not.
- Shot 6.1 is silent for its full 10 s, so the cue sits at full level under
  it with two ice events. No stinger, no swell. If a take of the cue rises on
  its own in the middle, it is rejected, not trimmed around.
- Video is generated with audio off throughout. Nothing above is prompted.

## Verticals — three candidate moments

**V1 — 730 against 15.** In on the first word of "The ice carries air trapped in
clathrates." Voice present at frame one. Out at the end of "Surface water at this
temperature holds about fifteen," a sentence end with a real pause after it.
Picture: 2.1, 2.2, 2.3 (the bubbles), 2.4. Spoken figures: 2.5 L/kg, fifty times, 730 mg/L, 15 mg/L.
Nothing in this cut depends on a card.

**V2 — nothing is thin.** In on "For everything that lives in water, oxygen is the
limiting resource." Out at the end of "Nothing down here is thin," a paragraph
end. Picture: 3.1, 3.2, 3.3. Spoken figures: fifty times. This cut is the only
one that carries an idea rather than a number, and it is the most likely of the
three to travel.

**V3 — the ledger.** In on "Neutralising one oxygen molecule costs four
electrons." Hard cut immediately after the word **"micromoles"** in "Measured
dissolved organic carbon in the accretion ice is eighty-six micrograms a litre.
Seven micromoles." Word boundary, sentence end, consequence withheld — the cut
states the requirement and the measurement and stops without saying they do not
match. Picture: 5.1, 5.2, 5.4. Spoken figures: four electrons, one to one, 76
mmol/L, 86 µg/L, 7 µmol/L. **Do not extend** into "The barrier that keeps the
oxygen out keeps the carbon out with it" — that line closes the gap this cut
exists to leave open.

---

## Appendix — what is real and what is invented

### Real, verifiable

- **The lake.** Subglacial Lake Vostok, East Antarctica. About 250 km long and
  50 km wide at its widest, roughly 12,500 km², average depth 432 m. Its surface
  sits about 4,000 m below the ice surface and about 500 m below sea level.
- **Isolation.** Estimated sealed about 15 million years ago, with the range
  given as 15–25 million years. **The effective mean residence time of the water
  is 13,300 years** — the lake is old, its water is not, and the coda uses that
  deliberately.
- **Pressure and temperature.** Hydrostatic pressure at the lake surface is
  reported as about 345–355 bar; the record says 350. Water temperature is
  calculated at about −3 °C. These are consistent and the record can show why:
  the melting point of ice falls about 0.0074 K per bar, so 350 bar depresses it
  by 2.6 K, to −2.6 °C. The lake is liquid because of the load above it.
- **The gas supersaturation.** The overlying ice carries air in clathrates;
  melting into the lake releases it. The water is estimated to hold about 2.5
  litres of nitrogen and oxygen per kilogram — roughly **50×** an ordinary
  surface freshwater lake. Modelled by Hugh McKay, Chris McKay and colleagues
  (Geophysical Research Letters, 2003).
- **The 730 mg/L figure is derived, not quoted.** Freshwater at 0 °C saturates at
  about 14.6 mg O₂/L. 50 × 14.6 = 730 mg/L, which is 22.8 mmol/L. The record says
  "around" and "estimated" both times it is spoken, because the lake water has
  never been cleanly sampled.
- **No clean sample exists.** The Russian team reached the lake in 2012; in 2017
  they reported that the recovered water was too heavily contaminated with
  drilling fluid to give reliable chemistry or biology. This is the last card in
  the record and it is true.
- **The organic carbon.** Dissolved organic carbon measured in Vostok accretion
  ice is on the order of **79–510 µg/L**, with 86 µg/L the commonly cited figure
  — about 7 µmol C/L. **Unit warning for anyone re-checking this:** at least one
  secondary rendering of the Siegert et al. 2001 review prints these as mg/L.
  That is a unit error; 79–510 mg/L of DOC would be hundreds of times richer than
  seawater. The values are micrograms per litre.
- **Electron bookkeeping.** Reducing O₂ to two H₂O takes 4 electrons. Oxidising
  one carbon atom from 0 to +4 releases 4. One carbon per one O₂, exactly — this
  is stoichiometry, not an estimate, and it is what makes scene 5 checkable.
- **Diffusion coefficients at this temperature.** O₂ in water ≈ 1.0 × 10⁻⁹ m²/s
  at 0 °C; small sugars ≈ 0.3 × 10⁻⁹ m²/s. Scaled from 25 °C values by
  Stokes–Einstein using the viscosity of water at 0 °C, which is about twice that
  at 25 °C.

### Invented

- The animal: a 120 mm sphere with a 40 mm living core, so 96% shield by volume
  and 871 g of rind at unit density.
- Its rind carrying **10 mol of oxidisable carbon** (129 g of carbon in 871 g of
  tissue — conservative for organic matter that is roughly 45% carbon by mass).
- That it does not feed, that the core consumes the rind, and that no
  thin-bodied form has been recorded.
- The specimen's recovery from accretion ice.

### The arithmetic, so it can be checked

- **Influx.** Steady-state diffusion through a spherical shell, J = 4πD·ΔC·Rr /
  (R − r). With D = 1.0 × 10⁻⁹ m²/s, ΔC = 22.8 mol/m³, R = 0.060 m, r = 0.020 m:
  J = 4π × 1.0 × 10⁻⁹ × 22.8 × 0.0012 / 0.040 = **8.6 × 10⁻⁹ mol/s**, which is
  0.742 mmol/day and 0.271 mol/year.
- **The carbon requirement.** Break-even needs carbon influx ≥ oxygen influx in
  moles. Through a non-selective barrier influx scales as D·C, so
  C_carbon ≥ (D_O₂/D_carbon) × C_O₂ = 3.33 × 22.8 = **76 mol/m³ = 76 mmol/L**.
  Against 7 µmol/L measured, the deficit is **10,600×**.
- **The most generous reading still fails.** Siegert et al. inferred the lake
  water itself might reach DOC "up to 1,200 µg/L" — 100 µmol/L. Even taking that
  figure, the deficit is 760×. The record uses the measured accretion-ice value
  and the appendix states the generous one, because the conclusion does not
  depend on which is used.
- **The shield life.** The rind is consumed from the inside, so the core radius
  r grows and the diffusion path R − r shrinks, and the arrival rate climbs.
  Balancing 4πr²ρ dr = J(r) dt gives dt = ρ·r(R − r)dr / (D·ΔC·R), so
  t = (ρ / D·ΔC·R) ∫ r(R − r) dr from 0.020 to 0.060. With ρ = 10 mol / 8.713 ×
  10⁻⁴ m³ = 11,477 mol/m³ and the integral equal to 2.667 × 10⁻⁵:
  t = (11,477 / 1.368 × 10⁻⁹) × 2.667 × 10⁻⁵ = 2.24 × 10⁸ s = **7.1 years**.
- **Why both numbers are on the card.** Dividing the store by the starting rate
  gives 10 / 0.271 = 36.9 years, which is wrong by a factor of five because it
  ignores the acceleration. The card shows 37 and 7.1 side by side on purpose:
  the naive answer is the one a viewer will get if they check, and the record
  gets ahead of it.
- **Consistency.** The 96% and the 8.6 nmol/s are the same two radii seen twice.
  The 10 mol and the 7.1 years are the same store seen twice. Changing R or r
  moves all four figures, and changing the carbon load moves only the last two.
