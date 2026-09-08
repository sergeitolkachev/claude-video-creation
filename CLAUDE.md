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
- `voice_id` is locked in `config/voice.yaml`. Never let it drift
  between episodes — the voice is the channel's identity.
- Room tone runs under the entire episode. Absolute digital silence
  destroys the illusion of a recording.

## Post

ffmpeg handles everything after generation. No models involved.

- Grain, vignette, slight chromatic aberration, occasional dropout.
- Timecode and record-number titles burned in.
- Do not upscale. Clean footage works against found-footage framing.
- Verticals: center-safe crop, hard cut mid-sentence at the end.

## Validation Before Generation

Run these checks against `shots.yaml` before spending anything. They are
cheap in text and expensive in credits.

- Shot durations must sum to the stated runtime, per scene and overall.
  A mismatch means either missing shots or an incorrect runtime — resolve
  it in the script, never by stretching clips in post.
- Narration word count divided by ~140 wpm must be less than the runtime.
  If speech fills more than two thirds of the episode, cut words.
- Every shot has a `model:` field.
- No shot exceeds the model's maximum clip length.
- Any figure stated in the narration (distances, delays, dates) must be
  internally consistent. The genre lives on numbers that check out.

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
