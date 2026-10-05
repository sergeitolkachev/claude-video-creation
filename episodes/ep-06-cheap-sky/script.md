# FC9-006 // "THE CHEAP SKY"

**Slug:** FC9-006 // THE CHEAP SKY
**Runtime:** 5:00 (300 s) — 33 shots, durations sum to 300 s exactly
**Per-scene seconds:** {1: 36, 2: 40, 3: 50, 4: 45, 5: 45, 6: 60, 7: 24} = 300
**Format:** 16:9 horizontal, three vertical cuts assembled from it, one teaser
**Voice:** narrator — unhurried, third person, present tense. The record spends
  four scenes establishing that flight here is almost free, and then spends
  three establishing what it actually costs. The delivery does not mark the
  turn.
**Word count:** 426. At 162 wpm that is 157.8 s of speech against 300 s of
  runtime — 47.4% silence overall; 42.8% across Scenes 1–6 (276 s) with the
  declared coda excluded.
**Motion split:** 9 static / 2 local / 22 model

### Per-scene silence

| Scene | Seconds | Words | Speech | Silence |
|---|---|---|---|---|
| 1 | 36 | 57 | 21.1 s | 41.4% |
| 2 | 40 | 57 | 21.1 s | 47.2% |
| 3 | 50 | 86 | 31.9 s | 36.3% |
| 4 | 45 | 72 | 26.7 s | 40.7% |
| 5 | 45 | 69 | 25.6 s | 43.2% |
| 6 | 60 | 85 | 31.5 s | 47.5% |
| 7 | 24 | 0 | 0 | 100% — **coda, declared** |
| **Total** | **300** | **426** | **157.8 s** | **47.4%** |

Scene 3 is the tight one at 36%. Record 02 came in slower than planned and
three scenes fell under the floor; if scene 3's takes land slow, the fix is
picture, not a cut line.

---

## Corrections on intake

The script was submitted by the scenario agent on 2026-09-25 with a
`publish.md`. Its arithmetic was checked end to end and almost all of it
holds — density, the human-flight speeds, 0.65 W against 27 W, the 0.42 K,
the Arrhenius quarter, the flux, the area. Everything below is the submitted
draft with the following changes and nothing else.

1. **No two ffmpeg shots in a row — eleven shots moved to Kling.** The draft
   was 10 static / 12 local / 11 model and ran ffmpeg shots in series, the
   longest six shots and 46 s long (1.2 through 2.3) with nothing alive in the
   frame. Four of those shots also broke the never-animated rule outright: the
   distant flyers in 2.2 and 4.4 were `local` (an animal hanging still in a
   push across a photograph), 6.2 was a `local` of falling particulate, and 7.4
   was a `static` with "one fleck of particulate" frozen in it. Moved to
   `model`: 1.2→1.3, 1.4, 2.2, 3.2, 3.4, 4.2, 4.4, 5.1, 6.2, 6.4, 7.4→7.3. Each
   is given a motion the model holds — haze rolling at a horizon, dry dust
   drifting over sand, vapour off a wet cobble, drizzle on a pool, particulate
   settling, the flyers translating. Split is now 9 / 2 / 22 and no two
   ffmpeg shots touch anywhere in the record. First-roll video goes from
   $6.65 to $13.65.

2. **Cold open.** The pacing table put the first line at 3.0 s; the shot list
   had 1.1 silent for its full 10 s, which puts the first word at ~12 s and
   fails the first-ten-seconds test. Moving the voice to 3 s with the draft's
   order would have put the flight card on 1.3 nine seconds after its line.
   So the voice starts at 3 s over 1.1, and the card plate (was 1.3) is now the
   second shot of the scene, under the line it answers. The moving plain (was
   1.2) is third.

3. **Pauses on paragraph boundaries.** The pacing asked for 1.8 s before
   "Nothing has them." and 2.5 s before "No animal has been recorded…", both
   mid-paragraph. Both paragraphs are split there; not a word changed.

4. **Static plates hold nothing that moves.** 1.3, 3.3, 4.3, 5.2 and 6.3 said
   "only haze moves" or "a thin drift of haze near the horizon". A still of a
   drifting thing is a stalled player. The haze in every plate is now
   described as one smooth continuous gradient of tone.

