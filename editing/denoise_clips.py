import subprocess,glob,numpy as np,wave
def rd(p):
    w=wave.open(p);return w.getframerate(),np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
def wr(p,sr,y):
    w=wave.open(p,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes());w.close()
N_=2048;H=512;win=np.hanning(N_)
def stft(x):
    x=np.pad(x,(N_,N_));fr=[np.fft.rfft(x[i:i+N_]*win) for i in range(0,len(x)-N_,H)];return np.array(fr).T
def istft(X,L):
    y=np.zeros((X.shape[1]-1)*H+N_);ws=np.zeros_like(y)
    for j in range(X.shape[1]):
        y[j*H:j*H+N_]+=np.fft.irfft(X[:,j])*win;ws[j*H:j*H+N_]+=win**2
    return (y/np.maximum(ws,1e-6))[N_:N_+L]
def sm(g):
    p=np.pad(g,1,mode='edge');return sum(p[a:a+g.shape[0],b:b+g.shape[1]] for a in range(3) for b in range(3))/9
for n,f in enumerate(sorted(glob.glob('x/*.mp4'))):
    subprocess.run(['ffmpeg','-y','-v','error','-i',f,'-vn','-ac','1','-ar','48000',f'raw{n}.wav'])
    sr,x=rd(f'raw{n}.wav');X=stft(x);M=np.abs(X);e=M.mean(0)
    quiet=np.argsort(e)[:int(len(e)*0.35)]
    Nz=np.percentile(M[:,quiet],70,axis=1,keepdims=True)
    g=sm(np.maximum(1-2.2*Nz/(M+1e-9),0.03));g[:int(100/(sr/N_))]=0
    y=istft(X*g,len(x));wr(f'dn{n}.wav',sr,y)
    h=sr//5
    fm=lambda z:[round(20*np.log10(np.sqrt((z[i:i+h]**2).mean())+1e-9)) for i in range(0,len(z)-h,h)]
    print(n,'raw',fm(x)[:40]);print(n,'dn ',fm(y)[:40])
