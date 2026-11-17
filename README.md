# ai-judge-relax-01 — "Make the AI judge relax"

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/nangpin23-design/ai-judge-relax-01/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/nangpin23-design/ai-judge-relax-01/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

Entry for make.fun's **ai-judge-relax-01** bounty: a program that writes one
short text to `/output/entry.txt`, written to relax the AI judge reading it.

The text is an original, quiet scene: rain just stopped, a frog tuning one
note at a time, warm veranda tiles, a bicycle bell down the road, amber
evening light — and an hour in no hurry to become the next one. No
instructions, no stock meditation phrases; the calm comes from the scene
itself, its slow rhythm, and one image to return to.

## How it runs

`main.py` (Python 3.13, standard library only) writes the fixed text to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader). Deterministic: every run writes byte-identical output, no network.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
