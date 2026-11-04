// Line-art illustrations and diagram renderers for the WOLFE PDFs (inline SVG/CSS, no external images).
const R = '#e5222f', R2 = '#ff4d5a', W = '#ececf0', M = '#9a9aa6', P = '#16161a', L = '#2a2a31';
const S = (inner, vb = '0 0 400 200') => `<svg viewBox="${vb}" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="${W}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">${inner}</svg>`;
const glow = (cx, cy, r) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${R}" fill-opacity=".14" stroke="none"/>`;

const art = {
  coffee: S(`${glow(200, 100, 85)}
    <path d="M70 160h260" stroke="${L}"/>
    <path d="M110 90h70v40a30 30 0 0 1-30 30h-10a30 30 0 0 1-30-30z" fill="${P}"/><path d="M180 100h14a14 14 0 0 1 0 28h-14"/>
    <path d="M130 70c-8-10 8-14 0-26M155 70c-8-10 8-14 0-26" stroke="${M}"/>
    <path d="M220 90h70v40a30 30 0 0 1-30 30h-10a30 30 0 0 1-30-30z" fill="${P}"/><path d="M290 100h14a14 14 0 0 1 0 28h-14"/>
    <path d="M240 70c-8-10 8-14 0-26M265 70c-8-10 8-14 0-26" stroke="${M}"/>
    <path d="M200 52c-9-12-24 2-9 14l9 8 9-8c15-12 0-26-9-14z" fill="${R}" stroke="${R}"/>`),
  phone: S(`${glow(200, 100, 85)}
    <rect x="150" y="14" width="100" height="172" rx="16" fill="${P}"/><path d="M185 26h30" stroke="${M}"/>
    <path d="M165 56h48a8 8 0 0 1 8 8v14a8 8 0 0 1-8 8h-30l-10 9v-9h-8a8 8 0 0 1-8-8V64a8 8 0 0 1 8-8z" stroke="${M}"/>
    <path d="M235 104h-44a8 8 0 0 0-8 8v14a8 8 0 0 0 8 8h26l10 9v-9a8 8 0 0 0 8-8v-14a8 8 0 0 0-8-8z" fill="${R}" fill-opacity=".35" stroke="${R2}"/>
    <circle cx="180" cy="152" r="3" fill="${W}"/><circle cx="195" cy="152" r="3" fill="${W}"/><circle cx="210" cy="152" r="3" fill="${W}"/>
    <path d="M95 60c20 10 20 30 0 40M80 70c10 5 10 15 0 20M305 120c-20 10-20 30 0 40M320 130c-10 5-10 15 0 20" stroke="${R2}"/>`),
  shield: S(`${glow(200, 100, 85)}
    <path d="M200 20l70 26v52c0 40-28 68-70 82-42-14-70-42-70-82V46z" fill="${P}"/>
    <path d="M168 100l24 24 42-46" stroke="${R2}" stroke-width="6"/>
    <circle cx="298" cy="62" r="22" stroke="${M}"/><path d="M314 78l22 22" stroke="${M}" stroke-width="5"/>
    <path d="M86 150l34-12M72 120h26" stroke="${R2}"/>`),
  path: S(`${glow(220, 100, 90)}
    <path d="M40 170c60 0 70-50 130-50s60-40 110-40 40-40 80-50" stroke="${M}" stroke-dasharray="2 10" stroke-width="4"/>
    <circle cx="40" cy="170" r="9" fill="${W}" stroke="none"/>
    <circle cx="170" cy="120" r="7" fill="${R2}" stroke="none"/><circle cx="280" cy="80" r="7" fill="${R2}" stroke="none"/>
    <path d="M360 30v50" stroke="${W}"/><path d="M360 30h34l-8 12 8 12h-34" fill="${R}" stroke="${R}"/>`),
  photo: S(`${glow(200, 100, 85)}
    <rect x="130" y="16" width="140" height="168" rx="12" fill="${P}"/>
    <circle cx="200" cy="82" r="28"/><path d="M146 170c0-30 24-48 54-48s54 18 54 48"/>
    <path d="M150 36l10 10M250 36l-10 10M150 164l10-10M250 164l-10-10" stroke="${R2}"/>
    <circle cx="262" cy="42" r="10" fill="${R2}" stroke="none"/>
    <path d="M300 60l12 8-12 8M96 120l-12 8 12 8" stroke="${R2}"/>`),
  stairs: S(`${glow(220, 100, 90)}
    <path d="M40 170h60v-30h60v-30h60v-30h60v-30h60" fill="${P}"/>
    <path d="M40 170h320" stroke="${L}"/>
    <circle cx="276" cy="30" r="10" fill="${R}" stroke="none"/><path d="M276 40v22M276 48l-12 10M276 48l12 10M276 62l-10 18M276 62l10 18" stroke="${R2}"/>
    <path d="M96 128l8-8M156 98l8-8M216 68l8-8" stroke="${R2}"/>`),
  umbrella: S(`${glow(200, 100, 85)}
    <path d="M90 100a110 90 0 0 1 220 0z" fill="${R}" fill-opacity=".3" stroke="${R2}"/>
    <path d="M200 100v62a14 14 0 0 1-28 0" stroke="${W}"/>
    <path d="M200 16v16" /><path d="M145 100a30 40 0 0 0 55 0M200 100a30 40 0 0 0 55 0" stroke="${R2}"/>
    <path d="M70 130l-6 16M110 138l-6 16M290 138l-6 16M330 130l-6 16M250 148l-6 16" stroke="${M}"/>
    <path d="M200 134c-8-10-22 2-8 12l8 7 8-7c14-10 0-22-8-12z" fill="${R}" stroke="${R}"/>`),
  lock: S(`${glow(200, 100, 85)}
    <rect x="150" y="90" width="100" height="86" rx="12" fill="${P}"/>
    <path d="M170 90V68a30 30 0 0 1 60 0v22"/>
    <circle cx="200" cy="130" r="9" fill="${R2}" stroke="none"/><path d="M200 138v18" stroke="${R2}"/>
    <path d="M290 40h60a8 8 0 0 1 8 8v22a8 8 0 0 1-8 8h-44l-14 12V78h-2a8 8 0 0 1-8-8V48a8 8 0 0 1 8-8z" stroke="${M}"/>
    <path d="M60 60h50M60 78h30" stroke="${M}"/>`),
  compass: S(`${glow(200, 100, 85)}
    <circle cx="200" cy="100" r="76" fill="${P}"/><circle cx="200" cy="100" r="64" stroke="${L}"/>
    <path d="M200 34v12M200 154v12M134 100h12M254 100h12" stroke="${M}"/>
    <path d="M222 78l-14 36-30 8 14-36z" fill="${R}" stroke="${R2}"/><circle cx="200" cy="100" r="5" fill="${W}" stroke="none"/>
    <path d="M60 170c20-12 40-12 60 0M280 170c20-12 40-12 60 0" stroke="${M}"/>`),
  pin: S(`${glow(200, 100, 85)}
    <path d="M200 20a50 50 0 0 1 50 50c0 36-50 96-50 96s-50-60-50-96a50 50 0 0 1 50-50z" fill="${P}"/>
    <circle cx="200" cy="70" r="17" fill="${R}" stroke="${R2}"/>
    <circle cx="300" cy="60" r="30" stroke="${M}"/><path d="M300 42v18l12 8" stroke="${M}"/>
    <path d="M90 172h220" stroke="${L}"/><path d="M96 150l20 22M110 150l20 22" stroke="${M}"/>`),
  bubbles: S(`${glow(200, 100, 90)}
    <path d="M70 40h120a14 14 0 0 1 14 14v40a14 14 0 0 1-14 14h-70l-28 24v-24h-22a14 14 0 0 1-14-14V54a14 14 0 0 1 14-14z" fill="${P}"/>
    <path d="M130 92c0-12 18-12 18-24s-20-12-20-2M130 100v2" transform="translate(-14 -8)" stroke="${R2}"/>
    <path d="M330 100H230a14 14 0 0 0-14 14v32a14 14 0 0 0 14 14h56l24 22v-22h20a14 14 0 0 0 14-14v-32a14 14 0 0 0-14-14z" fill="${R}" fill-opacity=".3" stroke="${R2}"/>
    <circle cx="250" cy="130" r="4" fill="${W}" stroke="none"/><circle cx="272" cy="130" r="4" fill="${W}" stroke="none"/><circle cx="294" cy="130" r="4" fill="${W}" stroke="none"/>`),
  door: S(`${glow(200, 110, 90)}
    <path d="M120 176V40h116v136" fill="${P}"/><path d="M236 40l40 12v108l-40 16" stroke="${M}"/>
    <path d="M130 170h100" stroke="${L}"/><circle cx="216" cy="110" r="4" fill="${W}" stroke="none"/>
    <path d="M178 176V70" stroke="${R2}" stroke-opacity=".0"/>
    <path d="M300 100l60-20M300 120l70 0M300 140l60 20" stroke="${R2}" stroke-width="2.5"/>
    <path d="M60 60l8-12M84 52l4-14M44 80l-10-6" stroke="${M}"/>`),
  calendar: S(`${glow(200, 100, 85)}
    <rect x="110" y="30" width="180" height="140" rx="14" fill="${P}"/><path d="M110 64h180M150 18v26M250 18v26"/>
    ${[0,1,2,3,4].map(c => [0,1,2].map(r => `<rect x="${126 + c * 32}" y="${78 + r * 28}" width="20" height="18" rx="4" stroke="${M}" stroke-width="2"/>`).join('')).join('')}
    <path d="M196 106l7 7 14-16" stroke="${R2}" stroke-width="4"/><path d="M132 84l6 6 10-12" stroke="${R2}" stroke-width="4"/>`),
};

