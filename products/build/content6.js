// "For her" editions (USA / Canada / UK): Starter Guide, Profile Fixer, 30-Day Confidence Challenge.
// General dating-safety and social-skills advice. No stereotypes, no promises. Evidence: research/conversation-psychology-35plus-both.md
const reg = require('./regional.js');
const NAME = 'Dorian Wolfe';
const BRAND = 'WOLFE';
const note = ['tip', 'A note on evidence', 'This guide uses general relationship, safety and social-skills advice plus common sense. There is little research on dating after 35, and almost none on conversations at this age, so treat everything as practical guidance, not a guarantee. Dorian Wolfe is an AI-generated character with no personal story.'];
const help = ['tip', 'If it feels heavier than nerves', 'If you feel hopeless, or think about harming yourself, please talk to someone now. USA and Canada: call or text 988. UK: Samaritans 116 123. Emergency: 911 (USA, Canada) or 999 (UK).'];

// ======================= 1. STARTER GUIDE FOR HER =======================
const starterHer = {
  id: 'wolfe-dating-again-starter-guide-for-her-us-ca-uk', kind: 'STARTER GUIDE · FOR HER · USA · CANADA · UK',
  titleLines: ['DATING AGAIN', 'AFTER 35', 'FOR WOMEN'],
  sub: 'A calm, safety-first plan for starting again after divorce, loss or a long time single. One small action in every chapter.',
  chapters: [
    {
      kicker: 'START HERE', title: 'You are not behind',
      blocks: [
        ['p', 'You may have been married for years, raising children, caring for parents, building a career, or simply busy. Now you want to meet someone again, and it feels like everyone else already knows how. They do not. Most people feel rusty.'],
        ['steps', [
          ['No clock', 'There is no correct age or timetable for starting again.'],
          ['No performance', 'You are not auditioning. You are deciding whether you enjoy someone.'],
          ['Safety first', 'Your comfort and safety come before politeness, always.'],
          ['Small steps', 'Each chapter ends with one small thing to try.'],
        ]],
        note,
      ],
    },
    {
      kicker: 'CHECK IN', title: 'Are you ready? A quick check',
      blocks: [
        ['p', 'There is no test you must pass. These questions only help you notice where you are.'],
        ['chk', ['I can talk about my past without feeling overwhelmed most of the time.', 'I want company or a relationship, not only to fill a silence.', 'I have people I can talk to if a date goes badly.', 'I have time and energy to meet someone this month, even once.', 'I know my basic limits: what I will and will not do.']],
        ['p', 'If you tick fewer than three, nothing is wrong. You may want more time, or some support first. See the support chapter near the end.'],
        help,
      ],
    },
    {
      kicker: 'GRIEF AND PACE', title: 'Grief, pace and expectations',
      blocks: [
        ['p', 'After a divorce or the death of a partner, mixed feelings are normal: relief, guilt, anger, excitement, sadness, sometimes in the same hour. Research on recovery shows wide differences between people, so there is no right amount of time to wait.'],
        ['steps', [
          ['Name it', 'Write down what you feel today. One line is enough.'],
          ['Set your pace', 'Decide how fast you want to go. "Slowly" is allowed.'],
          ['Keep your friends', 'A new person should add to your life, not replace it.'],
          ['Expect bumps', 'Some dates will be dull. Some will be nice and go nowhere. That is normal.'],
        ]],
        ['tip', 'Try this', 'Complete this sentence: "In six months, I would like dating to feel ..." Keep the answer on your phone.'],
      ],
    },
    {
      kicker: 'FOUNDATIONS', title: 'Rebuild your circle first',
      blocks: [
        ['p', 'People who have friends and activities do better at everything, including dating. A full week makes dating a nice extra, not a rescue.'],
        ['chk', ['Message one friend and make a plan.', 'Join one class, group or club (walking, books, choir, volunteering).', 'Say yes to one invitation you would usually turn down.', 'Tell one trusted person you are thinking of dating again.']],
        ['tip', 'Why it matters', 'You will want someone to call before and after a date. Pick that person now.'],
      ],
    },
    {
      kicker: 'YOUR STORY', title: 'Your story in 30 seconds',
      blocks: [
        ['p', 'You will be asked "So, tell me about yourself" often. A short, warm answer makes it easier.'],
        ['steps', [
          ['Who you are', 'Your work or what fills your days, in one line.'],
          ['What you enjoy', 'Two specific things (a walk by the river, baking, live music).'],
          ['What you are looking for', 'One honest sentence.'],
        ]],
        ['msg', 'I run a small bakery and spend weekends walking the dog by the river. I am back to meeting people after a few quiet years, and I am looking for something real, taken slowly.', 'For example only. Use your own words.'],
        ['lbl', 'WRITE YOURS'], ['lines', 4],
      ],
    },
    {
      kicker: 'THE PAST', title: 'Talking about your ex, your kids, your loss',
      blocks: [
        ['p', 'Say a short, honest line early. Save the long story for when you trust the person.'],
        ['steps', [
          ['Ex-partner', '"I was married for fourteen years. It ended two years ago and I am in a good place." Then move on.'],
          ['Late partner', '"I am widowed. I will mention him or her sometimes. That is part of my life."'],
          ['Children', 'Mention them early. Do not introduce a new person to them until you feel things are steady.'],
        ]],
        ['dont', ['Long stories about the ex on a first date.', 'Comparing a new person to your ex or late partner.', 'Sharing your address, your children\'s school, or your workplace early.']],
      ],
    },
    {
      kicker: 'MEETING PEOPLE', title: 'Where to meet people after 35',
      blocks: [
        ['steps', [
          ['Through friends', 'Tell friends you are open to being introduced. People like to help.'],
          ['Activities', 'Classes, clubs, volunteering, sports. You meet people while doing something.'],
          ['Community', 'Faith groups, neighbourhood events, alumni and work networks.'],
          ['Apps and sites', 'Useful, but you need a safety routine (next chapter).'],
        ]],
        ['tip', 'One goal for the month', 'Go to one place where you will see the same faces more than once.'],
      ],
    },
    {
      kicker: 'APPS AND SAFETY', title: 'Using dating apps safely',
      blocks: [
        ['p', 'US survey data (Pew, 2023, all ages) found women were more likely than men to feel they got too many messages and to report unwanted contact. So a routine helps.'],
        ['chk', ['Use a first name only. Keep your surname, address, workplace and children\'s details private.', 'Keep chatting inside the app until you trust the person.', 'Do a short video call before you meet.', 'Reverse-search a photo if something feels off.', 'Never send money, gift cards or crypto, or sensitive photos.', 'Block and report anyone who ignores a no.']],
        ['tip', 'You do not have to reply to everyone', 'Reply to people whose messages are warm and specific. Ignoring a message is allowed. Blocking is allowed.'],
      ],
    },
    {
      kicker: 'PROFILE', title: 'Photos and bio basics',
      blocks: [
        ['steps', [
          ['Photos', '4 to 6 recent ones. A clear smile in soft light, one full-length, one doing something you love.'],
          ['Bio', '2 to 4 lines. Something specific, something you love, and a question or an easy hook.'],
          ['Honesty', 'Real age and a recent photo. Surprises on the first date help nobody.'],
          ['Privacy', 'Avoid photos in front of your home, your children\'s school or your workplace.'],
        ]],
        ['tip', 'Want more?', 'The Profile Fixer for Women (35+) has templates, a photo audit and a rewrite worksheet.'],
      ],
    },
    {
      kicker: 'MESSAGES', title: 'The first message, and replying',
      blocks: [
        ['p', 'Anyone can send the first message. If you do, keep it short and easy to answer. If you receive one, you decide.'],
        ['chat', [['her', 'Hi Tom, you mention you cook. What is the dish you are proudest of?'], ['him', 'A slow-cooked lamb. It takes all day. What do you cook?'], ['her', 'Soups, mostly. Things that look after themselves.']]],
        ['tip', 'For examples only', 'Made-up names and lines that show a pattern. Use your own words.'],
        ['lbl', 'A QUICK FILTER FOR REPLYING'],
        ['ul', ['Is the message specific to me, or copy-paste?', 'Does it ask a question I want to answer?', 'Does it respect my pace and my no?']],
      ],
    },
    {
      kicker: 'KEEP IT GOING', title: 'Keep the conversation going',
      blocks: [
        ['steps', [
          ['Ask, then follow up', '"What is the best part of your week?" then "What made that good?"'],
          ['Share a little back', 'One question, one share. It keeps it from feeling like an interview.'],
          ['Ask about what matters', '"What are you hoping to find?" "How do you like to deal with disagreement?"'],
          ['Say your pace', '"I would like to go slowly" is a complete sentence.'],
        ]],
        ['tip', 'More questions', 'The Conversation Starters After 35 guide has cards for him, for her and for anyone.'],
      ],
    },
    {
      kicker: 'FIRST DATE', title: 'Your first-date safety plan',
      blocks: [
        ['chk', ['Meet in a public place, in daylight or early evening.', 'Make your own way there and back.', 'Tell a friend where you are going, who with, and when you will text them.', 'Share your live location with that friend.', 'Keep your phone charged and your drink and bag with you.', 'Leave if you feel uneasy. You do not owe anyone an explanation.']],
        ['tip', 'On paying', 'Customs vary. In all three countries a kind way to handle it is to offer to split, or say "next one is mine", and accept a no kindly.'],
      ],
    },
    {
      kicker: 'AFTER THE DATE', title: 'After the date',
      blocks: [
        ['p', 'Wait a day before you decide how it went. Many people leave a conversation thinking it went worse than the other person felt (the "liking gap"), though this was found in studies of strangers and students, not in daters over 35.'],
        ['steps', [
          ['If you liked it', 'Send a short message: "I enjoyed meeting you. Would you like to do it again?"'],
          ['If you are unsure', '"Thank you for tonight. I would like some time to think." That is allowed.'],
          ['If you did not', '"It was nice to meet you. I do not think we are a match. I wish you well."'],
        ]],
        ['lbl', 'DATE DEBRIEF'], ['lines', 4],
      ],
    },
    {
      kicker: 'BOUNDARIES', title: 'Saying no, clearly and kindly',
      blocks: [
        ['p', 'Saying no is a skill. It does not need a long reason.'],
        ['steps', [
          ['To a second date', '"Thank you, but I do not feel a match."'],
          ['To pressure', '"I am not comfortable with that. Please stop."'],
          ['To fast intimacy', '"I would like to go slowly."'],
          ['To contact after a no', 'Do not reply, and block. Keep the messages as a record.'],
        ]],
        ['tip', 'You do not need to be polite twice', 'If someone keeps contacting you after a clear no, you can block, report, and tell a friend.'],
      ],
    },
    {
      kicker: 'HEALTHY OR NOT', title: 'Is this relationship healthy?',
      blocks: [
        ['lbl', 'SIGNS IT IS HEALTHY'],
        ['ul', ['You feel calmer, not more anxious, after you see them.', 'They respect "no" and "not yet".', 'They are honest, including about awkward things.', 'You still see friends and keep your routines.']],
        ['lbl', 'SIGNS TO TAKE SERIOUSLY'],
        ['ul', ['They control who you see, what you wear, or your money.', 'They check your phone or track your location.', 'They put you down or lose their temper, then say it was your fault.', 'They isolate you from friends or family.', 'You feel afraid of them.']],
        ['tip', 'If you are frightened', 'You can get confidential help. See "Where to get help" near the end for numbers in the USA, Canada and the UK.'],
      ],
    },
    {
      kicker: 'YOUR PLAN', title: 'Your 30-day starter plan',
      blocks: [
        ['chk', ['Week 1: Read the guide. Call one friend. Write your 30-second story.', 'Week 2: Choose photos and write your bio. Join one activity.', 'Week 3: Send or answer a few messages using the filter. Do one video call.', 'Week 4: Meet someone for a safe, short coffee. Debrief and rest.']],
        ['tip', 'Remember', 'One small step each week is enough. You can stop at any time.'],
      ],
    },
    reg.supportChapter(),
    reg.etiquette(),
    ...reg.safety(true),
  ],
};

