import sys, subprocess, re, random
raw, out = sys.argv[1], sys.argv[2]
mode = sys.argv[3] if len(sys.argv) > 3 else 'dry'
W = 'voice'
def run(c): subprocess.run(c, shell=True, check=True)
# 1) find pauses in the raw voiceover
log = subprocess.run(f'ffmpeg -hide_banner -i {raw} -af silencedetect=n=-36dB:d=0.28 -f null - 2>&1', shell=True, capture_output=True, text=True).stdout
ends = [float(e) for e, d in re.findall(r'silence_end: ([\d.]+) \| silence_duration: ([\d.]+)', log) if float(d) >= 0.5]
print('pauses found:', len(ends))
# 2) breath samples (band-passed noise, soft attack, slow decay) in 3 variants
for i, (f1, f2, d) in enumerate([(350, 3200, 0.34), (300, 2800, 0.40), (400, 3500, 0.30)]):
    run(f'ffmpeg -y -loglevel error -f lavfi -i "anoisesrc=d={d}:c=pink:a=0.5:seed={i+3}" '
        f'-af "highpass=f={f1},lowpass=f={f2},afade=t=in:d={d*0.55},afade=t=out:st={d*0.55}:d={d*0.45},volume=0.55" -ar 48000 -ac 1 {W}/breath{i}.wav')
# 3) natural room impulse response (decaying filtered noise, 0.45 s)
run(f'ffmpeg -y -loglevel error -f lavfi -i "anoisesrc=d=0.45:c=white:a=0.5:seed=9" '
    f'-af "lowpass=f=2200,highpass=f=260,afade=t=in:d=0.09,afade=t=out:st=0.05:d=0.55:curve=exp,adelay=45|45" -ar 48000 -ac 1 {W}/ir.wav')
# 4) gentle voice chain (less pitch shift, light compression, almost no saturation) + convolution room
if mode.startswith("fierce"):
    voice = ("highpass=f=60,equalizer=f=100:t=h:w=100:g=6.5,equalizer=f=170:t=q:w=1.0:g=2.0,"
             "equalizer=f=350:t=q:w=1.2:g=-2.0,equalizer=f=3000:t=q:w=0.8:g=2.5,equalizer=f=5200:t=q:w=0.8:g=1.5,"
             "lowpass=f=10000,acompressor=threshold=-27dB:ratio=4.5:attack=8:release=130:makeup=6,"
             "aeval=val(0)+0.10*tanh(3*val(0)):c=same,alimiter=limit=0.9")
else:
    voice = ("highpass=f=70,"
             + ("" if mode.startswith("clean") else "rubberband=pitch=0.95:formant=preserved,") + "equalizer=f=95:t=h:w=100:g=4.8,equalizer=f=170:t=q:w=1.0:g=1.5,"
             "equalizer=f=350:t=q:w=1.2:g=-1.5,equalizer=f=2500:t=q:w=0.8:g=-2,lowpass=f=9000,"
             "acompressor=threshold=-24dB:ratio=2.5:attack=15:release=200:makeup=3,"
             "aeval=val(0)+0.04*tanh(2*val(0)):c=same")
if mode.endswith('tail'):
    fc = f"[0:a]{voice},asplit[d][w0];[w0][1:a]afir=dry=0:wet=10,volume=0.9[w];[d][w]amix=inputs=2:weights=1 0.10:normalize=0[v]"
else:
    fc = f"[0:a]{voice},acopy[v]"
ins = f'-i {raw} -i {W}/ir.wav '
labs = ['[v]']
rnd = random.Random(7)
for i, t in enumerate(ends):
    k = rnd.randrange(3); start = max(t - 0.36, 0)   # inhale just before the next phrase
    ins += f'-i {W}/breath{k}.wav '
    fc += f";[{i+2}:a]adelay={int(start*1000)}|{int(start*1000)},volume=-17dB[b{i}]"; labs.append(f'[b{i}]')
fc += f";{''.join(labs)}amix=inputs={len(labs)}:normalize=0,alimiter=limit=0.89,loudnorm=I=-14:TP=-1.5:LRA=9[a]"
run(f'ffmpeg -y -loglevel error {ins} -filter_complex "{fc}" -map "[a]" -ac 1 -ar 48000 -b:a 192k {out}')
print('done', out)
