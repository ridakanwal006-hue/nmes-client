const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
let NAME, BRAND, products;
if (process.env.CONTENT) { ({ NAME, BRAND, products } = require(process.env.CONTENT)); }
else { const c = require('./content.js'); NAME = c.NAME; BRAND = c.BRAND; products = require('./extend.js')(c.products); }

const OUT = process.env.OUTDIR || '/home/user/nmes-client/products';
const charPath = path.join('/home/user/nmes-client/products', 'character.jpg');
const hasChar = fs.existsSync(charPath);
const charB64 = hasChar ? 'data:image/jpeg;base64,' + fs.readFileSync(charPath).toString('base64') : '';

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const rich = s => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');

const css = `
:root{--bg:#09090b;--panel:#16161a;--line:#2a2a31;--red:#e5222f;--red2:#ff4d5a;--text:#ececf0;--mute:#9a9aa6}
@page{size:6in 9in;margin:0.7in 0.6in 0.75in 0.6in;background:#09090b;
  @bottom-center{content:counter(page);font:600 8pt Inter;color:#6d6d78}
  @bottom-left{content:"${BRAND}";font:800 7pt Inter;letter-spacing:.25em;color:#e5222f;margin-left:0}}
@page cover{margin:0;background:#09090b;@bottom-center{content:none}@bottom-left{content:none}}
html{background:var(--bg)}
*{box-sizing:border-box}
body{margin:0;font-family:Inter,sans-serif;color:var(--text);font-size:10pt;line-height:1.55}
b{color:#fff}
.cover{page:cover;width:6in;height:9in;position:relative;overflow:hidden;background:
 radial-gradient(ellipse at 70% 95%,#4a0a10 0%,transparent 60%),
 linear-gradient(180deg,#0b0b0e,#060607);break-after:page}
.cover .char{position:absolute;right:-.6in;bottom:0;height:6.6in;width:auto;
 -webkit-mask-image:linear-gradient(180deg,transparent 0,#000 22%);mask-image:linear-gradient(180deg,transparent 0,#000 22%);opacity:.95}
.cover .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(6,6,7,.92) 0,rgba(6,6,7,.55) 55%,transparent 100%)}
.cover .in{position:absolute;left:.6in;right:.6in;top:.65in}
.brand{font-weight:800;font-size:9pt;letter-spacing:.42em;color:var(--red)}
.byline{font-size:8pt;color:var(--mute);letter-spacing:.2em;margin-top:5px;text-transform:uppercase}
.bar{height:6px;background:var(--red);width:100%;margin:.55in 0 .35in;box-shadow:0 0 22px rgba(229,34,47,.7)}
.kind{display:inline-block;border:1px solid var(--red);color:var(--red2);font-size:7.5pt;font-weight:700;letter-spacing:.22em;padding:4px 9px;margin-bottom:.22in}
.title{font-family:"Inter Display",Inter;font-weight:900;font-size:40pt;line-height:.98;letter-spacing:-.01em;text-transform:uppercase;color:#fff}
.title span{color:var(--red2);text-shadow:0 0 28px rgba(229,34,47,.55)}
.sub{margin-top:.28in;max-width:3.1in;font-size:9.5pt;color:#c9c9d2}
.foot{position:absolute;left:.6in;bottom:.5in;font-size:7.5pt;letter-spacing:.22em;color:var(--mute);text-transform:uppercase}
.chap{break-before:page}
.chap:first-of-type{break-before:auto}
.kick{color:var(--red);font-weight:800;font-size:8pt;letter-spacing:.3em}
h1{font-family:"Inter Display",Inter;font-weight:900;font-size:22pt;line-height:1.08;margin:.08in 0 .2in;text-transform:uppercase;color:#fff;
 border-bottom:3px solid var(--red);padding-bottom:.12in}
p{margin:0 0 .14in}
ul{margin:0 0 .16in;padding-left:.2in}li{margin-bottom:5px}li::marker{color:var(--red)}
.lbl{break-after:avoid;font-weight:800;font-size:7.5pt;letter-spacing:.24em;color:var(--red2);margin:.15in 0 .06in}
.msg{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--red);border-radius:6px;padding:.085in .14in;margin:0 0 .07in;break-inside:avoid;position:relative}
.msg .n{position:absolute;left:-0.0in}
.msg .t{font-weight:600;color:#fff}
.msg .w{font-size:7.8pt;color:var(--mute);margin-top:3px;letter-spacing:.02em}
.nn{display:inline-block;min-width:22px;color:var(--red2);font-weight:800;margin-right:2px}
.dont{background:#1a0d0f;border:1px solid #4a1a1f;border-radius:6px;padding:.1in .16in;margin:0 0 .16in;break-inside:avoid}
.dont div{padding:3px 0 3px 20px;position:relative}
.dont div::before{content:"✕";position:absolute;left:0;color:var(--red2);font-weight:800}
.tip{background:linear-gradient(135deg,#1d0c0f,#121216);border:1px solid #4a1a1f;border-radius:6px;padding:.12in .16in;margin:.1in 0 .16in;break-inside:avoid}
.tip .h{font-weight:800;font-size:8pt;letter-spacing:.2em;color:var(--red2);text-transform:uppercase;margin-bottom:3px}
.step{display:flex;gap:.12in;margin-bottom:.1in;break-inside:avoid}
.step .k{flex:0 0 1.35in;font-weight:800;color:#fff;font-size:9.5pt}
.step .v{flex:1;color:#d8d8e0}
.q{display:flex;gap:8px;padding:3px 0;break-inside:avoid;border-bottom:1px solid #1d1d23}
.q .nn{min-width:24px}

.chat{margin:0 0 .16in;break-inside:avoid}
.chat .b{max-width:78%;padding:.07in .12in;border-radius:12px;margin-bottom:.06in;font-size:9.5pt}
.chat .She{background:#1d1d24;border:1px solid var(--line);border-bottom-left-radius:3px}
.chat .You{background:#3a0f14;border:1px solid #6a1b22;margin-left:auto;border-bottom-right-radius:3px;text-align:left}
.chat .w{font-size:6.5pt;letter-spacing:.2em;color:var(--mute);margin:0 0 2px 2px;text-transform:uppercase}
.chat .You .w{color:#ff8a93}
.lines div{height:.27in;border-bottom:1px solid #34343c}
.chk div{padding:4px 0 4px 26px;position:relative;border-bottom:1px solid #1d1d23;break-inside:avoid}
.chk div::before{content:"";position:absolute;left:2px;top:6px;width:12px;height:12px;border:1.5px solid var(--red2);border-radius:3px}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:.1in;margin-top:.12in}
.card{border:1.5px dashed #4a4a55;border-radius:10px;padding:.12in .15in;min-height:1.62in;display:flex;flex-direction:column;justify-content:space-between;background:#101014;break-inside:avoid}
.card .tag{font-size:6.5pt;font-weight:800;letter-spacing:.24em;color:var(--red2)}
.card .qq{font-size:11pt;line-height:1.35;font-weight:600;color:#fff;margin:.08in 0}
.card .no{font-size:7.5pt;color:var(--mute);text-align:right}
.toc{page-break-after:always}
.toc .row{display:flex;gap:10px;padding:3.5px 0;border-bottom:1px solid var(--line);font-size:9pt}
.toc .row b{color:var(--red2);min-width:30px}
.toc h1{margin-top:0}
.disc{font-size:8pt;color:var(--mute);margin-top:.3in}
.end{break-before:page;text-align:center;padding-top:2.2in}
.end .big{font-family:"Inter Display",Inter;font-weight:900;font-size:24pt;text-transform:uppercase;color:#fff}
.end .big span{color:var(--red2)}
`;