// ======================= 2. PROFILE FIXER FOR HER =======================
const profileHer = {
  id: 'wolfe-profile-fixer-for-women-35-plus-us-ca-uk', kind: 'WORKBOOK + SWIPE FILE · FOR HER · USA · CANADA · UK',
  titleLines: ['PROFILE', 'FIXER', 'FOR WOMEN 35+'],
  sub: 'Photos, a bio that sounds like you, and a safety routine for the messages that arrive.',
  chapters: [
    {
      kicker: 'INTRODUCTION', title: 'What your profile is for',
      blocks: [
        ['p', 'A profile has one job: to give a person a real, friendly reason to start a conversation. You do not have to impress everyone. You want the right few to feel they can reply.'],
        ['steps', [
          ['Be recent', 'Photos from the last year or two.'],
          ['Be specific', '"Sunday walker with a camera" says more than "adventurous".'],
          ['Be honest', 'Age and photos that match. Lies come out on the first date.'],
          ['Be private where it matters', 'Share personality, not your address or workplace.'],
        ]],
        note,
      ],
    },
    {
      kicker: 'STEP 1', title: 'Your photo plan',
      blocks: [
        ['chk', ['A clear, smiling headshot (main photo).', 'A full-length photo, so nobody is surprised.', 'You doing something you enjoy (hiking, baking, a class).', 'A relaxed candid, with a real smile.', 'Optional: you with friends (easy to tell which one is you), a pet or a place you love.']],
        ['lbl', 'LEAVE OUT'],
        ['dont', ['Heavy filters, or photos from many years ago.', 'Sunglasses in every photo.', 'Group shots where it is hard to tell who you are.', 'Photos at your front door, your children\'s school or your workplace.', 'Children\'s faces. Keep them private.']],
      ],
    },
    {
      kicker: 'STEP 2', title: 'Light, angle and ease',
      blocks: [
        ['steps', [
          ['Soft light', 'Face a window or stand in open shade.'],
          ['Eye level', 'Ask a friend to hold the camera at eye level.'],
          ['A real smile', 'Think of something that makes you laugh.'],
          ['Simple background', 'Tidy, uncluttered, nothing that shows your address.'],
          ['Wear what feels like you', 'Colours you like, clothes that fit.'],
        ]],
        ['tip', 'Try this', 'Ask a friend to take 20 photos in soft light. Pick the best three.'],
      ],
    },
    {
      kicker: 'STEP 3', title: 'The bio formula',
      blocks: [
        ['steps', [
          ['Line 1: who you are', 'What fills your days, in a specific detail.'],
          ['Line 2: what you love', 'Two or three specifics.'],
          ['Line 3: what you want', 'One honest sentence about what you are looking for.'],
          ['Line 4: an easy hook', 'A question or a "message me if ...".'],
        ]],
        ['msg', 'Nurse by day, bad singer in the car. Saturdays: farmers market, a long walk and soup. Looking for someone kind with a sense of humour. What is your go-to comfort food?', 'For example only. Use your own words.'],
        ['lbl', 'DRAFT YOUR BIO'], ['lines', 5],
      ],
    },
    {
      kicker: 'SWIPE FILE', title: '8 bio templates to adapt',
      blocks: [
        ['ul', [
          '"[Job or interest]. [Weekend ritual]. Looking for [quality]. Tell me your best [food, trail, film]."',
          '"Back in the dating pool after a few years. Slow and honest is my style. [Hobby] on weekends."',
          '"I laugh easily and cook badly. Ask me about [funny story topic]."',
          '"Walker, reader, tea drinker. Would like to meet someone who knows what he or she is looking for."',
          '"Mum of two grown kids and a very spoiled dog. Love [activity]. What is your favourite [thing]?"',
          '"I am here to meet someone kind, not to collect matches. [Interest] is a bonus."',
          '"[Place] local. [Interest]. If you can recommend a good [thing], we will get on."',
          '"Recently single, curious and in no hurry. Coffee first, then we will see."',
        ]],
        ['tip', 'Make it yours', 'Change two words in any template so it sounds like you.'],
      ],
    },
    {
      kicker: 'PROMPTS', title: 'Prompt answers to adapt',
      blocks: [
        ['steps', [
          ['A perfect Sunday', 'A slow breakfast, a long walk, and a book in the garden.'],
          ['I am looking for', 'Someone warm who takes his or her time and is honest.'],
          ['You will know I like you when', 'I send you my favourite song.'],
          ['My simple pleasures', 'Fresh bread, cold swims, and a good chat.'],
          ['Two truths and a lie', 'Choose something light and easy to guess.'],
        ]],
      ],
    },
    {
      kicker: 'SAFETY', title: 'Safety on your profile',
      blocks: [
        ['chk', ['First name only. No surname, address or workplace.', 'No photos that show where you live, your children\'s school or your car number plate.', 'Keep chatting inside the app until you trust the person.', 'Video call before meeting.', 'Never send money, gift cards or crypto, or private photos.', 'Block and report anyone who ignores a no.']],
        ['p', 'US survey data (Pew, 2023, all ages) found women were more likely than men to say they got too many messages and to report unwanted contact. A safety routine is not paranoia. It is a habit.'],
      ],
    },
    {
      kicker: 'MESSAGES', title: 'Handling the messages that arrive',
      blocks: [
        ['steps', [
          ['Use a filter', 'Reply to messages that are specific to you and ask an easy question.'],
          ['You can ignore', 'You never owe a reply.'],
          ['A polite close', '"Thank you for chatting. I do not think we are the right match. I wish you well."'],
          ['If it turns unpleasant', 'Do not argue. Block, report, and keep a screenshot.'],
        ]],
        ['tip', 'Take a break', 'If messages feel like too much, pause the app for a week. Nothing is lost.'],
      ],
    },
    {
      kicker: 'AUDIT', title: 'Photo audit',
      blocks: [
        ['p', 'Tick each photo you are keeping.'],
        ['chk', ['It is from the last two years.', 'My face is clear and I look like myself.', 'I look relaxed.', 'It shows nothing about where I live or work.', 'It shows nothing about my children.', 'A friend agrees it is a good one.']],
        ['lbl', 'MY FINAL SIX'], ['lines', 3],
      ],
    },
    {
      kicker: 'REWRITE', title: 'Rewrite your bio',
      blocks: [
        ['lbl', 'MY OLD BIO'], ['lines', 5],
        ['lbl', 'WHAT IS VAGUE OR TOO LONG?'], ['lines', 3],
        ['lbl', 'MY NEW BIO'], ['lines', 7],
      ],
    },
    {
      kicker: 'FEEDBACK', title: 'Ask a friend for feedback',
      blocks: [
        ['steps', [
          ['Ask', '"If you saw this profile, what would you guess about me?"'],
          ['Ask', '"Which photo looks most like me?"'],
          ['Ask', '"Is there anything that sounds unlike me?"'],
        ]],
        ['lbl', 'WHAT MY FRIEND SAID'], ['lines', 3],
      ],
    },
    {
      kicker: 'THIS WEEK', title: '7-day profile tune-up',
      blocks: [
        ['chk', ['Day 1: Gather 15 photos.', 'Day 2: Pick six.', 'Day 3: Write the bio.', 'Day 4: Add two prompt answers.', 'Day 5: Run the safety checklist.', 'Day 6: Ask a friend.', 'Day 7: Publish and rest. Check once a day, not ten times.']],
      ],
    },
    reg.etiquette(),
    ...reg.safety(true),
  ],
};

