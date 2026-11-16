// Builds one sales page per guide (and per bundle) in the store design.
// Data: CONFIG in ../store/index.html (names, prices, links) + chapter titles from products/build/content*.js.
// Run: node build_pages.js   (from this folder)
const fs = require('fs'), path = require('path'), vm = require('vm');
const here = __dirname;
const store = fs.readFileSync(path.join(here, '../store/index.html'), 'utf8');
const cfgSrc = store.slice(store.indexOf('const CONFIG = '), store.indexOf('/* ===== end of editable block'));
const ctx = {}; vm.createContext(ctx); vm.runInContext(cfgSrc.replace('const CONFIG =', 'CONFIG ='), ctx);
const CONFIG = ctx.CONFIG;
const css = store.match(/<style>([\s\S]*?)<\/style>/)[1];

// chapter titles from the content modules
const B = path.join(here, '../../products/build');
const chapters = {};
const add = (prods) => prods.forEach(p => { chapters[p.id] = p.chapters.filter(c => !c.hideToc).map(c => c.title); });
add(require(path.join(B, 'extend.js'))(require(path.join(B, 'content.js')).products));
add(require(path.join(B, 'content2.js')).products);
add(require(path.join(B, 'content3.js')).products);
add(require(path.join(B, 'content5.js')).products);
add(require(path.join(B, 'content6.js')).products);
add(require(path.join(B, 'content7.js')).products);

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const SEO = {
  'wolfe-dating-again-starter-guide-us-ca-uk': ['Dating After Divorce for Men: A Calm Starter Guide (PDF)', 'dating after divorce for men, how to start dating again after divorce, dating after 40'],
  'wolfe-profile-fixer-40-plus-us-ca-uk': ['Dating Profile Tips for Men Over 40: Profile Fixer (PDF)', 'dating profile tips for men over 50, dating profile photos for men, bald guy dating'],
  'wolfe-30-day-confidence-workbook-us-ca-uk': ['30-Day Dating Confidence Workbook for Men (PDF)', 'fear of dating again, dating confidence, dating anxiety'],
  'wolfe-rejection-resilience-guide-us-ca-uk': ['Ghosted or Rejected? Rejection & Resilience Guide (PDF)', 'ghosted, rejection, dating after 40'],
  'wolfe-scam-red-flag-checklist-us-ca-uk': ['Free Romance Scam Red-Flag Checklist (USA, Canada, UK)', 'romance scam red flags, elder romance scam, online dating safety'],
  'wolfe-scam-proof-dating-guide': ['Scam-Proof Dating Guide for 50+ (PDF)', 'romance scam explained, elder romance scam, online dating safety'],
  'wolfe-conversation-starters-35-plus-us-ca-uk': ['Conversation Starters After 35: What to Ask on a Date (PDF)', 'conversation starters for dates, how to text when you do not know what to say'],
  'wolfe-50-texts-cheat-sheet': ['50 Texts That Get Replies: Free Cheat Sheet', 'what to text a girl, what to never text'],
  'wolfe-she-went-quiet-guide': ['She Stopped Replying? What to Do (and Not Do) (PDF)', 'she stopped replying to my texts, ghosted'],
  'wolfe-first-date-blueprint': ['First Date Tips for Men Over 40: First Date Blueprint (PDF)', 'first date tips for men'],
  'wolfe-dating-again-starter-guide-for-her-us-ca-uk': ['Dating Again After 35 for Women: Safety-First Starter Guide (PDF)', 'dating after divorce for women, dating after 40 for women'],
  'wolfe-profile-fixer-for-women-35-plus-us-ca-uk': ['Dating Profile Tips for Women Over 35: Profile Fixer (PDF)', 'dating profile tips for women, online dating safety for women'],
  'wolfe-30-day-confidence-challenge-for-women-us-ca-uk': ['30-Day Dating Confidence Challenge for Women (PDF)', 'dating confidence for women, getting back into dating'],
};
const WHO = {
  free: [['Anyone dating online, or thinking about it.', 'People who want to try the style before buying.'], ['A substitute for legal, financial or medical advice.', 'A promise of any result.']],
  him: [['Men 35+ dating again after divorce, loss or a long time single.', 'Men who feel out of practice and want clear, calm steps.', 'Anyone who wants honest advice without tricks.'], ['Pickup tricks or ways to "make" someone like you.', 'Therapy, medical, legal or financial advice.', 'A promise of dates, partners or any result.']],
  her: [['Women 35+ dating again after divorce, loss or a long time single.', 'Women who want a calm, safety-first approach.', 'Anyone who wants honest advice without tricks.'], ['A promise of dates, partners or any result.', 'Therapy, medical, legal or financial advice.', 'Advice that blames you for how others behave.']],
  all: [['Men and women 35+ dating again, in the USA, Canada or the UK.', 'Anyone who blanks on what to ask.', 'Readers who like to know what research does and does not say.'], ['Pickup lines or tricks.', 'A promise of a date or a partner.', 'Therapy or professional advice.']],
};
const all = [...CONFIG.items, ...CONFIG.bundles];
const bundleIncludes = {
  'bundle-toolkit': ['wolfe-dating-again-starter-guide-us-ca-uk', 'wolfe-profile-fixer-40-plus-us-ca-uk', 'wolfe-30-day-confidence-workbook-us-ca-uk', 'wolfe-scam-proof-dating-guide', 'wolfe-80-conversation-starters', 'wolfe-rejection-resilience-guide-us-ca-uk'],
  'bundle-her': ['wolfe-dating-again-starter-guide-for-her-us-ca-uk', 'wolfe-profile-fixer-for-women-35-plus-us-ca-uk', 'wolfe-30-day-confidence-challenge-for-women-us-ca-uk'],
  'bundle-complete': ['wolfe-dating-again-starter-guide-us-ca-uk', 'wolfe-profile-fixer-40-plus-us-ca-uk', 'wolfe-30-day-confidence-workbook-us-ca-uk', 'wolfe-scam-proof-dating-guide', 'wolfe-80-conversation-starters', 'wolfe-rejection-resilience-guide-us-ca-uk', 'wolfe-conversation-playbook', 'wolfe-she-went-quiet-guide', 'wolfe-first-date-blueprint'],
};
const byId = Object.fromEntries(all.map(i => [i.id, i]));
const imgOf = i => '../store/img/' + (i.img || i.id) + '.png';
const priceOf = i => i.price === 0 ? '<span class="free">Free</span>' : '$' + i.price + (i.listTotal ? ' <small>instead of $' + i.listTotal + '</small>' : '');
const buy = i => i.price === 0 ? (i.url ? `<a class="btn" href="${esc(i.url)}">Get it free</a>` : '<a class="btn off">Free download coming soon</a>') : (i.url ? `<a class="btn" href="${esc(i.url)}">Buy now</a>` : '<a class="btn off">Coming soon</a>');
const li = a => a.map(x => `<li>${esc(x)}</li>`).join('');

