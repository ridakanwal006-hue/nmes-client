---
name: reel-edit
description: Edit the user's raw talking-head / podcast clips into a vertical 9:16 Reel/Short in their approved style - jump-cut punch-in zooms, black & white on the negative/"overthinking" beat, big bold Montserrat captions with yellow keywords, white label boxes with a red ✖, tilted pop titles, red strike-through reframes - with every caption checked against the voice. Use when the user uploads clips (and optionally a reference video) and asks to edit them, "is style mein edit karo", add captions, or make a reel.
---

# Reel edit (approved style)

The user writes in Roman Urdu; reply in Roman Urdu, keep it short, and send the finished
video with SendUserFile. Their priority is **"without any mistake"**: a caption that does not
match the voice is the worst failure. Never guess a word - check it against the audio.

## 1. Setup (every new session)

```bash
bash .claude/skills/reel-edit/scripts/setup.sh
```
Installs ffmpeg, Montserrat fonts, sherpa-onnx + Pillow, and Whisper medium.en (~1.9 GB download,
from GitHub because Hugging Face is blocked here). Uploaded files are under `/root/.claude/uploads/<session>/`.

## 2. Look before editing

- `ffprobe` each clip (size, fps, duration). Make a contact sheet to see framing and letterbox bars:
  `ffmpeg -i clip.mp4 -vf "fps=2,scale=216:-2,tile=8x2" -frames:v 1 sheet.png`, then Read it.
- If a reference video is given, contact-sheet it too and match it; if its look differs from the
  style below, follow the reference and tell the user what changed. Never copy the creator's
  handle/watermark.
- Find the picture area inside letterboxed sources (`crop=w:h:x:y`) and the face point for zooms.

## 3. Get the words and their times (scripts/asr.py)

```bash
A=.claude/skills/reel-edit/scripts/asr.py
python3 $A text clip.mp4                                  # full transcript
python3 $A end  clip.mp4 '[[0,"partner",0.4,1.3], ...]'   # first guess at where a word ends
python3 $A win  clip.mp4 '[[0,1.12],[1.12,2.3]]'          # confirm each caption window
python3 $A env  clip.mp4 3.6 5.2                          # loudness; pauses are below -35 dB
```
Whisper often "finishes" a word early, so confirm every boundary with `win` (the window must
contain the whole phrase and nothing of the next) and `env` (cut in a pause when there is one).
Cut the end of a clip before any clipped/half word; skip lead-in silence.

## 4. Build (scripts/reel_style.py)

Copy `scripts/example_plan.py` (the approved Clip 1 + Clip 2 edit) and change the clips, cuts and
captions. `render()` does crop -> zoom -> grade -> join -> captions -> loudness -14 LUFS.

Style rules:
- **Cuts / zoom**: cut on phrase boundaries; alternate zoom 1.0 / 1.12-1.25 / 1.35-1.45 so every
  cut is a visible punch-in, strongest zoom on punchlines.
- **B&W** (`bw=True`) on the negative thought / "overthinking" part only.
- **Captions** (`E.cap`): 2-5 words, at the spoken time, 1-2 keywords in `{Y}` yellow.
  Quoted self-talk uses `style="Quote"` (bold italic) with a quote mark.
- **Label** (`E.label`): white box, black caps, red ✖ ("OVERTHINKING:", "INSTEAD OF:"),
  above a Quote caption for the same span. `x=False` for neutral labels ("THE TEXT:").
- **Pop title** (`E.pop`): the punchline in big tilted caps, 1-2 lines, second line yellow.
- **Strike** (`E.strike`): old phrase crossed out in red with the new phrase under it, for a reframe.
- **Sizes**: Main 80, Quote 78, Label 62, Pop 110 (the user asked twice for bigger text: never go
  smaller). Split a caption if it would be wider than ~950 px.
- Numbers as digits ("4 minutes") are fine; every other word must be exactly what is said.

## 5. Verify before sending (all of these, every time)

1. `python3 $A verify out.mp4 out.ass` - every SAID must match its CAPTION. If a window looks off,
   re-check it with `win` using slightly different edges before changing anything.
2. `python3 $A text out.mp4` - the whole script is there, no cut-off word at a join.
3. Extract frames at each caption/title (`-ss t -frames:v 1`) and Read them: nothing off-screen,
   no overlapping lines, strike bar sits on its text, B&W only where intended.

Then commit the plan script, `.ass` and `.mp4` to the working branch, push, SendUserFile the
video, and reply with a short table of what was done plus anything that could not be checked
(e.g. "real-time playback nahi dekh sakta, ek dafa khud dekh lein").
