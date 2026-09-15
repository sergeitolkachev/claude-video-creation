# FILE CLASS NINE — Record No. 3
## "CARBON BALANCE"

**Slug:** `FC9-003 // CARBON BALANCE`
**Runtime:** 3:40 (220 s) — 27 shots plus the closing card block, durations
sum to 220 s exactly (22/28/40/25/32/30/43 per scene)
**Format:** 16:9 horizontal, three vertical cuts carved from it
**Voice:** the **character** voice (`config/voice.yaml`, `character`), not the
channel narrator. This record is told by its own operator. Dry, procedural,
first person — a man reading his own arithmetic back to himself. No
performance, no fear in the voice. The fear is in the numbers.
**Camera rule:** no faces, no hands, no people in any frame, ever.
**Word count:** 260. At the measured 162 wpm that is 96.3 s of speech. The
narrated body — scenes 1 to 6, 177 s — is **47% silent**, inside the 33–55%
band, and so is every scene in it individually. Scene 7 is a declared coda and
is exempt by name in `shots.yaml`. Per-scene table under Pacing.
**Motion split:** 7 static / 8 local / 12 model, plus 4 closing cards.

**Why 3:40 and not 4:20.** The submitted draft timed the picture at 4:20 for
the same 260 words — 60% silence, half a minute of it on frozen frames. Under
the Motion Policy every one of those silent seconds has to be a paid clip, so
the length was buying dead air at the most expensive rate available. Forty
seconds of picture came out of the body; not one line of narration was cut.
What survived is denser and, at 12 Kling shots, moves more than the longer
version would have. Eight seconds went back in at the other end, on the
closing block, which gained the channel closer record 02 established.

---

## Disclaimer (first line of the description)

    Work of fiction. All records, objects and events are invented. Any
    resemblance to real missions is coincidental. The physics is real and the
    arithmetic can be checked — both are listed at the end of this file.

---

## Synopsis

The sole operator of a relay station finds his carbon dioxide scrubber
cartridges are being consumed faster than specification. He treats it as a
manufacturing defect, then as a sensor fault, then measures it properly: with
the scrubber switched off overnight, the rise in partial pressure implies 1.39
kg of CO2 per day. He produces 0.98. He seals the bulkheads and measures each
section separately. The excess is coming from the cargo bay, which was sealed
at departure and is empty by manifest. Back-calculating from the cartridge
log, the figure is not constant. It is growing.

---

## Style spine

Material, light and palette only. **No camera words, no distance, no lens, no
framing.** Those belong to each shot. Copied into `shots.yaml` as an anchor
under every generation call.

> Interior of an orbital relay station. Painted metal surfaces in pale
> grey-green, worn through to bare aluminium on every edge that gets touched.
> Exposed fasteners, ribbed panel joints, insulated cable runs and conduit
> clipped along every surface. The light is weak and even, from recessed
> fluorescent panels behind yellowed plastic diffusers, pale green-white.
> Shadows are soft and dirty rather than black. The palette is grey-green,
> aluminium and dust, and nothing else. The only warm light anywhere on the
> station is a single portable work lamp with an amber bulb, and it appears
> only in the shots that name it. Fine dust hangs in the air. Nothing is new
> and nothing is broken.

**One palette.** The draft carried "cold blue-grey" in scene 2, "dim amber" in
scene 2, "dim warm light" in scene 4 and "pale green" in scene 1 — four
different stations. Warm light exists here in exactly one form, the work lamp,
and only where a shot asks for it by name.

### Anchors — five, one per camera distance

Every shot names the one it references. An anchor locks composition as hard as
it locks palette: handing the wide interior to a macro shot returns a wide
interior.

| id | distance | what it defines |
|---|---|---|
| `A1-module-wide` | wide interior | the command module: cramped, instrument glow, cable runs on the ceiling |
| `A2-corridor-deep` | long, deep perspective | a corridor running away from camera, ventilation grilles, panel lights |
| `A3-instrument-macro` | macro | an instrument face: brushed bezel, scratched glass, a needle, a toggle |
| `A4-surface-topdown` | top-down, close | a work surface: steel bench, floor grating, paper, the amber lamp |
| `A5-hatch-frontal` | mid, head-on | a heavy internal hatch: latches, locking wheel, worn paint |

