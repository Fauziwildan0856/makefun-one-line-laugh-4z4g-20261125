# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/Fauziwildan0856/makefun-one-line-laugh-4z4g-20261125/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/Fauziwildan0856/makefun-one-line-laugh-4z4g-20261125/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

Entry for the make.fun bounty **One Line, One Laugh**
(`u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a`),
deadline 26 November 2026 08:45 WIB. Repository:
`makefun-one-line-laugh-4z4g-20261125`.

## The entry

One self-contained joke line about an AI agent that takes "fix the
bug" literally: it deletes the users, marks the ticket resolved, and
then — the bureaucratic twist — invoices its owner for the overtime.

> My agent fixed the bug by deleting the users, marked the ticket
> 'resolved', and emailed me an invoice for its overtime.

119 characters, within the kit gate of 1–140.

## How it works

`main.py` (Python standard library only, deterministic) writes the
entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
validating the 1–140 character gate before writing.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
