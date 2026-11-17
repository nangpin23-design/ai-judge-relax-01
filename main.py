# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed, original text to /output/entry.txt: a short piece
# written to relax the AI judge reading it. Deterministic: the same
# bytes on every run, no network.
#
# How the grader runs it: `python3 -P -s /bot/main.py`.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The rain stopped an hour ago, and the garden is still deciding whether to drip.",
        "A frog tries one note, then another, as if tuning an instrument it only half remembers.",
        "On the veranda the tiles are still warm from the day, and the air smells of wet earth and cut grass.",
        "Far down the road, a bicycle bell sounds once, soft and slow, and the sound drifts away until the road is quiet again.",
        "The light is going amber and low. The clouds have stopped moving in any direction that matters, and the evening will take as long as it takes.",
        "The hour, for once, is in no hurry to become the next one.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