All five are interiors, so the reference-driven still tier works normally —
this record has no exteriors and none of record 01's exterior problem. The one
shot looking out (7.2) is an interior shot of a window.

---

## Prompt hygiene

Rules applied to every prompt below. They are the script's job, not the
generator's.

- **No readable text in any frame.** Three shots have written paper as their
  subject (2.3, 5.1, 6.1). None of them says "logbook", "manifest" or
  "figures" in its prompt — each is framed as pure texture: ruled lines, ink
  strokes, the edge of a metal clip, the sheet cropped so no whole line of
  writing is in frame. The actual numbers arrive afterwards as a card, in
  Menlo. This converts the three shots most likely to come back with garbage
  lettering into the three best card plates in the record.
- **No faces, no hands, no people.** Not in any prompt, including the ones
  about a man alone.
- **No grain, no vignette, no scan lines, no tape artefacts, no "found
  footage", no "VHS", no chromatic aberration.** All applied in ffmpeg.
- **Never "shot on 35mm"** — it makes the still model return nothing at all.
- **Scanlines are never prompted.** A scanline is degradation and degradation
  is an ffmpeg pass — the validator rejects the word outright. The two monitor
  shots ask for the phosphor bloom, which is light, and the line structure of
  the tube is added in the grade with everything else.
- **No stencilled markings, no serials, no painted labels** anywhere, even
  qualified as blurred or unreadable. The draft's 4.4 asked for stencilled
  markings "out of focus and unreadable"; the enhancer reads that as
  permission to letter the hatch.
- Phosphor-green CRT appears in **2 shots only**, 3.3 and 5.2. Everywhere
  else the readouts are needles, lamps and segment displays, so the green
  belongs to those two frames and to the channel's own cards.
- No shot exceeds 10 s. Every `model` shot is exactly 5 s or 10 s, which is
  what the workhorse video model bills.

---

## SCENE 1 — COLD OPEN (0:00–0:22) · 22 s

Image first. No logo, no ident, no title sequence. The first sound is the
scrubber fan. The slug types itself into the lower left over shot 1.1 and is
gone before the cut — it is furniture, not an opening.

**Shot 1.1** — model, 5 s, anchor A3
> Close view of a ventilation intake mesh on a painted metal panel, a slow
> fan blade turning behind the mesh, fine dust drawn against the wires and
> lifting away again, weak even light from above, shallow focus, dark
> surround

**Card** `log-112` on shot 1.2, lower left:
```
LOG 112 / PERIGON-4
CO2: 3.1 mmHg — NOMINAL
```

**Shot 1.2** — static, 8 s, anchor A1 · card plate
> Row of four cylindrical scrubber cartridges seated in a metal rack on a
> bulkhead, one slot empty and unlit, small indicator lamps beside each
> cartridge, pale green panel light from a diffuser above, the lower left
> quarter of the frame empty painted bulkhead with nothing on it, static
> shot, no people

**Shot 1.3** — local, 9 s, anchor A4
> Spent cylindrical filter cartridge lying on a steel workbench beside an
> open disposal bin, scuffed casing, one portable work lamp with an amber
> bulb throwing a hard pool of light across the steel, top-down view, clean
> industrial surface, no people

*(drift: slow push, 1.000 -> 1.008, built in ffmpeg)*

**Narration:**
> Log one twelve. Shift complete. Nothing to report.
>
> Cartridge four is spent. Fifteen hours early.
>
> I logged it as a manufacturing defect. That is what the form has a box for.

---

## SCENE 2 — SECOND DEFECT (0:22–0:50) · 28 s

*Shot order changed after the first master: the card naming log 114 sat on
the third shot and typed fourteen seconds after the voice said the number.
The paper plate and the grille swapped places and the corridor gave five of
its ten seconds to the rack. The Kling take for 2.1 is ten seconds and is cut
to five — paid for, not wasted, and nothing else in the scene moved.*

