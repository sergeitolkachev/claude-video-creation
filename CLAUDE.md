# The Archive — Production Pipeline

Faux-archival video channel. Each episode is a recording that was never
supposed to survive: a ship's log, a field report, a day in 1178.
Narration in English over slow atmospheric shots. No dialogue, no
recurring faces.

Language rule: everything in this repository is written in English —
scripts, prompts, commit messages, notes. Never translate from another
language into the narration; write it in English from the start.

## Core Constraints

- Audience: English-speaking. Narration is native English, not translated.
- Budget: ~5 hours of human time per week.
- Cadence: one long episode every two weeks, plus 3–4 vertical cuts
  carved out of the same footage.
- The bottleneck is **selection**, not generation. Automate everything
  except the decision of which frame is good.
- Do not build abstractions before the third episode. If something has
  not been done three times, it does not get a script.

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
and the config files are versioned. Everything else is reproducible.

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

Target: roughly 900–1100 words for a 10-minute episode. Narration
occupies well under half the runtime — silence is part of the format.

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
  destroys the illusion of a recording.

## Post

ffmpeg handles everything after generation. No models involved.

- Grain, vignette, slight chromatic aberration, occasional dropout.
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
- Do not upscale. Clean footage works against found-footage framing.
- Verticals: center-safe crop, hard cut mid-sentence at the end.

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