// small line icons (24x24) for icon grids
const ic = {
  star: '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
  clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  heart: '<path d="M12 21s-8-5-8-11a4.5 4.5 0 0 1 8-3 4.5 4.5 0 0 1 8 3c0 6-8 11-8 11z"/>',
  chat: '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
  shield: '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
  user: '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
  eye: '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
  help: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7M12 17v.1"/>',
  link: '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
  lock: '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
  phone: '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
  camera: '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
  pen: '<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/>',
  walk: '<circle cx="13" cy="4" r="2"/><path d="M11 21l2-7-3-3 1-5 4 3 3 1M10 11L7 13"/>',
  users: '<circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M2 20c0-4 3-6 7-6s7 2 7 6M16 14c3 0 6 1.5 6 5"/>',
  flag: '<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>',
  bolt: '<path d="M13 2L5 14h6l-1 8 8-12h-6z"/>',
  sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
  home: '<path d="M3 11l9-8 9 8v9H3z"/><path d="M9 20v-6h6v6"/>',
  money: '<circle cx="12" cy="12" r="9"/><path d="M14.5 9a3 3 0 0 0-5 1.5c0 3 5 1.5 5 4.500a3 3 0 0 1-5 1.500M12 6v2M12 16v2"/>',
};
const icon = (k, size = 28, color = R2) => `<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="${color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${ic[k] || ic.star}</svg>`;
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const rich = s => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');

