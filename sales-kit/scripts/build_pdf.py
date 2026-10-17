#!/usr/bin/env python3
"""Builds wolfe-reel-script-library.pdf (6x9in, one designed page per script) from the script packs.
Run: NODE_PATH=/opt/node22/lib/node_modules python3 -I build_pdf.py"""
import subprocess, html, pathlib, re
here = pathlib.Path(__file__).resolve().parent
exec(open(here/'build.py').read().split("data = dict")[0])
KWMAP = {'SCAM':('Free Scam Red-Flag Checklist','Scam-Proof Dating Guide $12'),'TEXTS':('Free 50 Texts That Get Replies','Conversation Playbook $17'),
 'STARTER':('Starter Guide $14','Toolkit bundle $39'),'PROFILE':('Profile Fixer for 40+ $12','Starter Guide $14'),
 'CHALLENGE':('30-Day Confidence Challenge $12','Rejection & Resilience $8'),'QUIET':('She Went Quiet $9','Rejection & Resilience $8'),
 'REJECT':('Rejection & Resilience $8','30-Day Confidence Challenge $12'),'DATE':('First Date Blueprint $12','80 Conversation Starters $9'),
 'ASK':('80 Conversation Starters $9','Conversation Playbook $17'),'PLAYBOOK':('The Conversation Playbook $17','Complete Library $59')}
ICON = {
 'SCAM':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 'TEXTS':'<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 'STARTER':'<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>',
 'PROFILE':'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
 'CHALLENGE':'<path d="M13 2L5 14h6l-1 8 8-12h-6z"/>',
 'QUIET':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'REJECT':'<path d="M12 21s-8-5-8-11a4.5 4.5 0 0 1 8-3 4.5 4.5 0 0 1 8 3c0 6-8 11-8 11z"/>',
 'DATE':'<rect x="4" y="5" width="16" height="16" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
 'ASK':'<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7M12 17v.1"/>',
 'PLAYBOOK':'<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5M9 8h6"/>'}
def icon(k, size=18, color='currentColor'):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICON.get(k,"")}</svg>'
e = lambda s: html.escape(str(s or ''))
cap = lambda s: s[:1].upper()+s[1:]

def phone(hook, word, scale=1.0, tilt=0, extra=''):
    return f'''<div class="phone" style="transform:rotate({tilt}deg) scale({scale});{extra}"><div class="notch"></div>
<div class="ph-ai">AI</div><div class="ph-hook">{e(hook)}<span class="cur"></span></div>
<div class="ph-cap">{e(word)}</div><div class="ph-bar"><i></i></div><div class="ph-side"><b></b><b></b><b></b></div></div>'''

def first_word(d):
    w = re.sub(r'[^A-Za-z0-9\'"]', '', d['script'][0].split()[0]) if d['script'] else ''
    return (w or 'LISTEN').upper()

def page_script(d):
    free = d['kw'] in FREE
    last = len(d['script'])-1
    lines = ''.join(f'<div class="ln{" cta" if k==last else ""}"><i>{k+1}</i><span>{e(l)}</span></div>' for k,l in enumerate(d['script']))
    sub = (e(d['fmt'])+(' · pain: '+e(d['pain']) if d['pain'] else '')) if d['pack']=='b' else e(cap(d['product']))
    kw = f'<div class="blk"><div class="lbl">Search words</div><p>{e(d["keywords"])}</p></div>' if d['keywords'] else ''
    cp = f'<div class="blk"><div class="lbl">Caption</div><p>{e(d["caption"])}</p></div>' if d['caption'] else ''
    note = f'<div class="note">{e(cap(d["note"]))}</div>' if d['note'] else ''
    p1, p2 = KWMAP.get(d['kw'],('',''))
    tag = '<span class="stk meme">MEME FORMAT</span>' if d['pack']=='b' else '<span class="stk">SEARCH-LED</span>'
    return f'''<section class="pg"><div class="ghost">{e(d["code"])}</div>
<div class="hdr">{phone(d["hook"], first_word(d))}
<div class="ht"><div class="code">{e(d["code"])} · {"MEME PACK" if d["pack"]=="b" else "SEARCH PACK"}</div><h2>{e(cap(d["title"]))}</h2><div class="sub">{sub}</div>
<div class="badges">{tag}<span class="kwb{" free" if free else ""}">{icon(d["kw"],13)} {e(d["kw"])}</span></div></div></div>
<div class="lbl sec">Say it, line by line</div><div class="lines">{lines}</div>
<div class="two">{kw}{cp}<div class="blk"><div class="lbl">Hashtags</div><p class="tg">{e(d["tags"])}</p></div></div>{note}
<div class="ctabar{" free" if free else ""}"><div class="ic">{icon(d["kw"],22)}</div><div class="c1"><small>COMMENT</small><b>{e(d["kw"])}</b></div><div class="arr">&#10140;</div>
<div class="c2"><small>{"YOU SEND (FREE)" if free else "YOU SEND"}</small><b>{e(p1)}</b><span>then: {e(p2)}</span></div></div></section>'''