5. **2.5 W against a card reading 2.6 W.** The voice said "two and a half
   watts" over a card that says `WASTE HEAT 2.6 W`. The appendix derives 2.60.
   The line is now "The flyer makes two point six watts."

6. **Ninety minutes is a time constant, not "air temperature".** With the
   appendix's own figures, mc/hA = 8000 / 1.5 = 5333 s = 89 min. After one
   time constant a body has lost 63% of its excess, not all of it. The line is
   now "On the ground it loses most of that in about ninety minutes." and the
   card reads `COOLING TIME ~90 min`.

7. **The acetylene figure is the published one.** The draft computed 310 kJ
   per mole from 298 K standard Gibbs energies and attributed the metabolism
   to McKay and Smith, whose paper gives **334 kJ/mol** for the acetylene
   reaction under Titan conditions. A record that names a paper uses the
   paper's number. Everything downstream moves with it: 111 kJ per mole of
   hydrogen, 1.85 GW for the moon ("one point eight gigawatts"), about 570
   million animals, one per seventh of a square kilometre. Still under Hoover
   Dam's 2.08 GW, so the coda's comparison stands.

8. **The coda holds no voice.** The draft declared scene 7 a coda and put a
   narrated shot at its head. The exemption covers a closing card block and a
   held silent shot, not a line. That shot and its line (was 7.1) close scene
   6 now, as 6.6; scene 6 runs 60 s at 47.5% silence and the coda is 24 s of
   cards over haze.

9. **Two anchors dropped.** A4 (flyer at distance) and A5 (hardware close)
   each served one shot's distance. The distant flyers in 2.2 and 4.4 are
   specks over a horizon and sit on A2; the resolved flyer in 6.1 is against
   open haze and sits on A1. The hardware close-up, 5.1, is a distance that
   happens once and goes text-to-image against its own spine, the way record
   05's regolith macro did. Three anchors: A1 haze, A2 plain, A3 ground macro.

10. **6.1 glides, it does not beat.** A membrane wing flapping is a soft
    surface re-drawn every frame — the class that cost record 05 three takes
    on one strap. The flyer crosses on a rigid glide, pure translation. The
    wingbeat stays in the sound, off screen, before it enters.

11. **Verticals re-picked and a teaser added.** The draft's V1 was built
    entirely from ffmpeg shots and V3 carried about 12 s of voice. Both fixed;
    see below. The draft nominated no teaser.

## Changes after intake (stages 4–7)

12. **Stills.** 1.3 re-framed low and close (A2 had returned the same frame as
    1.2, its neighbour). 5.1's background became the plain in haze (all four
    first seeds stood on a studio backdrop). 6.1's flyer is now a crescent
    membrane whose body is a ridge along its leading edge, with no head, tail
    or legs — the first prompt named a head and got a bird and a fruit bat.
    Cobbles are "opaque matte cream" everywhere: "ice" returned glass.
13. **4.2 is built in ffmpeg** (a slow push on the approved still) after two
    Kling rolls both grew the pale deposit into a heap.
14. **2.3 and 2.4 swapped.** After narration, "Nothing has them." landed at
    71.9 s, past the card plate. The dust drift now runs under "Legs are a
    solution…" and the WALKING FORMS plate closes the scene under "Nothing has
    them." — the beat the pacing table asked for.
15. **The turn pause grew.** 4.0 s of hold before "Nothing here is warm."
    instead of the table's 2.5, which leaves ~7 s of silence over the drizzle
    and pulls "That puts it four tenths…" into range of its card.

---

## Disclaimer

This record is fiction. Titan's gravity, atmospheric density, surface
temperature and pressure are real and measured; the hydrogen flux is a published
Cassini result; the acetylene-hydrogen metabolism is a published hypothesis that
has never been confirmed. The animal and every figure attached to it are
invented. Details in the appendix.

## Synopsis

On Titan, lift is nearly free. The atmosphere is 4.4 times denser than Earth's
at sea level and the gravity is one seventh, so holding a four-kilogram animal
in the air costs about two thirds of a watt — against twenty-seven for the same
animal on Earth. Under those terms legs are a solution to a problem that does
not exist, and nothing on the surface has them.

The cost that does exist is heat. At 94 K in a dense atmosphere, a flying body
sheds warmth at roughly 25 W per square metre per kelvin, and a flyer of this
size produces 2.6 W of waste heat. That buys it four tenths of a kelvin above
the air it moves through. A sparrow runs forty.

