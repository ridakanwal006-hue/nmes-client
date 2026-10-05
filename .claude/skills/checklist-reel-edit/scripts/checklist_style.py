"""The "checklist" podcast-tips style as a small library. See ../SKILL.md for the rules.

A plan script (copy example_plan.py) does:
    clips = {"c1": Clip("clip1.mp4", crop="1080:1444:0:238", face=(0.56, 0.24))}
    W1 = load_words("clip1.mp4")                     # Parakeet word timestamps
    segs = []
    for i, (a, b) in enumerate(speech_runs(W1, 0, 7.3)):   # pauses cut out
        segs.append(Seg("c1", a, b, zoom=ANGLES[i % 4]))
    T = Timeline(segs)                                # source time -> output time
    E = Events()
    E.title(T("c1", 0.0), T("c1", 2.3), ["3 steps to", "stop over-apologizing"])
    E.checklist(T("c1", 2.3), T.end, [("1.", "Look", "mute the video", T("c1", 2.9)), ...])
    auto_captions(E, T, "c1", W1)
    E.sfx(T("c1", 2.9), "pop")
    render(clips, segs, E, "out.mp4")
"""
import os, re, json, subprocess, tempfile, sys
from dataclasses import dataclass, field
from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import asr, sfx as sfxlib

W, H, FPS = 1080, 1920, 30
INTER = "/usr/share/fonts/opentype/inter/"
F_CAP, F_BOLD = "Inter Display SemiBold", "Inter Display ExtraBold"
FILE = {F_CAP: INTER + "InterDisplay-SemiBold.otf", F_BOLD: INTER + "InterDisplay-ExtraBold.otf"}
LIBASS_SCALE = 0.82  # libass draws Inter at ~0.82x the Pillow em size (measured)

Y = r"{\c&H00E5FF&}"   # yellow #FFE500 (ASS colours are BGR)
WH = r"{\c&HFFFFFF&}"
BK = r"{\c&H000000&}"

# Sizes: the reference uses small captions; this user wants text readable for all ages,
# so everything is larger than the reference. Do not go smaller.
SIZE_CAP, SIZE_LIST, SIZE_TITLE = 66, 54, 58
Y_CAP, Y_PANEL, Y_TITLE = 1150, 1215, 1265
LINE = 72            # checklist line spacing
ANGLES = (1.0, 1.32, 1.0, 1.55)   # "camera angles": wide, medium, wide, close - cycle on each cut

GRADES = {
    # warm natural podcast look of the reference: cream skin, dark background, soft vignette
    "warm": "eq=contrast=1.05:brightness=0.01:saturation=1.06,"
            "colorbalance=rs=0.04:gs=0.01:bs=-0.04:rm=0.02:bm=-0.02,vignette=angle=0.35",
    "neutral": "eq=contrast=1.04:saturation=1.04",
    "bw": "hue=s=0,eq=contrast=1.12:brightness=0.03",
    "punchy": "eq=contrast=1.10:saturation=1.12,colorbalance=rs=0.03:bs=-0.03,vignette=angle=0.45",
}
# light, natural voice clean-up: rumble cut, gentle denoise, de-ess, compression (loudness is set at the end)
VOICE = ("highpass=f=80,afftdn=nf=-30:nr=8,deesser=i=0.3,"
         "acompressor=threshold=-20dB:ratio=3:attack=5:release=90:makeup=2")

def text_width(font, size, text):
    clean = re.sub(r"\{[^}]*\}", "", text)
    return ImageFont.truetype(FILE[font], size).getlength(clean) * LIBASS_SCALE

def ts(t):
    t = max(t, 0)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"

# ---------------------------------------------------------------- footage
@dataclass
class Clip:
    path: str
    crop: str = ""            # picture area inside the source "w:h:x:y" (strip letterbox bars); "" = whole frame
    face: tuple = (0.5, 0.3)  # face position as a fraction of the picture (x, y); zooms centre on it

@dataclass
class Seg:
    clip: str
    start: float
    end: float
    zoom: float = 1.0
    zoom_to: float = None     # set to make a slow push-in / pull-out over the segment
    grade: str = "warm"       # a GRADES key, or "lut:/path/file.cube"

