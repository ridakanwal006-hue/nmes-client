import cv2,numpy as np,subprocess,sys
src,out=sys.argv[1],sys.argv[2]
cap=cv2.VideoCapture(src)
p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','bgr24','-s','720x1280','-r','24','-i','-','-i',src,'-map','0:v','-map','1:a','-c:v','libx264','-crf','12','-pix_fmt','yuv420p','-c:a','copy','-shortest',out],stdin=subprocess.PIPE)
k=np.ones((5,5),np.uint8)
while True:
    ok,fr=cap.read()
    if not ok:break
    y0,y1,x0,x1=840,1280,60,720
    R=fr[y0:y1,x0:x1].astype(int);g=R.min(axis=2);sat=R.max(axis=2)-g;m=((g>170)&(sat<30)).astype(np.uint8)*255
    m[:max(0,872-y0),max(0,300-x0):max(0,450-x0)]=0
    if m.sum()>255*60:
        m=cv2.dilate(m,k,iterations=2);full=np.zeros(fr.shape[:2],np.uint8);full[y0:y1,x0:x1]=m
        fr=cv2.inpaint(fr,full,4,cv2.INPAINT_TELEA)
    p.stdin.write(fr.tobytes())
p.stdin.close();p.wait()
