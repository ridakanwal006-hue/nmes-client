import sys, os, subprocess, tempfile
SRC = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/zip16/Woman_changing_trendy_outfits_20261009022723.mp4"
S17 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s17/"
sys.path.insert(0, S17)
from reel_style import Events, Y, WH, ts, W, H

FPS = 24
AX, AY = 540, 900                       # zoom anchor (torso), 1080x1920 frame
# (start, end, zoom) - contiguous cuts, so the audio and outfit changes are untouched
SEGS = [(0.00, 0.55, 1.0), (0.55, 1.00, 1.15), (1.00, 1.60, 1.05), (1.60, 2.45, 1.25),
        (2.45, 3.05, 1.0), (3.05, 3.70, 1.15), (3.70, 4.50, 1.3),
        (4.50, 5.30, 1.0), (5.30, 6.00, 1.15), (6.00, 6.60, 1.05), (6.60, 7.30, 1.3),
        (7.30, 8.10, 1.0), (8.10, 8.70, 1.12), (8.70, 9.40, 1.3), (9.40, 10.00, 1.0)]
fc, lbl = [], ""
for i, (a, b, z) in enumerate(SEGS):
    w, h = round(W * 1.5 * z * 2), round(H * 1.5 * z * 2)       # supersampled 2x for smooth edges
    x = min(max(AX * z * 2 - W, 0), w - 2 * W); y = min(max(AY * z * 2 - AY * 2, 0), h - 2 * H)
    fc += [f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS,scale={w}:{h}:flags=lanczos,crop={2 * W}:{2 * H}:{x:.0f}:{y:.0f},scale={W}:{H}:flags=lanczos,"
           f"setsar=1,fps={FPS},eq=contrast=1.04:saturation=1.05[v{i}]",
           f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000[a{i}]"]
    lbl += f"[v{i}][a{i}]"
fc.append(lbl + f"concat=n={len(SEGS)}:v=1:a=1[v][a]")

def seg_of(t):
    for a, b, z in SEGS:
        if a - 1e-6 <= t < b: return a, b, z
    return SEGS[-1]

def Ty(y, z): return AY + (y - AY) * z      # where a source point at 1080x1920 y lands after zoom z
E = Events()
CARD2 = (180, 1338, 915, 1512)   # two-line subtitles (looks 1-3)
CARD1 = (175, 1352, 920, 1432)   # one-line subtitle (look 4)               # covers the burned-in Flow subtitles at z=1 (x0,y0,x1,y1)
def pieces(a, b):                            # split an event at segment boundaries
    out = []
    for sa, sb, z in SEGS:
        lo, hi = max(a, sa), min(b, sb)
        if hi - lo > 0.02: out.append((lo, hi, z))
    return out
K = lambda w: "{\\fs98}" + Y + w + "{\\fs80}" + WH
def card(a, b, CARD):
    for lo, hi, z in pieces(a, b):
        x0, y0, x1, y1 = AX + (CARD[0] - AX) * z, Ty(CARD[1], z), AX + (CARD[2] - AX) * z, Ty(CARD[3], z)
        E.ev.append(f"Dialogue: 0,{ts(lo)},{ts(hi)},Line,,0,0,0,,{{\\an7\\pos(0,0)\\p1\\1c&H000000&\\3c&H000000&\\bord16\\blur3}}"
                    f"m {x0:.0f} {y0:.0f} l {x1:.0f} {y0:.0f} {x1:.0f} {y1:.0f} {x0:.0f} {y1:.0f}{{\\p0}}")
def cap(a, b, text):
    for lo, hi, z in pieces(a, b):
        yc = 1425 if a < 7.3 else 1392
        E.ev.append(f"Dialogue: 2,{ts(lo)},{ts(hi - .01)},Main,,0,0,0,,{{\\pos(540,{Ty(yc, z):.0f}){E.IN}}}{text}")
def label(a, b, text):
    for lo, hi, z in pieces(a, b):
        E.ev.append(f"Dialogue: 2,{ts(lo)},{ts(hi - .01)},Label,,0,0,0,,{{\\pos(540,{Ty(1290 if a < 7.3 else 1305, z):.0f})}}{text}")
card(0, 7.3, CARD2); card(7.3, 10, CARD1)
label(0.10, 2.40, "LOOK 1"); label(2.50, 4.45, "LOOK 2"); label(4.60, 7.15, "LOOK 3"); label(7.30, 10.0, "LOOK 4")
cap(0.12, 0.58, K("Burgundy"))
cap(0.58, 1.02, f"with {K('gold')}")
cap(1.02, 2.40, f"looks so {K('luxurious')}")
cap(2.85, 3.68, f"{K('Monochrome')} {K('brown')}")
cap(3.68, 4.45, f"looks so {K('chic')}")
cap(4.92, 6.00, f"{K('Gray')} with {K('denim')}")
cap(6.00, 7.15, f"looks so {K('effortless')}")
cap(8.10, 8.72, "Which look is")
cap(8.72, 9.60, f"your {K('favorite')}?")
ass = S17 + "reel.ass"; out = S17 + "reel.mp4"
open(ass, "w", encoding="utf-8").write(E.ass())
tmp = tempfile.mkdtemp(); joined = os.path.join(tmp, "j.mov")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium",
                "-crf", "16", "-c:a", "pcm_s16le", joined], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", joined, "-vf", f"ass={ass}", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000",
                "-c:v", "libx264", "-preset", "slow", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print(out)
