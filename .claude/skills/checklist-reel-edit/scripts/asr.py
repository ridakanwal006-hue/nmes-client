"""Speech tools for checklist-reel-edit.

Two models (installed by setup.sh):
  Parakeet TDT 0.6B v2 - word timestamps (80 ms steps), used to place cuts and captions.
  Whisper medium.en    - second opinion, used to double-check the words.

  python3 asr.py words  clip.mp4 [words.json]      word list with start/end (seconds)
  python3 asr.py text   clip.mp4                   Whisper transcript
  python3 asr.py win    clip.mp4 '[[0,1.1],...]'   Whisper transcript of each window
  python3 asr.py env    clip.mp4 3.6 5.2           loudness every 40 ms (pauses < -35 dB)
  python3 asr.py verify video.mp4 captions.ass     captions vs. what is said, word by word

`verify` transcribes the finished video with Parakeet, lines every caption word up with the
spoken words in order, and reports any word that differs or sits outside its caption's time
(±0.25 s). It also compares the whole text with Whisper; a word where the two models disagree
is printed as CHECK - listen to it with `win` before trusting either model.
"""
import sys, os, re, json, subprocess, difflib
import numpy as np

CACHE = os.environ.get("MODEL_DIR", os.path.expanduser("~/.cache/reel-edit"))
WHISPER = os.path.join(CACHE, "sherpa-onnx-whisper-medium.en", "medium.en-")
PARAKEET = os.path.join(CACHE, "sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8", "")
_wh = _pk = None

def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768

def whisper(x, a=0, b=None):
    global _wh
    if _wh is None:
        import sherpa_onnx
        _wh = sherpa_onnx.OfflineRecognizer.from_whisper(
            encoder=WHISPER + "encoder.int8.onnx", decoder=WHISPER + "decoder.int8.onnx",
            tokens=WHISPER + "tokens.txt", language="en", task="transcribe", num_threads=4)
    b = len(x) / 16000 if b is None else b
    s = _wh.create_stream(); s.accept_waveform(16000, x[int(a * 16000):int(b * 16000)])
    _wh.decode_stream(s)
    return s.result.text.strip()

def words(x):
    """[{'w': 'texted', 's': 0.32, 'e': 0.56}, ...] - times in seconds from the start of x.
    Long files are decoded in 25 s windows that overlap by 2 s."""
    global _pk
    if _pk is None:
        import sherpa_onnx
        _pk = sherpa_onnx.OfflineRecognizer.from_transducer(
            encoder=PARAKEET + "encoder.int8.onnx", decoder=PARAKEET + "decoder.int8.onnx",
            joiner=PARAKEET + "joiner.int8.onnx", tokens=PARAKEET + "tokens.txt",
            model_type="nemo_transducer", num_threads=4)
    out, dur, a = [], len(x) / 16000, 0.0
    while True:
        b = min(a + 25, dur)
        s = _pk.create_stream(); s.accept_waveform(16000, x[int(a * 16000):int(b * 16000)]); _pk.decode_stream(s)
        r, ws, cur = s.result, [], None
        for tok, t, d in zip(r.tokens, r.timestamps, r.durations):
            t += a
            if tok.startswith(" ") or cur is None:
                if cur: ws.append(cur)
                cur = {"w": tok.strip(), "s": round(t, 2), "e": round(t + d, 2)}
            else:
                cur["w"] += tok; cur["e"] = round(t + d, 2)
        if cur: ws.append(cur)
        # windows overlap by 2 s; each keeps the words that start in its half of the overlap
        lo = a + 1 if a > 0 else -1
        hi = b - 1 if b < dur else dur + 1
        out += [w for w in ws if lo <= w["s"] < hi]
        if b >= dur: break
        a = b - 2
    # Parakeet stamps the very first word at 0.0 s even after leading silence: move it to the
    # first 40 ms frame louder than -35 dB (before the next word).
    if out and out[0]["s"] < 0.1:
        lim = out[1]["s"] if len(out) > 1 else out[0]["e"] + 1
        for t in np.arange(0, lim, 0.04):
            seg = x[int(t * 16000):int((t + 0.04) * 16000)]
            if len(seg) and 20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9) > -35:
                out[0]["s"] = round(max(t - 0.04, 0), 2)
                out[0]["e"] = round(max(out[0]["e"], out[0]["s"] + 0.16), 2)
                break
    # punctuation-only tokens join the word before them
    merged = []
    for w in out:
        if merged and re.fullmatch(r"[^\w']+", w["w"]):
            merged[-1]["w"] += w["w"]; merged[-1]["e"] = w["e"]
        elif w["w"]:
            merged.append(w)
    return merged

