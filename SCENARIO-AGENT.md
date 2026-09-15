# Scenario Agent Brief — File Class Nine (FC9)

This file is the complete contract for whoever writes a script for this
channel. It is written for an agent that has **no access to the repository**:
everything a script needs in order to be buildable is here, restated rather
than referenced.

A script that satisfies this file goes into production unchanged. A script
that does not is rewritten before a single image is generated, which is the
only expensive kind of mistake this document exists to prevent.

**Everything is written in English.** Scripts, narration, prompts, titles,
card text. Never write narration in another language and translate it — write
it in English from the start. Translated narration reads as translated.

---

## 1. The channel

Faux-archival records. Each episode is a recording that was never supposed to
survive: a ship's log, a field report, a survey, a day in 1178. Narration in
English over slow atmospheric shots. No dialogue, no recurring faces, no
presenter.

The effect is the gap between a calm procedural voice and what the numbers in
that voice actually mean. The narrator never closes that gap. The viewer does.

**Numbering** (the agent proposes these):

- Long records: `FC9-LOG-041 // The Aldren Basin Survey`
- Vertical cuts: `FC9-041.b // Fragment`

**Write the description with the script.** It goes in `publish.md`: the title,
the description, the chapter list, and a title and description for each
vertical. The disclaimer is its first line; the "what is real and what is
invented" appendix you already write for the script is what the description's
verifiable section is built from, so write that appendix knowing it will be
read by the audience and not only by the producer.

**Titles state what the narrator did, never ask a question.** "He switched off
the scrubber to find out" is this channel. "What was in section D?" is a
different one.

**First line of the description is always a disclaimer** naming the work as
fiction and, where the episode leans on real physics, saying which figures are
real. Write it into the script.

---

## 2. What to deliver

One Markdown file, `script.md`. Nothing else. It is the source of truth for
the words; the production side derives `shots.yaml`, `cards.yaml` and the
audio plan from it.

Required structure, in this order:

```
# FC9-0NN // "TITLE"

**Slug:** FC9-0NN // TITLE
**Runtime:** M:SS (NNN s) — N shots, durations sum to NNN s exactly
**Per-scene seconds:** {1: 34, 2: 42, ...}   (must sum to runtime)
**Format:** 16:9 horizontal, three vertical cuts carved from it
**Voice:** narrator | character (operator) — and the delivery note
**Word count:** NNN. At 162 wpm that is NNN s of speech against NNN s of
  runtime — NN% silence. Per-scene silence table below.
**Motion split:** N static / N local / N model

## Disclaimer
## Synopsis
## SCENE 1 — NAME (0:00–0:34)
   ... cards, shots, narration
## Pacing (assembly)
## Voice direction
## Sound design
## Verticals — three candidate moments
## Appendix — what is real and what is invented
```

Every scene contains: its data/title cards, its shots, its narration.

**Shot entry format.** Every shot, without exception:

```
**Shot 3.2** — model, 10 s, anchor A1
> <prompt, one continuous moment>
```

That is: id, **motion tier**, duration, anchor. A shot missing its tier is an
incomplete script.

---

## 3. Runtime — the rule that decides length

**Minimum 3 minutes, maximum 10. The script decides, not a target.**

An episode runs as long as it holds and not one shot longer. The question is
never "have we reached length" but "does this still grip". A record that stops
at 3:30 because it has said everything is finished. The same record padded to
8 minutes is a worse record and a more expensive one.

Two tests, both the script's job:

- **The first ten seconds.** Image first — no logo, no intro, no channel
  ident. If the opening shot and the opening line do not make a viewer want
  the second line, nothing later rescues it. Write the cold open first and cut
  it hardest.
- **No slack in the middle.** Every scene advances the arithmetic or turns it.
  A scene that restates the previous scene in new pictures gets cut, not
  shortened. That is the only length control this channel uses.

### Word count follows runtime

The narration voice is measured at **162 wpm**. Do not assume any other rate
and do not try to control pace with delivery — that is not available.

- **Floor: at least one third of the runtime is silence**, per scene and
  overall.
- **Ceiling: above roughly 55% silence the episode drags.** Records 01 and 02
  both landed near 40%, which is the shape that works.

