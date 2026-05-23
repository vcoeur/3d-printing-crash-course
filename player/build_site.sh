#!/usr/bin/env bash
# Assemble the deployable site bundle under player/site/:
#   index.html (bilingual hub) · player.html · course.json · audio/<lang>/*.mp3
#   course_en.html · course_fr.html · course_en.pdf · course_fr.pdf  (from dist/)
#   robots.txt + _headers (no-index)
# Reproducible: merge_scenes.py -> gen_audio_{edge,voxtral}.py -> build_site.sh.
set -euo pipefail

PLAYER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$PLAYER_DIR")"
DIST="$REPO_DIR/dist"
SITE="$PLAYER_DIR/site"

rm -rf "$SITE"; mkdir -p "$SITE"
cp "$PLAYER_DIR/player.html" "$SITE/player.html"
cp "$PLAYER_DIR/diagrams.js" "$SITE/diagrams.js"
cp "$PLAYER_DIR/course.json" "$SITE/course.json"
cp -r "$PLAYER_DIR/audio" "$SITE/audio"
cp "$DIST/course_en.html" "$DIST/course_fr.html" "$DIST/course_en.pdf" "$DIST/course_fr.pdf" "$SITE/"

cat > "$SITE/index.html" << 'EOF'
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>3D Printing Crash Course</title>
<style>
  body{margin:0;min-height:100vh;background:radial-gradient(1200px 700px at 70% -10%,#171c27,#0e1014);
    color:#e8eaf0;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
    display:flex;align-items:center;justify-content:center;padding:32px}
  .wrap{max-width:760px;width:100%}
  h1{font-size:34px;margin:0 0 4px;font-weight:800}
  h1 .a{color:#ff7a2f}
  .sub{color:#9aa3b6;margin:0 0 28px}
  .hero{display:block;background:linear-gradient(135deg,#ff7a2f,#c2540a);color:#1a1205;text-decoration:none;
    border-radius:16px;padding:22px 24px;margin:0 0 18px;font-weight:800;font-size:20px;
    box-shadow:0 16px 40px rgba(255,122,47,.25)}
  .hero small{display:block;font-weight:600;font-size:13px;opacity:.8;margin-top:4px}
  .hero .langs{float:right;font-size:13px;font-weight:700}
  .hero .langs a{color:#1a1205;text-decoration:underline;margin-left:10px}
  .grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .card{background:#15181f;border:1px solid #272c38;border-radius:12px;padding:16px}
  .card h3{margin:0 0 10px;font-size:15px;color:#ffb066}
  .card a{display:inline-block;color:#e8eaf0;text-decoration:none;border:1px solid #272c38;border-radius:8px;
    padding:7px 12px;margin:4px 6px 0 0;font-size:14px}
  .card a:hover{border-color:#ff7a2f}
  .foot{color:#5b6478;font-size:12px;margin-top:24px}
</style>
</head>
<body><div class="wrap">
  <h1>3D Printing <span class="a">Crash Course</span></h1>
  <p class="sub">Cours accéléré d'impression 3D — 8 modules, 28 chapitres · EN / FR</p>

  <a class="hero" href="player.html?lang=fr">
    <span class="langs">▶ <a href="player.html?lang=en">EN</a> <a href="player.html?lang=fr">FR</a></span>
    ▶ Regarder le cours animé · Watch the animated course
    <small>Diaporama animé, narration vocale, lecture automatique — avec pause · Animated slides with voice narration, autoplay — pausable</small>
  </a>

  <div class="grid">
    <div class="card">
      <h3>📖 Lire le cours · Read the course</h3>
      <a href="course_fr.html">Français</a>
      <a href="course_en.html">English</a>
    </div>
    <div class="card">
      <h3>⬇ PDF</h3>
      <a href="course_fr.pdf">Français</a>
      <a href="course_en.pdf">English</a>
    </div>
  </div>

  <p class="foot">Lien non répertorié · unlisted link — please don't share publicly.</p>
</div></body>
</html>
EOF

printf 'User-agent: *\nDisallow: /\n' > "$SITE/robots.txt"
printf '/*\n  X-Robots-Tag: noindex, nofollow\n' > "$SITE/_headers"
sed -i 's|<head>|<head><meta name="robots" content="noindex, nofollow">|' "$SITE/course_fr.html" "$SITE/course_en.html"

echo "built $SITE"
du -sh "$SITE"
ls -la "$SITE"
