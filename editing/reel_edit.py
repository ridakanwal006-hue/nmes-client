#!/usr/bin/env python3
"""Reel edit template built from measurements of the reference reel.
Usage: reel_edit.py voice.wav script.txt out.mp4 [character_clip.mp4]
If no character clip is given a dark placeholder card is used (so you can preview timing, captions and sound)."""
import sys, re, json, subprocess, tempfile, os
voice, scriptf, out = sys.argv[1:4]
clip = sys.argv[4] if len(sys.argv) > 4 else None
tmp = tempfile.mkdtemp()
def run(c): subprocess.run(c, shell=True, check=True)
dur = float(subprocess.check_output(f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{voice}"', shell=True))
cfg = json.load(open(scriptf))
words = cfg['script'].split()
# ---- word timings: syllable-proportional over detected speech segments
log = subprocess.run(f'ffmpeg -hide_banner -i "{voice}" -af silencedetect=n=-38dB:d=0.18 -f null - 2>&1', shell=True, capture_output=True, text=True).stdout
sil = [(float(a), float(a) + float(b)) for a, b in re.findall(r'silence_start: ([\d.]+)\s*\n?.*?silence_duration: ([\d.]+)', log)] if False else []
starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', log)]
ends = [(float(e), float(d)) for e, d in re.findall(r'silence_end: ([\d.]+) \| silence_duration: ([\d.]+)', log)]
sil = [(e - d, e) for e, d in ends]
segs, t0 = [], 0.0
for a, b in sil:
    if a - t0 > 0.05: segs.append((t0, a))
    t0 = b
if dur - t0 > 0.05: segs.append((t0, dur))
seg_len = [b - a for a, b in segs]; total = sum(seg_len)
def syl(w):
    w = re.sub(r'[^a-z]', '', w.lower()); n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1 and not w.endswith('le'): n -= 1
    return max(n, 1)
sy = [syl(w) for w in words]; S = sum(sy)
# DP: assign consecutive words to speech segments; segment duration should match its syllables,
# and a segment should preferably end on a punctuated word (pause after , . ? : ...)
rate = total / S
n, m = len(segs), len(words)
punct = [bool(re.search(r'[,.?!:;]$|\.\.\.', w)) for w in words]
cs = [0]
for x in sy: cs.append(cs[-1] + x)
INF = 1e18
best = [[INF] * (m + 1) for _ in range(n + 1)]; back = [[0] * (m + 1) for _ in range(n + 1)]
best[0][0] = 0.0
for j in range(1, n + 1):
    L = seg_len[j - 1]
    for k in range(1, m + 1):
        for i in range(0, k):
            if best[j - 1][i] >= INF: continue
            exp = (cs[k] - cs[i]) * rate
            c = abs(L - exp) / max(L, 0.2)
            if j < n and not punct[k - 1]: c += 0.6      # pause after a word without punctuation: unlikely
            if j == n and k != m: continue
            v = best[j - 1][i] + c
            if v < best[j][k]: best[j][k] = v; back[j][k] = i
bounds = []; k = m
for j in range(n, 0, -1):
    i = back[j][k]; bounds.append((i, k)); k = i
bounds.reverse()
W = []
for (i, k), (a0, b0) in zip(bounds, segs):
    tot = sum(sy[i:k]) or 1; c0 = 0
    for w, sv in zip(words[i:k], sy[i:k]):
        W.append([w, a0 + (b0 - a0) * c0 / tot, a0 + (b0 - a0) * (c0 + sv) / tot]); c0 += sv
if os.environ.get('SHOW'):
    for (i, k), (a0, b0) in zip(bounds, segs): print('%5.2f-%5.2f  %s' % (a0, b0, ' '.join(words[i:k])))
json.dump(W, open(f'{tmp}/words.json', 'w'))
# ---- events
hook_end = cfg.get('hook_end', 4.9)
glitch = cfg.get('glitch') or next((a for a, b in sil if a > 7.0), 7.4)
punch = cfg.get('punch', [])
hits = []  # callouts for "one/two/three"
names = {'one:': 'NUMBER ONE', 'two:': 'NUMBER TWO', 'three...': 'NUMBER THREE', 'three': 'NUMBER THREE'}
for w, a, b in W:
    if w.lower() in names and a > hook_end: hits.append((a, names[w.lower()]))
# ---- voice (raw Brian, only loudness) + synthesized bed and sfx
run(f'ffmpeg -y -loglevel error -i "{voice}" -af anull -ar 48000 "{tmp}/voice.wav"')
bed = ("aevalsrc='0.5*sin(2*PI*55*t)+0.35*sin(2*PI*82.5*t+0.4*sin(2*PI*0.1*t))+0.18*sin(2*PI*110.4*t)"
       f"+0.25*sin(2*PI*55*t)*pow(0.5+0.5*sin(2*PI*(80/60)*t),6)':d={dur+1}:s=48000,lowpass=f=900,aecho=0.8:0.6:350:0.25,volume=0.5")
run(f'ffmpeg -y -loglevel error -f lavfi -i "{bed}" "{tmp}/bed.wav"')
sfx = []
def add(lavfi, af, t, name):
    run(f'ffmpeg -y -loglevel error -f lavfi -i "{lavfi}" -af "{af}" -ar 48000 "{tmp}/{name}.wav"'); sfx.append((f'{tmp}/{name}.wav', t))
add("anoisesrc=d=0.9:c=white:a=0.5", "highpass=f=1500,afade=t=in:d=0.5,afade=t=out:st=0.5:d=0.4,volume=0.6", max(glitch - 0.6, 0), 'whoosh')
add("aevalsrc='0.9*sin(2*PI*(60+900*exp(-14*t))*t)':d=0.5:s=48000", "afade=t=out:st=0.2:d=0.3", glitch, 'zap')
for i, (t, _) in enumerate(hits):
    add("aevalsrc='0.9*sin(2*PI*(45+60*exp(-9*t))*t)':d=0.7:s=48000", "afade=t=out:st=0.1:d=0.6,volume=0.7", t, f'hit{i}')
ins = f'-i "{tmp}/voice.wav" -i "{tmp}/bed.wav" ' + ' '.join(f'-i "{p}"' for p, _ in sfx)
fc = "[0:a]asplit=2[v][vsc];[1:a]volume=-24dB[b0];[b0][vsc]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[bd]"
labs = ['[v]', '[bd]']
for i, (_, t) in enumerate(sfx):
    fc += f";[{i+2}:a]adelay={int(t*1000)}|{int(t*1000)},volume=-8dB[s{i}]"; labs.append(f'[s{i}]')
fc += f";{''.join(labs)}amix=inputs={len(labs)}:normalize=0,loudnorm=I=-14:TP=-1.0:LRA=7[a]"
run(f'ffmpeg -y -loglevel error {ins} -filter_complex "{fc}" -map "[a]" -t {dur} "{tmp}/mix.wav"')
# ---- captions (ASS)
def ts(t): return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
def type_events(text, pos_y, st, en, dt, fs=None):
    """Typewriter: text is always laid out in full (stays centred); not-yet-typed characters are fully transparent."""
    ev = []
    n = len(text); fst = f'\\fs{fs}' if fs else ''
    for i in range(1, n + 1):
        a = st + (i - 1) * dt; b = en if i == n else st + i * dt
        rest = '{\\alpha&HFF&}' + text[i:] if i < n else ''
        ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},Glow,,0,0,0,,{{\\pos(540,{pos_y})\\blur22{fst}\\alpha&H70&}}{text[:i]}{rest}")
        rest2 = '{\\alpha&HFF&}' + text[i:] if i < n else ''
        ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},Red,,0,0,0,,{{\\pos(540,{pos_y})\\blur1{fst}}}{text[:i]}{rest2}")
    return ev
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 2", "",
 "[V4+ Styles]", "Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding",
 "Style: Red,Inter ExtraBold,100,&H00271EFF,&HFF271EFF,&H00271EFF,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,40,40,0,1",
 "Style: Glow,Inter ExtraBold,100,&H00271EFF,&HFF271EFF,&H00271EFF,&H00000000,0,0,0,0,100,100,0,0,1,14,0,5,40,40,0,1",
 "Style: Sub,Inter Medium,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,1,0,0,100,100,0,0,1,0,3,5,60,60,0,1",
 "Style: Body,Inter SemiBold,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H99000000,0,0,0,0,100,100,0,0,1,0,3,5,60,60,0,1",
 "", "[Events]", "Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text"]