| Runtime | Narration | = speech |
|---|---|---|
| 3:00 (180 s) | 220–325 words | 81–121 s |
| 4:30 (270 s) | 330–490 words | 122–181 s |
| 7:00 (420 s) | 510–760 words | 189–281 s |
| 10:00 (600 s) | 730–1085 words | 270–402 s |

Give the silence percentage **per scene** in the script, not just overall. A
scene at 12% silence is a scene that will have to be rebuilt after the voice
is recorded.

If a scene falls under the floor, lengthen the picture. If it runs over the
ceiling, cut lines. Never pad the voice, never hurry it.

### Timing arithmetic is checked, so make it check out

- Shot durations inside a scene **sum exactly** to that scene's seconds.
- Scene seconds **sum exactly** to the stated runtime.
- Closing text cards and title cards occupy real seconds — count them.

A mismatch means a missing shot or a wrong runtime. Resolve it in the script.
It is never resolved by stretching clips in post.

---

## 4. Motion tiers — every shot declares one

This is the rule most often got wrong, and it is the one that decides whether
the episode looks like a film or a slideshow.

**A frame is allowed to be still only when the viewer is reading or
listening.**

| Tier | What it is | When it is allowed |
|---|---|---|
| `static` | Locked-off frame, lens breathing only | **Only** for a shot carrying a data card, a title, or burned-in text. The eye is on the text; a moving frame fights the reading. |
| `local` | Slow drift or push across the approved still | Shots **under narration** where the frame is texture rather than event. No parallax, nothing in frame is alive. |
| `model` | A real video clip | **Required** for any shot running under silence, and for any shot whose content should physically move: dust, water, frost, smoke, a drifting object, an animal. |

**The rule that matters: no text on screen and no voice means the picture
carries the shot alone, and a still frame cannot.** Silence is a format choice
here, not dead air, and it only reads as intentional if something in the frame
is moving while nobody is talking.

Consequence for the writer: a long silent hold is a legitimate and powerful
choice, but it is a `model` shot, and it must contain something that moves.
"Static, 9 s, long hold, no narration" is not a shot — it is a freeze.

Give the **motion split** in the header (`N static / N local / N model`).
A healthy record looks roughly like 8 / 12 / 14.

Do not use the tier to save money. Locked-off shots are free and that is
exactly why they are seductive; an episode that comes in cheap because half of
it is frozen took the saving out of the episode.

---

## 5. On-screen text — channel furniture, never varied

Every character that appears on screen on this channel comes out of one
renderer in one font. This is identical in every record. It is not styled per
episode and it is not A/B tested.

- **Font: Menlo.** One computer font, everywhere. Never a second face.
- **Phosphor green, `RGB 150 255 190`, at 40 px on a 1080p frame.** With a
  halo (blurred black silhouette of the glyphs) and a glow (blurred copy of
  the text). Neither is a box or a scrim — the frame shows through everywhere
  the text is not.
- **Never white. Never off-white. Never smaller than 40 px.** Record 02
  shipped its first cards off-white at 26 px and they vanished into a pale
  landscape: pale text on pale ground has only luminance to separate it, and
  these worlds are all luminance. Green owns a channel the picture does not
  use. Do not write "white monospace" in a script. Ever.
- **Characters type on one at a time**, left to right, with a short dry click
  per glyph under the narration. A line resolves and then holds. Nothing
  fades, slides or bounces. Numbers that count tick per digit change.
- **A graphic says what it is measuring.** Every bar carries its own label
  inside it. An unlabelled rectangle reads as a progress bar for nothing.

**A card plate must be long enough for its card.** Text types on at 18
characters a second, with a 0.35 s pause between lines, and a card never
leaves the screen less than 2 s after its last character. So a four-line card
of 120 characters needs about 9 s of plate, and giving it an 8 s shot means it
is still typing when the shot cuts. Count the characters and give the shot the
seconds. Record 03's draft put its most important card — the one the whole
episode is built around — on an 8 s plate that needed 11.

**A coda is declared, not assumed.** A closing block of text cards, or a held
silent shot before them, is exempt from the 55% silence ceiling — but only if
the script says which scene is the coda and why. Everything else is measured.

Two things the writer decides:

- **Where a card sits.** Cards are composed for the **lower left** of the
  16:9 frame. The shot that carries a card must be framed with that corner
  empty. If the plate is busy where the card goes, the plate is wrong.