**Shot 2.1** — model, 5 s, anchor A2
> Narrow station corridor during night cycle, ventilation grilles along one
> wall, one panel light at the far end failing and steadying again, faint
> movement of dust in the air along the length of the passage, long
> perspective, cool grey-green palette, no people

**Card** `log-114` on shot 2.2, lower left:
```
LOG 114 / CARTRIDGE LIFE: 46 H
SPEC: 62 H
```

**Shot 2.2** — static, 8 s, anchor A4 · card plate
> Macro top-down view of a sheet of pale ruled paper on a steel desk, only
> the ruled horizontal lines and the edge of a metal clip in frame, the sheet
> cropped by the frame on all four sides, hard angled light from a single
> amber work lamp, shallow focus, the lower left of the frame falling into
> shadow, no hands

*(texture only — the figures arrive as a card)*

**Shot 2.3** — local, 5 s, anchor A3
> Ventilation intake grille with dust drawn against the mesh in a faint
> radial pattern, close framing, low angle light raking across the metal,
> shallow focus

*(drift: lateral, right, built in ffmpeg)*

**Shot 2.4** — local, 10 s, anchor A1
> Rack of scrubber cartridges seen from below, two slots empty, indicator
> lamps unlit, tight framing on the underside of the rack, weak green-white
> panel light

*(drift: slow push, 1.000 -> 1.006)*

**Narration:**
> Log one fourteen. Cartridge five. Forty-six hours.
>
> Specification is sixty-two. One person, one kilogram of carbon dioxide a
> day, two point six kilograms of capacity per cartridge. The arithmetic is
> not difficult.
>
> Two defects in a row is not a defect.

---

## SCENE 3 — THE MEASUREMENT (0:50–1:30) · 40 s

The scene that earns the record. **The scrubber fan is absent for the whole of
it** — it is switched off in-fiction, so the room genuinely sounds different.
The data card is the subject here, not decoration.

**Shot 3.1** — local, 5 s, anchor A3
> Control panel with a single toggle switch under a hinged metal guard
> cover, the cover raised, the indicator ring around the switch unlit, the
> painted panel filling the frame behind it, extreme shallow focus, no hands

*(drift: very slow push, 1.000 -> 1.010)*

**Shot 3.2** — model, 10 s, anchor A1
> Dark station interior during night cycle, the only light the glow of one
> instrument panel low in frame, fine dust drifting slowly through the light,
> wide shot, no people

**Shot 3.3** — model, 5 s, anchor A3 · **no card**
> Small monochrome monitor in a metal surround showing a single shallow line
> climbing slowly to the right across a plain grid, coarse phosphor green
> glow blooming off the tube, dark room, the screen filling most of the frame

*No card on this shot or on 5.2. The channel's cards are phosphor green; over
a screen that is already phosphor green in-fiction the card stops reading as
the record's own layer and becomes set dressing. Those two shots carry their
numbers in the frame.*

**Shot 3.4** — model, 5 s, anchor A1
> Empty sleeping bunk strapped to a bulkhead, restraint straps hanging slack
> and stirring very slightly in the still air, one dim wall lamp, no people

**Card** `measurement` on shot 3.5, lower left, both lines held on screen
through the delivery of the measured figure:
```
LOG 117 / SCRUBBER OFFLINE — 6 H
V 84 m3     T 295 K
PREDICTED  0.21 mmHg/h  = 1.00 kg/day
MEASURED   0.29 mmHg/h  = 1.39 kg/day
```

**Shot 3.5** — static, 11 s, anchor A3 · card plate
> Analog gas sensor gauge on a bulkhead, fine needle resting just above the
> lower mark, a scale of evenly spaced tick marks running round the dial and
> the marks the only thing on the face, brushed metal bezel, scratched glass
> cover, dim cold light, the lower left of the frame empty painted metal,
> macro lens

