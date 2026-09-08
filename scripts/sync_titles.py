#!/usr/bin/env python3
"""Pin every log card to the line it belongs to.

Hard-coded card times drift the moment narration placement changes. On the
first pass the paragraphs were redistributed across each scene and the cards
were not re-synced, which left LOG 046 three seconds early and LOG 047 six —
the card announced the reading before the operator said it. Times are now
derived from the audio, so the two cannot disagree.
"""
import re, subprocess, pathlib, yaml

SCENE_START = {1: 0, 2: 22, 3: 65, 4: 110, 5: 165, 6: 230}
SCENE_END   = {1: 22, 2: 65, 3: 110, 4: 165, 5: 230, 6: 250}
LEAD_IN, TAIL, MIN_GAP = 1.5, 3.0, 1.2
HOLD = {"s5p6": 2.5, "s5p8": 1.8}
CARD_LEAD = 0.5      # the card appears just before the line it labels

CARD_FOR = {"log-041": "s1p1", "log-043": "s2p1", "log-044": "s3p1",
            "log-045": "s4p1", "log-046": "s4p2", "log-047": "s4p3",
            "log-051": "s5p1"}

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
        "-of","default=nw=1:nk=1",str(p)], capture_output=True, text=True).stdout)

def placement(ep):
    A = ep / "audio"
    picks = yaml.safe_load((A / "narration.yaml").read_text())["picks"]
    by = {}
    for pid, seed in picks.items():
        by.setdefault(int(pid[1]), []).append((pid, A / "narration" / f"{pid}_s{seed}.mp3"))
    pos = {}
    for sc, items in by.items():
        span = SCENE_END[sc] - SCENE_START[sc] - LEAD_IN - TAIL
        speech = sum(dur(f) for _, f in items)
        holds = sum(HOLD.get(p, 0) for p, _ in items)
        gap = max(MIN_GAP, (span - speech - holds) / max(len(items) - 1, 1))
        t = SCENE_START[sc] + LEAD_IN
        for pid, f in items:
            t += HOLD.get(pid, 0); pos[pid] = t; t += dur(f) + gap
    return pos

def main():
    ep = pathlib.Path("episodes/ep-01-tishina-9")
    pos = placement(ep)
    path = ep / "titles.yaml"
    doc = yaml.safe_load(path.read_text())
    raw = path.read_text()
    changed = 0
    for c in doc["cards"]:
        pid = CARD_FOR.get(c["id"])
        if not pid:
            continue
        new = round(pos[pid] - CARD_LEAD, 1)
        # Anchor on the id line as it actually appears in the list ("  - id:"),
        # then rewrite the at: on the following line. A blind string replace
        # here failed silently once already and left the cards where they were.
        pat = re.compile(rf"(- id: {re.escape(c['id'])}\n\s+at: )([\d.]+)")
        raw, n = pat.subn(rf"\g<1>{new}", raw)
        if n != 1:
            raise SystemExit(f"could not rewrite {c['id']}: matched {n} times")
        if abs(new - c["at"]) > 0.05:
            print(f"  {c['id']:<10} {c['at']:6.1f} -> {new:6.1f}  (голос в {pos[pid]:.1f})")
            changed += 1
        else:
            print(f"  {c['id']:<10} {c['at']:6.1f}     совпадает")
    path.write_text(raw)

    # verify what actually landed on disk, not what we intended to write
    check = yaml.safe_load(path.read_text())
    for c in check["cards"]:
        pid = CARD_FOR.get(c["id"])
        if pid and abs(c["at"] - (pos[pid] - CARD_LEAD)) > 0.05:
            raise SystemExit(f"{c['id']} did not take: file says {c['at']}")
    print(f"\n  {changed} card(s) moved, all verified against the file")

if __name__ == "__main__":
    main()
