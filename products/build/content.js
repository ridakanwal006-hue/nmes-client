// Content for the 4 products. Block types:
// ['h', text] ['p', text] ['ul', [..]] ['msg', text, note] ['dont', [..]] ['tip', title, text]
// ['qs', [..]] ['steps', [[title, text], ..]] ['lbl', text]
const NAME = 'Dorian Wolfe';
const BRAND = 'WOLFE';

const honest = [
  ['tip', 'One honest note', 'No line works on everyone, and none replaces being a decent person. Use these to start and keep real conversations going. If she is not interested, thank her and move on. That is part of the skill.'],
];

const texts50 = {
  id: 'wolfe-50-texts-cheat-sheet',
  kind: 'FREE CHEAT SHEET',
  titleLines: ['50 TEXTS', 'THAT GET', 'REPLIES'],
  sub: 'Copy-paste messages for every stage: first message, keeping it alive, making plans, and reviving a quiet chat.',
  chapters: [
    {
      kicker: 'START HERE', title: 'The 3 rules of a text that gets a reply',
      blocks: [
        ['p', 'Most texts fail for one reason: they are hard to answer. Fix that and your reply rate changes overnight.'],
        ['steps', [
          ['1. Make it easy to answer', 'Short, specific, one question. "How was your week?" is a chore. "Best coffee spot you have found lately?" is a pleasure.'],
          ['2. Be specific to her', 'Mention something from her profile or your last chat. Generic texts feel copy-pasted (and these templates only work when you fill the [brackets] with real details).'],
          ['3. Give her something to react to', 'A small opinion, a light joke, a choice. Not just a question. Two-way beats interview.'],
        ]],
        ['tip', 'How to use this sheet', 'Replace everything in [brackets]. Change the words to sound like you. Never send a text you would not say out loud.'],
      ],
    },
    {
      kicker: 'PART 1', title: 'First messages (10)',
      blocks: [
        ['p', 'Goal: start a conversation, not impress her. Keep it light and specific.'],
        ['msg', 'That photo from [place]. Please tell me it was as good as it looks.', 'Specific to her photo'],
        ['msg', 'Okay, settle something: [tea or coffee]? Your answer decides whether this goes anywhere. 😄', 'Playful choice, easy to answer'],
        ['msg', 'Your bio says [thing]. Real passion or a flex?', 'Teasing, curiosity'],
        ['msg', 'I am terrible at openers, so: what was the best part of your week?', 'Honest and disarming'],
        ['msg', 'You look like someone with strong opinions about [food]. Am I right?', 'Invites her opinion'],
        ['msg', 'Quick question, I need a recommendation: best [coffee / restaurant] you have been to lately?', 'Low pressure, she is the expert'],
        ['msg', 'Hey [Name], I liked what you said about [topic]. What got you into it?', 'Shows you actually read it'],
        ['msg', 'Two truths and a lie. You go first.', 'A game, instant interaction'],
        ['msg', 'Your taste in [music/shows] is unexpectedly good. What is on repeat right now?', 'Compliment plus question'],
        ['msg', 'I almost did not message. Glad I did. How is your week going?', 'Warm and confident'],
      ],
    },
    {
      kicker: 'PART 2', title: 'Keeping it going (10)',
      blocks: [
        ['p', 'When she answers, do not jump to a new question. Dig into what she just said.'],
        ['msg', 'Wait, go back. How did you end up doing that?', 'Curiosity about her story'],
        ['msg', 'That sounds like there is a story behind it. I have time.', 'Invites more'],
        ['msg', 'What was the best part of that?', 'Moves from facts to feelings'],
        ['msg', 'Ha, I did not expect that answer. Now I am curious.', 'Shows genuine reaction'],
        ['msg', 'My turn to answer: [your answer]. Now yours.', 'Share back, avoid interview mode'],
        ['msg', 'What is something you are really into that most people do not know about?', 'Opens a deeper topic'],
        ['msg', 'You light up when you talk about [topic]. What do you love about it?', 'Notices her energy'],
        ['msg', 'If you could go back to that moment, would you do it again?', 'Reflection question'],
        ['msg', 'Great answer. Follow-up: what made you choose it?', 'Shows you listen'],
        ['msg', 'Is that a "tell the whole story" thing or a "short version" thing?', 'Light and funny'],
      ],
    },
    {
      kicker: 'PART 3', title: 'Playful and warm (10)',
      blocks: [
        ['p', 'Flirting is not a trick. It is warmth plus a little playfulness. Keep it respectful and watch how she responds.'],
        ['msg', 'You seem dangerously good at [thing]. I might need lessons.', 'Compliment with humour'],
        ['msg', 'I am starting to think you are the interesting one here. Do not let it go to your head.', 'Light teasing'],
        ['msg', 'Fine, you win this round. Rematch soon?', 'Playful and plants a seed'],
        ['msg', 'Your sense of humour is a problem. In a good way.', 'Honest compliment'],
        ['msg', 'I was going to say something smooth, then you sent that and I forgot.', 'Self-aware'],
        ['msg', 'Admit it, you are the one who always picks the restaurant.', 'Playful guess'],
        ['msg', 'Okay, I am officially a fan of [her opinion].', 'Validates her'],
        ['msg', 'You have excellent taste. Slightly suspicious, honestly.', 'Teasing'],
        ['msg', 'That made me laugh out loud, and I am at [place]. People are looking.', 'Shows genuine reaction'],
        ['msg', 'Good morning. I hope today is kind to you.', 'Warm, never needy'],
      ],
    },
    {
      kicker: 'PART 4', title: 'Making plans (10)',
      blocks: [
        ['p', 'A good invite is specific, easy to say yes to, and low pressure. Offer a day and a place. Do not ask "what are you up to?".'],
        ['msg', 'I am enjoying this chat. Want to continue it over coffee this week?', 'Simple and clear'],
        ['msg', 'There is a [place] I have been meaning to try. Free [day] evening?', 'Specific plan'],
        ['msg', 'Let us grab a drink [day]. Does [time] work, or is [time] better?', 'Two options, easy yes'],
        ['msg', 'I would rather hear the rest in person. Coffee on [day]?', 'Natural transition'],
        ['msg', 'Are you around this weekend? I would like to take you for [thing].', 'Direct and warm'],
        ['msg', 'I will be near [area] on [day]. Want to meet for a quick coffee?', 'Low commitment'],
        ['msg', 'Dinner or coffee? Your pick, I am easy.', 'Gives her the choice'],
        ['msg', 'Saturday afternoon: walk and coffee. Yes or no?', 'Playful confidence'],
        ['msg', 'That place you mentioned. Let us go. [Day] works for me. You?', 'Uses what she said'],
        ['msg', 'Great. [Day], [time], [place]. I will message you when I get there.', 'Confirms the details'],
      ],
    },
    {
      kicker: 'PART 5', title: 'After a quiet patch (10)',
      blocks: [
        ['p', 'Quiet does not always mean no. Send one light message. If there is still no reply, let it go.'],
        ['msg', 'Hey, hope your week is going well. I saw [thing] and thought of you.', 'Light, no pressure'],
        ['msg', 'Hi [Name], no pressure. Still up for that coffee if you are.', 'Gives her an easy out'],
        ['msg', 'Quick check-in: how did [thing she mentioned] go?', 'Shows you remember'],
        ['msg', 'Hey stranger. How is life?', 'Casual reopener'],
        ['msg', 'I realise I have been quiet. Work has been chaotic. How are you?', 'Honest and warm'],
        ['msg', 'Random, but this [meme/song] reminded me of you.', 'Small and sweet'],
        ['msg', 'If you are busy, no worries. I will be around if you want to catch up.', 'No pressure'],
        ['msg', 'I enjoyed talking to you. If the vibe changed, no hard feelings, just tell me.', 'Mature and honest'],
        ['msg', 'Still want that coffee? I would like to see you, but tell me honestly.', 'Clear and respectful'],
        ['msg', 'Last message from me, promise: I had a good time and I wish you well.', 'A graceful exit'],
      ],
    },
    {
      kicker: 'AVOID', title: 'Texts to never send',
      blocks: [
        ['dont', [
          '"hey" (alone). It gives her nothing to answer.',
          '"Why are you ignoring me?" Pressure kills interest.',
          '"u up?" Sends the wrong message about your intent.',
          'Three messages in a row with no reply (triple-texting).',
          '"Good morning princess" from a stranger. Too much, too soon.',
          'Anything you would be embarrassed for her friends to read.',
        ]],
        ['tip', 'The golden rule', 'Match her energy. If she writes one line, do not reply with a paragraph. If she goes quiet, give her space.'],
        ...honest,
        ['p', 'Want the full system for conversations that keep going? Get **The Conversation Playbook**. Comment PLAYBOOK on my reel and I will send it over.'],
      ],
    },
  ],
};