def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height", "-of", "csv=p=0", path], capture_output=True, text=True).stdout
    w, h = out.strip().split(",")[:2]
    return int(w), int(h)

def load_words(path, cache=True):
    """Parakeet word timestamps for a clip, cached next to it as <clip>.words.json."""
    js = os.path.splitext(path)[0] + ".words.json"
    if cache and os.path.exists(js):
        return json.load(open(js))
    ws = asr.words(asr.load(path))
    try:
        json.dump(ws, open(js, "w"))
    except OSError:
        pass
    return ws

def speech_runs(words, start, end, max_pause=0.30, pad=0.08):
    """Cut out every pause longer than max_pause between start and end. Returns [(a, b)]."""
    # a word belongs to the range if it overlaps it (first-word timestamps are often early)
    ws = [w for w in words if w["e"] > start and w["s"] < end]
    runs = []
    for w in ws:
        if runs and w["s"] - runs[-1][1] <= max_pause:
            runs[-1][1] = w["e"]
        else:
            runs.append([w["s"], w["e"]])
    out = []
    for a, b in runs:
        a, b = max(start, a - pad), min(end, b + pad)
        if out and a <= out[-1][1]:
            out[-1] = (out[-1][0], b)
        else:
            out.append((a, b))
    return out

class Timeline:
    """Maps a clip's source time to output time after cutting and joining the segments."""
    def __init__(self, segs):
        self.segs, t = [], 0.0
        for s in segs:
            self.segs.append((s, t)); t += s.end - s.start
        self.end = t

    def __call__(self, clip, t, edge="start"):
        best = None
        for s, o in self.segs:
            if s.clip != clip:
                continue
            if s.start - 1e-6 <= t <= s.end + 1e-6:
                return o + t - s.start
            # t is inside a cut-out pause: snap forward for a start, back for an end
            if edge == "start" and s.start > t and (best is None or s.start < best[0]):
                best = (s.start, o)
            if edge == "end" and s.end < t and (best is None or s.end > best[0]):
                best = (s.end, o + s.end - s.start)
        if best is None:
            raise ValueError(f"{clip} t={t} is outside every segment")
        return best[1]

