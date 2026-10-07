"""The approved reel style, as a small library. See ../SKILL.md for when to use each piece.

A plan script imports this, lists its cuts and captions, then calls render():

    import sys; sys.path.insert(0, "<skill>/scripts"); from reel_style import *
    clips = {"c1": Clip("clip1.mp4", crop="1080:1444:0:238", face=(804, 460))}
    segs = [Seg("c1", 0, 1.12), Seg("c1", 1.12, 2.30, zoom=1.25), ...]
    E = Events(); E.cap(0.10, 1.11, f"I texted my {Y}partner"); ...
    render(clips, segs, E, "out.mp4")
"""
import os, subprocess, tempfile
from dataclasses import dataclass
from PIL import ImageFont

W, H = 1080, 1920
FONT_DIR = "/usr/share/fonts/opentype/montserrat/"
Y = r"{\c&H00D7FF&}"      # yellow keyword colour (ASS is BGR)
WH = r"{\c&HFFFFFF&}"
RED = r"{\c&H2A2AE8&}"

# Approved sizes (user asked twice for bigger text: keep these as the minimum).
SIZE_MAIN, SIZE_QUOTE, SIZE_LABEL, SIZE_POP = 80, 78, 62, 110
Y_MAIN, Y_QUOTE, Y_LABEL = 1150, 1125, 1000

@dataclass
class Clip:
    path: str
    crop: str            # picture area inside the source (strip letterbox bars), "w:h:x:y"
    face: tuple = (804, 460)  # face point in the 1436x1920 base frame, used to centre zooms

@dataclass
class Seg:
    clip: str
    start: float
    end: float
    zoom: float = 1.0    # 1.0 / 1.12-1.25 / 1.35-1.45 punch-ins, switch on each cut
    bw: bool = False     # black & white for the negative / "overthinking" beat
    fade_in: bool = False   # 20 ms audio fade where two different clips join
    fade_out: bool = False

def ts(t):
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"

class Events:
    IN = r"\fscx85\fscy85\t(0,90,\fscx100\fscy100)"

    def __init__(self):
        self.ev = []

    def cap(self, a, b, text, style="Main", y=None):
        """Normal caption; wrap keywords in {Y}...  Quote style = bold italic."""
        y = y or (Y_QUOTE if style == "Quote" else Y_MAIN)
        self.ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y}){self.IN}}}{text}")

    def pop(self, a, b, text, rot=-4, y=Y_MAIN):
        """Big tilted title for the punchline words. Use \\N for two lines, second line in {Y}."""
        self.ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},Pop,,0,0,0,,"
                       f"{{\\pos(540,{y})\\frz{rot}\\fscx120\\fscy120\\t(0,110,\\fscx100\\fscy100)}}{text}")

    def label(self, a, b, text, x=True, y=Y_LABEL):
        """White box, black text, optional red ✖ - e.g. 'OVERTHINKING:', 'INSTEAD OF:'."""
        mark = RED + "✖ " + r"{\c&H000000&}" if x else ""
        self.ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},Label,,0,0,0,,{{\\pos(540,{y})}}{mark}{text}")

    def strike(self, a, b, old, new, y_old=1065, y_new=1185):
        """Reframe: old line crossed out with a red bar, new line under it."""
        self.cap(a, b, old, style="Struck", y=y_old)
        # libass draws ASS font sizes ~0.74x the Pillow em size, so scale the measured width
        w = ImageFont.truetype(FONT_DIR + "Montserrat-ExtraBold.otf", SIZE_MAIN).getlength(old) * 0.74 + 20
        self.ev.append(f"Dialogue: 2,{ts(a)},{ts(b)},Line,,0,0,0,,"
                       f"{{\\an5\\pos(540,{y_old + 5})\\p1}}m 0 0 l {w:.0f} 0 {w:.0f} 9 0 9{{\\p0}}")
        self.cap(a, b, new, y=y_new)

    def ass(self):
        return f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Main,Montserrat ExtraBold,{SIZE_MAIN},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,5,3,5,40,40,0,1
