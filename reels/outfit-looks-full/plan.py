import os, subprocess, tempfile
SRC = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/zip16/Woman_changing_trendy_outfits_20261009022723.mp4"
OUT = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s18/"
W, H = 1080, 1920
GOLD, INK = "&H0E7CC2&", "&H141414&"           # amber keyword colour, near-black text (ASS = BGR)
def ts(t): return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"

def typed(parts, dur=0.32):
    """Typewriter: each character pops in, keywords bigger + amber. parts = [(text, is_key)]"""
    n = sum(len(t) for t, _ in parts); k = max(1, round(dur * 100 / n)); out = ""
    for text, key in parts:
        out += "{\\fs88\\1c" + GOLD + "}" if key else "{\\fs80\\1c" + INK + "}"
        out += "".join("{\\k%d}%s" % (k, c) for c in text)
    return out

ev = []
def plate(a, b, box):                           # opaque rounded plate that hides the burned-in Flow subtitles
    x0, y0, x1, y1 = box
    for col, g in (("&H5BB3D9&", 7), ("&HFFFFFF&", 0)):     # thin gold rim, then white fill
        ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},Plate,,0,0,0,,{{\\an7\\pos(0,0)\\p1\\1c{col}\\3c{col}\\bord{16 + g}\\blur2.5}}"
                  f"m {x0} {y0} l {x1} {y0} {x1} {y1} {x0} {y1}{{\\p0}}")
def say(a, b, parts, y):
    ev.append(f"Dialogue: 2,{ts(a)},{ts(b)},Type,,0,0,0,,{{\\an5\\pos(540,{y})\\fad(0,90)}}{typed(parts)}")
def look(a, b, text):
    ev.append(f"Dialogue: 2,{ts(a)},{ts(b)},Label,,0,0,0,,{{\\pos(540,150)\\fad(120,120)}}{text}")

BOX2 = (180, 1340, 915, 1512)                  # two-line subtitles (looks 1-3)
BOX1 = (180, 1352, 915, 1434)                  # one-line subtitle (look 4)
plate(0, 7.30, BOX2); plate(7.30, 10.0, BOX1)
look(0.05, 2.45, "LOOK 1"); look(2.55, 4.55, "LOOK 2"); look(4.65, 7.20, "LOOK 3"); look(7.30, 10.0, "LOOK 4")
Y2, Y1 = 1426, 1393
say(0.12, 0.60, [("Burgundy", True)], Y2)
say(0.60, 1.04, [("with ", False), ("gold", True)], Y2)
say(1.04, 2.40, [("looks so ", False), ("luxurious", True)], Y2)
say(2.85, 3.70, [("Monochrome ", True), ("brown", True)], Y2)
say(3.70, 4.50, [("looks so ", False), ("chic", True)], Y2)
say(4.92, 6.00, [("Gray", True), (" with ", False), ("denim", True)], Y2)
say(6.00, 7.20, [("looks so ", False), ("effortless", True)], Y2)
say(8.10, 8.72, [("Which look is", False)], Y1)
say(8.72, 9.70, [("your ", False), ("favorite", True), ("?", False)], Y1)

ass = OUT + "reel.ass"
hdr = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Type,Montserrat ExtraBold,80,&H00141414,&HFF000000,&HFF000000,&HFF000000,0,0,0,0,100,100,0,0,1,0,0,5,40,40,0,1
Style: Plate,Montserrat Black,10,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1
Style: Label,Montserrat Black,60,&H00000000,&H00000000,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,3,12,0,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
open(ass, "w", encoding="utf-8").write(hdr + "\n".join(ev) + "\n")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-vf",
                f"scale={W}:{H}:flags=lanczos,eq=contrast=1.04:saturation=1.05,ass={ass}",
                "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", OUT + "reel.mp4"], check=True)
print(OUT + "reel.mp4")