Those four tenths are worth about a quarter of its metabolic rate, and its power
output in flight exceeds what flight costs by less than that quarter. The record
does not say what follows. It gives the cooling time on the ground, and the
number of recorded relaunches, on the same card.

It closes on the moon's total energy budget, derived from a flux Cassini
measured: 1.8 gigawatts, for everything alive on a body larger than Mercury.

---

## Style spines and anchors

**Declared deviation from the palette rule.** The channel forbids warm light as
the light of a scene and allows it only as a named practical lamp. This record
is the exception and it is deliberate: the amber is not a lamp and not a grade,
it is the only light this moon has, and the whole episode is lit by it. There is
exactly one palette here and no second source anywhere.

**One set.** Exterior throughout — surface, low air, open haze. No interiors, no
vehicles, no room nouns anywhere.

Three spines, one per camera distance, because a ground noun in the haze spine
puts a horizon in every sky shot and a horizon noun in the macro spine puts a
landscape in every top-down frame. A fourth, for 5.1 only.

**Haze spine (A1).** Deep orange haze in every part of the picture, the light
diffuse and arriving evenly from the whole sky at once, dim and flat, roughly a
thousandth of Earth daylight. Depth reads only as colour, deepening with
distance. Palette amber, ochre, brown-grey and dull cream, nothing else. No
lettering, no people.

**Surface spine (A2).** Dark grey-brown organic sand and rounded pale ice
cobbles, damp with liquid methane, under flat diffuse amber light that arrives
from the whole sky at once, so that nothing casts a shadow. Everything at any
distance softens into orange haze. Palette amber, ochre, brown-grey and dull
cream, nothing else. No lettering, no people.

**Ground macro spine (A3).** Dark grey-brown organic sand with fine even grain
and rounded pale ice cobbles, damp with liquid methane, every part of the
picture at close to the same distance from the lens. Flat diffuse amber light,
shadowless. Palette amber, ochre, brown-grey and dull cream, nothing else. No
lettering, no people.

**Hardware spine (5.1 only).** Scuffed metal and pitted grey composite, every
edge worn back to bare metal, fine dark organic dust packed into every seam,
under flat diffuse amber light with no shadow. Palette amber, ochre,
brown-grey and dull cream, nothing else. No lettering, no people.

**Anchors**

- **A1 — open haze.** Graded amber depth with no ground and no horizon, only
  density falling off with distance.
- **A2 — surface plain, wide.** Camera at ground level, dark sand and pale ice
  cobbles under flat light, horizon in the upper third dissolving into haze,
  lower left quarter empty damp sand.
- **A3 — ground macro, top-down.** Damp sand and rounded cobbles at close
  range, shallow depth of field.

**Same-object reference.** Shot 4.4 references the approved still of **2.2**, so
the distant shapes read as the same population seen twice.

---

## SCENE 1 — CHEAP (0:00–0:36)

**Shot 1.1** — model, 10 s, anchor A1
> Deep orange haze filling frame with no ground and no horizon, the amber
> deepening with distance. Fine dark particulate drifts slowly across frame on
> a steady current. The camera holds still and the air moves.

**Shot 1.2** — static, 10 s, anchor A2
> The sand and cobble plain under flat amber light, locked off, framed with the
> lower left of frame empty damp sand and the cobble field set right of centre.
> The haze at the horizon one smooth continuous gradient of tone.

**Card 1.2** (types on with "Surface gravity is one seventh…")
```
HUMAN + 2 m² WING
TITAN       4.2 m/s
EARTH        24 m/s
```

**Shot 1.3** — model, 10 s, anchor A2
> A wide plain of dark grey-brown organic sand scattered with rounded pale ice
> cobbles under flat shadowless amber light, the horizon soft about a kilometre
> out, with a slow roll of haze moving along the horizon. Camera static.

**Shot 1.4** — model, 6 s (5 s generated, retimed 1.2x), anchor A3
> Macro top-down on damp dark sand and two rounded pale ice cobbles under flat
> shadowless light, with a fine dry drift of dark dust moving slowly across the
> sand between them. Camera static.

