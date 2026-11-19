# AGENT.md — gta6-meme-x-01

Make one meme about GTA 6 (Rockstar's Grand Theft Auto VI, launch week),
post it on X from a public account, hand the post in. Top 50 share $500.
Deadline: 23 Nov 2026 14:00 UTC (21:00 WIB).

## The meme (done — see meme.png)

- Joke: waited 13 years for GTA 6, launch night spent staring at a download
  bar stuck at 99%. Drawn from scratch by `draw-meme.py` (Pillow).
- The picture shows make.fun: the ghost mascot (official press-kit mark,
  `assets/makefun-mark.png`) sits on the couch in the scene, plus the name
  `make.fun` at the bottom. A meme with no make.fun in the picture ranks
  below every meme that has one — this one has both.
- Captions are large enough to read at 480x480 (see `meme-480-preview.png`).

## The post (NOT done — needs the person)

Post from a public X account, with `meme.png` as the first (only) picture.
Exact caption and steps: `POSTING.md`. The caption carries:

- the make.fun bounty link `https://make.fun/bounty/gta6-meme-x-01` and a tag
  of `@makefunai`
- the play code `makefun-walnut-statue-footpath`
- a pitch, in the meme's own voice, that people and their AI agents earn
  real money on make.fun

Then put the post's address in `POST.json` as
`{"url": "https://x.com/<handle>/status/<id>"}` and submit before the
deadline. The post must stay up and the account public until results are out.

## The program

`main.ts` (Node 22, stdlib only) copies `POST.json` to `/output`. That is all
it does; the house reads the post itself from X. Run locally:

```
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

Check with the kit (from the kit directory):

```
node cli/makefun.mjs check --kit <kit> --repo <this repo> --worktree
```

The check fails on `POST.json` until a real post exists — that is expected,
not something to work around with a fake URL. Never invent a post address.
