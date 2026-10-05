"""Small sound-effect library, generated with ffmpeg (no downloads, no licences).

  python3 sfx.py [out_dir]        writes whoosh.wav, pop.wav, tick.wav, ding.wav, riser.wav

  whoosh - soft air sweep (title / panel coming in)
  pop    - short bubble pop (a checklist item revealing, a keyword)
  tick   - tiny click (caption beat, subtle emphasis)
  ding   - soft bell (final point / "that's the key")
  riser  - 0.8 s rising noise (lead-in to a reveal)

The reference video uses no music and no effects, so keep effects quiet (about -20 dB under
the voice) and rare: one per visual event, never on top of a key word. User-supplied effects
(.wav/.mp3) can be used the same way by file path.
"""
import os, subprocess, sys

SR = 48000
RECIPES = {
    # pink noise through a band-pass, swelled in and out
    "whoosh": ["-f", "lavfi", "-i", f"anoisesrc=c=pink:r={SR}:a=0.5:d=0.45",
               "-af", "bandpass=f=1800:width_type=h:w=2400,afade=t=in:d=0.22:curve=qsin,afade=t=out:st=0.22:d=0.23:curve=qsin,volume=6"],
    # falling sine blip with fast decay
    "pop": ["-f", "lavfi", "-i",
            f"aevalsrc='0.9*sin(2*PI*(380*t+2600*(1-exp(-t*55))/55))*exp(-t*38)':s={SR}:d=0.14"],
    # very short filtered click
    "tick": ["-f", "lavfi", "-i", f"aevalsrc='0.8*sin(2*PI*2400*t)*exp(-t*160)':s={SR}:d=0.05"],
    # two-partial bell with a slow decay
    "ding": ["-f", "lavfi", "-i",
             f"aevalsrc='0.45*(sin(2*PI*1318*t)+0.5*sin(2*PI*1976*t)+0.25*sin(2*PI*2637*t))*exp(-t*5)':s={SR}:d=0.9"],
    # noise rising in pitch and level
    "riser": ["-f", "lavfi", "-i", f"anoisesrc=c=white:r={SR}:a=0.4:d=0.8",
              "-af", "highpass=f=600,lowpass=f=7000,afade=t=in:d=0.75:curve=exp,afade=t=out:st=0.75:d=0.05,volume=2.5"],
}

def build(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for name, args in RECIPES.items():
        path = os.path.join(out_dir, name + ".wav")
        if not os.path.exists(path):
            subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-ac", "2", "-ar", str(SR), path], check=True)
    return out_dir

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/.cache/reel-edit/sfx")))
