import subprocess, glob, re, os
files = sorted(glob.glob('/home/user/nmes-client/products/*.pdf')) + sorted(glob.glob('/home/user/nmes-client/products/over40/*.pdf'))
risky = {
 'guarantee/promise': r'\bguarantee[sd]?\b|\bwill (?:make|get) (?:her|you)\b|\balways works\b',
 'manipulation words': r'\bmake her\b|\bchase\b|\balpha\b|\bnegg?ing\b|\bpickup\b|\btrick(?:s)?\b',
 'medical terms': r'\btestosterone\b|\berectile\b|\bED\b|\bdosage\b|\bsupplement[s]?\b|\bcure[sd]?\b|\bdiagnos\w+\b|\bminoxidil\b|\bfinasteride\b',
 'money/legal advice': r'\binvest(?:ment|ing)?\b|\blegal advice\b|\bsue\b|\bcustody\b',
}
req = {'not-therapy disclaimer': r'not therapy|not medical|not therapy, medical', 'AI-generated disclosure': r'AI-generated'}
rows=[]; nums=[]; findings=[]
for f in files:
    t = subprocess.run(['pdftotext','-layout',f,'-'],capture_output=True,text=True).stdout
    name=os.path.basename(f).replace('wolfe-','').replace('.pdf','')
    n_pages=len(t.split('\f'))-1
    flags=[]
    for k,pat in risky.items():
        hits=[m for m in re.finditer(pat,t,re.I) if not any(x in re.sub(r'\s+',' ',t[max(0,m.start()-60):m.end()+60]).lower() for x in ['no result is guaranteed','not a guarantee','not guaranteed','no guarantee','no tricks','not chase',"don't chase",'do not chase','legal or financial advice','not therapy, medical, legal'])]
        if hits:
            ctx=[re.sub(r'\s+',' ',t[max(0,m.start()-45):m.end()+45]) for m in hits[:2]]
            flags.append((k,len(hits),ctx))
    missing=[k for k,pat in req.items() if not re.search(pat,t,re.I)]
    has988='988' in t
    for m in re.finditer(r'\$[\d.,]+ ?(?:billion|million)?|\b\d{1,3}(?:\.\d+)?%',t):
        nums.append((name,re.sub(r'\s+',' ',t[max(0,m.start()-50):m.end()+40])))
    rows.append((name,n_pages,flags,missing,has988))
out=['# Guidelines audit of the Wolfe products','',
 'Automated text check of every PDF against the project guidelines (honest claims, no manipulation, no medical or legal advice, AI disclosure, safety info). It finds words and patterns, not meaning, so read the flags yourself.','',
 '| Product | Pages | AI disclosure | Disclaimer | 988 helpline | Flagged words |','|---|---|---|---|---|---|']
for name,n,flags,missing,h in rows:
    out.append(f"| {name} | {n} | {'yes' if 'AI-generated disclosure' not in missing else '**MISSING**'} | {'yes' if 'not-therapy disclaimer' not in missing else 'no'} | {'yes' if h else 'no'} | {', '.join(f'{k} x{c}' for k,c,_ in flags) or 'none'} |")
out+=['','## Flagged text (check context)','']
for name,n,flags,missing,h in rows:
    for k,c,ctx in flags:
        for x in ctx: out.append(f'- **{name}** ({k}): ...{x}...')
out+=['','## Numbers to verify before publishing','','These figures appear in the products. Check each against its primary source.','']
seen=set()
for name,s in nums:
    key=(name,s[:60])
    if key in seen: continue
    seen.add(key); out.append(f'- **{name}**: ...{s}...')
open('/home/user/nmes-client/products/over40/GUIDELINES_AUDIT.md','w').write('\n'.join(out))
print('\n'.join(out[:20]))