// ======================= 3. 30-DAY CHALLENGE FOR HER =======================
const days = [
  ['Day 1', 'Write down why you want to try dating again.'], ['Day 2', 'Smile and say hello to three people today.'],
  ['Day 3', 'Message one friend and make a plan.'], ['Day 4', 'Take a walk somewhere new.'],
  ['Day 5', 'Ask someone a follow-up question and listen to the answer.'], ['Day 6', 'Write your 30-second story.'], ['Day 7', 'Weekly review (below).'],
  ['Day 8', 'Have a coffee with a friend.'], ['Day 9', 'Practise saying "no thank you" out loud.'],
  ['Day 10', 'Choose three photos you like.'], ['Day 11', 'Join a class, club or group.'], ['Day 12', 'Compliment someone sincerely.'],
  ['Day 13', 'Write a bio draft.'], ['Day 14', 'Weekly review.'],
  ['Day 15', 'Set up your safety routine (first name, privacy, video call).'], ['Day 16', 'Send or answer one message using the filter.'],
  ['Day 17', 'Do a short video call with a friend to practise.'], ['Day 18', 'Write three questions you would like to ask a date.'],
  ['Day 19', 'Say your pace out loud, to yourself.'], ['Day 20', 'Do something kind for yourself.'], ['Day 21', 'Weekly review.'],
  ['Day 22', 'Plan a safe first-date: place, time, friend.'], ['Day 23', 'Practise your answer about your past.'],
  ['Day 24', 'Go to one event alone.'], ['Day 25', 'Suggest a short, public meet-up to someone you trust.'],
  ['Day 26', 'Meet for a short coffee, or practise with a friend.'], ['Day 27', 'Do a date debrief.'], ['Day 28', 'Weekly review.'],
  ['Day 29', 'Write what you learned about yourself.'], ['Day 30', 'Celebrate. Choose your next step.'],
];
const dayRows = (a, b) => ['chk', days.slice(a, b).map(([d, t]) => `**${d}:** ${t}`)];
const challengeHer = {
  id: 'wolfe-30-day-confidence-challenge-for-women-us-ca-uk', kind: 'WORKBOOK · FOR HER · USA · CANADA · UK',
  titleLines: ['30-DAY', 'CONFIDENCE', 'CHALLENGE'],
  sub: 'One small action a day for 30 days. For women dating again after 35. Print it, tick it, write on it.',
  chapters: [
    {
      kicker: 'START', title: 'How to use this workbook',
      blocks: [
        ['p', 'Confidence usually comes from doing small things, not from waiting to feel ready. Each day has one small action. Skip a day and carry on. Nothing here promises a result.'],
        ['steps', [
          ['Do one thing', 'Pick the day\'s action. It should take 5 to 20 minutes.'],
          ['Tick it', 'A tick is enough.'],
          ['Review weekly', 'On days 7, 14, 21 and 28, answer three questions.'],
          ['Go at your pace', 'You can stop, repeat or slow down.'],
        ]],
        note, help,
      ],
    },
    {
      kicker: 'WHERE I AM', title: 'Where I am today',
      blocks: [
        ['lbl', 'HOW I FEEL ABOUT DATING (1-10)'], ['lines', 1],
        ['lbl', 'WHAT WORRIES ME MOST'], ['lines', 3],
        ['lbl', 'ONE THING I WOULD LIKE TO BE ABLE TO DO AT THE END'], ['lines', 3],
      ],
    },
    { kicker: 'WEEK 1', title: 'Week 1: warm up', blocks: [dayRows(0, 7), ['lbl', 'WEEK 1 REVIEW'], ['lines', 3]] },
    { kicker: 'WEEK 2', title: 'Week 2: prepare', blocks: [dayRows(7, 14), ['lbl', 'WEEK 2 REVIEW'], ['lines', 3]] },
    { kicker: 'WEEK 3', title: 'Week 3: safe first steps', blocks: [dayRows(14, 21), ['lbl', 'WEEK 3 REVIEW'], ['lines', 3]] },
    { kicker: 'WEEK 4', title: 'Week 4: meet and reflect', blocks: [dayRows(21, 30), ['lbl', 'WEEK 4 REVIEW'], ['lines', 3]] },
    {
      kicker: 'LADDER', title: 'My exposure ladder',
      blocks: [
        ['p', 'List steps from easiest to hardest. Do the easiest first. Move up when it feels manageable.'],
        ['chk', ['1. (easiest) ________', '2. ________', '3. ________', '4. ________', '5. (hardest) ________']],
        ['lbl', 'NOTES: WHAT HELPED, WHAT IS HARD'], ['lines', 8],
      ],
    },
    {
      kicker: 'THOUGHTS', title: 'Changing a worrying thought',
      blocks: [
        ['steps', [
          ['The thought', '"I am too old to start again."'],
          ['The evidence for', 'What really supports it?'],
          ['The evidence against', 'What else is also true?'],
          ['A kinder thought', '"I am starting later than some and sooner than others, and that is fine."'],
        ]],
        ['lbl', 'MY THOUGHT'], ['lines', 2], ['lbl', 'A KINDER VERSION'], ['lines', 2],
      ],
    },
    {
      kicker: 'DEBRIEF', title: 'Date debrief',
      blocks: [
        ['lbl', 'WHAT WENT WELL'], ['lines', 2], ['lbl', 'WHAT I WOULD CHANGE'], ['lines', 2], ['lbl', 'HOW I FELT WITH THEM'], ['lines', 2], ['lbl', 'MY NEXT STEP'], ['lines', 1],
      ],
    },
    {
      kicker: 'NO LOG', title: 'My boundary and "no" log',
      blocks: [
        ['p', 'Write down each time you said no, or held a boundary. Notice that you can.'],
        ['lines', 18],
      ],
    },
    reg.supportChapter(),
    ...reg.safety(false),
  ],
};

module.exports = { NAME, BRAND, products: [starterHer, profileHer, challengeHer] };
