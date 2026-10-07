"""Office outfit colour-combos reel. python3 plan.py <indir> <out.mp4>"""
import os, sys, glob
sys.path.insert(0, glob.glob("/root/.claude/skills/synced/*/reel-edit/scripts")[0])
from reel_style import Clip, Seg, Events, render, Y

d, out = sys.argv[1:3]
face = (718, 235)
clips = {k: Clip(os.path.join(d, k + ".mp4"), crop="720:960:0:0", face=face) for k in ["c4", "c1", "c2", "c3"]}

segs = [  # (clip, start, end, zoom)
    ("c4", 0.10, 2.70, 1.0), ("c4", 3.32, 3.95, 1.35),
    ("c1", 0.30, 2.64, 1.25), ("c1", 3.30, 4.20, 1.0), ("c1", 4.20, 6.22, 1.35),
    ("c2", 0.30, 1.02, 1.12), ("c2", 1.02, 3.04, 1.3), ("c2", 3.96, 4.44, 1.0), ("c2", 4.44, 5.92, 1.4),
    ("c3", 0.15, 1.54, 1.12), ("c3", 1.54, 1.96, 1.4), ("c3", 2.56, 3.12, 1.0), ("c3", 3.12, 4.60, 1.3),
    ("c3", 4.90, 6.70, 1.2),
]
S, t, prev = [], 0.0, None
for c, a, b, z in segs:
    S.append(dict(c=c, a=a, b=b, o=t)); t += b - a
def T(c, x):  # source time -> output time
    for s in S:
        if s["c"] == c and s["a"] - 1e-6 <= x <= s["b"] + 1e-6: return s["o"] + x - s["a"]
    raise ValueError((c, x))
segobjs = []
for i, (c, a, b, z) in enumerate(segs):
    fi = i > 0 and segs[i - 1][0] != c
    fo = i + 1 < len(segs) and segs[i + 1][0] != c or i + 1 == len(segs)
    segobjs.append(Seg(c, a, b, z, fade_in=fi, fade_out=fo))

E = Events()
def cap(c, a, b, text): E.cap(T(c, a), T(c, b) - 0.01, text)
cap("c4", 0.10, 0.92, f"{Y}Office Outfit")
cap("c4", 0.92, 1.84, f"{Y}Color Combos")
cap("c4", 1.84, 2.70, f"that never {Y}miss")
E.pop(T("c4", 3.32), T("c4", 3.95), f"SAVE {Y}THIS")
cap("c1", 0.30, 1.70, f"{Y}Pink{Y} with black")
cap("c1", 1.70, 2.64, f"looks so {Y}chic")
cap("c1", 3.30, 4.20, f"{Y}Green with")
cap("c1", 4.20, 5.40, "black looks so")
cap("c1", 5.40, 6.22, f"{Y}sophisticated")
cap("c2", 0.30, 1.02, f"{Y}Light blue with")
cap("c2", 1.02, 1.80, "black looks")
cap("c2", 1.80, 3.04, f"{Y}effortlessly classy")
cap("c2", 3.96, 4.44, f"{Y}Black with")
cap("c2", 4.44, 5.00, f"{Y}beige")
cap("c2", 5.00, 5.92, f"looks {Y}expensive")
cap("c3", 0.15, 1.54, f"And {Y}yellow with")
cap("c3", 1.54, 1.96, f"{Y}black?")
cap("c3", 2.56, 3.12, "Such a")
cap("c3", 3.12, 4.60, f"{Y}timeless combo")
cap("c3", 4.90, 5.95, "Which one are you")
cap("c3", 5.95, 6.70, f"{Y}trying first?")
print(render(clips, segobjs, E, out))
