import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d7/"
sys.path.insert(0, "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s7")
from reel_style import Clip, Seg, Events, render, Y, WH

CR = "720:964:0:200"
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=(838, 520)) for k in ("p4", "p1", "p2", "p3")}
# (clip, start, end, zoom, bw, fade_in, fade_out)
S = [("p4", .66, 1.42, 1.0, 0, 0, 0), ("p4", 1.42, 2.86, 1.3, 0, 0, 1),
     ("p1", .22, .98, 1.0, 0, 1, 0), ("p1", .98, 1.90, 1.25, 0, 0, 0), ("p1", 1.90, 2.84, 1.12, 0, 0, 0),
     ("p1", 3.82, 4.84, 1.3, 0, 0, 0), ("p1", 4.86, 5.58, 1.45, 0, 0, 1),
     ("p2", .90, 2.08, 1.0, 0, 1, 0), ("p2", 2.40, 3.94, 1.25, 0, 0, 0), ("p2", 4.70, 6.04, 1.12, 0, 0, 0), ("p2", 6.06, 6.68, 1.45, 0, 0, 1),
     ("p3", .26, 1.42, 1.0, 1, 1, 0), ("p3", 1.44, 2.84, 1.25, 1, 0, 0), ("p3", 3.06, 3.86, 1.12, 0, 0, 0),
     ("p3", 4.58, 5.28, 1.3, 0, 0, 0), ("p3", 6.10, 6.80, 1.45, 0, 0, 1)]
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
cap("p4", .66, 1.41, f"{Y}Here's{WH} a sentence")
cap("p4", 1.42, 2.16, f"I {Y}wish{WH} I'd heard")
cap("p4", 2.17, 2.85, f"{Y}years ago")
cap("p1", .22, .97, f"You made the {Y}best")
cap("p1", .98, 1.89, f"{Y}call{WH} you could with")
cap("p1", 1.90, 2.83, f"what you {Y}knew{WH} then")
cap("p1", 3.82, 4.83, f"That's not {Y}failure")
pop("p1", 4.86, 5.57, f"BEING\\N{Y}HUMAN")
cap("p2", .90, 2.07, f"{Y}Forgive{WH} yourself")
cap("p2", 2.40, 3.93, f"for not knowing\\N{Y}earlier")
cap("p2", 4.70, 6.03, f"what only {Y}time{WH} could")
pop("p2", 6.06, 6.67, f"TEACH\\N{Y}YOU")
cap("p3", .26, 1.41, f"Stop {Y}punishing{WH} yourself")
cap("p3", 1.44, 2.83, f"for old {Y}versions{WH}\\Nof you")
cap("p3", 3.06, 3.85, f"They didn't {Y}know{WH} yet")
cap("p3", 4.58, 5.27, f"Now you {Y}do")
pop("p3", 6.10, 6.79, f"MOVE LIKE\\N{Y}IT")
print(render(clips, segs, E, "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s7/reel7.mp4"), round(t, 2))