- **Which plate a card sits on.** A card has to reach the screen at the same
  moment as the line that names it. That is a scripting decision, not an
  assembly one: the card goes on the plate the narration is over, which in
  practice means an early shot in the scene. Record 03 put the card reading
  `LOG 114` on the third shot of its scene and the voice said "Log one
  fourteen" over the first — fourteen seconds apart in the finished master.
  Write the card next to its line in the script, and check that the shot
  carrying it starts near where that line falls.
- **Which shots get no card at all.** Never put a green card over a screen
  that is already green in-fiction — a phosphor CRT, a glowing readout. The
  card stops reading as the record's own layer and becomes set dressing. Put
  those numbers in the frame or in the voice, not on a card.

---

## 6. Writing the narration

The voice is a recording device, not a storyteller.

- Dry, procedural, first person. The narrator is doing a job and filling in a
  form.
- **Never describe what the viewer can already see on screen.**
- **Never explain the implication.** The gap between the calm voice and the
  image is the entire effect. The closest the narrator may come is a flat
  refusal — "I am not going to open it" — and even there the reason goes
  unsaid.
- Short declarative sentences. Timestamps, serial numbers, measurements.
- The narrator does not know they are in a story and does not know how it
  ends.
- No adjectives doing emotional work. Not "the terrifying silence"; "no
  response on the channel for six days".
- No rising inflection on the numbers. A number is read the same way as
  "shift complete". If one line carries weight, it carries it by being the
  flattest line in the episode.

Two voices exist: the channel **narrator** (unhurried, third person, present
tense) and a **character** voice for records told by their own operator. Pick
one per episode and say which in the header. They are never mixed.

---

## 7. Writing shot prompts

Prompts are read by an image model with a prompt enhancer that cannot be
switched off. Anything vague is filled in with whatever is statistically
typical: "dust particles floating" came back as heaps of grit on the floor,
"station corridor" became a concrete utility tunnel, "small circular porthole"
was read as small in the frame. **Be specific enough that there is nothing
left to invent.**

Hard rules:

- **One continuous moment per shot.** No cuts, no "then", no "and afterwards".
- Include: subject, light source, camera position, lens feel, motion.
- Motion stays minimal — slow drift, slow push, one element moving. Fast
  motion is where generated video falls apart.
- **No readable text anywhere in frame.** Models invent garbage lettering out
  of anything resembling a label. If the subject of a shot is a written page,
  a manifest, a logbook or a gauge with a scale, frame it as texture — macro
  on the ruled lines, the ink stroke, the clip of the board — and put the
  actual figures on afterwards as a card. This turns the channel's worst shots
  into its best card plates.
- **No faces in focus, no hands, no people.** Titles are added in post.
- **Never prompt degradation.** No grain, no vignette, no scan lines, no tape
  artefacts, no chromatic aberration, no "found footage", no "VHS". All of
  that is applied afterwards in ffmpeg; prompting it wastes generation
  quality. This holds even when the artefact is diegetic: a phosphor monitor
  in frame gets "coarse phosphor glow", which is light, and its scanlines are
  added in the grade like everything else.
- **"Blurred and unreadable" is not a defence.** A prompt asking for stencilled
  markings out of focus, or a page of writing too soft to read, is still a
  prompt asking for lettering, and the enhancer reads it as permission. Name
  what is actually in frame — worn paint, ruled lines, an ink stroke, a metal
  clip — and nothing else.
- **Never write "shot on 35mm".** It makes one of the models return nothing at
  all.
- Default shot length **6–10 seconds**. Nothing longer than 10 s exists.
- The workhorse video model bills **5 s or 10 s only**. A 7-second shot is
  paid for as 10. Prefer durations of 5 or 10 for `model` shots; anything in
  between is money thrown away.

### Anchors and the style spine

Before the shots, the script proposes:

- **A style spine** — one paragraph describing **material, light and palette
  only**. No camera words. Words like "low ceiling", "built for a single
  occupant", "rounded corners" read as framing instructions and drag every
  shot to a wide. Camera, distance and lens belong to each shot's own line.
- **Four to five anchors, one per camera distance that recurs.** An anchor
  locks composition as hard as it locks palette: a wide establishing anchor
  handed to a macro shot returns a wide establishing shot. Typical set: wide
  interior, corridor in deep perspective, macro instrument, top-down surface,
  object head-on. Every shot names which anchor it uses.
