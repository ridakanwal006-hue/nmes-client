// Second product set (from the men-over-40 research). Same block types as content.js, plus ['cards', [[tag, text], ...]].
const NAME = 'Dorian Wolfe';
const BRAND = 'WOLFE';

const note = ['tip', 'A note on evidence', "This guide uses general relationship and social-skills research plus common sense. Studies of men over 40 are limited, so treat everything here as practical guidance, not a guarantee. It is not therapy, medical advice, legal advice or financial advice."];
const help = ['tip', 'If it feels heavier than nerves', 'If you feel hopeless, or think about harming yourself, please talk to someone now. In the US, call or text 988. In the UK, Samaritans: 116 123. Elsewhere, findahelpline.com lists local services.'];

// ============ 1. SCAM RED-FLAG CHECKLIST (free, 2 pages) ============
const scamChecklist = {
  id: 'wolfe-scam-red-flag-checklist', kind: 'FREE CHECKLIST', noToc: true, noEnd: true,
  titleLines: ['SCAM', 'RED-FLAG', 'CHECKLIST'],
  sub: 'Ten warning signs of a dating scam, what to do if something feels wrong, and where to report it.',
  chapters: [
    {
      kicker: 'CHECKLIST', title: '10 red flags',
      blocks: [
        ['p', 'Tick any that apply to someone you met online. One flag is a reason to slow down. **Two or more: stop and talk to someone you trust.**'],
        ['chk', [
          'Their photos look too perfect, or a reverse image search finds the same pictures under another name.',
          'They want to move from the app to WhatsApp, Telegram or text within days.',
          'They say "I love you" or call you "soulmate" very quickly, before you have met.',
          'They always have a reason not to video call or meet in person.',
          'They live or work far away: overseas, military, a ship, an oil rig, "a doctor abroad".',
          'Their story has gaps or changes when you ask simple questions.',
          'A sudden emergency: hospital bill, customs fee, plane ticket, "business problem".',
          'They ask for money, gift cards, crypto, wire transfers or your bank details, in any amount.',
          'They pressure you to act fast, or to keep the relationship secret from family and friends.',
          'They bring up an investment or trading app ("my cousin made a fortune").',
        ]],
        ['tip', 'Remember', 'Real people will happily video call, meet in a public place, and let you take your time. Scammers cannot.'],
      ],
    },
    {
      kicker: 'IF SOMETHING FEELS WRONG', title: 'What to do',
      blocks: [
        ['steps', [
          ['1. Stop', 'Do not send more money or personal information. Do not confront them: it can make things worse.'],
          ['2. Keep evidence', 'Screenshots, usernames, phone numbers, payment details, dates.'],
          ['3. Call your bank', 'Call your bank or card provider straight away. Speed matters.'],
          ['4. Report', 'US: reportfraud.ftc.gov (FTC) and ic3.gov (FBI). UK: Action Fraud / Report Fraud. Elsewhere: your local police or consumer authority. Also report the profile on the dating app.'],
          ['5. Tell someone', 'A friend, family member or helpline. Scammers rely on shame and secrecy.'],
          ['6. Be kind to yourself', 'It is not your fault. Skilled criminals do this for a living.'],
        ]],
        ['lbl', 'SAFE-MEETING RULES'],
        ['ul', ['Video call before you meet.', 'Meet in a public place and tell a friend where you are going.', 'Use your own transport.', 'Keep your address, workplace and finances private until you really know the person.']],
        ['tip', 'The numbers', 'People 60+ reported about $2.4 billion in fraud losses to the FTC in 2024 (all fraud types). Verify current figures on ftc.gov. Dorian Wolfe is an AI-generated character. General information, not legal or financial advice.'],
      ],
    },
  ],
};

