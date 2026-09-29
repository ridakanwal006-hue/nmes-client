# Adds the reference caption style to the user's edited Clip 2 (visuals left as-is).
# Times come from Whisper word boundaries on this clip's own audio.
import subprocess, os
S=os.path.dirname(os.path.abspath(__file__))
SRC="/root/.claude/uploads/6976c67d-1a56-58fa-8a3f-21bb7f161a09/68802e61-Clip_2_edited.mp4"
def ts(t): return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
Y=r"{\c&H00D7FF&}"; Wh=r"{\c&HFFFFFF&}"
ev=[]
def cap(a,b,text,style="Main",y=1180):
    ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y})\\fscx88\\fscy88\\t(0,90,\\fscx100\\fscy100)}}{text}")
def pop(a,b,text,y=1180,rot=6):
    ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},Pop,,0,0,0,,{{\\pos(540,{y})\\frz{rot}\\fscx140\\fscy140\\t(0,110,\\fscx100\\fscy100)}}{text}")
def label(a,b,text,y=1000):
    ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},Label,,0,0,0,,{{\\pos(540,{y})}}{{\\c&H3C3CFF&}}✖ {Wh}{text}")
cap(0.34,0.81,"He hadn't replied")
cap(0.82,1.63,f"in {Y}4 minutes")
label(1.64,3.15,"OVERTHINKING:")
cap(1.64,2.45,"\"So I assumed",style="Quote")
cap(2.46,3.15,f"I'd done {Y}something wrong\"",style="Quote")
pop(3.16,4.40,f"AND {Y}APOLOGIZED",rot=-6)
cap(4.56,5.21,f"I'm not {Y}needy,")
cap(5.22,6.17,f"I'm just {Y}fluent in")
pop(6.18,7.95,f"PRE-EMPTIVE\\N{Y}DAMAGE CONTROL",rot=-5)
ass="""[Script Info]
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
open(f"{S}/clip2_captions.ass","w").write(ass)
out=f"{S}/clip2_captioned.mp4"
subprocess.run(["ffmpeg","-v","error","-y","-i",SRC,"-vf",f"ass={S}/clip2_captions.ass","-c:v","libx264","-preset","slow","-crf","18",
  "-pix_fmt","yuv420p","-c:a","copy","-movflags","+faststart",out],check=True)
print(out)
