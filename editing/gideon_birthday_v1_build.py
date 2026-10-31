import subprocess,glob,json
fs=sorted(glob.glob('x/*.mp4'))
G=lambda k:[f for f in fs if k in f][0]
c0,c1,c2,c3,c4,c5,c6,c7,c8,c9=[G(k) for k in ['e883b442','4dde9e85','506a0b29','bc5adad4','6ad6ee72','85b02953','52277ec6','70f8fc06','cea4bda8','faeb782e']]
COMP='/tmp/claude-0/up21/comp.mp4'
order=[(c0,[(0.34,1.26),(1.54,3.54),(4.1,7.6)]),(c6,[(4.82,7.46)]),(c4,[(2.42,5.08),(5.87,6.9)]),(c5,[(0.28,1.92),(2.26,4.1),(6.16,6.8)]),
(c3,[(0.0,3.68),(4.56,6.02),(6.4,7.56)]),(c1,[(0.46,1.12),(1.7,2.54),(3.16,4.64),(5.4,7.4)]),(c7,[(0.9,2.38),(3.08,4.84),(5.06,6.3)]),
(c2,[(1.3,2.2),(2.7,3.7),(4.1,7.46)]),(c9,[(0.0,1.24),(1.88,2.68),(3.72,5.0),(5.58,7.02)]),(COMP,[(0.0,1.1),(1.17,3.2),(3.7,6.1)])]
txt=["On her birthday,","never text just happy birthday.","These four messages get screenshotted and shown to her friends.","Stop sending happy birthday like everyone else.",
"She notices the man who really thinks about her.","So try one of these.","And stay until the last one,","because that's the one she'll screenshot.","Number one:",
"Today the world celebrates the best thing that happened years ago.","I'm not congratulating you.","I'm telling you what matters.",
"Number two:","Happy birthday.","I'm not giving you a gift today.","I'm giving you a plan for this weekend.",
"Everything is already booked.","All you have to do is say","yes to the date.","Number three:","Happy birthday.","Another year of you being dangerously hard to forget.",
"Number four:","Make a wish.","Just don't waste it on me,","because you already have that one.","Comment BIRTHDAY,","and I'll send you my free playbook.","It shows you exactly what to text."]
D=0.12;inp=[];parts=[];raw=[];alen={}
for i,(f,segs) in enumerate(order):
    inp+=['-i',f]
    L=6.6 if f==COMP else (7.9 if f!=c2 else 8.0)
    for a,b in segs: parts.append((i,max(0,a-0.10),min(L-D,b+0.14)));raw.append((a,b))
i,s,e=parts[-1];parts[-1]=(i,s,min(6.6-D,raw[-1][1]+0.32))
for i,(f,segs) in enumerate(order): inp+=['-i','/tmp/claude-0/up21/dncomp.wav' if f==COMP else '/tmp/claude-0/up21/dn%d.wav'%fs.index(f)]
NO=len(order);fl=[];lab=[]
for k,(i,s,e) in enumerate(parts):
    fl.append(f'[{i}:v]trim={s}:{e+D},setpts=PTS-STARTPTS,fps=24[v{k}]')
    fl.append(f'[{NO+i}:a]atrim={s}:{e},asetpts=PTS-STARTPTS,highpass=f=90,afade=t=in:d=0.012,afade=t=out:st={e-s-0.012:.3f}:d=0.012[a{k}]');lab.append(f'[a{k}]')
fl.append(''.join(lab)+f'concat=n={len(parts)}:v=0:a=1[A]')
cv='v0';cum=parts[0][2]-parts[0][1]
for k in range(1,len(parts)):
    fl.append(f'[{cv}][v{k}]xfade=transition=fade:duration={D}:offset={cum-D:.3f}[x{k}]');cv=f'x{k}';cum+=parts[k][2]-parts[k][1]
subprocess.run(['ffmpeg','-y','-v','error']+inp+['-filter_complex',';'.join(fl),'-map',f'[{cv}]','-map','[A]','-t',f'{cum:.3f}','-c:v','libx264','-crf','14','-pix_fmt','yuv420p','-c:a','pcm_s16le','j.mkv'],check=True)
cum=0;sp=[]
for (i,s,e),(a,b) in zip(parts,raw): sp.append([round(cum+a-s,3),round(cum+b-s,3)]);cum+=e-s
assert len(sp)==len(txt),(len(sp),len(txt))
json.dump({"script":' '.join(txt),"seg_text":txt,"speech_segs":sp,"hook_red":["On her birthday","never text this"],"hook_sub":[],"hook_end":3.4,"hook_y":860,"type_style":"mono","type_dt":0.05,"captions_from_start":True,"clean_audio":True,"sfx_only":True,"no_grade":True,"glitch_neg":True,"glitch_ref_sfx":True,"glitch":round(sp[0][1]+0.12,2),"whoosh_at":[],"no_hits":True,"punch":[]},open('cfg.json','w'))
print(cum,sp[0],len(sp))
