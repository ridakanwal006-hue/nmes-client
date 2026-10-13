#!/usr/bin/env python3
"""Builds WOLFE-research-book.pdf (7x10in, designed pages) from the research markdown files.
Run: NODE_PATH=/opt/node22/lib/node_modules python3 -I build_book.py"""
import re, subprocess, pathlib, html, sys
here = pathlib.Path(__file__).resolve().parent
root = here.parent
sys.path.insert(0, str(root/'products/build'))
rd = lambda p: pathlib.Path(p).read_text().strip()
def md(text):
    return subprocess.run(['pandoc','-f','gfm-tex_math_dollars','-t','html','--wrap=none'],input=text,capture_output=True,text=True,check=True).stdout
esc = html.escape

# ART (inline SVG) from art.js, exported via node
import json
art = json.loads(subprocess.run(['node','-e',"console.log(JSON.stringify(require('%s/products/build/art.js').art))"%root],capture_output=True,text=True,check=True).stdout)

all_md = rd(here/'ALL-RESEARCH.md')
def section(a, b=None):
    i = all_md.index(a); j = all_md.index(b, i) if b else len(all_md); return all_md[i:j]
summ = {
 'A1': ('Pain points', 'Men 40+ ka dukh', section('## A1.','## A2.'), 'umbrella'),
 'A2': ('Psychology', 'Mard kaise sochte aur baat karte hain', section('## A2.','## A3.'), 'bubbles'),
 'A3': ('35+ baat-cheet', 'Mard aur aurat, USA/Canada/UK', section('## A3.','## A4.'), 'coffee'),
 'A4': ('USA / Canada / UK', 'Helpline aur scam report', section('## A4.','## A5.'), 'shield'),
 'A5': ('Competitors', 'Kaun kya bech raha hai', section('## A5.','\n---\n'), 'path'),
}
def strip_h(t): return re.sub(r'^## .*\n','',t,count=1).strip()

parts = [
 ('1','Competitors','Kaun kya bech raha hai, kitne mein, aur jagah kahan khali hai.','path', rd(here/'competitors-men-over-40.md')),
 ('2','First scan','Pehle scan ke shuruati pain points.','door', rd(here/'older-men-problems.md')),
 ('3','Pain points report','40+ mardon ka dukh, har platform se. Kya mazboot saboot hai, kya sirf kahani.','umbrella', rd(root/'reports/Men over 40 pain points.md')),
 ('4','Dating psychology report','Mard kaise sochte aur aapas mein baat karte hain; pehli aur doosri date; dar aur dealbreaker.','bubbles', rd(root/'reports/Men over 40 dating psychology.md')),
 ('5','35+ conversation psychology','Baat karna kyun mushkil hota hai, kaun kya pooche, aur research kya kehti hai (mard aur aurat).','coffee', rd(here/'conversation-psychology-35plus-both.md')),
 ('6','USA / Canada / UK resources','Helpline, scam reporting, dating customs. Search results se liye gaye: check karein.','shield', rd(here/'regional-resources-us-ca-uk.md')),
]

# evidence chart from pain-points table
pain = rd(root/'reports/Men over 40 pain points.md')
rows = []
for ln in pain.splitlines():
    c = [x.strip() for x in ln.strip().strip('|').split('|')]
    if len(c) >= 3 and c[0].isdigit():
        ev = c[2].lower(); sc = 3 if ev.startswith('strong') else 2 if ev.startswith('medium') else 1
        rows.append((c[0], re.sub(r'\*\*','',c[1]), sc, c[2]))
def chart():
    lab = {3:'Strong evidence',2:'Medium',1:'Anecdotal / thin'}; col = {3:'#34d27b',2:'#ffc83d',1:'#ff4d5a'}
    return '<div class="chart"><h3>Evidence behind each pain point</h3>'+''.join(
      f'<div class="cr"><span class="n">{n}</span><span class="t">{esc(t)}</span><span class="b"><i style="width:{sc/3*100:.0f}%;background:{col[sc]}"></i></span><span class="l" style="color:{col[sc]}">{lab[sc]}</span></div>' for n,t,sc,_ in rows)+'<p class="note">Bar = how well the evidence holds up (my ranking from the report, not a measured frequency). Full table in the report.</p></div>'

