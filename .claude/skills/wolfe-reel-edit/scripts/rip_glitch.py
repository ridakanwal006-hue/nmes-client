"""Paper-rip glitch transition (copied from the user's reference reel).

A jagged white paper strip sweeps left -> right across the picture; behind the first strip the frame turns
into a black-and-white halftone, a second strip follows and brings the normal picture back (~0.6 s total).
No music, only a synthesized paper-rip sound.
"""
import subprocess, wave
import numpy as np

W, H, FPS = 1080, 1920, 30
LEN = 0.6


def _smooth(x):
    x = np.clip(x, 0, 1)
    return x * x * (3 - 2 * x)


def _wobble(rng, amp, smooth=9):
    """jagged edge profile along y (random walk, high-passed)"""
    w = np.cumsum(rng.normal(0, 1, H))
    w = w - np.convolve(w, np.ones(220) / 220, mode='same')
    w = np.convolve(w, np.ones(smooth) / smooth, mode='same')
    return w / (np.abs(w).max() + 1e-6) * amp


def _halftone(img):
    g = (0.30 * img[..., 0] + 0.59 * img[..., 1] + 0.11 * img[..., 2]) / 255.0
    g = np.clip((g - 0.06) * 1.7, 0, 1)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    c, s, cell = np.cos(0.785), np.sin(0.785), 7.0
    u = (xx * c + yy * s) / cell
    v = (-xx * s + yy * c) / cell
    pat = (np.cos(2 * np.pi * u) + np.cos(2 * np.pi * v)) / 4 + 0.5
    ht = (g > pat * 0.85 + 0.05).astype(np.float32)
    out = 0.72 * ht + 0.28 * g
    out = out * 232 + 10
    return np.repeat(out[..., None], 3, axis=2)


def apply(frames, seed=7):
    rng = np.random.default_rng(seed)
    n = len(frames)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    wob_a, wob_b = _wobble(rng, 46), _wobble(rng, 46)
    wid_a = 46 + 30 * np.abs(_wobble(rng, 1.0))
    wid_b = 40 + 26 * np.abs(_wobble(rng, 1.0))
    wob_a2, wob_b2 = _wobble(rng, 30, 5), _wobble(rng, 30, 5)
    ht_cache = {}
    out = []
    for k, fr in enumerate(frames):
        p = k / max(n - 1, 1)
        xa = -0.12 * W + 1.30 * W * _smooth(p / 0.64)          # first tear: brings the halftone in
        xb = -0.16 * W + 1.32 * W * _smooth((p - 0.30) / 0.66)  # second tear: takes it away
        img = fr.astype(np.float32)
        # tiny camera shake while the paper rips
        sh = int(round(7 * np.sin(p * 18) * (1 - p)))
        if sh:
            img = np.roll(img, sh, axis=1)
        ht = _halftone(img)
        ea = xa + wob_a[:, None]
        eb = xb + wob_b[:, None]
        inside = (xx < ea) & (xx >= eb)                      # between the two tears: halftone
        res = np.where(inside[..., None], ht, img)
        paper = np.zeros((H, W), np.float32)
        shadow = np.zeros((H, W), np.float32)
        for edge, wid, wob2 in ((ea, wid_a[:, None], wob_a2[:, None]), (eb, wid_b[:, None], wob_b2[:, None])):
            for dx, wd in ((0, wid), (-(0.07 * W) + wob2 * 0, wid * 0.35)):
                c = edge + dx
                m = (np.abs(xx - c) < wd / 2).astype(np.float32)
                paper = np.maximum(paper, m)
                shadow = np.maximum(shadow, ((xx > c + wd / 2) & (xx < c + wd / 2 + 9)).astype(np.float32))
        res = res * (1 - 0.55 * shadow[..., None] * (1 - paper[..., None]))
        grain = rng.normal(0, 7, (H, W)).astype(np.float32)
        pv = np.clip(238 + grain, 0, 255)[..., None]
        res = np.where(paper[..., None] > 0, pv, res)
        out.append(np.clip(res, 0, 255).astype(np.uint8))
    return out


def make_sfx(path, sr=48000):
    """synthesized paper-rip sound: two crackling rips + a soft thud, ~0.7 s, no music"""
    rng = np.random.default_rng(3)
    n = int(0.7 * sr)
    t = np.arange(n) / sr

    def rip(t0, dur, gain):
        env = np.zeros(n)
        i0, i1 = int(t0 * sr), int((t0 + dur) * sr)
        pulses = (rng.random(i1 - i0) < 0.012) * rng.random(i1 - i0)
        pulses = np.convolve(pulses, np.hanning(180), mode='same')
        pulses = pulses / (pulses.max() + 1e-9)
        shape = np.hanning(i1 - i0) ** 0.6
        env[i0:i1] = (0.35 + 0.65 * pulses) * shape
        noise = rng.normal(0, 1, n)
        spec = np.fft.rfft(noise)
        f = np.fft.rfftfreq(n, 1 / sr)
        spec *= ((f > 900) & (f < 9000)).astype(float) * (1 / (1 + f / 5000))
        return np.fft.irfft(spec, n) * env * gain

    y = rip(0.0, 0.34, 1.0) + rip(0.17, 0.36, 0.85)
    y += 0.5 * np.sin(2 * np.pi * (70 + 40 * np.exp(-t * 20)) * t) * np.exp(-t * 14)
    y = y / (np.abs(y).max() + 1e-9) * 0.75
    w = wave.open(path, 'wb')
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((y * 32767).astype(np.int16).tobytes()); w.close()


def run_on_video(src, dst, start, length=LEN):
    """read frames [start, start+length) of src (must be 1080x1920 @30 fps), rip them, overlay back, keep audio"""
    n = int(round(length * FPS))
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-vf', f'trim=start={start}:end={start + length},setpts=PTS-STARTPTS,fps={FPS}',
                          '-frames:v', str(n), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    frames = list(np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3))
    res = apply(frames)
    enc = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', dst + '.rip.mp4'], stdin=subprocess.PIPE)
    for f in res:
        enc.stdin.write(f.tobytes())
    enc.stdin.close(); enc.wait()
    end = start + len(res) / FPS
    fc = f"[1:v]setpts=PTS-STARTPTS+{start}/TB[g];[0:v][g]overlay=enable='between(t,{start},{end})':eof_action=pass[v]"
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-i', dst + '.rip.mp4', '-filter_complex', fc, '-map', '[v]', '-map', '0:a',
                    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', dst], check=True)