css = '''
@page{size:6in 9in;margin:0;background:#2e2e36}
*{box-sizing:border-box}
html,body{margin:0;background:#2e2e36;counter-reset:pg;color:#ececf0;font-family:Inter,system-ui,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{counter-increment:pg;background:#09090b;border:.17in solid #2e2e36;border-top:.17in solid #e5222f;width:6in;height:9in;padding:.34in .36in .3in;page-break-after:always;overflow:hidden;position:relative;font-size:10pt;line-height:1.42}
.pg:last-child{page-break-after:auto}
.pg::after{content:'PAGE ' counter(pg);position:absolute;right:.36in;top:.1in;font-size:7pt;letter-spacing:.2em;color:#6b6b76;font-weight:700}
.pg::before{content:'';position:absolute;left:0;right:0;top:0;bottom:0;background:radial-gradient(ellipse at 100% 0%,rgba(229,34,47,.16),transparent 55%);pointer-events:none}
.ghost{position:absolute;right:.2in;top:1.0in;font-size:92pt;font-weight:900;color:transparent;-webkit-text-stroke:1px #25252b;letter-spacing:-.03em;line-height:1;z-index:0}
.pg>*{position:relative;z-index:1}
.ghost{position:absolute!important}
.code{font-size:7.5pt;font-weight:800;letter-spacing:.2em;color:#ff4d5a}
h1{font-size:33pt;line-height:1.02;margin:.25em 0;text-transform:uppercase;font-weight:900}
h1 b{color:#ff4d5a}
h2{font-size:17pt;line-height:1.15;margin:.18em 0 .1em;font-weight:800}
.sub{font-size:8.5pt;color:#9a9aa6;margin-bottom:6px}
.hdr{display:flex;gap:14px;align-items:flex-start;margin-top:4px}
.ht{flex:1;padding-top:6px}
.badges{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.stk{font-size:6.5pt;font-weight:800;letter-spacing:.14em;color:#cfcfd8;border:1px solid #3a3a44;border-radius:4px;padding:2px 7px}
.stk.meme{color:#09090b;background:#ffd23f;border-color:#ffd23f;transform:rotate(-2deg)}
.kwb{display:inline-flex;align-items:center;gap:4px;font-size:7pt;font-weight:800;letter-spacing:.12em;color:#ff4d5a;background:#1f0d10;border:1px solid #4a1a1f;border-radius:99px;padding:2px 9px}
.kwb.free{color:#6ee7a0;background:#0d1f14;border-color:#1f4a2c}
.phone{position:relative;width:1.05in;height:1.86in;flex:0 0 1.05in;border-radius:14px;border:2px solid #3a3a44;background:linear-gradient(170deg,#1a1a20,#0b0b0e 60%,#2a0d11);overflow:hidden;box-shadow:0 6px 18px rgba(229,34,47,.25)}
.notch{position:absolute;top:5px;left:50%;margin-left:-14px;width:28px;height:4px;border-radius:4px;background:#2a2a31}
.ph-ai{position:absolute;top:13px;left:7px;font-size:5pt;font-weight:800;letter-spacing:.15em;color:#9a9aa6;border:1px solid #3a3a44;border-radius:3px;padding:0 3px}
.ph-hook{position:absolute;top:30px;left:7px;right:7px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:6pt;line-height:1.3;color:#ff4d5a;font-weight:700;text-shadow:0 0 8px rgba(229,34,47,.7)}
.cur{display:inline-block;width:3px;height:7px;background:#ff4d5a;margin-left:2px;vertical-align:middle}
.ph-cap{position:absolute;left:0;right:0;top:62%;text-align:center;font-weight:900;font-size:11pt;color:#fff;letter-spacing:.03em;text-shadow:0 2px 6px #000}
.ph-bar{position:absolute;left:7px;right:7px;bottom:8px;height:2px;background:#33333a}
.ph-bar i{display:block;width:38%;height:2px;background:#e5222f}
.ph-side{position:absolute;right:4px;bottom:20px;display:flex;flex-direction:column;gap:5px}
.ph-side b{display:block;width:7px;height:7px;border-radius:50%;background:#4a4a55}
.lbl{display:block;color:#9a9aa6;font-weight:700;font-size:6.5pt;letter-spacing:.16em;text-transform:uppercase;margin-bottom:2px}
.lbl.sec{margin:10px 0 4px;color:#ff4d5a}
.lines{position:relative}
.lines::before{content:'';position:absolute;left:8px;top:10px;bottom:10px;width:2px;background:linear-gradient(#e5222f,#4a1a1f)}
.ln{display:flex;gap:10px;padding:4px 0;font-size:10.5pt;line-height:1.38;color:#e8e8ee}
.ln i{position:relative;z-index:1;flex:0 0 18px;height:18px;border-radius:50%;background:#e5222f;color:#fff;font-style:normal;font-size:7.5pt;font-weight:800;text-align:center;line-height:18px;margin-top:1px;box-shadow:0 0 0 3px #09090b}
.ln.cta i{background:#fff;color:#09090b}
.ln.cta span{font-weight:700;color:#fff;background:#1f0d10;border:1px solid #4a1a1f;border-radius:7px;padding:4px 9px;margin-left:-2px}
p{margin:.15em 0;color:#cfcfd8;font-size:8.8pt;line-height:1.38}
p.tg{color:#ff8a93}
.two{display:grid;grid-template-columns:1fr;gap:5px;margin-top:8px}
.blk{border-left:2px solid #2e2e36;padding-left:8px}
.note{margin-top:7px;font-size:7.8pt;color:#d8c9a8;background:#1c1810;border:1px solid #3a321c;border-radius:6px;padding:4px 8px}
.ctabar{position:absolute!important;left:.36in;right:.36in;bottom:.27in;display:flex;align-items:center;gap:10px;background:linear-gradient(90deg,#2a0d11,#14080a);border:1px solid #5a1f26;border-radius:12px;padding:8px 12px}
.ctabar.free{background:linear-gradient(90deg,#0e2616,#0a140e);border-color:#1f4a2c}
.ctabar .ic{width:34px;height:34px;border-radius:50%;background:#e5222f;display:flex;align-items:center;justify-content:center;color:#fff;flex:0 0 34px}
.ctabar.free .ic{background:#2d9b5c}
.ctabar small{display:block;font-size:5.8pt;letter-spacing:.16em;color:#9a9aa6;font-weight:700}
.ctabar .c1 b{font-size:13pt;letter-spacing:.06em;color:#fff;font-weight:900}
.ctabar .arr{color:#ff4d5a;font-size:14pt}
.ctabar.free .arr{color:#6ee7a0}
.ctabar .c2{flex:1;min-width:0}
.ctabar .c2 b{display:block;font-size:8.8pt;color:#fff;line-height:1.2}
.ctabar .c2 span{display:block;font-size:7pt;color:#9a9aa6}
ul{margin:.3em 0;padding-left:16px}li{margin:.22em 0;font-size:9pt;color:#d8d8e0}
li::marker{color:#e5222f}
.cover{background:radial-gradient(ellipse at 80% 100%,rgba(229,34,47,.4),transparent 60%),#09090b!important}
.cover .grid{position:absolute!important;inset:0;background-image:linear-gradient(#17171c 1px,transparent 1px),linear-gradient(90deg,#17171c 1px,transparent 1px);background-size:.4in .4in;opacity:.7}
.brand{letter-spacing:.5em;color:#e5222f;font-weight:800;font-size:11pt;margin:.35in 0 .15in}
.cphones{position:absolute!important;left:0;right:0;bottom:.35in;height:3.2in}
.cphones .phone{position:absolute;bottom:0}
.rbar{position:absolute!important;left:-.2in;right:-.2in;bottom:2.6in;height:.14in;background:#e5222f;transform:rotate(-4deg);opacity:.9}
.chart{margin-top:6px}
.crow{display:grid;grid-template-columns:.62in 1fr .5in;gap:6px;align-items:center;padding:3px 0;border-bottom:1px solid #1d1d22;font-size:7.6pt}
.crow .tp{font-size:6pt;font-weight:800;letter-spacing:.12em;color:#9a9aa6;text-transform:uppercase}
.crow .ph{color:#e4e4ea;line-height:1.25}
.crow .bar{height:5px;border-radius:3px;background:linear-gradient(90deg,#e5222f,#ff4d5a);margin-top:3px}
.crow .v{text-align:right;font-weight:800;color:#fff;font-size:7.6pt}
.crow .v i{display:inline-block;width:6px;height:6px;border-radius:50%;margin-left:4px}
.legend{font-size:6.8pt;color:#9a9aa6;margin-top:6px}
.legend i{display:inline-block;width:6px;height:6px;border-radius:50%;margin:0 3px 0 8px}
.idx{display:grid;grid-template-columns:1fr 1fr;gap:4px 14px;margin-top:6px}
.idx div{display:flex;gap:6px;align-items:center;padding:3px 0;border-bottom:1px solid #1d1d22;font-size:8pt;line-height:1.2}
.idx b{color:#ff4d5a;min-width:24px;font-size:7.5pt}
.idx svg{flex:0 0 12px;color:#6b6b76}
.panels{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px}
.panel{border-radius:10px;padding:10px 12px}
.panel.do{background:#0c1a11;border:1px solid #1f4a2c}.panel.dont{background:#1a0c0e;border:1px solid #4a1a1f}
.panel h3{margin:0 0 4px;font-size:10pt;text-transform:uppercase;letter-spacing:.1em}
.panel.do h3{color:#6ee7a0}.panel.dont h3{color:#ff4d5a}
.panel li{font-size:8.2pt}
.flow{display:flex;align-items:stretch;gap:5px;margin:10px 0}
.flow div{flex:1;border:1px solid #2e2e36;background:#111116;border-radius:9px;padding:8px 6px;text-align:center;font-size:7.2pt;line-height:1.25}
.flow b{display:block;font-size:8pt;color:#fff;margin-bottom:2px}
.flow .a{color:#ff4d5a;align-self:center;flex:0 0 auto;border:0;background:none;padding:0;font-size:12pt}
.flow div.hot{border-color:#e5222f;background:#1f0d10}
table{width:100%;border-collapse:collapse;font-size:7.8pt;margin-top:6px}
th,td{text-align:left;padding:4px 5px;border-bottom:1px solid #26262c;vertical-align:top}
th{color:#9a9aa6;font-size:6.3pt;letter-spacing:.1em;text-transform:uppercase}
.pill{font-weight:800;letter-spacing:.1em;font-size:6.8pt;background:#1f0d10;border:1px solid #4a1a1f;color:#ff4d5a;padding:2px 7px;border-radius:99px}
.pill.free{background:#0d1f14;border-color:#1f4a2c;color:#6ee7a0}
h3{font-size:11pt;margin:.2em 0 .3em;text-transform:uppercase}
'''

