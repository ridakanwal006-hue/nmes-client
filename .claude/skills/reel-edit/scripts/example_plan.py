"""Worked example: the approved Clip 1 + Clip 2 podcast edit (edited/podcast_edit_styled.mp4).
Copy this file next to the new clips, change paths, cuts and captions, and run it.

  python3 example_plan.py <clip1.mp4> <clip2.mp4> <out.mp4>
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reel_style import Clip, Seg, Events, render, Y

c1, c2, out = sys.argv[1:4]
clips = {"c1": Clip(c1, crop="1080:1444:0:238"), "c2": Clip(c2, crop="720:964:0:158")}
END1, START2 = 7.30, 0.20   # clip 1 stops before its cut-off last word; clip 2 skips lead-in silence
O = END1 - START2           # clip 2 source time + O = output time

segs = [Seg("c1", 0, 1.12), Seg("c1", 1.12, 2.30, 1.25), Seg("c1", 2.30, 4.30), Seg("c1", 4.30, 5.14, 1.35),
        Seg("c1", 5.14, 6.80, 1.12), Seg("c1", 6.80, END1, 1.35, fade_out=True),
        Seg("c2", START2, 1.62, fade_in=True), Seg("c2", 1.62, 3.30, 1.25, bw=True), Seg("c2", 3.30, 4.40, 1.45, bw=True),
        Seg("c2", 4.40, 6.20), Seg("c2", 6.20, 7.95, 1.25)]

E = Events()
E.cap(0.10, 1.11, f"I texted my {Y}partner")
E.label(1.12, 2.29, "THE TEXT:", x=False)
E.cap(1.12, 2.29, f"\"Sorry, {Y}ignore me\"", style="Quote")
E.cap(2.30, 2.92, "before he had even")
E.cap(2.93, 4.29, f"read the {Y}first message")
E.pop(4.76, 5.13, f"SAVE {Y}THIS")
E.cap(5.14, 5.99, f"if you {Y}apologize")
E.cap(6.00, 6.79, "to the person who")
E.cap(6.80, END1 - 0.01, f"{Y}loves you")
E.cap(O + 0.30, O + 0.97, "He hadn't replied")
E.cap(O + 0.98, O + 1.61, f"in {Y}4 minutes")
E.label(O + 1.62, O + 3.29, "OVERTHINKING:")
E.cap(O + 1.62, O + 2.45, "\"So I assumed", style="Quote")
E.cap(O + 2.46, O + 3.29, f"I'd done {Y}something wrong\"", style="Quote")
E.pop(O + 3.30, O + 4.39, f"AND {Y}APOLOGIZED")
E.cap(O + 4.56, O + 5.35, f"I'm not {Y}needy,")
E.strike(O + 5.36, O + 6.19, "I'm not needy,", f"I'm just {Y}fluent in")
E.pop(O + 6.20, O + 7.95, f"PRE-EMPTIVE\\N{Y}DAMAGE CONTROL")

print(render(clips, segs, E, out))
