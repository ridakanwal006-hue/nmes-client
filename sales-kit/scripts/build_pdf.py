#!/usr/bin/env python3
"""Builds wolfe-reel-script-library.pdf (6x9in, one script per page) from the script packs.
Run: NODE_PATH=/opt/node22/lib/node_modules python3 -I build_pdf.py"""
import subprocess, html, pathlib
here = pathlib.Path(__file__).resolve().parent
src = open(here/'build.py').read().split("data = dict")[0]
exec(src)
KWMAP = {'SCAM':('Free Scam Red-Flag Checklist','Scam-Proof Dating Guide $12'),'TEXTS':('Free 50 Texts That Get Replies','Conversation Playbook $17'),
 'STARTER':('Starter Guide $14','Toolkit bundle $39'),'PROFILE':('Profile Fixer for 40+ $12','Starter Guide $14'),
 'CHALLENGE':('30-Day Confidence Challenge $12','Rejection & Resilience $8'),'QUIET':('She Went Quiet $9','Rejection & Resilience $8'),
 'REJECT':('Rejection & Resilience $8','30-Day Confidence Challenge $12'),'DATE':('First Date Blueprint $12','80 Conversation Starters $9'),
 'ASK':('80 Conversation Starters $9','Conversation Playbook $17'),'PLAYBOOK':('The Conversation Playbook $17','Complete Library $59')}
e = lambda s: html.escape(str(s or ''))
cap = lambda s: s[:1].upper()+s[1:]
def page_script(d):
    free = d['kw'] in FREE
    last = len(d['script'])-1
    lines = ''.join(f'<div class="ln{" cta" if k==last else ""}"><i>{k+1}</i><span>{e(l)}</span></div>' for k,l in enumerate(d['script']))
    sub = (e(d['fmt'])+(' · pain: '+e(d['pain']) if d['pain'] else '')) if d['pack']=='b' else e(cap(d['product']))
    kw = f'<div class="lbl">Search words</div><p>{e(d["keywords"])}</p>' if d['keywords'] else ''
    cp = f'<div class="lbl">Caption</div><p>{e(d["caption"])}</p>' if d['caption'] else ''
    note = f'<div class="note">{e(cap(d["note"]))}</div>' if d['note'] else ''
    p1, p2 = KWMAP.get(d['kw'],('',''))
    return f'''<section class="pg"><div class="code">{e(d["code"])} · {"MEME PACK" if d["pack"]=="b" else "SEARCH PACK"}</div>
<h2>{e(cap(d["title"]))}</h2><div class="sub">{sub}</div>
<div class="hook"><small>1 · On-screen hook</small>{e(d["hook"])}</div>
<div class="lbl">2 · Say it, line by line</div><div class="lines">{lines}</div>
{kw}{cp}<div class="lbl">Hashtags</div><p>{e(d["tags"])}</p>{note}
<div class="foot"><span class="pill{" free" if free else ""}">COMMENT {e(d["kw"])}</span> <span>→ {e(p1)}, then {e(p2)}</span></div></section>'''

