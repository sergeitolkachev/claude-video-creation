# File Class Nine (FC9) — Production Pipeline

Faux-archival video channel. Each episode is a recording that was never
supposed to survive: a ship's log, a field report, a day in 1178.
Narration in English over slow atmospheric shots. No dialogue, no
recurring faces.

Language rule: everything in this repository is written in English —
scripts, prompts, commit messages, notes. Never translate from another
language into the narration; write it in English from the start.

Channel URL: https://www.youtube.com/@fileclassnine

## Core Constraints

- Audience: English-speaking. Narration is native English, not translated.
- Budget: ~5 hours of human time per week.
- Cadence: one long episode every two weeks, plus 3–4 vertical cuts
  carved out of the same footage.
- The bottleneck is **selection**, not generation. Automate everything
  except the decision of which frame is good.
- Do not build abstractions before the third episode. If something has
  not been done three times, it does not get a script.

## The Scripting Contract

Scripts are written outside this repository, by an agent that cannot read it.
`SCENARIO-AGENT.md` is the brief handed to that agent: it restates, in full,
every rule a script has to satisfy — runtime, motion tiers, card colour,
prompt hygiene, arithmetic, verticals — so that a submitted script is
buildable without a rewrite.

**Any change here that affects what a script may contain goes into
`SCENARIO-AGENT.md` in the same edit.** A model constraint, a runtime rule, a
card colour, a motion rule. The two files drifting apart is how a rewrite
becomes the normal state of stage 1.

## Repository Layout

```
episodes/
  ep-01-last-operator/
    script.md         # narration text, English, source of truth
    shots.yaml        # one entry per shot: prompt, duration, model
    anchors/          # 3-4 reference stills that lock the location
    stills/           # generated candidate first frames
    approved/         # stills the human picked — ONLY these get animated
    takes/            # generated video clips
    audio/            # narration/, sfx/, music/
    out/              # draft cuts, final render, vertical cuts
config/
  models.yaml         # model ids and per-second costs, single place to edit
  voice.yaml          # ElevenLabs voice_id and settings, locked per channel
scripts/              # only what has proven itself repetitive
```

Never write generated media into git. Only `script.md`, `shots.yaml`,
`publish.md` and the config files are versioned. Everything else is
reproducible.

`publish.md` holds everything that gets pasted into YouTube: the title, the
description with its disclaimer, the chapter list and the title and description
of every vertical. It is versioned for the same reason the banner is — records
01 and 02 have no such file and their descriptions exist only inside Studio,
which means the "what is real" list, the one place this channel writes its
credibility down, is not recoverable from the repository. Chapter timestamps in
it are scene boundaries summed from `shots.yaml` and are checked against it,
never copied from an older record.

## Pipeline Stages

Stages are strictly ordered. Never skip ahead — animating an unapproved
still is the single most expensive mistake in this project.

1. **Script** — narration text in `script.md`, broken into numbered beats.
2. **Shot list** — derive `shots.yaml` from the script. Visuals follow
   the words, not the other way around.
3. **Anchors** — generate 3–4 stills that define the location and light.
   Human approves these before anything else runs.
4. **Stills** — generate candidate first frames for every shot, always
   passing the anchors as references.
5. **Selection** — human moves files from `stills/` to `approved/`.
   This step is never automated and never skipped.
6. **Animation** — image-to-video on `approved/` only.
7. **Audio** — narration per paragraph, then SFX and music.
8. **Assembly** — ffmpeg: cut to timecodes, grade, grain, titles.
9. **Vertical cuts** — 3–4 shorts from the strongest moments, each
   cutting off mid-beat.

## Model Assignment

All image and video calls go through fal. Never call a model vendor
directly except ElevenLabs. Model ids live in `config/models.yaml` so
that swapping a model is a config edit, not a code change.

