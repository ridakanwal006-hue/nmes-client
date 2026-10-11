import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d27/"
S27 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s27/"
S27 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s27/"
sys.path.insert(0, S27)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (790, 880)   # tight framing, mic close to the camera
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("c", "a", "b", "d")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - hook (c, a little B&W), proof (a), evidence (b), the ending (d)
S = [("c", .84, 2.60, 1.0, 1, 1, 0), ("c", 3.24, 4.12, 1.15, 0, 0, 1),
     ("a", .40, 1.20, 1.0, 0, 1, 0), ("a", 1.28, 2.80, 1.1, 0, 0, 0), ("a", 2.84, 4.36, 1.18, 0, 0, 0), ("a", 4.44, 6.24, 1.05, 0, 0, 1),
     ("b", .60, 1.52, 1.0, 1, 1, 0), ("b", 1.88, 3.40, 1.1, 0, 0, 0), ("b", 4.20, 5.52, 1.05, 0, 0, 1),
     ("d", .28, 2.24, 1.0, 0, 1, 0), ("d", 3.44, 4.60, 1.12, 0, 0, 0), ("d", 4.60, 6.20, 1.05, 0, 0, 1)]
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
# c hook
cap("c", .84, 1.40, f"For the {K('days')}")
cap("c", 1.41, 2.00, f"you {K('doubt')}")
cap("c", 2.01, 2.59, K("yourself"))
pop("c", 3.24, 4.11, f"REMEMBER\\N{Y}THIS")
# a proof
cap("a", .40, 1.19, f"you've {K('survived')}")
cap("a", 1.28, 2.10, f"every {K('hard')} day")
cap("a", 2.11, 2.79, f"so {K('far')}")
pop("a", 2.84, 4.35, f"EVERY SINGLE\\N{Y}ONE")
cap("a", 4.44, 5.20, f"That's {K('100%')}")
cap("a", 5.21, 6.23, f"success {K('rate')}")
# b evidence
cap("b", .60, 1.51, f"Doubt is {K('loud')}")
cap("b", 1.88, 2.72, f"but {K('evidence')}")
cap("b", 2.76, 3.39, f"is {K('louder')}")
cap("b", 4.20, 4.70, f"Come {K('back')}")
cap("b", 4.71, 5.20, "to this when you")
cap("b", 5.21, 5.51, K("forget"))
# d ending
cap("d", .28, 1.20, f"the {K('version')} of you")
cap("d", 1.21, 1.80, f"that you're {K('scared')}")
cap("d", 1.81, 2.23, f"to {K('become')}")
cap("d", 3.44, 4.00, f"{K('someone')} already")
cap("d", 4.01, 4.59, K("admires"))
cap("d", 4.60, 5.20, f"the {K('version')}")
cap("d", 5.21, 6.19, f"you are {K('right now')}")
print(render(clips, segs, E, S27 + "reel.mp4"), round(TOTAL, 2))
