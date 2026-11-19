// gta6-meme-x-01 entry: stage the prepared post payload for publishing.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";

const destinationFolder = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const sourceFile = resolve("POST.json");
const targetFile = resolve(destinationFolder, "POST.json");
const payload = readFileSync(sourceFile);
if (!existsSync(destinationFolder)) {
  mkdirSync(destinationFolder, { recursive: true });
}
writeFileSync(targetFile, payload);