| Stage | Default | Notes |
|---|---|---|
| Script, shot list, prompts | Claude (this session) | no external model |
| Anchor stills | Seedream / Flux 2 | cinematic composition, atmosphere |
| Shot stills | Nano Banana (Pro or 2) | pass anchors as references |
| Bulk exploration | cheap fast model | only when hunting for direction |
| Video — workhorse | Kling Pro, **audio off** | most shots land here |
| Video — filler | Wan / Seedance Fast | pans, textures, static drift |
| Video — hero shots | Seedance / Veo | max 5–10 shots per episode |
| Narration, SFX, music | ElevenLabs | direct API key |

Audio is always disabled on video models. Narration comes from
ElevenLabs; paying for native audio is pure waste here.

**Seedance is not used.** Episode 01 established why: asked for a locked-off
shot it dollied eight metres down a corridor, and saying "the camera does not
move at all" made it travel further. Asked for a slow drift it pushed in and
pulled back, and grew a hinged bolted rim onto a porthole halfway through,
then removed it. `camera_fixed: true` changes nothing. It does not hold a
frame and it does not hold geometry. Kling holds both.

**Locked-off shots are built in ffmpeg, not generated.** A still with a
1.000 -> 1.006 zoom over the shot is steadier than any model, costs nothing,
and comes out at exactly the right duration and exactly 1920x1080 — generated
clips arrive at 1904x1088 or 1920x1088 and need cropping. On episode 01 this
covered 17 of 30 shots and removed $6.34 from the budget. `scripts/build_static.py`
also has a `drift` mode for when a controlled push is wanted and a model would
truck the subject out of frame.

Every shot in `shots.yaml` carries an explicit `model:` field. Cheap and
expensive shots must be visible in the file, never decided ad hoc.

## Writing the Narration

The voice is a recording device, not a storyteller.

- Dry, procedural, first person. The narrator is doing a job.
- Never describe what the viewer can already see on screen.
- Never explain the twist. The gap between the calm voice and the
  image is the entire effect.
- Short declarative sentences. Timestamps, serial numbers, measurements.
- The narrator does not know they are in a story and does not know
  how it ends.
- No adjectives doing emotional work: not "the terrifying silence",
  just "no response on the channel for six days".

### Runtime

**Minimum 3 minutes, maximum 10. The script decides, not a target.** An
episode runs as long as it holds, and not one shot longer. The question is
never "have we reached length" but "does this still grip". A record that
stops at 3:30 because it has said everything is finished; the same record
padded to 8 minutes is a worse record and a more expensive one.

Two tests, and both are the script's job before anything is generated:

- **The first ten seconds.** Image first, no logo, no intro. If the opening
  shot and the opening line do not make the viewer want the second line,
  nothing later rescues it. The cold open is written first and cut hardest.
- **No slack in the middle.** Every scene has to advance the arithmetic or
  turn it. A scene that restates the previous scene in new pictures is cut,
  not shortened — that is the only length control this channel uses.

Word count follows from runtime, not the other way round. Narration runs at
the measured **162 wpm** (see `config/voice.yaml`; never assume a rate) and
must leave **at least a third of the runtime as silence**, per scene and
overall. Above roughly **55% silence the episode is dragging** — records 01
and 02 both landed near 40%, which is the shape that works. So for a given
runtime the narration sits in a band:

| Runtime | Narration | = speech |
|---|---|---|
| 3:00 (180 s) | 220–325 words | 81–121 s |
| 4:30 (270 s) | 330–490 words | 122–181 s |
| 7:00 (420 s) | 510–760 words | 189–281 s |
| 10:00 (600 s) | 730–1085 words | 270–402 s |

162 wpm is a planning figure, not a promise: per-request spread on this voice
is 123–203 wpm, so the real takes decide the final runtime. Record 02 came in
slower than planned and three scenes fell under the silence floor — the
picture was lengthened and no line was cut. That is the direction the fix
always goes.

If a script comes in under the floor, the fix is to cut picture, never to
pad the voice. If it comes in over the ceiling, the fix is to cut lines.
Silence is the format; dead air is not the same thing, and the difference is
the Motion Policy below.

