# 3D Printing Crash Course

A bilingual (English / French) crash course on 3D printing — 8 modules, 28 chapters,
fact-checked with ~200 sourced citations.

The online experience is one phone-first **single-page app** (`player/site/index.html`, built
by `build/build_app.py`): one URL whose GET parameters switch three views in place, with a
shared header toggle linking them.

```
index.html?lang=<en|fr>&view=<watch|read|pdf>&at=<module.chapter.scene>
```

- **Watch** — animated, module-by-module slideshow with synced voiceover, autoplay,
  pause/scrub, captions.
- **Read** — the full course prose, with a chapter accordion and schematic diagrams.
- **PDF** — opens `course_<lang>.pdf`.

`lang`, `view`, and `at` are all bookmarkable; a shared module → chapter nav (a drawer on
phones) drives both Watch and Read. Self-contained **offline** builds remain in `dist/`:
`course_<lang>.html` (dark/light, no network) and `course_<lang>.pdf`.

## Layout

| Path | What |
|------|------|
| `course_modules/{en,fr}/module_*.md` | the course content sources (per module) |
| `build/` | `build_all.sh` → offline PDF + self-contained HTML; `build_app.py` → the online single-page app |
| `player/` | scene data + audio for the watch view: `course.json`, `scenes/`, `diagrams.js`, audio pipeline, `build_site.sh` |
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

# Assemble the deployable single-page-app bundle -> player/site/
#   (index.html via build_app.py + course.json + diagrams.js + audio/ + assets/images/ + PDFs)
bash player/build_site.sh
```

Narration audio (`player/audio/`) is committed via Git LFS. Only the assembled
`player/site/` bundle is git-ignored — rebuild it with the command above.
