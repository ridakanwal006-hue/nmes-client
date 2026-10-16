import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d31/"
S31 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s31/"
sys.path.insert(0, S31)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look; tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("c", "b", "d", "a")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - five opinions (c), outsourcing (b), self-trust (d), decide (a)
S = [("c", .36, 1.84, 1.0, 0, 1, 0), ("c", 2.40, 3.72, 1.1, 0, 0, 0), ("c", 4.40, 5.84, 1.18, 1, 0, 1),
     ("b", .52, 2.80, 1.0, 0, 1, 0), ("b", 2.92, 6.64, 1.1, 0, 0, 1),
     ("d", .40, 2.80, 1.0, 0, 1, 0), ("d", 3.56, 4.88, 1.12, 0, 0, 0), ("d", 5.36, 6.60, 1.18, 0, 0, 1),
     ("a", .36, 1.20, 1.0, 0, 1, 0), ("a", 1.32, 3.28, 1.1, 0, 0, 0), ("a", 3.52, 4.98, 1.15, 0, 0, 0), ("a", 5.20, 6.68, 1.05, 1, 0, 1)]
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
# c five opinions
cap("c", .36, 1.10, f"You asked {K('five')}\\Npeople")
cap("c", 1.11, 1.83, f"what to {K('do')}.")
cap("c", 2.40, 2.90, f"Got {K('five')}")
cap("c", 2.91, 3.71, f"different\\N{K('answers')}.")
pop("c", 4.40, 5.30, f"MORE\\N{Y}CONFUSED")
cap("c", 5.31, 5.83, "than before.")
# b outsourcing
cap("b", .52, 1.20, "That's what\\Nhappens")
cap("b", 1.21, 2.00, f"when you\\N{K('outsource')}")
cap("b", 2.01, 2.79, f"your {K('decisions')}.")
cap("b", 2.92, 4.00, f"You {K('collect')}\\Nopinions")
cap("b", 4.01, 5.45, "hoping one\\Nof them")
cap("b", 5.48, 6.63, f"feels like\\N{K('certainty')}.")
# d self-trust
cap("d", .40, 1.70, f"But no amount\\Nof {K('advice')}")
cap("d", 1.71, 2.79, f"replaces\\N{K('self-trust')}.")
cap("d", 3.56, 4.87, f"You already know\\Nwhat you {K('want')}.")
pop("d", 5.36, 6.59, f"YOU'RE JUST\\N{Y}SCARED TO OWN IT.")
# a decide
cap("a", .36, 1.19, f"So {K('decide')}.")
cap("a", 1.32, 2.55, f"One {K('voice')}\\Nmatters here,")
pop("a", 2.56, 3.27, "YOURS.")
cap("a", 3.52, 4.97, f"Wrong decisions\\N{K('teach')}.")
pop("a", 5.20, 6.67, f"NO DECISIONS\\N{Y}JUST TRAP.")
print(render(clips, segs, E, S31 + "reel.mp4"), round(TOTAL, 2))
