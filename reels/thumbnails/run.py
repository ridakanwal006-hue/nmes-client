import sys
sys.path.insert(0, ".")
from cover import cover, SC
C1, F1 = "720:962:0:40", (650, 720)
C2, F2 = "720:962:0:40", (790, 880)
jobs = [
 ("manipulation", SC+"d19/t4.mp4", 7.3, "720:964:0:150", (660, 540), [("THAT'S", False), ("MANIPULATION", True)]),
 ("biggest-fan", SC+"d21/c3.mp4", 6.5, C1, F1, [("BE THEIR", False), ("BIGGEST", True), ("FAN", True)]),
 ("partner-choices", SC+"d20/P.mp4", 7.2, C1, F1, [("COMPLIMENT", False), ("OR INSULT?", True)]),
 ("self-trust", SC+"d23/d.mp4", 6.9, C1, F1, [("SELF-DOUBT", False), ("TO", False), ("SELF-TRUST", True)]),
 ("3am-replay", SC+"d24/c.mp4", 3.7, C2, F2, [("THE REPLAY", False), ("HELPS", True), ("NO ONE", True)]),
 ("boundaries", SC+"d25/b.mp4", 6.8, C2, F2, [("NO IS A", False), ("COMPLETE", True), ("SENTENCE", True)]),
 ("nobody-watching", SC+"d26/a.mp4", 6.4, C2, F2, [("NOBODY IS", False), ("THINKING", True), ("ABOUT IT", True)]),
 ("proof-of-survival", SC+"d27/a.mp4", 6.8, C2, F2, [("100%", False), ("SUCCESS", True), ("RATE", True)]),
 ("rehearsing", SC+"d28/a.mp4", 6.2, C2, F2, [("REHEARSED", False), ("10 TIMES", True)]),
]
for n, src, t, crop, face, lines in jobs:
    cover(src, t, crop, face, 1.1, lines, f"cov_{n}.jpg")
cover(SC+"d29/b.mp4", 6.2, "720:962:0:40", (660, 880), 1.1, [("YOU HAD", False), ("THE", True), ("ANSWER", True)], "cov_spoke-first.jpg")
print("done")