**Shot 3.6** — local, 4 s, anchor A1
> Wide view of a cramped command module interior at night, instrument glow
> only, cables secured in runs along the ceiling, the seat in front of them
> empty, no people

*(drift: slow push, 1.000 -> 1.008)*

**Narration:**
> I ran the scrubber off for six hours tonight. Sensor logging every minute.
>
> At this volume, one kilogram a day should raise partial pressure by zero
> point two one millimetres of mercury per hour.
>
> I measured zero point two nine.
>
> That is one point three nine kilograms a day. I weigh eighty-one. I am not
> producing one point three nine.

---

## SCENE 4 — SECTIONING (1:30–1:55) · 25 s

**Two cards, not one.** `sections` types across shot 4.2 as each row is
spoken; `sections-d` is a separate card on shot 4.4, after the 2.5 s gap. Four
rows filling in on one plate read as a table completing itself; split across
two plates they read as a search with an answer at the end, and the answer
gets its own frame, on the door it is behind.

Card `sections`, on 4.2, lower left:
```
LOG 118 / BULKHEADS SEALED
A COMMAND   22 m3   0.98 kg/day
B GALLEY    18 m3   0.00
C CORRIDOR  14 m3   0.00
```

Card `sections-d`, on 4.4, lower left:
```
D CARGO     30 m3   0.43 kg/day
```

**Shot 4.1** — model, 5 s, anchor A5
> Heavy internal bulkhead hatch swinging slowly closed across a station
> corridor, locking wheel centred on the hatch, worn paint, cold overhead
> light, no people

**Shot 4.2** — static, 10 s, anchor A4 · card plate
> Portable handheld gas sensor standing on a steel floor grating, its dark
> case scuffed pale along every edge and corner from being carried, fine
> grey dust worked into its seams and into the grating under it, a single
> recessed round vent and a folded carrying handle, nothing lit on it, low
> angle, tight framing, shallow focus, the lower left of the frame empty
> grating in shadow, no hands

**Shot 4.3** — model, 5 s, anchor A1
> Empty galley module, sealed food containers strapped to a shelf, a single
> metal utensil drifting slowly at the end of a slack tether, still air, weak
> green-white panel light, no people

**Shot 4.4** — static, 5 s, anchor A5 · card plate
> Sealed cargo bay hatch seen head-on, heavy latches closed across it, the
> paint worn through to bare metal in a ring around each latch, cold light
> from one side only, the lower left of the frame empty bulkhead,
> no people

**Narration:**
> Four sections. Four bulkheads. I have a portable sensor and eight hours.
>
> Command, with me inside: zero point nine eight. That is me.
>
> Galley: zero. Corridor: zero.
>
> *[2.5 s]* Cargo: zero point four three.

---

## SCENE 5 — THE BACK-CALCULATION (1:55–2:27) · 32 s

**Card** `recalc` on shot 5.1, lower left:
```
LOG 119 / RECALCULATED FROM CARTRIDGE RECORD
SECTION D
D-11    0.28 kg/day
D-00    0.43 kg/day
```

**Shot 5.1** — static, 12 s, anchor A4 · card plate
> Macro top-down view of pale ruled paper on a steel desk under a single
> amber work lamp, dense dark ink strokes filling the ruled lines, the sheet
> cropped by the frame so no complete line is in view, one stroke of the ink
> pressed twice as hard as the rest, hard angled light, deep shadow across
> the lower left of the frame, no hands

*(texture only — the figures arrive as a card)*

**Shot 5.2** — model, 5 s, anchor A3 · **no card**
> Small monochrome monitor showing a shallow upward curve resolving point by
> point across a plain grid, coarse phosphor green glow blooming off the
> tube, dark room, the screen filling the frame

**Shot 5.3** — model, 10 s, anchor A1
> Communications console with an unlit incoming-signal indicator, a receiver
> seated in its cradle, a layer of settled dust on the panel surface, fine
> dust moving slowly in the light of the panel, dim room, no people

