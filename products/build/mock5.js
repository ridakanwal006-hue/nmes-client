const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const OUT='/home/user/nmes-client/products/us-ca-uk';
const ids=['wolfe-scam-red-flag-checklist','wolfe-dating-again-starter-guide','wolfe-profile-fixer-40-plus','wolfe-30-day-confidence-workbook','wolfe-rejection-resilience-guide','wolfe-conversation-starters-35-plus','wolfe-dating-again-starter-guide-for-her','wolfe-profile-fixer-for-women-35-plus','wolfe-30-day-confidence-challenge-for-women'].map(x=>x+'-us-ca-uk');
const b64=id=>'data:image/png;base64,'+fs.readFileSync(path.join(OUT,id+'-cover.png')).toString('base64');
const row=(label,arr)=>`<div style="margin-top:34px"><div style="font-weight:800;letter-spacing:.3em;font-size:20px;color:#ff4d5a;margin-bottom:16px">${label}</div><div style="display:flex;gap:18px">${arr.map(id=>`<img src="${b64(id)}" style="width:160px;border-radius:3px 8px 8px 3px;box-shadow:0 18px 30px rgba(0,0,0,.8),0 0 30px rgba(229,34,47,.2)">`).join('')}</div></div>`;
const html=`<html><head><meta charset=utf-8><style>*{box-sizing:border-box}body{margin:0;width:1080px;height:1350px;background:#07070a;font-family:Inter,sans-serif;color:#fff;position:relative;overflow:hidden}.g{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 80%,rgba(229,34,47,.3),transparent 60%)}.w{position:relative;padding:60px 70px}</style></head><body><div class=g></div><div class=w>
<div style="font-weight:800;letter-spacing:.4em;color:#e5222f;font-size:22px">WOLFE</div>
<div style="height:6px;background:#e5222f;margin:24px 0 34px;box-shadow:0 0 22px rgba(229,34,47,.8)"></div>
<div style="font-weight:900;font-size:68px;line-height:1;text-transform:uppercase">Dating After 35+<br><span style="color:#ff4d5a">USA · Canada · UK</span></div>
<div style="color:#9a9aa6;margin-top:14px;font-size:20px;letter-spacing:.1em">9 GUIDES · FOR HIM · FOR HER · FOR EVERYONE</div>
${row('FOR HIM',[ids[1],ids[2],ids[3],ids[4]])}${row('FOR HER',ids.slice(6,9))}${row('FOR EVERYONE',[ids[5],ids[0]])}
</div></body></html>`;
(async()=>{const br=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});const p=await br.newPage({viewport:{width:1080,height:1350}});await p.setContent(html);await p.screenshot({path:path.join(OUT,'wolfe-us-ca-uk-library-mockup.png')});await br.close();console.log('ok')})();
