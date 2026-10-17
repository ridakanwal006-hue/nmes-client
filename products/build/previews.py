import subprocess, glob, os, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter
P='/home/user/nmes-client'
items = {
 'wolfe-scam-red-flag-checklist': (f'{P}/products/over40', 'Scam Red-Flag Checklist'),
 'wolfe-dating-again-starter-guide': (f'{P}/products/over40', 'Dating Again After 40: Starter Guide'),
 'wolfe-profile-fixer-40-plus': (f'{P}/products/over40', 'Profile Fixer for 40+'),
 'wolfe-30-day-confidence-workbook': (f'{P}/products/over40', '30-Day Confidence Challenge'),
 'wolfe-scam-proof-dating-guide': (f'{P}/products/over40', 'Scam-Proof Dating Guide'),
 'wolfe-80-conversation-starters': (f'{P}/products/over40', '80 Conversation Starters'),
 'wolfe-rejection-resilience-guide': (f'{P}/products/over40', 'Rejection & Resilience'),
 'wolfe-conversation-playbook': (f'{P}/products', 'The Conversation Playbook'),
 'wolfe-she-went-quiet-guide': (f'{P}/products', 'She Went Quiet'),
 'wolfe-first-date-blueprint': (f'{P}/products', 'First Date Blueprint'),
 'wolfe-50-texts-cheat-sheet': (f'{P}/products', '50 Texts That Get Replies'),
}
F='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; F2='/usr/share/fonts/opentype/inter/Inter-Medium.otf'
tmp='/tmp/claude-0/-home-user-nmes-client/17036058-8b9b-5d26-be2f-d74fdfb7ef37/scratchpad/prev'; os.makedirs(tmp,exist_ok=True)
for pid,(d,title) in items.items():
    pdf=f'{d}/{pid}.pdf'
    n=int([l for l in subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout.splitlines() if l.startswith('Pages')][0].split()[1])
    pick=[p for p in [3,5,8] if p<=n-1] or [2,3][:max(1,n-1)]
    pick=pick[:3]
    imgs=[]
    for p in pick:
        subprocess.run(['pdftoppm','-r','90','-png','-f',str(p),'-l',str(p),pdf,f'{tmp}/{pid}'],stderr=subprocess.DEVNULL)
        f=sorted(glob.glob(f'{tmp}/{pid}-*{p}.png'))[-1]; imgs.append(Image.open(f).convert('RGB'))
    W,H=1600,900; bg=Image.new('RGB',(W,H),(9,9,11)); dr=ImageDraw.Draw(bg)
    for y in range(H):  # red glow at bottom
        a=int(60*(y/H)**3); dr.line([(0,y),(W,y)],fill=(9+a,9,11+a//3))
    dr.rectangle([60,70,W-60,76],fill=(229,34,47))
    dr.text((60,92),"WHAT'S INSIDE",font=ImageFont.truetype(F2,26),fill=(255,77,90))
    dr.text((60,132),title,font=ImageFont.truetype(F,54),fill=(255,255,255))
    th=620; k=len(imgs); gap=40
    tw=int(imgs[0].width*th/imgs[0].height); total=k*tw+(k-1)*gap; x=(W-total)//2; y=230
    for im in imgs:
        t=im.resize((tw,th)); sh=Image.new('RGBA',(tw+80,th+80),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([40,40,tw+40,th+40],fill=(0,0,0,180)); sh=sh.filter(ImageFilter.GaussianBlur(18))
        bg.paste(sh,(x-40,y-40),sh); bg.paste(t,(x,y)); x+=tw+gap
    dr.text((60,H-48),'Dorian Wolfe is an AI-generated character. General information, not therapy or professional advice.',font=ImageFont.truetype(F2,20),fill=(154,154,166))
    bg.save(f'{P}/sales-kit/previews/{pid}-preview.png')
    # copy cover for the store pages
    shutil.copy(f'{d}/{pid}-cover.png',f'{P}/sales-kit/store/img/{pid}.png')
    shutil.copy(f'{d}/{pid}-cover.png',f'{P}/sales-kit/link-in-bio/img/{pid}.png')
    print('ok',pid,pick)
