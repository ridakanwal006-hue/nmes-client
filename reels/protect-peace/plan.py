import sys
sys.path.insert(0, ".")
from reel_style import Clip, Seg, Events, render, Y, WH

CR, FACE = "720:964:0:200", (897, 528)
clips = {k: Clip(f"{k}.mp4", crop=CR, face=FACE) for k in ("k3", "k4", "k2", "k1")}
# (clip, start, end, zoom, bw, fade_in, fade_out)
S = [("k3", .62, 2.18, 1.0, 1, 0, 0), ("k3", 3.02, 4.34, 1.25, 1, 0, 0), ("k3", 4.36, 5.06, 1.45, 1, 0, 1),
     ("k4", .46, 2.08, 1.12, 1, 1, 0), ("k4", 3.12, 4.08, 1.3, 1, 0, 0), ("k4", 4.60, 5.84, 1.45, 1, 0, 1),
     ("k2", .50, 2.40, 1.0, 0, 1, 0), ("k2", 2.96, 4.20, 1.25, 0, 0, 0), ("k2", 4.28, 5.30, 1.45, 0, 0, 1),
     ("k1", .30, 1.34, 1.0, 0, 1, 0), ("k1", 1.56, 2.54, 1.3, 0, 0, 0), ("k1", 3.16, 4.60, 1.12, 0, 0, 0), ("k1", 4.60, 6.48, 1.45, 0, 0, 1)]
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
cap("k3", .62, 2.17, f"Some people are only {Y}happy")
cap("k3", 3.02, 4.33, f"when they {Y}drag you down")
pop("k3", 4.36, 5.05, f"TO THEIR\\N{Y}LEVEL")
cap("k4", .46, 2.07, f"They'll {Y}pick apart\\N{WH}everything you do")
cap("k4", 3.12, 4.07, f"not to {Y}help you")
cap("k4", 4.60, 5.83, f"it just makes them\\N{Y}feel better")
cap("k2", .50, 2.39, f"So I {Y}stopped explaining\\N{WH}myself")
cap("k2", 2.96, 4.19, f"to people who'd\\N{Y}already{WH} made up")
pop("k2", 4.28, 5.29, f"THEIR MINDS\\N{Y}ABOUT ME")
cap("k1", .30, 1.33, f"{Y}Protect{WH} your peace")
cap("k1", 1.56, 2.53, f"It's {Y}expensive")
cap("k1", 3.16, 4.59, f"Stop handing it out\\Nfor {Y}free")
cap("k1", 4.60, 6.47, f"to people who'd {Y}never\\N{WH}do the same for you")
print(render(clips, segs, E, "reel4.mp4"), round(t, 2))
