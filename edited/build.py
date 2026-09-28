import subprocess, os
S=os.path.dirname(os.path.abspath(__file__)); U="/root/.claude/uploads/d180e573-1650-59e7-9dec-b2351106d63f/"
C1=U+"a34bd925-Clip_1_1080p_20260927182605.mp4"; C2=U+"cff302aa-Clip_2_20260927182932.mp4"
crop={C1:"1080:1444:0:238", C2:"720:964:0:158"}
FX,FY=804,460  # face point in 1436x1920 base frame
# (clip, start, end, zoom, bw)
segs=[(C1,0,1.12,1.0,0),(C1,1.12,2.18,1.3,1),(C1,2.18,3.04,1.15,0),(C1,3.04,4.57,1.0,0),(C1,4.57,6.30,1.3,0),(C1,6.30,7.30,1.0,0),
      (C2,0.25,1.79,1.0,0),(C2,1.79,3.38,1.25,1),(C2,3.38,4.53,1.45,1),(C2,4.53,5.37,1.0,0),(C2,5.37,8.0,1.2,0)]
fc=[]; lbl=""
for i,(c,a,b,z,bw) in enumerate(segs):
    W,H=round(1436*z/2)*2,round(1920*z/2)*2
    x=min(max(FX*z-540,0),W-1080); y=min(max(FY*z-FY,0),H-1920)
    n=0 if c==C1 else 1
    vf=f"[{n}:v]trim={a}:{b},setpts=PTS-STARTPTS,crop={crop[c]},scale={W}:{H}:flags=lanczos,crop=1080:1920:{x:.0f}:{y:.0f},setsar=1,fps=30"
    vf+=",eq=contrast=1.08:saturation=1.1" if not bw else ",hue=s=0,eq=contrast=1.15:brightness=0.02"
    fc.append(vf+f"[v{i}]"); fc.append(f"[{n}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000"+(f",afade=t=out:st={b-a-0.03:.3f}:d=0.03" if i==5 else "")+(",afade=t=in:d=0.02" if i==6 else "")+f"[a{i}]"); lbl+=f"[v{i}][a{i}]"
fc.append(lbl+f"concat=n={len(segs)}:v=1:a=1[v][a]")
subprocess.run(["ffmpeg","-v","error","-y","-i",C1,"-i",C2,"-filter_complex",";".join(fc),"-map","[v]","-map","[a]",
    "-c:v","libx264","-preset","medium","-crf","16","-c:a","pcm_s16le",f"{S}/joined.mov"],check=True)

def ts(t): return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
Y=r"{\c&H00D7FF&}"; Wh=r"{\c&HFFFFFF&}"
ev=[]
def cap(a,b,text,style="Main",y=1180,extra=""):
    ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y})\\fscx88\\fscy88\\t(0,90,\\fscx100\\fscy100){extra}}}{text}")
def pop(a,b,text,y=1180,rot=6):
    ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},Pop,,0,0,0,,{{\\pos(540,{y})\\frz{rot}\\fscx140\\fscy140\\t(0,110,\\fscx100\\fscy100)}}{text}")
def label(a,b,text,y=1000):
    ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},Label,,0,0,0,,{{\\pos(540,{y})}}{{\\c&H3C3CFF&}}✖ {Wh}{text}")
# --- Clip 1 ---
cap(0.12,1.11,f"I texted my {Y}partner")
label(1.12,2.17,"THE TEXT:")
pop(1.12,2.17,y=1200,text="\"SORRY,\\N"+Y+"IGNORE ME\"")
cap(2.18,3.03,"before he even")
cap(3.04,4.40,f"read the {Y}first message")
cap(4.58,5.24,"Think about this")
cap(5.25,6.29,f"if you {Y}apologize")
cap(6.30,7.28,"to the person who...")
# --- Clip 2 ---
o=7.30-0.25  # clip 2 starts at 0.25s, joined right after clip 1 ends at 7.30s
cap(o+0.25,o+1.76,f"He hadn't replied\\Nin {Y}4 minutes")
label(o+1.80,o+3.37,"OVERTHINKING:")
cap(o+1.80,o+3.37,f"\"I must've done\\N{Y}something wrong\"",style="Quote")
pop(o+3.39,o+4.50,f"I {Y}APOLOGIZED",rot=-6)
cap(o+4.54,o+5.37,"I'm not anxious...")
cap(o+5.38,o+6.17,"it's just")
pop(o+6.18,o+7.95,f"PRE-EMPTIVE\\N{Y}DAMAGE CONTROL",rot=-5)
ass=f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Main,Montserrat ExtraBold,72,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,5,3,5,40,40,0,1
Style: Quote,Montserrat ExtraBold,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,1,0,0,100,100,0,0,1,5,3,5,40,40,0,1
Style: Label,Montserrat Black,60,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,3,10,0,5,40,40,0,1
Style: Pop,Montserrat Black,112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,8,5,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""+"\n".join(ev)+"\n"
open(f"{S}/captions.ass","w").write(ass)
os.makedirs("/home/user/nmes-client/edited",exist_ok=True)
out="/home/user/nmes-client/edited/podcast_edit_styled.mp4"
subprocess.run(["ffmpeg","-v","error","-y","-i",f"{S}/joined.mov","-vf",f"ass={S}/captions.ass:fontsdir={S}/fonts",
  "-af","loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000","-c:v","libx264","-preset","slow","-crf","19","-pix_fmt","yuv420p",
  "-c:a","aac","-b:a","192k","-movflags","+faststart",out],check=True)
print(out)