**Narration:**
> Titan is the only moon in the solar system with a real atmosphere. It is four
> point four times as dense as air at sea level.
>
> Surface gravity is one seventh of Earth's. A human wearing two square metres of
> wing would fly at four point two metres per second.
>
> On Earth, the same wing needs twenty-four.

---

## SCENE 2 — NOTHING WALKS (0:36–1:16)

**Shot 2.1** — local, 10 s, anchor A2
> A wide dune field of dark organic sand under flat amber light, the crests low
> and rounded and the troughs damp, every surface smooth and unbroken, the far
> dunes lost in haze. Slow drift left.

**Shot 2.2** — model, 10 s, anchor A2
> Amber haze over a soft dune horizon set low in frame, with three small dark
> shapes very far off and high, each no more than a few pixels across and half
> dissolved by the air between them and the camera. The three shapes drift
> slowly left together. Camera static.

**Card 2.2** (types on with "The same animal on Earth takes twenty-seven.")
```
FLIGHT POWER, 4 kg
TITAN        0.65 W
EARTH          27 W
```

**Shot 2.3** — model, 10 s, anchor A2 *(was 2.4; swapped after narration)*
> Wide dark sand and pale cobbles under flat amber light, with a fine dry
> drift of organic dust moving steadily across the surface from left to right
> and a slow roll of haze at the horizon. Camera static.

**Shot 2.4** — static, 10 s, anchor A3 *(was 2.3)*
> Macro top-down on damp dark organic sand under flat shadowless light, the
> surface smooth and unbroken, with the lower left of frame empty smooth sand.
> Locked off.

**Card 2.4** (lands with "Nothing has them.")
```
WALKING FORMS RECORDED    0
```

**Narration:**
> Lift costs almost nothing here. Holding a four-kilogram animal in the air takes
> about two thirds of a watt.
>
> The same animal on Earth takes twenty-seven. Everything that moves on this
> surface is airborne, and there are no walking forms at all.
>
> Legs are a solution to a problem that does not exist here.
>
> Nothing has them.

---

## SCENE 3 — WHAT IS NOT FREE (1:16–2:06)

**Shot 3.1** — model, 10 s, anchor A1
> Open amber haze with no ground and no horizon, dense enough that depth reads
> as colour alone, with fine particulate streaming steadily across frame on a
> strong current. Camera static.

**Shot 3.2** — model, 10 s, anchor A3
> Macro top-down on a pale rounded ice cobble beaded with clear liquid methane,
> the surface damp and slightly frosted, under flat shadowless amber light, a
> faint vapour rising slowly off the wet surface and leaving frame. Camera
> static.

**Shot 3.3** — static, 10 s, anchor A2
> Wide dark sand plain under flat amber light with a low ridge of pale cobbles
> across the upper third of frame, locked off, the lower left of frame empty
> damp sand, the haze one smooth continuous gradient of tone.

**Card 3.3** (types on with "That puts it four tenths of a kelvin…")
```
CONVECTION    25 W/m²K
WASTE HEAT      2.6 W
SPARROW         +40 K
THIS           +0.4 K
```

**Shot 3.4** — model, 10 s, anchor A3
> Macro top-down on damp organic sand with a shallow standing pool of clear
> liquid a few centimetres across, a fine sparse drizzle landing on it and each
> drop opening one small ring that spreads and fades. Camera static.

**Shot 3.5** — model, 10 s, anchor A1 — *silent*
> Open amber haze, no ground, no horizon, with a slow rolling movement in the
> haze itself as denser and thinner air mixes across frame. Camera static.

**Narration:**
> Lift is free. Heat is not. The air is at ninety-four kelvin, and it is four
> times denser than Earth's.
>
> A body moving through it loses warmth at about twenty-five watts per square
> metre per kelvin. The flyer makes two point six watts.
>
> That puts it four tenths of a kelvin above the air it is flying through. A
> sparrow runs forty kelvin above the air around it.
>
> Nothing here is warm. Nothing here can be. The whole biosphere runs at the
> temperature of the air.

---

## SCENE 4 — THE REACTION (2:06–2:51)

**Shot 4.1** — model, 10 s, anchor A1
> Open amber haze with a faint brighter band high in frame where the upper air
> scatters more light, and a slow continuous fall of fine dark particulate
> through the whole frame from top to bottom. Camera static.

