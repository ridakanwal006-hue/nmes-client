"""Worked example: the Sophia Clip 1 + Clip 2 story cut in the checklist style.

  python3 example_plan.py <clip1.mp4> <clip2.mp4> <out.mp4>

Copy this file for a new video and change: clips (crop, face), the clip ranges, the title,
the checklist items and their reveal words, and the effects.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from checklist_style import Clip, Seg, Timeline, Events, load_words, speech_runs, auto_captions, render, ANGLES

def first(words, text, after=0.0):
    """Start time of the first spoken word equal to text (ignoring punctuation) after a time."""
    for w in words:
        if w["s"] >= after and w["w"].strip(".,!?;:'\"").lower() == text.lower():
            return w["s"]
    raise ValueError(f"'{text}' is not spoken after {after}s")

c1, c2, out = sys.argv[1:4]
clips = {"c1": Clip(c1, crop="1080:1444:0:238", face=(0.56, 0.24)),
         "c2": Clip(c2, crop="720:964:0:158", face=(0.56, 0.24))}
W1, W2 = load_words(c1), load_words(c2)

# clip ranges: clip 1 stops before its cut-off last word, clip 2 skips its lead-in silence
segs, k = [], 0
for name, words, a, b in [("c1", W1, 0.0, 7.30), ("c2", W2, 0.20, 7.60)]:
    for s, e in speech_runs(words, a, b):
        zoom = ANGLES[k % len(ANGLES)]
        if name == "c2" and k % len(ANGLES) == 3:
            zoom = 1.42            # clip 2 is 720p: keep close-ups at or under ~1.45x
        segs.append(Seg(name, s, e, zoom=zoom)); k += 1
segs[-1].zoom_to = segs[-1].zoom * 1.08     # slow push-in on the final line
T = Timeline(segs)

E = Events()
panel_at = T("c1", first(W1, "sorry"))
E.title(0.0, panel_at, ["3 steps of", "over-apologizing"])
E.sfx(0.0, "whoosh", -24)
E.checklist(panel_at, T.end, [
    ("1.", "Text", "'sorry, ignore me'", panel_at),
    ("2.", "Wait", "4 minutes", T("c2", first(W2, "four"))),
    ("3.", "Apologize", "again", T("c2", first(W2, "apologized"))),
])
E.sfx(panel_at, "whoosh", -24)
E.sfx(T("c2", first(W2, "four")), "pop", -20)
E.sfx(T("c2", first(W2, "apologized")), "pop", -20)
for name, words, a, b in [("c1", W1, 0.0, 7.30), ("c2", W2, 0.20, 7.60)]:
    auto_captions(E, T, name, words, start=a, end=b)
print(render(clips, segs, E, out))
