import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d37/"
S37 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s37/"
sys.path.insert(0, S37)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look; tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("q1", "q2", "q3", "q4")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - Day 3 product: reading isn't practicing (q1 a little B&W), small reps, free lesson
S = [("q1", .05, 2.40, 1.0, 0, 1, 0), ("q1", 2.40, 4.44, 1.1, 1, 0, 1),
     ("q2", .56, 1.36, 1.0, 0, 1, 0), ("q2", 2.00, 3.64, 1.1, 0, 0, 0), ("q2", 3.72, 5.96, 1.05, 0, 0, 1),
     ("q3", .48, 1.84, 1.0, 0, 1, 0), ("q3", 2.16, 4.84, 1.1, 0, 0, 0), ("q3", 5.08, 6.20, 1.15, 0, 0, 1),
     ("q4", .28, 1.92, 1.0, 0, 1, 0), ("q4", 2.28, 4.48, 1.15, 0, 0, 0), ("q4", 4.68, 6.00, 1.05, 0, 0, 1)]
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
# q1 hook
cap("q1", .05, 1.40, f"You've read\\N{K('10 posts')}")
cap("q1", 1.41, 2.39, f"about\\N{K('self-doubt')}")
cap("q1", 2.40, 3.30, "this month")
cap("q1", 3.31, 4.43, f"and {K('nothing really')}\\N{K('changed')}.")
# q2 reading vs practicing
cap("q2", .56, 1.35, f"That's {K('because')}")
cap("q2", 2.00, 3.63, f"reading about\\N{K('confidence')}")
cap("q2", 3.72, 4.60, "is not the same")
cap("q2", 4.61, 5.95, f"as {K('practicing')} it.")
# q3 small reps
cap("q3", .48, 1.83, f"{K('Self-trust')} is a skill,")
cap("q3", 2.16, 3.20, "and skills are built")
cap("q3", 3.21, 4.83, f"with {K('small daily reps')},")
cap("q3", 5.08, 6.19, f"not {K('motivation')}.")
# q4 the free lesson
cap("q4", .28, 1.91, f"I made a {K('free lesson')}\\Nfor this.")
pop("q4", 2.28, 4.47, f"COMMENT\\N{Y}TRUST")
cap("q4", 4.68, 5.99, "and I'll send\\Nit to you.")
print(render(clips, segs, E, S37 + "reel.mp4"), round(TOTAL, 2))