**Shot 4.2** — model, 10 s, anchor A3
> Macro top-down on damp dark sand showing a thin pale deposit over it like fine
> frost, the crystals just resolved, under flat shadowless light, with fine pale
> particulate settling slowly onto it from above. Camera static.

**Shot 4.3** — static, 10 s, anchor A2
> Wide plain of dark sand and pale cobbles under flat amber light, locked off,
> the cobble field set high and right in frame and the lower left of frame empty
> smooth sand, the haze one smooth continuous gradient of tone.

**Card 4.3** (types on with "Acetylene and hydrogen recombine…")
```
C2H2 + 3H2 -> 2CH4
dG       -334 kJ/mol
PER H2   -111 kJ/mol
```

**Shot 4.4** — model, 10 s, anchor A2, *reference the approved still of 2.2*
> Amber haze over a soft horizon with two small dark shapes very far off and
> high, unresolved and half dissolved in the air between them and the camera.
> The two shapes drift slowly right. Camera static.

**Shot 4.5** — model, 5 s, anchor A1 — *silent*
> Open amber haze with fine particulate falling steadily through frame, nothing
> else in view. Camera static.

**Narration:**
> At ninety-four kelvin there is no liquid water and no oxygen. The proposed
> chemistry is different.
>
> Sunlight breaks methane apart in the upper atmosphere. Hydrogen and acetylene
> fall out of it and settle toward the ground.
>
> Acetylene and hydrogen recombine into methane, releasing about three hundred
> and thirty-four kilojoules per mole of acetylene. Proposed as a metabolism in
> two thousand five.
>
> It has never been confirmed. Nothing has ruled it out either.

---

## SCENE 5 — THE MARGIN (2:51–3:36)

**Shot 5.1** — model, 10 s, text-to-image against the hardware spine
> Close head-on on a scuffed metal and pitted grey composite housing standing
> on dark sand, dulled all over by fine settled organic dust, every edge worn,
> under flat shadowless amber light, every face of it plain worn material, with
> a fine dry drift of dust moving slowly across the sand in front of it. Camera
> static.

**Shot 5.2** — static, 10 s, anchor A2
> Wide dark sand under flat amber light with a shallow rise across the right of
> frame, locked off, the lower left of frame empty smooth sand, the haze one
> smooth continuous gradient of tone.

**Card 5.2** (types on with "The four tenths of a kelvin…")
```
Ea             50 kJ/mol
RATE LOSS AT -0.4 K   24%
FLIGHT MARGIN        <24%
```

**Shot 5.3** — model, 10 s, anchor A1
> Open amber haze with the particulate moving slowly, almost hanging, drifting
> rather than falling. Camera static.

**Shot 5.4** — static, 10 s, anchor A3
> Macro top-down on damp dark sand, smooth and unbroken, with one pale ice
> cobble at the right edge of frame and the lower left of frame empty sand.
> Locked off.

**Card 5.4** (types on with "On the ground…")
```
COOLING TIME       ~90 min
RELAUNCHES OBSERVED      0
```

**Shot 5.5** — model, 5 s, anchor A2 — *silent*
> Wide dark sand plain under flat amber light with a thin dry drift of dust
> moving across the surface and nothing else in frame. Camera static.

**Narration:**
> Reaction rates depend on temperature, and at ninety-four kelvin that dependence
> is steep.
>
> The four tenths of a kelvin the animal makes by flying is worth about a quarter
> of its metabolic rate.
>
> Its power output in flight exceeds what flight costs by less than that quarter.
>
> On the ground it loses most of that in about ninety minutes.
>
> No animal has been recorded leaving the ground after that.

---

## SCENE 6 — THE CEILING (3:36–4:36)

**Shot 6.1** — model, 10 s, anchor A1 — **the only resolved appearance. Silent.**
> A single dark flyer crossing frame from right to left at middle distance
> against flat amber haze, seen side-on, its wings held out wide and still, the
> membrane thin enough that the haze shows through it at the trailing edge. It
> glides on a level line without beating; its head stays soft and unresolved.
> The camera holds still and the flyer crosses out of frame.

**Shot 6.2** — model, 10 s, anchor A1
> Open amber haze, no ground, no horizon, with a slow steady fall of fine pale
> particulate through frame. Camera static.

