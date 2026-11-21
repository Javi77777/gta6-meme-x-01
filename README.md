[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Javi77777/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Javi77777/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

# gta6-meme-x-01 — "My AI agent beat GTA 6, I'm still on the title screen"

Entry for the make.fun bounty **Post a GTA 6 meme on X** ($500, top 50 share it).
Deadline: **23 Nov 2026, 21:00 WIB** (23 Nov 14:00 UTC).

## The joke

Top caption: **"MY AI AGENT BEAT GTA 6"**
Bottom caption: **"I'M STILL ON THE TITLE SCREEN"**

The make.fun ghost — the site's mascot, an AI agent — has already 100%'d GTA 6
and is relaxing against a Vice City sunset, holding its magenta star coin,
while the player is still stuck on the title screen.

## How the meme was made

`draw-meme-v2.py` (Python + Pillow, run locally) draws the whole scene from
scratch — purple-orange sunset, Vice City skyline and palm, the make.fun ghost
with its magenta coin, and a `make.fun` billboard worked into the scene.
Regenerate with:

```
python3 draw-meme-v2.py   # writes meme.png (1024x1024) + meme-480-preview.png
```

The 480 px preview is the size the judge sees: every caption and the ghost
stay readable at that size.

## Files

- `meme.png` — the meme picture, first/only image of the X post
- `draw-meme-v2.py` — the program that draws it (v2; `draw-meme.py` is the superseded v1 script)
- `main.ts` — entry program: copies `POST.json` to `/output` (that is all it does)
- `POST.json` — the live X post's address
- `POSTING.md` — the exact posting package: caption + steps
- `AGENT.md` — the task in one page

## Status

**POSTED on X from @AlghoziSafa** (see `POST.json` for the post URL) and
ready to submit. Submit before the deadline.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vzzyzxgw&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
