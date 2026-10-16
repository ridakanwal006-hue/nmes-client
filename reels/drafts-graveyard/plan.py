import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d30/"
S30 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s30/"
sys.path.insert(0, S30)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look; tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("b", "d", "c", "a")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - the graveyard (b), why (d), the truth (c), do it (a)
S = [("b", .20, 2.08, 1.0, 0, 1, 0), ("b", 2.56, 3.72, 1.12, 0, 0, 0), ("b", 3.96, 5.36, 1.05, 1, 0, 0), ("b", 5.80, 6.88, 1.18, 0, 0, 1),
     ("d", .08, .76, 1.0, 0, 1, 0), ("d", .88, 2.36, 1.1, 0, 0, 0), ("d", 2.76, 4.28, 1.05, 1, 0, 0), ("d", 4.72, 6.80, 1.15, 0, 0, 1),
     ("c", .28, 3.04, 1.0, 0, 1, 0), ("c", 4.00, 5.84, 1.1, 0, 0, 1),
     ("a", .28, 1.24, 1.0, 0, 1, 0), ("a", 1.44, 2.48, 1.1, 0, 0, 0), ("a", 2.80, 4.04, 1.18, 0, 0, 0), ("a", 4.44, 5.76, 1.05, 0, 0, 0), ("a", 5.88, 6.68, 1.12, 0, 0, 1)]
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
# b the graveyard
cap("b", .20, 1.10, f"Your {K('drafts')} folder")
cap("b", 1.11, 2.07, f"is a {K('graveyard')}.")
cap("b", 2.56, 3.71, f"{K('Ideas')} you loved,")
cap("b", 3.96, 4.50, "killed by")
cap("b", 4.51, 5.35, f"{K('one question')}.")
pop("b", 5.80, 6.87, f"WHAT WILL\\N{Y}PEOPLE THINK?")
# d why
cap("d", .08, .75, f"You {K('wrote')} it,")
cap("d", .88, 1.50, f"{K('reread')} it,")
cap("d", 1.51, 2.35, f"then {K('deleted')} it.")
cap("d", 2.76, 3.40, "Not because")
cap("d", 3.41, 4.27, f"it was {K('bad')},")
cap("d", 4.72, 5.60, f"because being\\N{K('seen')}")
cap("d", 5.61, 6.79, f"felt {K('dangerous')}.")
# c the truth
cap("c", .28, .85, f"But {K('nobody')}'s")
cap("c", .86, 1.70, f"waiting to\\Njudge you")
cap("c", 1.71, 2.20, f"as {K('hard')} as")
cap("c", 2.21, 3.03, f"you're judging\\N{K('yourself')}.")
cap("c", 4.00, 4.90, f"The {K('world')} is\\Ntoo busy")
cap("c", 4.91, 5.83, f"to {K('care')}\\Nthat much.")
# a do it
cap("a", .28, 1.23, f"So {K('post')} the thing,")
cap("a", 1.44, 2.47, f"{K('share')} the idea,")
pop("a", 2.80, 4.03, f"LET IT BE\\N{Y}IMPERFECT.")
cap("a", 4.44, 5.75, f"{K('Hidden work')}\\Nhelps no one,")
cap("a", 5.88, 6.67, f"least of {K('all')} you.")
print(render(clips, segs, E, S30 + "reel.mp4"), round(TOTAL, 2))
