import cv2,glob,numpy as np,subprocess,os
from PIL import Image
alpha=np.array(Image.open('bgmask.png'))[:,:,3].astype(np.float32)/255   # 1 = black
Y,X=np.mgrid[0:1280,0:720]
core=(((X-395)/150.0)**2+((Y-335)/205.0)**2)<=1   # outside: always black
core2=(((X-395)/118.0)**2+((Y-345)/180.0)**2)<=1  # inside: keep; between core2 and core: keep only dark (hair) pixels
ring=(~core2)&(Y<478)
outside=(~core)&(Y<478)
for f in sorted(glob.glob('x/*.mp4')):
    out='m/'+os.path.basename(f)
    cap=cv2.VideoCapture(f)
    p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','bgr24','-s','720x1280','-r','24','-i','-','-i',f,'-map','0:v','-map','1:a','-c:v','libx264','-crf','12','-pix_fmt','yuv420p','-c:a','copy','-shortest',out],stdin=subprocess.PIPE)
    while True:
        ok,fr=cap.read()
        if not ok:break
        fr=fr.astype(np.float32)
        luma=fr.mean(2)
        # ring pixels that are brighter than hair -> background light: black them (soft)
        kill=np.clip((luma-70)/15,0,1)*ring
        a=np.maximum(np.maximum(alpha,kill),outside.astype(np.float32))
        a=cv2.GaussianBlur(a,(0,0),1.2)
        fr=fr*(1-a[:,:,None])
        p.stdin.write(np.clip(fr,0,255).astype(np.uint8).tobytes())
    p.stdin.close();p.wait();print(out)
