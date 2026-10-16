import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d29/"
S29 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s29/"
sys.path.insert(0, S29)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look: face is left of centre; mic stays close; zooms kept small
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("b", "d", "a", "c")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - the silence (b), the cause (d), the cost (a), the fix (c)
S = [("b", .40, 1.36, 1.0, 0, 1, 0), ("b", 2.00, 2.92, 1.12, 1, 0, 0), ("b", 3.80, 5.52, 1.05, 0, 0, 1),
     ("d", .32, 1.64, 1.0, 0, 1, 0), ("d", 2.68, 4.92, 1.1, 0, 0, 0), ("d", 5.16, 5.92, 1.18, 1, 0, 1),
     ("a", .28, 2.64, 1.0, 0, 1, 0), ("a", 3.08, 5.40, 1.1, 0, 0, 1),
     ("c", .32, 1.08, 1.0, 0, 1, 0), ("c", 1.56, 2.40, 1.18, 0, 0, 0), ("c", 3.24, 4.44, 1.05, 0, 0, 0), ("c", 5.44, 6.28, 1.15, 0, 0, 1)]
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
# b the silence
cap("b", .40, 1.35, f"You had the {K('answer')}")
cap("b", 2.00, 2.91, f"You stayed {K('silent')}")
cap("b", 3.80, 4.40, f"Then {K('someone else')}")
cap("b", 4.41, 4.90, "said it and got")
cap("b", 4.91, 5.51, f"the {K('credit')}")
# d the cause
cap("d", .32, .85, "Not because")
cap("d", .86, 1.63, f"they were {K('smarter')}")
cap("d", 2.68, 3.30, f"because they {K('trusted')}")
cap("d", 3.31, 3.80, f"their {K('voice')}")
cap("d", 3.81, 4.91, f"enough to {K('use it')}")
pop("d", 5.16, 5.91, f"AND YOU\\N{Y}DIDN'T")
# a the cost
cap("a", .28, 1.00, "Every time you")
cap("a", 1.01, 1.75, f"{K('swallow')} your")
cap("a", 1.76, 2.63, K("idea"))
cap("a", 3.08, 3.60, "you're telling")
cap("a", 3.61, 4.15, K("yourself"))
cap("a", 4.16, 4.80, f"your {K('thoughts')}")
cap("a", 4.81, 5.39, f"aren't worth {K('hearing')}")
# c the fix
cap("c", .32, 1.07, f"So {K('next time')}")
pop("c", 1.56, 2.39, f"SPEAK\\N{Y}FIRST")
cap("c", 3.24, 3.80, "even if your")
cap("c", 3.81, 4.43, K("voice shakes"))
pop("c", 5.44, 6.27, f"ESPECIALLY\\N{Y}THEN")
print(render(clips, segs, E, S29 + "reel.mp4"), round(TOTAL, 2))
