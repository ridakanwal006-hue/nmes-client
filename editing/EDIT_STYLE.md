# Editing style copied from the reference reel (measured)

Measured on the uploaded 71.8 s reel (720x1280, 30 fps). Numbers below are measurements, not guesses.

| Element | Reference | How reel_edit.py does it |
|---|---|---|
| Cuts | Single medium shot, only 3 scene changes (7.3, 7.7, 36.0 s) | No jump cuts |
| Hook | Red neon text TYPES in from the left over the chest, then a small white italic sub-line | Per-character reveal, glow layer, sub-line fades in at 2.0 s, hook ends at 4.9 s |
| Body captions | One word at a time, about 2.0 per second, median 0.37 s on screen, white, around 65% height | Same, Inter SemiBold 64 px, hard cut per word |
| Number callouts | Red typed text ("number three") in the middle of the video | Red typed "NUMBER ONE / TWO / THREE" for 1.3 s plus a quiet sub-hit |
| Glitch | Flash and negative frames at 7.3-7.6 s (not at 4 s) | RGB split, negative frame, white flash at the first pause after 7 s, whoosh and zap |
| Punch-ins | Zoom-ins at about 17-24, 30-35, 42-44 and 49-56 s (of 72 s) | 5 punch-ins of +22 percent, 0.35 s ease, scaled to the reel length |
| Sound | Voice around -16 dB RMS, quiet bed under it | Synthesised drone bed with sidechain ducking, final -14 LUFS |

## Run

```
python3 -I reel_edit.py voice.wav reel1.json out.mp4 [character_clip.mp4]
```

Without a character clip it renders a dark preview card so you can check timing, captions and sound.

## Known limits

- Word timings are estimated (syllables aligned to detected pauses). There is no speech-to-text here, so check captions against the voice before posting.
- Font is Inter (Poppins is not installed).
- The reference footage and lines are not reused. Only the editing style is copied.
