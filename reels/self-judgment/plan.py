import sys
sys.path.insert(0, ".")
from reel_style import Clip, Seg, Events, render, Y, WH

CR = "720:964:0:200"
clips = {"m4": Clip("m4.mp4", crop=CR, face=(840, 520)), "m2": Clip("m2.mp4", crop=CR, face=(810, 520)),
         "m1": Clip("m1.mp4", crop=CR, face=(750, 520)), "m3": Clip("m3.mp4", crop=CR, face=(810, 520))}
# (clip, start, end, zoom, bw, fade_in, fade_out)
S = [("m4", .42, 1.16, 1.0, 1, 0, 0), ("m4", 1.18, 2.56, 1.25, 1, 0, 0), ("m4", 2.58, 3.90, 1.12, 1, 0, 0), ("m4", 3.90, 4.54, 1.45, 1, 0, 1),
     ("m2", 0.0, 2.26, 1.12, 1, 1, 0), ("m2", 2.86, 3.82, 1.3, 0, 0, 0), ("m2", 4.40, 5.96, 1.45, 0, 0, 1),
     ("m1", .02, .84, 1.0, 0, 1, 0), ("m1", 1.28, 2.80, 1.25, 0, 0, 0), ("m1", 4.06, 5.64, 1.12, 0, 0, 0), ("m1", 5.66, 6.00, 1.45, 0, 0, 1),
     ("m3", .18, 2.02, 1.0, 0, 1, 0), ("m3", 2.24, 3.48, 1.25, 0, 0, 0), ("m3", 4.46, 5.20, 1.12, 0, 0, 0), ("m3", 5.76, 6.90, 1.45, 0, 0, 1)]
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
cap("m4", .42, 1.15, f"{Y}Words{WH} and opinions")
cap("m4", 1.18, 2.55, f"can only {Y}hurt")
cap("m4", 2.58, 3.89, f"you as much as\\Nyou {Y}believe")
pop("m4", 3.90, 4.53, f"THEY'RE\\N{Y}TRUE")
cap("m2", 0.0, .97, f"next time you {Y}worry{WH} about")
cap("m2", .98, 2.25, f"someone {Y}judging{WH} you")
cap("m2", 2.86, 3.81, f"{Y}Realize{WH} something")
cap("m2", 4.40, 5.95, f"You're actually\\N{Y}judging yourself")
cap("m1", .02, .83, f"So {Y}ask")
cap("m1", 1.28, 2.79, f"Why does {Y}this sting")
cap("m1", 4.06, 4.86, f"What {Y}part{WH} of me")
cap("m1", 4.87, 5.63, f"{Y}agrees{WH} with")
cap("m1", 5.66, 5.99, f"{Y}them")
cap("m3", .18, .80, "It's not their")
cap("m3", .81, 2.01, f"{Y}judgment{WH} hurting you")
cap("m3", 2.24, 3.47, f"It's your own {Y}self-doubt")
cap("m3", 4.46, 5.19, f"{Y}Reframe{WH} it")
cap("m3", 5.76, 6.89, f"and take your\\N{Y}power back")
print(render(clips, segs, E, "reel5.mp4"), round(t, 2))