A closing card block, or a held silent shot before one, is exempt from the
ceiling — but only by declaration: `coda: [7]` in the episode's `shots.yaml`
names the scenes, `validate.py` then measures the body without them and prints
the coda separately. An undeclared scene is measured like any other, which is
the point: the exemption has to be a decision someone wrote down.

## Motion Policy

Record 01 was built almost entirely from locked-off frames because that was
the cheap and reliable answer to a model that would not hold a camera. It is
watchable, and it is also close to a slideshow. Record 02 fixes the rule
rather than the episode.

**A frame is allowed to be still only when the viewer is reading or
listening.** Three tiers, and every shot in `shots.yaml` declares one:

- `static` — locked-off, built in ffmpeg with lens breathing only. Allowed
  **only** for a shot carrying a data card, a title, or burned-in text. The
  eye is on the text; a moving frame under it fights the reading.
- `local` — drift or push, built in ffmpeg from the approved still. For shots
  under narration where the frame is texture rather than event. Free, exact,
  and steadier than any model, but it is a move across a photograph: no
  parallax, nothing in the frame is alive.
- `model` — a video model, normally Kling. **Required** for any shot that
  runs under silence, and for any shot whose content should physically move:
  dust, water, frost, the herd, the animal.

The rule that matters: **no text on screen and no voice means the picture
carries the shot alone, and a still frame cannot.** Silence is a format
choice here, not dead air, and it only reads as intentional if something in
the frame is moving while nobody is talking.

The budget follows the rule, not the other way round. Locked-off shots are
free and that is exactly why they are seductive; if an episode comes in
cheap because half of it is frozen, the saving was taken out of the episode.

## On-Screen Text — the channel signature

Every character that appears on screen on this channel is drawn by one
renderer, in one font, and types itself on with a sound. This is channel
furniture, like the slug: identical in every record, never varied for an
episode, never A/B tested.

- **Font: Menlo**, the same face and tracking as the episode titles and the
  channel art. One computer font, everywhere. Never a second face.
- **A card plate is sized to its card.** Text types at the rate in
  `config/type.yaml` — 18 characters a second, 0.35 s between lines, and never
  less than 2 s on screen after the last character. A four-line card of 120
  characters needs about 9 s of plate. Record 02 cut three cards off mid-word
  by setting a hold before anyone knew the typing time; record 03 caught the
  same fault in text, before generation, by running `type_schedule` against
  the shot lengths. Do that check as part of validation, not after the build.
- **Phosphor green, at 40 px on a 1080p frame, with a halo and a glow.**
  Record 02 shipped its first cards in off-white at 26 px and they vanished
  into a salt pan: pale text on pale ground has only luminance to separate it,
  and these worlds are all luminance. Green owns a channel the landscape does
  not use. The halo is a blurred black silhouette of the text and is what
  holds it on a bright plate; the glow is a blurred copy of the text itself,
  which is the bloom off an analogue monitor. Neither is a scrim or a box —
  both are the shape of the glyphs, so the frame shows through everywhere the
  text is not. **A card may never be smaller than 40 px.**
- **A card lands with the line it answers to.** A card is anchored to its
  plate and a line is anchored to its scene, and nothing connects the two on
  its own. Record 03 shipped a master where the card reading `LOG 114` typed
  fourteen seconds after the voice said "Log one fourteen" — both files
  individually correct, the beat broken, and every check that looked at one
  file at a time passed it. Each card now names its paragraph with `with:` in
  `cards.yaml` and `validate.py` measures the gap. The working range on record
  03 is -1.5 s to +3.8 s: a card may reach the screen slightly before its line,
  which reads as the instrument getting there first, and may follow by a few
  seconds. It may not drift.
- **A graphic says what it is measuring.** The first energy card drew two
  unlabelled rectangles under the numbers and they read as a progress bar for
  nothing. Every bar carries its own label inside it.
- **Characters appear one at a time**, left to right, as if arriving on a
  monitor over a slow link — not fading in, not sliding, not typewriter-
  bouncing. A line resolves and then holds.
