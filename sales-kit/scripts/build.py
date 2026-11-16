#!/usr/bin/env python3
"""Builds sales-kit/scripts/index.html from the two script-pack markdown files.
Run: python3 -I build.py   (from this folder)"""
import re, json, html, pathlib
root = pathlib.Path(__file__).resolve().parents[2] / 'reels'
KW = ['SCAM','TEXTS','STARTER','PROFILE','CHALLENGE','QUIET','REJECT','DATE','ASK','PLAYBOOK']
FREE = {'SCAM','TEXTS'}

def parse(path, rx):
    txt = path.read_text()
    parts = re.split(r'\n(?=## (?:Script \d+|M\d+):)', txt)
    out = []
    for p in parts:
        m = re.match(r'## ((?:Script \d+|M\d+)):\s*(.+)', p)
        if not m: continue
        code, title = m.group(1), m.group(2).strip()
        kw = next((k for k in KW if re.search(r'\b'+k+r'\b', title)), '')
        lines = p.split('\n')[1:]
        d = dict(code=code.replace('Script ','S'), title=re.sub(r'\s*\((.*?)\)\s*$','',title), kw=kw, hook='', product='', script=[], caption='', tags='', keywords='', note='')
        if '(' in title and not kw: pass
        for ln in lines:
            if ln.startswith('Hook'):
                h = re.search(r'\*\*(.+?)\*\*', ln); d['hook'] = h.group(1) if h else ''
            elif ln.startswith('Product:'): d['product'] = ln[8:].strip()
            elif ln.startswith('> '): d['script'].append(ln[2:].strip())
            elif ln.startswith('Caption:'): d['caption'] = ln[8:].strip()
            elif ln.startswith('Hashtags:'): d['tags'] = ln[9:].strip()
            elif ln.startswith('Keywords:'):
                k = ln[9:]
                if 'Hashtags:' in k:
                    k, t = k.split('Hashtags:'); d['tags'] = t.strip()
                d['keywords'] = k.strip().rstrip('.')
            elif ln.startswith('Note:'): d['note'] = ln[5:].strip()
        d['title'] = re.sub(r'\s*\(([A-Z]+),?.*\)$','',d['title']) if kw else d['title']
        d['title'] = re.sub(r'\s*→\s*[A-Z]+.*$','',d['title']).strip()
        d['pack'] = 'a' if code.startswith('Script') else 'b'
        d['title'] = d['title'].strip('"')
        d['fmt'] = ''; d['pain'] = ''
        if d['pack']=='b':
            raw = title
            pm = re.search(r'\(pain:\s*(.+?)\)', raw); d['pain'] = pm.group(1) if pm else ''
            raw = re.sub(r'\(pain:.*?\)','',raw); raw = re.sub(r'\s*→\s*[A-Z]+.*$','',raw) if False else raw
            f, _, rest = raw.partition('→')
            d['fmt'] = f.strip().strip('"'); d['title'] = re.sub(r'\s*→.*$','',rest).strip() if False else rest.strip()
            d['title'] = re.sub(r'\s*→\s*[A-Z]+.*$','',d['title']).strip()
        out.append(d)
    return out

a = parse(root/'script-pack-by-product.md', 0)
b = parse(root/'script-pack-meme-painpoints.md', 0)
# keyword bank rows
bank = []
for ln in (root/'script-pack-by-product.md').read_text().split('\n'):
    c = [x.strip() for x in ln.strip().strip('|').split('|')]
    if len(c)==4 and c[0] not in ('Topic','---') and not c[0].startswith('---'):
        bank.append(c)
data = dict(scripts=a+b, bank=bank, free=sorted(FREE))
tpl = (pathlib.Path(__file__).parent/'template.html').read_text()
(pathlib.Path(__file__).parent/'index.html').write_text(tpl.replace('/*__DATA__*/null', json.dumps(data, ensure_ascii=False)))
print(len(a), 'pack A,', len(b), 'pack B,', len(bank), 'keyword rows')
