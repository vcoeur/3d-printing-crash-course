# 3D Printing Crash Course

A bilingual (English / French) crash course on 3D printing — 8 modules, 28 chapters,
fact-checked with ~200 sourced citations. Shipped in three forms:

- **Animated player** — `player/player.html`: a module-by-module slideshow with synced
  voiceover narration, autoplay, pause/scrub, captions, and an EN ↔ FR toggle.
- **Read** — self-contained single-file course apps: `dist/course_en.html`,
  `dist/course_fr.html` (dark/light toggle, embedded fonts/diagrams, no network).
- **PDF** — `dist/course_en.pdf`, `dist/course_fr.pdf`.

## Layout

| Path | What |
|------|------|
| `course_modules/{en,fr}/module_*.md` | the course content sources (per module) |
| `build/` | consolidate → PDF + self-contained HTML (`build_all.sh`) |
| `player/` | the animated player: `player.html`, `course.json`, `scenes/`, build scripts |
| `assets/fonts/` | embedded display + body fonts (woff2) |
| `assets/images/` | module banner images |
| `dist/` | built deliverables (HTML + PDF) |

Large binaries (PDF, audio, fonts, images) are tracked with **Git LFS** — run
`git lfs install` once, then `git lfs pull` after cloning.

## Building

```bash
# Consolidated PDF + HTML, both languages -> dist/
bash build/build_all.sh

# Narration audio for the player (writes player/audio/<lang>/<id>.mp3)
python3 player/gen_audio_gpt.py     --course player/course.json --out player/audio   # GPT-4o Mini TTS — cheap (~$0.60/1M chars), voice marin
python3 player/gen_audio_voxtral.py --course player/course.json --out player/audio   # Voxtral — expressive (~$16/1M chars)
# (or the free Edge TTS variant: gen_audio_edge.py, via `uv run --with edge-tts`)

# Assemble the deployable player bundle -> player/site/
bash player/build_site.sh
```

Narration audio (`player/audio/`) is committed via Git LFS. Only the assembled
`player/site/` bundle is git-ignored — rebuild it with the command above.