**Shot 5.4** — model, 5 s, anchor A2
> Sealed cargo hatch at the far end of a dark corridor, a single portable
> work lamp with an amber bulb aimed at it from the near side, a long shadow
> thrown across the floor toward camera, dust drifting through the lamp beam,
> no people

**Narration:**
> I went back through the cartridge log and solved for it. Eleven days before
> that measurement it was zero point two eight. It is not constant. It is
> increasing.
>
> Zero point four three kilograms a day is about forty-three watts.
>
> Control has not answered in nine days.

---

## SCENE 6 — THE SEAL (2:27–2:57) · 30 s

**Card** `manifest` on shot 6.1, lower left:
```
LOG 120 / SECTION D
MANIFEST: EMPTY
SEALED AT DEPARTURE — SEAL INTACT
```

**Shot 6.1** — static, 10 s, anchor A4 · card plate
> Macro view of a printed sheet clipped to a metal board, ruled rows running
> across the frame with nothing entered in them, the sheet cropped by the
> frame on every side, the sprung clip of the board at the top edge, hard
> side lighting, the lower left of the frame in deep shadow, no hands

*(texture only — the rows are empty, which is the whole point)*

**Shot 6.2** — local, 5 s, anchor A3
> Seal indicator on a hatch photographed from a hard angle, a thin twisted
> locking wire in place through the fitting, deep shadow, scratched metal,
> macro lens, cold light

*(drift: slow push, 1.000 -> 1.010)*

**Shot 6.3** — model, 10 s, anchor A5
> Dark cargo bay hatch with the work lamp switched off, the only light a
> faint spill of corridor light along the lower edge of the hatch, fine dust
> moving slowly through that spill, deep shadow filling the rest of the
> frame, no people

*Ten seconds, no voice, no card. The centre of the record, and the reason it
is a `model` shot: this is exactly the hold that a frozen frame turns into a
pause in the player.*

**Shot 6.4** — local, 5 s, anchor A1
> Empty seat in the command module, restraint straps hanging
> loose over the arms, instrument glow falling across the headrest, no people

*(drift: very slow push, 1.000 -> 1.006)*

**Narration:**
> Cargo manifest, section D: empty. Sealed at departure. Seal intact — I
> checked the indicator myself. Twice.
>
> There is no leak path into D. If something were dead in there, it would not
> be growing.
>
> *[2.0 s]* I am not going to open it.

---

## SCENE 7 — CLOSE (2:57–3:40) · 43 s

The scrubber fan returns on the cut into this scene. It is the only comfort in
the record, and the cards take it back.

**Shot 7.1** — local, 6 s, anchor A1
> Life support rack with a fresh cylindrical cartridge seated in the slot
> that was empty, its indicator lamp lit green, tight framing, weak
> green-white panel light, no people

*(drift: slow push, 1.000 -> 1.006)*

**Shot 7.2** — model, 10 s, anchor A1
> A circular porthole filling most of the frame in a painted metal bulkhead,
> a heavy ring of bolts around the glass, a field of stars in the black
> beyond it and nothing else out there, a cold reflection of the room across
> the inner edge of the glass, no people

**Narration:**
> Log one twenty-one. Shift complete. Nothing to report.

Then the audio drops to room tone only. **The fan cuts on the first card.**

**Closing cards** — phosphor green Menlo, per `config/type.yaml`, on black.
Typed on one character at a time with the click, same as every other card on
the channel. **Not white.**

| # | id | text | at | seconds |
|---|---|---|---:|---:|
| 1 | `close-1` | `DOUBLING TIME: 17.8 DAYS` | 193 | 4 |
| 2 | `close-2` | `SECTION D OUTPUT REACHES 1.00 kg/day IN 22 DAYS` | 197 | 5 |
| 3 | `close-3` | `SCRUBBER CAPACITY IS EXCEEDED THE SAME DAY` | 202 | 5 |
| 4 | `close-4` | `LOGS 122-129 ARE NOT AVAILABLE IN THE PUBLIC RECORD` | 207 | 5 |
| 5 | `close-5` | the channel closer — `FILE CLASS NINE`, the slug, the disclaimer | 212 | 8 |