css = '''
@page{size:7in 10in;margin:.7in .6in .75in .6in;background:#09090b;
 @bottom-center{content:counter(page);font:600 8pt Inter;color:#6d6d78}
 @bottom-left{content:"WOLFE RESEARCH";font:800 7pt Inter;letter-spacing:.25em;color:#e5222f}}
@page cover{margin:0;background:#09090b;@bottom-center{content:none}@bottom-left{content:none}}
@page opener{margin:0;background:#09090b;@bottom-center{content:none}@bottom-left{content:none}}
*{box-sizing:border-box}
html{background:#09090b}
body{margin:0;font-family:Inter,sans-serif;color:#e4e4ea;font-size:9.2pt;line-height:1.55}
a{color:#ff8a93;text-decoration:none;word-break:break-word}
b,strong{color:#fff}
.cover{page:cover;width:7in;height:10in;position:relative;overflow:hidden;background:radial-gradient(ellipse at 70% 95%,#4a0a10 0%,transparent 60%),linear-gradient(180deg,#0b0b0e,#060607);break-after:page;padding:.8in .7in}
.cover .brand{font-weight:800;font-size:10pt;letter-spacing:.45em;color:#e5222f}
.cover .bar{height:6px;background:#e5222f;margin:.55in 0 .4in;box-shadow:0 0 22px rgba(229,34,47,.7)}
.cover h1{font-family:"Inter Display",Inter;font-weight:900;font-size:46pt;line-height:.98;text-transform:uppercase;color:#fff;margin:0;border:0;padding:0}
.cover h1 span{color:#ff4d5a}
.cover p{max-width:4in;color:#c9c9d2;font-size:10.5pt;margin-top:.3in}
.cover .art{position:absolute;right:.2in;bottom:.9in;width:4.6in;opacity:.95}
.cover .art svg{width:100%}
.cover .ft{position:absolute;left:.7in;bottom:.5in;font-size:7.5pt;letter-spacing:.2em;color:#9a9aa6;text-transform:uppercase}
.opener{page:opener;width:7in;height:10in;position:relative;overflow:hidden;break-before:page;break-after:page;background:radial-gradient(ellipse at 80% 100%,rgba(229,34,47,.35),transparent 60%),#09090b;padding:.9in .7in}
.opener .num{font-family:"Inter Display",Inter;font-weight:900;font-size:150pt;line-height:1;color:transparent;-webkit-text-stroke:1.5px #3a1a1e}
.opener h2{font-family:"Inter Display",Inter;font-weight:900;font-size:34pt;line-height:1;text-transform:uppercase;color:#fff;margin:.1in 0 .2in}
.opener p{max-width:4.4in;font-size:11pt;color:#c9c9d2}
.opener .art{position:absolute;right:.4in;bottom:.9in;width:4.4in}
.opener .art svg{width:100%}
.opener .bar{height:5px;background:#e5222f;width:1.4in;margin:.2in 0}
h1{font-family:"Inter Display",Inter;font-weight:900;font-size:21pt;line-height:1.1;margin:0 0 .2in;text-transform:uppercase;color:#fff;border-bottom:3px solid #e5222f;padding-bottom:.1in;break-after:avoid}
h2{font-family:"Inter Display",Inter;font-weight:900;font-size:14pt;line-height:1.15;margin:.3in 0 .1in;color:#fff;border-left:4px solid #e5222f;padding-left:9px;break-after:avoid}
h3{font-size:10.5pt;color:#ff4d5a;margin:.2in 0 .06in;break-after:avoid}
h4{font-size:9.5pt;color:#fff;margin:.15in 0 .04in;break-after:avoid}
p{margin:0 0 .11in}
ul,ol{margin:0 0 .13in;padding-left:.22in}li{margin-bottom:3px}li::marker{color:#e5222f}
table{width:100%;border-collapse:collapse;margin:.1in 0 .2in;font-size:7.4pt;line-height:1.4;table-layout:auto}
th{background:#1d0c0f;color:#ff8a93;text-align:left;font-size:6.6pt;letter-spacing:.1em;text-transform:uppercase;padding:5px 6px;border-bottom:2px solid #e5222f}
td{overflow-wrap:anywhere;padding:5px 6px;border-bottom:1px solid #26262c;vertical-align:top}
tr{break-inside:avoid}
blockquote{margin:.1in 0;padding:.08in .15in;border-left:3px solid #e5222f;background:#14141a;color:#cfcfd8}
hr{border:0;border-top:1px solid #26262c;margin:.2in 0}
code{font-size:8pt;background:#1b1b21;padding:1px 4px;border-radius:3px}
.sum{break-before:page}
.sum h2{border:0;padding:0;font-size:20pt;text-transform:uppercase;border-bottom:3px solid #e5222f;padding-bottom:.08in;margin-top:0}
.sum .sub{color:#9a9aa6;font-size:8pt;letter-spacing:.2em;text-transform:uppercase;margin-bottom:.15in}
.sum ol{list-style:none;padding:0;counter-reset:c}
.sum ol li{counter-increment:c;position:relative;padding:.09in .12in .09in .5in;margin-bottom:.07in;background:#111116;border:1px solid #26262c;border-radius:9px;break-inside:avoid}
.sum ol li::before{content:counter(c);position:absolute;left:.12in;top:.09in;width:.26in;height:.26in;border-radius:50%;background:#e5222f;color:#fff;font-weight:800;font-size:8.5pt;display:flex;align-items:center;justify-content:center}
.sum .ic{float:right;width:1.5in;margin:-.05in 0 .05in .2in;opacity:.9}
.sum .ic svg{width:100%}
.chart{margin:.2in 0;padding:.15in;background:#101015;border:1px solid #26262c;border-radius:10px;break-inside:avoid}
.chart h3{margin:0 0 .1in}
.cr{display:grid;grid-template-columns:.22in 2.2in 1fr .95in;gap:6px;align-items:center;padding:3px 0;font-size:8pt}
.cr .n{color:#ff4d5a;font-weight:800}.cr .t{color:#e4e4ea;line-height:1.25}
.cr .b{height:7px;border-radius:4px;background:#26262c;display:block}.cr .b i{display:block;height:7px;border-radius:4px}
.cr .l{font-size:7pt;font-weight:700}
.note{font-size:7.5pt;color:#9a9aa6;margin-top:.08in}
.how{break-before:page}
.how .grid{display:grid;grid-template-columns:1fr 1fr;gap:.1in;margin:.1in 0}
.how .box{background:#111116;border:1px solid #26262c;border-radius:10px;padding:.12in}
.how .box b{display:block;color:#ff4d5a;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;margin-bottom:3px}
.legend{display:flex;gap:.12in;margin:.1in 0}
.legend span{font-size:8pt;font-weight:700;padding:3px 10px;border-radius:99px;border:1px solid}
'''
out = ['<!doctype html><html><head><meta charset="utf-8"><title>WOLFE Research Book</title><style>'+css+'</style></head><body>']
out.append(f'''<section class="cover"><div class="brand">WOLFE</div><div class="bar"></div>
<h1>The research<br><span>book</span></h1>
<p>Men and women dating again after 35 in the USA, Canada and the UK. Pain points, psychology, conversation, competitors and safety resources, in one designed book. Roman Urdu summary first.</p>
<div class="art">{art['bubbles']}</div><div class="ft">By Dorian Wolfe, an AI-generated character</div></section>''')
how_items = ''.join(f'<div class="box"><b>{n}. {esc(t)}</b>{esc(d)}</div>' for n,t,d,_,_ in parts)
out.append(f'''<section class="how"><h1 style="margin-top:0">How to read this book</h1>
<p><b>Pehle Roman Urdu khulasa</b> (5 pages), phir 6 poore reports (English). Har report se pehle ek opener page hai.</p>
<div class="legend"><span style="color:#34d27b;border-color:#1f4a2c">Strong: meta-analysis, large survey</span><span style="color:#ffc83d;border-color:#4a3f1f">Medium: single study, dated</span><span style="color:#ff4d5a;border-color:#4a1a1f">Anecdotal: blogs, opinion</span></div>
<div class="grid">{how_items}</div>
<h2>Sab se zaroori hadd (limits)</h2>
<ul><li>Reddit band tha, Instagram aur TikTok ke comments nahi mile, aur bohat si websites khulti hi nahi thi (DNS error).</li>
<li>Zyada tar numbers <b>search summaries</b> se aaye hain, poore pages se nahi. Camera par koi number bolne se pehle asal source se check karein.</li>
<li>35+ ki pehli baat-cheet par almost koi research hai hi nahi. Reports mein yeh saaf likha hai.</li>
<li>Helpline numbers search results se liye gaye, official sites kholkar nahi. Becne se pehle check karein.</li></ul></section>''')
for key,(title,sub,body,a) in summ.items():
    out.append(f'<section class="sum"><div class="sub">Roman Urdu khulasa · {esc(sub)}</div><div class="ic">{art[a]}</div>{md(body)}</section>')
for n,t,d,a,body in parts:
    out.append(f'<section class="opener"><div class="num">{n}</div><div class="bar"></div><h2>{esc(t)}</h2><p>{esc(d)}</p><div class="art">{art[a]}</div></section>')
    if n=='3': out.append(chart())
    out.append(f'<section class="part">{md(body)}</section>')
out.append('</body></html>')
(here/'_book.html').write_text('\n'.join(out))
js=f"""const {{chromium}}=require('/opt/node22/lib/node_modules/playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']}});const p=await b.newPage();await p.goto('file://{here}/_book.html');await p.pdf({{path:'{here}/WOLFE-research-book.pdf',width:'7in',height:'10in',printBackground:true,preferCSSPageSize:true}});await b.close()}})()"""
(here/'_b.js').write_text(js); subprocess.run(['node',str(here/'_b.js')],check=True); (here/'_b.js').unlink()
print('ok')