# ---------------------------------------------------------------- overlays
class Events:
    def __init__(self):
        self.ev, self.fx, self.caps = [], [], []

    def _add(self, layer, a, b, style, text):
        self.ev.append(f"Dialogue: {layer},{ts(a)},{ts(b)},{style},,0,0,0,,{text}")

    def cap(self, a, b, text, y=Y_CAP):
        """Spoken-word caption, 1-3 words, white; {Y} for a yellow keyword if wanted."""
        self.caps.append([a, b, y, text])

    def _caps(self):
        # one caption on screen at a time: each ends where the next begins
        cs = sorted(self.caps)
        for i, (a, b, y, text) in enumerate(cs):
            if i + 1 < len(cs):
                b = min(b, cs[i + 1][0] - 0.01)
            self._add(4, a, b, "Cap", f"{{\\an5\\pos(540,{y})\\fscx92\\fscy92\\t(0,80,\\fscx100\\fscy100)}}{text}")

    def title(self, a, b, lines, y=Y_TITLE):
        """Hook title: each line on its own white rounded box, black bold text."""
        h, pad, r = 76, 24, 14
        for i, line in enumerate(lines):
            cy = y + i * (h + 4)
            w = text_width(F_BOLD, SIZE_TITLE, line) + 2 * pad
            x0, y0 = (W - w) / 2, cy - h / 2
            box = (f"m {r} 0 l {w - r:.0f} 0 b {w:.0f} 0 {w:.0f} 0 {w:.0f} {r} l {w:.0f} {h - r} "
                   f"b {w:.0f} {h} {w:.0f} {h} {w - r:.0f} {h} l {r} {h} b 0 {h} 0 {h} 0 {h - r} l 0 {r} b 0 0 0 0 {r} 0")
            self._add(2, a, b, "Box", f"{{\\an7\\pos({x0:.0f},{y0:.0f})\\fad(150,150)\\p1}}{box}{{\\p0}}")
            self._add(3, a, b, "Title", f"{{\\an5\\pos(540,{cy + 2:.0f})\\fad(150,150)}}{line}")

    def checklist(self, a, b, items, y=Y_PANEL):
        """Numbered list on a dark see-through band. items = [(num, keyword, rest, reveal_time)].
        Each item is blurred (a teaser) until reveal_time, then sharpens; reveal_time None = sharp."""
        n = len(items)
        band_h = n * LINE + 36
        self._add(0, a, b, "Band", f"{{\\an7\\pos(0,{y})\\fad(200,150)\\p1}}m 0 0 l {W} 0 {W} {band_h} 0 {band_h}{{\\p0}}")
        texts = [f"{Y}{num} {key}{WH} - {rest}" for num, key, rest, _ in items]
        left = (W - max(text_width(F_BOLD, SIZE_LIST, t) for t in texts)) / 2
        for i, (t, (_, _, _, at)) in enumerate(zip(texts, items)):
            cy = y + 18 + LINE / 2 + i * LINE
            tag = f"\\an4\\pos({left:.0f},{cy:.0f})\\fad(200,150)"
            if at is not None and at > a:
                ms = int((at - a) * 1000)
                tag += f"\\blur14\\alpha&H50&\\t({ms},{ms + 260},\\blur0\\alpha&H00&)"
            self._add(1, a, b, "List", f"{{{tag}}}{t}")

    def sfx(self, t, name, gain_db=-20):
        """Sound effect at output time t: a name from sfx.py or a path to a .wav/.mp3."""
        self.fx.append((t, name, gain_db))

    def ass(self):
        if self.caps and not any(",Cap," in e for e in self.ev):
            self._caps()
        return f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{F_CAP},{SIZE_CAP},&H00FFFFFF,&H00FFFFFF,&H00000000,&H70000000,0,0,0,0,100,100,0,0,1,2,3,5,40,40,0,1
Style: List,{F_BOLD},{SIZE_LIST},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,0,2,4,0,0,0,1
Style: Title,{F_BOLD},{SIZE_TITLE},&H00000000,&H00000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1
Style: Box,{F_BOLD},10,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Band,{F_BOLD},10,&H70000000,&H70000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(self.ev) + "\n"

def auto_captions(E, T, clip, words, start=None, end=None, max_words=3, max_chars=20, keywords=()):
    """1-3 word captions from word timestamps, cut at punctuation, shown until the next one starts."""
    ws = [w for w in words if (start is None or w["e"] > start) and (end is None or w["s"] < end)]
    chunks, cur = [], []
    for w in ws:
        txt = " ".join(x["w"] for x in cur + [w])
        # new caption when full, too long, or after a breath (>= 0.15 s gap)
        if cur and (len(cur) >= max_words or len(txt) > max_chars or w["s"] - cur[-1]["e"] >= 0.15):
            chunks.append(cur); cur = []
        cur.append(w)
        if re.search(r"[.,!?;:]$", w["w"]):
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    kw = {k.lower() for k in keywords}
    for i, ch in enumerate(chunks):
        a = T(clip, max(ch[0]["s"], start or 0), "start")
        # pauses are already cut, so a caption stays up until the next one starts
        b = T(clip, chunks[i + 1][0]["s"], "start") if i + 1 < len(chunks) else T(clip, min(ch[-1]["e"], end or 1e9), "end") + 0.12
        b = max(b, a + 0.25)
        text = " ".join(Y + w["w"] + WH if re.sub(r"[^\w']", "", w["w"]).lower() in kw else w["w"] for w in ch)
        E.cap(a, b - 0.01, text)

# ---------------------------------------------------------------- render
def _even(v):
    return int(round(v / 2) * 2)

