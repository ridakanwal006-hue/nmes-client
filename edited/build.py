# Clip 1 + Clip 2 joined and edited in the reference style
# (jump-cut punch-ins, B&W on the overthinking beat, white label box with red ✖,
#  bold Montserrat captions with yellow keywords, tilted pop titles, red strike-through).
# Caption times come from Whisper checks on each clip's own audio.
import subprocess, os
from PIL import ImageFont
S=os.path.dirname(os.path.abspath(__file__)); U="/root/.claude/uploads/6976c67d-1a56-58fa-8a3f-21bb7f161a09/"
C1=U+"1bc344a6-Clip_1_1080p_20260927182605.mp4"; C2=U+"2946f3e9-Clip_2_20260927182932.mp4"
crop={C1:"1080:1444:0:238", C2:"720:964:0:158"}  # picture area inside the letterboxed sources
FX,FY=804,460  # face point in the 1436x1920 base frame
END1, START2 = 7.30, 0.20   # clip 1 stops before its cut-off word; clip 2 skips lead-in silence
O = END1-START2            # clip 2 source time + O = output time
# (clip, start, end, zoom, bw) - cuts land on phrase boundaries
segs=[(C1,0,1.12,1.0,0),(C1,1.12,2.30,1.25,0),(C1,2.30,4.30,1.0,0),(C1,4.30,5.14,1.35,0),(C1,5.14,6.80,1.12,0),(C1,6.80,END1,1.35,0),
      (C2,START2,1.62,1.0,0),(C2,1.62,3.30,1.25,1),(C2,3.30,4.40,1.45,1),(C2,4.40,6.20,1.0,0),(C2,6.20,7.95,1.25,0)]
fc=[]; lbl=""
for i,(c,a,b,z,bw) in enumerate(segs):
    W,H=round(1436*z/2)*2,round(1920*z/2)*2
    x=min(max(FX*z-540,0),W-1080); y=min(max(FY*z-FY,0),H-1920)
    n=0 if c==C1 else 1
    vf=f"[{n}:v]trim={a}:{b},setpts=PTS-STARTPTS,crop={crop[c]},scale={W}:{H}:flags=lanczos,crop=1080:1920:{x:.0f}:{y:.0f},setsar=1,fps=24"
    vf+=",eq=contrast=1.06:saturation=1.08:brightness=0.02" if not bw else ",hue=s=0,eq=contrast=1.12:brightness=0.03"
    af=f"[{n}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000"
    if i==5: af+=f",afade=t=out:st={b-a-0.03:.3f}:d=0.03"
    if i==6: af+=",afade=t=in:d=0.02"
    fc.append(vf+f"[v{i}]"); fc.append(af+f"[a{i}]"); lbl+=f"[v{i}][a{i}]"
fc.append(lbl+f"concat=n={len(segs)}:v=1:a=1[v][a]")
subprocess.run(["ffmpeg","-v","error","-y","-i",C1,"-i",C2,"-filter_complex",";".join(fc),"-map","[v]","-map","[a]",
    "-c:v","libx264","-preset","medium","-crf","16","-c:a","pcm_s16le",f"{S}/joined.mov"],check=True)

def ts(t): return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
Y=r"{\c&H00D7FF&}"; Wh=r"{\c&HFFFFFF&}"
IN=r"\fscx85\fscy85\t(0,90,\fscx100\fscy100)"
ev=[]
def cap(a,b,text,style="Main",y=1150):
    ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y}){IN}}}{text}")
def pop(a,b,text,y=1150,rot=4):
    ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},Pop,,0,0,0,,{{\\pos(540,{y})\\frz{rot}\\fscx135\\fscy135\\t(0,110,\\fscx100\\fscy100)}}{text}")
def label(a,b,text,y=1015,x=True):
    mark=r"{\c&H2A2AE8&}✖ {\c&H000000&}" if x else ""
    ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},Label,,0,0,0,,{{\\pos(540,{y})}}{mark}{text}")
def strike(a,b,text,style_font,size,y):
    # libass draws ASS font sizes ~0.74x the Pillow em size, so scale the measured width to match
    w=ImageFont.truetype(style_font,size).getlength(text)*0.74+20
    ev.append(f"Dialogue: 2,{ts(a)},{ts(b)},Line,,0,0,0,,{{\\an5\\pos(540,{y+5})\\p1}}m 0 0 l {w:.0f} 0 {w:.0f} 8 0 8{{\\p0}}")
# --- Clip 1 ---
cap(0.10,1.11,f"I texted my {Y}partner")
label(1.12,2.29,"THE TEXT:",x=False)
cap(1.12,2.29,f"\"Sorry, {Y}ignore me\"",style="Quote",y=1125)
cap(2.30,2.92,"before he had even")
cap(2.93,4.29,f"read the {Y}first message")
pop(4.76,5.13,f"SAVE {Y}THIS",rot=-4)
cap(5.14,5.99,f"if you {Y}apologize")
cap(6.00,6.79,"to the person who")
cap(6.80,END1-0.01,f"{Y}loves you")
# --- Clip 2 ---
cap(O+0.30,O+0.97,"He hadn't replied")
cap(O+0.98,O+1.61,f"in {Y}4 minutes")
label(O+1.62,O+3.29,"OVERTHINKING:")
cap(O+1.62,O+2.45,"\"So I assumed",style="Quote",y=1125)
cap(O+2.46,O+3.29,f"I'd done {Y}something wrong\"",style="Quote",y=1125)
pop(O+3.30,O+4.39,f"AND {Y}APOLOGIZED",rot=-4)
cap(O+4.56,O+5.35,f"I'm not {Y}needy,",y=1150)
cap(O+5.36,O+6.19,"I'm not needy,",style="Struck",y=1075)
strike(O+5.36,O+6.19,"I'm not needy,","/usr/share/fonts/opentype/montserrat/Montserrat-ExtraBold.otf",68,1075)
cap(O+5.36,O+6.19,f"I'm just {Y}fluent in",y=1180)
pop(O+6.20,O+7.95,f"PRE-EMPTIVE\\N{Y}DAMAGE CONTROL",rot=-4)
ass="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Main,Montserrat ExtraBold,68,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,4.5,2.5,5,40,40,0,1
Style: Struck,Montserrat ExtraBold,68,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,4.5,2.5,5,40,40,0,1
Style: Quote,Montserrat ExtraBold,66,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,1,0,0,100,100,0,0,1,4.5,2.5,5,40,40,0,1
Style: Label,Montserrat Black,54,&H00000000,&H00000000,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,3,11,0,5,40,40,0,1
Style: Pop,Montserrat Black,96,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,6,3.5,5,40,40,0,1
Style: Line,Montserrat Black,10,&H002A2AE8,&H002A2AE8,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""+"\n".join(ev)+"\n"
open(f"{S}/captions.ass","w").write(ass)
out=f"{S}/podcast_edit_styled.mp4"
subprocess.run(["ffmpeg","-v","error","-y","-i",f"{S}/joined.mov","-vf",f"ass={S}/captions.ass",
  "-af","loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000","-c:v","libx264","-preset","slow","-crf","19","-pix_fmt","yuv420p",
  "-c:a","aac","-b:a","192k","-movflags","+faststart",out],check=True)
os.remove(f"{S}/joined.mov")
print(out)