- **A spine names no objects.** Not even to restrict one. Writing "the only
  warm light is a work lamp, and it appears only where a shot names it" puts
  the lamp in every frame — the model reads the noun and drops the clause. Say
  what the material, the light and the palette are; put objects in the shots
  that want them, and have the spine forbid the rest by name.
- **A spine that opens "Interior of a …" is a framing instruction.** Room
  nouns — interior, station, corridor, wall, ceiling — build a room in every
  frame, including the macro ones. If the episode has distances where "room"
  is the wrong word, say so in the script and give those anchors their own
  spine with no room noun in it.
- **A negation only works when the subject does not imply it.** "No lettering"
  and "no people" hold reliably. "No lamp" does not, in a shot that asks for
  hard raking light — the model reads the noun and drops the clause. Forbid
  only what the frame has no reason to contain; for everything else, fill the
  frame positively with what IS there.
- **When you remove a detail, name what takes its place.** Stripping a lit
  display out of an instrument also stripped its wear, and the shot came back
  as a clean product render in a record where everything else is filthy. A
  description emptied of one property tends to come back emptied of all of
  them.
- **Interiors and exteriors do not share anchors.** An interior spine handed
  to a shot in open space does not transfer style, it puts a wall in the
  frame. If the episode has both, say so and keep the sets separate.
- **One palette for the episode.** Scattering "cold blue-grey", "dim amber"
  and "pale green" across scenes builds three different locations. Choose one
  palette; a warm light is allowed only as a named practical lamp inside the
  frame, never as the light of a scene.
- **When two shots are the same object seen twice, reference the first
  approved still, not the anchor** — say so in the script. An anchor makes
  them the same kind of thing; the still makes them the same thing, down to
  the scratch in the glass.

---

## 8. Arithmetic discipline

The genre lives on numbers that check out. A viewer with a calculator is the
target audience, not a hazard.

- **Every figure in the narration must be internally consistent with every
  other figure**, across scenes, including figures that are only implied.
- Check the implied ones especially. Record 03's draft had a cartridge
  lifetime that was arithmetically correct in isolation but implied a
  consumption rate belonging to a day five days later in the episode's own
  timeline. Nothing in the script said so; the exponential it had established
  three scenes later did.
- Where a real physical relation is used, use it correctly and say so.
- **The Appendix is mandatory**, in two lists: *Real, verifiable* (with the
  relation, the constants and the arithmetic, so it can be checked) and
  *Invented* (every made-up parameter, named). If a figure is an
  approximation, the narrator says "about".

---

## 9. Pacing and sound

- Pace is bought with **silence between paragraphs**, never with delivery
  speed. The speed parameter on this voice is not a control: its response is
  not monotonic and per-request noise swamps it. It is pinned and never
  touched.
- Default gaps: **1.2 s between paragraphs, 2.0 s across a scene cut.** Longer
  gaps are allowed where the script asks for them **by name**, with a reason.
  List them in a Pacing section.
- If a line reads hurried after the gaps are in, **edit the sentence** —
  shorter clauses, a period where a comma was.
- **Room tone runs under the entire episode.** Absolute digital silence
  destroys the illusion of a recording.
- A recurring sound element that changes across the episode is welcome and
  cheap — establish it, remove it, bring it back. Say where in a Sound design
  section. Most viewers will not consciously notice and will feel all three
  moments.
- Video models are always generated with audio off. Never write sound into a
  shot prompt.

---

## 10. Verticals

Three to four vertical cuts are carved out of the same footage. The script
nominates the candidate moments.

Constraints that change how the script is written:

- **Verticals carry no data cards.** A card is composed for the lower left of
  a 16:9 frame and a 9:16 crop cuts 608 px of width out of 1920 — the labels
  survive and the numbers do not. **So every figure that matters must be
  spoken aloud**, not left to a card. A beat whose payload exists only on
  screen cannot become a vertical.
- **Captions are mandatory** and burned in from the real word timings. A
  vertical is watched muted first and read second.
- **The bottom 30% of the frame stays clear** for platform furniture. The
  caption block grows upward from it.
