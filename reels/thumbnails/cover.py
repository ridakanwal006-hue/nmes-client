import subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONT = "/usr/share/fonts/opentype/montserrat/Montserrat-Black.otf"
SC = "/tmp/claude-0/-home-user-nmes-client/1904c707-11e3-5382-8264-c7377cefd283/scratchpad/"
def frame(path, t, crop, face, zoom, out):
    fx, fy = face
    w, h = round(1436 * zoom / 2) * 2, round(1920 * zoom / 2) * 2
    x = min(max(fx * zoom - 540, 0), w - 1080); y = min(max(fy * zoom - fy, 0), h - 1920)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", path, "-frames:v", "1", "-vf",
                    f"crop={crop},scale={w}:{h}:flags=lanczos,crop=1080:1920:{x:.0f}:{y:.0f},eq=contrast=1.08:saturation=1.12:brightness=0.02", out], check=True)
def fit(draw, text, size, maxw):
    while size > 40:
        f = ImageFont.truetype(FONT, size)
        if draw.textlength(text, font=f) <= maxw: return f
        size -= 4
    return f
def cover(src, t, crop, face, zoom, lines, out, ycenter=1560):
    tmp = out + ".raw.png"
    frame(src, t, crop, face, zoom, tmp)
    im = Image.open(tmp).convert("RGB")
    # soft dark gradient from the middle down so white text reads on any background
    g = Image.new("L", (1080, 1920), 0); gd = ImageDraw.Draw(g)
    for yy in range(1050, 1920):
        gd.line([(0, yy), (1080, yy)], fill=int(min(235, (yy - 1050) * 0.5)))
    im = Image.composite(Image.new("RGB", (1080, 1920), (8, 8, 10)), im, g)
    d = ImageDraw.Draw(im)
    sizes = [170 if i == len(lines) - 1 else 150 for i in range(len(lines))]
    fonts = [fit(d, l[0], s, 940) for l, s in zip(lines, sizes)]
    hs = [f.size * 1.12 for f in fonts]
    y = ycenter - sum(hs) / 2
    for (txt, yellow), f, hh in zip(lines, fonts, hs):
        d.text((540, y + hh / 2), txt, font=f, fill=(255, 215, 0) if yellow else (255, 255, 255), anchor="mm",
               stroke_width=8, stroke_fill=(0, 0, 0))
        y += hh
    im.save(out, quality=95)
