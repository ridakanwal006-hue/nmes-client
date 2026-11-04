// Flagship: Conversation Starters After 35 (for men and women, USA / Canada / UK).
// Evidence: research/conversation-psychology-35plus-both.md. Almost no research exists on first conversations among
// daters 35+, so the guide says so and labels what is research, what is common advice and what is inference.
const reg = require('./regional.js');
const NAME = 'Dorian Wolfe';
const BRAND = 'WOLFE';
const help = ['tip', 'If it feels heavier than nerves', 'If you feel hopeless, or think about harming yourself, please talk to someone now. USA and Canada: call or text 988. UK: Samaritans 116 123. Emergency: 911 (USA, Canada) or 999 (UK).'];
const C = (arr, tag) => arr.map(q => [tag, q]);

// ---------- card sets ----------
const himToHer = {
  open: [
    'What has been the best part of your week so far?',
    'What do you do when you have a free Saturday?',
    'What is something small you have been enjoying lately?',
    'What made you choose this place (or this app)?',
    'What is your favourite thing to eat when nobody is watching?',
    'What are you looking forward to this month?',
    'Is there a show, book or podcast you keep telling people about?',
    'What does a really good day off look like for you?',
  ],
  warm: [
    'What is something you are proud of that does not show on a profile?',
    'What do you like most about where you live?',
    'Who is the person you call when you have good news?',
    'What did you do for fun as a kid that you still miss?',
    'What kind of trip would you take if time and money were no problem?',
    'What has changed for you in the last few years that you are glad about?',
    'What does a good friend do for you?',
    'What would you like more of in your life right now?',
  ],
  steady: [
    'What would be a good pace for you? I am happy to go slowly.',
    'Is there anything that would help you feel comfortable on a first date?',
    'What are you hoping to find, if you do not mind me asking?',
    'Is there anything I should know about your schedule, so I can plan around it?',
    'Is there a place or an activity you would rather do than a restaurant?',
    'If I say something that does not land well, will you tell me?',
    'How do you like to stay in touch while we get to know each other: texts, calls, something else?',
    'Is there something you would like me to ask you about?',
  ],
};
const herToHim = {
  open: [
    'What does a normal week look like for you?',
    'What do you do for fun when you are not working?',
    'What is the best thing you have eaten recently?',
    'What made you decide to try meeting people again?',
    'What is something you could talk about for an hour?',
    'What is the last thing that made you laugh properly?',
    'Is there a place near here that you love?',
    'What are you looking forward to this month?',
  ],
  intent: [
    'What are you hoping to find? A relationship, company, something still undecided?',
    'What does a good relationship look like to you, day to day?',
    'How long has it been since your last relationship, and how are you feeling about dating now?',
    'What did you learn from your last relationship that you would do differently?',
    'How do you like to deal with it when you disagree with someone?',
    'What would you need from a partner that you could not do without?',
    'How do you feel about moving fast, moving slowly, or somewhere in between?',
    'Is there anything you want me to know early, so there are no surprises later?',
  ],
  life: [
    'Do you have children or other people you take care of? How does that shape your week?',
    'How are things between you and your ex now, in a sentence?',
    'What does your work take out of you, and what does it give you?',
    'How do you look after your health and your free time?',
    'Who are the people in your life that I would hear about?',
    'What are you building at the moment: a home, a career, a hobby?',
    'What would a good weekend with someone you care about look like?',
    'Is there anything that would make you feel safe and comfortable meeting me?',
  ],
};
const both = {
  light: [
    'What is the best thing that happened to you this week?',
    'If you could be anywhere for a long weekend, where would it be?',
    'What is a skill you wish you had picked up years ago?',
    'What is the one app on your phone you could not live without?',
    'What is your go-to meal when you cannot be bothered?',
    'What was the last concert, match or event you really enjoyed?',
    'What is your favourite season, and what do you do in it?',
    'What is a small thing that always puts you in a good mood?',
  ],
  honest: [
    'I have not done this in years, so I might be a bit rusty. How about you?',
    'What is the best part about being this age? I would like to hear yours.',
    'What do you know about yourself now that you wish you had known at 25?',
    'What is something you have let go of that felt heavy for a long time?',
    'What do you need to feel at ease with someone new?',
    'What would a good first few dates look like, for you?',
    'What kind of people make you feel at home?',
    'What is something you are working on in yourself right now?',
  ],
};

