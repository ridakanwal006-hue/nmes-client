"""Gentle background clean-up that keeps the words intact.

The old denoise_clips.py subtracts a noise profile estimated from the quietest 35 % of frames. When the speaker talks
almost without pauses, those frames still contain speech, so the subtraction eats into the words (e.g. "comment the
word hungry" turned into "now what the word week").  This version:
  1. estimates the noise only from the quietest ~6 % of frames and subtracts it lightly (alpha 1.2, floor 0.15), then
  2. gates the pauses: inside speech (plus a small pad) the audio is untouched, outside it fades to near silence.
Run from a folder that has x/*.mp4 ; writes raw{n}.wav (original) and dn{n}.wav (cleaned).
"""
import subprocess, glob, numpy as np, wave

def rd(p):
    w = wave.open(p); return w.getframerate(), np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
def wr(p, sr, y):
    w = wave.open(p, 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()
N_ = 2048; H = 512; win = np.hanning(N_)
def stft(x):
    x = np.pad(x, (N_, N_)); return np.array([np.fft.rfft(x[i:i + N_] * win) for i in range(0, len(x) - N_, H)]).T
def istft(X, L):
    y = np.zeros((X.shape[1] - 1) * H + N_); ws = np.zeros_like(y)
    for j in range(X.shape[1]):
        y[j * H:j * H + N_] += np.fft.irfft(X[:, j]) * win; ws[j * H:j * H + N_] += win ** 2
    return (y / np.maximum(ws, 1e-6))[N_:N_ + L]
def sm(g):
    p = np.pad(g, 1, mode='edge'); return sum(p[a:a + g.shape[0], b:b + g.shape[1]] for a in range(3) for b in range(3)) / 9

ALPHA, FLOOR, QFRAC, PCT, HP = 1.2, 0.15, 0.06, 60, 100
PAD_BEFORE, PAD_AFTER, RAMP, GAP_GAIN = 0.06, 0.10, 0.04, 0.02

for n, f in enumerate(sorted(glob.glob('x/*.mp4'))):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', f, '-vn', '-ac', '1', '-ar', '48000', f'raw{n}.wav'])
    sr, x = rd(f'raw{n}.wav'); X = stft(x); M = np.abs(X); e = M.mean(0)
    quiet = np.argsort(e)[:max(3, int(len(e) * QFRAC))]
    Nz = np.percentile(M[:, quiet], PCT, axis=1, keepdims=True)
    g = sm(np.maximum(1 - ALPHA * Nz / (M + 1e-9), FLOOR)); g[:int(HP / (sr / N_))] = 0
    y = istft(X * g, len(x))
    # speech mask: threshold is relative to THIS clip's own background level (not to the loudest word), so a loud
    # background no longer counts as speech; frames next to speech that are only a little above the floor are kept
    # (soft consonants, word tails).
    w = int(0.02 * sr); en = np.array([20 * np.log10(np.sqrt(np.mean(y[i:i + w] ** 2)) + 1e-9) for i in range(0, len(y) - w, w)])
    n0 = np.percentile(en, 8)
    core = en > n0 + 14
    grow = en > n0 + 6
    sp = core.copy()
    for _ in range(12):                      # grow core into connected "a bit above floor" frames (max 12 frames each side)
        nb = np.r_[sp[1:], False] | np.r_[False, sp[:-1]]
        sp = sp | (nb & grow)
    mask = np.zeros(len(y))
    for i, v in enumerate(sp):
        if v: mask[max(0, int((i * w) - PAD_BEFORE * sr)):int((i + 1) * w + PAD_AFTER * sr)] = 1
    k = int(RAMP * sr); mask = np.convolve(mask, np.hanning(2 * k) / np.hanning(2 * k).sum(), mode='same')
    gain = GAP_GAIN + (1 - GAP_GAIN) * np.clip(mask, 0, 1)
    wr(f'dn{n}.wav', sr, y * gain)
    print(n, 'speech %', round(sp.mean() * 100), 'floor dB', round(float(n0), 1))