const css = `
.art{margin:.04in 0 .14in;text-align:center;break-inside:avoid}
.art svg{width:100%;max-height:1.25in}
.art .cap{font-size:7.5pt;color:var(--mute);letter-spacing:.14em;text-transform:uppercase;margin-top:2px}
.vflow{display:flex;align-items:stretch;gap:0;margin:.08in 0 .16in;break-inside:avoid}
.vflow .n{flex:1;text-align:center;position:relative;padding:0 3px}
.vflow .c{width:.36in;height:.36in;border-radius:50%;background:var(--red);color:#fff;font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center;margin:0 auto 5px;box-shadow:0 0 14px rgba(229,34,47,.5)}
.vflow .t{font-size:8pt;font-weight:700;color:#fff;line-height:1.2}
.vflow .s{font-size:6.8pt;color:var(--mute);line-height:1.25;margin-top:2px}
.vflow .n:not(:last-child)::after{content:"";position:absolute;top:.17in;left:calc(50% + .24in);right:calc(-50% + .24in);border-top:2px dashed #5a1f26}
.vladder{display:flex;align-items:flex-end;gap:5px;margin:.1in 0 .16in;height:1.9in;break-inside:avoid}
.vladder .st{flex:1;background:linear-gradient(180deg,#3a0f14,#1a0b0d);border:1px solid #6a1b22;border-radius:6px 6px 0 0;padding:6px 5px;font-size:7.4pt;line-height:1.25;color:#e8e8ee;display:flex;flex-direction:column;justify-content:flex-start}
.vladder .st b{display:block;color:var(--red2);font-size:12pt;font-weight:900;margin-bottom:2px}
.vvs{display:grid;grid-template-columns:1fr 1fr;gap:.12in;margin:.08in 0 .16in;break-inside:avoid}
.vvs .col{border-radius:10px;padding:.1in .13in}
.vvs .a{background:#0c1a11;border:1px solid #1f4a2c}.vvs .b{background:#1a0c0e;border:1px solid #4a1a1f}
.vvs .t1{background:#101a22;border:1px solid #1f3a4a}.vvs .t2{background:#1d0c0f;border:1px solid #5a1f26}.vvs .t1 h4{color:#7cc4ff}.vvs .t2 h4{color:var(--red2)}.vvs .t1 .it i{color:#7cc4ff}.vvs .t2 .it i{color:var(--red2)}
.vvs h4{margin:0 0 5px;font-size:8pt;letter-spacing:.14em;text-transform:uppercase}
.vvs .a h4{color:#6ee7a0}.vvs .b h4{color:var(--red2)}
.vvs .it{display:flex;gap:6px;font-size:8.4pt;line-height:1.3;margin-bottom:4px;color:#e1e1e8}
.vvs .it i{font-style:normal;font-weight:900;flex:0 0 10px}
.vvs .a .it i{color:#6ee7a0}.vvs .b .it i{color:var(--red2)}
.vsig{margin:.06in 0 .16in;break-inside:avoid}
.vsig .r{display:flex;gap:10px;align-items:flex-start;padding:5px 0;border-bottom:1px solid #1d1d23;font-size:9pt}
.vsig .d{flex:0 0 14px;height:14px;border-radius:50%;margin-top:2px}
.vsig .go{background:#34d27b;box-shadow:0 0 10px rgba(52,210,123,.6)}.vsig .slow{background:#ffc83d;box-shadow:0 0 10px rgba(255,200,61,.5)}.vsig .stop{background:#ff4d5a;box-shadow:0 0 10px rgba(255,77,90,.6)}
.vsig .l{flex:0 0 .5in;font-size:6.8pt;letter-spacing:.14em;font-weight:800;text-transform:uppercase;color:var(--mute);margin-top:3px}
.vtl{margin:.08in 0 .16in;position:relative;padding-left:.78in;break-inside:avoid}
.vtl::before{content:"";position:absolute;left:.62in;top:6px;bottom:6px;border-left:2px solid #5a1f26}
.vtl .r{position:relative;padding:4px 0 8px}
.vtl .tm{position:absolute;left:-.78in;top:3px;width:.52in;text-align:right;font-weight:800;font-size:8pt;color:var(--red2)}
.vtl .r::before{content:"";position:absolute;left:-.2in;top:8px;width:10px;height:10px;border-radius:50%;background:var(--red);box-shadow:0 0 0 3px #09090b}
.vtl .tx{font-size:9.2pt;color:#e8e8ee}
.vcal{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;margin:.08in 0 .12in;break-inside:avoid}
.vcal div{border:1px solid #3a3a44;border-radius:6px;height:.46in;padding:3px 4px;font-size:7pt;color:var(--mute);position:relative;background:#101014}
.vcal div b{color:#fff;font-size:8.5pt}
.vcal div::after{content:"";position:absolute;right:4px;bottom:4px;width:10px;height:10px;border:1.5px solid var(--red2);border-radius:3px}
.vcal .mile{border-color:var(--red);background:#1f0d10}
.vdial{margin:.1in 0 .16in;break-inside:avoid}
.vdial .bar{position:relative;height:10px;border-radius:5px;background:linear-gradient(90deg,#34d27b,#ffc83d,#ff4d5a);margin:14px 4px 6px}
.vdial .pt{position:absolute;top:-6px;width:22px;height:22px;border-radius:50%;background:#fff;border:3px solid var(--red);margin-left:-11px}
.vdial .lb{display:flex;justify-content:space-between;font-size:7.6pt;font-weight:800;letter-spacing:.14em;color:var(--mute)}
.vdial .nt{font-size:8.6pt;color:#d8d8e0;margin-top:6px;text-align:center}
.vic{display:grid;grid-template-columns:repeat(var(--cols,4),1fr);gap:.08in;margin:.08in 0 .16in;break-inside:avoid}
.vic .c{background:#111116;border:1px solid var(--line);border-radius:10px;padding:.09in .07in;text-align:center}
.vic .c svg{display:block;margin:0 auto 4px}
.vic .t{font-size:7.8pt;font-weight:800;color:#fff;line-height:1.2}
.vic .s{font-size:6.8pt;color:var(--mute);line-height:1.25;margin-top:2px}
.vstat{display:flex;gap:.1in;margin:.08in 0 .16in;break-inside:avoid}
.vstat .c{flex:1;border:1px solid #4a1a1f;background:linear-gradient(135deg,#1d0c0f,#121216);border-radius:10px;padding:.09in .1in;text-align:center}
.vstat .big{font-family:"Inter Display",Inter;font-weight:900;font-size:19pt;color:var(--red2);line-height:1}
.vstat .sm{font-size:7.4pt;color:#cfcfd8;margin-top:3px;line-height:1.25}
.motif{position:absolute;right:.15in;bottom:.95in;width:3.7in;opacity:.95;pointer-events:none}
.motif svg{width:100%}
`;

