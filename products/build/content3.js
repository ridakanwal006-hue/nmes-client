// Product 3: Profile Fixer for 40+ (bald-friendly)
const NAME = 'Dorian Wolfe';
const BRAND = 'WOLFE';
const note = ['tip', 'A note on evidence', "This guide uses general dating-profile advice and common sense. There is little research on profiles for men over 40, and none that I found on how baldness changes match rates, so treat everything here as practical guidance, not a guarantee. It is not therapy, medical advice or a promise of results."];

const profile = {
  id: 'wolfe-profile-fixer-40-plus', kind: 'WORKBOOK + SWIPE FILE',
  titleLines: ['PROFILE', 'FIXER', 'FOR 40+'],
  sub: 'Better photos, a clearer bio, and a profile that sounds like you. Bald-friendly and honest.',
  chapters: [
    {
      kicker: 'INTRODUCTION', title: 'What your profile is for',
      blocks: [
        ['p', 'A profile has one job: to give a stranger a real, friendly reason to message you. It does not have to be perfect, and it does not have to impress everyone.'],
        ['steps', [
          ['Be recent', 'Photos from the last year or two.'],
          ['Be specific', 'Details beat adjectives. "Weekend hiker" says more than "adventurous".'],
          ['Be honest', 'Age, height, looks. Lies come out on the first date.'],
          ['Be easy to message', 'End with a question that is simple to answer.'],
        ]],
        ['p', 'In a 2023 Pew survey of online daters (all ages), 64% of men said they felt insecure about getting too few messages. You are not alone, and a clearer profile is one thing you control.'],
        note,
      ],
    },
    {
      kicker: 'STEP 1', title: 'Your photo plan',
      blocks: [
        ['p', 'Aim for 4 to 6 photos that show different sides of you.'],
        ['chk', [
          'A clear, smiling headshot (main photo).',
          'A full-body photo, so nobody is surprised.',
          'You doing something you enjoy (hiking, cooking, music, a hobby).',
          'You with friends or at an event (only if you are easy to spot).',
          'A relaxed, candid smile.',
          'Optional: a pet, travel or a place that matters to you.',
        ]],
        ['lbl', 'LEAVE OUT'],
        ['dont', ['Old photos, or heavy filters.', 'Sunglasses or a hat in every photo.', 'Group shots where it is hard to tell which one is you.', 'Mirror selfies, shirtless photos, car selfies.', 'Photos with an ex, even cropped.']],
      ],
    },
    {
      kicker: 'STEP 2', title: 'Light, angle and a clean look',
      blocks: [
        ['steps', [
          ['Soft light', 'Face a window or stand in open shade. Avoid harsh overhead light.'],
          ['Eye level', 'Have someone hold the camera at eye level, not from below.'],
          ['Smile with your eyes', 'Think of something that makes you laugh.'],
          ['Simple background', 'Tidy and uncluttered.'],
          ['Groomed', 'Tidy head and beard, clean clothes that fit.'],
          ['Shine', 'A shaved head can reflect light. Blot with a tissue or use a matte moisturiser before photos.'],
        ]],
        ['tip', 'Try this', 'Ask a friend to take 20 photos in soft light. Pick the best 3.'],
      ],
    },
    {
      kicker: 'FOR BALD MEN', title: 'Own it, do not hide it',
      blocks: [
        ['p', 'Studies on how people see bald men are mixed, and I found no real-world data on match rates by hair status. What is practical:'],
        ['steps', [
          ['Show your head', 'In the main photo, no hat. Hiding in every picture can read as insecurity.'],
          ['Look deliberate', 'A clean shave or tidy short cut looks intentional. A neat beard can frame the face.'],
          ['Do not apologise', 'Skip "yes, I am bald" in your bio. A light, confident line is fine, but it should not be the headline.'],
          ['Let personality lead', 'Warmth, humour and interests give her something to respond to.'],
        ]],
        ['lbl', 'ILLUSTRATIVE LINES (OPTIONAL, ADAPT TO YOU)'],
        ['msg', 'Easy to spot in a crowd. Great at finding the best coffee in any town.', ''],
        ['msg', 'Zero hair, plenty of opinions about breakfast.', ''],
      ],
    },
    {
      kicker: 'STEP 3', title: 'The bio formula',
      blocks: [
        ['p', 'Two to four short sentences. Use this order:'],
        ['steps', [
          ['1. Who you are', 'One line: what you do or how you spend your time.'],
          ['2. What you enjoy', 'Two or three specific things.'],
          ['3. What you are looking for', 'Honest and positive.'],
          ['4. An easy question', 'Something she can answer in a line.'],
        ]],
        ['lbl', 'ILLUSTRATIVE EXAMPLE'],
        ['msg', 'Weekend hiker, terrible cook, decent listener. I enjoy live music, long walks and finding the best coffee in town. Looking for someone to laugh with and explore new places. Tell me the best meal you have had this year.', ''],
        ['dont', ['Negativity: "no drama", "no games", long lists of dislikes.', 'Complaining about exes.', 'Lying about age or height.', 'Copying someone else\'s bio.']],
      ],
    },
    {
      kicker: 'SWIPE FILE', title: '10 bio templates to adapt',
      blocks: [
        ['p', 'Fill in the blanks with your own details. Change the wording until it sounds like you. (Illustrative, not sourced.)'],
        ['qs', [
          '[Job or interest] by day, [hobby] by weekend. Looking for someone to [activity] with. Best [food/place] you have found lately?',
          'I [enjoy 1], [enjoy 2] and [enjoy 3]. Recently single and happy to take things slowly. What is your favourite way to spend a Sunday?',
          'Widower, dad, [hobby] fan. I would like someone kind to share good conversation and good coffee. What are you looking forward to this month?',
          'Never married, still curious. [Hobby], [hobby], and a decent cook. Tell me your signature dish.',
          'Retired [job]. Now I [new interest]. Looking for company on walks and travels. Where would you go next?',
          'Divorced, grateful, and ready to meet someone real. I love [interest]. Ask me about [funny story].',
          'Quiet guy with a loud laugh. [Interest], [interest]. What makes you laugh?',
          'Fitness, [hobby], and bad puns. Hoping to meet someone warm and honest. Best pun you know?',
          'Looking for a friend first, and a partner if it clicks. I enjoy [interest]. What is your go-to comfort food?',
          'Dad of [number], proud of them. Outdoors, music and cooking. What is something you are proud of?',
        ]],
      ],
    },
    {
      kicker: 'SWIPE FILE', title: 'Prompt answers to adapt',
      blocks: [
        ['p', 'Many apps ask for short answers to prompts. Specific and warm beats clever. (Illustrative, not sourced.)'],
        ['steps', [
          ['A perfect weekend', '"A long walk, a good coffee, and no alarm. Add a live band and it is perfect."'],
          ['I am looking for', '"Someone kind who enjoys a good conversation."'],
          ['Two truths and a lie', '"I have run a marathon. I can cook. I have never been to Paris. Guess."'],
          ['The way to win me over', '"Make me laugh and tell me about your favourite place."'],
          ['A fact about me', '"I know the lyrics to every song from 1985."'],
          ['Together we could', '"Find the best breakfast spot in the city."'],
        ]],
        ['tip', 'Rule', 'Every answer should give someone something to reply to.'],
      ],
    },
    {
      kicker: 'STEP 4', title: 'Safety on your profile',
      blocks: [
        ['chk', [
          'No home address, workplace or phone number.',
          'No financial details, ever.',
          'Use first name or a nickname only.',
          'Check that your social media is private or limited.',
          'Be wary of anyone who rushes you to another app or asks for money.',
        ]],
        ['tip', 'Learn more', 'See the free Scam Red-Flag Checklist and the Scam-Proof Dating Guide for 50+.'],
      ],
    },
    {
      kicker: 'WORKSHEET', title: 'Photo audit',
      blocks: [
        ['chk', ['My main photo is clear and smiling.', 'It was taken in the last two years.', 'I show my head and face, no hat or sunglasses.', 'I have a full-body photo.', 'I have a photo doing something I enjoy.', 'Nobody else is hard to tell apart from me.', 'The light is soft.']],
        ['lbl', 'MY BEST 3 PHOTOS ARE'], ['lines', 3],
        ['lbl', 'WHAT I WANT TO CHANGE'], ['lines', 3],
      ],
    },
    {
      kicker: 'WORKSHEET', title: 'Rewrite your bio',
      blocks: [
        ['lbl', 'MY CURRENT BIO'], ['lines', 4],
        ['lbl', 'WHO I AM / WHAT I ENJOY / WHAT I WANT'], ['lines', 4],
        ['lbl', 'MY NEW BIO'], ['lines', 5],
      ],
    },
    {
      kicker: 'WORKSHEET', title: 'Ask a friend for feedback',
      blocks: [
        ['p', 'A trusted friend can see what you cannot. Send them your profile and ask:'],
        ['msg', 'Would you message this man? What would make you more likely to? Be honest, I can take it.', ''],
        ['lbl', 'WHAT MY FRIEND SAID'], ['lines', 4],
        ['lbl', 'WHAT I WILL CHANGE'], ['lines', 3],
      ],
    },
    {
      kicker: 'THE PLAN', title: '7-day profile tune-up',
      blocks: [
        ['chk', [
          'Day 1: Choose or take new photos.',
          'Day 2: Pick your best 4 to 6.',
          'Day 3: Write your bio using the formula.',
          'Day 4: Add two prompt answers.',
          'Day 5: Ask a friend for feedback.',
          'Day 6: Make changes and go live.',
          'Day 7: Send two thoughtful first messages.',
        ]],
        ['tip', 'Then', 'Keep it simple. Do not rewrite it every day. Give it two weeks, then review.'],
        ['p', 'Need conversation help? See the Conversation Playbook and the 80 Conversation Starters.'],
      ],
    },
  ],
};

module.exports = { NAME, BRAND, products: [profile] };
