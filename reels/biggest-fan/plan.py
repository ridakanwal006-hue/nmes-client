import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d21/"
S21 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s21/"
sys.path.insert(0, S21)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (650, 720)
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("c3", "c2", "c1", "c4")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - hook (c3), the test (c2), the root (c1), the choice (c4)
S = [("c3", .50, 1.18, 1.0, 0, 1, 0), ("c3", 1.18, 2.38, 1.25, 0, 0, 0), ("c3", 2.40, 3.30, 1.45, 0, 0, 0), ("c3", 3.78, 5.14, 1.15, 0, 0, 1),
     ("c2", .50, 2.82, 1.0, 0, 1, 0), ("c2", 2.84, 4.60, 1.3, 0, 0, 0), ("c2", 5.46, 6.60, 1.5, 0, 0, 1),
     ("c1", .40, 1.50, 1.0, 0, 1, 0), ("c1", 1.96, 3.66, 1.3, 0, 0, 0), ("c1", 3.70, 6.30, 1.12, 0, 0, 1),
     ("c4", .30, 1.12, 1.0, 0, 1, 0), ("c4", 1.12, 3.92, 1.3, 0, 0, 0), ("c4", 4.40, 7.16, 1.15, 0, 0, 1)]
segs, off, t = [], [], 0.0
for c, a, b, z, bw, fi, fo in S:
    segs.append(Seg(c, a, b, z, bool(bw), bool(fi), bool(fo))); off.append((c, a, b, t)); t += b - a
TOTAL = t

def T(c, s):
    for cc, a, b, o in off:
        if cc == c and a - 1e-6 <= s <= b + 1e-6: return o + s - a
    raise ValueError((c, s))

K = lambda w: "{\\fs104}" + Y + w + "{\\fs80}" + WH
E = Events()
def cap(c, a, b, text, **k): E.cap(T(c, a), T(c, b) - .01, text, **k)
def pop(c, a, b, text, **k): E.pop(T(c, a), T(c, b) - .01, text, **k)
E.ev.append(f"Dialogue: 3,{ts(0)},{ts(TOTAL)},Line,,0,0,0,,{{\\an7\\pos(0,0)\\p1\\1c&H00D7FF&\\fscx0\\t(0,{int(TOTAL * 1000)},\\fscx100)}}m 0 0 l 1080 0 1080 12 0 12{{\\p0}}")
E.label(TOTAL - 2.0, TOTAL - 0.05, "SAVE THIS  -  SHARE IT", x=False, y=130)
# c3 hook
cap("c3", .50, 1.17, "You need to")
cap("c3", 1.18, 2.37, f"be your\\N{K('partner' + chr(39) + 's')}")
pop("c3", 2.40, 3.29, f"BIGGEST\\N{Y}FAN")
cap("c3", 3.78, 4.35, "I mean that")
cap("c3", 4.36, 5.13, f"with my\\N{K('whole heart')}")
# c2 the test
cap("c2", .50, 1.35, "If you don't want")
cap("c2", 1.36, 1.72, f"their {K('dreams')}")
cap("c2", 1.73, 2.81, f"to come {K('true')}")
cap("c2", 2.84, 3.75, f"if you can't\\N{K('celebrate')}")
cap("c2", 3.76, 4.59, f"their {K('wins')}")
pop("c2", 5.46, 6.59, f"ASK YOURSELF\\N{Y}WHY?")
# c1 the root
cap("c1", .40, 1.49, "And if you can't be")
cap("c1", 1.96, 2.82, "check in on your")
cap("c1", 2.83, 3.65, K("insecurities"))
cap("c1", 3.70, 4.71, f"because that's\\N{K('usually')}")
cap("c1", 4.72, 6.29, f"what's really\\Ngoing on")
# c4 the choice
cap("c4", .30, 1.11, "Either face your")
cap("c4", 1.12, 1.94, K("insecurities"))
cap("c4", 1.95, 2.75, "or admit")
cap("c4", 2.76, 3.19, "you chose")
cap("c4", 3.20, 3.91, f"the {K('wrong person')}")
cap("c4", 4.40, 5.92, f"But don't promise\\N{K('a lifetime')}")
cap("c4", 5.93, 7.15, f"to someone you\\N{K('can' + chr(39) + 't root for')}")
print(render(clips, segs, E, S21 + "reel.mp4"), round(TOTAL, 2))
