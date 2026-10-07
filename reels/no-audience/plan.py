import sys, os, subprocess, tempfile
S8 = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/s8/"
D = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/d8/"
sys.path.insert(0, S8)
from reel_style import Events, Y, WH, ts, W, H

FPS = 24
CR, FACE = "720:964:0:200", (838, 520)
r = lambda t: round(t * FPS) / FPS
# clip, trim start, trim end, [(t_source, new_zoom)]
CLIPS = [("q1", .40, 7.00, [(.48, 1.07)]),
         ("q2", .28, 6.54, [(.32, 1.05), (2.16, 1.08), (3.56, 1.11)]),
         ("q3", .44, 6.96, []),
         ("q4", .10, 6.04, [(5.22, 1.12)])]
RAMP = 4  # frames, ~0.17 s

pieces, off, t = [], {}, 0.0   # pieces: (clip, a, b, zoom)
for c, a, b, zs in CLIPS:
    a, b = r(a), r(b); z, cur = 1.0, a
    for tz, zn in zs:
        tz = r(tz)
        if tz > cur: pieces.append((c, cur, tz, z))
        for i in range(RAMP):
            e = (i + 1) / RAMP; e = e * e * (3 - 2 * e)
            pieces.append((c, tz + i / FPS, tz + (i + 1) / FPS, z + (zn - z) * e))
        cur, z = tz + RAMP / FPS, zn
    pieces.append((c, cur, b, z))
    off[c] = (a, b, t); t += b - a
TOTAL = t

def T(c, s):
    a, b, o = off[c]; return o + s - a

fc, lbl, first = [], "", {c for c, *_ in CLIPS}
inputs = []
names = [c for c, *_ in CLIPS]
for i, (c, a, b, z) in enumerate(pieces):
    n = names.index(c); fx, fy = FACE
    w, h = round(1436 * z / 2) * 2, round(1920 * z / 2) * 2
    x = min(max(fx * z - 540, 0), w - W); y = min(max(fy * z - fy, 0), h - H)
    vf = (f"[{n}:v]trim={a:.4f}:{b:.4f},setpts=PTS-STARTPTS,crop={CR},scale={w}:{h}:flags=lanczos,"
          f"crop={W}:{H}:{x:.0f}:{y:.0f},setsar=1,fps={FPS},eq=contrast=1.04:saturation=1.05")
    af = f"[{n}:a]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,aresample=48000"
    ca, cb, _ = off[c]
    if abs(a - ca) < 1e-6: af += ",afade=t=in:d=0.02"
    if abs(b - cb) < 1e-6: af += f",afade=t=out:st={max(b - a - 0.03, 0):.3f}:d=0.03"
    fc += [vf + f"[v{i}]", af + f"[a{i}]"]; lbl += f"[v{i}][a{i}]"
fc.append(lbl + f"concat=n={len(pieces)}:v=1:a=1[v][a]")

# text overlays (only the words the brief lists)
E = Events()
def pop(a, b, text, size=None, y=1150, rot=-3):
    fs = f"\\fs{size}" if size else ""
    E.ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},Pop,,0,0,0,,{{\\pos(540,{y})\\frz{rot}{fs}\\fscx120\\fscy120\\t(0,110,\\fscx100\\fscy100)}}{text}")
pop(T("q1", .48), T("q1", .48) + 1.5, f"{Y}90%", size=260, y=1130)                       # C001 "90%"
pop(T("q2", 5.56), T("q2", 5.56) + 1.3, f"EXCEPT\\N{Y}YOURSELF")                       # C002 "except yourself"
pop(T("q3", 3.50), T("q3", 3.50) + 1.1, f"BRUTALLY\\N{Y}HONEST")                        # C003 "brutally honest"
fa = T("q4", 2.95)                                                                       # C004 "self-doubt fade": fades out as "fade" is said
E.ev.append(f"Dialogue: 1,{ts(T('q4', 2.58))},{ts(fa + 1.0)},Pop,,0,0,0,,{{\\pos(540,1150)\\frz-3\\fad(120,1000)}}SELF-DOUBT {Y}FADE")

# sound effects (low volume, under the voice): (output time, file)
sfx = [(T("q1", 4.50), "whoosh"),
       (T("q2", .32), "tick"), (T("q2", 2.16), "tick"), (T("q2", 3.56), "tick"), (T("q2", 5.56), "chime"),
       (T("q3", 3.50), "click"),
       (T("q4", 5.60), "ding")]
out = S8 + "reel8.mp4"
ass = S8 + "reel8.ass"
open(ass, "w", encoding="utf-8").write(E.ass())
tmp = tempfile.mkdtemp()
joined = os.path.join(tmp, "joined.mov")
cmd = ["ffmpeg", "-v", "error", "-y"]
for c in names: cmd += ["-i", D + c + ".mp4"]
cmd += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-c:a", "pcm_s16le", joined]
subprocess.run(cmd, check=True)
# mix sfx onto the untouched voice, burn the overlays
cmd = ["ffmpeg", "-v", "error", "-y", "-i", joined]
for _, n in sfx: cmd += ["-i", S8 + n + ".wav"]
parts = ["[0:a]apad=pad_dur=0.6[v0]"]
labels = "[v0]"
for k, (tt, n) in enumerate(sfx, 1):
    parts.append(f"[{k}:a]adelay={int(tt * 1000)}|{int(tt * 1000)}[s{k}]"); labels += f"[s{k}]"
parts.append(f"{labels}amix=inputs={len(sfx) + 1}:normalize=0,atrim=0:{TOTAL:.3f}[a]")
cmd += ["-filter_complex", ";".join(parts), "-map", "0:v", "-map", "[a]", "-vf", f"ass={ass}", "-c:v", "libx264", "-preset", "slow", "-crf", "19",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
subprocess.run(cmd, check=True)
print(out, round(TOTAL, 2), [(c, round(o, 2)) for c, (a, b, o) in off.items()])