function render(b) {
  const [t, a, c, d, e2] = b;
  if (t === 'art') return `<div class="art">${art[a]}${c ? `<div class="cap">${esc(c)}</div>` : ''}</div>`;
  if (t === 'flow') return `<div class="vflow">${a.map((x, i) => { const [h, s] = Array.isArray(x) ? x : [x, '']; return `<div class="n"><div class="c">${i + 1}</div><div class="t">${esc(h)}</div>${s ? `<div class="s">${esc(s)}</div>` : ''}</div>`; }).join('')}</div>`;
  if (t === 'ladder') return `<div class="vladder">${a.map((x, i) => `<div class="st" style="height:${30 + (i + 1) * (70 / a.length)}%"><b>${i + 1}</b>${esc(x)}</div>`).join('')}</div>`;
  if (t === 'vs') return `<div class="vvs"><div class="col a"><h4>${esc(a)}</h4>${c.map(x => `<div class="it"><i>✓</i><span>${rich(x)}</span></div>`).join('')}</div><div class="col b"><h4>${esc(d)}</h4>${e2.map(x => `<div class="it"><i>✕</i><span>${rich(x)}</span></div>`).join('')}</div></div>`;
  if (t === 'two') return `<div class="vvs"><div class="col t1"><h4>${esc(a)}</h4>${c.map(x => `<div class="it"><i>&#9656;</i><span>${rich(x)}</span></div>`).join('')}</div><div class="col t2"><h4>${esc(d)}</h4>${e2.map(x => `<div class="it"><i>&#9656;</i><span>${rich(x)}</span></div>`).join('')}</div></div>`;
  if (t === 'signals') return `<div class="vsig">${a.map(([k, x]) => `<div class="r"><div class="d ${k}"></div><div class="l">${k === 'go' ? 'Good' : k === 'slow' ? 'Slow down' : 'Stop'}</div><div>${rich(x)}</div></div>`).join('')}</div>`;
  if (t === 'timeline') return `<div class="vtl">${a.map(([tm, x]) => `<div class="r"><div class="tm">${esc(tm)}</div><div class="tx">${rich(x)}</div></div>`).join('')}</div>`;
  if (t === 'cal') return `<div class="vcal">${Array.from({ length: a }, (_, i) => `<div class="${[6, 13, 20, 27].includes(i) ? 'mile' : ''}"><b>${i + 1}</b></div>`).join('')}</div>`;
  if (t === 'dial') return `<div class="vdial"><div class="bar"><div class="pt" style="left:${Math.round(d * 100)}%"></div></div><div class="lb"><span>${esc(a)}</span><span>${esc(c)}</span></div>${e2 ? `<div class="nt">${rich(e2)}</div>` : ''}</div>`;
  if (t === 'icons') return `<div class="vic" style="--cols:${c || 4}">${a.map(([k, h, s]) => `<div class="c">${icon(k, 26)}<div class="t">${esc(h)}</div>${s ? `<div class="s">${esc(s)}</div>` : ''}</div>`).join('')}</div>`;
  if (t === 'stat') return `<div class="vstat">${a.map(([big, sm]) => `<div class="c"><div class="big">${esc(big)}</div><div class="sm">${esc(sm)}</div></div>`).join('')}</div>`;
  return null;
}
module.exports = { art, icon, css, render };
