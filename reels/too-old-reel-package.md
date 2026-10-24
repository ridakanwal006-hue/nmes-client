# Reel package: "She said you're too old"

Brian voice (locked). Honest rules: Dorian Wolfe is an AI character, no personal story, no promise of results.
Ye script ek **raay (opinion) / hausla** hai, koi research ka daava nahi. Isay fact ki tarah mat bolna.

## 1. Final spoken script (about 42 seconds)
```
She said you're too old. Listen carefully.
She didn't reject you.
She rejected a man who apologizes for his age.
At twenty-five, you had energy.
At forty-five, you have standards, stories, and a spine.
Stop explaining your age. Stop joking about it first.
Say it once, calmly, and move on.
The right woman isn't looking for young.
She's looking for steady.
Be steady.
If a no still stings, I put a short guide together. Comment REJECT, and I'll send it over.
```
Aap ki asli script wahi hai. Maine sirf **aakhri CTA line** (comment keyword) jodi hai. Agar CTA nahi chahiye to aakhri line hata dein.

## 2. On-screen text (reel template ke mutabiq)
| Waqt (approx) | Text | Style |
|---|---|---|
| 0:00-0:05 | **SHE SAID YOU'RE TOO OLD.** | laal typewriter hook |
| 0:05-0:06 | Listen carefully. | chhota safed sub-line |
| 0:15 | "Standards. Stories. A spine." | one-word captions, laal highlight |
| 0:26 | STOP EXPLAINING YOUR AGE. | laal callout |
| 0:36 | BE STEADY. | bada safed, glitch |
| 0:38-0:42 | Comment REJECT | CTA badge |

Hook ke 3 badal (A/B test ke liye):
1. SHE SAID YOU'RE TOO OLD.
2. TOO OLD? HEAR THIS.
3. STOP APOLOGIZING FOR YOUR AGE.

## 3. Caption (Instagram)
```
She said you're too old. Here's what to say to yourself first.

Dating after 40 is not about being young. It's about being steady. If a "no" still stings, comment REJECT and I'll send you the short guide.

Dorian Wolfe is an AI-generated character. General advice, not therapy. If you feel hopeless, talk to someone (USA/Canada: call or text 988. UK: Samaritans 116 123).
```
**Search keywords (caption ki pehli line aur hashtags mein):** dating after 40, dating over 50, ghosted, rejection, men over 40, dating confidence.

**Hashtags:** #datingafter40 #menover40 #datingover50 #rejection #datingconfidence #datingadviceformen

**Pinned comment:** "Dorian Wolfe is an AI character. This is a pep talk, not advice for every situation. Comment REJECT for the guide."

## 4. Product / CTA
- **REJECT** → Rejection & Resilience ($8). Free pehle chahiye to **TEXTS** ya **SCAM** wali free guide ko doosre reel mein rakhein.
- Doosra option: **CHALLENGE** (30-Day Confidence Challenge, $12) agar aap "confidence" ka angle chahti hain.

## 5. Edit config
`editing/too_old.json` (script, hook, punch-ins). Voice (WAV) milte hi:
```
python3 -I editing/reel_edit.py voice.wav editing/too_old.json out.mp4 [dorian_clip.mp4]
```
Voice abhi nahi bani (vidIQ credits 0, refill 18 Oct).

## 6. Series: isi andaaz ki 3 aur scripts (same Brian voice)
Har script ek "she said / they said" jhatka + palat kar hausla + "Be steady." jaisi aakhri line.

### S2: "She ghosted you"
```
She ghosted you. Okay.
It stings. Let it.
But don't write a story about what's wrong with you.
Maybe she was busy. Maybe she wasn't ready. Maybe it just wasn't a fit.
You don't need to know which.
Send one kind message. Then let it go.
A man who can lose gracefully is rarer than a man who wins.
Walk tall.
```
CTA: Comment QUIET.

### S3: "You're bald"
```
She said she doesn't date bald guys. Fine.
Then she wasn't your woman.
Don't hide under a hat. Don't make the joke first.
A clean head, a good smile, and a straight back.
Own it once, and move on.
Confidence isn't hair.
It's how you stand when nobody's clapping.
```
CTA: Comment PROFILE. (Dhyan: "bald guys" par koi data nahi, isay raay ki tarah rakhein, aur Profile Fixer ka bald section yaad dilayein.)

### S4: "Divorced at 45"
```
You're forty-five and starting over. That's not a failure.
It's a second draft.
You know what you won't put up with now.
You know what actually matters.
Don't rush to fill the silence.
Rebuild your week first. Then your dating life.
Small steps. Steady steps.
Be steady.
```
CTA: Comment STARTER. (Isme 988 wali line pinned comment mein rakhein, kyunke topic bhaari hai.)

## 7. Posting se pehle
- [ ] Bio/pinned comment mein "AI character" likha hai.
- [ ] Koi personal kahani ya jhoothi tareef nahi.
- [ ] Koi result ka wada nahi ("tumhein partner mil jayega").
- [ ] Voice Brian ki hai, bina reverb ya pitch change ke.
