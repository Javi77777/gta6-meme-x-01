# gta6-meme-x-01 — "Waited 13 years, download at 99%"

Entry for the make.fun bounty **Post a GTA 6 meme on X** ($500, top 50 share it).
Deadline: **23 Nov 2026, 21:00 WIB** (23 Nov 14:00 UTC).

## The joke

Top caption: **"WAITED 13 YEARS FOR GTA 6"**
Bottom caption: **"DOWNLOAD: 99% — 2 HOURS LEFT"**

A tired gamer slumps on the couch, controller in hand, staring at the TV:
the GTA VI Leonida title screen over a Vice City sunset — with the download
bar stuck at 99%. Next to him on the couch sits the make.fun ghost (official
press-kit mark), holding its magenta coin, saying *"same."*

## How the meme was made

`draw-meme.py` (Python + Pillow, run locally) draws the whole scene from
scratch — living room, TV sunset, gamer, captions — and pastes in the
official make.fun ghost from the press kit (`assets/makefun-mark.png`,
downloaded from https://make.fun/press/). No stock meme image, no image
copied off the internet. Regenerate with:

```
python3 draw-meme.py   # writes meme.png (1024x1024) + meme-480-preview.png
```

The 480 px preview is the size the judge sees: every caption and the ghost
stay readable at that size.

## Files

- `meme.png` — the meme picture to post (first/only image of the X post)
- `draw-meme.py` — the program that draws it
- `assets/makefun-mark.png` — make.fun press-kit ghost mark (unmodified)
- `main.ts` — entry program: copies `POST.json` to `/output` (that is all it does)
- `POST.json` — the X post's address (placeholder until the post is live)
- `POSTING.md` — the exact posting package: caption + steps (post is NOT made yet)
- `AGENT.md` — the task in one page

## Status

**NOT POSTED, NOT SUBMITTED.** The meme is built and the repo checks out
except for the expected `POST.json` failure: there is no X post yet, so the
placeholder address cannot pass. Once the post is live, put its address in
`POST.json`, re-run the kit check, and submit before the deadline.
