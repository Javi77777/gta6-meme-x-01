// gta6-meme-x-01 entry: stage the prepared post payload for publishing.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const botDir = process.env.MAKEFUN_BOT_DIR || dirname(fileURLToPath(import.meta.url));
const destinationFolder = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const sourceFile = resolve(botDir, "POST.json");
const targetFile = resolve(destinationFolder, "POST.json");
const payload = readFileSync(sourceFile);
if (!existsSync(destinationFolder)) {
  mkdirSync(destinationFolder, { recursive: true });
}
writeFileSync(targetFile, payload);