css = '''
@page{size:6in 9in;margin:0;background:#2e2e36}
*{box-sizing:border-box}
html,body{margin:0;background:#2e2e36;counter-reset:pg;color:#ececf0;font-family:Inter,system-ui,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{counter-increment:pg;background:#09090b;border:.17in solid #2e2e36;border-top:.17in solid #e5222f;width:6in;height:9in;padding:.42in .36in .4in;page-break-after:always;overflow:hidden;position:relative;font-size:10.5pt;line-height:1.45}
.pg:last-child{page-break-after:auto}
.code{font-size:7.5pt;font-weight:800;letter-spacing:.2em;color:#ff4d5a}
h1{font-size:34pt;line-height:1.02;margin:.3em 0;text-transform:uppercase;font-weight:900}
h1 b{color:#ff4d5a}
h2{font-size:19pt;line-height:1.15;margin:.2em 0 .1em;font-weight:800}
.sub{font-size:9pt;color:#9a9aa6;margin-bottom:10px}
.hook{margin:8px 0;background:#0d0d10;border:1px solid #4a1a1f;border-left:3px solid #e5222f;border-radius:6px;padding:8px 10px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:10pt;color:#ff4d5a;font-weight:700}
.hook small,.lbl{display:block;color:#9a9aa6;font-weight:700;font-size:7pt;letter-spacing:.15em;text-transform:uppercase;font-family:Inter,sans-serif;margin-bottom:2px}
.lbl{margin:11px 0 3px}
.lines{margin-top:2px}
.ln{display:flex;gap:10px;padding:6px 0;border-bottom:1px solid #222228;font-size:11.5pt;line-height:1.4;color:#e8e8ee}
.ln i{flex:0 0 17px;font-style:normal;font-size:8pt;font-weight:800;color:#ff4d5a;padding-top:3px}
.ln.cta{color:#fff;font-weight:700;border-bottom:0}
p{margin:.2em 0;color:#cfcfd8;font-size:9.5pt}
.note{margin-top:10px;font-size:8.5pt;color:#d8c9a8;background:#1c1810;border:1px solid #3a321c;border-radius:6px;padding:6px 9px}
.pg::after{content:'PAGE ' counter(pg);position:absolute;right:.36in;top:.16in;font-size:7pt;letter-spacing:.2em;color:#6b6b76;font-weight:700}
.foot{position:absolute;left:.36in;right:.36in;bottom:.3in;border-top:1px solid #2a2a31;padding-top:8px;font-size:8.5pt;color:#9a9aa6}
.pill{font-weight:800;letter-spacing:.1em;font-size:7.5pt;background:#1f0d10;border:1px solid #4a1a1f;color:#ff4d5a;padding:2px 8px;border-radius:99px;margin-right:4px}
.pill.free{background:#0d1f14;border-color:#1f4a2c;color:#6ee7a0}
.cover{background:radial-gradient(ellipse at 80% 100%,rgba(229,34,47,.35),transparent 60%),#09090b;display:flex;flex-direction:column;justify-content:center}
.brand{letter-spacing:.5em;color:#e5222f;font-weight:800;font-size:11pt;margin-bottom:22px}
ul{margin:.3em 0;padding-left:16px}li{margin:.25em 0;font-size:9.5pt;color:#d8d8e0}
li::marker{color:#e5222f}
table{width:100%;border-collapse:collapse;font-size:8pt}
th,td{text-align:left;padding:4px 5px;border-bottom:1px solid #26262c;vertical-align:top}
th{color:#9a9aa6;font-size:6.5pt;letter-spacing:.1em;text-transform:uppercase}
h3{font-size:12pt;margin:.2em 0 .4em;text-transform:uppercase}
.idx{columns:2;column-gap:20px;font-size:9pt}
.idx div{display:flex;gap:8px;padding:3px 0;border-bottom:1px solid #222228;break-inside:avoid}
.idx b{color:#ff4d5a;min-width:26px}
'''
cover = '''<section class="pg cover"><div class="brand">WOLFE</div><div class="code">REEL SCRIPT LIBRARY</div>
<h1>22 reel scripts<br>built on <b>real search words</b></h1>
<p style="font-size:12pt;max-width:4.2in">Hook, spoken lines, caption, hashtags and a comment keyword for each script. Free guide first, paid guide second.</p>
<p style="margin-top:20px;color:#9a9aa6;font-size:9pt">Dorian Wolfe is an AI-generated character, not a real person.</p></section>'''
idx_items = ''.join(f'<div><b>{e(d["code"])}</b><span>{e(cap(d["title"]))} <span style="color:#9a9aa6">· {e(d["kw"])}</span></span></div>' for d in a+b)
how = f'''<section class="pg"><div class="code">START HERE</div><h2>How to use this library</h2>
<ul><li>Each script is one page: the on-screen hook, then the words you say, <b>one line per row</b>.</li>
<li>Read the lines into the locked voice (Brian), in order. The last line is the comment-keyword call to action.</li>
<li>Copy the caption and the hashtags under the script.</li>
<li>Put the free keyword (SCAM or TEXTS) on at least half of your posts.</li></ul>
<h3 style="margin-top:14px">All scripts</h3><div class="idx">{idx_items}</div></section>'''
rules = '''<section class="pg"><div class="code">RULES</div><h2>Rules for every post</h2>
<h3 style="color:#6ee7a0;font-size:10pt">Do</h3><ul>
<li>Say "AI character" in the bio and in a pinned comment.</li><li>Label message examples "for example".</li>
<li>Say "try" and "practise", not "this will work".</li><li>Add the 988 line on sad or hopeless topics (US).</li>
<li>Use meme formats with your own clips and sound.</li></ul>
<h3 style="color:#ff4d5a;font-size:10pt;margin-top:12px">Don't</h3><ul>
<li>Tell personal stories ("my ex", "I dated 100 women").</li><li>Promise a date, a partner or a reply.</li>
<li>Invent numbers or reviews. Only the FTC ($2.4B, people 60+, all fraud) and Pew (64% of men, all ages) numbers are checked.</li>
<li>Use another person's clip, or trending audio outside the app.</li><li>Make medical, legal or financial claims.</li>
<li>Joke at a person or group. Joke with them, or at the common mistake.</li></ul>
<h3 style="margin-top:12px;font-size:10pt">Reel 1 fix</h3><p>The old Reel 1 says "comment PLAYBOOK, free guide". The Playbook is paid. Change the keyword to TEXTS, or say "I'll send you the link".</p></section>'''
def kwpage(chunk, first):
    rows = ''.join(f'<tr><td>{e(r[0])}</td><td>{e(r[1])}</td><td>{e(r[2])}</td><td>{e(r[3])}</td></tr>' for r in chunk)
    intro = '<p>Estimated monthly <b>YouTube</b> searches (vidIQ, 12 Oct 2026). Instagram and TikTok volume is not available, so use this as a guide to the words, not exact reach.</p>' if first else '<p>Put the main phrase in five places: the first spoken sentence, the on-screen hook, the first line of the caption, 3-5 hashtags, and the file name or alt text.</p>'
    return f'''<section class="pg"><div class="code">KEYWORD BANK {"1/2" if first else "2/2"}</div><h2>What people type</h2>{intro}
<table><thead><tr><th>Topic</th><th>Phrase</th><th>Searches/mo</th><th>Comp.</th></tr></thead><tbody>{rows}</tbody></table></section>'''
kwp = kwpage(bank[:15], True) + kwpage(bank[15:], False)
frows = ''.join(f'<tr><td><span class="pill{" free" if k in FREE else ""}">{k}</span></td><td>{e(v[0])}</td><td>{e(v[1])}</td></tr>' for k,v in KWMAP.items())
funnel = f'''<section class="pg"><div class="code">FUNNEL</div><h2>Comment keyword → reply</h2>
<table><thead><tr><th>Keyword</th><th>First reply</th><th>Then offer</th></tr></thead><tbody>{frows}</tbody></table>
<p style="margin-top:14px">Every DM carries: "Dorian Wolfe is an AI-generated character. General information. 7-day refund."</p>
<p style="margin-top:14px;color:#9a9aa6;font-size:8pt">General information for adults. Not therapy, medical, legal or financial advice. No result is guaranteed. In the US, call or text 988 if you feel hopeless.</p></section>'''
body = cover+how+rules+kwp+''.join(page_script(d) for d in a+b)+funnel
(here/'print.html').write_text(f'<!doctype html><meta charset="utf-8"><title>WOLFE Reel Script Library</title><style>{css}</style>{body}')
js = f"""const {{chromium}}=require('/opt/node22/lib/node_modules/playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']}});const p=await b.newPage();await p.goto('file://{here}/print.html');await p.pdf({{path:'{here}/wolfe-reel-script-library.pdf',width:'6in',height:'9in',printBackground:true,preferCSSPageSize:true}});await b.close()}})()"""
(here/'_pdf.js').write_text(js)
subprocess.run(['node',str(here/'_pdf.js')],check=True)
(here/'_pdf.js').unlink()
print('ok')
