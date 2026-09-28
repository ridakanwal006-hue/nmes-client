"""Speech checks for reel-edit, built on Whisper medium.en (sherpa-onnx).

  python3 asr.py text  clip.mp4                    full transcript
  python3 asr.py win   clip.mp4 '[[0,1.1],[1.1,2.3]]'   transcript of each window
  python3 asr.py end   clip.mp4 '[[0,"partner",0.4,1.3]]'  earliest t in [lo,hi] where
                                                     window [start,t] contains the word
  python3 asr.py env   clip.mp4 3.6 5.2             loudness (dB) every 40 ms, to see pauses
  python3 asr.py verify video.mp4 captions.ass      each caption vs what is said in its time (±50 ms)

Whisper tends to "finish" a word slightly before it is spoken, so treat `end`
results as a first guess and confirm with `win` and `env` (pauses are < -35 dB).
"""
import sys, os, re, json, wave, subprocess, tempfile
import numpy as np

MODEL = os.path.join(os.environ.get("MODEL_DIR", os.path.expanduser("~/.cache/reel-edit")),
                     "sherpa-onnx-whisper-medium.en", "medium.en-")
_rec = None

def load(path):
    wav = tempfile.mktemp(suffix=".wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "1", "-ar", "16000", wav], check=True)
    w = wave.open(wav)
    x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    os.remove(wav)
    return x

def run(x, a, b):
    global _rec
    if _rec is None:
        import sherpa_onnx
        _rec = sherpa_onnx.OfflineRecognizer.from_whisper(
            encoder=MODEL + "encoder.int8.onnx", decoder=MODEL + "decoder.int8.onnx",
            tokens=MODEL + "tokens.txt", language="en", task="transcribe", num_threads=4)
    s = _rec.create_stream()
    s.accept_waveform(16000, x[int(a * 16000):int(b * 16000)])
    _rec.decode_stream(s)
    return s.result.text.strip()

def sec(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)

if __name__ == "__main__":
    cmd, path = sys.argv[1], sys.argv[2]
    x = load(path)
    if cmd == "text":
        print(run(x, 0, len(x) / 16000))
    elif cmd == "win":
        for a, b in json.loads(sys.argv[3]):
            print(f"[{a}-{b}] {run(x, a, b)}")
    elif cmd == "end":
        for st, word, lo, hi in json.loads(sys.argv[3]):
            t = lo
            while t <= hi and not re.search(r"\b" + re.escape(word.lower()) + r"\b", run(x, st, t).lower()):
                t += 0.04
            print(f"{word}: {t:.2f}  ({run(x, st, t)})")
    elif cmd == "env":
        a, b = float(sys.argv[3]), float(sys.argv[4])
        for t in np.arange(a, b, 0.04):
            seg = x[int(t * 16000):int((t + 0.04) * 16000)]
            print(f"{t:.2f} {20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9):.0f}")
    elif cmd == "verify":
        for line in open(sys.argv[3], encoding="utf-8"):
            if not line.startswith("Dialogue") or ",Label," in line or ",Line," in line:
                continue
            p = line.split(",", 9)
            a, b = sec(p[1]), sec(p[2])
            cap = re.sub(r"\{[^}]*\}", "", p[9]).strip().replace("\\N", " ")
            # ±50 ms pad: a word ending right on a caption switch is otherwise dropped
            print(f"{a:6.2f}-{b:5.2f}  SAID: {run(x, max(a - 0.05, 0), b + 0.05):40s} CAPTION: {cap}")