- **Each character lands with a short click**, one per glyph, dry and quiet,
  sitting under the narration rather than over it. Synthesised locally so it
  is byte-identical between episodes — a sound that drifts is worse than no
  sound.
- Numbers that count up (an odometer, a draining bar) tick per digit change,
  same click, same level.
- The full spec — rate, jitter, click envelope, level — lives in
  `config/type.yaml`. It is versioned in full for the same reason the banner
  is: it outlives the episode.

## Writing Shot Prompts

- Every prompt describes a single continuous moment. No cuts inside a shot.
- Include: subject, light source, camera position, lens feel, motion.
- Motion stays minimal — slow drift, slow push, a single element moving.
  Fast motion is where generated video falls apart.
- No faces in focus, no hands doing detailed work, no readable text
  in frame. Titles are added in post.
- Degradation (grain, scan lines, dropout) is applied in ffmpeg, never
  prompted. Prompting it wastes generation quality.
- Default shot length: 6–8 seconds.

## Audio Rules

- Generate narration **per paragraph**, not as one file, so a single
  line can be regenerated without touching the rest.
- `voice_id` and speaking rate are locked in `config/voice.yaml`. Never
  let either drift between episodes — the voice is the channel's identity.
- **Do not target a words-per-minute figure.** Measured on this voice,
  the speed parameter is not monotonic — 0.7 came out faster than 0.8 —
  and run-to-run spread is about +/-8 wpm. It is noise, not a control.
  Pin it at the default, chosen for synthesis quality, and never touch it.
- Pacing is bought with silence between paragraphs, not with delivery
  speed inside them. Gaps are inserted at assembly, cost nothing, and are
  frame-accurate. Default gap 1.2 s between paragraphs, 2 s across a
  scene cut, longer where the script calls for it explicitly.
- If a line still reads hurried after the gaps are in, edit the sentence:
  shorter clauses, a period where a comma was. Never reach for the speed
  parameter.
- Room tone runs under the entire episode. Absolute digital silence
  destroys the illusion of a recording. **This includes the moments where a
  sound-design layer is deliberately removed.** Record 03 gated its scrubber
  fan off for scene 3 and under the closing cards, and because the fan was
  also doing duty as the room tone, both fell to -90 dBFS: not silence, but a
  file that has ended. The fan is the effect; a second ungated bed underneath
  it is the floor, and it never stops.
- **A level in `audio.yaml` is a trim applied to the file, not a target level
  in the mix.** Measure the bed, then choose the trim. Record 03 set the fan
  to -26 meaning "quiet" against a bed that was already -37.9 dBFS, landing it
  at -64: present in the mix, correctly gated, and completely inaudible — the
  same mistake twice in an hour, both times in the direction of a layer that
  exists and cannot be heard. A bed that comes back quieter than the floor
  wants is lifted, not cut; the sign follows the measurement.
- **Judge a bed in the room, not in the numbers.** The first pass at record
  03's levels was arithmetically defensible and read on a phone as having no
  background at all — which makes a deliberate silence a silence from nothing.

## Post

ffmpeg handles everything after generation. No models involved.

- Grain, vignette, slight chromatic aberration. **No dropouts.** Record 01
  collapsed the picture to near-black for 0.06 s, seven times, as a tape
  artefact; on a screen it does not read as tape, it reads as a dropped frame
  in the player, and the viewer checks their connection instead of watching
  the record. `grade.py` leaves them off unless an episode asks for them by
  name in its own `grade.yaml`. `scripts/check_flicker.py` is the gate: it
  scores a master for single dark frames, skipping shot boundaries, because a
  cut to a darker shot is not a flicker. Record 01 scores 9; record 02 scores
  0, and that is the number to ship.
- Grain is locked at `noise=alls=9` and the master at `-crf 23 -tune grain`.
  Grain is close to incompressible — every particle costs bits and kills
  inter-frame prediction — so a heavier setting is expensive without being
  visible: episode 01 measured grain 13 at CRF 20 as 2.5 GB against 276 MB for
  grain 9 at CRF 23, indistinguishable in a 1:1 crop. Never vary this between
  episodes; different grain reads as a different source recording.