const playbook = {
  id: 'wolfe-conversation-playbook',
  kind: 'THE PLAYBOOK',
  titleLines: ['THE', 'CONVERSATION', 'PLAYBOOK'],
  sub: 'How to take any conversation from "hey" to genuinely connected, and what to say when it stalls.',
  chapters: [
    {
      kicker: 'INTRODUCTION', title: 'Why conversations die',
      blocks: [
        ['p', 'You match. You text. The first few messages go fine, then it slowly fades. Or you sit across from someone on a date and run out of things to say.'],
        ['p', 'It feels like a personality problem. It is not. It is a **skills problem**, and skills can be learned.'],
        ['p', 'Conversations die for three reasons:'],
        ['steps', [
          ['Interview mode', 'You fire question after question and share nothing. It feels like a job interview.'],
          ['Surface level', 'You stay on facts (work, weather, weekend) and never reach feelings or stories.'],
          ['Fear of silence', 'You panic at a pause and say something forgettable, or nothing at all.'],
        ]],
        ['p', 'This playbook fixes all three with simple, repeatable tools. Read it once, then practise one chapter a day.'],
      ],
    },
    {
      kicker: 'CHAPTER 1', title: 'The 3-layer rule',
      blocks: [
        ['p', 'Every conversation has three layers. Most people never leave the first.'],
        ['steps', [
          ['Layer 1: Facts', '"Where did you grow up?" "What do you do?" Safe, easy, forgettable.'],
          ['Layer 2: Feelings', '"What did you like about growing up there?" "What do you enjoy about your job?" This is where she lights up.'],
          ['Layer 3: Meaning', '"What did that teach you?" "Why does it matter to you?" This is where real connection happens.'],
        ]],
        ['p', 'Psychologist Arthur Aron and colleagues found in 1997 that gradually deeper, mutual sharing can create closeness even between strangers. The key words are **gradually** and **mutual**. You go deeper only as fast as she is comfortable, and you share too.'],
        ['tip', 'Your rule', 'Spend a minute in Layer 1, then ask one Layer 2 question. Only go to Layer 3 when the mood allows it.'],
      ],
    },
    {
      kicker: 'CHAPTER 2', title: 'Echo, Dig, Share',
      blocks: [
        ['p', 'A simple loop that keeps any conversation moving.'],
        ['steps', [
          ['Echo', 'Repeat her key word with curiosity. She says "I just got back from Lisbon." You say "Lisbon! What took you there?"'],
          ['Dig', 'Ask about the feeling or the reason. "What was the best part?" "Why that city?"'],
          ['Share', 'Offer a short story or opinion of your own. "I have always wanted to go. I got lost in Istanbul once, completely lost."'],
        ]],
        ['p', 'Then loop back to Echo. This loop alone turns a Q&A into a conversation.'],
        ['lbl', 'EXAMPLE'],
        ['msg', 'She: I started pottery classes last month.', ''],
        ['msg', 'You: Pottery! (Echo) What made you try it? (Dig)', ''],
        ['msg', 'She: I needed something that was not a screen.', ''],
        ['msg', 'You: I get that. I spend all day at a laptop and I started cooking for the same reason. (Share) What is the hardest part so far?', ''],
      ],
    },
    {
      kicker: 'CHAPTER 3', title: 'Escape interview mode',
      blocks: [
        ['p', 'If you ask three questions in a row without sharing, you are interviewing her. The fix is the **1:1 rule**: for every question you ask, give one piece of yourself.'],
        ['lbl', 'INTERVIEW MODE (BAD)'],
        ['dont', ['"Where do you work?" "Do you like it?" "How long?" "Any siblings?"']],
        ['lbl', 'CONVERSATION MODE (GOOD)'],
        ['msg', 'What do you do? ... Oh nice, I am in [field]. I actually fell into it by accident. How did you end up there?', ''],
        ['tip', 'Quick test', 'Look at your last 3 messages. If all three end with a question mark, add a statement about you.'],
      ],
    },
    {
      kicker: 'CHAPTER 4', title: '30 better questions',
      blocks: [
        ['p', 'Keep these in your notes app. Ask them naturally, not like a checklist.'],
        ['lbl', 'EASY (LAYER 1 TO 2)'],
        ['qs', [
          'What is the best thing you have eaten recently?',
          'What is a small thing that always makes your day better?',
          'If you had a free Saturday, what would you do?',
          'What was the last show or book you could not stop?',
          'What is your go-to comfort food?',
          'What is the best trip you have ever taken?',
          'What is something you are weirdly good at?',
          'Are you a morning or night person, and how bad is it?',
          'What is on your playlist you would be embarrassed by?',
          'What would your perfect Sunday look like?',
        ]],
        ['lbl', 'WARM (LAYER 2)'],
        ['qs', [
          'What was your favourite thing about growing up where you did?',
          'What is something you are proud of that no one asks about?',
          'Who has influenced you the most?',
          'What do you do when you need to recharge?',
          'What did you want to be when you were ten?',
          'What is the best advice you have ever received?',
          'What kind of people do you feel most yourself around?',
          'What are you looking forward to this year?',
          'What is a skill you wish you had?',
          'What is the happiest memory that comes to mind right now?',
        ]],
        ['lbl', 'DEEP (LAYER 3, USE SPARINGLY)'],
        ['qs', [
          'What is something you used to believe that you do not anymore?',
          'What do you wish people understood about you?',
          'When do you feel most alive?',
          'What is a risk you took that changed things?',
          'What are you still figuring out?',
          'What is something you are afraid to say out loud?',
          'What does a good relationship look like to you?',
          'What would you do differently if no one was watching?',
          'What do you value more as you get older?',
          'What is a moment that shaped who you are?',
        ]],
        ['tip', 'Important', 'Always share your own answer too. Deep questions only work when it is a trade, not an interrogation.'],
      ],
    },
    {
      kicker: 'CHAPTER 5', title: 'What to say when she opens up',
      blocks: [
        ['p', 'This is where most people freeze. She shares something personal and you say "oh, that is rough" or change the subject. Use the **ARAS** steps:'],
        ['steps', [
          ['A: Acknowledge', '"That sounds like it was really hard." / "That must have felt amazing."'],
          ['R: Reflect', 'Say back what you heard. "So you moved alone at 22 and had to figure it out."'],
          ['A: Ask', '"What was that like for you?" / "How did you get through it?"'],
          ['S: Share', 'A short, relevant moment from your life. Keep it brief and return the focus to her.'],
        ]],
        ['lbl', 'EXAMPLE'],
        ['msg', 'She: My dad was sick last year. It was a rough time.', ''],
        ['msg', 'You: I am sorry, that sounds exhausting. (Acknowledge) You were looking after everyone while holding it together. (Reflect) How are you doing now? (Ask)', ''],
        ['dont', [
          'Do not try to fix it ("You should just...").',
          'Do not one-up her ("Oh, mine was worse").',
          'Do not rush to a joke to escape the discomfort.',
          'Do not change the subject.',
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 6', title: '5 ways to beat awkward silence',
      blocks: [
        ['p', 'A pause is not a failure. Two seconds of silence feels like ten to you and almost nothing to her. If it still feels stuck, use one of these:'],
        ['steps', [
          ['1. Breathe and smile', 'Do nothing for three seconds. Comfortable people tolerate silence.'],
          ['2. The callback', 'Return to something she said earlier. "Wait, earlier you mentioned [thing]. Tell me more."'],
          ['3. Observe the moment', '"This place has great lighting." / "That is the loudest espresso machine I have ever heard."'],
          ['4. The pivot question', '"Can I switch topics? What is something you are excited about this month?"'],
          ['5. The honest line', '"I lost my train of thought. Your turn to pick a topic." Honesty charms people.'],
        ]],
        ['tip', 'Prepare in advance', 'Pick two callbacks and one pivot question before every conversation. Confidence is mostly preparation.'],
      ],
    },
    {
      kicker: 'CHAPTER 7', title: '"Tell me about yourself"',
      blocks: [
        ['p', 'She says "so, tell me about yourself" and your mind goes blank. Use the **Present, Past, Passion** formula. Aim for 20 to 30 seconds, then hand it back.'],
        ['steps', [
          ['Present', 'What you do now, in one line.'],
          ['Past', 'One interesting thing that shaped you.'],
          ['Passion', 'Something you love, with energy.'],
        ]],
        ['lbl', 'EXAMPLE'],
        ['msg', 'I run a small [business/role] (Present). I grew up in [place], which is why I am obsessed with [thing] (Past). Right now I am trying to get better at [hobby], badly, but I love it (Passion). What about you?', ''],
        ['dont', [
          'Do not recite your CV.',
          'Do not brag or list achievements.',
          'Do not talk for more than 30 seconds.',
          'Always end by asking her back.',
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 8', title: 'From texting to talking',
      blocks: [
        ['p', 'A good chat over text should lead to a real meeting. Do not stay in text-land for weeks.'],
        ['steps', [
          ['Rule of 3 days', 'After about 3 days of good chatting, suggest meeting.'],
          ['Be specific', '"Coffee Thursday at 6?" beats "We should hang out sometime."'],
          ['Offer two options', '"Thursday or Saturday?" makes saying yes easy.'],
          ['Accept a no gracefully', '"No worries, take care." Never argue or guilt-trip.'],
        ]],
        ['msg', 'I am enjoying this. Want to continue it over coffee Thursday or Saturday?', ''],
      ],
    },
    {
      kicker: 'CHAPTER 9', title: 'End on a high',
      blocks: [
        ['p', 'The last 30 seconds are what people remember. Leave while it is still good.'],
        ['msg', 'I have to run, but I loved this. Let us do it again soon.', 'In person'],
        ['msg', 'I had a great time. Same again next week?', 'After a date'],
        ['msg', 'I have to head off. Let us pick this up tomorrow.', 'Over text'],
        ['p', 'Do not wait for the energy to drop. Ending early leaves her wanting more, in the healthiest way.'],
      ],
    },
    {
      kicker: 'CHAPTER 10', title: '10 conversation killers',
      blocks: [
        ['dont', [
          'Interrogating with question after question.',
          'Talking only about yourself.',
          'Checking your phone while she talks.',
          'Interrupting to finish her sentence.',
          'Giving advice she did not ask for.',
          'Complaining about exes, work or the world.',
          'Fake agreement. Be honest, politely.',
          'Over-complimenting. One genuine compliment beats ten.',
          'Dropping a heavy topic too early.',
          'Trying to impress instead of connect.',
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 11', title: '7-day practice plan',
      blocks: [
        ['p', 'Skills come from practice. Do one task a day with anyone: coworker, barista, friend.'],
        ['steps', [
          ['Day 1', 'Echo: repeat the key word of what someone says and ask about it.'],
          ['Day 2', 'Ask one Layer 2 question in a normal conversation.'],
          ['Day 3', 'Use the 1:1 rule. Share before you ask.'],
          ['Day 4', 'Practise ARAS with a friend who shares something.'],
          ['Day 5', 'Tolerate a 3-second silence on purpose.'],
          ['Day 6', 'Practise your Present, Past, Passion answer out loud.'],
          ['Day 7', 'Invite someone (a friend, a match) to a specific plan.'],
        ]],
        ['tip', 'Final note', 'Conversation is a way of being curious about another person. No script replaces that. Respect her boundaries, accept a no, and keep improving. Good luck.'],
      ],
    },
  ],
};

const quiet = {
  id: 'wolfe-she-went-quiet-guide',
  kind: 'RECOVERY GUIDE',
  titleLines: ['SHE', 'WENT', 'QUIET'],
  sub: 'What to do (and what not to do) when she stops replying. Stay calm, keep your dignity, and know when to let go.',
  chapters: [
    {
      kicker: 'PART 1', title: 'Why people go quiet',
      blocks: [
        ['p', 'You cannot know the reason from the outside. That is the hard part. The common ones:'],
        ['steps', [
          ['She is busy', 'Work, family, life. Many people forget to reply, then feel awkward about it.'],
          ['She is unsure', 'She likes you but does not know what to say, or feels pressured.'],
          ['The interest faded', 'It happens. It is not a verdict on your worth.'],
          ['Bad timing', 'Something else is going on in her life.'],
        ]],
        ['tip', 'Do not play detective', 'Do not analyse timestamps or "read" her silence for hours. You will not get a correct answer, only anxiety.'],
      ],
    },
    {
      kicker: 'PART 2', title: 'The 48-hour rule',
      blocks: [
        ['p', 'When replies slow down, do nothing for 48 hours. No follow-ups, no "??", no story reactions.'],
        ['steps', [
          ['Why', 'It gives her space, and it gives you time to calm down before acting on emotion.'],
          ['What to do instead', 'Go out, train, call a friend, work on your own goals.'],
          ['After 48 hours', 'Send one message from the next section, then stop.'],
        ]],
        ['dont', ['Do not send multiple messages.', 'Do not post things to make her jealous.', 'Do not ask mutual friends to investigate.']],
      ],
    },
    {
      kicker: 'PART 3', title: 'The one message',
      blocks: [
        ['p', 'Send one message that is light, warm and easy to answer. Pick the version that fits.'],
        ['lbl', 'IF YOU WERE CHATTING WELL'],
        ['msg', 'Hey, hope your week is going well. I saw [thing] and thought of you.', ''],
        ['msg', 'Hey [Name], quick check-in. How did [thing she mentioned] go?', ''],
        ['lbl', 'IF YOU ARRANGED TO MEET'],
        ['msg', 'Hi [Name], no pressure. Still up for that coffee if you are. If plans changed, that is fine.', ''],
        ['lbl', 'IF YOU WANT HONESTY'],
        ['msg', 'I enjoyed talking to you. If the vibe has changed, no hard feelings. Just let me know.', ''],
        ['tip', 'The rule', 'One message. If she does not reply, do not send another.'],
      ],
    },
    {
      kicker: 'PART 4', title: 'What never to send',
      blocks: [
        ['dont', [
          '"Why are you ignoring me?" It creates guilt, not interest.',
          '"I guess you are not interested." It is fishing for reassurance.',
          'Long paragraphs explaining your feelings.',
          'Insults or anger after being left on read.',
          '"Hello??" or repeated "?" messages.',
          'A flood of voice notes or calls.',
        ]],
        ['p', 'Anything that makes her feel guilty, pressured or afraid makes interest worse and can cross into harassment. Respect silence as a "no" if she stays quiet.'],
      ],
    },
    {
      kicker: 'PART 5', title: 'If she replies / if she does not',
      blocks: [
        ['lbl', 'SHE REPLIES'],
        ['p', 'Match her energy. Do not scold her for the delay. Keep it light and suggest a specific plan.'],
        ['msg', 'No worries, life gets busy. Coffee Thursday or Saturday?', ''],
        ['lbl', 'SHE DOES NOT REPLY'],
        ['p', 'Accept it. Silence is an answer. You can send a graceful goodbye if you want closure, but you do not need to.'],
        ['msg', 'Looks like the timing is not right. I wish you all the best.', ''],
        ['tip', 'Strength', 'Leaving with dignity is attractive and good for you. You protect your energy for people who are interested.'],
      ],
    },
    {
      kicker: 'PART 6', title: 'Rebuild your focus',
      blocks: [
        ['p', 'Being left on read stings. Use it as a reset:'],
        ['steps', [
          ['Move your body', 'A walk, gym or sport clears your head.'],
          ['See friends', 'Do not sit with your phone waiting for a reply.'],
          ['Work on one goal', 'Career, fitness, a hobby. Progress builds confidence.'],
          ['Keep meeting people', 'Do not wait on one person. Keep your options open.'],
        ]],
      ],
    },
    {
      kicker: 'CHECKLIST', title: 'Chasing or inviting?',
      blocks: [
        ['p', 'Before you send anything, answer honestly:'],
        ['ul', [
          'Am I sending this to feel better, or to genuinely invite her?',
          'Would I be fine if she never replied?',
          'Is it light, short and easy to answer?',
          'Is this my first message in 48 hours, not my third?',
          'Would I be proud of this message tomorrow?',
        ]],
        ['tip', 'Remember', 'Reply speed is not a measure of your worth. The right person makes the effort without being chased.'],
        ['p', 'Want to avoid the stall in the first place? Get **The Conversation Playbook**.'],
      ],
    },
  ],
};

const firstdate = {
  id: 'wolfe-first-date-blueprint',
  kind: 'DATE GUIDE',
  titleLines: ['FIRST', 'DATE', 'BLUEPRINT'],
  sub: 'Where to go, what to say, how to read the room, and how to end it well. A calm plan for your first date.',
  chapters: [
    {
      kicker: 'STEP 1', title: 'Pick the right date',
      blocks: [
        ['p', 'The best first date is short, public and easy to leave or extend.'],
        ['steps', [
          ['Coffee or a walk', 'Low pressure, great for talking. 60 to 90 minutes.'],
          ['A quiet bar or cafe', 'Slightly more relaxed. Avoid loud places where you cannot hear.'],
          ['Avoid', 'Movies (no talking), long dinners (too much commitment), your home.'],
        ]],
        ['tip', 'Pick a place you know', 'Choose somewhere you have been, close to her, and easy to find. Confirm the time and place the day before.'],
        ['msg', 'Looking forward to tomorrow. [Place] at [time]. See you there. 🙂', 'Day-before text'],
      ],
    },
    {
      kicker: 'STEP 2', title: 'Prepare (30 minutes)',
      blocks: [
        ['ul', [
          'Clean, fitted clothes that make you feel good.',
          'Grooming: haircut, nails, fresh breath.',
          'Arrive 5 to 10 minutes early. Never late.',
          'Phone on silent. Charged. Put away.',
          'Two stories you can tell in 30 seconds.',
          'Three questions you can ask (see Playbook chapter 4).',
          'Know your budget and offer to pay or split gracefully.',
        ]],
        ['tip', 'Mindset', 'The goal is not to impress her. The goal is to find out whether you two genuinely enjoy each other.'],
      ],
    },
    {
      kicker: 'STEP 3', title: 'The first 5 minutes',
      blocks: [
        ['p', 'Nerves peak in the first five minutes. Make them easy:'],
        ['steps', [
          ['Smile and greet', 'Eye contact, a warm "Hi [Name], great to meet you." Offer a brief hug or handshake if comfortable.'],
          ['Compliment once', '"You look great" is enough. Keep it simple and sincere.'],
          ['Ease in', 'Talk about the place, the journey, something light.'],
        ]],
        ['msg', 'Hi [Name], great to finally meet you. Did you find this place okay?', ''],
        ['msg', 'I picked this spot because [reason]. I hope you like it.', ''],
      ],
    },
    {
      kicker: 'STEP 4', title: 'What to talk about',
      blocks: [
        ['p', 'Aim for a mix of light and meaningful. Good topics:'],
        ['ul', [
          'Travel: best trip, next trip.',
          'Food and places she loves.',
          'Hobbies and things she is passionate about.',
        ]],
        ['lbl', '15 QUESTIONS'],
        ['qs', [
          'What is the best part of your week so far?',
          'What do you do when you want to switch off?',
          'What is the best meal you have ever had?',
          'Where would you go if you could leave tomorrow?',
          'What are you most proud of this year?',
          'What is something you are curious about?',
          'What made you laugh recently?',
          'What do you enjoy about your work?',
          'What kind of music do you actually listen to?',
          'What was your favourite thing about growing up?',
          'What are you looking forward to?',
          'What is a perfect weekend for you?',
          'Do you have a hobby that surprised people?',
          'What is your most useless talent?',
          'What matters most to you in life?',
        ]],
        ['dont', ['Avoid: ex-partners, money problems, politics rants, complaining.']],
      ],
    },
    {
      kicker: 'STEP 5', title: 'Answering "tell me about yourself"',
      blocks: [
        ['p', 'Use Present, Past, Passion and keep it under 30 seconds.'],
        ['msg', 'I work in [field], which I got into by accident. I grew up in [place], so I am a little obsessed with [thing]. Lately I have been getting into [hobby]. Your turn, how about you?', ''],
        ['tip', 'Be real', 'Do not exaggerate. Honesty builds trust and saves awkward moments later.'],
      ],
    },
    {
      kicker: 'STEP 6', title: 'Body language basics',
      blocks: [
        ['steps', [
          ['Eye contact', 'Look at her while she speaks. Break away naturally.'],
          ['Posture', 'Sit relaxed, shoulders back, uncrossed arms.'],
          ['Phone', 'Out of sight. Never check it.'],
          ['Voice', 'Slow down. Nervous people speak fast.'],
          ['Listening', 'Nod, smile, react. Do not interrupt.'],
        ]],
      ],
    },
    {
      kicker: 'STEP 7', title: 'The bill and reading interest',
      blocks: [
        ['lbl', 'THE BILL'],
        ['msg', 'Let me get this one.', 'If you want to pay'],
        ['msg', 'Shall we split it? Next one is on me.', 'If she offers to split'],
        ['p', 'Do not argue or make it awkward. Be gracious either way.'],
        ['lbl', 'SIGNS SHE IS ENJOYING IT'],
        ['ul', [
          'She asks you questions back.',
          'She laughs, smiles and stays engaged.',
          'She turns her body toward you and keeps eye contact.',
          'She suggests extending the date or seeing you again.',
        ]],
        ['lbl', 'WHEN YOU CANNOT TELL'],
        ['msg', 'I am having a really good time. How about you?', 'Ask directly. Honesty is attractive.'],
      ],
    },
    {
      kicker: 'STEP 8', title: 'Ending the date',
      blocks: [
        ['p', 'End while it is still going well. Be clear and warm.'],
        ['msg', 'I really enjoyed this. I would like to see you again. Would you like that?', 'If you want a second date'],
        ['msg', 'I had a nice time. I do not think we are a match, but I enjoyed meeting you.', 'If you do not feel it'],
        ['tip', 'Consent matters', 'For a hug or a kiss, read her body language and ask: "Can I kiss you?" A respectful yes is better than a guess. Accept a no with a smile.'],
      ],
    },
    {
      kicker: 'STEP 9', title: 'After the date',
      blocks: [
        ['p', 'Message within 24 hours. Do not play games or wait three days.'],
        ['msg', 'I had a great time tonight. Thanks for coming. Let us do it again soon. 🙂', 'If you want another date'],
        ['msg', 'Got home safe? I really enjoyed meeting you.', 'Caring and light'],
        ['msg', 'Thanks for meeting me. I do not think there was a spark for me, but I wish you the best.', 'If you are not interested'],
        ['p', 'If she is not interested, accept it. You still gained practice.'],
      ],
    },
    {
      kicker: 'SAFETY', title: 'Stay safe, stay kind',
      blocks: [
        ['ul', [
          'Meet in public, arrive and leave separately for the first dates.',
          'Tell a friend where you are going.',
          'Trust your gut. Leave if something feels off.',
          'Limit alcohol. Keep your own drink in sight.',
          'Respect her boundaries. No means no.',
        ]],
        ['lbl', '10 FIRST-DATE MISTAKES'],
        ['dont', [
          'Being late or cancelling last minute.',
          'Talking only about yourself.',
          'Checking your phone.',
          'Complaining about your ex.',
          'Trying too hard to impress.',
          'Heavy topics too early.',
          'Drinking too much.',
          'Interrupting.',
          'Ignoring signs she is uncomfortable.',
          'Pushing for more when she says no.',
        ]],
        ['p', 'Want to keep the conversation flowing all night? Get **The Conversation Playbook**.'],
      ],
    },
  ],
};

module.exports = { NAME, BRAND, products: [texts50, playbook, quiet, firstdate] };
