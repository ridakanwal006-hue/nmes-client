import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d33/"
S33 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s33/"
sys.path.insert(0, S33)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look; tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("x2", "x3", "x1")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - Quiet Rules #1: the unsent draft (x2, x3), the rule (x1)
S = [("x2", .52, 1.64, 1.0, 0, 1, 0), ("x2", 2.16, 3.48, 1.1, 0, 0, 0), ("x2", 3.76, 4.80, 1.15, 0, 0, 0), ("x2", 5.24, 6.80, 1.05, 0, 0, 1),
     ("x3", .52, 2.32, 1.0, 0, 1, 0), ("x3", 2.72, 5.64, 1.08, 1, 0, 1),
     ("x1", .20, .88, 1.0, 0, 1, 0), ("x1", 1.36, 2.64, 1.15, 0, 0, 0), ("x1", 3.24, 4.20, 1.05, 0, 0, 0), ("x1", 4.32, 5.76, 1.18, 0, 0, 1)]
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
# series labels (top): title of the reel, then the rule number
E.label(T("x1", .20) + .05, TOTAL - .05, "THE QUIET RULES  -  RULE 1", x=False, y=130)
# x2 the draft
cap("x2", .52, 1.64, f"You {K('type')} the\\Nmessage,")
cap("x2", 2.16, 3.48, f"read it {K('five')} times,")
cap("x2", 3.76, 4.80, f"change {K('one word')},")
cap("x2", 5.24, 6.80, f"then {K('close')} the app.")
# x3 an hour later
cap("x3", .52, 1.40, "An hour later")
cap("x3", 1.41, 2.31, f"you opened it\\N{K('again')},")
cap("x3", 2.72, 3.50, f"still {K('staring')}")
cap("x3", 3.51, 4.50, f"at the same\\N{K('grey')},")
cap("x3", 4.51, 5.63, f"{K('unsent')} text.")
# x1 the rule
cap("x1", .20, .87, f"{K('Rule 1')},")
cap("x1", 1.36, 2.63, f"send the {K('rough')}\\Nversion.")
cap("x1", 3.24, 4.19, f"{K('Rough')} and sent")
cap("x1", 4.32, 5.75, f"beats {K('perfect')}\\Nand {K('stuck')}.")
print(render(clips, segs, E, S33 + "reel.mp4"), round(TOTAL, 2))
