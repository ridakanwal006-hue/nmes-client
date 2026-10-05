import sys
sys.path.insert(0, ".")
from reel_style import Clip, Seg, Events, render, Y, WH

CR, FACE = "720:964:0:158", (660, 520)
clips = {k: Clip(f"{k}.mp4", crop=CR, face=FACE) for k in ("e4", "e3", "e1", "e2")}
# (clip, start, end, zoom, bw, fade_in, fade_out)
S = [("e4", .42, .96, 1.0, 1, 0, 0), ("e4", .96, 2.30, 1.25, 1, 0, 0), ("e4", 3.06, 4.30, 1.12, 1, 0, 0),
     ("e4", 4.70, 5.68, 1.3, 1, 0, 0), ("e4", 5.76, 6.58, 1.45, 1, 0, 1),
     ("e3", .20, .66, 1.45, 0, 1, 0), ("e3", 1.08, 2.07, 1.0, 0, 0, 0), ("e3", 2.10, 3.40, 1.25, 0, 0, 0),
     ("e3", 4.64, 6.36, 1.12, 0, 0, 0), ("e3", 6.38, 6.82, 1.45, 0, 0, 1),
     ("e1", .22, 1.86, 1.0, 0, 1, 0), ("e1", 1.94, 2.84, 1.25, 0, 0, 0), ("e1", 3.94, 4.92, 1.12, 0, 0, 0), ("e1", 5.58, 6.48, 1.45, 0, 0, 1),
     ("e2", .74, 1.62, 1.0, 0, 1, 0), ("e2", 1.62, 2.26, 1.3, 0, 0, 0), ("e2", 2.82, 3.74, 1.12, 0, 0, 0), ("e2", 3.74, 4.72, 1.45, 0, 0, 1)]
segs, off, t = [], [], 0.0
for c, a, b, z, bw, fi, fo in S:
    segs.append(Seg(c, a, b, z, bool(bw), bool(fi), bool(fo))); off.append((c, a, b, t)); t += b - a

def T(c, s):
    for cc, a, b, o in off:
        if cc == c and a - 1e-6 <= s <= b + 1e-6: return o + s - a
    raise ValueError((c, s))

E = Events()
def cap(c, a, b, text, **k): E.cap(T(c, a), T(c, b) - .01, text, **k)
def pop(c, a, b, text, **k): E.pop(T(c, a), T(c, b) - .01, text, **k)
cap("e4", .42, .95, f"But {Y}self-doubt")
cap("e4", .96, 2.29, f"doesn't care about {Y}logic")
cap("e4", 3.06, 4.29, f"It {Y}replays{WH} every moment")
cap("e4", 4.70, 5.67, f"{Y}hunting{WH} for proof")
E.label(T("e4", 5.76), T("e4", 6.58) - .01, "SELF-DOUBT:")
cap("e4", 5.76, 6.57, f"\"You're the {Y}problem\"", style="Quote")
cap("e3", .20, .65, f"{Y}You're not")
cap("e3", 1.08, 2.06, f"Their {Y}no{WH} is information")
cap("e3", 2.10, 3.39, f"not a {Y}verdict")
cap("e3", 4.82, 6.35, f"Stop letting {Y}rejection\\N{WH}write your")
pop("e3", 6.38, 6.81, f"{Y}STORY")
cap("e1", .22, 1.85, f"{Y}Rejection{WH} doesn't\\Nmean you're {Y}lacking")
cap("e1", 1.94, 2.83, f"Sometimes it's {Y}just")
cap("e1", 3.94, 4.91, f"{Y}not your person")
pop("e1", 5.58, 6.47, f"NOT YOUR\\N{Y}PLACE")
cap("e2", .74, 1.61, f"You can be a {Y}great")
cap("e2", 1.62, 2.25, f"{Y}person")
cap("e2", 2.82, 3.73, f"and still be {Y}wrong")
pop("e2", 3.74, 4.71, f"FOR\\N{Y}SOMEONE")
print(render(clips, segs, E, "reel3.mp4"), round(t, 2))
