import sys
sys.path.insert(0, ".")
from reel_style import Clip, Seg, Events, render, Y, WH

CR, FACE = "720:964:0:158", (660, 520)
clips = {k: Clip(f"{k}.mp4", crop=CR, face=FACE) for k in ("c3", "c1", "c4", "c2")}
# (clip, start, end, zoom, bw, fade_in, fade_out)
S = [("c3", .18, 1.28, 1.0, 0, 0, 0), ("c3", 1.28, 2.82, 1.25, 1, 0, 0), ("c3", 2.82, 3.46, 1.12, 0, 0, 0), ("c3", 3.68, 5.56, 1.4, 0, 0, 1),
     ("c1", .56, 1.74, 1.0, 0, 1, 0), ("c1", 1.74, 3.42, 1.25, 0, 0, 0), ("c1", 3.74, 4.38, 1.12, 0, 0, 0), ("c1", 4.38, 5.88, 1.4, 0, 0, 1),
     ("c4", .30, .94, 1.0, 1, 1, 0), ("c4", .94, 2.30, 1.25, 1, 0, 0), ("c4", 2.30, 3.74, 1.12, 1, 0, 0), ("c4", 3.76, 4.82, 1.0, 1, 0, 0),
     ("c4", 4.82, 6.14, 1.25, 1, 0, 0), ("c4", 6.14, 6.86, 1.45, 1, 0, 1),
     ("c2", .26, 1.28, 1.0, 0, 1, 0), ("c2", 1.28, 2.50, 1.25, 1, 0, 0), ("c2", 2.50, 3.22, 1.45, 1, 0, 0), ("c2", 3.22, 4.48, 1.0, 0, 0, 0),
     ("c2", 4.48, 5.54, 1.25, 0, 0, 0), ("c2", 6.42, 7.20, 1.45, 0, 0, 1)]
segs, off, t = [], [], 0.0
for c, a, b, z, bw, fi, fo in S:
    segs.append(Seg(c, a, b, z, bool(bw), bool(fi), bool(fo))); off.append((c, a, b, t)); t += b - a

def T(c, s):  # source time -> output time
    for cc, a, b, o in off:
        if cc == c and a - 1e-6 <= s <= b + 1e-6: return o + s - a
    raise ValueError((c, s))

E = Events()
def cap(c, a, b, text, **k): E.cap(T(c, a), T(c, b) - .01, text, **k)
cap("c3", .20, 1.27, f"I used to {Y}think{WH} I had")
cap("c3", 1.28, 2.81, f"an {Y}overthinking problem")
cap("c3", 2.82, 3.45, f"{Y}Turns out")
cap("c3", 3.68, 4.54, f"I had a {Y}trusting")
cap("c3", 4.55, 5.55, f"{Y}myself problem")
cap("c1", .56, 1.73, f"I didn't {Y}trust myself")
cap("c1", 1.74, 2.46, "to handle it")
cap("c1", 2.47, 3.41, f"if things went {Y}wrong")
cap("c1", 3.74, 4.37, f"So I {Y}tried to")
cap("c1", 4.38, 5.15, f"{Y}control everything")
cap("c1", 5.16, 5.87, f"{Y}instead")
cap("c4", .30, .93, f"{Y}catastrophize,")
cap("c4", .94, 2.29, f"{Y}strategize,")
cap("c4", 2.30, 3.01, f"plan {Y}A")
cap("c4", 3.02, 3.73, f"through {Y}Z")
cap("c4", 3.76, 4.81, "and still end up")
cap("c4", 4.82, 6.13, f"{Y}exhausted at")
E.pop(T("c4", 6.14), T("c4", 6.86) - .01, f"{Y}2 A.M.")
cap("c2", .26, 1.27, f"The {Y}solution isn't")
cap("c2", 1.28, 2.49, f"{Y}overthinking the")
cap("c2", 2.50, 3.21, f"{Y}overthinking")
cap("c2", 3.22, 4.47, f"It's just {Y}deciding")
cap("c2", 4.48, 5.53, f"to {Y}believe")
E.pop(T("c2", 6.42), T("c2", 7.20) - .01, f"I'VE GOT\\N{Y}THIS")
print(render(clips, segs, E, "reel.mp4"), round(t, 2))