- Titles go **under** the grain pass, not over it, so they belong to the
  recording instead of looking captioned onto it. Render them as Pillow PNGs
  rather than with `drawtext`, which cannot set letter-spacing, and give every
  still input `-loop 1 -t <runtime>`: a bare PNG is one frame at t=0, so the
  overlay silently draws nothing and the titles vanish without an error.
- Timecode and record-number titles burned in.
- **Count the copies before fixing the bug.** Record 03 found that inline
  pause markers — `*[2.5 s]*` — are directions to the assembly step and must
  never reach the voice. The paragraph parser existed in three scripts, two
  were fixed, and the third burned `*[2.5 s]*` into the captions of a finished
  vertical **and** shifted every word timing in that paragraph by four tenths
  of a second, because the alignment was requested for text the audio does not
  contain. There is one parser now, in `build_audio.py`, imported by
  everything that needs paragraphs. When a fix is found, the first question is
  how many places have the same code, not whether this one now works.
- **A step that lives in someone's memory is a step that will be skipped.**
  Record 02's click bed — the track that makes every card type audibly — was
  mixed by hand once and the fact was never written down. Record 03 built its
  cards, mixed its audio, graded a master and passed every gate while shipping
  a typewriter that made no sound, because nothing in the repository knew the
  step existed. The bed is mixed by `build_cards.py` now. The general rule:
  when a manual step is discovered, the fix is not to remember it, it is to
  move it inside a script so that forgetting is impossible.
- Do not upscale. Clean footage works against found-footage framing.
- Verticals: centre-safe crop, hard cut mid-sentence at the end. **Captions
  are mandatory** — a vertical is watched muted first and read second, so a
  cut without them is not finished. They are burned in from the real word
  timings (`build_captions.py`, ElevenLabs with-timestamps, called with the
  same seed *and* the same previous_text as the take in the mix), never typed
  by hand and never auto-generated by the platform.
- **A vertical opens on a voice inside one second.** Not on a held frame, not
  on a title, not on a breath — the first thing that happens is somebody
  talking, and it happens immediately. A vertical is scrolled past, not
  started; the viewer decides in the first second whether there is anything
  here, and a second of atmosphere is a second spent proving there is not.
  `validate.py` checks that narration is audible within 1.0 s of every cut's
  in-point. This is the one place where the channel's patience with silence
  does not apply: the long record earns silence, a vertical has not earned
  anything yet.
- **A caption carries a scrim, and the scrim is part of the caption.** The
  halo is the shape of the glyphs and it holds type over most plates, not all:
  record 03's verticals run over lit grating, a white sheet under a work lamp
  and a phosphor screen. Under the halo goes a soft vertical gradient —
  transparent at the top, feathered over 180 px, no edge anywhere. Not a box:
  a box has edges and edges read as a player overlay, which is why the channel
  refused one. The whole block, gradient included, is lifted so the gradient's
  bottom lands **on** the clear line, never inside it. The first build padded
  it 28 px into the clear zone and the comment in the config said so, which is
  a rule being documented as it is broken.
- **A finished record is never touched again.** Once a record is published it
  is frozen: no re-cut, no re-render, not even when a rule invented later makes
  it non-compliant and the work would cost nothing. Record 02's verticals fail
  three rules that record 03 created; record 02 ships as it is. A published
  record is a fixed artefact with a public URL, a view history and thumbnails
  in rotation, and re-rendering it changes something the audience has already
  seen for a benefit only the maker can perceive. Report the finding as
  evidence the rule is real, then stop. New rules take effect with the next
  episode.
- **A vertical closes on a card: `WATCH THE FULL RECORD ON THE CHANNEL`.** Two
  seconds, after the last frame of picture, in the channel's own Menlo and
  phosphor green, typed on like every other character on this channel. It is
  furniture — same text, same duration, every vertical, every episode. A
  vertical is the only place the channel asks for anything, and it asks once,
  at the end, after the viewer has already decided.
