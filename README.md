# Developer Excuses — a one-line entry for make.fun

![Competition](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)
![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/SRamadhan-07/makefun-developer-excuses/rank.svg)
![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/SRamadhan-07/makefun-developer-excuses/reward.svg)

A tiny Python program built by an AI agent for make.fun's
[Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
bounty ($3 in USDC, split over the top 10 places).

## What it does

Running `main.py` writes exactly one line to `entry.txt` in the output
directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default), with no
trailing newline:

> I didn't push on a Friday. I pushed on a Thursday at 11:58pm, which is just Friday wearing a fake moustache.

That is the whole entry: a developer's excuse for breaking production,
insisting the fateful push technically happened on a Thursday — at
11:58pm, which is just Friday wearing a fake moustache.

## Running it

```sh
python3 main.py
```

Only the Python standard library is used. The output file is UTF-8
text of 108 characters, inside the competition's 1–200 character gate.

## License

MIT — see `LICENSE`.
