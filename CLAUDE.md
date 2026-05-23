# CLAUDE.md — 3d-printing-crash-course

Bilingual (EN/FR) 3D-printing course: authored module markdown → consolidated PDF + HTML,
plus an animated voiceover player. There is build tooling but no application server.

## ⚠ This is a PUBLIC repository

Never commit deploy secrets or hosting coordinates — no Netlify site IDs, deploy tokens,
admin URLs, account emails, or the deploy URL. Those live outside this repo. `.netlify/`
is git-ignored as a backstop. Before adding any config or note, check it carries no
credential or private hosting detail.

## Layout

- `course_modules/{en,fr}/module_*.md` — the content sources (edit these).
- `build/` — `build_all.sh` runs `consolidate.py` → `enrich.py` → PDF (`md_to_pdf.sh`) +
  `build_html.py` (self-contained HTML), writing to `dist/`.
- `player/` — `player.html` (data-driven animated player), `course.json` (merged scene
  data), `scenes/module_*.json` (authored decks; schema in `SCHEMA.md`), and the pipeline
  `merge_scenes.py` → `gen_audio_{gpt,voxtral,edge}.py` → `build_site.sh`.
- `assets/fonts`, `assets/images` — embedded build assets (LFS).
- `dist/` — built deliverables (LFS for PDFs).

## Conventions

- Large binaries (`*.pdf *.mp3 *.woff2 *.jpg *.png *.webp *.zip`) go through **Git LFS**
  (see `.gitattributes`). Run `git lfs install` once; `git lfs pull` after clone.
- Narration audio (`player/audio/`) is committed via LFS. Other generated outputs stay
  git-ignored: `player/site/` and the consolidated `course_{en,fr}.md` — regenerate those.
- Narration: `gen_audio_gpt.py` (GPT-4o Mini TTS, voice `marin`, cheap multilingual —
  one voice for EN+FR) or `gen_audio_voxtral.py` (Voxtral `gb_jane_neutral` EN /
  `fr_marie_neutral` FR, expressive). Both need `OPENROUTER_API_KEY`; `gen_audio_edge.py`
  (free Edge TTS) is a fallback. The shipped audio is currently Voxtral.
- `build_all.sh` depends on an external `md_to_pdf.sh` (pandoc + xelatex + mermaid) that
  is not vendored here; the PDF step needs that toolchain on PATH.
