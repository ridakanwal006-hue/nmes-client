const fs=require('fs'),path=require('path');
const {chromium}=require('playwright');
const OUT='/home/user/nmes-client/products/over40';
const ids=['wolfe-scam-red-flag-checklist','wolfe-dating-again-starter-guide','wolfe-profile-fixer-40-plus','wolfe-30-day-confidence-workbook','wolfe-scam-proof-dating-guide','wolfe-80-conversation-starters','wolfe-rejection-resilience-guide'];
const tags=['FREE CHECKLIST','STARTER GUIDE','PROFILE FIXER','WORKBOOK','GUIDE FOR 50+','PRINTABLE CARDS','MINI GUIDE'];
const b64=id=>'data:image/png;base64,'+fs.readFileSync(path.join(OUT,id+'-cover.png')).toString('base64');
const base=`*{box-sizing:border-box}body{margin:0;background:#07070a;font-family:Inter,sans-serif;color:#fff;overflow:hidden}
.glow{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 70%,rgba(229,34,47,.35),transparent 60%)}
.book{position:absolute;transform-style:preserve-3d}
.book img{width:100%;display:block;border-radius:3px 8px 8px 3px;box-shadow:0 40px 60px rgba(0,0,0,.8),0 0 60px rgba(229,34,47,.25)}
.book:before{content:"";position:absolute;left:0;top:0;bottom:0;width:14px;background:linear-gradient(90deg,rgba(255,255,255,.28),rgba(0,0,0,.35));border-radius:3px 0 0 3px;z-index:2}
.brand{position:absolute;font-weight:800;letter-spacing:.4em;color:#e5222f}
.bar{position:absolute;height:6px;background:#e5222f;box-shadow:0 0 22px rgba(229,34,47,.8)}`;
const single=(id,tag)=>`<html><head><meta charset=utf-8><style>${base}</style></head><body style="width:1080px;height:1080px;position:relative">
<div class=glow></div><div class=brand style="left:70px;top:64px;font-size:22px">WOLFE</div>
<div class=bar style="left:70px;right:70px;top:110px"></div>
<div class=book style="left:300px;top:170px;width:480px;transform:perspective(1600px) rotateY(-16deg) rotateX(2deg)"><img src="${b64(id)}"></div>
<div style="position:absolute;left:0;right:0;bottom:64px;text-align:center;font-weight:800;letter-spacing:.35em;font-size:22px;color:#ff4d5a">${tag}</div></body></html>`;
const bundle=`<html><head><meta charset=utf-8><style>${base}</style></head><body style="width:1080px;height:1350px;position:relative">
<div class=glow></div><div class=brand style="left:70px;top:64px;font-size:22px">WOLFE</div>
<div style="position:absolute;left:70px;top:105px;font-size:20px;letter-spacing:.2em;color:#9a9aa6">BY DORIAN WOLFE</div>
<div class=bar style="left:70px;right:70px;top:160px"></div>
<div style="position:absolute;left:70px;top:200px;font-family:'Inter Display';font-weight:900;font-size:78px;line-height:1;text-transform:uppercase">Dating After 40<br><span style="color:#ff4d5a">Starter</span><br>Toolkit</div>
${ids.map((id,i)=>`<div class=book style="left:${30+i*145}px;top:${640-(i%2)*40}px;width:200px;transform:perspective(1400px) rotateY(-14deg);z-index:${i}"><img src="${b64(id)}"></div>`).join('')}
<div style="position:absolute;left:0;right:0;bottom:60px;text-align:center;font-weight:800;letter-spacing:.3em;font-size:22px;color:#9a9aa6">7 TOOLS · GUIDE · WORKBOOK · SCAM SAFETY</div></body></html>`;
(async()=>{const br=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(let i=0;i<ids.length;i++){const p=await br.newPage({viewport:{width:1080,height:1080}});await p.setContent(single(ids[i],tags[i]));await p.screenshot({path:path.join(OUT,ids[i]+'-mockup.png')});}
const p=await br.newPage({viewport:{width:1080,height:1350}});await p.setContent(bundle);await p.screenshot({path:path.join(OUT,'wolfe-over40-toolkit-mockup.png')});
await br.close();console.log('done')})();
