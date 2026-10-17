// "Start Here" welcome guide delivered with every purchase.
const NAME = 'Dorian Wolfe';
const BRAND = 'WOLFE';
const help = ['tip', 'If it feels heavier than nerves', 'If you feel hopeless, or think about harming yourself, please talk to someone now. In the US, call or text 988. In the UK, Samaritans: 116 123. Elsewhere, findahelpline.com lists local services.'];

const start = {
  id: 'wolfe-start-here', kind: 'WELCOME GUIDE',
  titleLines: ['START', 'HERE', 'GUIDE'],
  sub: 'Welcome. How to use your Wolfe guides, which one to open first, and what to expect.',
  chapters: [
    {
      kicker: 'WELCOME', title: 'Thank you, and welcome',
      blocks: [
        ['p', 'Thank you for buying. These guides are built for men over 40 who are dating again, or dating for the first time in a long time. They are practical, calm and honest.'],
        ['steps', [
          ['Who writes these', 'Dorian Wolfe is an AI-generated character, not a real person, and has no personal life story. The advice comes from general relationship and social-skills research and common sense.'],
          ['What you will find', 'Step-by-step guides, worksheets, checklists and question cards. No tricks and no promises of results.'],
          ['What you will not find', 'Pickup lines that "make her chase you", medical advice, legal advice, or guarantees.'],
        ]],
        ['tip', 'How to use these guides', 'Read one chapter at a time. Do the small action at the end. Practice beats reading. Go at your own pace.'],
      ],
    },
    {
      kicker: 'PICK YOUR PATH', title: 'Which guide first?',
      blocks: [
        ['p', 'Start where you are.'],
        ['steps', [
          ['I am just starting again', 'Dating Again After 40: Starter Guide, then the 30-Day Confidence Challenge.'],
          ['I do not know what to say', 'Conversation Playbook and the 80 Conversation Starters.'],
          ['My profile is not getting messages', 'Profile Fixer for 40+.'],
          ['I am worried about scams', 'Scam Red-Flag Checklist (free), then the Scam-Proof Dating Guide.'],
          ['A date went quiet or said no', 'Rejection & Resilience, and She Went Quiet.'],
          ['I have a first date coming up', 'First Date Blueprint and the 80 Conversation Starters.'],
        ]],
      ],
    },
    {
      kicker: 'YOUR FIRST 7 DAYS', title: 'A simple plan',
      blocks: [
        ['chk', [
          'Day 1: Read the Starter Guide introduction and chapter 1.',
          'Day 2: Message one friend and make a plan.',
          'Day 3: Write your 30-second story.',
          'Day 4: Choose your best photos.',
          'Day 5: Write or refresh your bio.',
          'Day 6: Read the Scam Red-Flag Checklist.',
          'Day 7: Review the week. What felt easier?',
        ]],
        ['tip', 'Remember', 'You do not need to do everything. One small step each day is enough.'],
      ],
    },
    {
      kicker: 'TERMS', title: 'How you can use these guides',
      blocks: [
        ['ul', [
          'Personal use: you may read and print them for yourself.',
          'Please do not share, resell, copy or upload them elsewhere.',
          'No guarantee: results depend on you and on other people. Nothing here promises a partner, a date or any outcome.',
          'Not professional advice: these guides are not therapy, medical advice, legal advice or financial advice.',
          'Be kind: respect other people\'s boundaries and consent at all times.',
        ]],
        ['p', 'The seller sets the final terms on the store page. If they differ from this page, the store page applies.'],
      ],
    },
    {
      kicker: 'REFUNDS AND SUPPORT', title: 'If something is not right',
      blocks: [
        ['steps', [
          ['Refunds', 'If a guide is not useful to you, reply to your receipt email within 7 days and ask for a refund. [Seller: confirm this period matches your store settings.]'],
          ['Support', 'Questions or problems? Write to [your support email].'],
          ['Feedback', 'Tell us what helped and what did not. We will improve the guides.'],
        ]],
      ],
    },
    {
      kicker: 'SAFETY', title: 'Stay safe, and get help',
      blocks: [
        ['ul', [
          'Scams: reportfraud.ftc.gov and ic3.gov (US). Action Fraud / Report Fraud (UK).',
          'Domestic abuse: US National Domestic Violence Hotline 1-800-799-7233.',
          'Meeting someone new: video call first, meet in public, tell a friend.',
          'Therapy: ask your doctor, or look for a licensed therapist who uses CBT.',
        ]],
        help,
        ['tip', 'A note on evidence', 'Studies of men over 40 are limited. Treat everything in these guides as practical guidance, not a guarantee. If you are struggling, a professional can help in ways a guide cannot.'],
      ],
    },
  ],
};
module.exports = { NAME, BRAND, products: [start] };
