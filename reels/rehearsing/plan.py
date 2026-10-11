import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d28/"
S28 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s28/"
S28 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s28/"
sys.path.insert(0, S28)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (790, 880)   # tight framing, mic close; zooms kept small (mouth looks too big when close)
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("a", "c", "d", "b")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - hook (a), the loop (c, a little B&W), the truth (d), the way out (b)
S = [("a", .64, 1.56, 1.0, 0, 1, 0), ("a", 1.64, 4.04, 1.1, 0, 0, 0), ("a", 4.20, 4.52, 1.18, 0, 0, 0), ("a", 5.08, 5.56, 1.18, 0, 0, 1),
     ("c", .72, 1.92, 1.0, 0, 1, 0), ("c", 2.20, 2.88, 1.12, 1, 0, 0), ("c", 3.24, 4.16, 1.05, 1, 0, 0), ("c", 4.64, 5.96, 1.12, 0, 0, 0), ("c", 6.04, 7.16, 1.05, 0, 0, 1),
     ("d", .40, 1.36, 1.0, 0, 1, 0), ("d", 1.76, 2.58, 1.15, 0, 0, 0), ("d", 2.58, 4.80, 1.05, 0, 0, 0), ("d", 5.08, 6.28, 1.12, 0, 0, 1),
     ("b", .36, 1.20, 1.0, 0, 1, 0), ("b", 1.40, 2.28, 1.1, 0, 0, 0), ("b", 2.68, 3.80, 1.05, 0, 0, 0), ("b", 4.32, 5.40, 1.15, 0, 0, 0), ("b", 5.76, 6.76, 1.05, 0, 0, 1)]
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
# a hook
cap("a", .64, 1.55, f"You {K('rehearsed')} a")
cap("a", 1.64, 2.45, K("30 second"))
cap("a", 2.46, 3.05, "phone call")
cap("a", 3.06, 4.03, f"{K('10 times')}")
pop("a", 4.20, 4.51, "10")
pop("a", 5.08, 5.55, f"{Y}10")
# c the loop
cap("c", .72, 1.91, f"You wrote\\Nthe {K('text')}")
cap("c", 2.20, 2.87, f"{K('deleted')} it")
cap("c", 3.24, 4.15, f"{K('rewrote')} it")
cap("c", 4.64, 5.20, "then asked")
cap("c", 5.21, 5.95, f"a {K('friend')}")
cap("c", 6.04, 6.70, "if it sounds")
cap("c", 6.71, 7.15, K("okay"))
# d the truth
cap("d", .40, .85, "That's not")
cap("d", .86, 1.35, f"being {K('careful')}")
cap("d", 1.76, 2.57, "That's not")
cap("d", 2.58, 3.30, K("trusting"))
cap("d", 3.31, 4.00, f"your own {K('voice')}")
cap("d", 4.01, 4.79, "to handle")
cap("d", 5.08, 5.70, "a normal")
cap("d", 5.71, 6.27, K("moment"))
# b the way out
cap("b", .36, 1.19, f"So {K('next time')}")
cap("b", 1.40, 2.27, f"send it {K('messy')}")
cap("b", 2.68, 2.95, "say it")
cap("b", 2.96, 3.79, K("imperfect"))
cap("b", 4.32, 4.90, f"The {K('world')}")
cap("b", 4.91, 5.39, f"won't {K('end')}")
cap("b", 5.76, 6.40, f"but the {K('rehearsing')}")
cap("b", 6.41, 6.75, K("will"))
print(render(clips, segs, E, S28 + "reel.mp4"), round(TOTAL, 2))
