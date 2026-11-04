import cv2,numpy as np,subprocess
src='x/Man_speaking_about_love_20261023033216.mp4';out='m/love_clean.mp4'
cap=cv2.VideoCapture(src)
p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','bgr24','-s','720x1280','-r','24','-i','-','-i',src,'-map','0:v','-map','1:a','-c:v','libx264','-crf','12','-pix_fmt','yuv420p','-c:a','copy','-shortest',out],stdin=subprocess.PIPE)
k=np.ones((5,5),np.uint8)
while True:
    ok,fr=cap.read()
    if not ok:break
    y0,y1,x0,x1=900,1040,250,560
    reg=fr[y0:y1,x0:x1];g=cv2.cvtColor(reg,cv2.COLOR_BGR2GRAY)
    m=(g>105).astype(np.uint8)*255
    if m.sum()>255*60:
        m=cv2.dilate(m,k,iterations=2)
        full=np.zeros(fr.shape[:2],np.uint8);full[y0:y1,x0:x1]=m
        fr=cv2.inpaint(fr,full,4,cv2.INPAINT_TELEA)
    p.stdin.write(fr.tobytes())
p.stdin.close();p.wait()