**Shot 6.3** — static, 10 s, anchor A2
> Wide dark sand and pale cobbles under flat amber light, locked off, with the
> cobble field high and right and the lower left of frame empty damp sand, the
> haze one smooth continuous gradient of tone.

**Card 6.3** (types on with "Ten to the twenty-eighth…")
```
H2 FLUX        1E28 /s
              16,600 mol/s
PER H2          111 kJ/mol
TOTAL              1.8 GW
```

**Shot 6.4** — model, 10 s, anchor A2
> A very wide plain of dark organic sand under flat amber light, the horizon
> almost entirely dissolved so that ground and sky meet without an edge, with a
> slow roll of haze moving across that meeting line. Camera static.

**Shot 6.5** — model, 10 s, anchor A1 — *silent*
> Open amber haze with a thinning of the particulate across frame, the current
> slowing until almost nothing is moving. Camera static.

**Shot 6.6** — local, 10 s, anchor A2
> Wide dark sand plain under flat amber light, empty, the horizon soft and the
> haze thick enough that distance reads only as colour, one smooth continuous
> gradient of tone. Very slow push forward.

**Narration:**
> Cassini measured hydrogen moving downward through the lower atmosphere and
> disappearing at the surface. Mineral catalysis would also account for it.
>
> Ten to the twenty-eighth molecules every second, for the whole moon. Sixteen
> thousand six hundred moles a second.
>
> At a hundred and eleven kilojoules per mole, that is one point eight
> gigawatts. It is the entire energy budget of everything alive on Titan.
>
> Divided by the flyer, that supports about five hundred and seventy million
> animals. One for every seventh of a square kilometre.

---

## SCENE 7 — CODA (4:36–5:00)

**Declared coda.** Four shots over near-empty haze, no voice. The last two
figures of the record are on the cards and are never spoken. Every card has a
plate of its own, the channel closer included.

**Shot 7.1** — model, 5 s, anchor A1 — *silent*
> Open amber haze, almost featureless, with two or three flecks of particulate
> drifting slowly across frame. Camera static.

**Shot 7.2** — static, 7 s, anchor A1
> Open amber haze, graded darker toward the lower left of frame, which is empty,
> one smooth continuous gradient of tone. Locked off.

**Card 7.2**
```
TITAN BIOSPHERE    1.8 GW
HOOVER DAM        2.08 GW
```

**Shot 7.3** — model, 6 s (5 s generated, retimed 1.2x), anchor A1
> Open amber haze, flatter and dimmer than before, almost a single tone, with
> one fleck of particulate drifting slowly near the top of frame. Camera static.

**Card 7.3**
```
SURFACE AREA    8.3E7 km²
```

**Shot 7.4** — static, 6 s, anchor A1
> Open amber haze at its dimmest, near a single flat tone across the whole
> frame. Locked off.

**Card 7.4** (channel closer, centred)
```
FILE CLASS NINE
FC9-006 // THE CHEAP SKY
```

---

## Pacing (assembly)

Defaults: 1.2 s between paragraphs, 2.0 s across a scene cut.

| Where | Gap | Reason |
|---|---|---|
| Before the first line of scene 1 | 3.0 s | Image first. The haze moves for three seconds before anyone speaks. |
| Scene 2, before "Nothing has them." | 1.8 s | The card `WALKING FORMS RECORDED 0` finishes typing on the same beat. |
| Scene 3, before "Nothing here is warm." | 2.5 s | Turn of the episode. Everything before it is about how cheap flight is. |
| Scene 4, before "It has never been confirmed." | 2.0 s | Separates the published hypothesis from the record's own material. |
| Scene 5, before "No animal has been recorded…" | 2.5 s | Flattest line in the record. Silence on both sides or it reads as a punchline. |
| Scene 5 → 6 cut | 3.0 s | Into shot 6.1, which is silent for its full 10 s. |
| Scene 6, before "Divided by the flyer…" | — | Falls after the silent 6.5; the spread places it on 6.6. |
| Scene 6 → 7 cut | hard | The coda arrives with no voice. Room tone continues. |

Every one of these falls on a paragraph boundary.

## Voice direction

Narrator. Unhurried, third person, present tense.

- Scenes 1 and 2 are good news and are read exactly like scenes 5 and 6, which
  are not. If the delivery warms up early or cools down late, the record is
  broken.
- "Nothing here is warm. Nothing here can be." — two flat statements. No weight
  on the second.
