// US / Canada / UK editions of the men's guides: #1 Scam Checklist, #2 Starter, #3 Profile Fixer, #4 30-Day Challenge, #7 Rejection.
const reg = require('./regional.js');
const c2 = require('./content2.js');
const c3 = require('./content3.js');
const NAME = c2.NAME, BRAND = c2.BRAND;
const all = [...c2.products, ...c3.products];
const get = id => JSON.parse(JSON.stringify(all.find(p => p.id === id)));
const suffix = (p, kind) => { p.id += '-us-ca-uk'; p.kind = kind; return p; };

const scam = suffix(get('wolfe-scam-red-flag-checklist'), 'FREE CHECKLIST · USA · CANADA · UK');
scam.chapters.push({
  kicker: 'USA · CANADA · UK', title: 'Where to report',
  blocks: [['p', 'Stop contact. Do not send more money. Tell your bank or card company straight away, keep the messages and screenshots, then report it. You are not the first, and reporting helps.'], reg.fraud, reg.check],
});

const starter = suffix(get('wolfe-dating-again-starter-guide'), 'STARTER GUIDE · USA · CANADA · UK');
const ri = starter.chapters.findIndex(c => c.title.toLowerCase().includes('resources'));
starter.chapters.splice(ri, 0, reg.supportChapter(), reg.etiquette(), ...reg.safety(true));
starter.chapters.splice(ri + 4); // drop the old resources chapter (replaced by the regional ones)

const profile = suffix(get('wolfe-profile-fixer-40-plus'), 'WORKBOOK + SWIPE FILE · USA · CANADA · UK');
profile.chapters.push(reg.etiquette(), ...reg.safety(true));

const challenge = suffix(get('wolfe-30-day-confidence-workbook'), 'WORKBOOK · USA · CANADA · UK');
challenge.chapters.push(reg.supportChapter(), ...reg.safety(false));

const rejection = suffix(get('wolfe-rejection-resilience-guide'), 'MINI GUIDE · USA · CANADA · UK');
rejection.chapters.push(reg.supportChapter(), ...reg.safety(false));

module.exports = { NAME, BRAND, products: [scam, starter, profile, challenge, rejection] };
