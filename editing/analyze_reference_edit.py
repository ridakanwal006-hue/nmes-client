import subprocess, numpy as np, sys
f = sys.argv[1]
def frames(vf, w, h):
    raw = subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-an','-vf',vf,'-f','rawvideo','-pix_fmt','gray','-'],capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)
fps = 30
# 1) whole-frame brightness + non-black coverage (zoom proxy) + flash detection
F = frames('fps=30,scale=90:160', 90, 160)
bright = F.mean((1,2)); cover = (F > 40).mean((1,2))
print('frames', len(F), 'dur %.1fs' % (len(F)/fps))
d = np.abs(np.diff(bright)); spikes = np.where(d > 12)[0]
print('brightness spikes (flash/negative) at s:', sorted(set(np.round(spikes/fps, 2)))[:12])
# zoom timeline: smooth coverage per second
cs = cover[:len(F)//fps*fps].reshape(-1, fps).mean(1)
base = np.median(cs)
print('zoom proxy (coverage vs median) per 5s:', ' '.join('%d:%+.0f%%' % (i*5, 100*(cs[i*5:(i+1)*5].mean()/base-1)) for i in range(len(cs)//5)))
big = [i for i, c in enumerate(cs) if c > base*1.10]
print('seconds with >10%% zoom-in: %s' % big)
# 2) caption region changes (one-word captions): crop y 60-72%
C = frames('fps=30,crop=720:150:0:790,scale=180:38', 180, 38)
cd = np.abs(np.diff(C, axis=0)).mean((1,2)); ev = np.where(cd > 3.0)[0]
# merge events closer than 4 frames
merged = [ev[0]] if len(ev) else []
for e in ev[1:]:
    if e - merged[-1] > 4: merged.append(e)
print('caption changes: %d in %.1fs => %.2f/s' % (len(merged), len(C)/fps, len(merged)/(len(C)/fps)))
gaps = np.diff(merged)/fps
print('caption on-screen median %.2fs  p10 %.2fs p90 %.2fs' % (np.median(gaps), np.percentile(gaps,10), np.percentile(gaps,90)))
# 3) hook region (y 40-55%) activity in first 4 s
H = frames('fps=30,crop=720:260:0:500,scale=180:65', 180, 65)
ha = np.abs(np.diff(H[:150], axis=0)).mean((1,2))
print('hook activity frames (typewriter) active until ~%.2fs' % (np.where(ha > 1.0)[0].max()/fps if (ha>1.0).any() else 0))