def numval(s):
    m = re.search(r'[\d,]+', s); return int(m.group().replace(',','')) if m else 0
def compcolor(c):
    n = numval(c)
    return '#6ee7a0' if n < 25 else '#ffd23f' if n < 40 else '#ff4d5a'
def kwpage(chunk, first, mx):
    rows = ''.join(f'<div class="crow"><div class="tp">{e(r[0])}</div><div class="ph">{e(r[1])}<div class="bar" style="width:{max(4,round(100*numval(r[2])/mx))}%"></div></div><div class="v">{e(r[2].split(" ")[0])}<i style="background:{compcolor(r[3])}"></i></div></div>' for r in chunk)
    intro = '<p>Estimated monthly <b>YouTube</b> searches (vidIQ, 12 Oct 2026). Instagram and TikTok volume is not available, so use this as a guide to the words, not exact reach. Bar = searches. Dot = competition.</p>' if first else '<p>Put the main phrase in five places: the first spoken sentence, the on-screen hook, the first line of the caption, 3-5 hashtags, and the file name or alt text.</p>'
    return f'''<section class="pg"><div class="code">KEYWORD BANK {"1/2" if first else "2/2"}</div><h2>What people type</h2>{intro}
<div class="chart">{rows}</div><div class="legend">Competition: <i style="background:#6ee7a0"></i>low (&lt;25) <i style="background:#ffd23f"></i>medium <i style="background:#ff4d5a"></i>high (40+)</div></section>'''

