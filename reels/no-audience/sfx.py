import numpy as np, wave
SR = 48000
rng = np.random.default_rng(7)

def save(name, x, peak):
    x = x / (np.max(np.abs(x)) + 1e-9) * peak
    st = np.stack([x, x], 1)
    w = wave.open(name, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes()); w.close()

def env(n, a, d):  # attack/decay seconds
    t = np.arange(n) / SR
    return np.minimum(t / a, 1) * np.exp(-t / d)

def whoosh(dur=0.5):
    n = int(SR * dur); noise = rng.standard_normal(n)
    t = np.arange(n) / SR; fc = 300 + 5200 * np.sin(np.pi * t / dur) ** 2
    out = np.zeros(n); y = 0.0
    for i in range(n):
        a = 1 - np.exp(-2 * np.pi * fc[i] / SR); y += a * (noise[i] - y); out[i] = y
    return out * np.sin(np.pi * t / dur) ** 2

def tick(f=1900):
    n = int(SR * 0.06); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) * 0.8 + rng.standard_normal(n) * 0.25) * np.exp(-t / 0.008)

def click():
    n = int(SR * 0.05); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 3600 * t) + rng.standard_normal(n) * 0.5) * np.exp(-t / 0.005)

def chime(dur=1.4):
    n = int(SR * dur); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * t) for f, a in ((880, 1), (1320, .5), (1760, .35), (2640, .15)))
    return x * env(n, 0.008, 0.45)

def ding(dur=1.2):
    n = int(SR * dur); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t / d) for f, a, d in ((1568, 1, .5), (4327, .3, .18), (2350, .4, .3)))
    return x * np.minimum(t / 0.004, 1)

for name, x, pk in (("whoosh", whoosh(), .06), ("tick", tick(), .06), ("chime", chime(), .07), ("click", click(), .06), ("ding", ding(), .07)):
    save(f"{name}.wav", x, pk)
print("ok")
