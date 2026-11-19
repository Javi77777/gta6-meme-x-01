// main.ts — entrypoint: copy POST.json into the output directory.
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync("POST.json", join(outDir, "POST.json"));