// ============ 2. STARTER GUIDE ============
const starter = {
  id: 'wolfe-dating-again-starter-guide', kind: 'STARTER GUIDE',
  titleLines: ['DATING', 'AGAIN', 'AFTER 40'],
  sub: 'A calm, practical guide for men starting over after divorce, loss, or a long time single.',
  chapters: [
    {
      kicker: 'INTRODUCTION', title: "You're not behind",
      blocks: [
        ['p', 'If you are 40, 50 or 60 and dating again, you may feel out of practice, awkward, or worried that you have missed your chance. That feeling is common. It does not mean something is wrong with you.'],
        ['steps', [
          ['What this guide is', 'A step-by-step plan: get ready, rebuild your circle, meet people, talk, go on dates, handle rejection, set boundaries, stay safe.'],
          ['What it is not', 'It is not a set of tricks. There are no lines that make anyone fall for you. It will not make promises about results.'],
          ['How to use it', 'Read one chapter a day. Do the "Try this" action at the end. Move at your own pace.'],
        ]],
        note,
      ],
    },
    {
      kicker: 'CHAPTER 1', title: 'Are you ready? A quick check',
      blocks: [
        ['p', 'There is no right answer, and no deadline. Use these questions to see where you are.'],
        ['chk', [
          'I can talk about my past relationship without anger most of the time.',
          'I have friends or activities outside of dating.',
          'I want companionship, not just to fill a silence.',
          'I can handle someone saying no.',
          'I have the time and energy to go on a date.',
          'I am willing to be a little awkward at the start.',
        ]],
        ['p', 'If you ticked most, you are probably ready to start. If not, go slower and spend more time on chapters 2 and 3 first. Studies of loneliness after divorce or widowhood suggest that a new partner can help, but there is no single timeline that works for everyone.'],
        ['tip', 'Try this', 'Write down one reason you want to date again. Keep it somewhere you can see it.'],
      ],
    },
    {
      kicker: 'CHAPTER 2', title: 'Grief, pace and expectations',
      blocks: [
        ['steps', [
          ['Let yourself grieve', 'Divorce, separation or the death of a partner is a loss. Sadness, anger and numbness are normal.'],
          ['Go at your pace', 'You do not have to date because others say you should, or avoid dating because others say it is too soon.'],
          ['Expect awkward moments', 'You will say the wrong thing sometimes. Smile, laugh, carry on.'],
          ['One thing at a time', 'You do not need to rebuild your whole life before a first coffee.'],
        ]],
        ['tip', 'If you are widowed', 'Many widowed people feel guilty when they think about dating. This is common. There is no correct date to start, and your feelings for your late partner do not have to disappear.'],
        help,
      ],
    },
    {
      kicker: 'CHAPTER 3', title: 'Rebuild your circle first',
      blocks: [
        ['p', 'After a divorce, many men find their social life shrank. Loneliness is hard on its own, and it makes dating feel higher-stakes. Rebuilding friendships takes pressure off.'],
        ['ul', [
          'Message one old friend and suggest a coffee or a walk.',
          'Join a group: walking club, running club, volunteering, a class, a men\'s shed, a faith or community group.',
          'Say yes to invitations, even when you feel like staying home.',
          'Tell one trusted person you are thinking of dating again.',
        ]],
        ['tip', 'Try this', 'This week, message one friend and make one plan.'],
      ],
    },
    {
      kicker: 'CHAPTER 4', title: 'Your story in 30 seconds',
      blocks: [
        ['p', 'Someone says, "Tell me about yourself," and your mind goes blank. Use **Present, Past, Passion** and keep it under 30 seconds.'],
        ['steps', [
          ['Present', 'What you do now, in one line.'],
          ['Past', 'One interesting thing that shaped you.'],
          ['Passion', 'Something you enjoy, said with energy.'],
        ]],
        ['lbl', 'ILLUSTRATIVE EXAMPLE'],
        ['msg', 'I run a small landscaping business. I grew up near the coast, so I am happiest outdoors. Lately I am trying to get better at cooking, with mixed results. What about you?', 'Then hand it back'],
        ['dont', ['Do not recite your CV.', 'Do not list achievements.', 'Do not turn it into a monologue.']],
        ['tip', 'Try this', 'Write and say your 30-second story out loud three times.'],
      ],
    },
    {
      kicker: 'CHAPTER 5', title: 'Talking about your ex and your kids',
      blocks: [
        ['p', 'You do not have to hide your past, but you do not have to tell it all on the first date either.'],
        ['lbl', 'ABOUT YOUR EX: WHAT YOU COULD SAY (ILLUSTRATIVE)'],
        ['msg', 'We wanted different things. It ended, and I learned a lot from it.', 'Short, calm, no blame'],
        ['dont', ['Complaining about your ex for more than a sentence or two.', 'Details of the divorce, money or legal fights.', 'Comparing her to your ex.']],
        ['lbl', 'ABOUT YOUR KIDS: WHAT YOU COULD SAY (ILLUSTRATIVE)'],
        ['msg', 'I have two kids. They are a big part of my life, and I am proud of them.', 'Honest and positive'],
        ['p', 'Introducing kids to someone new is a big step. Many people wait until the relationship is steady and exclusive. There is no fixed rule, so go at the pace that is right for your family.'],
      ],
    },
    {
      kicker: 'CHAPTER 6', title: 'Where to meet people after 40',
      blocks: [
        ['steps', [
          ['In person', 'Friends of friends, classes, volunteering, hobby clubs, faith groups, running or walking groups, community events.'],
          ['Online', 'Apps and sites such as OurTime, SilverSingles, Match or eharmony. Prices and features vary, so check each site.'],
          ['A mix', 'Do both. Online dating is common, but in a 2022 Pew survey only about 17% of adults 50+ had ever used a dating app, so many people still meet in person.'],
        ]],
        ['tip', 'Try this', 'Pick one in-person activity you would enjoy anyway, and go this week.'],
      ],
    },
    {
      kicker: 'CHAPTER 7', title: 'Using dating apps safely',
      blocks: [
        ['chk', [
          'Use a recent photo and be honest about age.',
          'Video call before meeting.',
          'Meet in a public place and tell a friend.',
          'Keep your address, workplace and finances private.',
          'Never send money, gift cards or crypto.',
          'Be wary of anyone who rushes to another app or says "I love you" quickly.',
        ]],
        ['tip', 'Learn more', 'People 60+ reported about $2.4 billion in fraud losses to the FTC in 2024 (all fraud types). See the free Scam Red-Flag Checklist and the Scam-Proof Dating Guide for 50+.'],
      ],
    },
    {
      kicker: 'CHAPTER 8', title: 'Photos and bio basics',
      blocks: [
        ['steps', [
          ['Photos', 'Four to six clear, recent photos: a smiling headshot, a full-body shot, you doing something you enjoy, one with friends. Good light helps. Avoid hats and sunglasses in every photo.'],
          ['Bio', 'Two or three short sentences: what you enjoy, what you are looking for, and an easy question to answer.'],
          ['Tone', 'Positive and specific. Avoid lists of dislikes or complaints about past partners.'],
        ]],
        ['lbl', 'ILLUSTRATIVE EXAMPLE'],
        ['msg', 'Weekend hiker, terrible cook, decent listener. Looking for someone to laugh with and explore new places. Tell me the best meal you have had this year.', ''],
        ['dont', ['Old photos.', 'Lying about age, height or looks.', '"No drama" or "no games" as your headline.']],
      ],
    },
    {
      kicker: 'CHAPTER 9', title: 'The first message',
      blocks: [
        ['p', 'Many men feel they get too few messages. In a 2023 Pew survey of online daters (all ages), 64% of men said they felt insecure about getting too few. You are not alone. A better first message helps.'],
        ['steps', [
          ['1. Be specific', 'Mention one thing from her profile.'],
          ['2. Ask one easy question', 'Something she can answer in a sentence.'],
          ['3. Keep it short and warm', 'Two or three lines.'],
        ]],
        ['msg', 'That photo from the lake: please tell me it was as good as it looks.', ''],
        ['msg', 'I liked what you said about gardening. What are you growing this year?', ''],
        ['msg', 'Best coffee spot you have found lately? I need a recommendation.', ''],
        ['dont', ['Just "hi" or "hey".', 'Compliments about her body.', 'Copy-pasted messages.']],
      ],
    },
    {
      kicker: 'CHAPTER 10', title: 'Keep the conversation going',
      blocks: [
        ['p', 'A conversation stays alive when you show interest and share something of yourself. Use **Echo, Dig, Share**.'],
        ['steps', [
          ['Echo', 'Repeat a key word she said, with curiosity. "Lisbon! What took you there?"'],
          ['Dig', 'Ask what she liked or why. "What was the best part?"'],
          ['Share', 'Offer a short story or opinion of your own.'],
        ]],
        ['tip', 'The 1:1 rule', 'For every question you ask, share one thing about yourself. This stops it feeling like an interview.'],
        ['p', 'When she tells you something personal: acknowledge it, say back what you heard, ask a gentle question, and share briefly. Do not try to fix it or turn it into your story.'],
      ],
    },
    {
      kicker: 'CHAPTER 11', title: 'The first date',
      blocks: [
        ['steps', [
          ['Choose a simple plan', 'Coffee or a walk. 60 to 90 minutes. Public place.'],
          ['Arrive early', 'Phone on silent, put away.'],
          ['Start light', 'Talk about the place, the journey, something easy.'],
          ['Then go warmer', 'Interests, travel, food, work you enjoy.'],
          ['Share, don\'t interview', 'Use the 1:1 rule.'],
          ['End on a high', 'Leave while it is going well. Say you enjoyed it, and whether you would like to meet again.'],
        ]],
        ['lbl', '10 QUESTIONS TO TRY'],
        ['qs', [
          'What was the best part of your week?',
          'What do you do to unwind?',
          'What was your favourite trip?',
          'What are you looking forward to?',
          'What is a hobby you would do all day?',
          'What did you enjoy about growing up where you did?',
          'What is a skill you would love to learn?',
          'What makes you laugh?',
          'What is a good day like for you?',
          'What matters to you most right now?',
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 12', title: 'After the date',
      blocks: [
        ['p', 'Send a message within a day. Do not play games.'],
        ['msg', 'I had a great time today. I would like to see you again. Free Saturday?', 'If you are interested'],
        ['msg', 'Thank you for meeting me. I enjoyed meeting you, but I do not think we are a match. I wish you well.', 'If you are not'],
        ['p', 'If she is not interested, thank her and let it go.'],
      ],
    },
    {
      kicker: 'CHAPTER 13', title: 'Rejection and ghosting',
      blocks: [
        ['steps', [
          ['It is information about fit', 'It is not a verdict on your worth.'],
          ['Take a short break', 'Walk, talk to a friend, do something you enjoy.'],
          ['Learn one thing', 'Then move on. Do not argue or ask "why" repeatedly.'],
          ['Ghosting', 'Send one light message if you wish, then let it go.'],
        ]],
        ['p', 'For more, see the Rejection and Resilience guide and the "She Went Quiet" guide.'],
      ],
    },
    {
      kicker: 'CHAPTER 14', title: 'Boundaries and pace',
      blocks: [
        ['p', 'A boundary is a calm statement about what you need or are comfortable with. It is not a punishment or a threat.'],
        ['msg', 'I am enjoying this, and I would like to take it slowly.', ''],
        ['msg', 'I am not comfortable with that, but I would love to do something else.', ''],
        ['msg', 'I would like to be exclusive. How do you feel about that?', 'A clear, kind question'],
        ['p', 'Respect hers too. If she says no or slows things down, accept it without argument.'],
      ],
    },
    {
      kicker: 'CHAPTER 15', title: 'Is this relationship healthy?',
      blocks: [
        ['lbl', 'SIGNS OF HEALTH'],
        ['ul', ['You can be yourself.', 'She respects your time, friends and boundaries.', 'Both of you share and listen.', 'Disagreements are handled calmly.', 'Your words and actions match.']],
        ['lbl', 'WARNING SIGNS'],
        ['dont', ['Rapid, intense flattery followed by control or withdrawal.', 'Blame, guilt or dismissing your feelings.', 'Pressure about money, secrecy or isolation from friends.', 'A story that keeps changing.']],
        ['tip', 'If you feel unsafe', 'Emotional pressure, intimidation or violence are not normal. In the US, the National Domestic Violence Hotline is 1-800-799-7233.'],
      ],
    },
    {
      kicker: 'CHAPTER 16', title: 'Your 30-day starter plan',
      blocks: [
        ['chk', [
          'Week 1: Message one friend. Join one group or activity. Write your 30-second story.',
          'Week 1: Take three new photos in good light.',
          'Week 2: Write or refresh your bio. Read the scam checklist.',
          'Week 2: Send two thoughtful first messages.',
          'Week 3: Keep two conversations going with Echo, Dig, Share.',
          'Week 3: Suggest one coffee or walk.',
          'Week 4: Go on a first date, or a friendly practice meet-up.',
          'Week 4: Review what went well and what to try next.',
        ]],
        ['tip', 'Next step', 'For a daily plan with worksheets, see the 30-Day Confidence Challenge.'],
      ],
    },
    {
      kicker: 'HELP', title: 'Resources and help',
      blocks: [
        ['ul', [
          'Crisis or distress: US 988 (call or text). UK Samaritans 116 123. Elsewhere findahelpline.com.',
          'Scams: reportfraud.ftc.gov and ic3.gov (US). Action Fraud / Report Fraud (UK).',
          'Domestic abuse: US National Domestic Violence Hotline 1-800-799-7233.',
          'Therapy: ask your doctor, or look for a licensed therapist who uses CBT.',
          'Community: men\'s sheds, walking clubs, volunteering groups.',
        ]],
        note,
      ],
    },
  ],
};

// ============ 4. 30-DAY CONFIDENCE CHALLENGE (workbook) ============
const week = (kick, title, items) => ({
  kicker: kick, title,
  blocks: [
    ['p', 'Tick each task when you do it. Small steps count.'],
    ['chk', items],
    ['lbl', 'WHAT I DID'], ['lines', 3],
    ['lbl', 'HOW IT FELT'], ['lines', 2],
    ['lbl', 'WHAT I LEARNED'], ['lines', 2],
  ],
});
const workbook = {
  id: 'wolfe-30-day-confidence-workbook', kind: 'WORKBOOK',
  titleLines: ['30-DAY', 'CONFIDENCE', 'CHALLENGE'],
  sub: 'One small action a day. Build the skills and the courage to date again.',
  chapters: [
    {
      kicker: 'START HERE', title: 'How to use this workbook',
      blocks: [
        ['p', 'Confidence grows from doing things, not from waiting to feel ready. Each day has one small task. Most take 5-10 minutes.'],
        ['steps', [
          ['1. Do the task', 'Tick it off. It does not have to be perfect.'],
          ['2. Write a line', 'What happened, how it felt.'],
          ['3. Review each week', 'Notice what is getting easier.'],
        ]],
        ['tip', 'If you miss a day', 'Carry on from where you are. Do not start over.'],
        ['p', 'This workbook is not therapy. If anxiety or low mood makes daily life hard, speak to a doctor or therapist. In the US, call or text 988 if you feel hopeless.'],
      ],
    },
    {
      kicker: 'DAY 0', title: 'Where I am today',
      blocks: [
        ['lbl', 'MY CONFIDENCE TODAY (1-10)'], ['lines', 1],
        ['lbl', 'MY BIGGEST FEAR ABOUT DATING'], ['lines', 3],
        ['lbl', 'ONE THING I WANT AFTER 30 DAYS'], ['lines', 3],
        ['lbl', 'WHO CAN SUPPORT ME'], ['lines', 2],
      ],
    },
    week('WEEK 1', 'Warm up: talk to people', [
      'Day 1: Smile and say hello to three people.',
      'Day 2: Ask one open question to someone (barista, colleague).',
      'Day 3: Learn one new person\'s name and one detail about them.',
      'Day 4: Give one sincere, non-romantic compliment.',
      'Day 5: Start a short chat in a queue.',
      'Day 6: Call or message an old friend.',
      'Day 7: Review the week.',
    ]),
    week('WEEK 2', 'Conversation skills', [
      'Day 8: Echo a word someone says and ask about it.',
      'Day 9: Use the 1:1 rule (share before you ask).',
      'Day 10: Ask one "what did you enjoy about it?" question.',
      'Day 11: Pause two seconds before answering.',
      'Day 12: Tell a 60-second story.',
      'Day 13: Say your Present, Past, Passion answer out loud.',
      'Day 14: Review the week.',
    ]),
    week('WEEK 3', 'Real dating steps', [
      'Day 15: Take or choose three clear, recent photos.',
      'Day 16: Write or refresh your bio.',
      'Day 17: Send one thoughtful first message.',
      'Day 18: Reply to a message with a follow-up question.',
      'Day 19: Suggest a coffee (day and place) or invite a friend to an event.',
      'Day 20: Write two lines you could use to say no kindly.',
      'Day 21: Review the week.',
    ]),
    week('WEEK 4', 'Dates, rejection and resilience', [
      'Day 22: Go on a coffee or walk (date or friend practice).',
      'Day 23: Fill in the debrief page.',
      'Day 24: Practice receiving a "no" kindly.',
      'Day 25: Write a self-compassion note to yourself.',
      'Day 26: Go to one social event or class alone.',
      'Day 27: Re-read the scam checklist.',
      'Day 28: Review the week.',
    ]),
    {
      kicker: 'DAY 29-30', title: 'Look back and plan ahead',
      blocks: [
        ['chk', ['Day 29: Re-read your notes and list your wins.', 'Day 30: Write what changed and set your next goal.']],
        ['lbl', 'MY WINS'], ['lines', 4],
        ['lbl', 'MY CONFIDENCE NOW (1-10)'], ['lines', 1],
        ['lbl', 'MY NEXT 30-DAY GOAL'], ['lines', 3],
      ],
    },
    {
      kicker: 'TOOL', title: 'My exposure ladder',
      blocks: [
        ['p', 'List steps from easiest to hardest. Move up one rung at a time.'],
        ['lbl', 'EASIEST'], ['lines', 2],
        ['lbl', 'MIDDLE'], ['lines', 3],
        ['lbl', 'HARDEST'], ['lines', 2],
      ],
    },
    {
      kicker: 'TOOL', title: 'Changing a worrying thought',
      blocks: [
        ['steps', [
          ['1. The thought', 'Write it down. For example: "Nobody will want to date a man my age."'],
          ['2. Evidence for', 'What facts support it?'],
          ['3. Evidence against', 'What facts do not?'],
          ['4. A balanced thought', 'A fair version you believe.'],
        ]],
        ['lbl', 'THE THOUGHT'], ['lines', 2],
        ['lbl', 'EVIDENCE FOR'], ['lines', 2],
        ['lbl', 'EVIDENCE AGAINST'], ['lines', 2],
        ['lbl', 'A BALANCED THOUGHT'], ['lines', 2],
      ],
    },
    {
      kicker: 'TOOL', title: 'Date debrief',
      blocks: [
        ['lbl', 'WHAT WENT WELL'], ['lines', 3],
        ['lbl', 'WHAT FELT AWKWARD'], ['lines', 3],
        ['lbl', 'ONE THING TO TRY NEXT TIME'], ['lines', 2],
        ['chk', ['I shared as much as I asked.', 'I followed up on something she said.', 'I stayed calm in the quiet moments.', 'I kept my phone away.', 'I ended on a high.']],
      ],
    },
    {
      kicker: 'TOOL', title: 'Rejection log',
      blocks: [
        ['p', 'Write what happened, what you felt, and one thing you learned. Then close the page.'],
        ['lbl', 'WHAT HAPPENED'], ['lines', 3],
        ['lbl', 'WHAT I FELT'], ['lines', 2],
        ['lbl', 'WHAT I LEARNED'], ['lines', 2],
        ['lbl', 'WHAT I WILL DO NEXT'], ['lines', 2],
      ],
    },
  ],
};

// ============ 5. SCAM-PROOF DATING GUIDE ============
const scamGuide = {
  id: 'wolfe-scam-proof-dating-guide', kind: 'GUIDE FOR 50+',
  titleLines: ['SCAM-PROOF', 'DATING', 'GUIDE'],
  sub: 'How romance scams work, how to check a profile, what to say, and what to do if you have been caught.',
  chapters: [
    {
      kicker: 'INTRODUCTION', title: 'Why this matters',
      blocks: [
        ['p', 'Online dating can be a good way to meet people. It is also where criminals look for lonely, trusting people. Anyone can be fooled. Scammers are professionals, and they are good at it.'],
        ['steps', [
          ['The size of the problem', 'The FTC reported that people aged 60 and over lost about $2.4 billion to fraud in 2024. That covers all fraud types, and romance scams are one part of it.'],
          ['Who is targeted', 'Men and women. A 2023 Pew report found that men and women aged 50+ were about equally likely to meet scams on dating sites.'],
          ['The goal of this guide', 'Help you enjoy online dating while staying safe.'],
        ]],
        ['tip', 'Not your fault', 'If you have been scammed, you are not stupid. Shame is what scammers rely on. Read chapter 8.'],
        ['p', 'This guide focuses on the US. In other countries, use your local police and consumer protection agency.'],
      ],
    },
    {
      kicker: 'CHAPTER 1', title: 'How a romance scam works',
      blocks: [
        ['steps', [
          ['1. Contact', 'A friendly message from an attractive profile.'],
          ['2. Fast bond', 'Lots of attention. "I have never felt this way." Messages morning and night.'],
          ['3. Move off the app', 'They ask you to switch to WhatsApp, Telegram or text, away from the app\'s protections.'],
          ['4. A story', 'They are overseas, in the military, a widower, a business owner, a doctor.'],
          ['5. The problem', 'A sudden emergency, a fee, a ticket, a business problem.'],
          ['6. The ask', 'Money, gift cards, crypto or a wire transfer. Or an "investment" opportunity.'],
          ['7. More asks', 'Once you pay, the requests continue. They may disappear, or threaten.'],
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 2', title: '12 red flags',
      blocks: [
        ['chk', [
          'Perfect photos, or photos found elsewhere online.',
          'Wants to leave the dating app very quickly.',
          'Says "I love you" within days or weeks.',
          'Will not video call, or the camera "never works".',
          'Lives or works abroad, or is away on a ship, base or project.',
          'Story has gaps, or changes.',
          'Asks questions about your money, home or retirement.',
          'A sudden emergency needing money.',
          'Asks for gift cards, crypto or wire transfers.',
          'Pressures you to hurry or keep it secret.',
          'Suggests an investment or trading platform.',
          'Gets angry or sad when you hesitate.',
        ]],
        ['tip', 'The rule', 'One flag: slow down. Two or more: stop and talk to someone you trust.'],
      ],
    },
    {
      kicker: 'CHAPTER 3', title: 'How to check a profile',
      blocks: [
        ['steps', [
          ['Reverse image search', 'Upload their photos to Google Lens or TinEye. If they appear under other names, it is a fake.'],
          ['Search the name and details', 'Search their name, job, and phone number with the word "scam".'],
          ['Check consistency', 'Do the age, job, location and story fit together?'],
          ['Ask for a live video call', 'A real person will agree. Scammers make excuses.'],
          ['Ask simple questions', 'About their town or workplace. Notice vague or copied answers.'],
        ]],
        ['tip', 'Remember', 'AI can fake photos and voices. A live video call helps but is not foolproof. Judge the whole pattern.'],
      ],
    },
    {
      kicker: 'CHAPTER 4', title: 'Money rules',
      blocks: [
        ['dont', [
          'Never send money, gift cards, crypto or wire transfers to someone you have met online.',
          'Never share your bank details, card numbers, ID or one-time passcodes.',
          'Never "invest" with someone you met online.',
          'Never receive money or packages and forward them for someone. This can be used for money laundering.',
          'Never click links they send, or install apps they suggest.',
        ]],
        ['tip', 'Simple test', 'If a person you have never met in person asks for money, the answer is no. There are no exceptions.'],
      ],
    },
    {
      kicker: 'CHAPTER 5', title: 'Investment and crypto scams',
      blocks: [
        ['p', 'The FTC\'s data for older adults names **investment scams** as the category with the largest losses. In a typical version, a person you met online mentions a profitable trading app, shows fake gains, and encourages you to put in more.'],
        ['ul', ['Be suspicious of any "guaranteed" or very high returns.', 'Be suspicious if the person you met online suggests the platform.', 'Check any firm with your country\'s financial regulator before investing.', 'Talk to an independent adviser or trusted friend first.']],
      ],
    },
    {
      kicker: 'CHAPTER 6', title: 'What to say',
      blocks: [
        ['lbl', 'WHEN THEY ASK FOR MONEY'],
        ['msg', 'I do not discuss money with someone I have not met.', ''],
        ['lbl', 'WHEN THEY REFUSE A VIDEO CALL'],
        ['msg', 'I would like to video call this week. If that is not possible, I will step back.', ''],
        ['lbl', 'WHEN THEY PRESS YOU TO MOVE APPS'],
        ['msg', 'I am happy to keep chatting here for now.', ''],
        ['lbl', 'WHEN YOU WANT TO END IT'],
        ['msg', 'I am going to stop here. Take care.', ''],
        ['tip', 'You do not owe an explanation', 'You can stop replying and block them.'],
      ],
    },
    {
      kicker: 'CHAPTER 7', title: 'Meeting in person safely',
      blocks: [
        ['chk', [
          'Video call first.',
          'Meet in a public place.',
          'Tell a friend who, where and when.',
          'Use your own transport.',
          'Keep your phone charged.',
          'Do not share your address or workplace early.',
          'Trust your instincts. Leave if something feels wrong.',
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 8', title: 'If you have sent money',
      blocks: [
        ['steps', [
          ['1. Stop contact', 'Do not send more. Do not tell them you know.'],
          ['2. Call your bank or card provider now', 'Ask whether the payment can be stopped or reversed.'],
          ['3. Keep evidence', 'Messages, usernames, account numbers, receipts.'],
          ['4. Report', 'US: reportfraud.ftc.gov and ic3.gov. UK: Action Fraud / Report Fraud. Canada: Canadian Anti-Fraud Centre. Australia: Scamwatch.'],
          ['5. Beware "recovery" scams', 'Anyone who contacts you offering to get your money back for a fee is probably another scammer.'],
          ['6. Tell someone', 'A friend, family member or helpline. You are not alone.'],
          ['7. Look after yourself', 'Shame and anger are normal. Talk to someone. If you feel hopeless, call or text 988 in the US.'],
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 9', title: 'Protect your accounts',
      blocks: [
        ['ul', [
          'Use a different strong password for each account.',
          'Turn on two-factor authentication.',
          'Never share one-time codes.',
          'Do not click links from people you have not met.',
          'Keep your social media private, and limit what strangers can see.',
          'Review your bank and card statements regularly.',
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 10', title: 'Talk to someone',
      blocks: [
        ['p', 'Scammers try to isolate you: "Don\'t tell your family, they won\'t understand." That is a red flag in itself. Show your messages to a friend you trust, or ask someone to be your "second pair of eyes".'],
        ['tip', 'Try this', 'Pick one person you would tell. Tell them you are dating online and ask them to check in.'],
        help,
        note,
      ],
    },
  ],
};

// ============ 6. 80 CONVERSATION STARTERS (cards) ============
const C = (arr, tag) => arr.map(t => [tag, t]);
const easy = [
  'What was the best part of your week so far?', "What's your go-to coffee or tea order?", 'Do you have a favourite place in this town?', "What's the best meal you've had recently?",
  'Are you a morning or evening person?', "What's something you're looking forward to this month?", 'What was the last show or film you really enjoyed?', 'What do you like to do on a free Saturday?',
  "What's your favourite season, and why?", 'Dogs, cats or neither?', "What's the best trip you've taken?", 'What music do you listen to when you cook or drive?',
  "What's a small thing that makes your day better?", "What's your favourite local spot to take visitors?", 'Do you prefer cooking at home or eating out?', "What's a skill you'd love to learn?",
  'What was your first job?', "What's the best advice you've ever received?", 'Are you a planner or a go-with-the-flow person?', "What's on your bucket list?",
];
const warm = [
  'What do you enjoy most about your work?', 'What was your favourite thing about growing up where you did?', 'Who has influenced you most?', 'What do you do to recharge?',
  "What are you proud of that people don't often ask about?", 'What kind of people do you feel most yourself around?', "What's a tradition you love?", 'What do you value most in a friendship?',
  "What's a hobby you'd do all day if you could?", 'What made you smile today?', "What's something you're grateful for this week?", 'What do you look forward to on weekends?',
  "What's a recent small win?", 'How do you like to celebrate good news?', "What's a happy memory that comes to mind?", 'What do you wish you had more time for?',
  'What was a turning point that changed your direction?', "What are you curious about at the moment?", "What's the kindest thing someone did for you recently?", "What's a place that makes you feel at peace?",
];
const playful = [
  "What's your most useless talent?", 'What would the title of your autobiography be?', 'If you could have dinner with anyone, who and why?', "What's the strangest food you've eaten and would eat again?",
  'Which fictional world would you live in?', "What's your guilty-pleasure show or song?", 'What would you do with a free month off?', "What's the funniest thing that happened to you this year?",
  'Pineapple on pizza: crime or genius?', "What's a harmless opinion you'll defend to the end?", 'Which decade would you time-travel to?', "What's the most spontaneous thing you've done?",
  "What's a hidden talent that would surprise people?", 'If you had a theme song, what would it be?', "What's the best gift you've given or received?", 'What movie can you quote by heart?',
  'What would you do if you won a small lottery?', "What's your go-to karaoke song?", "What's your most irrational fear?", 'What do you do when no one is watching?',
];
const deeper = [
  "What's something you used to believe that you don't anymore?", 'What do you wish people understood about you?', 'When do you feel most alive?', "What's a risk you took that changed things?",
  'What are you still figuring out?', 'What does a good relationship look like to you?', 'What did your family teach you that you still use?', "What's a moment that shaped who you are?",
  'What do you value more as you get older?', 'What does "home" mean to you?', 'What are you looking for in the next chapter of your life?', 'What would you tell your younger self?',
  "What's something hard that you're glad you went through?", 'How do you like to be supported when things are tough?', 'What makes you feel appreciated?', "What's a fear you've overcome?",
  'What do you want your days to look like in five years?', 'What kind of partnership would feel right to you?', 'What are you most hopeful about?', "What's something you'd like to be remembered for?",
];
const cardsProduct = {
  id: 'wolfe-80-conversation-starters', kind: 'PRINTABLE CARDS',
  titleLines: ['80', 'CONVERSATION', 'STARTERS'],
  sub: 'Easy, warm, playful and deeper questions for dates and new connections. Print, cut or just read.',
  chapters: [
    {
      kicker: 'HOW TO USE', title: 'Use them like a person, not a list',
      blocks: [
        ['steps', [
          ['Pick, don\'t read', 'Choose a card that fits the moment. Skip any that do not.'],
          ['Share back', 'After she answers, share your own answer. This stops it feeling like an interview.'],
          ['Follow up', 'The best question is the follow-up: "What was the best part?" "Why that one?"'],
          ['Read the room', 'Start with Easy, move to Warm, then Playful or Deeper if it feels right.'],
          ['Go slowly with Deeper', 'These work after you have built some comfort. Never push.'],
        ]],
        ['lbl', '8 FOLLOW-UPS THAT ALWAYS WORK'],
        ['ul', ['"What was the best part?"', '"How did that feel?"', '"Tell me more."', '"What made you choose that?"', '"What happened next?"', '"Is that a thing you still do?"', '"What did you learn from it?"', '"That sounds like a story. I have time."']],
        ['tip', 'Printing', 'Print on stiff paper and cut along the dotted lines, or just keep the PDF on your phone.'],
      ],
    },
    { kicker: 'EASY (1-20)', title: 'Easy: for first messages and first dates', noTitle: true, blocks: [['cards', C(easy.slice(0, 8), 'EASY')]] },
    { kicker: 'EASY', title: 'Easy, continued', noTitle: true, blocks: [['cards', C(easy.slice(8, 16), 'EASY')]] },
    { kicker: 'EASY', title: 'Easy, last cards', noTitle: true, blocks: [['cards', C(easy.slice(16), 'EASY')]] },
    { kicker: 'WARM (21-40)', title: 'Warm: getting to know someone', noTitle: true, blocks: [['cards', C(warm.slice(0, 8), 'WARM')]] },
    { kicker: 'WARM', title: 'Warm, continued', noTitle: true, blocks: [['cards', C(warm.slice(8, 16), 'WARM')]] },
    { kicker: 'WARM', title: 'Warm, last cards', noTitle: true, blocks: [['cards', C(warm.slice(16), 'WARM')]] },
    { kicker: 'PLAYFUL (41-60)', title: 'Playful: add some fun', noTitle: true, blocks: [['cards', C(playful.slice(0, 8), 'PLAYFUL')]] },
    { kicker: 'PLAYFUL', title: 'Playful, continued', noTitle: true, blocks: [['cards', C(playful.slice(8, 16), 'PLAYFUL')]] },
    { kicker: 'PLAYFUL', title: 'Playful, last cards', noTitle: true, blocks: [['cards', C(playful.slice(16), 'PLAYFUL')]] },
    { kicker: 'DEEPER (61-80)', title: 'Deeper: use sparingly', blocks: [['tip', 'Before you ask', 'Share your own answer too. Deeper questions work best as a trade, not an interrogation. Skip them on a first message.'], ['cards', C(deeper.slice(0, 6), 'DEEPER')]] },
    { kicker: 'DEEPER', title: 'Deeper, continued', noTitle: true, blocks: [['cards', C(deeper.slice(6, 14), 'DEEPER')]] },
    { kicker: 'DEEPER', title: 'Deeper, last cards', noTitle: true, blocks: [['cards', C(deeper.slice(14), 'DEEPER')]] },
  ],
};

// ============ 7. REJECTION & RESILIENCE MINI GUIDE ============
const rejection = {
  id: 'wolfe-rejection-resilience-guide', kind: 'MINI GUIDE',
  titleLines: ['REJECTION', '&', 'RESILIENCE'],
  sub: 'How to take a "no" or silence without losing your confidence, and keep going.',
  chapters: [
    {
      kicker: 'INTRODUCTION', title: 'What rejection is, and is not',
      blocks: [
        ['p', 'Rejection hurts. It is part of dating for everyone, whatever their age or looks. How you respond shapes your confidence far more than the rejection itself.'],
        ['steps', [
          ['It is information about fit', 'It says what she wants right now. It does not say what you are worth.'],
          ['You usually cannot know why', 'Timing, chemistry, her own situation. Do not invent a reason.'],
          ['People like you more than you think', 'Research on the "liking gap" finds people underestimate how much others liked them after a conversation.'],
        ]],
      ],
    },
    {
      kicker: 'CHAPTER 1', title: 'The first 24 hours',
      blocks: [
        ['steps', [
          ['1. Pause', 'Do not reply in anger or send long messages.'],
          ['2. Name the feeling', '"I feel disappointed." Naming it lowers its grip.'],
          ['3. Move', 'A walk, gym, a run. Movement helps.'],
          ['4. Talk to someone', 'A friend. Not to fix it, just to say it.'],
          ['5. Write it down', 'What happened, what you felt, what you can learn.'],
          ['6. Do something you enjoy', 'Cook, call a friend, watch something good.'],
        ]],
        ['tip', 'Do not', 'Do not send insults, repeated messages or ask "why" again and again. It does not help you, and it can cross into harassment.'],
      ],
    },
    {
      kicker: 'CHAPTER 2', title: 'Reframe the thought',
      blocks: [
        ['steps', [
          ['"I am not good enough."', '"We were not a match. That is all this tells me."'],
          ['"I am too old."', '"Some people will not be interested. Others will."'],
          ['"I will never find anyone."', '"I have had one no. One no does not predict the future."'],
          ['"I should give up."', '"I can take a break, then try again with what I learned."'],
        ]],
        ['tip', 'Try this', 'Write your own harsh thought on a page. Next to it, write what you would say to a friend in the same position.'],
      ],
    },
    {
      kicker: 'CHAPTER 3', title: 'Graceful replies',
      blocks: [
        ['msg', 'Thanks for telling me. I appreciate the honesty. Take care.', ''],
        ['msg', 'No hard feelings at all. It was good to meet you.', ''],
        ['msg', 'All good, I enjoyed chatting. Best of luck.', ''],
        ['p', 'A kind exit builds respect, even from someone who said no.'],
      ],
    },
    {
      kicker: 'CHAPTER 4', title: 'When she goes quiet (ghosting)',
      blocks: [
        ['steps', [
          ['Wait two days', 'Do not send follow-ups.'],
          ['Send one light message', '"Hey, hope your week is going well. Still up for that coffee?"'],
          ['Then let it go', 'Silence is an answer. You can stay kind and move on.'],
        ]],
        ['p', 'For more, see the "She Went Quiet" guide.'],
      ],
    },
    {
      kicker: 'CHAPTER 5', title: 'When it keeps happening',
      blocks: [
        ['p', 'A run of no\'s is discouraging. Look at it calmly:'],
        ['chk', [
          'Are my photos clear, recent and smiling?',
          'Are my messages specific and easy to answer?',
          'Am I contacting people who match what I want?',
          'Am I moving to a coffee after a few good messages?',
          'Do I need a break to recharge?',
        ]],
        ['p', 'Change one thing at a time. Ask a trusted friend to look at your profile.'],
      ],
    },
    {
      kicker: 'CHAPTER 6', title: 'A self-compassion exercise',
      blocks: [
        ['steps', [
          ['1. Notice', '"This is a painful moment."'],
          ['2. Remember others', '"Rejection happens to everyone. I am not alone."'],
          ['3. Be kind', '"May I be kind to myself. What do I need right now?"'],
        ]],
        ['p', 'Research suggests self-compassion helps people recover from setbacks better than harsh self-criticism does.'],
      ],
    },
    {
      kicker: 'WORKSHEET', title: 'My rejection log',
      blocks: [
        ['lbl', 'WHAT HAPPENED'], ['lines', 3],
        ['lbl', 'WHAT I FELT'], ['lines', 2],
        ['lbl', 'WHAT I TELL MYSELF'], ['lines', 2],
        ['lbl', 'WHAT I WOULD SAY TO A FRIEND'], ['lines', 2],
        ['lbl', 'ONE THING I WILL DO NEXT'], ['lines', 2],
      ],
    },
    {
      kicker: 'HELP', title: 'When to get support',
      blocks: [
        ['p', 'If rejection leaves you feeling hopeless, avoiding people for weeks, or thinking of harming yourself, please reach out.'],
        help,
        ['p', 'A therapist, especially one who uses CBT, can help with confidence and low mood.'],
        note,
      ],
    },
  ],
};

module.exports = { NAME, BRAND, products: [scamChecklist, starter, workbook, scamGuide, cardsProduct, rejection] };