function cover(p) {
  const t = p.titleLines.map((l, i) => i === p.titleLines.length - 1 ? `<span>${esc(l)}</span>` : esc(l)).join('<br>');
  return `<section class="cover">
  ${hasChar ? `<img class="char" src="${charB64}"><div class="shade"></div>` : ''}
  <div class="in">
    <div class="brand">${BRAND}</div>
    <div class="byline">by ${esc(NAME)}</div>
    <div class="bar"></div>
    <div class="kind">${esc(p.kind)}</div>
    <div class="title">${t}</div>
    <div class="sub">${esc(p.sub)}</div>
  </div>
  <div class="foot">${esc(NAME)} · AI-generated character</div>
</section>`;
}

function blocks(bl, counter) {
  return bl.map(b => {
    const [t, a, c] = b;
    if (t === 'p') return `<p>${rich(a)}</p>`;
    if (t === 'lbl') return `<div class="lbl">${esc(a)}</div>`;
    if (t === 'ul') return `<ul>${a.map(x => `<li>${rich(x)}</li>`).join('')}</ul>`;
    if (t === 'msg') { counter.n++; const num = counter.number ? `<span class="nn">${counter.n}</span>` : '';
      return `<div class="msg"><div class="t">${num}${rich(a)}</div>${c ? `<div class="w">${esc(c)}</div>` : ''}</div>`; }
    if (t === 'dont') return `<div class="dont">${a.map(x => `<div>${rich(x)}</div>`).join('')}</div>`;
    if (t === 'tip') return `<div class="tip"><div class="h">${esc(a)}</div>${rich(c)}</div>`;
    if (t === 'qs') return a.map(q => { counter.q++; return `<div class="q"><span class="nn">${counter.q}</span><span>${esc(q)}</span></div>`; }).join('');
    if (t === 'chat') return `<div class="chat">${a.map(([w, x]) => `<div class="b ${w}"><div class="w">${w}</div>${rich(x)}</div>`).join('')}</div>`;
    if (t === 'lines') return `<div class="lines">${'<div></div>'.repeat(a)}</div>`;
    if (t === 'chk') return `<div class="chk">${a.map(x => `<div>${rich(x)}</div>`).join('')}</div>`;
    if (t === 'cards') return `<div class="cards">${a.map(([tag, q]) => { counter.c = (counter.c||0)+1; return `<div class="card"><div class="tag">${esc(tag)}</div><div class="qq">${esc(q)}</div><div class="no">${counter.c}</div></div>`; }).join('')}</div>`;
    if (t === 'steps') return a.map(([k, v]) => `<div class="step"><div class="k">${esc(k)}</div><div class="v">${rich(v)}</div></div>`).join('');
    return '';
  }).join('\n');
}