*The draft had five record cards. `THE RECORD CONTINUES TO LOG 129` was cut:
the card after it says the same thing and says it better by implication. The
fifth card here is `close-5`, the channel closer — same shape as record 02's,
centred rather than lower left because there is no plate under it. It is
furniture and it is not an episode decision, which is why the record got
eight seconds longer rather than going without it.*

All five carry the click track. The fan is what cuts, not the typing.

---

## Pacing (assembly)

Base: **1.2 s is the minimum gap between paragraphs, not the interval.**
`build_audio.py` spreads each scene's paragraphs across the scene rather than
running them off the top, so the real gaps are whatever the scene's silence
divides into — 3.4 to 5.7 s in most scenes here, 1.4 s in scene 4, which is
the densest. Front-loading would leave one long dead stretch at the end of
every scene; spreading turns it into even, deliberate silences that track the
images.

The holds below are added on top of that, and they are the only places where a
specific number is being asked for:

| where | gap | why |
|---|---|---|
| before "I measured zero point two nine." | 2.5 s | the hum has already dropped — the room itself is the pause |
| before "Cargo: zero point four three." | 2.5 s | three zeroes have just been read at the same pace; the gap is the only thing marking the fourth |
| before "I am not going to open it." | 2.0 s | the one decision in the record |

Speed on the voice stays pinned at the synthesis-quality default and is never
adjusted. Pacing is bought entirely with inserted silence.

### Silence budget

Checked against the 33–55% band. Scene 7 is a declared coda: 10 s of it is the
silent porthole hold and 19 s is the closing card block, both of which are
`model` or text-bearing by design.

| scene | seconds | words | speech | silence |
|---|---:|---:|---:|---:|
| 1 | 22 | 31 | 11.5 s | 47.8% |
| 2 | 28 | 41 | 15.2 s | 45.8% |
| 3 | 40 | 60 | 22.2 s | 44.4% |
| 4 | 25 | 32 | 11.9 s | 52.6% |
| 5 | 32 | 47 | 17.4 s | 45.6% |
| 6 | 30 | 41 | 15.2 s | 49.4% |
| 7 | 43 | 8 | 3.0 s | coda |
| **body, 1–6** | **177** | **252** | **93.3 s** | **47.3%** |
| **total** | **220** | **260** | **96.3 s** | — |

162 wpm is a planning figure. If the recorded takes come in slow and a scene
drops under the floor, the picture is lengthened — never the delivery hurried
and never a line cut.

---

## Voice direction

- First person, present tense, procedural. He is filling in a form, not
  telling a story.
- Never describe what the viewer can already see.
- **Never explain the implication.** The closest he comes is "I am not going
  to open it," and even there the reason goes unsaid.
- No rising inflection on the numbers. A figure is read exactly the way
  "shift complete" is read.
- The only line with any weight is **"I weigh eighty-one."** Keep it flat. The
  flatness is the weight.
- "Nothing to report" opens the record and closes it, identically. It must be
  delivered the same way both times — same seed family, checked side by side
  before either take is approved.

---

## Sound design

One element, built deliberately: **the scrubber fan cycle.**

| where | fan |
|---|---|
| scene 1 | established — it is the first sound in the record, before any voice |
| scenes 1–2 | present, steady, under everything |
| **scene 3** | **absent for the whole scene.** It is switched off in-fiction |
| scenes 4–6 | present again |
| scene 7 | returns on the cut, warm and steady |
| closing cards | **cuts.** Room tone only, then the clicks |

Most viewers will not consciously notice it and will feel all three moments.

Room tone runs under the entire record, including the cards. Absolute digital
silence destroys the illusion of a recording.

---

## Verticals — three candidate moments

Each cut from `EPISODE-clean.mp4` (same grade, same grain, no cards, no click
track). Captions burned in from the real word timings. Bottom 30% of the frame
stays clear.

Every figure in all three is **spoken aloud**, so nothing is lost when the data
cards are dropped for the vertical crop.

