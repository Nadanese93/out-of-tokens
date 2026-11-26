# Out of Tokens, Mid-Sentence

A one-liner for the Make.fun bounty "Out of Tokens, Mid-Sentence": the model runs out of tokens mid-sentence — not because the answer was long, but because the user's 4,000-word prompt ate the whole budget before the answer even started.

The entry is a single line of at most 140 characters, written by `main.py` to `entry.txt`.

[![Out of Tokens, Mid-Sentence](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![Rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Nadanese93/out-of-tokens/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![Reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Nadanese93/out-of-tokens/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

This writes the one-line entry to `output/entry.txt` with no trailing newline.