for i, line in enumerate(cfg['hook_red']):
    y = 880 + i * 112; st = i * 0.85 + 0.1
    ass += type_events(line, y, st, hook_end, 0.05)
for i, line in enumerate(cfg['hook_sub']):
    ass.append(f"Dialogue: 1,{ts(2.0)},{ts(hook_end)},Sub,,0,0,0,,{{\\pos(540,{1200 + i*76})\\fad(200,150)}}{line}")
for t, label in hits:   # red typed callout, ~1.3 s, at about 56% height
    ass += type_events(label, 1080, t, t + 1.3, 0.045, fs=84)
for i, (w, a, b) in enumerate(W):
    if a < hook_end: continue
    end = min(b + 0.06, W[i+1][1] if i + 1 < len(W) else b + 0.3)
    ass.append(f"Dialogue: 0,{ts(a)},{ts(max(end, a + 0.12))},Body,,0,0,0,,{{\\pos(540,1250)}}{w}")
open(f'{tmp}/cap.ass', 'w').write('\n'.join(ass))
# ---- video
if clip: src = f'-i "{clip}"'
else:
    src = (f'-f lavfi -i "color=c=0x0a0a0c:s=1080x1920:r=30:d={dur},'
           "drawtext=fontfile=/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf:text='WOLFE':fontsize=260:fontcolor=white@0.05:x=(w-text_w)/2:y=1500,"
           "drawtext=fontfile=/usr/share/fonts/opentype/inter/Inter-Medium.otf:text='PREVIEW - character clip goes here':fontsize=34:fontcolor=white@0.35:x=(w-text_w)/2:y=120\"")
z = '1' + ''.join(f"+0.22*clip((t-{a})/0.35,0,1)*clip(({b}-t)/0.35,0,1)" for a, b in punch)
vf = ("scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
      f"scale=w='iw*({z})':h='ih*({z})':eval=frame,crop=1080:1920,"
      "curves=all='0/0 0.12/0.06 0.5/0.52 0.88/0.95 1/1',eq=saturation=0.93:contrast=1.06,vignette=angle=PI/4.5,"
      f"rgbashift=rh=-14:bh=14:gh=4:enable='between(t,{glitch},{glitch+0.3})',"
      f"negate=enable='between(t,{glitch+0.1},{glitch+0.16})',"
      f"eq=brightness=0.45:enable='between(t,{glitch+0.16},{glitch+0.2})',"
      f"ass={tmp}/cap.ass:fontsdir=/usr/share/fonts")
run(f'ffmpeg -y -loglevel error {src} -i "{tmp}/mix.wav" -vf "{vf}" -map 0:v -map 1:a -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -t {dur} -movflags +faststart "{out}"')
print('OK', out, 'glitch', round(glitch, 2), 'hits', [round(h[0], 2) for h in hits], 'words', len(W))
