---
name: wolfe-reel-edit
description: Make a finished 9:16 Instagram Reel for the AI character Dorian Wolfe (WOLFE brand, dating and conversation advice for men). Covers the script, the natural-sounding voiceover (raw ElevenLabs Brian via vidIQ), and the edit copied from a reference reel (typewriter red hook, one-word captions, red number callouts, glitch, punch-ins, dark drone bed). Use this whenever the user says reel, Wolfe, Dorian, voiceover, "awaz", captions, "editing copy karo", "is reel ki editing", hook, comment-keyword CTA, or wants to analyse a reference reel's editing, even if they never name the skill. Also use when they say the voice sounds robotic, doubled or flat.
---

# Wolfe Reel Edit

Turns a script into a finished vertical Reel in the style measured from a reference reel. The user writes Roman Urdu mixed with English: reply in that mix, keep scripts and captions in English.

## Who and what
- Character: **Dorian Wolfe** (bald, grey beard, dark suit, leather chair, boom mic). Brand: **WOLFE**. Tagline: "Calm. Direct. Real."
- Products the CTAs lead to (comment keyword, then DM the guide): PLAYBOOK = The Conversation Playbook, QUIET = She Went Quiet guide, DATE = First Date Blueprint. Files live in `products/`.
- Advice stays honest. No "make her chase you", no manipulation promises, always respect consent and a "no". This keeps the account safe on the platform and the buyers satisfied.

## Workflow

1. **Script.** About 100 to 140 words for 40 to 55 s. Hook line, a 3-point list ("Number one: ...", "Number two: ..."), one early micro-CTA, final CTA "Comment KEYWORD and I'll send you ...". Write it the way a person talks: contractions ("don't", "that's"), short sentences, "Okay, listen.", "...", rhetorical questions. Flat written prose sounds robotic when read by TTS. Ideas are in `references/reel_scripts.md`.
2. **Voice.** Tool `vidiq_voiceover_generate`, voiceId `nPczCjzI2devNBz1zQrb` (Brian, locked), `output: url_and_audio`. About 14 credits per 1000 characters. Poll with `vidiq_job_poll`; the inline audio only comes on the first completed poll, otherwise download `audioUrl` with curl right away. **This voice is approved by the user and locked for every video** (reference sample: `voice/approved/approved-voice-reference.mp3`, see `voice/approved/README.md`). Process with **loudness only**: `ffmpeg -i in.mp3 -af loudnorm=I=-14:TP=-1:LRA=7 -ar 48000 out.wav`. Do not pitch-shift, add reverb or saturation: those caused the robotic sound and the doubled voice in earlier versions. If the user ever wants it deeper, only change the voice after asking (alternatives: George `JBFqnCBsd6RMkjVDRZzb`, Bill `pqHfZKP75CvOlQylNhV4`, Adam `pNInz6obpgDQGcFmaJgB`).
3. **Character clip.** There is no video or lip-sync tool in the sandbox. The user makes the talking-head clip (HeyGen, Hedra or Kling Avatar with the WAV) and sends it. Test one clip first. Without a clip, render the preview card to check timing and sound.
4. **Edit.** Write a config like `assets/example_reel1.json` (script text, `hook_red` lines, `hook_sub` lines, `hook_end`, `punch` ranges) then run, with Python in isolated mode:
   `python3 -I scripts/reel_edit.py voice.wav config.json out.mp4 [character_clip.mp4]`
   The script aligns words to the detected pauses, types the red hook, shows one-word captions at about 65% height, red typed NUMBER ONE/TWO/THREE callouts, a glitch at the first pause after 7 s, +22% punch-ins and a ducked drone bed, final -14 LUFS. Measured numbers and the reasons are in `references/edit_style.md`.
5. **QA before delivering.** Extract frames (hook typing, glitch, a callout, a punch-in, the CTA) and look at them. Check loudness with `ffmpeg -af ebur128=peak=true`. Word timings are estimated, not transcribed, so say so and ask the user to check the captions against the voice.
6. **Deliver** with `SendUserFile`, commit and push to the session branch if the repo is in use, and offer the next script.

## Analysing a new reference reel
Run `python3 -I scripts/analyze_reference_edit.py reel.mp4` (needs ffmpeg and numpy). It reports cuts, flash frames, zoom proxy per 5 s, caption changes per second and how long the hook animates. Look at frames too (montage at several timestamps). Update `references/edit_style.md` with what is different instead of assuming the numbers carry over: the reference's glitch was at 7.3 s, not the 4 s a previous skill suggested.

## Rules
- Never clone a real person's voice. Use stock TTS voices for the user's own AI character.
- Reproduce style only. Do not reuse the reference's footage, lines, names or product names ("Kane Method" and similar).
- Put "AI-generated character" in the post caption, not on the video.
- Font is Inter (Poppins is not installed). Say so if the user asks about it.
- Be honest about what was not checked by ear or by transcript.