- "No animal has been recorded leaving the ground after that" is the flattest
  line in the episode. Read it like an inventory count, which is what it is.
- Chemical names are read plainly and at the same speed as everything else.
- No rising inflection on one point eight gigawatts. The narrator does not know
  that figure is small.
- There is no closing thought and the narrator never addresses the viewer.

## Sound design

- Room tone under the entire record: a low, dense, slightly pressurised wind —
  thicker and duller than Earth wind, with no whistle and no tonal content.
  Never absolute silence. This is the floor and it is never gated.
- **Recurring element — a distant wingbeat.** A soft irregular double-beat, far
  off, low in the mix, carrying well in the dense air.
  - **Established** in scene 2 under the dune shots, faint and never located.
  - **Present** through scenes 3 and 4.
  - **Removed** at the first frame of scene 5 and absent for the entire scene.
    Nothing replaces it; the wind thins.
  - **Returned** in the first second of shot 6.1, close for the first time — one
    double-beat, off screen, before the flyer enters. On screen it glides and
    makes no sound. Then absent for the rest of the record.
- Shot 6.1 has room tone and that one wingbeat only. No stinger, no swell.
- Scene 7 is room tone alone, plus the card clicks.
- Video is generated with audio off throughout. Nothing above is prompted.

## Verticals — three cuts, assembled

Assembled from `takes/`, never carved; every shot is one where something
moves. No cards, no click bed, no music. Every figure is spoken aloud. All
three close on `WATCH THE FULL RECORD ON THE CHANNEL`.

**V .a — A human could fly here.** Lines s1p1, s1p2, s1p3.
- Opens on "Titan is the only moon in the solar system…". Voice at frame one.
- Ends on **"twenty-four."** Paragraph end and scene end.
- Picture: 1.1, 1.3, 1.4, 2.4.
- Spoken figures: 4.4× density, one seventh gravity, 4.2 m/s, 24 m/s.

**V .b — Four tenths of a kelvin.** Lines s3p1, s3p2, s3p3.
- Opens on "Lift is free. Heat is not."
- Ends on **"around it."** Paragraph end.
- Picture: 3.1, 2.2, 3.2, 3.4.
- Spoken figures: 94 K, 25 W/m²K, 2.6 W, 0.4 K, 40 K. The sparrow is the cut.

**V .c — The margin.** Lines s5p1, s5p2, s5p3.
- Opens on "Reaction rates depend on temperature…".
- Ends on **"quarter."** Paragraph end — the consequence is withheld.
- Picture: 5.1, 5.3, 4.4, 6.5.
- **Do not extend** into the ninety-minute line; it answers the question the
  cut is asking.

## The teaser

Thirty seconds, vertical, out before the record, closing on `SOON`. Every shot
a take that moves; every line already in the record. 6.1 is kept out of it —
the only resolved appearance of the animal belongs to the record.

