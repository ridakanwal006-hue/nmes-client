import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d26/"
S26 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s26/"
sys.path.insert(0, S26)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (790, 880)   # tight framing, mic close to the camera
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("d", "a", "c", "b")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - the cringe (d), nobody cares (a), the prison (c, a little B&W), freedom (b)
S = [("d", .68, 1.96, 1.12, 0, 1, 0), ("d", 1.98, 3.14, 1.3, 0, 0, 0), ("d", 3.14, 4.20, 1.45, 0, 0, 0), ("d", 4.22, 6.08, 1.2, 0, 0, 1),
     ("a", .28, 1.08, 1.12, 0, 1, 0), ("a", 1.12, 2.96, 1.3, 0, 0, 0), ("a", 3.40, 3.96, 1.5, 0, 0, 0), ("a", 4.28, 5.10, 1.2, 0, 0, 0), ("a", 5.10, 6.00, 1.35, 0, 0, 1),
     ("c", .38, 2.16, 1.12, 1, 1, 0), ("c", 2.60, 5.08, 1.3, 0, 0, 0), ("c", 6.08, 7.10, 1.5, 1, 0, 1),
     ("b", .44, 1.36, 1.12, 0, 1, 0), ("b", 1.88, 2.60, 1.4, 0, 0, 0), ("b", 4.04, 5.28, 1.2, 0, 0, 0), ("b", 5.72, 6.40, 1.35, 0, 0, 1)]
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
# d the cringe
cap("d", .68, 1.35, "You spent")
cap("d", 1.36, 1.95, K("three days"))
cap("d", 1.98, 3.13, f"{K('cringing')}\\Nover a")
pop("d", 3.14, 4.19, f"10-SECOND\\N{Y}MOMENT")
cap("d", 4.22, 4.85, f"{K('everyone')} else")
cap("d", 4.86, 5.30, K("forgot"))
cap("d", 5.31, 5.65, "in 10")
cap("d", 5.66, 6.07, K("seconds"))
# a nobody cares
cap("a", .28, 1.07, f"{K('Nobody')} is")
cap("a", 1.12, 1.95, "thinking about that")
cap("a", 1.96, 2.50, K("embarrassing"))
cap("a", 2.51, 2.95, "thing you did")
pop("a", 3.40, 3.95, "NOBODY")
cap("a", 4.28, 5.09, "They're all too")
cap("a", 5.10, 5.60, K("replaying"))
cap("a", 5.61, 5.99, f"their {K('own')}")
# c the prison
cap("c", .38, 1.40, f"That's the {K('prison')}")
cap("c", 1.41, 2.15, f"of {K('self-doubt')}")
cap("c", 2.60, 3.30, "You think you're")
cap("c", 3.31, 3.94, f"the {K('main character')}")
cap("c", 3.95, 4.50, "in everyone's")
cap("c", 4.51, 5.07, K("judgment"))
pop("c", 6.08, 7.09, f"YOU'RE\\N{Y}NOT")
# b freedom
cap("b", .44, 1.35, f"And that's {K('not sad')}")
pop("b", 1.88, 2.59, f"THAT'S\\N{Y}FREEDOM")
cap("b", 4.04, 4.50, "Live like")
cap("b", 4.51, 5.27, f"{K('nobody' + chr(39) + 's')} watching")
cap("b", 5.72, 6.05, "because")
cap("b", 6.06, 6.39, f"they're {K('not')}")
print(render(clips, segs, E, S26 + "reel.mp4"), round(TOTAL, 2))