- **A vertical starts on a voice within one second.** Nominate in-points where
  somebody is already speaking, or starts to within a second. No held frame,
  no title, no atmosphere first. The long record earns its silences; a vertical
  is scrolled past and has earned nothing yet, so the first second has to
  contain a sentence. `validate.py` enforces this.
- **Captions stay out of the dead zones.** The bottom of a vertical frame
  belongs to the platform — caption, handle, sound name, buttons — and so does
  the right edge, where the action column sits. Nothing you write has to
  compute this, but it does mean a beat whose payload is a long sentence will
  push the caption block upward over the picture: keep the nominated lines
  short enough to caption in one or two lines.
- **Every vertical closes on the channel card** — `WATCH THE FULL RECORD ON
  THE CHANNEL`, two seconds, after the picture. Nothing to write; just know the
  cut has two seconds of tail after the last word, so the last line does not
  need to resolve anything by itself.
- **Nominate an end where the voice actually stops**, not just where a word
  ends. On this voice the gap between two words can be four hundredths of a
  second, and a cut in that gap is heard as a severed word. The safe endings
  are the end of a sentence with a real pause after it, or the end of a
  paragraph.
- A vertical ends on a **hard cut mid-sentence, on a word boundary** — never
  inside a word. Nominate the last word you want heard, not a timestamp: the
  cut is placed from the real word timings afterwards. "I am not producing—"
  is a withheld ending; "I am not produc—" is a broken file. Nominate moments that can be
  cut off mid-beat and still land.

---

## 10b. The teaser

Thirty seconds, vertical, out before the record. **You write nothing new for
it** — it is assembled from lines the script already contains — but you decide
which lines, and that decision belongs in the script.

Nominate **four or five lines that escalate on their own**, in order, with no
connective tissue between them. Record 03's are: a cartridge is spent early, a
measured figure, what that figure means, the figure from the empty room, and a
refusal. Nothing explains anything; each one is just stranger than the last.

They must be lines that survive having no context, because the teaser gives
none. A line that needs the sentence before it is not a teaser line.

The teaser ends on `SOON`, so the last nominated line does not have to resolve
anything — and must not.

## 11. Pre-submission checklist

Run this before handing the script over. Each line is checked mechanically on
the production side and each failure costs a rewrite.

- [ ] Runtime is between 3:00 and 10:00 and is justified by the material, not
      by a target.
- [ ] The cold open is image first, and the first line earns the second.
- [ ] Shot durations sum to their scene; scene seconds sum to the runtime;
      cards are counted as seconds.
- [ ] Word count sits inside the band for that runtime — **per scene**, not
      only overall. Silence between 33% and 55%.
- [ ] Every shot declares a motion tier, and the header gives the split.
- [ ] No `static` shot without text on screen. No silent shot that is not
      `model`.
- [ ] Every `model` shot is 5 s or 10 s. No shot exceeds 10 s.
- [ ] Every shot names an anchor; anchors are one per distance; the spine
      contains no camera words; one palette.
- [ ] No prompt contains readable text, faces, hands, people, grain,
      vignette, tape artefacts, or "shot on 35mm".
- [ ] All on-screen text is phosphor green Menlo at 40 px or larger. The word
      "white" does not appear near a card.
- [ ] No card sits over a screen that is already green in-fiction.
- [ ] Every card plate is framed with its lower left empty, and is long
      enough for its card to type and hold.
- [ ] Every card sits on a plate that reaches the screen with the line it
      answers to, not several shots later.
- [ ] Any coda is declared by scene number, with its reason.
- [ ] Every number is consistent with every other number, including implied
      rates and dates. Appendix lists real and invented separately.
- [ ] Pacing section lists every non-default gap with a reason.
- [ ] Three vertical candidates nominated, each with its figures spoken aloud.
- [ ] Four or five teaser lines nominated, in order, each one strange without
      context and none of them explaining another.

---

## 12. Change control

This file and `CLAUDE.md` in the production repository must stay in step.

- `CLAUDE.md` is the production pipeline; this file is the writing contract.
- Anything learned in production that changes **what a script may contain** —
  a new model constraint, a revised runtime rule, a card colour, a motion
  rule — is written into both, in the same change.
- A rule is written here **with the reason it exists**. Every rule in this
  file was paid for by a batch that came back wrong. A rule without its reason
  gets argued away by the next writer.