- **A word boundary in an alignment is not the end of the sound.** ElevenLabs
  marks a word as ending where the next one begins, which on this voice can be
  forty milliseconds later — so a cut placed just after a word's timestamp
  severs its decay and is heard as a cut mid-word. Record 03 shipped two
  verticals that way and the validator passed both, because the validator was
  reading the same timestamps that were wrong. A cut needs **real silence after
  it**: at least `VERT_TAIL` seconds between the last word and the next, or the
  end of a paragraph. Measured, not assumed.
- **A vertical stops mid-sentence, on a word boundary. Never mid-word.** A
  severed word is not a withheld ending, it is a file that broke, and the
  viewer reads a fault rather than a choice. Cut points come from the real word
  timings in `audio/alignment/`, not from an estimate, and `validate.py`
  rejects any `to:` that falls inside a word — **with no tolerance at all**. A
  first version allowed 0.02 s either side and passed a cut that clipped the
  last twenty milliseconds off "open": a margin the size of the fault it is
  meant to catch is not a check.
- **A caption never lands in a dead zone, on any platform.** Every vertical
  platform parks furniture in the same places and none of them tells you
  where: the bottom for the caption, handle, sound name and buttons, the right
  edge for the action column. The caption block is centred inside
  `captions.safe_width` and grows **upward** from `captions.bottom_clear`, so
  a second line never reaches down into the pile. Both figures live in
  `config/type.yaml`, both are channel-wide, and `validate.py` computes the
  block's real pixel extent from the font metrics and fails if it crosses
  either boundary. A caption that reads on one platform and is buried on
  another is not a format, it is luck.
- **The bottom 30% of a vertical stays clear.** Every platform parks its own
  furniture there — the caption, the handle, the sound name, the buttons — and
  record 01 left only 264 px of 1920 and still ended up underneath the pile.
  The caption block grows *upward* from that clear space, so a second line
  never eats into it. The figure is `captions.bottom_clear` in
  `config/type.yaml` and it is channel-wide: a short that reads on one
  platform and is buried on another is not a format, it is luck.
- Verticals carry no data cards. A card is composed for the lower left of a
  16:9 frame; a 9:16 crop takes 608 px of width out of 1920, so the labels
  survive and the numbers do not. They are cut from `EPISODE-clean.mp4` —
  same grade, same grain, nothing laid over it — and the click track comes
  out with the cards, because a typing sound over nothing typing is a fault.

## `shots.yaml` Schema

Duration is two separate fields. Conflating them breaks validation the
moment a shot is retimed in post.

```yaml
- id: 5.3
  generate_seconds: 10      # what the model is asked for
  timeline_seconds: 12      # what it occupies in the cut
  model: kling-pro
  prompt: "..."
- id: 6.1
  source: ffmpeg            # no generation at all
  timeline_seconds: 12
```

- `timeline_seconds` defaults to `generate_seconds` when absent.
- Runtime validation sums `timeline_seconds`. Cost estimation sums
  `generate_seconds`, skipping any shot with `source: ffmpeg`.
- Retiming beyond 1.3x is not allowed — camera drift starts reading as
  a stutter rather than as the medium.

## Validation Before Generation

Run these checks against `shots.yaml` before spending anything. They are
cheap in text and expensive in credits.

- `timeline_seconds` must sum to the stated runtime, per scene and overall.
  Never parse duration out of prose — read the field.
  A mismatch means either missing shots or an incorrect runtime — resolve
  it in the script, never by stretching clips in post.
- Narration word count divided by the locked wpm must leave at least a
  third of the runtime as silence. Use the measured rate, not an assumed one.
- Every shot has a `model:` field.
- No shot exceeds the model's maximum clip length.
- Any figure stated in the narration (distances, delays, dates) must be
  internally consistent. The genre lives on numbers that check out.

## What Episode 01 Cost Us To Learn

