import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d35/"
S35 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s35/"
sys.path.insert(0, S35)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look; tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("x3", "x1", "x2")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - Day 1 Gaslighting: hook (x3), how it works (x1, a little B&W), what to do (x2)
S = [("x3", .28, 2.96, 1.0, 0, 1, 0), ("x3", 3.12, 4.20, 1.12, 0, 0, 0), ("x3", 4.84, 5.68, 1.18, 0, 0, 1),
     ("x1", .64, 2.90, 1.0, 1, 1, 0), ("x1", 2.96, 4.72, 1.1, 0, 0, 1),
     ("x2", .40, 1.20, 1.0, 0, 1, 0), ("x2", 1.96, 3.52, 1.1, 0, 0, 0), ("x2", 4.24, 5.72, 1.15, 0, 0, 1)]
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
# x3 the hook
cap("x3", .28, 1.30, "If they keep\\Nsaying")
cap("x3", 1.31, 2.20, f"you're\\N{K('remembering')}")
cap("x3", 2.21, 2.95, f"it {K('wrong')},")
cap("x3", 3.12, 4.19, f"That's not\\N{K('confusion')}.")
pop("x3", 4.84, 5.67, f"THAT'S\\N{Y}CONTROL.")
# x1 how it works
cap("x1", .64, 1.30, f"They {K('deny')}")
cap("x1", 1.31, 2.00, f"what {K('happened')}")
cap("x1", 2.01, 2.89, "until you")
cap("x1", 2.96, 3.80, f"{K('trust')} their {K('memory')}")
cap("x1", 3.81, 4.71, f"more than\\Nyour {K('own')}.")
# x2 what to do
cap("x2", .40, 1.19, f"{K('Write')} it down.")
cap("x2", 1.96, 3.51, f"Your {K('memory')}\\Nisn't the {K('problem')}.")
pop("x2", 4.24, 5.71, f"THEIR STORY\\N{Y}KEEPS CHANGING.")
print(render(clips, segs, E, S35 + "reel.mp4"), round(TOTAL, 2))
