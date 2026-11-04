# Google Flow v2: "She said you're too old" (baal theek kiye hue)

**Kya galat hua tha:** pehle prompt mein "completely bald" likha tha, lekin aap ki photo mein Dorian ke **baal hain**. Flow har clip photo ke wide shot se shuru karta tha, phir ganje close-up mein morph karta tha.
**Is dafa fix:** (1) prompt mein baal photo ke mutabiq, (2) start frame **close-up crop** (file: `reels/dorian-closeup-start-frame.png`), taake wide shot aur morph aaye hi nahi, (3) "no cuts, no dissolve, no zoom".

## Kaise use karein
1. Flow mein **Frames to Video** (ya Ingredients) chunen. Start frame ke taur par `dorian-closeup-start-frame.png` lagayein (9:16 close-up, baal wala Dorian).
2. Neeche ka **MASTER LOCK** har clip ke prompt ke shuru mein paste karein.
3. Pehle **C001** se test karein. Dekhein: chehra aur baal wahi rehte hain? Awaaz gehri aur sukoon wali hai? Wide shot ya dissolve to nahi aaya?
4. Theek ho to C002 se C005 banayein. Har clip ke aakhri frame ko agli clip ka start frame na banayein (isse chehra badalne lagta hai); har clip mein wahi close-up crop use karein.
5. Mujhe clips bhej dein, main dobara edit kar dunga (bina zoom, bina glitch, sirf voice).

**Hadd:** Flow aap ki di hui awaaz ki file se awaaz copy nahi kar sakta. Neeche bayan se milti-julti awaaz banti hai, bilkul Brian nahi.

---

## MASTER LOCK (har clip ke shuru mein paste karein)
```
MASTER LOCK. Identical in every clip.

CHARACTER: Dorian Wolfe, a man in his late 40s. Thick swept-back dark hair graying at the temples (the hair never changes, never disappears, he is never bald), short well-groomed salt-and-pepper beard, calm direct eyes, strong jaw. Dark charcoal three-piece suit, white open-collar shirt, no tie. Looks exactly like the reference image. Same face, same hair, same suit in every frame.

FRAMING: vertical 9:16, medium close-up, chest up, exactly like the reference image. Keep this framing for the whole clip. One continuous take. No cuts, no zoom out, no wide shot, no dissolve, no morph, no camera movement except a barely visible slow push-in.

SETTING: dark moody room with warm amber light strips and shelves softly out of focus behind him, a studio microphone on an arm at the right edge of the frame. Single soft key light on his face. Subtle film grain.

VOICE (this exact voice in every clip): a deep, resonant, warm male baritone. Mature, steady and comforting, like a trusted older friend talking to one person across a table. Low pitch (around 100 to 110 Hz), smooth with a very slight natural gravel. Slow, measured pace with natural half-second pauses between sentences. Calm and confident, never shouting, never dramatic, never announcer-like. Neutral American accent. Close-microphone, intimate sound. No echo, no reverb, no chorus or doubled voice, no robotic or processed tone, no background music, no sound effects.

PERFORMANCE: calm, serious, warm. Small natural head movements and slight hand movement. Lips perfectly synced to the spoken words. He does not smile broadly.

DO NOT: add on-screen text, captions, subtitles, logos, music, other people, or a different voice. Do not change his hair, face or suit.
```

## Ek hi prompt mein poori script (agar Flow ek lamba clip de)
```
[MASTER LOCK]

He says, word for word, in the locked voice:
"She said you're too old. Listen carefully.
She didn't reject you.
She rejected a man who apologizes for his age.
At twenty-five, you had energy.
At forty-five, you have standards, stories, and a spine.
Stop explaining your age. Stop joking about it first.
Say it once, calmly, and move on.
The right woman isn't looking for young.
She's looking for steady.
Be steady."
```
(Flow ek clip 8 second tak hi banata hai, isliye neeche ke 5 clips behtar hain.)

## 5 clips (har ek ke shuru mein MASTER LOCK)

### C001 (about 6 s)
```
[MASTER LOCK]

Dorian looks straight into the lens, serious and calm. He speaks slowly in the locked deep, resonant baritone voice:
"She said you're too old. Listen carefully."
Half-second pause.
"She didn't reject you."
```
### C002 (about 7 s)
```
[MASTER LOCK]

Same framing and lighting. Calm and firm, same deep, resonant baritone voice:
"She rejected a man who apologizes for his age."
Half-second pause. His expression softens slightly.
"At twenty-five, you had energy."
```
### C003 (about 8 s)
```
[MASTER LOCK]

Same framing. He leans in a little, steady and warm, same deep, resonant baritone voice:
"At forty-five, you have standards, stories, and a spine."
Half-second pause.
"Stop explaining your age. Stop joking about it first."
```
### C004 (about 6 s)
```
[MASTER LOCK]

Same framing. Quiet and calm, same deep, resonant baritone voice:
"Say it once, calmly, and move on."
Half-second pause. A small nod.
"The right woman isn't looking for young."
```
### C005 (about 5 s)
```
[MASTER LOCK]

Same framing. Holds eye contact, low and steady, same deep, resonant baritone voice:
"She's looking for steady."
One-second pause. A faint, quiet look of confidence.
"Be steady."
Holds the final look for a second in silence.
```

## Check list (har clip par)
- [ ] Baal poori clip mein ek jaise (koi ganja nahi).
- [ ] Koi wide shot, dissolve ya zoom-out nahi.
- [ ] Awaaz gehri aur sukoon wali, koi echo ya doubling nahi.
- [ ] Lines script ke mutabiq (Flow kabhi kabhi lafz badal deta hai).
- [ ] On-screen text ya music nahi.
