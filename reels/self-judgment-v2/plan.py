import sys
sys.path.insert(0, ".")
from reel_style import Clip, Seg, Events, render, Y, WH

CR = "720:964:0:200"
clips = {"n3": Clip("n3.mp4", crop=CR, face=(810, 520)), "n2": Clip("n2.mp4", crop=CR, face=(810, 520)),
         "n4": Clip("n4.mp4", crop=CR, face=(870, 520)), "n1": Clip("n1.mp4", crop=CR, face=(838, 520))}
# (clip, start, end, zoom, bw, fade_in, fade_out)
S = [("n3", .98, 2.28, 1.0, 1, 0, 0), ("n3", 2.30, 3.72, 1.25, 1, 0, 0), ("n3", 3.76, 4.98, 1.12, 1, 0, 0), ("n3", 5.00, 5.64, 1.45, 1, 0, 1),
     ("n2", .26, 2.92, 1.12, 1, 1, 0), ("n2", 3.04, 3.94, 1.3, 0, 0, 0), ("n2", 4.64, 6.34, 1.45, 0, 0, 1),
     ("n4", .30, .98, 1.0, 0, 1, 0), ("n4", 1.18, 2.58, 1.25, 0, 0, 0), ("n4", 3.78, 5.50, 1.12, 0, 0, 0), ("n4", 5.50, 5.98, 1.45, 0, 0, 1),
     ("n1", .02, 2.04, 1.0, 0, 1, 0), ("n1", 2.12, 3.56, 1.25, 0, 0, 0), ("n1", 4.48, 5.24, 1.12, 0, 0, 0),
     ("n1", 5.66, 6.12, 1.3, 0, 0, 0), ("n1", 6.14, 6.90, 1.45, 0, 0, 1)]
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
cap("n3", .98, 2.27, f"{Y}Words{WH} and opinions")
cap("n3", 2.30, 3.71, f"can only {Y}hurt{WH} you")
cap("n3", 3.76, 4.97, f"as much as\\Nyou {Y}believe")
pop("n3", 5.00, 5.63, f"THEY'RE\\N{Y}TRUE")
cap("n2", .26, 1.20, f"next time you {Y}worry{WH} about")
cap("n2", 1.21, 2.91, f"someone {Y}judging{WH} you")
cap("n2", 3.04, 3.93, f"{Y}realize{WH} something")
cap("n2", 4.64, 5.16, "You're actually")
cap("n2", 5.17, 6.33, f"{Y}judging yourself")
cap("n4", .30, .97, f"So {Y}ask")
cap("n4", 1.18, 2.57, f"Why does {Y}this sting")
cap("n4", 3.78, 5.49, f"What {Y}part{WH} of me\\Nagrees with")
cap("n4", 5.50, 5.97, f"{Y}them")
cap("n1", .02, .80, "It's not their")
cap("n1", .81, 2.03, f"{Y}judgment{WH} hurting you")
cap("n1", 2.12, 3.55, f"It's your own {Y}self-doubt")
cap("n1", 4.48, 5.23, f"{Y}Reframe{WH} it")
cap("n1", 5.66, 6.11, "and take your")
pop("n1", 6.14, 6.89, f"{Y}POWER\\NBACK")
print(render(clips, segs, E, "reel6.mp4"), round(t, 2))
