---
name: checklist-reel-edit
description: Edit the user's talking-head / podcast clips into a 9:16 "tips" Reel in the checklist style - a hook title on white rounded boxes, then a numbered list ("1. Look - mute the video") on a dark see-through band whose items start blurred and sharpen when each step is spoken, short 1-3 word white captions timed to every word, tight jump cuts with no pauses, wide/medium/close "camera angle" zooms and slow push-ins, warm natural colour grade, cleaned-up voice, and quiet sound effects - with every caption checked word-by-word against the voice. Use when the user asks for the checklist / steps / list style, the "communication skills" reference style, a numbered-tips reel, or "is naye style mein edit karo". For the older bold-caption style with B&W, red ✖ labels and tilted titles, use reel-edit instead.
---

# Checklist reel edit

The style comes from the user's reference: a podcast tips clip, "3 steps to dramatically improve
your communication: 1. Look - mute the video / 2. Listen - phone face down / 3. Read - get it
transcribed". The user writes in Roman Urdu. Reply in Roman Urdu, keep replies short, and send the
finished video with SendUserFile. Their rule is **"without any mistake"**: every caption word
must be what is said, at the time it is said.

`SKILL_DIR` below is the folder this SKILL.md is in.

## 1. Setup (once per session)

```bash
bash "$SKILL_DIR/scripts/setup.sh"
```
This installs:
- ffmpeg (with libass) and the Inter font
- sherpa-onnx, Pillow and numpy
- **Parakeet TDT 0.6B** (~480 MB): word timestamps
- **Whisper medium.en** (~1.9 GB): a second opinion on the words
- the generated sound effects

The downloads come from GitHub releases because Hugging Face was blocked here. Nothing else
needs to be connected. Uploaded files are under `/root/.claude/uploads/<session>/`.
Copy them to a scratch folder first: word timestamps are cached next to each clip as `<clip>.words.json`.

## 2. Look and listen first

- Run `ffprobe` on each clip, then make a contact sheet and Read it:
  `ffmpeg -i c.mp4 -vf "fps=2,scale=216:-2,tile=8x2" -frames:v 1 s.png`.
  - Find the picture area if the clip is letterboxed. This is `Clip(crop="w:h:x:y")`.
  - Find the face position as a fraction of the picture: `face=(x, y)`.
- `python3 $SKILL_DIR/scripts/asr.py words clip.mp4` prints every word with its start and end.
  `asr.py text clip.mp4` gives the Whisper transcript, to read alongside it.
- Decide with the content:
  - the **hook title**: 2 short lines, said or clearly implied in the opening
  - the **list**: 2-5 items, each `num`, `keyword`, `- short rest`
  - the **reveal word** for each item: the moment the speaker says that step
  - which clip ranges to keep (drop clipped words at the ends)

  If the clips have no natural list, say so and propose one before building. Never put words
  on screen that contradict what is said.

## 3. Build (copy scripts/example_plan.py)

`scripts/checklist_style.py` is the style as a small library. The example is the Sophia
Clip 1 + Clip 2 story, built and verified with 51/51 caption words correct.

| Piece | Call | Notes |
|---|---|---|
| Tight cuts | `speech_runs(words, a, b)` | Cuts every pause over 0.30 s, keeping 0.08 s of air. The reference has no dead air at all. |
| Camera angles | `Seg(..., zoom=ANGLES[i % 4])` | Cycles wide 1.0 → medium 1.32 → wide → close 1.55 on each cut. Cap zoom at ~1.45 for 720p sources. |
| Push-in / pull-out | `Seg(..., zoom_to=z*1.08)` | A slow zoom over one segment. Use it on the last line or a key line, not everywhere. |
| Output time | `T = Timeline(segs)`, `T(clip, t)` | Turns source time into output time after the cuts. Always place overlays with it. |
| Colour grade | `Seg(grade=...)` | `warm` is the reference look and the default. `neutral`, `punchy`, `bw`, or `lut:/path.cube` for the user's own LUT. |
| Voice | `render(voice=True)` | 80 Hz high-pass, light denoise, de-ess, compression, then -14 LUFS. This matches the reference loudness, -14.4 LUFS. |
| Hook title | `E.title(a, b, [line1, line2])` | White rounded boxes with black Inter ExtraBold. Shown from 0 s until the list appears. |
| Checklist | `E.checklist(a, b, [(num, key, rest, reveal_t)])` | Dark see-through band. Number and keyword are yellow, the rest white. Items stay blurred until `reveal_t`, then sharpen over 0.26 s. The list stays to the end. |
| Captions | `auto_captions(E, T, clip, words, start, end)` | 1-3 words each. A new caption starts at punctuation or after a breath. Each stays up until the next one. White Inter SemiBold, sitting above the band. `keywords=(...)` makes chosen words yellow. |
| Sound effects | `E.sfx(t, "whoosh"/"pop"/"tick"/"ding"/"riser" or a file path, gain_db)` | The reference has none. Keep them quiet and rare: a whoosh (-24 dB) when the title or band appears, a pop (-20 dB) on each reveal, maybe a ding on the last point. User-supplied SFX or music files work by path. |

Sizes are Cap 66, List 54, Title 58. They are bigger than the reference on purpose: the user
wants text readable for every age. Never go smaller, and split text that would be wider than ~950 px.

Layout on 1080×1920:

| Element | Vertical position |
|---|---|
| Caption | y = 1150 |
| Band | starts at y = 1215, 72 px per line |
| Title | y = 1265 |

Keep faces above y ≈ 1100. If a face sits low, move the overlays down with the `y=` arguments
rather than covering the mouth.

## 4. Verify (every time, before sending)

1. `python3 $SKILL_DIR/scripts/asr.py verify out.mp4 out.ass`
   - This transcribes the finished video and lines up every caption word with the spoken word.
   - **WORD** means a caption differs from the speech. **TIME** means a word is outside its caption's time.
   - **CHECK** means Parakeet and Whisper disagree. Listen to that spot with `asr.py win out.mp4 '[[a,b]]'` before deciding.
   - It must end with `0 caption problem(s)`. Numbers written as digits ("4") count as their words.
2. Extract frames at the title, at each reveal, and at the end, then Read them. Check that:
   - nothing is off-screen and nothing overlaps
   - each item is sharp only after its reveal word
   - no overlay covers the mouth
   - the zooms are not too soft
3. Make sure no clipped word or click remains at any cut. A cut-off word sounds wrong even when the captions are right.

Then send the video, and reply with a short table of what was done plus anything that could not
be checked (for example, "I can't watch it in real time, please watch it once").
Commit the plan, `.ass` and `.mp4` if working in a repo.

## Never
- Copy the reference creator's branding, show name or watermark.
- Guess caption words, or use the script instead of the audio. Veo-generated speech often differs from its script.
- Add music unless the user gives the track (licensing).
