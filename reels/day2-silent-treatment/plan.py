import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d36/"
S36 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s36/"
sys.path.insert(0, S36)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look; tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("p4", "p1", "p5", "p2", "p3")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - Day 2 silent treatment: hook (p4), the pattern (p1, p5 a little B&W, p2), the rule (p3)
S = [("p4", .56, 2.56, 1.0, 0, 1, 0), ("p4", 3.16, 4.32, 1.1, 0, 0, 0), ("p4", 5.48, 6.28, 1.18, 0, 0, 1),
     ("p1", .44, 1.52, 1.0, 0, 1, 0), ("p1", 1.80, 3.84, 1.08, 0, 0, 0), ("p1", 3.88, 5.40, 1.15, 0, 0, 1),
     ("p5", .10, 3.00, 1.0, 1, 1, 0), ("p5", 3.04, 4.70, 1.12, 1, 0, 1),
     ("p2", .64, 2.24, 1.0, 0, 1, 0), ("p2", 2.80, 4.96, 1.1, 0, 0, 1),
     ("p3", .52, 2.88, 1.0, 0, 1, 0), ("p3", 3.72, 6.24, 1.12, 0, 0, 1)]
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
# p4 hook
cap("p4", .56, 1.50, f"When someone\\N{K('goes silent')}")
cap("p4", 1.51, 2.55, f"to {K('punish')} you,")
cap("p4", 3.16, 4.31, f"that's not {K('space')}.")
pop("p4", 5.48, 6.27, f"THAT'S\\N{Y}A WEAPON.")
# p1 the pattern
cap("p1", .44, 1.51, f"They stop\\N{K('answering')},")
cap("p1", 1.80, 2.50, "and suddenly")
cap("p1", 2.51, 3.10, "you're the one")
cap("p1", 3.11, 3.83, f"{K('rewriting')}")
cap("p1", 3.88, 4.60, f"every {K('message')}")
cap("p1", 4.61, 5.39, f"you ever {K('sent')}.")
# p5 apologizing (grey)
cap("p5", .10, 1.00, f"You {K('apologized')}")
cap("p5", 1.01, 2.20, f"for something\\Nyou {K('never did')}")
cap("p5", 2.21, 2.99, "just to make")
cap("p5", 3.04, 4.69, f"the {K('quiet')} stop.")
# p2 they act like nothing happened
cap("p2", .64, 1.40, "And the second")
cap("p2", 1.41, 2.23, f"you {K('apologize')},")
cap("p2", 2.80, 3.60, "they act like")
cap("p2", 3.61, 4.95, f"{K('nothing ever happened')}\\Nat all.")
# p3 the rule
cap("p3", .52, 1.50, f"Real {K('peace')}\\Ndoesn't")
cap("p3", 1.51, 2.87, f"require you to {K('beg')}.")
cap("p3", 3.72, 4.60, f"{K('Silence')} used as")
cap("p3", 4.61, 5.40, f"{K('punishment')}")
cap("p3", 5.41, 6.23, f"is {K('control')}.")
print(render(clips, segs, E, S36 + "reel.mp4"), round(TOTAL, 2))