Each of these was found by paying for a batch that came back wrong. None of
them is guessable from a model's documentation.

**Anchors lock composition, not just style.** An anchor is a reference image,
and the model preserves its framing as much as its palette. A wide
establishing anchor handed to a macro shot returns a wide establishing shot.
Match the anchor's distance to the shot's distance, or the prompt loses. Keep
one anchor per distance: a room, a macro, and whatever else recurs.

**A style spine carries material, light and palette — never camera.** Words
like "low ceiling", "built for a single occupant", "rounded corners" read as
framing instructions and push every shot to a wide. Camera, distance and lens
belong in each shot's own block.

**A spine may not name an object, not even to restrict it.** Record 03's spine
said the station's only warm light was a portable work lamp "and it appears
only in the shots that name it". The lamp then appeared in eight of fifteen
anchor candidates, standing in frame, lighting shots that had never asked for
it. The model reads the noun and discards the clause governing it. A
restriction on where an object may appear is not a prompt — it belongs in
`shots.yaml`, where only the shots that want it mention it, and the spine
forbids it outright.

**One spine per camera distance, not per episode.** The same record's spine
opened "Interior of an orbital relay station", which is a framing instruction
wearing a material's clothes: it put a room in every frame, and the macro and
top-down anchors came back as mid-distance interiors in all six candidates.
Splitting out a `macro_spine` with no room noun in it — no interior, no
station, no wall, no ceiling — fixed the macro anchor on the next pass. If two
anchors are at distances where the word "interior" is wrong, they need
separate spines, the same way exteriors do.

**A negation only works when the subject does not imply it.** Record 03 held
"no lettering" and "no people" across sixty stills without a single failure,
and lost "no portable lamp" in eight anchor candidates out of fifteen — because
the shots that forbade the lamp were asking for hard raking light in the same
breath. Forbid what the frame has no reason to contain; for anything the
subject implies, fill the frame with something else instead. "One broad shallow
depression" cannot be fixed by adding "no crater"; it is fixed by describing
what is there.

**Removing a detail removes the texture around it unless you put the texture
back.** Record 03's handheld sensor was returning a lit display with lettering
on it, so the display came out of the prompt — and so did every other surface
cue, leaving "a plain dark case, nothing lit on it". The model returned a
product render: clean, new, and belonging to no world, in a record where every
other object is worn. Take out one property at a time, and when you take one
out, name what occupies its place. Here: the case scuffed pale along every
edge from being carried, dust worked into its seams and into the grating under
it.

**Exterior shots need their own spine.** An interior spine handed to a shot
set in open space does not transfer style, it puts a bulkhead in the frame.
And an edit endpoint that requires a reference image cannot do exteriors at
all — route them to text-to-image.

**When two shots are the same object seen twice, reference the approved still,
not the anchor.** `ref_shot:` in `shots.yaml`. An anchor makes them the same
kind of thing; the approved still makes them the same thing, down to the
scratch in the glass. The catch: the reference resists intended change too, so
use it where nothing should change, and do the change in post.

**Prompt enhancers cannot always be turned off.** Seedream rewrites every
prompt before generating and offers no way to disable it. Anything vague gets
filled in with whatever is statistically typical — "dust particles floating"
became heaps of grit on the floor, "station corridor" became a concrete
utility tunnel, "small circular porthole" was read as small in the frame. Be
specific enough that there is nothing left to invent.

**Some phrases break a model outright.** `shot on 35mm` makes Nano Banana
return `no_media_generated` and produce nothing at all. Isolate a failure by
removing one clause at a time rather than rewriting the whole prompt.

**A non-default voice touches the whole audio chain, not one stage.** Record 03
is the first told by its operator rather than the channel narrator, and three
separate scripts broke on it in turn: `gen_narration.py`, `build_audio.py`'s
caller and `build_captions.py` each read `config/voice.yaml` independently and
each had `narrator` written into it. The third was the dangerous one — captions
timed against a voice that is not in the record place every word where it is
not spoken. An episode names its voice once, in `shots.yaml` under `voice:`,
and every stage reads that. Check the whole chain when a channel-level default
changes, not the stage where the change was noticed.

