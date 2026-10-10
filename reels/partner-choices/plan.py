import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d20/"
S20 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s20/"
sys.path.insert(0, S20)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (650, 720)
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("P", "L", "T", "W")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - hook (P), the symptom (L), the cause (T), the choice (W)
S = [("P", .20, 2.50, 1.0, 0, 1, 0), ("P", 2.52, 3.60, 1.3, 0, 0, 0), ("P", 3.66, 6.40, 1.15, 0, 0, 1),
     ("L", .00, 2.54, 1.0, 0, 1, 0), ("L", 3.72, 6.34, 1.25, 0, 0, 1),
     ("T", .24, 2.54, 1.12, 0, 1, 0), ("T", 3.68, 4.74, 1.45, 0, 0, 0), ("T", 5.04, 6.62, 1.2, 0, 0, 1),
     ("W", .48, 3.00, 1.0, 0, 1, 0), ("W", 3.08, 5.82, 1.3, 0, 0, 0), ("W", 6.36, 7.08, 1.5, 0, 0, 1)]
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
E.label(TOTAL - 2.0, TOTAL - 0.05, "SAVE THIS  -  SHARE IT", x=False, y=130)
# P hook
cap("P", .20, 1.29, "You can tell\\Nhow much")
cap("P", 1.30, 1.84, f"someone {K('loves')}")
cap("P", 1.85, 2.49, f"{K('themselves')}\\Nby the")
cap("P", 2.52, 2.85, K("partner"))
cap("P", 2.86, 3.59, "they've chosen")
pop("P", 3.66, 5.25, f"COMPLIMENT\\N{Y}OR INSULT?")
cap("P", 5.26, 6.39, f"how did that\\N{K('land')}")
# L the symptom
cap("L", .00, .95, f"Have you {K('tolerated')}")
cap("L", .96, 1.45, K("treatment"))
cap("L", 1.46, 2.53, f"that doesn't\\Nfeel {K('loving')}")
cap("L", 3.72, 4.45, "That's not what")
cap("L", 4.46, 5.04, f"someone who {K('loves')}")
cap("L", 5.05, 5.74, K("themselves"))
cap("L", 5.75, 6.33, "puts up with")
# T the cause
cap("T", .24, .85, f"We {K('accept')}")
cap("T", .86, 1.60, "the treatment we")
cap("T", 1.61, 1.95, f"{K('think')} we")
cap("T", 1.96, 2.53, K("deserve"))
pop("T", 3.68, 4.73, f"DOUBT YOUR\\N{Y}WORTH")
cap("T", 5.04, 5.80, f"and you'll {K('doubt')}")
cap("T", 5.81, 6.20, "you deserve")
cap("T", 6.21, 6.61, K("better"))
# W the choice
cap("W", .48, .99, f"So {K('choose')}")
cap("W", 1.00, 1.65, "like a man")
cap("W", 1.66, 2.05, "who loves")
cap("W", 2.06, 2.99, K("himself"))
cap("W", 3.08, 3.95, f"The {K('right')}\\Nperson")
cap("W", 3.96, 4.60, "doesn't make you")
cap("W", 4.61, 5.15, K("question"))
cap("W", 5.16, 5.81, f"your {K('worth')}")
pop("W", 6.36, 7.07, f"THEY CONFIRM\\N{Y}IT")
print(render(clips, segs, E, S20 + "reel.mp4"), round(TOTAL, 2))