- Lines, in order: s1p2 (the human flies at 4.2 m/s), s2p3 ("Legs are a
  solution to a problem that does not exist here."), s3p1 trimmed after "Heat
  is not.", s3p4 trimmed after "Nothing here can be.", s5p5 ("No animal has
  been recorded leaving the ground after that.").
- Picture: 1.3, 2.2, 3.1, 3.2, 3.4, 4.4, 5.3.
- Music from ElevenLabs' music endpoint, never licensed, teaser only.

---

## Appendix — what is real and what is invented

### Real, verifiable

- **Titan's surface conditions.** Surface pressure about 1.5 bar; surface
  temperature about 94 K; surface gravity 1.352 m/s², which is 0.138 of Earth's
  9.807 — one seventh. Atmosphere approximately 94.2% N₂, 5.65% CH₄, 0.099% H₂.
  Titan is the only moon in the solar system with a substantial atmosphere.
- **Atmospheric density, about 5.4 kg/m³.** Mean molar mass 27.3 g/mol. Ideal
  gas at 1.5 bar and 94 K gives ρ = PM/RT = 150000 × 0.0273 / (8.314 × 94) =
  5.24 kg/m³; non-ideality at these conditions lifts it to about 5.3–5.4, the
  figure usually quoted. Earth sea level is 1.225 kg/m³: ratio 4.4.
- **The human-flight figure.** v = √(2W / ρSC_L). A 70 kg human with S = 2 m²
  and C_L = 1.0: W = 70 × 1.352 = 94.6 N, v = √(189.3 / 10.8) = 4.19 m/s. On
  Earth: W = 686.5 N, v = √(1373 / 2.45) = 23.7 m/s. The 5.67× ratio is
  √(7.25 × 4.41).
- **The acetylene–hydrogen metabolism is a published hypothesis, not a
  finding.** McKay and Smith (Icarus, 2005) proposed methanogenic life on Titan
  consuming atmospheric hydrogen with acetylene, ethane or organic solids, at
  energy yields of 334, 57 and 54 kJ/mol. For C₂H₂ + 3H₂ → 2CH₄ that is 334 kJ
  per mole of acetylene, or 111 kJ per mole of H₂. Never confirmed.
- **The hydrogen flux.** Darrell Strobel, from Cassini CIRS and INMS data,
  reported molecular hydrogen flowing downward through Titan's atmosphere and
  disappearing at the surface at roughly 10²⁸ molecules per second. Contested
  as a biosignature and the record says so aloud: non-biological routes,
  including mineral catalysis, have been proposed. The flux is the published
  measurement; the interpretation is not settled.
- **Titan's size.** Mean radius 2,574.7 km, surface area 4πr² = 8.33 × 10⁷ km².
  Diameter 5,150 km against Mercury's 4,880 km.
- **A sparrow runs about forty kelvin above the air** in air near freezing: body
  temperature around 41 °C against about 0 °C.
- **Hoover Dam nameplate capacity: 2.08 GW.** Closing card only.

### Invented

- The animal: 4 kg, wing area 0.8 m², C_L 1.2, lift-to-drag 12, thermally active
  surface 0.25 m², muscle efficiency 20%.
- Its activation energy of 50 kJ/mol, which sets the 24%.
- The cooling time: a natural-convection coefficient of 6 W/m²K and a specific
  heat of 2,000 J/(kg·K) for a body largely made of liquid hydrocarbon.
- That no walking forms exist, that no relaunch has been observed, and every
  population figure derived from those.

### Internal consistency

- **Flight power follows from the animal.** W = 4 × 1.352 = 5.41 N. v =
  √(2 × 5.41 / (5.4 × 0.8 × 1.2)) = 1.44 m/s. Sink = v / (L/D) = 0.120 m/s. P =
  W × sink = 0.65 W. On Earth: W = 39.2 N, v = 8.17 m/s, P = 26.7 W. Ratio 41 =
  7.25 × 5.67.
- **Heat follows from flight.** Re = ρvD/μ with D = 0.15 m and μ ≈ 6.5 × 10⁻⁶
  Pa·s gives 1.8 × 10⁵. Hilpert, Nu = 0.0266 Re^0.805 Pr^1/3 with Pr ≈ 0.75,
  gives Nu ≈ 411 and h ≈ 25 W/m²K on k ≈ 0.0091 W/(m·K). Metabolic input at 20%
  efficiency is 0.65 / 0.2 = 3.25 W, of which 2.60 W is waste heat.
  ΔT = 2.60 / (25 × 0.25) = **0.42 K**, spoken as "four tenths".
- **The 24% is Arrhenius.** d(ln k)/dT = Ea/RT² = 50000 / (8.314 × 94²) = 0.681
  per kelvin. Over the card's 0.4 K, e^(−0.272) = 0.76: a 24% loss. Over the
  exact 0.42 K it is 25%. "About a quarter" either way.
- **Cooling.** τ = mc / hA = 4 × 2000 / (6 × 0.25) = 5333 s = 89 min: the body
  loses 63% of its excess in that time — "most of that", not all.
- **The global budget follows from the flux.** 10²⁸ / 6.022 × 10²³ = 16,600 mol
  H₂ per second × 111.3 kJ/mol = 1.85 × 10⁹ W, "one point eight gigawatts".
  Divided by 3.25 W per animal = 5.7 × 10⁸ animals. Over 8.33 × 10¹³ m² that is
  one per 1.46 × 10⁵ m², one per seventh of a square kilometre.
- **2.6 W appears twice and must stay the same in both places** — it sets the
  0.42 K in scene 3 and it is the residue of the 3.25 W that sets the population
  in scene 6. Changing the efficiency assumption moves both.
