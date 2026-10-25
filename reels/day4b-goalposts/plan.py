import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d39/"
S39 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s39/"
sys.path.insert(0, S39)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look; tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("g1", "g2", "g3", "g4", "g5", "g6")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - Day 4 part 2, moving the goalposts; cut only inside the speech, never the music/noise tails
S = [("g1", .20, 2.56, 1.0, 0, 1, 0), ("g1", 2.96, 4.72, 1.12, 0, 0, 1),
     ("g2", .44, 3.72, 1.0, 0, 1, 0), ("g2", 4.08, 5.72, 1.1, 0, 0, 1),
     ("g3", .36, 1.76, 1.0, 0, 1, 0), ("g3", 2.24, 3.80, 1.12, 0, 0, 1),
     ("g4", .44, 1.64, 1.0, 0, 1, 0), ("g4", 1.96, 2.96, 1.1, 0, 0, 0), ("g4", 3.36, 5.00, 1.15, 1, 0, 1),
     ("g5", .40, 2.32, 1.0, 0, 1, 0), ("g5", 2.60, 3.68, 1.1, 0, 0, 1),
     ("g6", .32, 1.64, 1.05, 0, 1, 0), ("g6", 2.28, 5.04, 1.0, 0, 0, 1)]
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
# g1 part two hook
pop("g1", .20, .90, f"PART {Y}TWO.")
cap("g1", 1.04, 2.55, f"You do exactly\\Nwhat {K('they asked')},")
cap("g1", 2.96, 4.71, f"and suddenly the\\N{K('rules change')}.")
# g2 yesterday / today
cap("g2", .48, 1.56, "Yesterday\\Nit was...")
cap("g2", 1.68, 2.44, f"{K('clean the kitchen')}.")
cap("g2", 2.60, 3.71, f"{K('Today')}, it's...")
cap("g2", 4.08, 5.23, f"Why didn't you\\Nthink of it")
cap("g2", 5.24, 5.71, f"{K('first')}?")
# g3 the name
cap("g3", .36, 1.75, f"It's called\\N{K('moving the goalposts')},")
cap("g3", 2.24, 3.79, f"and it makes sure\\Nyou can {K('never win')}.")
# g4 the effect
cap("g4", .44, 1.63, f"You start trying\\N{K('harder')},")
cap("g4", 1.96, 2.95, f"{K('explaining')} more,")
cap("g4", 3.36, 4.99, f"and {K('shrinking')}\\Na little every time.")
# g5 the fix
cap("g5", .40, 1.63, f"Ask them to name\\Nwhat {K('enough')}")
cap("g5", 1.72, 2.31, f"{K('looks like')},")
cap("g5", 2.60, 3.67, f"and watch how\\Nthey {K('answer')}.")
# g6 follow CTA
pop("g6", .32, 1.63, f"FOLLOW FOR\\N{Y}PART THREE.")
cap("g6", 2.28, 3.19, f"The last {K('trick')}")
cap("g6", 3.52, 5.03, f"is the one\\N{K('nobody talks about')}.")
E.cap(10.3, 12.3, f"Follow for the {K('next part')}", y=1640)
print(render(clips, segs, E, S39 + "reel.mp4"), round(TOTAL, 2))
