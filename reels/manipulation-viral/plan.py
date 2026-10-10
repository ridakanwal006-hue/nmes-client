import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d19/"
S19 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s19/"
sys.path.insert(0, S19)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:964:0:150", (660, 540)
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("t4", "t1", "t2", "t3")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - hook first (t4), then the pattern (t1, t2), then the way out (t3)
S = [("t4", .24, 1.00, 1.0, 0, 1, 0), ("t4", 1.00, 2.20, 1.3, 0, 0, 0), ("t4", 2.66, 3.40, 1.12, 0, 0, 0), ("t4", 3.40, 4.20, 1.3, 0, 0, 0),
     ("t4", 4.58, 5.46, 1.4, 0, 0, 0), ("t4", 5.62, 7.00, 1.5, 0, 0, 1),
     ("t1", .56, 1.45, 1.0, 0, 1, 0), ("t1", 1.92, 2.50, 1.25, 0, 0, 0), ("t1", 2.50, 3.92, 1.12, 0, 0, 0), ("t1", 4.24, 5.12, 1.3, 0, 0, 0),
     ("t1", 5.12, 6.05, 1.0, 0, 0, 0), ("t1", 6.12, 7.40, 1.45, 0, 0, 1),
     ("t2", .32, 1.50, 1.0, 0, 1, 0), ("t2", 1.50, 2.40, 1.25, 0, 0, 0), ("t2", 2.40, 3.42, 1.4, 0, 0, 0), ("t2", 3.52, 4.40, 1.12, 0, 0, 0),
     ("t2", 4.40, 5.42, 1.3, 0, 0, 0), ("t2", 5.48, 6.50, 1.0, 0, 0, 0), ("t2", 6.50, 7.38, 1.45, 0, 0, 1),
     ("t3", .40, 1.00, 1.0, 0, 1, 0), ("t3", 1.00, 1.85, 1.35, 0, 0, 0), ("t3", 1.85, 3.30, 1.15, 0, 0, 0), ("t3", 3.30, 4.95, 1.3, 0, 0, 0),
     ("t3", 5.70, 7.20, 1.5, 0, 0, 1)]
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
# retention helpers: top progress bar, "watch till the end" hook, save/share end card
E.ev.append(f"Dialogue: 3,{ts(0)},{ts(TOTAL)},Line,,0,0,0,,{{\\an7\\pos(0,0)\\p1\\1c&H00D7FF&\\fscx0\\t(0,{int(TOTAL * 1000)},\\fscx100)}}m 0 0 l 1080 0 1080 12 0 12{{\\p0}}")
E.label(TOTAL - 2.0, TOTAL - 0.05, "SAVE THIS  -  SHARE IT", x=False, y=130)
# t4 hook
cap("t4", .24, .99, f"If {K('someone')} pushes")
cap("t4", 1.00, 2.19, f"you to your\\N{K('breaking point')}")
cap("t4", 2.66, 3.39, f"then {K('shames')}")
cap("t4", 3.40, 4.19, f"you for {K('breaking')}")
pop("t4", 4.58, 5.45, f"NOT YOUR\\N{Y}FAULT")
pop("t4", 5.62, 6.99, f"THAT'S\\N{Y}MANIPULATION")
# t1 the pattern
cap("t1", .56, 1.44, f"They {K('ignore')} your\\N{K('boundaries')}")
cap("t1", 1.92, 2.49, f"{K('dismiss')} your")
cap("t1", 2.50, 3.91, f"{K('feelings')}, wear\\Nyou {K('down')}")
cap("t1", 4.24, 5.11, f"then use your\\N{K('reaction')}")
cap("t1", 5.12, 6.04, f"as {K('proof')}")
E.label(T("t1", 6.12), T("t1", 7.40) - .01, "THEIR TRICK:", x=True)
cap("t1", 6.12, 7.39, f"that you are\\Nthe {K('problem')}")
# t2 the pattern
cap("t2", .32, 1.49, f"They call you\\Ntoo {K('emotional')}")
cap("t2", 1.50, 2.39, "so they never")
cap("t2", 2.40, 3.41, f"take {K('accountability')}")
cap("t2", 3.52, 4.39, f"and you start\\N{K('doubting')}")
cap("t2", 4.40, 5.41, K("yourself"))
cap("t2", 5.48, 6.49, "instead of seeing")
pop("t2", 6.50, 7.37, f"THE\\N{Y}PATTERN")
# t3 the way out
cap("t3", .40, .99, f"But {K('clarity')}")
cap("t3", 1.00, 1.84, f"destroys\\N{K('manipulation')}")
cap("t3", 1.85, 3.29, f"{K('Trust')} what you saw")
cap("t3", 3.30, 4.94, f"{K('trust')} what you felt")
pop("t3", 5.70, 7.19, f"STOP\\N{Y}TOLERATING IT")
print(render(clips, segs, E, S19 + "reel.mp4"), round(TOTAL, 2))