mx = max(numval(r[2]) for r in bank)
cover = f'''<section class="pg cover"><div class="grid"></div><div class="brand">WOLFE</div><div class="code">REEL SCRIPT LIBRARY</div>
<h1>22 reel scripts<br>built on <b>real search words</b></h1>
<p style="font-size:11pt;max-width:3.6in">Hook, spoken lines, caption, hashtags and a comment keyword for each script. Free guide first, paid guide second.</p>
<div class="rbar"></div>
<div class="cphones">{phone(a[6]["hook"],"OKAY",1.25,-8,"left:.15in;bottom:.1in")}{phone(b[4]["hook"],"RED FLAG",1.45,0,"left:1.95in;bottom:.35in;z-index:3")}{phone(a[4]["hook"],"ROMANCE",1.25,8,"left:3.85in;bottom:.1in")}</div>
<p style="position:absolute;bottom:.12in;left:.36in;color:#9a9aa6;font-size:7.5pt">Dorian Wolfe is an AI-generated character, not a real person.</p></section>'''
idx_items = ''.join(f'<div><b>{e(d["code"])}</b>{icon(d["kw"],12)}<span>{e(cap(d["title"]))}</span></div>' for d in a+b)
how = f'''<section class="pg"><div class="code">START HERE</div><h2>How to use this library</h2>
<div class="flow"><div><b>1 · Hook</b>red text on screen</div><div class="a">&#10140;</div><div><b>2 · Lines</b>read in order</div><div class="a">&#10140;</div><div><b>3 · Caption</b>+ hashtags</div><div class="a">&#10140;</div><div class="hot"><b>4 · Keyword</b>comment CTA</div></div>
<ul><li>Each script is one page: the on-screen hook, then the words you say, <b>one line per row</b>.</li>
<li>Read the lines into the locked voice (Brian), in order. The last line is the comment-keyword call to action.</li>
<li>Put the free keyword (SCAM or TEXTS) on at least half of your posts.</li></ul>
<h3 style="margin-top:14px">All 22 scripts</h3><div class="idx">{idx_items}</div></section>'''
rules = '''<section class="pg"><div class="code">RULES</div><h2>Rules for every post</h2><div class="panels">
<div class="panel do"><h3>&#10003; Do</h3><ul>
<li>Say "AI character" in the bio and in a pinned comment.</li><li>Label message examples "for example".</li>
<li>Say "try" and "practise", not "this will work".</li><li>Add the 988 line on sad or hopeless topics (US).</li>
<li>Use meme formats with your own clips and sound.</li></ul></div>
<div class="panel dont"><h3>&#10007; Don't</h3><ul>
<li>Tell personal stories ("my ex", "I dated 100 women").</li><li>Promise a date, a partner or a reply.</li>
<li>Invent numbers or reviews. Only FTC ($2.4B, people 60+, all fraud) and Pew (64% of men, all ages) are checked.</li>
<li>Use another person's clip, or trending audio outside the app.</li><li>Make medical, legal or financial claims.</li>
<li>Joke at a person or group.</li></ul></div></div>
<div class="note" style="margin-top:14px"><b>Reel 1 fix.</b> The old Reel 1 says "comment PLAYBOOK, free guide". The Playbook is paid. Change the keyword to TEXTS, or say "I'll send you the link".</div></section>'''
frows = ''.join(f'<tr><td><span class="pill{" free" if k in FREE else ""}">{k}</span></td><td>{e(v[0])}</td><td>{e(v[1])}</td></tr>' for k,v in KWMAP.items())
funnel = f'''<section class="pg"><div class="code">FUNNEL</div><h2>Comment keyword → reply</h2>
<div class="flow"><div><b>Reel</b>hook + lines</div><div class="a">&#10140;</div><div class="hot"><b>Comment</b>TEXTS / SCAM...</div><div class="a">&#10140;</div><div><b>Auto-DM</b>free guide first</div><div class="a">&#10140;</div><div><b>Offer</b>paid guide</div></div>
<table><thead><tr><th>Keyword</th><th>First reply</th><th>Then offer</th></tr></thead><tbody>{frows}</tbody></table>
<p style="margin-top:12px">Every DM carries: "Dorian Wolfe is an AI-generated character. General information. 7-day refund."</p>
<p style="margin-top:12px;color:#9a9aa6;font-size:7.5pt">General information for adults. Not therapy, medical, legal or financial advice. No result is guaranteed. In the US, call or text 988 if you feel hopeless.</p></section>'''
body = cover+how+rules+kwpage(bank[:15],True,mx)+kwpage(bank[15:],False,mx)+''.join(page_script(d) for d in a+b)+funnel
(here/'print.html').write_text(f'<!doctype html><meta charset="utf-8"><title>WOLFE Reel Script Library</title><style>{css}</style>{body}')
js = f"""const {{chromium}}=require('/opt/node22/lib/node_modules/playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']}});const p=await b.newPage();await p.goto('file://{here}/print.html');await p.pdf({{path:'{here}/wolfe-reel-script-library.pdf',width:'6in',height:'9in',printBackground:true,preferCSSPageSize:true}});await b.close()}})()"""
(here/'_pdf.js').write_text(js)
subprocess.run(['node',str(here/'_pdf.js')],check=True)
(here/'_pdf.js').unlink()
print('ok')
