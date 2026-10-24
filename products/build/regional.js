// US / Canada / UK regional chapters. Contact details come from research/regional-resources-us-ca-uk.md
// (seen in search results on 2026-10-13, not opened on the official sites). Readers are told to check before relying on them.
const check = ['tip', 'Check first', 'Numbers and hours change. If one fails, search the service\'s official website.'];

const crisis = ['steps', [
  ['USA', '**988 Suicide & Crisis Lifeline.** Call or text 988, or chat at 988lifeline.org/chat. Free, 24/7. Emergency: 911.'],
  ['Canada', '**9-8-8 Suicide Crisis Helpline.** Call or text 988, 24/7, in English and French. Info: 988.ca. Emergency: 911.'],
  ['UK', '**Samaritans:** 116 123 (free, 24/7). **Shout:** text SHOUT to 85258. **NHS 111** for urgent mental-health help (choose the mental-health option). Emergency: 999.'],
]];

const fraud = ['steps', [
  ['USA', 'Report to the FTC at **reportfraud.ftc.gov** and to the FBI Internet Crime Complaint Center at **ic3.gov**. If you sent money, tell your bank or card company straight away.'],
  ['Canada', 'Report to the **Canadian Anti-Fraud Centre: 1-888-495-8501**, or online at antifraudcentre-centreantifraude.ca. If you lost money, also contact your local police and your bank.'],
  ['UK', 'Report to **Report Fraud: reportfraud.police.uk, 0300 123 2040** (England, Wales and Northern Ireland; in Scotland call Police Scotland on 101). It replaced Action Fraud in December 2025. To reach your own bank\'s fraud team, **dial 159**.'],
]];

const abuse = ['steps', [
  ['USA', '**National Domestic Violence Hotline:** 1-800-799-7233, or text START to 88788. thehotline.org. Internet use can be monitored: use a safe device.'],
  ['Canada', 'There is no single national line. Find your province at **canada.ca** (search "gender-based violence crisis lines") or look up shelters at **sheltersafe.ca**. Emergency: 911.'],
  ['UK', '**National Domestic Abuse Helpline:** 0808 2000 247 (free, 24/7). **Men\'s Advice Line:** 0808 801 0327 for men experiencing abuse. If you cannot speak on a 999 call, press 55.'],
]];

const support = ['steps', [
  ['USA and Canada', '**DivorceCare** (divorcecare.org) and **GriefShare** (griefshare.org) run local group programmes, often in churches. Fees and style vary. Some are faith-based.'],
  ['UK', '**Relate** (relate.org.uk) offers relationship counselling. Local centres set their own fees. **Cruse Bereavement Support:** 0808 808 1677.'],
]];

const lang = ['p', 'This guide is written in plain English that works in the USA, Canada and the UK. Where words differ, both are given (for example "trousers / pants", "mobile / cell"). Money is shown in dollars for the USA and Canada, and pounds for the UK where it matters.'];

// ---- chapter builders ----
function safety(withFraud) {
  const help = {
    kicker: 'USA · CANADA · UK', title: 'Where to get help',
    blocks: [
      ['lbl', 'IF YOU FEEL HOPELESS OR UNSAFE'],
      crisis,
      ['lbl', 'IF A PARTNER OR EX FRIGHTENS YOU'],
      abuse,
      check,
    ],
  };
  if (!withFraud) return [help];
  return [help, {
    kicker: 'USA · CANADA · UK', title: 'If you think you are being scammed', hideToc: true,
    blocks: [
      ['p', 'Stop contact. Do not send more money. Tell your bank or card company straight away, keep the messages and screenshots, and report it. Shame keeps scams going: you are not the first, and reporting helps.'],
      fraud,
      check,
    ],
  }];
}
function supportChapter() {
  return {
    kicker: 'USA · CANADA · UK', title: 'Support for divorce, grief and relationships',
    blocks: [
      ['p', 'Starting again is easier with people around you. These services are for the stage before dating, or alongside it.'],
      support,
      ['tip', 'A note on counselling', 'A licensed counsellor or therapist can help in ways a guide cannot. In the UK you can ask your GP or look for a BACP-registered counsellor. In the USA and Canada, ask your doctor or search a licensed-professional directory in your state or province.'],
      check,
    ],
  };
}
function etiquette() {
  return {
    kicker: 'USA · CANADA · UK', title: 'Dating customs: what is normal where you live',
    blocks: [
      ['p', 'Customs vary by city, age and background. Surveys on them are small and often company-run, and I found none on first dates for over-35s, so treat this as common practice and be kind.'],
      ['steps', [
        ['Who pays', 'Surveys disagree. In US polls, answers were split between "the man", "whoever asked" and "split it". A UK survey found "split evenly" the most common answer. The safe move in all three countries: offer to split, or say "this one is on me, next one is yours", and accept a no kindly.'],
        ['What to call it', 'In the USA and Canada people say "date" fairly early. In the UK, "meeting up" or "going for a drink" is common before anyone says "date". Match the other person\'s word.'],
        ['Where to meet', 'A public place, in daylight, that you chose or know. Tell a friend where you are going and when you will message them. This is general safety advice, not a rule of any one country.'],
        ['Apps', 'Pew (USA, 2022) found Tinder, Match and Bumble the most used among online daters. UK figures (Ofcom, 2024) show Tinder, Hinge and Bumble with the largest reach, and that Plenty of Fish and Badoo skew towards ages 35 to 54. No reliable ranking for Canada was found. Pick the app where people your age actually are.'],
      ]],
    ],
  };
}
module.exports = { safety, supportChapter, etiquette, check, crisis, fraud, abuse, support };
