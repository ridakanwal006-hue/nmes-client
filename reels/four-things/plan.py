import sys
sys.path.insert(0, ".")
from reel_style import Clip, Seg, Events, render, Y, WH

CR, FACE = "720:964:0:158", (660, 520)
clips = {k: Clip(f"{k}.mp4", crop=CR, face=FACE) for k in ("d1", "d3", "d2", "d4", "d5")}
# (clip, start, end, zoom, bw, fade_in, fade_out)
S = [("d1", .30, 1.22, 1.0, 0, 0, 0), ("d1", 1.22, 2.84, 1.25, 0, 0, 0), ("d1", 3.66, 4.50, 1.12, 0, 0, 0),
     ("d1", 4.50, 4.92, 1.4, 0, 0, 0), ("d1", 4.92, 5.76, 1.45, 0, 0, 1),
     ("d3", .18, 1.86, 1.0, 1, 1, 0), ("d3", 1.86, 2.84, 1.25, 1, 0, 0), ("d3", 4.26, 5.74, 1.4, 0, 0, 1),
     ("d2", .20, 1.44, 1.12, 1, 1, 0), ("d2", 1.44, 2.50, 1.3, 1, 0, 0), ("d2", 3.22, 4.74, 1.0, 0, 0, 0), ("d2", 4.74, 5.78, 1.4, 0, 0, 1),
     ("d4", .24, .98, 1.12, 0, 1, 0), ("d4", .98, 2.30, 1.3, 1, 0, 0), ("d4", 2.30, 3.30, 1.0, 0, 0, 0), ("d4", 3.30, 4.72, 1.4, 0, 0, 1),
     ("d5", .50, 2.18, 1.25, 0, 1, 0), ("d5", 4.06, 4.50, 1.0, 0, 0, 0), ("d5", 4.50, 5.10, 1.45, 0, 0, 1)]
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
cap("d1", .30, 1.21, f"{Y}Four things")
cap("d1", 1.22, 2.83, f"you need to {Y}stop doing")
cap("d1", 3.66, 4.49, f"{Y}Most people")
cap("d1", 4.50, 4.91, f"{Y}quit before")
pop("d1", 4.92, 5.75, f"NUMBER\\N{Y}FOUR")
cap("d3", .18, 1.85, f"{Y}Stop replaying{WH} the past")
cap("d3", 1.86, 2.83, f"You can't {Y}edit it")
cap("d3", 4.26, 5.73, f"But you can {Y}steal\\Nits lessons")
cap("d2", .20, 1.43, f"{Y}Stop fearing{WH} a future")
cap("d2", 1.44, 2.49, f"that hasn't {Y}happened")
cap("d2", 3.22, 4.73, f"And stop {Y}outsourcing{WH} your")
cap("d2", 4.74, 5.77, f"{Y}happiness{WH} to other people")
cap("d4", .24, .97, f"and {Y}stop")
cap("d4", .98, 2.29, f"{Y}underestimating\\N{WH}yourself")
cap("d4", 2.30, 3.29, f"{Y}Look{WH} at")
cap("d4", 3.30, 4.71, f"{Y}everything{WH} you survived")
cap("d5", .50, 2.17, f"You're {Y}stronger\\N{WH}than your {Y}doubt says")
pop("d5", 4.06, 5.09, f"START ACTING\\N{Y}LIKE IT")
print(render(clips, segs, E, "reel2.mp4"), round(t, 2))
