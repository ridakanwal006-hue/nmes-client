# Google Flow v3: "She said you're too old" (seedha camera mein, koi host nahi, ruk ruk ke nahi)

## ! Pichli clips mein kya galat tha (v3 mein theek kiya)
- Dorian **kisi host ya interviewer se baat kar raha tha** (nazar aur sar side mein), camera se nahi. Wajah: start frame wahi **poori podcast wali photo** thi (wide shot, microphone, armchair). Flow ne use "interview" samjha.
- Wo **ruk ruk ke** bolta tha, lambe waqfe ke saath.
- Beech mein ek **dusri awaaz** ("Yeah") aayi, jo host ki lagti thi.

**Is dafa fix:** (1) start frame **`dorian-closeup-start-frame.png`** (chest-up, camera ki taraf dekhta hua), wide photo nahi. (2) Prompt mein "akela hai, koi host ya interviewer nahi, har pal lens mein dekhta hai". (3) "continuous flow, chhote waqfe". (4) Setting se microphone aur podcast ka zikr hata diya.

---

## Kaise use karein
1. Flow mein **Frames to Video** chunein. **Har clip ke liye wahi ek start frame** lagayein: `reels/dorian-closeup-start-frame.png` (baal wala Dorian, chest-up). Pichli clip ka aakhri frame agli clip mein mat dein, isse chehra badalne lagta hai.
2. Har clip ke prompt ke shuru mein neeche ka **MASTER LOCK** paste karein, phir us clip ka text.
3. Pehle **C001** banayein. Check: chehra aur baal wahi, koi zoom nahi, awaaz gehri aur sukoon wali. Theek ho tabhi C002 se aage badhein.
4. Jo clip mein zoom, baal ya chehra badle, use dobara generate karein (Flow kabhi kabhi nahi manta).
5. Clips mujhe bhej dein, main edit kar dunga (bina zoom, bina glitch, sirf voice).

**Sachai:** Flow awaaz ki file se awaaz copy nahi kar sakta. Is bayan se **milti-julti** awaaz banti hai, bilkul Brian nahi. Bilkul wahi Brian chahiye to: Brian ki voiceover (credits 18 October ko) + HeyGen/Hedra/Kling jo audio se hont chalate hain.

---

## MASTER LOCK (har clip ke shuru mein paste karein)
```
MASTER LOCK. Identical in every clip.

CHARACTER (identical in every clip): Dorian Wolfe, a man in his late 40s. Thick swept-back dark hair graying at the temples (his hair never changes, he is never bald), short well-groomed salt-and-pepper beard, calm direct eyes, strong jaw. Dark charcoal three-piece suit, white open-collar shirt, no tie. He looks exactly like the reference image. Same face, same hair, same suit, same room in every frame.

CAMERA: vertical 9:16, medium close-up, chest up, exactly like the reference image. Completely locked-off tripod shot. NO zoom, NO push-in, NO pull-out, NO camera movement, NO cuts, NO dissolve, NO wide shot. The framing stays exactly the same from the first frame to the last.

SETTING: dark moody room, warm amber light strips and shelves softly out of focus behind him, one soft key light on his face, subtle film grain. No microphone visible, not a podcast, not an interview.

VOICE (the exact same voice in every clip): a deep, resonant, warm adult male baritone with a full chest tone and a very slight natural gravel, like a calm audiobook narrator speaking to one person across a table. Median pitch about 103 Hz (low), settling to about 75 to 80 Hz at the end of sentences and rising to about 140 Hz only on emphasis. Natural conversational pace, about 155 words per minute, flowing and continuous, with only short pauses of about a quarter of a second between sentences, never halting. Calm, confident, intimate, never shouting, never announcer-like, never dramatic. Neutral American accent. Close-microphone, dry, clean sound. No echo, no reverb, no chorus or doubled voice, no robotic or processed tone, no pitch effects, no music, no sound effects.

PERFORMANCE: He is completely alone in the room, speaking directly to the viewer through the lens. He looks straight into the camera lens the entire time, steady eye contact, never glancing to the side, never looking at anyone off-screen, no host, no interviewer, no second person, no second voice, no one answering or reacting. Serious, calm and natural, like a real man talking to one person he respects. His delivery is continuous and flowing: he does not stop and start, he does not hesitate between words, and there are only short natural pauses (about a quarter of a second) between sentences. Minimal hand movement, head mostly still, lips perfectly synced. He does not smile broadly.

DO NOT: add on-screen text, captions, subtitles, logos, music, other people, a host, an interviewer, any second voice, or a different voice. Do not change his hair, face or suit.
```

## Clip prompts

### C001 (about 6 s)
```
[MASTER LOCK]

Dorian looks straight into the lens, serious and calm. He speaks in the locked voice:
"She said you're too old. Listen carefully."
Half-second pause.
"She didn't reject you."
```

### C002 (about 7 s)
```
[MASTER LOCK]

Same framing, same lighting, same character. Calm and firm, in the same locked voice:
"She rejected a man who apologizes for his age."
Half-second pause. His expression softens slightly.
"At twenty-five, you had energy."
```

### C003 (about 8 s)
```
[MASTER LOCK]

Same framing, same lighting, same character. Steady and warm, in the same locked voice:
"At forty-five, you have standards, stories, and a spine."
Half-second pause.
"Stop explaining your age. Stop joking about it first."
```

### C004 (about 6 s)
```
[MASTER LOCK]

Same framing, same lighting, same character. Quiet and calm, in the same locked voice:
"Say it once, calmly, and move on."
Half-second pause. A small nod.
"The right woman isn't looking for young."
```

### C005 (about 5 s)
```
[MASTER LOCK]

Same framing, same lighting, same character. Holds eye contact, low and steady, in the same locked voice:
"She's looking for steady."
One-second pause. A faint, quiet look of confidence.
"Be steady."
He holds the final look for a second in silence.
```

## Check list (har clip par)
- [ ] Chehra aur baal poori clip mein ek jaise (koi ganja nahi, koi dusra aadmi nahi).
- [ ] Koi zoom, push-in, wide shot ya dissolve nahi.
- [ ] Awaaz gehri, garm aur sukoon wali, koi echo ya doubling nahi.
- [ ] Lines script ke mutabiq (Flow kabhi kabhi lafz badal deta hai).
- [ ] On-screen text ya music nahi.