function related(item) {
  const pool = CONFIG.items.filter(i => i.id !== item.id && i.group === item.group);
  const rest = CONFIG.items.filter(i => i.id !== item.id && i.group !== item.group && i.price > 0);
  return [...pool, ...rest].slice(0, 3);
}
function page(item) {
  const isBundle = !!bundleIncludes[item.id];
  const [seoT, kw] = SEO[item.id] || [item.name + ' (PDF)', ''];
  const grp = item.group || (isBundle ? 'all' : 'him');
  const [who, not] = WHO[item.price === 0 ? 'free' : grp] || WHO.him;
  const chs = chapters[item.id] || [];
  const inc = isBundle ? bundleIncludes[item.id].map(id => byId[id]).filter(Boolean) : [];
  const dsc = (item.tagline || '').replace(/"/g, "'");
  const prev = fs.existsSync(path.join(here, '../previews/' + item.id + '-preview.png')) ? `<section><div class="wrap"><div class="kicker">A look inside</div><h2>What the pages look like</h2><img class="prev" src="../previews/${item.id}-preview.png" alt="${esc(item.name)}: sample pages" loading="lazy"></div></section>` : '';
  const ld = { '@context': 'https://schema.org', '@type': 'Product', name: item.name, description: item.tagline, image: imgOf(item), brand: { '@type': 'Brand', name: 'WOLFE' }, offers: { '@type': 'Offer', price: String(item.price), priceCurrency: 'USD', availability: item.url ? 'https://schema.org/InStock' : 'https://schema.org/PreOrder' } };
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(seoT)} | WOLFE</title>
<meta name="description" content="${esc(dsc)}${kw ? ' ' : ''}">
${kw ? `<meta name="keywords" content="${esc(kw)}">` : ''}
<script type="application/ld+json">${JSON.stringify(ld)}</script>
<style>${css}
.back{color:var(--mute);font-size:14px;text-decoration:none}.back:hover{color:#fff}
.hero2{display:grid;grid-template-columns:minmax(220px,340px) 1fr;gap:40px;align-items:center;padding:56px 0 48px;background:radial-gradient(ellipse at 80% 100%,rgba(229,34,47,.28),transparent 60%)}
.hero2 img.cv{width:100%;border-radius:6px 14px 14px 6px;box-shadow:0 30px 60px rgba(0,0,0,.7),0 0 60px rgba(229,34,47,.25)}
.hero2 h1{font-size:clamp(30px,5vw,50px)}
.meta{color:var(--mute);font-size:14px;margin:.4em 0}
.pricebig{font-size:38px;font-weight:900;margin:14px 0 6px}
.pricebig small{font-size:15px;color:var(--mute);font-weight:500}
img.prev{width:100%;border-radius:12px;border:1px solid var(--line)}
.chl{columns:2;column-gap:28px;padding-left:20px}.chl li{break-inside:avoid;margin-bottom:6px;color:#d8d8e0}
.inc{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px}
.inc a{text-decoration:none;font-size:13.5px;color:#d8d8e0}.inc img{width:100%;border-radius:6px;display:block;margin-bottom:6px}
.more{margin-top:8px;display:block;color:var(--red2);font-size:14px;text-decoration:none}
@media(max-width:760px){.hero2{grid-template-columns:1fr}.chl{columns:1}}
</style></head><body>
<header><div class="wrap"><div class="brand">WOLFE</div><nav><a class="back" href="../store/index.html">&larr; All guides</a></nav></div></header>
<div class="wrap"><div class="hero2">
  <img class="cv" src="${imgOf(item)}" alt="${esc(item.name)} cover">
  <div>
    <div class="kicker">${esc(item.tag)}</div>
    <h1>${esc(item.name)}</h1>
    <p class="sub">${esc(item.tagline)}</p>
    <div class="meta">${item.pages ? item.pages + ' pages &middot; ' : ''}PDF &middot; read on your phone or print</div>
    <div class="pricebig">${priceOf(item)}</div>
    ${buy(item)}
    <div class="ai">Dorian Wolfe is an AI-generated character, not a real person.</div>
    <div class="meta" style="margin-top:12px">7-day refund. If it is not useful to you, reply to your receipt email within 7 days.</div>
  </div>
</div></div>

<section><div class="wrap">
  <div class="kicker">What you get</div><h2>${isBundle ? 'Included in this bundle' : 'Inside'}</h2>
  ${item.bullets ? `<ul>${li(item.bullets)}</ul>` : ''}
  ${isBundle ? `<div class="inc">${inc.map(p => `<a href="${p.id}.html"><img src="${imgOf(p)}" alt="${esc(p.name)}">${esc(p.name)}</a>`).join('')}</div>` : (chs.length ? `<div class="lbl" style="margin:22px 0 10px;color:var(--mute);letter-spacing:.2em;font-size:12px;text-transform:uppercase">Chapters</div><ol class="chl">${li(chs)}</ol>` : '')}
</div></section>
${prev}
<section><div class="wrap"><div class="two">
  <div class="box yes"><h3>Who this is for</h3><ul>${li(who)}</ul></div>
  <div class="box no"><h3>What this is not</h3><ul>${li(not)}</ul></div>
</div></div></section>

<section><div class="wrap"><div class="kicker">Honest note</div><h2>How these guides are made</h2>
  <p class="lead">Dorian Wolfe is an AI-generated character with no personal life story. The guides draw on general relationship and social-skills research and common sense. Studies of dating after 35 are limited, so the advice is practical guidance, not a guarantee. Nothing here promises a date, a partner or any result.</p>
  <p class="lead">General information for adults. Not therapy, medical, legal or financial advice. If you feel hopeless, please talk to someone now: USA or Canada, call or text 988; UK, Samaritans 116 123.</p>
</div></section>

<section><div class="wrap"><div class="kicker">More</div><h2>You might also like</h2>
  <div class="grid">${related(item).map(r => `<div class="card"><img src="${imgOf(r)}" alt="${esc(r.name)} cover" loading="lazy"><div class="b"><div class="tag">${esc(r.tag)}</div><h3>${esc(r.name)}</h3><div class="price">${priceOf(r)}</div><a class="more" href="${r.id}.html">See details &rarr;</a></div></div>`).join('')}</div>
</div></section>

<footer><div class="wrap"><p><strong>WOLFE</strong> by Dorian Wolfe, an AI-generated character. General information for adults. Not therapy, medical advice, legal advice or financial advice. No result is guaranteed. For personal use only: please do not share or resell the PDFs.</p><p>Support: ${esc(CONFIG.support)}</p></div></footer>
</body></html>`;
}
let n = 0;
for (const item of all) { fs.writeFileSync(path.join(here, item.id + '.html'), page(item)); n++; }
console.log('built', n, 'pages');
