// Extra chapters to make every product full length.
// New block types: ['chat', [[who, text], ...]]  ['lines', n]  ['chk', [items]]  ['pb']  (page break filler is automatic)
module.exports = function extend(products) {
  const by = id => products.find(p => p.id.includes(id));
  const idx = (p, title) => p.chapters.findIndex(c => c.title.toLowerCase().includes(title.toLowerCase()));
  const insertAfter = (p, title, chaps) => { const i = idx(p, title); p.chapters.splice(i + 1, 0, ...chaps); };

  // ===================== PLAYBOOK =====================
  const pb = by('conversation-playbook');

  const mindset = {
    kicker: 'MINDSET', title: 'Why people connect',
    blocks: [
      ['p', 'Before techniques, understand what is actually happening when two people click. It is rarely about perfect lines. It is about how the other person **feels** around you.'],
      ['steps', [
        ['Safe', 'She feels she can relax, be herself and not be judged.'],
        ['Seen', 'You noticed something real about her and showed it.'],
        ['Interested', 'Your attention is on her, not on your phone or your performance.'],
        ['Equal', 'You are not begging for approval and not trying to dominate. You are two people exploring each other.'],
      ]],
      ['tip', 'The reframe that removes pressure', 'You are not auditioning. You are checking whether you two enjoy each other. Either outcome is fine.'],
      ['lbl', 'THE 3 THINGS YOU CONTROL'],
      ['ul', ['Your curiosity (ask, listen, follow up).', 'Your honesty (kindly).', 'Your presence (phone away, calm voice).']],
      ['lbl', 'THE 3 THINGS YOU DO NOT CONTROL'],
      ['ul', ['Whether she is interested in you.', 'Her mood or her day.', 'How fast she replies.']],
    ],
  };

  const listening = {
    kicker: 'SKILL', title: 'Listen like it matters',
    blocks: [
      ['p', 'Most people listen while waiting for their turn. Real listening is rare, and she will notice it.'],
      ['steps', [
        ['Stop planning', 'Do not prepare your next line while she speaks. You will find it when she finishes.'],
        ['Listen for the emotion', 'Notice how she says it: excited, tired, proud, worried. Respond to that.'],
        ['Use small signals', 'Nod, "mm", "really?", "go on". They show you are with her.'],
        ['Pause before answering', 'A one-second pause shows you took it in.'],
        ['Remember details', 'Her sister\'s name, her favourite place, her big meeting. Bring it up later.'],
      ]],
      ['lbl', 'THE DETAIL TRICK'],
      ['p', 'After a conversation, write down two details she mentioned. Next time, open with one of them.'],
      ['msg', 'How did the presentation go? You were nervous about it last time.', 'Shows you were listening'],
      ['lbl', 'LISTENING MISTAKES'],
      ['dont', ['Finishing her sentences.', 'Checking your phone "just once".', 'Turning every story into your story.', 'Giving advice when she only wanted to be heard.', 'Nodding while thinking about something else. People can tell.']],
      ['tip', 'Exercise', 'In your next conversation with anyone, ask one follow-up question about something they said earlier. Count how their face changes.'],
    ],
  };

  const stories = {
    kicker: 'SKILL', title: 'Tell a story in 60 seconds',
    blocks: [
      ['p', 'Stories make you memorable. The good news: you do not need dramatic ones. A small, honest, funny moment works better than a big boast.'],
      ['lbl', 'THE 4-PART STORY'],
      ['steps', [
        ['1. Set the scene', '"Last summer I decided I could fix my own bike."'],
        ['2. The problem', '"Forty minutes in, I realised I had taken it apart and had no idea how it went together."'],
        ['3. The twist', '"A ten-year-old neighbour came over and quietly put it back together."'],
        ['4. The point', '"Lesson learned: ask for help earlier, and never underestimate ten-year-olds."'],
      ]],
      ['p', 'Keep it under a minute. End with a short line, then hand the conversation back: "Have you ever done something like that?"'],
      ['lbl', 'BUILD YOUR STORY BANK'],
      ['p', 'Prepare five stories before you meet people. Write a one-line summary of each:'],
      ['ul', ['A funny travel mishap.', 'A time you failed and learned something.', 'Something you are proud of (told humbly).', 'A weird job or school memory.', 'A moment of kindness you saw or received.']],
      ['dont', ['Do not exaggerate or invent. If it is made up, it will show.', 'Do not tell long stories with many side details.', 'Do not make yourself the hero every time.']],
    ],
  };

  const humor = {
    kicker: 'SKILL', title: 'Humour and playfulness',
    blocks: [
      ['p', 'You do not need to be a comedian. You need to be relaxed and willing to be a little playful. Three easy forms:'],
      ['steps', [
        ['Observational', 'Notice something funny in the moment. "That waiter is clearly judging my coffee order."'],
        ['Self-deprecating', 'Light, not sad. "I cook, but only three dishes. All of them pasta."'],
        ['Playful teasing', 'Gentle, mutual, never about something she is sensitive about. "You ordered the same thing twice? Bold strategy."'],
      ]],
      ['lbl', 'SAFE TEASING RULES'],
      ['ul', ['Tease things she is proud of, never insecure about.', 'If she looks uncomfortable, stop and soften immediately.', 'Make sure she can tease you back.', 'Smile when you do it. Tone matters.']],
      ['lbl', 'EXAMPLE'],
      ['chat', [['She', 'I always arrive early. It is a problem.'], ['You', 'A problem? That sounds like a superpower. I am the person who sprints in at the last second.'], ['She', 'Ha, I would be stressed just watching you.']]],
      ['dont', ['Jokes about her appearance.', 'Sarcasm that sounds like criticism.', 'Offensive or crude jokes to "test" her.', 'Laughing at your own joke too hard.']],
    ],
  };

  const compliments = {
    kicker: 'SKILL', title: 'Compliments that land',
    blocks: [
      ['p', 'A good compliment is specific, sincere and about something she chose, not just something she was born with.'],
      ['lbl', 'WEAK VS STRONG'],
      ['steps', [
        ['Weak', '"You are beautiful." (Generic. She hears it often.)'],
        ['Stronger', '"You have a great laugh. It made the whole table look over."'],
        ['Weak', '"You are smart."'],
        ['Stronger', '"The way you explained that was so clear. I understood it first time."'],
      ]],
      ['lbl', 'COMPLIMENT FORMULA'],
      ['p', '**Notice** a specific thing + **say why** it stands out. Then move on without waiting for a reaction.'],
      ['msg', 'I love how passionate you get about your garden. It is contagious.', ''],
      ['msg', 'You have great taste in music. I added three songs to my playlist already.', ''],
      ['msg', 'You are really good at making people feel comfortable.', ''],
      ['dont', ['Compliment overload. One or two a date is plenty.', 'Compliments that are really requests.', 'Looking for a reaction or fishing for a "thank you".']],
    ],
  };

  const moreQs = {
    kicker: 'BONUS', title: '50 more conversation starters',
    blocks: [
      ['p', 'Use these when you run out of ideas. Mix them with your own.'],
      ['lbl', 'FUN'],
      ['qs', [
        'If you could instantly master any skill, what would it be?',
        'What would be the title of your autobiography?',
        'What is the strangest food you have eaten and would eat again?',
        'Which fictional world would you want to live in?',
        'What is your most irrational fear?',
        'What is the best gift you have ever received?',
        'What was your first job and what did it teach you?',
        'If you had to eat one cuisine forever, which?',
        'What is your guilty pleasure show?',
        'What is the best concert or event you have been to?',
        'Which decade would you time-travel to?',
        'What is your most-used app besides messaging?',
        'Are you a planner or a go-with-the-flow person?',
        'What is the funniest thing that happened to you this year?',
        'What would you do with a free month off work?',
      ]],
      ['lbl', 'LIFE AND GOALS'],
      ['qs', [
        'What is a goal you are working toward right now?',
        'What does success look like to you in five years?',
        'What do you do that makes you lose track of time?',
        'What is something you would try if you knew you could not fail?',
        'What was the best decision you ever made?',
        'What is one habit you are proud of?',
        'What is something you learned the hard way?',
        'What is the most meaningful compliment you have received?',
        'Who is someone you really admire and why?',
        'What would your younger self think of you now?',
        'What is your favourite thing about your city?',
        'Where do you feel most at peace?',
        'What are you reading, watching or learning right now?',
        'What do you like most about your friends?',
        'What does a good day look like for you?',
      ]],
      ['lbl', 'CONNECTION'],
      ['qs', [
        'What do you value most in friendships?',
        'What makes you feel appreciated?',
        'What is your favourite way to spend time with someone?',
        'What is a tradition you love?',
        'What is something small that makes you feel cared for?',
        'What did your family teach you that you still use?',
        'What is the most adventurous thing you have done?',
        'What kind of conversations do you enjoy most?',
        'How do you like to celebrate good news?',
        'What is something you are grateful for this week?',
        'What do you wish you had more time for?',
        'What is a compliment you love to receive?',
        'What is the best part of being your age?',
        'What does "home" mean to you?',
        'What would make this week a great one?',
      ]],
      ['p', 'Some of these are too deep for a first message. Use the Easy list first and go deeper as the mood allows.'],
    ],
  };

  const online = {
    kicker: 'REAL CHATS', title: 'From match to meeting',
    blocks: [
      ['p', 'Online chats follow a simple path: **Open → Connect → Plan.** Aim to move through it in about 3 to 5 days.'],
      ['steps', [
        ['Day 1: Open', 'A specific, light first message. Ask one easy question.'],
        ['Day 1-3: Connect', 'Use Echo, Dig, Share. Find one or two things you genuinely have in common.'],
        ['Day 3-5: Plan', 'Suggest a specific meet-up. Offer two options.'],
      ]],
      ['lbl', 'FULL EXAMPLE 1: A GOOD CHAT'],
      ['chat', [
        ['You', 'That photo from the lake. Please tell me it was as good as it looks.'],
        ['She', 'Ha, it was. Lake Como last summer.'],
        ['You', 'Jealous. What was the best part?'],
        ['She', 'Probably the boat trip. We got completely lost.'],
        ['You', 'Lost is when the good stories start. I once took the wrong train in Italy and ended up in a village with one bar and one very opinionated barman.'],
        ['She', 'That sounds amazing. What did you order?'],
        ['You', 'Whatever he told me to. Best coffee of my life. Do you travel a lot?'],
      ]],
      ['lbl', 'FULL EXAMPLE 2: MOVING TO A PLAN'],
      ['chat', [
        ['You', 'I am enjoying this. Want to continue it over coffee this week?'],
        ['She', 'Sure, maybe. I am pretty busy.'],
        ['You', 'No problem. Thursday evening or Saturday morning, whichever suits you?'],
        ['She', 'Saturday morning works.'],
        ['You', 'Great. 10:30 at [place]. I will message you when I arrive.'],
      ]],
      ['lbl', 'FULL EXAMPLE 3: ONE-WORD ANSWERS'],
      ['chat', [
        ['You', 'How was your weekend?'],
        ['She', 'Good.'],
        ['You', 'Good as in relaxing or good as in "I need a holiday from my holiday"?'],
        ['She', 'Haha, definitely the second.'],
      ]],
      ['tip', 'Remember', 'If she keeps giving one-word answers across many messages, she may not be interested. Do not push. Thank her and move on.'],
    ],
  };

  const scenarios1 = {
    kicker: 'SCENARIOS', title: '10 tricky moments and what to say (1/2)',
    blocks: [
      ['lbl', '1. SHE GIVES ONE-WORD ANSWERS'],
      ['msg', 'Okay, I am going to ask a better question. What is the best thing you ate this week?', 'Makes it easy and fun to answer'],
      ['lbl', '2. "WHAT ARE YOU LOOKING FOR?"'],
      ['msg', 'Honestly, someone I can laugh with and be myself around. A real connection. What about you?', 'Honest, short, hands it back'],
      ['lbl', '3. SHE SHARES BAD NEWS'],
      ['msg', 'I am really sorry. That sounds hard. Do you want to talk about it, or would you rather think about something else for a bit?', 'Gives her the choice'],
      ['lbl', '4. YOU DISAGREE WITH HER'],
      ['msg', 'I see it a bit differently, but I love that you have such strong views. Why do you feel that way?', 'Respectful disagreement'],
      ['lbl', '5. YOU HAVE NOTHING IN COMMON'],
      ['msg', 'We are clearly different. I am more [x], you are more [y]. Teach me something about your world.', 'Turns difference into curiosity'],
    ],
  };

  const scenarios2 = {
    kicker: 'SCENARIOS', title: '10 tricky moments and what to say (2/2)',
    blocks: [
      ['lbl', '6. SHE ASKS ABOUT YOUR EX'],
      ['msg', 'It ended, we are fine, we wanted different things. I learned a lot from it. How about you?', 'Short, positive, no bashing'],
      ['lbl', '7. YOU GET NERVOUS MID-CONVERSATION'],
      ['msg', 'I will be honest, I am a little nervous. That is a good sign for me. Let me start again.', 'Honesty disarms nerves'],
      ['lbl', '8. SHE IS DISTRACTED / ON HER PHONE'],
      ['msg', 'Looks like you have a lot going on. Want to pick this up another time?', 'Calm, respectful, no sulking'],
      ['lbl', '9. A COMPLIMENT YOU DO NOT KNOW HOW TO ANSWER'],
      ['msg', 'Thank you, that made my day.', 'Simple and sincere'],
      ['lbl', '10. RECONNECTING AFTER A LONG GAP'],
      ['msg', 'Hey, I came across [thing] and thought of you. How have you been?', 'No guilt, just warmth'],
    ],
  };

  const nerves = {
    kicker: 'MINDSET', title: 'Handling nerves',
    blocks: [
      ['p', 'Nerves are normal. They are not a sign you will fail. They are a sign you care. Here is how to manage them:'],
      ['steps', [
        ['Slow breathing', 'In for 4 seconds, out for 6. Do this before and during.'],
        ['Reframe', 'Say "I am excited" instead of "I am nervous". The body feels almost the same.'],
        ['Focus outward', 'Put your attention on her: her words, her face, her story. Less time in your own head.'],
        ['Move first', 'A short walk before you arrive burns off adrenaline.'],
        ['Prepare an opener', 'Have your first sentence and first question ready.'],
        ['Accept mistakes', 'You will stumble sometimes. Smile and carry on. People like humans.'],
      ]],
      ['lbl', 'THE 5-MINUTE PRE-CONVERSATION ROUTINE'],
      ['chk', ['Drink water.', 'Three slow breaths.', 'Stand tall, relax shoulders.', 'Remind yourself: curiosity, not performance.', 'Smile before you walk in.']],
      ['tip', 'Long-term fix', 'Confidence is built by doing. Have one small conversation a day with anyone and your comfort grows quickly.'],
    ],
  };

  const rejection = {
    kicker: 'MINDSET', title: 'Handling "no" and silence',
    blocks: [
      ['p', 'Rejection is part of dating for everyone. How you handle it shapes your confidence and your reputation.'],
      ['steps', [
        ['Accept it quickly', 'A no is information, not an insult. Do not argue or persuade.'],
        ['Respond gracefully', '"No problem, thanks for being honest. Take care."'],
        ['Do not take it as a verdict', 'It says what she wants, not what you are worth.'],
        ['Learn, do not obsess', 'Ask yourself once what you could improve, then move on.'],
      ]],
      ['lbl', 'GRACEFUL EXIT LINES'],
      ['msg', 'Thanks for telling me. I appreciate the honesty. Take care.', ''],
      ['msg', 'No hard feelings at all. It was good to meet you.', ''],
      ['msg', 'All good, I enjoyed chatting. Best of luck.', ''],
      ['dont', ['Arguing or asking "why?" repeatedly.', 'Insulting her afterwards.', 'Sending long angry messages.', 'Continuing to contact her after a clear no.']],
      ['tip', 'Remember', 'People remember how you leave. A kind exit builds respect, even from someone who said no.'],
    ],
  };

  const worksheets = {
    kicker: 'WORKSHEETS', title: 'Your story bank',
    blocks: [
      ['p', 'Write one line for each story you can tell. Practise saying them out loud.'],
      ['lbl', 'MY 5 STORIES'],
      ['lines', 8],
      ['lbl', 'MY 5 FAVOURITE QUESTIONS'],
      ['lines', 5],
      ['lbl', 'MY "PRESENT, PAST, PASSION" ANSWER'],
      ['lines', 5],
    ],
  };

  const worksheets2 = {
    kicker: 'WORKSHEETS', title: 'Conversation review',
    blocks: [
      ['p', 'After each conversation or date, answer these. This is how skills grow fast.'],
      ['lbl', 'WHAT WENT WELL'],
      ['lines', 3],
      ['lbl', 'WHAT FELT AWKWARD'],
      ['lines', 2],
      ['lbl', 'ONE THING TO TRY NEXT TIME'],
      ['lines', 2],
      ['lbl', 'DID I...'],
      ['chk', ['Share as much as I asked?', 'Follow up on something she said?', 'Stay calm during silence?', 'Keep my phone away?', 'End on a high?']],
    ],
  };

  const plan30 = {
    kicker: 'THE PLAN', title: '30-day conversation challenge',
    blocks: [
      ['p', 'One small task a day. Do them with anyone: coworkers, friends, strangers, matches. Tick them off.'],
      ['chk', [
        'Day 1: Smile and greet three people.',
        'Day 2: Learn one new person\'s name and a detail.',
        'Day 3: Echo a word and ask about it.',
        'Day 4: Ask one Layer 2 question.',
        'Day 5: Share a short story.',
        'Day 6: Pause 2 seconds before answering.',
        'Day 7: Review the week.',
        'Day 8: Give one specific compliment.',
        'Day 9: Use the 1:1 rule.',
        'Day 10: Start a conversation in a queue.',
        'Day 11: Practise ARAS with a friend.',
        'Day 12: Tolerate a 3-second silence.',
        'Day 13: Send a first message you are proud of.',
        'Day 14: Review the fortnight.',
      ]],
    ],
  };
  const plan30b = {
    kicker: 'THE PLAN', title: '30-day challenge, continued',
    blocks: [
      ['chk', [
        'Day 15: Tell your best story.',
        'Day 16: Use light humour once.',
        'Day 17: Ask a Deep question (with a share).',
        'Day 18: Follow up on a detail from last time.',
        'Day 19: Practise your Present, Past, Passion answer.',
        'Day 20: End a conversation on a high.',
        'Day 21: Review the three weeks.',
        'Day 22: Suggest a specific plan.',
        'Day 23: Practise a graceful "no".',
        'Day 24: Go on a first date or meet-up.',
        'Day 25: Review your date with the worksheet.',
        'Day 26: Reconnect with someone you lost touch with.',
        'Day 27: Practise your nerve routine.',
        'Day 28: Teach someone a skill or tell them a story.',
        'Day 29: Re-read your story bank and refresh it.',
        'Day 30: Write down what changed.',
      ]],
      ['tip', 'Finish line', 'Thirty days of small, honest practice will change how you talk to people. Keep going. Skills compound.'],
    ],
  };

  const quickref = {
    kicker: 'CHEAT SHEET', title: 'One-page quick reference',
    blocks: [
      ['steps', [
        ['3 layers', 'Facts, Feelings, Meaning. Move one step at a time.'],
        ['Echo, Dig, Share', 'Repeat a word, ask why, share your own.'],
        ['1:1 rule', 'For every question, share something.'],
        ['ARAS', 'Acknowledge, Reflect, Ask, Share.'],
        ['Silence', 'Breathe, callback, observe, pivot, be honest.'],
        ['About you', 'Present, Past, Passion. Then ask her.'],
        ['Plan', 'Specific day and place, two options.'],
        ['End', 'Leave on a high.'],
        ['No', 'Accept it kindly and move on.'],
      ]],
      ['tip', 'Core idea', 'Be curious. Be honest. Be kind. Respect boundaries. Everything else is a tool.'],
    ],
  };

  // assemble playbook order
  const find = t => pb.chapters.find(c => c.title.toLowerCase().includes(t));
  const intro = pb.chapters[0];
  const ch = {
    l3: find('3-layer'), eds: find('echo, dig'), interview: find('interview'),
    q30: find('30 better'), aras: find('opens up'), silence: find('silence'),
    tell: find('tell me about'), text: find('texting to'), end: find('high'),
    killers: find('killers'),
  };
  pb.chapters = [intro, mindset, ch.l3, ch.eds, ch.interview, listening, stories, humor, compliments,
    ch.q30, moreQs, ch.aras, ch.silence, ch.tell, ch.text, online, scenarios1, scenarios2, ch.end,
    ch.killers, nerves, rejection, worksheets, worksheets2, plan30, plan30b, quickref];
  pb.chapters.forEach((c, i) => { if (i > 0) c.kicker = (c.kicker === 'MINDSET' || c.kicker === 'SKILL' || c.kicker === 'BONUS' || c.kicker === 'REAL CHATS' || c.kicker === 'SCENARIOS' || c.kicker === 'WORKSHEETS' || c.kicker === 'THE PLAN' || c.kicker === 'CHEAT SHEET' ? c.kicker + ' · ' : '') + 'CHAPTER ' + i; });

  // ===================== 50 TEXTS =====================
  const t50 = by('50-texts');
  insertAfter(t50, 'quiet patch', [
    {
      kicker: 'BONUS 1', title: 'When she says... you say',
      blocks: [
        ['p', 'Replies to the most common things she might text. Keep your tone, change the words.'],
        ['lbl', '"HAHA"'],
        ['msg', 'Glad I made you laugh. Okay, serious question now: [question].', ''],
        ['lbl', '"I AM PRETTY BUSY THIS WEEK"'],
        ['msg', 'No problem. Tell me when things calm down and we will find a time.', ''],
        ['lbl', '"WHAT ARE YOU LOOKING FOR?"'],
        ['msg', 'Something real. Someone I can laugh with. You?', ''],
        ['lbl', '"WHAT DO YOU DO?"'],
        ['msg', 'I [job]. I love [part]. What about you?', ''],
        ['lbl', '"HEY, SORRY FOR THE SLOW REPLY"'],
        ['msg', 'No worries, life happens. How was your day?', ''],
        ['lbl', '"HOW WAS YOUR DAY?"'],
        ['msg', 'Pretty good. [One specific thing]. How was yours?', ''],
        ['lbl', '"I AM TIRED"'],
        ['msg', 'Rough day? Go rest. Tell me about it tomorrow.', ''],
        ['lbl', '"I AM NOT SURE I AM READY TO MEET"'],
        ['msg', 'That is completely fine. No pressure at all. We can keep chatting until you feel comfortable.', ''],
      ],
    },
    {
      kicker: 'BONUS 2', title: 'When she says... you say (2)',
      blocks: [
        ['lbl', '"I HAD A GREAT TIME"'],
        ['msg', 'Me too. I would love to see you again. Free [day]?', ''],
        ['lbl', '"CAN WE TAKE THINGS SLOW?"'],
        ['msg', 'Of course. I am happy to go at your pace.', ''],
        ['lbl', '"I AM TALKING TO OTHER PEOPLE TOO"'],
        ['msg', 'That is fair. Let us see where this goes.', ''],
        ['lbl', '"I DO NOT THINK WE ARE A MATCH"'],
        ['msg', 'Thanks for being honest. I wish you the best.', ''],
        ['lbl', '"WHAT ARE WE DOING THIS WEEKEND?"'],
        ['msg', 'I would love to see you. How about [plan] on Saturday?', ''],
        ['lbl', '"YOU SEEM QUIET TODAY"'],
        ['msg', 'A bit. Long day. Thinking about [thing]. Tell me something fun to cheer me up.', ''],
        ['lbl', '"SEND ME A PHOTO"'],
        ['msg', 'Let us save that for when we meet. Tell me more about you instead.', 'Set your own boundaries'],
      ],
    },
    {
      kicker: 'BONUS 3', title: 'Texting timing and tone',
      blocks: [
        ['steps', [
          ['Reply time', 'Reply when you naturally can. Do not wait on purpose to look busy, and do not reply instantly every time either.'],
          ['Length', 'Match hers. One line for one line.'],
          ['Emojis', 'One or two, used naturally. Not every message.'],
          ['Voice notes', 'Only after you both feel comfortable.'],
          ['Calls', 'A short call before meeting is a great idea if she is open to it.'],
          ['Late-night texts', 'Avoid mixed signals. Say what you mean.'],
        ]],
        ['lbl', 'BEFORE YOU SEND, CHECK'],
        ['chk', ['Is it easy to answer?', 'Is it specific to her?', 'Is it kind?', 'Would I say it in person?', 'Is it one message, not a flood?']],
        ['tip', 'When in doubt', 'Delete the extra sentence and send the shorter version.'],
      ],
    },
    {
      kicker: 'WORKSHEET', title: 'My personal text bank',
      blocks: [
        ['p', 'Write your own versions of your five favourite texts. Make them sound like you.'],
        ['lines', 12],
      ],
    },
  ]);

  // ===================== SHE WENT QUIET =====================
  const q = by('went-quiet');
  insertAfter(q, 'rebuild', [
    {
      kicker: 'PART 7', title: 'Real scenarios',
      blocks: [
        ['lbl', 'SCENARIO 1: MATCH GONE QUIET AFTER 3 DAYS'],
        ['chat', [['You', 'Hey, hope your week is going well. Still up for that coffee?'], ['She', '(no reply for a week)']]],
        ['p', 'Do not send more. Move on. This match was probably not that into it.'],
        ['lbl', 'SCENARIO 2: SHE CANCELLED LAST MINUTE'],
        ['chat', [['She', 'So sorry, something came up. Can we rebook?'], ['You', 'No problem. Tell me when you are free and we will sort something.']]],
        ['p', 'One cancellation is fine. Repeated cancellations without a new plan are a sign.'],
        ['lbl', 'SCENARIO 3: SHE REPLIES SLOWLY BUT KEEPS CHATTING'],
        ['p', 'Some people simply text slowly. Match her pace, suggest a plan, and see what happens in person.'],
        ['lbl', 'SCENARIO 4: SHE VIEWED YOUR STORY BUT DID NOT REPLY'],
        ['p', 'Ignore it. Social media views are not messages.'],
        ['lbl', 'SCENARIO 5: SHE REPLIES AFTER WEEKS'],
        ['chat', [['She', 'Hey, sorry I disappeared. Work was crazy.'], ['You', 'No worries. Glad you are back. How have you been?']]],
        ['p', 'You do not have to forgive and fully re-engage. Decide whether you still want to.'],
      ],
    },
    {
      kicker: 'PART 8', title: 'Your 14-day reset plan',
      blocks: [
        ['chk', [
          'Days 1-2: Do nothing. Do not send anything.',
          'Day 3: Send one message from Part 3.',
          'Day 4: Exercise. 30 minutes minimum.',
          'Day 5: Meet a friend.',
          'Day 6: Plan something fun for the weekend.',
          'Day 7: Delete drafts you wrote and did not send.',
          'Day 8: Update your dating profile photos.',
          'Day 9: Start one new conversation with a new person.',
          'Day 10: Work on a goal for one hour.',
          'Day 11: Write down what you learned.',
          'Day 12: Cook or try something new.',
          'Day 13: Call a family member or friend.',
          'Day 14: Review: how do you feel compared with Day 1?',
        ]],
        ['tip', 'The point', 'You are not waiting for her. You are rebuilding your own life so that her reply is a bonus, not a need.'],
      ],
    },
    {
      kicker: 'FAQ', title: 'Common questions',
      blocks: [
        ['steps', [
          ['Should I double-text?', 'Once, after 48 hours, if the first one was light. Not more.'],
          ['Should I call?', 'No, not after silence. It adds pressure.'],
          ['Should I block her?', 'Only if you need space or she asks. It is not a punishment.'],
          ['Should I ask why?', 'You can send one honest question like the "if the vibe changed" message. Do not demand reasons.'],
          ['Was it something I said?', 'Maybe. Maybe not. You cannot know. Reflect once, then move on.'],
          ['Should I wait for her?', 'No. Keep meeting people.'],
          ['What if she is a friend or colleague?', 'Be kind and normal. Do not make it awkward.'],
        ]],
      ],
    },
    {
      kicker: 'WORKSHEET', title: 'Write it out',
      blocks: [
        ['p', 'Write what you feel, then close the notebook. Do not send it.'],
        ['lbl', 'WHAT I AM FEELING'],
        ['lines', 5],
        ['lbl', 'WHAT I CAN CONTROL'],
        ['lines', 4],
        ['lbl', 'WHAT I WILL DO TODAY FOR ME'],
        ['lines', 4],
      ],
    },
  ]);

  // ===================== FIRST DATE =====================
  const fd = by('first-date');
  insertAfter(fd, 'after the date', [
    {
      kicker: 'BONUS 1', title: '25 first date ideas',
      blocks: [
        ['p', 'Short, public, easy to enjoy. Pick one that suits both of you.'],
        ['qs', [
          'Coffee and a walk in a nice park.',
          'A local market or street-food tour.',
          'A museum or gallery visit.',
          'A cosy bookshop and hot chocolate.',
          'A quiet cafe with board games.',
          'A sunset walk by the water.',
          'A casual brunch.',
          'A small live-music night.',
          'A pottery or cooking drop-in class.',
          'Mini golf or bowling.',
          'An ice cream and a stroll.',
          'A farmers market and picnic.',
          'A scenic viewpoint with coffee.',
          'A food-truck lunch.',
          'A botanical garden.',
          'A rooftop drink at sunset.',
          'A quiet wine or mocktail bar.',
          'An arcade evening.',
          'A zoo or aquarium visit.',
          'A flea market hunt.',
          'A trivia or quiz night.',
          'A local festival.',
          'A hike (easy trail) with a coffee stop.',
          'A dessert tasting.',
          'A walk plus a small gallery.',
        ]],
        ['tip', 'Rule', 'Choose something that gives you things to talk about (a place, a view, a task) so conversation feels natural.'],
      ],
    },
    {
      kicker: 'BONUS 2', title: 'Look and feel your best',
      blocks: [
        ['steps', [
          ['Clothes', 'Clean, well-fitting and appropriate for the place. Wear what makes you comfortable.'],
          ['Hair and grooming', 'Fresh haircut or tidy beard, clean nails.'],
          ['Smell', 'Light fragrance, fresh breath.'],
          ['Shoes', 'Clean. People notice.'],
          ['Sleep', 'Aim for a good night before. Tired people are less fun.'],
          ['Eat lightly', 'Avoid garlic-heavy or very heavy meals beforehand.'],
        ]],
        ['lbl', 'DAY-OF CHECKLIST'],
        ['chk', ['Confirmed time and place.', 'Phone charged.', 'Cash or card ready.', 'Arrive 10 minutes early.', 'Two stories ready.', 'Three questions ready.', 'Told a friend where I am going.']],
      ],
    },
    {
      kicker: 'BONUS 3', title: 'A date, minute by minute',
      blocks: [
        ['steps', [
          ['0-5 min', 'Greet warmly, compliment once, ease in with the place or journey.'],
          ['5-20 min', 'Light topics: travel, food, week. Use Echo, Dig, Share.'],
          ['20-45 min', 'Go warmer: passions, growing up, goals. Share your own too.'],
          ['45-60 min', 'Check the mood. If good, extend or plan the next one.'],
          ['60-90 min', 'End on a high. Do not outstay the good part.'],
        ]],
        ['lbl', 'SCRIPT FOR EXTENDING'],
        ['msg', 'I am enjoying this. Do you want to grab a bite or walk a bit more?', ''],
        ['lbl', 'SCRIPT FOR ENDING'],
        ['msg', 'I have to head off, but I loved this. I would like to see you again.', ''],
      ],
    },
    {
      kicker: 'BONUS 4', title: 'Handling common date problems',
      blocks: [
        ['steps', [
          ['She is late', 'Message once, relax, read a book. Do not complain when she arrives.'],
          ['Awkward silence', 'Use a callback or an observation. See the Playbook.'],
          ['She is quiet', 'Ask easy questions and share more yourself. Do not push.'],
          ['You are nervous', 'Tell her. "I am a bit nervous." It often relaxes both of you.'],
          ['Wrong spark', 'Be kind, finish the date politely, and be honest afterwards.'],
          ['She seems uncomfortable', 'Slow down, give space, ask if she wants to end early.'],
          ['Money awkwardness', 'Offer to pay, or split gracefully. No scenes.'],
        ]],
      ],
    },
    {
      kicker: 'BONUS 5', title: 'The second date',
      blocks: [
        ['p', 'The second date is where you get to know the person beyond the first-impression layer.'],
        ['steps', [
          ['Do something different', 'A new activity, not just another coffee.'],
          ['Go deeper', 'Move to Layer 2 and 3 questions, sharing your own.'],
          ['Be consistent', 'Be the same person you were on date one.'],
          ['Talk about future plans lightly', 'Ask about her next few weeks.'],
          ['Check in', '"How are you finding this so far?"'],
        ]],
        ['msg', 'I had a great time on our first date. Want to try [activity] this weekend?', 'Invite for the second'],
      ],
    },
    {
      kicker: 'WORKSHEET', title: 'Date review',
      blocks: [
        ['lbl', 'WHAT I ENJOYED'], ['lines', 3],
        ['lbl', 'WHAT I LEARNED ABOUT HER'], ['lines', 4],
        ['lbl', 'WHAT I WOULD DO DIFFERENTLY'], ['lines', 4],
        ['lbl', 'WOULD I SEE HER AGAIN?'], ['lines', 2],
      ],
    },
  ]);

  // Generic: also extend the intro "disclaimer"/CTAs not needed.
  return products;
};
