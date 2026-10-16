import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d32/"
S32 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s32/"
sys.path.insert(0, S32)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (650, 800)   # vintage look: tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("d", "c", "a", "b", "e")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - scrolling (d), self-doubt (c, a little B&W), their highlight reel (a), being lost (b), your timeline (e)
S = [("d", .02, 1.76, 1.0, 0, 1, 0), ("d", 1.88, 3.08, 1.1, 0, 0, 0), ("d", 3.68, 4.08, 1.18, 0, 0, 0), ("d", 4.88, 5.52, 1.12, 0, 0, 0), ("d", 6.00, 6.60, 1.18, 0, 0, 1),
     ("c", .68, 2.32, 1.0, 0, 1, 0), ("c", 2.68, 3.56, 1.15, 1, 0, 0), ("c", 4.68, 6.16, 1.05, 1, 0, 1),
     ("a", .20, 2.00, 1.0, 0, 1, 0), ("a", 2.00, 3.60, 1.1, 0, 0, 0), ("a", 3.60, 5.28, 1.05, 0, 0, 0), ("a", 5.32, 6.56, 1.15, 0, 0, 1),
     ("b", .40, 1.76, 1.0, 0, 1, 0), ("b", 2.04, 3.60, 1.1, 0, 0, 0), ("b", 4.36, 7.08, 1.05, 0, 0, 1),
     ("e", .56, 3.96, 1.0, 0, 1, 0), ("e", 4.76, 6.64, 1.12, 0, 0, 1)]
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
# d scrolling
cap("d", .02, 1.15, f"{K('Scroll')} for\\N{K('five minutes')}")
cap("d", 1.16, 1.75, f"and you'll\\Nbelieve")
cap("d", 1.88, 2.55, f"{K('Everyone')} has it")
cap("d", 2.56, 3.07, "figured out.")
cap("d", 3.68, 4.07, f"The {K('job')},")
cap("d", 4.88, 5.51, f"the {K('partner')},")
cap("d", 6.00, 6.59, f"the {K('plan')}.")
# c self-doubt
cap("c", .68, 1.20, "Then you\\Nlook")
cap("c", 1.21, 1.90, f"at your own\\N{K('life')}")
cap("c", 1.91, 2.31, "and think,")
pop("c", 2.68, 3.55, f"WHAT'S WRONG\\N{Y}WITH ME?")
cap("c", 4.68, 5.20, "Why am I")
cap("c", 5.21, 6.15, f"still {K('figuring')}\\Nit out?")
# a their highlight reel
cap("a", .20, .90, f"But {K('nobody')}\\Nposts")
cap("a", .91, 1.40, f"the {K('panic')}")
cap("a", 1.41, 1.99, "at 2 a.m.")
cap("a", 2.00, 2.70, f"{K('Nobody')} posts")
cap("a", 2.71, 3.59, f"the {K('rejection')}\\Nemails.")
cap("a", 3.60, 4.40, f"You're\\N{K('comparing')}")
cap("a", 4.41, 5.27, f"your {K('raw')}")
cap("a", 5.32, 6.00, f"{K('footage')} to\\Ntheir")
pop("a", 6.04, 6.55, f"FINAL\\N{Y}CUT.")
# b being lost
cap("b", .40, 1.00, f"Being {K('lost')}")
cap("b", 1.01, 1.75, f"isn't {K('failure')},")
cap("b", 2.04, 2.70, "it's the part")
cap("b", 2.71, 3.59, f"before the\\N{K('finding')}.")
cap("b", 4.36, 5.20, f"{K('Everyone')} you\\N{K('admire')}")
cap("b", 5.21, 5.80, "was once")
cap("b", 5.81, 7.07, f"exactly where\\Nyou are.")
# e your timeline
cap("e", .56, 1.50, f"So stop\\N{K('measuring')}")
cap("e", 1.51, 2.50, f"your {K('behind')}\\N{K('the scenes')}")
cap("e", 2.51, 3.10, "against\\Ntheir")
cap("e", 3.11, 3.95, f"{K('highlights')}.")
pop("e", 4.76, 5.50, f"YOUR\\N{Y}TIMELINE")
cap("e", 5.51, 6.63, f"is still being\\N{K('written')}.")
print(render(clips, segs, E, S32 + "reel.mp4"), round(TOTAL, 2))
