# FC9-004 // THE LINE — publish

## Title

**No Fish Lives Below 8,200 Metres. This One Was Found At 9,450.**

Backups for CTR rotation (all declarative, none ask a question):

1. Crustaceans Live 2,700 Metres Deeper Than Any Fish. The Reason Is Not Pressure.
2. The Deepest Fish Ever Filmed Stopped 136 Metres Past The Calculation.
3. Every Specimen Dies 3,000 Metres Below The Ship. It Is Always The Same Depth.

---

## Description

```
This record is fiction. The depth limit, the molecule and both depth records
in it are real and published; the specimen below the line is invented. The
figures are separated out at the bottom.

There is a depth below which the ocean contains no fish — not fewer, none —
and it is the same depth in every ocean, on different plates, at different
temperatures. Pressure is not what sets it. Amphipod crustaceans live and
feed 2,700 metres deeper than any fish can live.

The limit is chemical, it applies to vertebrates only, and it can be
calculated.

FC9-004 // THE LINE — Survey

0:00  The line
0:34  Not pressure
1:14  The molecule
2:05  The prediction
2:40  The other solution
3:28  The ascent
4:08  Coda

REAL, AND CHECKABLE

Deep-sea fish protect their proteins against pressure by accumulating
trimethylamine N-oxide. In the hadal snailfish Notoliparis kermadecensis
from about 7,000 m in the Kermadec Trench, Yancey et al. (PNAS, 2014)
measured TMAO at 386 mmol/kg and internal osmolality at 991 mOsm/kg.
Seawater is about 1,100 mOsm/kg; shallow marine fish run near 350.

Internal concentration rises with depth. Seawater does not. Extrapolated,
the two meet at approximately 8,200 m, with the physiological ceiling placed
in the 8,200-8,400 m band. Below it, a fish carrying enough TMAO to function
would be isosmotic with the sea around it.

The prediction was published in 2014. In 2022 a Pseudoliparis snailfish was
filmed in the Izu-Ogasawara Trench at 8,336 m - 136 metres past the figure,
inside the band. Two specimens were caught in the Japan Trench at 8,022 m.
Nothing has been recorded below 8,336 m.

Pressure at 8,200 m is about 830 bar. The Challenger Deep is about 10,935 m
and roughly 1,100 bar, and Hirondellea gigas lives there.

Osmotic pressure depends on the number of dissolved particles, not their
mass. That part is real too.

INVENTED

The polymerised protectant and its 300 bar stability limit. The specimen at
9,450 m and every figure attached to it - 1,900 mmol/kg of protection at an
osmotic cost of 3 mOsm/kg, internal osmolality 380 mOsm/kg. The six surveyed
trenches. The lander's 9,600 m depth rating.

1,900 divided by 380 is 5. That was not an accident, and it is the only
number in this file that had to be arranged.

File Class Nine: material withheld from public record. Every file is
reconstructed, dramatized, and entirely invented. This channel is fiction,
start to finish.

All footage in this record is synthetic.

#fileclassnine #speculativebiology #deepsea
```

## Thumbnails

Three variants for rotation in Studio, a week at a time. Each sells a different
thing — a number, the animal, and the fact that rules pressure out — because
three plates with the same promise and the text moved around measure nothing.
Plates are approved stills the viewer actually meets in the record: 1.3 at
0:19, 6.1 at 3:31, 2.2 at 0:44. Ids never get renamed; the id is what a
conversion figure gets attached to.

| id | Plate | Says | Reads at 210 px |
|---|---|---|---|
| `a-the-line` | 1.3, the empty plain | `8,200 m` / NO FISH BELOW THIS DEPTH | yes |
| `b-the-specimen` | 6.1, the animal | `9,450 m` / 2,000 METRES PAST THE LIMIT | yes, strongest |
| `c-not-pressure` | 2.2, the crustaceans | NOT PRESSURE / THESE LIVE 2,700 m DEEPER | yes, after the plate was dimmed under the text |

