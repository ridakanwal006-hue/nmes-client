import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d25/"
S25 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s25/"
sys.path.insert(0, S25)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (790, 880)   # tighter framing: the mic sits close to the camera
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("d", "a", "c", "b")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - hook (d), the fear (a, B&W), the cost (c), the way out (b)
S = [("d", .40, 1.46, 1.12, 0, 1, 0), ("d", 2.36, 4.20, 1.3, 0, 0, 0), ("d", 4.68, 5.76, 1.45, 1, 0, 1),
     ("a", .30, 1.32, 1.12, 0, 1, 0), ("a", 1.72, 2.66, 1.4, 0, 0, 0), ("a", 3.04, 4.14, 1.2, 1, 0, 0), ("a", 4.60, 5.48, 1.35, 1, 0, 0), ("a", 5.96, 7.20, 1.25, 1, 0, 1),
     ("c", .30, 2.74, 1.12, 0, 1, 0), ("c", 3.56, 6.58, 1.3, 0, 0, 1),
     ("b", .40, 2.54, 1.15, 0, 1, 0), ("b", 2.68, 4.06, 1.3, 0, 0, 0), ("b", 4.20, 5.18, 1.2, 0, 0, 0), ("b", 5.84, 6.38, 1.5, 0, 0, 1)]
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
# d hook
cap("d", .40, 1.05, f"You said {K('yes')}")
cap("d", 1.06, 1.45, "again")
cap("d", 2.36, 3.00, f"and the {K('second')}")
cap("d", 3.01, 3.54, f"the word {K('left')}")
cap("d", 3.55, 4.19, f"your {K('mouth')}")
pop("d", 4.68, 5.75, f"YOUR STOMACH\\N{Y}DROPPED")
# a the fear
cap("a", .30, .85, f"Not {K('because')}")
cap("a", .86, 1.31, f"you're {K('kind')}")
pop("a", 1.72, 2.65, f"BECAUSE YOU'RE\\N{Y}SCARED")
cap("a", 3.04, 3.70, f"{K('Scared')} they'll")
cap("a", 3.71, 4.13, f"be {K('upset')}")
cap("a", 4.60, 5.47, f"{K('Scared')} they'll\\N{K('leave')}")
cap("a", 5.96, 7.19, f"{K('Scared')} of seeming\\N{K('difficult')}")
# c the cost
cap("c", .30, .95, f"Every {K('yes')}")
cap("c", .96, 1.70, f"you don't {K('mean')}")
cap("c", 1.71, 2.20, f"is a {K('no')}")
cap("c", 2.21, 2.73, "to yourself")
cap("c", 3.56, 4.55, f"and {K('resentment')}\\Nis just")
cap("c", 4.56, 5.20, K("unspoken"))
cap("c", 5.21, 5.89, "boundaries")
cap("c", 5.90, 6.57, f"{K('piling')} up")
# b the way out
cap("b", .40, 1.15, f"{K('No')} is a")
pop("b", 1.16, 2.53, f"COMPLETE\\N{Y}SENTENCE")
cap("b", 2.68, 4.05, f"the people who\\N{K('respect')} you")
cap("b", 4.20, 5.17, f"won't {K('leave')}\\Nover it")
pop("b", 5.84, 6.37, f"TRUST\\N{Y}THAT")
print(render(clips, segs, E, S25 + "reel.mp4"), round(TOTAL, 2))
