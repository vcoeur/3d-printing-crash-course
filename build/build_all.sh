#!/usr/bin/env bash
# Build every course deliverable: consolidated PDF + self-contained HTML, per language.
#
# Layout: run from the repo root. Deliverables are written to dist/:
#   dist/course_<lang>.pdf    all-in-one PDF  (via md_to_pdf.sh)
#   dist/course_<lang>.html   all-in-one HTML (dark/light toggle, self-contained)
# Intermediate consolidated markdown stays in course_<lang>.md (git-ignored).
#
# Usage: build/build_all.sh [en|fr ...]   (defaults to all languages with sources)

set -euo pipefail

BUILD_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_DIR="$(dirname "$BUILD_DIR")"   # repo root
OUT="$LOCAL_DIR/dist"
ASSETS="$LOCAL_DIR/assets/images"
HERO="$ASSETS/hero-bg.jpg"
FONTS="$LOCAL_DIR/assets/fonts"
MD_TO_PDF="$HOME/.config/agents/scripts/md_to_pdf.sh"
mkdir -p "$OUT"

declare -A SIBLING_LABEL=( [en]="Français" [fr]="English" )

build_lang() {
  local lang="$1" other
  local modules="$LOCAL_DIR/course_modules/$lang"
  if ! ls "$modules"/module_*.md >/dev/null 2>&1; then
    echo "skip $lang: no module sources in $modules"
    return
  fi
  [[ "$lang" == "en" ]] && other="fr" || other="en"

  echo "== $lang: consolidate =="
  python3 "$BUILD_DIR/consolidate.py" --lang "$lang" --modules-dir "$modules" --out "$LOCAL_DIR/course_$lang.md"
  python3 "$BUILD_DIR/consolidate.py" --lang "$lang" --modules-dir "$modules" --out "$LOCAL_DIR/.course_$lang.pdfsrc.md" --pdf
  # Inject the schema/diagrams into the PDF source as mermaid (rendered by md_to_pdf.sh).
  python3 "$BUILD_DIR/enrich.py" --pdf "$LOCAL_DIR/.course_$lang.pdfsrc.md" "$lang"

  echo "== $lang: PDF =="
  bash "$MD_TO_PDF" "$LOCAL_DIR/.course_$lang.pdfsrc.md" "$OUT/course_$lang.pdf"
  rm -f "$LOCAL_DIR/.course_$lang.pdfsrc.md"

  echo "== $lang: HTML =="
  python3 "$BUILD_DIR/build_html.py" \
    --src "$LOCAL_DIR/course_$lang.md" --out "$OUT/course_$lang.html" --lang "$lang" \
    --assets-dir "$ASSETS" --hero "$HERO" --fonts-dir "$FONTS" \
    --sibling-href "course_$other.html" --sibling-label "${SIBLING_LABEL[$lang]}" \
    --pdf-href "course_$lang.pdf"
}

langs=("$@")
[[ ${#langs[@]} -eq 0 ]] && langs=(en fr)
for lang in "${langs[@]}"; do
  build_lang "$lang"
done
echo "done -> $OUT"
ls -la "$OUT"
