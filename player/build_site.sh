#!/usr/bin/env bash
# Assemble the deployable site bundle under player/site/ — the unified, phone-first web app:
#   index.html          one page, one URL: ?lang&view&at switches Watch / Read / PDF in place
#                       (built by build/build_app.py, both prose bodies embedded)
#   course.json         merged scene data (fetched by the watch view)
#   diagrams.js         schematic SVG library (watch + read diagrams)
#   audio/<lang>/*.mp3   narration (fetched by the watch view)
#   assets/images/      module banners referenced by the read prose (relative paths)
#   course_en.pdf · course_fr.pdf   download targets for the PDF view (from dist/)
#   robots.txt + _headers           no-index
# Reproducible: build_all.sh (dist PDFs) -> merge_scenes.py -> gen_audio_*.py -> build_site.sh.
set -euo pipefail

PLAYER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$PLAYER_DIR")"
DIST="$REPO_DIR/dist"
SITE="$PLAYER_DIR/site"

rm -rf "$SITE"; mkdir -p "$SITE"

# Unified single-page app (consolidates + enriches + renders both languages' prose).
python3 "$REPO_DIR/build/build_app.py" --out "$SITE/index.html"

cp "$PLAYER_DIR/diagrams.js" "$SITE/diagrams.js"
cp "$PLAYER_DIR/course.json" "$SITE/course.json"
cp -r "$PLAYER_DIR/audio" "$SITE/audio"
cp -r "$REPO_DIR/assets/images" "$SITE/assets-images-tmp"; mkdir -p "$SITE/assets"; mv "$SITE/assets-images-tmp" "$SITE/assets/images"
cp "$DIST/course_en.pdf" "$DIST/course_fr.pdf" "$SITE/"

printf 'User-agent: *\nDisallow: /\n' > "$SITE/robots.txt"
printf '/*\n  X-Robots-Tag: noindex, nofollow\n' > "$SITE/_headers"

echo "built $SITE"
du -sh "$SITE"
ls -la "$SITE"
