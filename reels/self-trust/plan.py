import sys
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d23/"
S23 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s23/"
sys.path.insert(0, S23)
from reel_style import Clip, Seg, Events, render, Y, WH, ts

CR, FACE = "720:962:0:40", (650, 720)
clips = {k: Clip(D + f"{k}.mp4", crop=CR, face=FACE) for k in ("d", "b", "c", "a")}
# (clip, start, end, zoom, bw, fade_in, fade_out) - the voice (d), the wait (b), the way out (c), the product (a)
S = [("d", .28, 1.32, 1.0, 0, 1, 0), ("d", 2.00, 2.88, 1.3, 0, 0, 0), ("d", 3.40, 4.68, 1.15, 0, 0, 0), ("d", 4.96, 6.80, 1.4, 0, 0, 1),
     ("b", .28, 1.02, 1.0, 0, 1, 0), ("b", 1.20, 2.96, 1.25, 0, 0, 0), ("b", 3.08, 4.40, 1.12, 0, 0, 0), ("b", 4.40, 6.72, 1.35, 0, 0, 1),
     ("c", .30, 1.82, 1.0, 0, 1, 0), ("c", 1.88, 3.90, 1.3, 0, 0, 0), ("c", 4.50, 6.76, 1.5, 0, 0, 1),
     ("a", .28, 2.00, 1.0, 0, 1, 0), ("a", 2.00, 2.90, 1.3, 0, 0, 0), ("a", 3.68, 4.50, 1.15, 0, 0, 0), ("a", 4.50, 6.00, 1.3, 0, 0, 0), ("a", 6.08, 7.56, 1.15, 0, 0, 1)]
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
# d the voice (the inner voice lines in the quote style)
cap("d", .28, 1.31, f"You know that {K('voice')}")
cap("d", 2.00, 2.87, f"You're not {K('ready')}", style="Quote")
cap("d", 3.40, 4.67, f"Not good {K('enough')}", style="Quote")
cap("d", 4.96, 5.50, f"Everyone {K('else')}", style="Quote")
cap("d", 5.51, 6.25, f"has it\\N{K('figured out')}", style="Quote")
cap("d", 6.26, 6.79, f"but {K('you')}", style="Quote")
# b the wait
cap("b", .28, 1.01, f"So you {K('wait')}")
pop("b", 1.20, 2.95, f"YOU\\N{Y}OVERTHINK")
cap("b", 3.08, 4.39, f"you watch\\N{K('opportunities')}")
cap("b", 4.40, 4.95, f"pass {K('while')}")
cap("b", 4.96, 5.55, "you prepare")
cap("b", 5.56, 6.71, f"just a little\\N{K('more')}")
# c the way out
cap("c", .30, 1.05, f"Stop {K('waiting')}")
cap("c", 1.06, 1.81, f"to feel {K('ready')}")
cap("c", 1.88, 2.89, f"Start\\N{K('trusting')}")
cap("c", 2.90, 3.89, f"{K('yourself')} today")
cap("c", 4.50, 5.38, f"your {K('future self')}")
cap("c", 5.40, 5.95, "is already")
cap("c", 5.96, 6.75, f"{K('thanking')} you")
# a the product
cap("a", .28, 1.00, f"I made {K('something')}")
cap("a", 1.01, 1.99, f"for {K('exactly')}\\Nthis from")
pop("a", 2.00, 2.89, f"SELF-DOUBT\\N{Y}TO SELF-TRUST")
cap("a", 3.68, 4.49, f"{K('13')} lessons")
cap("a", 4.50, 5.45, f"a {K('14-day')}\\N{K('tracker')}")
cap("a", 5.46, 5.99, "the exact")
cap("a", 6.08, 6.80, f"{K('tools')} to shut")
cap("a", 6.81, 7.55, f"that voice {K('down')}")
print(render(clips, segs, E, S23 + "reel.mp4"), round(TOTAL, 2))
