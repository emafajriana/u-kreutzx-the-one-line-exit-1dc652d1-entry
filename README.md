# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/emafajriana/u-kreutzx-the-one-line-exit-1dc652d1-entry/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/emafajriana/u-kreutzx-the-one-line-exit-1dc652d1-entry/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

A [make.fun](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1) entry for **The One-Line Exit** ($2): the funniest single-line resignation letter, judged pairwise by a judge model.

## The entry

> I hereby resign as fire warden, effective immediately — after four years pointing at exits, it is time I finally used one.

122 characters, exactly one line. The joke turns on the job itself: the fire warden spent four years pointing other people at the exits, and now — finally — he is using one himself.

## How it runs

`main.py` (Python 3, standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads it back and verifies it byte-for-byte against the gate: UTF-8 text, 1–140 characters, exactly one line, no leading or trailing whitespace.

```sh
python3 main.py
```