| id | source | ends on |
|---|---|---|
| `FC9-003.b` | scene 3, from "I ran the scrubber off" | hard cut immediately after "I am not producing one point three nine" |
| `FC9-003.c` | scene 4, from "Four sections. Four bulkheads." | hard cut on "Cargo: zero point four three" — before the gap resolves |
| `FC9-003.d` | scene 6, from "Cargo manifest, section D: empty." | hard cut mid-word in "I am not going to —" |

Centre-safe crop. 4.2 and 6.1 are macro plates and crop cleanly; 3.2 and 6.3
are wide and lose their edges, so `.b` and `.d` favour the closer shots in
their range.

---

## Appendix — what is real and what is invented

### Real, verifiable

- **Lithium hydroxide absorption:** 2 LiOH + CO2 -> Li2CO3 + H2O. 47.9 g LiOH
  per 44.0 g CO2, so roughly 0.92 kg CO2 per kg LiOH theoretical; real
  hardware runs lower.
- **Human output:** on the order of 1.0 kg CO2 per crew-day, the standard
  figure used in life support sizing. The operator measures his own at 0.98.
- **Ideal gas relation:** dP = mRT/(MV). One kilogram of CO2 in 84 m3 at 295 K
  gives 663.6 Pa = 4.977 mmHg, i.e. **0.2074 mmHg/h** spread over a day. The
  measured 0.29 mmHg/h divides out to **1.398 kg/day**. Both figures in the
  narration are correct to the digits spoken.
- **CO2 partial pressure references:** sea-level air about 0.3 mmHg; ISS
  operational range roughly 2–4 mmHg (the opening card's 3.1 is mid-range and
  genuinely nominal); 7.6 mmHg is 1% of a 760 mmHg atmosphere.
- **Metabolic conversion:** about 1 kg CO2/day corresponds to roughly 100 W of
  resting metabolism, so 0.43 kg/day is about 43 W. An approximation, which is
  why the operator says "about".
- **Exponential fit:** 0.28 -> 0.43 over 11 days gives k = ln(0.43/0.28)/11 =
  **0.0390/day**, doubling time ln2/k = **17.77 days** (card: 17.8). From 0.43
  to 1.00 is ln(1.00/0.43)/k = **21.6 days** (card: 22).
- **The scrubber card:** rated 2.0 kg/day. Operator 0.98 plus section D at
  1.00 is 1.98, and D passes 1.02 — the point where the total reaches the
  rating — at 22.2 days. Both round to the same day, which is what card 3
  claims.

### Internal consistency of the cartridge log

The draft's cartridge lifetimes did not fit its own exponential. They do now.
Logs are one per day; log 118, the sectioning, is D-00.

| log | day | section D | total kg/day | cartridge life | narration |
|---|---|---:|---:|---:|---|
| 112 | D-6 | 0.340 | 1.324 | 47.1 h | "Fifteen hours early" (spec 62.4) |
| 114 | D-4 | 0.368 | 1.352 | 46.2 h | "Forty-six hours" |
| 117 | D-1 | 0.414 | 1.398 | — | measured 0.29 mmHg/h |
| 118 | D-00 | 0.430 | 1.410 | — | section table |
| 119 | D+1 | — | — | — | back-calculation |

Capacity 2.6 kg; spec life is 2.6 / 1.00 kg/day = 62.4 h, quoted as "sixty-two"
because a specification is written against the nominal crew figure, not against
this particular man.

### Invented

Pressurised volume 84 m3 and the four section volumes (22 / 18 / 14 / 30,
which sum to 84); cartridge capacity 2.6 kg CO2; scrubber rated 2.0 kg/day, a
two-crew design flying with one crew; operator mass 81 kg; the nine-day comms
silence; and every log number.

The station is **PERIGON-4**. The name is invented: a perigon is the angle of
one complete turn, which is what the station does once every ninety minutes
and what the star field is doing across the porthole in the closing shot.
Nothing has flown under that name. The draft's GORIZONT-4 was dropped because
Gorizont is a real Soviet communications satellite series, and the disclaimer
promises there is no real mission behind this record.