Style: Struck,Montserrat ExtraBold,{SIZE_MAIN},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,5,3,5,40,40,0,1
Style: Quote,Montserrat ExtraBold,{SIZE_QUOTE},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,1,0,0,100,100,0,0,1,5,3,5,40,40,0,1
Style: Label,Montserrat Black,{SIZE_LABEL},&H00000000,&H00000000,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,3,12,0,5,40,40,0,1
Style: Pop,Montserrat Black,{SIZE_POP},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,7,4,5,40,40,0,1
Style: Line,Montserrat Black,10,&H002A2AE8,&H002A2AE8,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(self.ev) + "\n"

def render(clips, segs, events, out, fps=24, cutaway=None):
    """Cut + zoom + grade + join, then burn captions and normalise loudness to -14 LUFS."""
    names = list(clips)
    fc, lbl = [], ""
    for i, s in enumerate(segs):
        c = clips[s.clip]; n = names.index(s.clip); fx, fy = c.face
        w, h = round(1436 * s.zoom / 2) * 2, round(1920 * s.zoom / 2) * 2
        x = min(max(fx * s.zoom - 540, 0), w - W); y = min(max(fy * s.zoom - fy, 0), h - H)
        vf = (f"[{n}:v]trim={s.start}:{s.end},setpts=PTS-STARTPTS,crop={c.crop},scale={w}:{h}:flags=lanczos,"
              f"crop={W}:{H}:{x:.0f}:{y:.0f},setsar=1,fps={fps}")
        vf += ",hue=s=0,eq=contrast=1.12:brightness=0.03" if s.bw else ",eq=contrast=1.06:saturation=1.08:brightness=0.02"
        af = f"[{n}:a]atrim={s.start}:{s.end},asetpts=PTS-STARTPTS,aresample=48000"
        if s.fade_out: af += f",afade=t=out:st={s.end - s.start - 0.03:.3f}:d=0.03"
        if s.fade_in: af += ",afade=t=in:d=0.02"
        fc += [vf + f"[v{i}]", af + f"[a{i}]"]; lbl += f"[v{i}][a{i}]"
    fc.append(lbl + f"concat=n={len(segs)}:v=1:a=1[v][a]")
    tmp = tempfile.mkdtemp()
    joined, ass = os.path.join(tmp, "joined.mov"), os.path.splitext(out)[0] + ".ass"
    inputs = sum((["-i", clips[k].path] for k in names), [])
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-c:a", "pcm_s16le", joined], check=True)
    open(ass, "w", encoding="utf-8").write(events.ass())
    if cutaway:
        img, t0, t1 = cutaway; d = t1 - t0
        fcx = (f"[1:v]setpts=PTS-STARTPTS+{t0}/TB,format=rgba,split=2[a][b];"
               f"[a]crop=230:1350:0:0,scale=1080:1920,gblur=sigma=40[bg];"
               f"[b]crop=605:835:255:195,scale=w='740*(1+0.07*min(max((t-{t0})/{d},0),1))':h=-2:eval=frame[fg];"
               f"[bg][fg]overlay=x='540-0.5*w':y='610-0.5*h':eval=frame,format=rgba,"
               f"fade=t=in:st={t0}:d=0.18:alpha=1,fade=t=out:st={t1 - 0.18}:d=0.18:alpha=1[card];"
               f"[0:v][card]overlay=enable='between(t,{t0},{t1})':eof_action=pass,ass={ass}[v]")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", joined, "-framerate", str(fps), "-loop", "1", "-t", "30", "-i", img,
                        "-filter_complex", fcx, "-map", "[v]", "-map", "0:a",
                        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000", "-c:v", "libx264", "-preset", "slow",
                        "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
        os.remove(joined)
        return out
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", joined, "-vf", f"ass={ass}",
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000", "-c:v", "libx264", "-preset", "slow",
                    "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out],
                   check=True)
    os.remove(joined)
    return out