function html(p) {
  const counter = { n: 0, q: 0, number: p.id.includes('50-texts') };
  const toc = `<section class="toc"><div class="kick">INSIDE</div><h1>Contents</h1>${p.chapters.map(c =>
    `<div class="row"><b>›</b><span><b style="color:#fff">${esc(c.title)}</b></span></div>`).join('')}
  <div class="disc">${esc(NAME)} is an AI-generated character, not a real person, and has no personal life story. This is general communication advice for adults. It is not therapy, medical, legal or financial advice, and no result is guaranteed. Always respect other people's boundaries and consent.</div></section>`;
  const chaps = p.chapters.map(c => { counter.q = 0;
    return `<section class="chap"><div class="kick">${esc(c.kicker)}</div>${c.noTitle ? '' : `<h1>${esc(c.title)}</h1>`}${blocks(c.blocks, counter)}</section>`; }).join('\n');
  const end = `<section class="end"><div class="big">Be calm.<br><span>Be curious.</span><br>Be real.</div><p style="color:#9a9aa6;margin-top:.3in">— ${esc(NAME)}</p></section>`;
  return `<!doctype html><html><head><meta charset="utf-8"><title>${esc(p.titleLines.join(' '))}</title><style>${css}</style></head><body>${cover(p)}${p.noToc ? '' : toc}${chaps}${p.noEnd ? '' : end}</body></html>`;
}

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  for (const p of products) {
    const h = html(p);
    fs.writeFileSync(path.join(process.env.SCRATCH, p.id + '.html'), h);
    const page = await browser.newPage();
    await page.setContent(h, { waitUntil: 'load' });
    await page.pdf({ path: path.join(OUT, p.id + '.pdf'), width: '6in', height: '9in', printBackground: true, preferCSSPageSize: true });
    // cover PNG
    const cp = await browser.newPage({ viewport: { width: 576, height: 864 }, deviceScaleFactor: 2 });
    await cp.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0}</style></head><body>${cover(p)}</body></html>`, { waitUntil: 'load' });
    await cp.screenshot({ path: path.join(OUT, p.id + '-cover.png'), clip: { x: 0, y: 0, width: 576, height: 864 } });
    console.log('built', p.id);
  }
  await browser.close();
})();
