import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d38/"
S38 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s38/"
sys.path.insert(0, S38)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (660, 880)   # spotlight look; tight framing, small zooms
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("f1", "f5", "f2", "f4", "f3", "f6")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - Day 4 flipping the story: hook (f1), the pattern (f5, f2 a little B&W), the name (f4), the fix (f3), follow CTA (f6)
S = [("f1", .05, 3.68, 1.0, 0, 1, 0), ("f1", 5.56, 7.30, 1.15, 0, 0, 1),
     ("f5", .44, 1.36, 1.0, 0, 1, 0), ("f5", 2.20, 3.72, 1.1, 0, 0, 0), ("f5", 4.32, 5.62, 1.05, 0, 0, 1),
     ("f2", .32, 2.90, 1.0, 1, 1, 0), ("f2", 2.90, 5.10, 1.1, 0, 0, 1),
     ("f4", .40, 1.76, 1.0, 0, 1, 0), ("f4", 2.04, 3.58, 1.1, 0, 0, 0), ("f4", 3.58, 4.64, 1.15, 0, 0, 1),
     ("f3", .40, 3.04, 1.0, 0, 1, 0), ("f3", 3.16, 4.92, 1.1, 0, 0, 1),
     ("f6", .16, 1.68, 1.05, 0, 1, 0), ("f6", 2.32, 5.00, 1.0, 0, 0, 1)]
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
# f1 hook
cap("f1", .05, 1.60, f"If you bring up\\Nwhat {K('they did')}")
cap("f1", 1.61, 3.67, f"and end up\\N{K('apologizing')},")
pop("f1", 5.56, 7.29, f"THAT'S NOT\\N{Y}A COINCIDENCE.")
# f5 the pattern
cap("f5", .44, 1.35, f"{K('First')}, they\\Ndeny it.")
cap("f5", 2.20, 3.71, f"Then they say\\Nyou're {K('exaggerating')}.")
cap("f5", 4.32, 5.61, f"Then they become\\Nthe {K('victim')}.")
# f2 one concern
cap("f2", .32, 1.80, f"You walk in with\\N{K('one concern')}")
cap("f2", 1.81, 2.89, "and walk out")
cap("f2", 2.90, 3.80, f"{K('apologizing')} for")
cap("f2", 3.81, 5.09, f"{K('everything')}\\Nyou ever said.")
# f4 the name
cap("f4", .40, 1.75, f"It's called\\N{K('flipping the story')},")
cap("f4", 2.04, 3.57, "and its only job\\Nis to make you")
cap("f4", 3.58, 4.63, f"{K('forget')} your {K('point')}.")
# f3 the fix
cap("f3", .40, 1.50, f"Next time,\\N{K('stay calm')}")
cap("f3", 1.51, 3.03, f"and repeat\\N{K('one sentence')}:")
cap("f3", 3.16, 4.91, f"I'm still talking\\Nabout what {K('you did')}.")
# f6 follow CTA
pop("f6", .16, 1.67, f"FOLLOW FOR\\N{Y}PART TWO.")
cap("f6", 2.32, 4.99, f"The next trick is\\Neven {K('harder to spot')}.")
# extra bottom line at 10-12 s: follow for the next part
E.cap(10.3, 12.3, f"Follow for the {K('next part')}", y=1640)
print(render(clips, segs, E, S38 + "reel.mp4"), round(TOTAL, 2))