def norm(t):
    t = t.lower().replace("’", "'")
    nums = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six",
            "7": "seven", "8": "eight", "9": "nine", "10": "ten"}
    return [nums.get(w, w) for w in re.findall(r"[a-z0-9']+", t.replace("-", " "))]

def sec(t):
    h, m, s = t.split(":"); return int(h) * 3600 + int(m) * 60 + float(s)

def captions(ass):
    """Caption events (style Cap) from a .ass file: [(start, end, text)]."""
    out = []
    for line in open(ass, encoding="utf-8"):
        if line.startswith("Dialogue") and ",Cap," in line:
            p = line.split(",", 9)
            out.append((sec(p[1]), sec(p[2]), re.sub(r"\{[^}]*\}", "", p[9]).strip().replace("\\N", " ")))
    return out

def verify(video, ass):
    x = load(video)
    said = words(x)
    sw = [(n, w) for w in said for n in norm(w["w"])]
    cw = [(n, c) for c in captions(ass) for n in norm(c[2])]
    sm = difflib.SequenceMatcher(a=[n for n, _ in cw], b=[n for n, _ in sw], autojunk=False)
    problems = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                (n, c), (_, w) = cw[i1 + k], sw[j1 + k]
                if not (c[0] - 0.25 <= w["s"] <= c[1] + 0.25):
                    problems += 1
                    print(f"TIME  '{n}' said at {w['s']:.2f}s but caption '{c[2]}' is {c[0]:.2f}-{c[1]:.2f}s")
        else:
            problems += 1
            cap = " ".join(n for n, _ in cw[i1:i2]) or "-"
            spk = " ".join(n for n, _ in sw[j1:j2]) or "-"
            at = f"{sw[j1][1]['s']:.2f}s" if j1 < len(sw) else "end"
            print(f"WORD  caption '{cap}'  vs  said '{spk}'  (at {at})")
    wt = norm(whisper(x)); pt = [n for n, _ in sw]
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=pt, b=wt, autojunk=False).get_opcodes():
        if op != "equal":
            at = f"{sw[i1][1]['s']:.2f}s" if i1 < len(sw) else "end"
            print(f"CHECK models disagree at {at}: parakeet '{' '.join(pt[i1:i2]) or '-'}' / whisper '{' '.join(wt[j1:j2]) or '-'}'")
    print(f"{len(cw)} caption words, {len(sw)} spoken words, {problems} caption problem(s)")
    return problems

if __name__ == "__main__":
    cmd, path = sys.argv[1], sys.argv[2]
    if cmd == "verify":
        sys.exit(1 if verify(path, sys.argv[3]) else 0)
    x = load(path)
    if cmd == "words":
        ws = words(x)
        if len(sys.argv) > 3:
            json.dump(ws, open(sys.argv[3], "w"), indent=0)
        for w in ws: print(f"{w['s']:6.2f} {w['e']:6.2f} {w['w']}")
    elif cmd == "text":
        print(whisper(x))
    elif cmd == "win":
        for a, b in json.loads(sys.argv[3]):
            print(f"[{a}-{b}] {whisper(x, a, b)}")
    elif cmd == "env":
        a, b = float(sys.argv[3]), float(sys.argv[4])
        for t in np.arange(a, b, 0.04):
            seg = x[int(t * 16000):int((t + 0.04) * 16000)]
            print(f"{t:.2f} {20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9):.0f}")