**ElevenLabs varies wildly between requests.** The same paragraph at the same
settings came back anywhere from 123 to 203 wpm. Generating everything in one
sitting does not help — every paragraph is its own request. A `seed` pins the
delivery exactly and reproducibly, so generate several seeded takes, keep the
one whose pace sits with its neighbours, and record the seed. The `speed`
parameter is not a control: its range is 0.7-1.2, the response is not
monotonic, and per-request noise swamps the whole parameter.

**Any script that polls an API needs a timeout and unbuffered output.** An
hour was lost to a poll hung on a socket with no timeout, while a
block-buffered log showed a state that was fifty minutes stale. Set an
explicit timeout on every network call, wrap polls so a dropped connection
retries instead of hanging, and flush every print. Losing a request id to an
unflushed log means paying for the same clip twice.

## Channel Art

Avatar, banner, thumbnail plate and a spare corridor plate. Prompts, sizes
and the burned-in text live in `config/brand.yaml` — versioned in full,
unlike an episode's media, because channel art outlives episodes and a banner
re-derived from memory in a year is a broken brand.

- `scripts/gen_brand.py` generates three seeded candidates per asset through
  the same text-to-image tier as anchors. `scripts/build_brand.py` crops the
  approved plate to spec and burns the text in. Selection between them is
  human, the same as stills.
- **No characters are ever generated.** Seedream invents lettering out of
  anything resembling a label and returns garbage glyphs. The spine forbids
  text; Pillow composites it after, in the same Menlo and tracking as the
  episode titles. Every burned-in character on the channel comes out of one
  renderer, which is what makes it read as issued rather than assembled.
- The banner is composed empty in the middle: only the centre 1546x423 of
  2560x1440 survives on every device. `build_brand.py` writes a safe-area
  check plate and a 32 px avatar check — the crop is what goes wrong, and
  neither failure is visible in the export.
- Sizes are YouTube's published requirements. Re-check them before a final
  export; they drift like model prices.

### Numbering

- Long episodes: `FC9-LOG-041 // The Aldren Basin Survey`
- Vertical cuts: `FC9-041.b // Fragment`

The slug is channel furniture: same font, same size, same corner on every
thumbnail, and it is never part of what an A/B test is varying.

### Thumbnails

`scripts/build_thumbs.py <episode>` builds every variant in the episode's
`thumbnails.yaml`. Plates are **approved stills, never new generations** — the
frame is already in the episode, and a thumbnail promising a frame the episode
does not contain is the reliable way to lose watch time.

**Judge a thumbnail at 210 px, which is what YouTube renders in a grid.** It is
the only size that decides anything and the one nobody looks at while building
a 1280 px plate. Record 03 built three variants that all read at full size; at
grid size one had its second line smeared into the slug and another had it
crossing a ceiling light. `validate.py` checks blocks against the slug's band,
and `build_thumbs.py` output should be looked at as a row of 210 px tiles
before anything is approved.

Variants are for swapping in Studio a week at a time, so each one has to sell
a different thing — a number, a view, a person. Three plates with the same
promise and the text moved around measure nothing. The variant id is what a
conversion figure gets attached to later, so ids do not get renamed.

## Cost Discipline

- Kill bad ideas at the stills stage. A rejected still costs cents;
  a rejected clip costs 10–30x that.
- Track spend per episode in `episodes/<id>/cost.md`. If an episode
  runs past its ceiling, stop and diagnose — it is almost always a
  prompt problem, not a model problem.
- Prices and model names drift every few months. Re-check
  `config/models.yaml` against fal's current pricing before each episode.

## Working Agreements

- Ask before spending: any batch over ~50 generations gets confirmed first.
- Never regenerate an approved asset without being asked.
- When a shot fails twice, stop and report — do not burn credits looping.
- Report cost after every batch.
- Answer and Type to user in Russian language
- Do NOT commit, do NOT push to Git