def _video_chain(n, s, c, fps):
    vw, vh = probe(c.path)
    cw, ch, cx, cy = (map(int, c.crop.split(":")) if c.crop else (vw, vh, 0, 0))
    k = max(W / cw, H / ch)
    bw, bh = _even(cw * k), _even(ch * k)
    fx, fy = c.face[0] * bw, c.face[1] * bh
    x1 = min(max(fx - W / 2, 0), bw - W); y1 = min(max(fy - H / 2, 0), bh - H)
    sx, sy = fx - x1, fy - y1                      # face position on screen at zoom 1
    v = f"[{n}:v]trim={s.start}:{s.end},setpts=PTS-STARTPTS,crop={cw}:{ch}:{cx}:{cy},"
    if s.zoom_to is None or abs(s.zoom_to - s.zoom) < 1e-3:
        z = s.zoom
        zw, zh = _even(bw * z), _even(bh * z)
        x = min(max(fx * z - W / 2, 0), zw - W); y = min(max(fy * z - sy, 0), zh - H)
        v += f"scale={zw}:{zh}:flags=lanczos,crop={W}:{H}:{x:.0f}:{y:.0f},setsar=1,fps={fps}"
    else:
        frames = max(int(round((s.end - s.start) * fps)), 2)
        z0, z1 = s.zoom, s.zoom_to
        v += (f"scale={bw}:{bh}:flags=lanczos,crop={W}:{H}:{x1:.0f}:{y1:.0f},fps={fps},"
              f"scale={2 * W}:{2 * H}:flags=lanczos,"
              f"zoompan=z='{z0}+({z1}-{z0})*on/{frames - 1}':x='{2 * sx:.0f}-{2 * sx:.0f}/zoom':"
              f"y='{2 * sy:.0f}-{2 * sy:.0f}/zoom':d=1:s={W}x{H}:fps={fps},setsar=1")
    g = s.grade
    v += "," + (f"lut3d=file='{g[4:]}'" if g.startswith("lut:") else GRADES[g])
    return v

def render(clips, segs, E, out, fps=FPS, voice=True, lufs=-14):
    """Cut + zoom + grade + join, clean the voice, burn overlays, add effects, set loudness."""
    names = list(clips)
    fc, lbl = [], ""
    for i, s in enumerate(segs):
        n = names.index(s.clip)
        fc.append(_video_chain(n, s, clips[s.clip], fps) + f"[v{i}]")
        d = s.end - s.start
        fc.append(f"[{n}:a]atrim={s.start}:{s.end},asetpts=PTS-STARTPTS,aresample=48000,"
                  f"afade=t=in:d=0.008,afade=t=out:st={max(d - 0.012, 0):.3f}:d=0.012[a{i}]")
        lbl += f"[v{i}][a{i}]"
    fc.append(lbl + f"concat=n={len(segs)}:v=1:a=1[v][a0]")
    fc.append(f"[a0]{VOICE if voice else 'anull'}[a]")
    tmp = tempfile.mkdtemp()
    joined = os.path.join(tmp, "joined.mov")
    ins = sum((["-i", clips[k].path] for k in names), [])
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "15", "-c:a", "pcm_s16le", joined], check=True)
    ass = os.path.splitext(out)[0] + ".ass"
    open(ass, "w", encoding="utf-8").write(E.ass())
    lib = sfxlib.build(os.path.expanduser("~/.cache/reel-edit/sfx"))
    ins, af = ["-i", joined], []
    for j, (t, name, g) in enumerate(E.fx, 1):
        ins += ["-i", name if os.path.sep in name else os.path.join(lib, name + ".wav")]
        ms = int(max(t, 0) * 1000)
        af.append(f"[{j}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms},volume={g}dB[f{j}]")
    mix = "[0:a]aformat=channel_layouts=stereo[vo];" + "".join(x + ";" for x in af)
    mix += "[vo]" + "".join(f"[f{j}]" for j in range(1, len(E.fx) + 1))
    mix += f"amix=inputs={len(E.fx) + 1}:normalize=0:duration=first,loudnorm=I={lufs}:TP=-1.5:LRA=11,aresample=48000[a]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", f"[0:v]ass={ass}[v];" + mix,
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "slow", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
    os.remove(joined)
    return out