Built by `scripts/build_thumbs.py` into `out/thumbs/`. Judge them at 210 px,
which is what YouTube renders in a grid and the size nobody looks at while
building a 1280 px plate: variant C's second line smeared into lit silt at grid
size until the ground under the type was darkened.

**Upload settings**

- Tick **Altered or synthetic content** → *Realistic scenes*. Every shot is
  model-generated; this record would otherwise read as real survey footage,
  which is exactly what the disclosure exists for.
- Category: Science & Technology.
- Language: English. Country: United States.

**Pinned comment**

```
The survey below 9,450 m is not in this file.
```

---

## Verticals

> Assembled, not carved — the first record on this channel where they are.
> Each cut is a shot list out of `takes/` in its own order, framed per shot
> with `crop_x`, and a line list of paragraphs the record already contains.
> Nothing was generated for any of them. Built by `scripts/vertical.py` from
> `verticals.yaml`; captions are burned in from the real word timings in
> `audio/alignment/`.

### fc9-004-b — "None."

**File:** `out/verticals/fc9-004-b-the-line.mp4` — 21.0 s
**Title:** There Are No Fish Below 8,200 Metres

**Description:**
```
Not fewer. None - and it is the same depth in every ocean, on different
plates, at different temperatures. Full record on the channel.
Fiction; the 8,200 m limit is real.
#fileclassnine #deepsea #speculativebiology
```

**Opens on** the first word of "There is a depth in every ocean below which
there are no fish." Voice at 0.2 s.
**Ends on** "Eight thousand two hundred metres." — a word boundary with 0.32 s
of real silence after it. The sentence that says what the figure means is the
next one in the record and is not in the cut.
**Picture:** 1.1, 1.2, 1.3, 1.4, then the animal in 3.1 last, after the cut has
said there are none below the line.
**Spoken figures:** 8,200 m. No card is needed for this cut to make sense.

### fc9-004-c — Pressure Is Not The Barrier

**File:** `out/verticals/fc9-004-c-not-pressure.mp4` — 28.0 s
**Title:** Crustaceans Live 2,700 Metres Deeper Than Any Fish

**Description:**
```
At the bottom of the Challenger Deep the sediment is covered in animals.
The barrier that stops fish is not mechanical. Full record on the channel.
Fiction; these figures are real.
#fileclassnine #deepsea #marinebiology
```

**Opens on** "The first answer is pressure, and it is wrong," over the
crustaceans already moving.
**Ends on** "...and only to vertebrates, and it is chemical." Paragraph end.
**Picture:** 2.2, 2.1, 2.4, 5.3, 2.3, and back to 2.2 on the last line.
**Spoken figures:** 830 bar, 1,100 bar.

### fc9-004-d — The Ascent

**File:** `out/verticals/fc9-004-d-the-ascent.mp4` — 24.5 s
**Title:** Every Specimen Is Destroyed 3,000 Metres Below The Ship

**Description:**
```
The protection is held together by pressure. It comes apart on the way up,
at the same depth every time. Full record on the channel. Fiction.
#fileclassnine #speculativebiology #deepsea
```

**Opens on** the only appearance of the animal, under "The chain is held
together by pressure."
**Ends on** "There is no version of the ascent that does not do this." The
consequence — "Nothing has reached the surface alive" — is in the record and
not in the cut.
**Picture:** 6.1, 6.2, 5.1, 6.4, 7.2.
**Spoken figures:** 300 bar, 3,000 m, 1,900 mmol/kg, 380 mOsm/kg.

---

## Teaser

**File:** `out/TEASER.mp4` — 30.0 s. Goes out **before** the record.

**Title:** There Is A Depth Where The Ocean Stops Having Fish

**Description:**
```
Not fewer. None. Full record soon.
Fiction; the depth limit and the molecule are real.
#fileclassnine #deepsea #speculativebiology
```

Opens on the animal with a voice at 0.2 s, runs five of the record's own lines
in escalating order and stops before any of them is explained. Closes on
`SOON`, never on `WATCH THE FULL RECORD` — that card belongs to the cuts, which
go out after the record exists.

Music is generated, never licensed, and it stays here: music never goes under
the record itself.
