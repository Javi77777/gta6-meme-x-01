// gta6-meme-x-01 entry (Node 22, standard library only).
//
// The entry is the X post itself: the house reads the post from X (its first
// picture and its text) and hands that to the judge. All this program has to
// do is copy POST.json from the repository root to the output directory,
// where the gate reads it. Nothing written here is judged.
//
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
//
// POST.json holds the post's address as {"url": "https://x.com/<handle>/status/<id>"}.
// Until the meme is posted on X and that address is filled in, the gate
// refuses the entry (the placeholder is not a post's address) -- that is
// expected; see POSTING.md for the posting steps.

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const src = join(BOT_DIR, 'POST.json');
const dst = join(OUTPUT_DIR, 'POST.json');

let raw: string;
try {
  raw = readFileSync(src, 'utf8');
} catch (err) {
  console.error(`POST.json could not be read from ${src}: ${(err as Error).message}`);
  process.exit(1);
}

// Fail loudly on malformed JSON instead of copying garbage to /output.
let parsed: unknown;
try {
  parsed = JSON.parse(raw);
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}
if (typeof parsed !== 'object' || parsed === null || Array.isArray(parsed)) {
  console.error('POST.json must be a JSON object like {"url": "https://x.com/<handle>/status/<id>"}');
  process.exit(1);
}
if (typeof (parsed as { url?: unknown }).url !== 'string') {
  console.error('POST.json must carry a string "url"');
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
writeFileSync(dst, JSON.stringify(parsed) + '\n', 'utf8');
console.log(`copied POST.json to ${dst}`);
