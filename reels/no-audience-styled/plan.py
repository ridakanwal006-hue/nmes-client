import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d9/"
S9 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s9/"
sys.path.insert(0, S9)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:964:0:200", (838, 520)
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("r1", "r2", "r3", "r4")}
# (clip, start, end, zoom, bw, fade_in, fade_out)
S = [("r1", .42, .95, 1.3, 1, 1, 0), ("r1", .95, 1.64, 1.0, 1, 0, 0), ("r1", 1.64, 2.46, 1.25, 1, 0, 0), ("r1", 2.62, 4.46, 1.0, 0, 0, 0),
     ("r1", 4.52, 5.50, 1.3, 0, 0, 0), ("r1", 5.54, 6.12, 1.45, 0, 0, 1),
     ("r2", .30, 1.52, 1.12, 0, 1, 0), ("r2", 2.12, 3.48, 1.3, 0, 0, 0), ("r2", 3.56, 3.90, 1.45, 0, 0, 0), ("r2", 3.92, 5.30, 1.12, 0, 0, 0),
     ("r2", 5.54, 6.50, 1.45, 0, 0, 1),
     ("r3", .46, 1.90, 1.0, 1, 1, 0), ("r3", 1.90, 2.88, 1.25, 1, 0, 0), ("r3", 3.30, 4.30, 1.3, 0, 0, 0), ("r3", 4.30, 5.28, 1.0, 0, 0, 0),
     ("r3", 5.42, 5.80, 1.12, 0, 0, 0), ("r3", 5.80, 6.94, 1.45, 0, 0, 1),
     ("r4", .14, .58, 1.0, 0, 1, 0), ("r4", .60, 1.64, 1.25, 0, 0, 0), ("r4", 1.78, 2.56, 1.0, 1, 0, 0), ("r4", 2.58, 3.30, 1.4, 1, 0, 0),
     ("r4", 3.88, 4.40, 1.12, 0, 0, 0), ("r4", 4.45, 5.20, 1.3, 0, 0, 0), ("r4", 5.22, 5.88, 1.5, 0, 0, 1)]
segs, off, t = [], [], 0.0
for c, a, b, z, bw, fi, fo in S:
    segs.append(Seg(c, a, b, z, bool(bw), bool(fi), bool(fo))); off.append((c, a, b, t)); t += b - a

def T(c, s):
    for cc, a, b, o in off:
        if cc == c and a - 1e-6 <= s <= b + 1e-6: return o + s - a
    raise ValueError((c, s))

K = lambda w: "{\\fs104}" + Y + w + "{\\fs80}" + WH       # important word: bigger + yellow
E = Events()
def cap(c, a, b, text, **k): E.cap(T(c, a), T(c, b) - .01, text, **k)
def pop(c, a, b, text, **k): E.pop(T(c, a), T(c, b) - .01, text, **k)
def big(c, a, b, text, size):
    E.ev.append(f"Dialogue: 1,{ts(T(c, a))},{ts(T(c, b) - .01)},Pop,,0,0,0,,{{\\pos(540,1150)\\frz-4\\fs{size}\\fscx125\\fscy125\\t(0,120,\\fscx100\\fscy100)}}{text}")

big("r1", .42, .94, f"{Y}90%", 250)
cap("r1", .95, 1.63, "of your")
cap("r1", 1.64, 2.45, K("self-doubt"))
cap("r1", 2.62, 4.45, f"{K('disappears')} the moment\\Nyou realize")
cap("r1", 4.52, 5.49, f"there's {K('no audience')}")
cap("r1", 5.54, 6.11, f"to {K('perform')} for")
cap("r2", .30, 1.51, f"{K('No approval')} to win")
cap("r2", 2.12, 3.47, f"{K('No one')} to impress")
pop("r2", 3.56, 3.89, f"{Y}NOBODY")
cap("r2", 3.92, 5.29, f"to {K('convince')}")
pop("r2", 5.54, 6.49, f"EXCEPT\\N{Y}YOURSELF")
cap("r3", .46, 1.89, f"So {K('stop playing')}\\Nthe role you think")
cap("r3", 1.90, 2.87, f"everyone {K('expects')}")
pop("r3", 3.30, 4.29, f"BRUTALLY\\N{Y}HONEST")
cap("r3", 4.30, 5.27, f"about {K('who you are')}")
cap("r3", 5.42, 5.79, "and what")
cap("r3", 5.80, 6.93, f"actually\\N{K('fulfills you')}")
cap("r4", .14, .57, f"{K('Start')} acting")
cap("r4", .60, 1.63, f"from that {K('place')}")
cap("r4", 1.78, 2.55, "and watch your")
pop("r4", 2.58, 3.29, f"SELF-DOUBT\\N{Y}FADE")
cap("r4", 3.88, 4.39, f"The {K('performance')}")
cap("r4", 4.45, 5.19, f"{K('ends')} when you")
pop("r4", 5.22, 5.87, f"STOP\\N{Y}AUDITIONING")
print(render(clips, segs, E, S9 + "reel10.mp4"), round(t, 2))
