import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d24/"
S24 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s24/"
sys.path.insert(0, S24)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

# framing is a little tighter than the other reels so the mic sits closer to the camera
CR, FACE = "720:962:0:40", (790, 880)
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("d", "a", "b", "c")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - 3 a.m. hook (d), the replay (a), the real reason (b), tonight's fix (c)
S = [("d", .28, 1.26, 1.12, 0, 1, 0), ("d", 1.62, 2.50, 1.3, 0, 0, 0), ("d", 3.44, 4.26, 1.45, 0, 0, 0), ("d", 4.40, 6.78, 1.2, 0, 0, 1),
     ("a", .10, 2.12, 1.12, 0, 1, 0), ("a", 2.12, 3.20, 1.35, 0, 0, 0), ("a", 3.52, 4.30, 1.2, 0, 0, 0), ("a", 4.64, 5.44, 1.45, 0, 0, 0), ("a", 5.92, 7.40, 1.25, 0, 0, 1),
     ("b", .48, .94, 1.12, 0, 1, 0), ("b", .96, 3.50, 1.3, 0, 0, 0), ("b", 3.64, 6.20, 1.2, 0, 0, 1),
     ("c", .20, .96, 1.12, 0, 1, 0), ("c", 1.08, 1.76, 1.35, 0, 0, 0), ("c", 1.88, 3.48, 1.2, 0, 0, 0), ("c", 3.92, 4.60, 1.45, 0, 0, 0), ("c", 5.16, 6.44, 1.3, 0, 0, 1)]
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
# d 3 a.m. hook
cap("d", .28, 1.25, f"It's {K('3 a.m.')}")
cap("d", 1.62, 2.49, f"Everyone's\\N{K('asleep')}")
cap("d", 3.44, 4.25, f"except {K('you')}")
cap("d", 4.40, 5.75, f"replaying a\\N{K('conversation')}")
cap("d", 5.76, 6.77, f"from {K('three days')} ago")
# a the replay
cap("a", .10, .95, f"Your {K('brain')}")
cap("a", .96, 1.60, "treats a casual")
cap("a", 1.61, 2.11, f"okay {K('text')}")
cap("a", 2.12, 2.55, "like a")
pop("a", 2.56, 3.19, f"CRIME\\N{Y}SCENE")
pop("a", 3.52, 4.29, "ANALYZING")
pop("a", 4.64, 5.43, f"{Y}REWINDING")
cap("a", 5.92, 6.50, f"{K('searching')} for")
cap("a", 6.51, 7.39, f"what you did\\N{K('wrong')}")
# b the real reason
cap("b", .48, .93, "But you're")
cap("b", .96, 1.90, K("overthinking"))
cap("b", 1.91, 2.20, "because")
cap("b", 2.21, 3.49, f"{K('something')}\\Nis wrong")
cap("b", 3.64, 4.70, f"You're\\N{K('overthinking')}")
cap("b", 4.72, 5.35, "because you don't")
cap("b", 5.36, 5.75, K("trust"))
cap("b", 5.76, 6.19, f"yourself {K('yet')}")
# c tonight's fix
cap("c", .20, .95, f"So {K('tonight')}")
cap("c", 1.08, 1.75, f"try {K('this')}")
cap("c", 1.88, 2.70, f"I did my\\N{K('best')}")
cap("c", 2.71, 3.47, f"with what I\\N{K('knew')}")
pop("c", 3.92, 4.59, f"THEN\\N{Y}SLEEP")
pop("c", 5.16, 6.43, f"THE REPLAY\\N{Y}HELPS NO ONE")
print(render(clips, segs, E, S24 + "reel.mp4"), round(TOTAL, 2))