// ---------- chapters ----------
const chapters = [
  {
    kicker: 'START HERE', title: 'Why talking feels harder now',
    blocks: [
      ['p', 'You may be 35, 45 or 55. You may be newly divorced, widowed, coming out of a long relationship, or single for years. Either way, you know how to hold a conversation at work, with friends, with family. Yet a first message or a first date can make your mind go blank.'],
      ['p', 'That is common. It is not a flaw. This guide explains **why** it happens, shows what research does and does not say, and gives you **questions to ask**, for both sides: what he can ask her, what she can ask him, and what anyone can ask.'],
      ['steps', [
        ['What it is', 'A guide to conversation after 35: psychology, plain-English rules, 70+ question cards, topic scripts and worksheets.'],
        ['Who it is for', 'Men and women, in the USA, Canada and the UK, dating again or for the first time in years.'],
        ['What it is not', 'A set of tricks. Nothing here is built to manipulate anyone, and nothing promises a date or a partner.'],
      ]],
      ['tip', 'A note on evidence', 'I found almost no research on first conversations among people over 35. Most studies of conversation used students or strangers in labs. So this guide marks each idea as research (with its limits), common advice, or my own reasoning. Dorian Wolfe is an AI-generated character with no personal story, so none of this is "what happened to me".'],
    ],
  },
  {
    kicker: 'THE MIND', title: 'Eight things going on in your head',
    blocks: [
      ['p', 'Usual reasons conversation feels hard after 35. They come from counselling-style advice and common sense, not from studies of this age group, so treat them as likely, not proven.'],
      ['steps', [
        ['1. "I am rusty"', 'It has been years, and the way people meet has changed. **Do:** expect to be clumsy at first, and say once: "I have not done this in a while."'],
        ['2. "I will look foolish"', 'Fear of saying the wrong thing makes you say nothing. **Do:** a short, simple question is better than a clever one.'],
        ['3. "What if I get hurt again?"', 'After a divorce or loss, it is normal to be guarded. **Do:** go at a pace you choose, and say so.'],
        ['4. Comparing with the ex or late spouse', 'It is easy to hold a new person up against someone you knew for years. **Do:** notice the comparison, then ask about the person in front of you.'],
        ['5. "I do not have time"', 'Work, children, parents to care for. **Do:** suggest simple plans (a coffee, a walk).'],
        ['6. "I am too old, or too (anything)"', 'Age and body worries make people hide. **Do:** be honest about your age and aim for warm, not impressive.'],
        ['7. Grief and guilt', 'Guilt or rawness can surface mid-conversation. **Do:** it is fine to say "I lost my husband/wife, and some days are harder." There is no right timetable.'],
        ['8. "I do not know the rules any more"', 'Apps, texting norms, who messages first. **Do:** there is no single rule. Be clear and kind.'],
      ]],
    ],
  },
  {
    kicker: 'WHAT RESEARCH SAYS', title: 'Three findings, and their limits',
    blocks: [
      ['p', 'The few findings with support. All come from students, strangers or general adults, not daters over 35. Use them as ideas, not rules.'],
      ['steps', [
        ['Follow-up questions', 'Huang and colleagues (2017) found people who asked more questions, especially **follow-ups**, were better liked, and in a speed-dating sample were more likely to get a "yes" for a second date. **Limit:** other researchers have debated the method, and asking is not listening.'],
        ['The liking gap', 'Boothby and colleagues (2018) found people tend to **underestimate** how much the other person liked them after a conversation. **Limit:** strangers and students. Safe reading: they may have enjoyed it more than you think.'],
        ['Matching depth', 'Aron and colleagues (1997): pairs who took turns answering gradually more personal questions felt closer than pairs given small talk. **Limit:** a lab task. No list of questions makes people fall in love.'],
      ]],
      ['lbl', 'WHAT US SURVEY DATA ADDS'],
      ['p', 'A Pew survey of US online daters (2023, all ages) found men were much more likely to feel they got too few messages, and women more likely to feel they got too many or to report unwanted contact. The same app can feel like silence to one person and noise to another.'],
      
    ],
  },
  {
    kicker: 'THE RULES', title: 'Five rules for conversation after 35',
    blocks: [
      ['steps', [
        ['1. One question, one share', 'Ask something, then share a little yourself. Questions without sharing feel like an interview. Sharing without questions feels like a speech.'],
        ['2. Follow up before you switch', 'When they answer, ask one more thing about that answer before you change topic. "Tell me more", "What did you like about it?"'],
        ['3. Match the depth', 'If they answer lightly, stay light. If they open up, you may go a step deeper. Do not skip ahead.'],
        ['4. Be clear about your pace', 'Say in plain words what pace you like. "I would like to go slowly" is a complete sentence.'],
        ['5. Be honest about the basics', 'Age, kids, divorce, work. Short and kind. You do not have to share every detail on day one.'],
      ]],
      ['tip', 'The "I am nervous" line', 'It is allowed to say, "I will be honest, I am a bit nervous. It has been a while." Most people relax when you do.'],
    ],
  },
  {
    kicker: 'WHO ASKS WHAT', title: 'Who goes first, and what to ask',
    blocks: [
      ['p', '"Should the man ask, or the woman?" There is **no strong evidence that one gender should always go first.** Apps differ. What matters is that the first message is easy to answer.'],
      ['lbl', 'WHY THE QUESTIONS DIFFER (INFERENCE, NOT PROVEN)'],
      ['ul', ['Many men find it hard to get **any** replies, so they need questions that are warm, low-pressure and easy to answer.', 'Many women get **too many** messages, some unwanted, so they need questions that check **intentions, pace and comfort** quickly.', 'Anyone can use any card in this guide.']],
      ['steps', [
        ['For him to ask her', 'Curious, light, easy to answer, with a clear offer to go at her pace.'],
        ['For her to ask him', 'What he wants, how he handles disagreement, what his life looks like, so she can decide how she feels.'],
        ['For anyone', 'Light questions, and honest ones for nerves.'],
      ]],
    ],
  },
  {
    kicker: 'FOR HIM TO ASK HER', title: 'Question cards: for him, for her, for anyone (70)', noTitle: true,
    blocks: [['cards', C(himToHer.open, 'HIM → HER · EASY')]],
  },
  {
    kicker: 'FOR HIM TO ASK HER', title: 'For him to ask her: warm questions', noTitle: true, hideToc: true,
    blocks: [['cards', C(himToHer.warm, 'HIM → HER · WARM')]],
  },
  {
    kicker: 'FOR HIM TO ASK HER', title: 'For him to ask her: steady and respectful', noTitle: true, hideToc: true,
    blocks: [['cards', C(himToHer.steady, 'HIM → HER · STEADY')]],
  },
  {
    kicker: 'FOR HER TO ASK HIM', title: 'For her to ask him: easy openers', noTitle: true, hideToc: true,
    blocks: [['cards', C(herToHim.open, 'HER → HIM · EASY')]],
  },
  {
    kicker: 'FOR HER TO ASK HIM', title: 'For her to ask him: intentions and pace', noTitle: true, hideToc: true,
    blocks: [['cards', C(herToHim.intent, 'HER → HIM · INTENTIONS')]],
  },
  {
    kicker: 'FOR HER TO ASK HIM', title: 'For her to ask him: his life', noTitle: true, hideToc: true,
    blocks: [['cards', C(herToHim.life, 'HER → HIM · LIFE')]],
  },
  {
    kicker: 'FOR ANYONE', title: 'For anyone: light questions', noTitle: true, hideToc: true,
    blocks: [['cards', C(both.light, 'ANYONE · LIGHT')]],
  },
  {
    kicker: 'FOR ANYONE', title: 'For anyone: honest questions', noTitle: true, hideToc: true,
    blocks: [['cards', C(both.honest, 'ANYONE · HONEST')]],
  },
  {
    kicker: 'GOOD AND WORRYING ANSWERS', title: 'What the answers tell you',
    blocks: [
      ['p', 'Questions are only half of it. Listen to the answers, and to how the other person treats your answers. This is **common-sense guidance**, not a test. One answer never decides anything.'],
      ['lbl', 'ANSWERS THAT FEEL GOOD'],
      ['ul', ['They answer, then ask you something back.', 'They are specific. They tell a small story, not a slogan.', 'They respect "no", "not yet" or "I would like to go slower".', 'They are honest when the answer is awkward ("we are still sorting out the divorce").', 'You feel calmer, not more anxious, after the chat.']],
      ['lbl', 'ANSWERS TO SLOW DOWN FOR'],
      ['ul', ['They speak badly about every ex and blame everyone else.', 'They push for more contact or more intimacy than you want.', 'They get annoyed when you say "not yet".', 'Their story changes between messages.', 'They ask you for money, or for photos or details you are not ready to share. (See the scam red-flag checklist.)']],
      ['tip', 'Trust yourself', 'If something feels wrong, you do not need to explain. You can end the chat politely, or stop replying if you feel unsafe.'],
    ],
  },
  {
    kicker: 'SENSITIVE TOPICS', title: 'Hard topics, said simply',
    blocks: [
      ['p', 'No professional body sets rules on what to say when. This is common counselling-style guidance, so adapt it. Say a **short, honest line** early. Save the long story for when you trust each other.'],
      ['steps', [
        ['Your ex', '"I was married for twelve years. It ended two years ago, and I am in a good place now." Then move on. Avoid long stories or running them down.'],
        ['Your late spouse', '"I am widowed. I lost my wife / husband three years ago. I will mention them sometimes, and that is part of my life." It is fine to say this early.'],
        ['Children', 'Mention them early, because they affect your time. Wait to introduce them to someone new until things feel steady.'],
        ['Age', 'Be honest. "I am 47." You do not have to apologise.'],
        ['Work and money', 'Keep it light at first. Share more as trust builds. Never lend money to someone you have just met.'],
        ['Health', 'Share what affects plans when it becomes relevant. You do not owe anyone your medical history on date one.'],
        ['What you want', '"I am looking for something real, and I do not mind if it takes time." Ask the same, plainly.'],
        ['Exclusivity, pace', 'Do not guess. "I am enjoying this. Are you seeing other people?" And: "I would like to go slowly." Consent matters at every step.'],
      ]],
    ],
  },
  {
    kicker: 'MESSAGES', title: 'First messages and replies',
    blocks: [
      ['p', 'A first message needs one thing: it must be easy to answer. Use something from their profile, ask one question, and keep it short.'],
      ['lbl', 'EXAMPLE: HIM TO HER'],
      ['chat', [['him', 'Hi Priya, I noticed your photo with the lake. Do you get out there much?'], ['her', 'Most weekends in summer. Do you hike?'], ['him', 'Slowly, and with snacks. What is your favourite trail?']]],
      ['lbl', 'EXAMPLE: HER TO HIM'],
      ['chat', [['her', 'Hi Tom, you mention you cook. What is the dish you are proudest of?'], ['him', 'A slow-cooked lamb. It takes all day. What do you cook?'], ['her', 'Soups, mostly. I like things that look after themselves.']]],
      ['tip', 'For examples only', 'Made-up names and messages that show a pattern. Use your own words. To end a chat politely: "Thank you for chatting. I do not think we are the right match, but I wish you well."'],
    ],
  },
  {
    kicker: 'THE FIRST DATE', title: 'A simple flow for the first hour',
    blocks: [
      ['steps', [
        ['0-5 minutes', 'Say hello, ask how the journey was, and say one honest line: "I am a bit nervous."'],
        ['5-20 minutes', 'Easy questions. Place, food, weekend. Follow up on one thing they say.'],
        ['20-45 minutes', 'Warm questions. Work, family, interests. Share a little in return.'],
        ['45-60 minutes', 'Check the pace. "I have enjoyed this. Would you like to do something again?" A clear yes, a no, or a maybe are all fine.'],
      ]],
      ['lbl', 'IF CONVERSATION STALLS'],
      ['ul', ['Return to something they said earlier: "You mentioned the lake..."', 'Ask a light card: "What are you looking forward to this month?"', 'Say what you notice: "This place is lovely, have you been here before?"', 'Pause. A short silence is not a failure.']],
      ['tip', 'The liking gap again', 'After the date, you may think it went worse than it did. Wait a day before you decide.'],
    ],
  },
  {
    kicker: 'AVOID', title: 'Questions to leave out',
    blocks: [
      ['dont', ['"Why are you still single?"', '"How much do you earn?" or "Do you own your home?" on a first date.', '"How many people have you slept with?"', 'Anything that compares them to your ex.', 'Questions fired one after another, without sharing back.', 'Anything you would not want asked of you.']],
      ['p', 'If someone asks you something you do not want to answer, you are allowed to say, "I would rather not say yet", and then ask them something else.'],
    ],
  },
  {
    kicker: 'WORKSHEET', title: 'Your conversation sheet',
    blocks: [
      ['lbl', 'MY 30-SECOND STORY'],
      ['lines', 4],
      ['lbl', 'THREE THINGS I CAN TALK ABOUT'],
      ['lines', 3],
      ['lbl', 'MY ONE-LINE ANSWER ABOUT MY PAST'],
      ['lines', 2],
      ['lbl', 'MY PACE SENTENCE'],
      ['lines', 2],
      ['lbl', 'FIVE CARDS I WILL TRY THIS WEEK'],
      ['lines', 5],
    ],
  },
  reg.etiquette(),
  ...reg.safety(true),
  {
    kicker: 'REMEMBER', title: 'Small steps beat perfect lines',
    blocks: [
      ['p', 'You do not need to be smooth. You need to be **curious, honest and kind**. Ask one question. Follow up once. Share a little. Go at your pace.'],
      ['chk', ['I tried one easy card this week.', 'I followed up on an answer.', 'I said one honest line about myself.', 'I said my pace out loud.', 'I stopped when something felt wrong.']],
      ['p', 'Sources used, in short: Huang et al. 2017 (question asking), Boothby et al. 2018 (liking gap), Aron et al. 1997 (closeness), Pew Research Center 2023 (US online daters). All with the limits noted above.'],
    ],
  },
];

const starters35 = {
  id: 'wolfe-conversation-starters-35-plus-us-ca-uk', kind: 'GUIDE + 70 CARDS · USA · CANADA · UK',
  titleLines: ['CONVERSATION', 'STARTERS', 'AFTER 35'],
  sub: 'The psychology of why talking feels hard, and what he can ask her, what she can ask him, and what anyone can ask.',
  chapters,
};
module.exports = { NAME, BRAND, products: [starters35] };
