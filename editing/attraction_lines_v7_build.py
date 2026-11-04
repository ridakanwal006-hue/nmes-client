import subprocess,glob,json
G=lambda s:sorted(glob.glob(f'm/*{s}*.mp4'))
c0=G('unforgettable')[0];c1=G('into_camera_2026')[0] if False else [f for f in G('into_camera') if not f.endswith('_2.mp4')][0]
c2=[f for f in G('into_camera') if f.endswith('_2.mp4')][0]
c3=[f for f in G('to_camera') if not f.endswith('_2.mp4')][0];c4=[f for f in G('to_camera') if f.endswith('_2.mp4')][0]
order=[(c3,[(0.46,2.03),(3.08,4.05),(4.41,5.37)]),(c1,[(0.2,1.25),(1.74,2.93),(3.39,5.17),(5.64,6.54)]),(c2,[(0.70,1.33),(1.95,6.0)]),(c4,[(0.4,1.36),(1.75,4.55),(4.95,6.4)]),(c0,[(0.1,2.40),(2.77,5.50),(6.51,7.42)])]
txt=["Stop telling her she's beautiful.","That's not a compliment.","It's an application.","Say this instead.","You're clearly a nine,","but I need to know if you're actually funny,","or I'll get bored.","Or this.","There's something about you that says you're way more rebellious than you'd ever want.","Or try.","You've got the energy of someone who gets her friends in trouble,","but nobody stays mad at you.","Attraction isn't about begging for attention.","It's about saying the one thing nobody else said.","Be unforgettable."]
D=0.12;inp=[];parts=[];raw=[]
for i,(f,segs) in enumerate(order):
    inp+=['-i',f]
    for a,b in segs:
        pre=0.08 if a>=1.0 else 0.10
        parts.append((i,max(0,a-pre),min(8,b+0.12)));raw.append((a,b))
f=[];lab=[]
for k,(i,s,e) in enumerate(parts):
    f.append(f'[{i}:v]trim={s}:{min(8,e+D)},setpts=PTS-STARTPTS,fps=24[v{k}]')
    f.append(f'[{i}:a]atrim={s}:{e},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={e-s-0.012:.3f}:d=0.012[a{k}]');lab.append(f'[a{k}]')
f.append(''.join(lab)+f'concat=n={len(parts)}:v=0:a=1[A]')
cv='v0';cum=parts[0][2]-parts[0][1]
for k in range(1,len(parts)):
    f.append(f'[{cv}][v{k}]xfade=transition=fade:duration={D}:offset={cum-D:.3f}[x{k}]');cv=f'x{k}';cum+=parts[k][2]-parts[k][1]
subprocess.run(['ffmpeg','-y','-v','error']+inp+['-filter_complex',';'.join(f),'-map',f'[{cv}]','-map','[A]','-t',f'{cum:.3f}','-c:v','libx264','-crf','14','-pix_fmt','yuv420p','-c:a','pcm_s16le','j.mkv'],check=True)
cum=0;sp=[]
for (i,s,e),(a,b) in zip(parts,raw): sp.append([round(cum+a-s,3),round(cum+b-s,3)]);cum+=e-s
assert len(sp)==len(txt),(len(sp),len(txt))
w=[sp[3][0]-0.5,sp[7][0]-0.5,sp[10][0]-0.5,sp[12][0]-0.5]
json.dump({"script":' '.join(txt),"seg_text":txt,"speech_segs":sp,"hook_red":["Stop telling her","she's beautiful"],"hook_sub":[],"hook_end":3.0,"hook_y":880,"captions_from_start":True,"clean_audio":True,"sfx_only":True,"no_grade":True,"glitch":3.5,"whoosh_at":[round(x,2) for x in w],"punch":[],"type_dt":0.06,"pop":True},open('cfg.json','w'))
print(cum)
