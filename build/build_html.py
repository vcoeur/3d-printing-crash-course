#!/usr/bin/env python3
"""Render a consolidated course markdown into one self-contained, module-centric web app.

The output is a single HTML file (embedded fonts, base64 images, inline SVG diagrams,
no network) presenting the course as an interactive course console: an overview grid of
module cards with per-module progress, and a focused single-module reader with a chapter
accordion, schema diagram, banner photo, reading-progress bar, and module-to-module
navigation. Aesthetic: warm-orange-on-graphite engineering blueprint.

Pipeline: enrich the markdown (banner + diagram per module, HTML-only), render with
pandoc + mermaid-filter (--section-divs gives nested per-module/chapter <section>s),
embed everything, and wrap in the interactive template below.
"""

import argparse
import base64
import shutil
import subprocess
import tempfile
from pathlib import Path

from enrich import enrich_markdown

UI = {
    "en": {
        "eyebrow": "FDM · CoreXY · Bambu Lab", "start": "Start course", "browse": "Browse modules",
        "pdf": "PDF", "search": "Search modules…", "theme": "Theme", "modules": "modules",
        "words": "words", "read": "min read", "complete": "Mark complete", "completed": "Completed",
        "all": "All modules", "prev": "Previous", "next": "Next", "open": "Open module",
        "chapters": "chapters", "progress": "complete", "module": "Module", "top": "Top",
        "footer": "Self-contained course — view in any browser, online or offline.",
        "of": "of",
    },
    "fr": {
        "eyebrow": "FDM · CoreXY · Bambu Lab", "start": "Commencer le cours", "browse": "Parcourir les modules",
        "pdf": "PDF", "search": "Rechercher un module…", "theme": "Thème", "modules": "modules",
        "words": "mots", "read": "min de lecture", "complete": "Marquer comme terminé", "completed": "Terminé",
        "all": "Tous les modules", "prev": "Précédent", "next": "Suivant", "open": "Ouvrir le module",
        "chapters": "chapitres", "progress": "terminés", "module": "Module", "top": "Haut",
        "footer": "Cours autonome — consultable dans tout navigateur, en ligne ou hors ligne.",
        "of": "sur",
    },
}

FONTS = [
    ("Bricolage Grotesque", 700, "bricolage-700.woff2"),
    ("Bricolage Grotesque", 800, "bricolage-800.woff2"),
    ("Spline Sans", 400, "spline-400.woff2"),
    ("Spline Sans", 600, "spline-600.woff2"),
    ("Spline Sans Mono", 400, "splinemono-400.woff2"),
    ("Spline Sans Mono", 600, "splinemono-600.woff2"),
]

# Pandoc HTML template. Pandoc directives are $...$ — JS uses string concatenation
# (never `${}` template literals) so nothing collides with pandoc variable syntax.
# __FONTS__ and __HERO_BG__ are substituted before rendering.
TEMPLATE = r"""<!DOCTYPE html>
<html lang="$lang$">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>$title$</title>
<script>
  (function () {
    var t = localStorage.getItem("pf-theme") || (window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
    document.documentElement.setAttribute("data-theme", t);
  })();
</script>
<style>
__FONTS__
  :root {
    --display:"Bricolage Grotesque",Georgia,serif; --body:"Spline Sans",-apple-system,system-ui,sans-serif;
    --mono:"Spline Sans Mono",ui-monospace,Menlo,monospace;
    --bg:#0b0e13; --panel:#11161d; --panel2:#161d27; --border:#222c38; --fg:#e8edf3; --muted:#8b97a6;
    --accent:#ff6a1a; --accent-soft:rgba(255,106,26,.14); --accent-fg:#0b0e13; --link:#ff8a4c;
    --steel:#5fb0ff; --grid:rgba(255,255,255,.035); --glow:rgba(255,106,26,.16);
    --warn-bd:#f5a524; --warn-bg:#241a0c; --note-bd:#5fb0ff; --note-bg:#0e1d2b; --tip-bd:#4ade80; --tip-bg:#0e2018;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35); --nav-h:56px;
  }
  :root[data-theme="light"] {
    --bg:#f4f1ec; --panel:#ffffff; --panel2:#faf8f4; --border:#e4ddd1; --fg:#1b1813; --muted:#6c6358;
    --accent:#dc5310; --accent-soft:rgba(220,83,16,.12); --accent-fg:#ffffff; --link:#bd460c;
    --steel:#2f6fb0; --grid:rgba(40,30,20,.04); --glow:rgba(220,83,16,.10);
    --warn-bd:#c2700a; --warn-bg:#fdf3e3; --note-bd:#2f6fb0; --note-bg:#eef5fc; --tip-bd:#1f9d57; --tip-bg:#edfaf1;
    --shadow:0 1px 2px rgba(30,25,20,.06),0 10px 28px rgba(30,25,20,.08);
  }
  * { box-sizing:border-box; }
  html { scroll-behavior:smooth; }
  body { margin:0; font-family:var(--body); font-size:17px; line-height:1.7; color:var(--fg);
    background:var(--bg);
    background-image:
      radial-gradient(900px 480px at 78% -8%, var(--glow), transparent 60%),
      linear-gradient(var(--grid) 1px, transparent 1px),
      linear-gradient(90deg, var(--grid) 1px, transparent 1px);
    background-size:auto, 34px 34px, 34px 34px; -webkit-font-smoothing:antialiased; }
  a { color:var(--link); text-decoration:none; } a:hover { text-decoration:underline; }
  .mono { font-family:var(--mono); }
  .eyebrow { font-family:var(--mono); font-size:.74rem; letter-spacing:.22em; text-transform:uppercase; color:var(--accent); }

  #progress-top { position:fixed; top:0; left:0; height:3px; width:100%; z-index:60; }
  #progress-top > i { display:block; height:100%; width:0; background:var(--accent); transition:width .1s linear; }

  .nav { position:sticky; top:0; z-index:50; height:var(--nav-h); border-bottom:1px solid var(--border);
    background:color-mix(in srgb,var(--bg) 82%,transparent); backdrop-filter:saturate(1.5) blur(10px); }
  .nav-inner { max-width:1180px; margin:0 auto; height:100%; padding:0 1.3rem; display:flex; align-items:center; gap:.7rem; }
  .brand { display:flex; align-items:center; gap:.6rem; font-family:var(--display); font-weight:800; letter-spacing:-.01em;
    margin-right:auto; cursor:pointer; background:none; border:none; color:var(--fg); font-size:1.02rem; }
  .brand .mark { width:26px; height:26px; border-radius:7px; background:linear-gradient(135deg,var(--accent),#ffae6b);
    display:grid; place-items:center; color:#0b0e13; font-family:var(--mono); font-weight:700; font-size:.8rem; box-shadow:0 0 0 3px var(--accent-soft); }
  .nav .search { flex:0 1 230px; }
  .nav input { width:100%; padding:.42rem .7rem; border:1px solid var(--border); border-radius:9px; background:var(--panel);
    color:var(--fg); font-family:var(--mono); font-size:.8rem; }
  .btn { cursor:pointer; border:1px solid var(--border); background:var(--panel); color:var(--fg); border-radius:9px;
    padding:.42rem .7rem; font-family:var(--mono); font-size:.78rem; display:inline-flex; align-items:center; gap:.4rem; }
  .btn:hover { border-color:var(--accent); color:var(--accent); }
  .btn.solid { background:var(--accent); color:var(--accent-fg); border-color:var(--accent); font-weight:600; }
  .btn.solid:hover { color:var(--accent-fg); filter:brightness(1.06); }
  .btn.ghostline { background:transparent; }
  #menu { display:none; }

  .wrap { max-width:1180px; margin:0 auto; padding:0 1.3rem; }

  /* Overview hero */
  .hero { position:relative; overflow:hidden; border-bottom:1px solid var(--border); }
  .hero .bg { position:absolute; inset:0; background:url("__HERO_BG__") center/cover; opacity:.34; }
  .hero::after { content:""; position:absolute; inset:0;
    background:linear-gradient(180deg, color-mix(in srgb,var(--bg) 55%,transparent), var(--bg) 92%); }
  .hero .inner { position:relative; z-index:1; max-width:1180px; margin:0 auto; padding:clamp(2.6rem,7vw,5rem) 1.3rem clamp(2rem,4vw,3rem); }
  .hero h1 { font-family:var(--display); font-weight:800; font-size:clamp(2.4rem,6.5vw,4.6rem); line-height:.98;
    letter-spacing:-.025em; margin:.7rem 0 .5rem; }
  .hero .subtitle { font-size:clamp(1.05rem,2.2vw,1.4rem); color:var(--fg); max-width:36ch; margin:0 0 1rem; }
  .hero .lead { color:var(--muted); max-width:62ch; margin:0 0 1.5rem; }
  .hero .stats { display:flex; flex-wrap:wrap; gap:1.6rem; margin:1.4rem 0; }
  .stat { display:flex; flex-direction:column; }
  .stat b { font-family:var(--mono); font-weight:600; font-size:1.6rem; color:var(--accent); line-height:1; }
  .stat span { font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin-top:.35rem; }
  .hero .cta { display:flex; flex-wrap:wrap; gap:.7rem; }
  .cta .btn { font-size:.85rem; padding:.62rem 1.1rem; }

  /* Overall progress strip */
  .overall { max-width:1180px; margin:0 auto; padding:1.4rem 1.3rem 0; display:flex; align-items:center; gap:1rem; }
  .overall .track { flex:1; height:7px; background:var(--panel2); border:1px solid var(--border); border-radius:99px; overflow:hidden; }
  .overall .fill { height:100%; width:0; background:linear-gradient(90deg,var(--accent),#ffb072); transition:width .5s ease; }
  .overall .lbl { font-family:var(--mono); font-size:.76rem; color:var(--muted); white-space:nowrap; }

  /* Module grid */
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:1.1rem;
    max-width:1180px; margin:1.4rem auto; padding:1rem 1.3rem 4rem; }
  .card { position:relative; border:1px solid var(--border); border-radius:16px; background:var(--panel); overflow:hidden;
    cursor:pointer; display:flex; flex-direction:column; box-shadow:var(--shadow); opacity:0; transform:translateY(14px);
    animation:rise .5s forwards; transition:border-color .2s, transform .2s; }
  .card:hover { border-color:var(--accent); transform:translateY(-4px); }
  @keyframes rise { to { opacity:1; transform:none; } }
  .card .thumb { position:relative; aspect-ratio:16/9; overflow:hidden; background:var(--panel2); }
  .card .thumb img { width:100%; height:100%; object-fit:cover; filter:saturate(1.06) contrast(1.02); transition:filter .3s, transform .4s; }
  .card:hover .thumb img { filter:saturate(1.15); transform:scale(1.05); }
  .card .thumb::after { content:""; position:absolute; inset:0; background:linear-gradient(180deg,transparent 55%, color-mix(in srgb,var(--panel) 72%,transparent)); }
  .card .num { position:absolute; top:.7rem; left:.8rem; z-index:2; font-family:var(--mono); font-weight:700; font-size:1.5rem;
    color:#fff; text-shadow:0 2px 10px rgba(0,0,0,.6); }
  .card .check { position:absolute; top:.7rem; right:.8rem; z-index:2; width:26px; height:26px; border-radius:50%;
    display:grid; place-items:center; font-size:.85rem; background:var(--accent); color:var(--accent-fg); opacity:0; transform:scale(.6); transition:.2s; }
  .card.done .check { opacity:1; transform:none; }
  .card.done { border-color:color-mix(in srgb,var(--accent) 50%,var(--border)); }
  .card .body { padding:.95rem 1.05rem 1.1rem; display:flex; flex-direction:column; gap:.5rem; flex:1; }
  .card .body h3 { font-family:var(--display); font-weight:700; font-size:1.22rem; line-height:1.15; margin:0; letter-spacing:-.01em; }
  .card .meta { font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; color:var(--muted); text-transform:uppercase; }
  .card .blurb { font-size:.9rem; color:var(--muted); margin:0; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }
  .card .go { margin-top:auto; font-family:var(--mono); font-size:.78rem; color:var(--accent); }

  /* Reader (single module) */
  #reader[hidden] { display:none; }
  .module-bar { position:sticky; top:var(--nav-h); z-index:30; border-bottom:1px solid var(--border);
    background:color-mix(in srgb,var(--bg) 88%,transparent); backdrop-filter:blur(8px); }
  .module-bar .row { max-width:1080px; margin:0 auto; padding:.7rem 1.3rem; display:flex; align-items:center; gap:.8rem; flex-wrap:wrap; }
  .module-bar .idx { font-family:var(--mono); font-size:.74rem; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); }
  .module-bar .spacer { flex:1; }
  .module-bar .pbar { height:3px; background:var(--panel2); }
  .module-bar .pbar > i { display:block; height:100%; width:0; background:var(--accent); }

  .reader-main { max-width:880px; margin:0 auto; padding:2rem 1.3rem 5rem; }
  .content section.level1 { display:none; }
  .content section.level1.active { display:block; animation:fade .35s ease; }
  @keyframes fade { from { opacity:0; transform:translateY(8px); } to { opacity:1; } }
  .content section.level1 > h1 { font-family:var(--display); font-weight:800; font-size:clamp(1.9rem,4vw,2.7rem);
    line-height:1.05; letter-spacing:-.02em; margin:.2rem 0 1rem; }
  .content h1 .header-section-number { display:none; }
  .module-banner { margin:0 0 1.6rem; }
  .module-banner img { width:100%; max-height:460px; object-fit:contain; border-radius:14px; box-shadow:var(--shadow); display:block; background:var(--panel2); }
  .module-banner p { margin:.5rem 0 0; font-family:var(--mono); font-size:.74rem; color:var(--muted); text-align:center; letter-spacing:.04em; }

  .diagram { position:relative; margin:1.7rem 0; background:var(--panel2); border:1px solid var(--border); border-radius:16px; padding:2rem 1.2rem 1rem; box-shadow:var(--shadow); }
  .diagram::before { content:"SCHEMATIC"; position:absolute; top:.7rem; left:1.1rem; font-family:var(--mono); font-size:.62rem; letter-spacing:.2em; color:var(--muted); }
  html[lang="fr"] .diagram::before { content:"SCHÉMA"; }
  .diagram > p { margin:1rem 0 0; text-align:center; font-family:var(--mono); font-size:.74rem; color:var(--muted); }
  .schema-flow { display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:.35rem .1rem; }
  .sunit { display:inline-flex; align-items:center; }
  .snode { display:inline-block; background:var(--panel); border:1px solid var(--border); border-radius:10px; padding:.55rem .8rem; font-weight:600; font-size:.9rem; text-align:center; max-width:170px; box-shadow:var(--shadow); }
  .snode.accent { background:linear-gradient(135deg,var(--accent),#ffae6b); color:var(--accent-fg); border-color:transparent; }
  .sarrow { width:24px; height:2px; background:var(--accent); margin:0 .3rem; position:relative; flex:0 0 auto; }
  .sarrow::after { content:""; position:absolute; right:-1px; top:-3px; border-left:7px solid var(--accent); border-top:4px solid transparent; border-bottom:4px solid transparent; }
  .schema-tree { display:flex; flex-direction:column; align-items:center; gap:1rem; }
  .sroot { background:linear-gradient(135deg,var(--accent),#ffae6b); color:var(--accent-fg); font-family:var(--display); font-weight:700; padding:.55rem 1.1rem; border-radius:10px; font-size:1.05rem; position:relative; }
  .sroot::after { content:""; position:absolute; bottom:-11px; left:50%; transform:translateX(-50%); border-top:7px solid var(--accent); border-left:5px solid transparent; border-right:5px solid transparent; }
  .sfan { display:grid; grid-template-columns:repeat(auto-fit,minmax(155px,1fr)); gap:.8rem; width:100%; }
  .sgroup { background:var(--panel); border:1px solid var(--border); border-radius:12px; padding:.7rem .9rem; }
  .sgroup-h { font-family:var(--mono); font-size:.74rem; letter-spacing:.05em; text-transform:uppercase; color:var(--accent); font-weight:600; margin-bottom:.4rem; }
  .sgroup ul { margin:0; padding-left:1.05rem; } .sgroup li { font-size:.88rem; margin:.15rem 0; }
  .schema-dec { display:flex; flex-direction:column; align-items:center; gap:.3rem; }
  .drow { display:flex; align-items:center; gap:.55rem; flex-wrap:wrap; justify-content:center; background:var(--panel); border:1px solid var(--border); border-radius:10px; padding:.5rem .9rem; }
  .drow .dq { font-weight:600; } .drow .darr, .drow .dlbl { font-family:var(--mono); font-size:.76rem; color:var(--muted); }
  .drow .dout { font-weight:700; } .drow .dout.accent { color:var(--accent); }
  .drow.dfin { border-color:var(--accent); } .dno { font-family:var(--mono); font-size:.72rem; color:var(--muted); }

  /* Chapter accordion */
  section.level2 { border:1px solid var(--border); border-radius:14px; margin:.8rem 0; overflow:hidden; background:var(--panel); }
  section.level2 > h2 { cursor:pointer; margin:0; padding:1rem 1.1rem; font-family:var(--display); font-weight:700; font-size:1.15rem;
    display:flex; align-items:center; gap:.7rem; user-select:none; }
  section.level2 > h2 .header-section-number { font-family:var(--mono); font-weight:600; font-size:.85rem; color:var(--accent);
    background:var(--accent-soft); border-radius:7px; padding:.15rem .5rem; }
  section.level2 > h2::after { content:"+"; margin-left:auto; font-family:var(--mono); color:var(--muted); font-size:1.2rem; transition:transform .2s; }
  section.level2.open > h2::after { content:"\2212"; color:var(--accent); }
  .chapter-body { padding:0 1.2rem; max-height:0; overflow:hidden; transition:max-height .35s ease; }
  section.level2.open .chapter-body { padding:.2rem 1.2rem 1.1rem; }

  h3 { font-family:var(--display); font-weight:700; font-size:1.18rem; margin-top:1.6rem; }
  h4 { font-size:1.04rem; margin-top:1.3rem; } h5 { font-family:var(--mono); font-size:.8rem; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); }
  .content hr { display:none; }
  p,li { overflow-wrap:break-word; }

  blockquote { margin:1.2rem 0; padding:.7rem 1.05rem; border-left:3px solid var(--border); background:var(--panel2); border-radius:0 10px 10px 0; }
  blockquote p { margin:.3rem 0; }
  blockquote.callout-warning { border-left-color:var(--warn-bd); background:var(--warn-bg); }
  blockquote.callout-note { border-left-color:var(--note-bd); background:var(--note-bg); }
  blockquote.callout-tip { border-left-color:var(--tip-bd); background:var(--tip-bg); }
  blockquote strong:first-child { display:inline-flex; align-items:center; gap:.4rem; }
  blockquote.callout-warning strong:first-child::before { content:"\26A0"; }
  blockquote.callout-note strong:first-child::before { content:"\2139"; }
  blockquote.callout-tip strong:first-child::before { content:"\1F4A1"; }

  .table-wrap { overflow-x:auto; margin:1.3rem 0; border:1px solid var(--border); border-radius:12px; }
  table { border-collapse:collapse; width:100%; font-size:.9rem; }
  th,td { border-bottom:1px solid var(--border); padding:.55rem .8rem; text-align:left; vertical-align:top; }
  thead th { background:var(--panel2); font-family:var(--mono); font-size:.78rem; letter-spacing:.04em; position:sticky; top:0; }
  tbody tr:hover { background:var(--accent-soft); }

  code { font-family:var(--mono); background:var(--panel2); padding:.1rem .35rem; border-radius:5px; font-size:.85em; }
  .codeblock { position:relative; }
  pre { background:var(--panel2); border:1px solid var(--border); border-radius:12px; padding:1rem 1.1rem; overflow-x:auto; font-family:var(--mono); }
  pre code { background:none; padding:0; }
  .copy-btn { position:absolute; top:.5rem; right:.5rem; opacity:0; transition:.15s; }
  .codeblock:hover .copy-btn { opacity:1; }

  .modnav { display:flex; justify-content:space-between; gap:1rem; margin-top:2.5rem; }
  .modnav a { flex:1; border:1px solid var(--border); border-radius:12px; padding:.9rem 1.1rem; background:var(--panel); cursor:pointer; }
  .modnav a:hover { border-color:var(--accent); text-decoration:none; }
  .modnav .dir { font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); }
  .modnav .ttl { font-family:var(--display); font-weight:700; display:block; margin-top:.2rem; }
  .modnav .next { text-align:right; }
  .modnav .disabled { opacity:.35; pointer-events:none; }

  #totop { position:fixed; right:1.1rem; bottom:1.1rem; z-index:40; width:42px; height:42px; border-radius:12px;
    border:1px solid var(--border); background:var(--panel); color:var(--fg); cursor:pointer; box-shadow:var(--shadow);
    opacity:0; pointer-events:none; transition:.2s; font-family:var(--mono); }
  #totop.show { opacity:1; pointer-events:auto; }
  footer { border-top:1px solid var(--border); color:var(--muted); font-family:var(--mono); font-size:.76rem; text-align:center; padding:2rem 1rem; }

  @media (max-width:760px) {
    .nav .search { display:none; } #menu { display:inline-flex; }
    .grid { grid-template-columns:1fr; }
  }
$highlighting-css$
</style>
</head>
<body>
<div id="progress-top"><i></i></div>
<header class="nav">
  <div class="nav-inner">
    <button class="brand" id="home-btn"><span class="mark">3D</span>$title$</button>
    <span class="search"><input type="search" id="search" placeholder="$search$" aria-label="$search$"></span>
$if(player_href)$    <a class="btn solid" href="$player_href$" title="$player_label$">▶ $player_label$</a>
$endif$$if(pdf_href)$    <a class="btn ghostline" href="$pdf_href$" title="$pdf$">⬇ $pdf$</a>
$endif$$if(sibling_href)$    <a class="btn ghostline" href="$sibling_href$">$sibling_label$</a>
$endif$    <button class="btn" id="theme-toggle" title="$theme$">◐</button>
    <button class="btn" id="menu" title="$theme$">◐</button>
  </div>
</header>

<div id="overview">
  <section class="hero">
    <div class="bg"></div>
    <div class="inner">
      <div class="eyebrow">$eyebrow$</div>
      <h1>$title$</h1>
$if(subtitle)$      <p class="subtitle">$subtitle$</p>
$endif$$if(abstract)$      <p class="lead">$abstract$</p>
$endif$      <div class="stats">
        <div class="stat"><b id="s-mod">8</b><span>$modules$</span></div>
        <div class="stat"><b id="s-words">—</b><span>$words$</span></div>
        <div class="stat"><b id="s-read">—</b><span>$read$</span></div>
      </div>
      <div class="cta">
        <button class="btn solid" id="start-btn">$start$ →</button>
$if(player_href)$        <a class="btn solid" href="$player_href$" title="$player_label$">▶ $player_label$</a>
$endif$$if(pdf_href)$        <a class="btn ghostline" href="$pdf_href$">⬇ $pdf$</a>
$endif$      </div>
    </div>
  </section>
  <div class="overall">
    <span class="lbl" id="overall-lbl"></span>
    <div class="track"><div class="fill" id="overall-fill"></div></div>
  </div>
  <div class="grid" id="grid"></div>
</div>

<div id="reader" hidden>
  <div class="module-bar">
    <div class="row">
      <button class="btn" id="back-btn">← $all$</button>
      <span class="idx" id="mod-idx"></span>
      <span class="spacer"></span>
      <button class="btn" id="complete-btn"></button>
    </div>
    <div class="pbar"><i id="mod-progress"></i></div>
  </div>
  <main class="reader-main">
    <div class="content" id="content">
$body$
    </div>
    <nav class="modnav" id="modnav"></nav>
  </main>
</div>

<button id="totop" title="$top$">↑</button>
<footer>$footer$</footer>

<script>
(function () {
  var root = document.documentElement, byId = function (i){ return document.getElementById(i); };
  var UI = { all:"$all$", complete:"$complete$", completed:"$completed$", module:"$module$",
             of:"$of$", chapters:"$chapters$", read:"$read$", progress:"$progress$", open:"$open$" };
  var DONE_KEY = "pf-done-$lang$";

  function setTheme(t){ root.setAttribute("data-theme", t); localStorage.setItem("pf-theme", t); }
  function toggleTheme(){ setTheme(root.getAttribute("data-theme") === "light" ? "dark" : "light"); }
  byId("theme-toggle").addEventListener("click", toggleTheme);
  byId("menu").addEventListener("click", toggleTheme);

  var modules = Array.prototype.slice.call(document.querySelectorAll("#content > section.level1"));
  var overview = byId("overview"), reader = byId("reader"), grid = byId("grid");

  function cleanTitle(h){
    var t = (h.textContent || "").trim();
    return t.replace(/^\s*\d+(\.\d+)*\s*/, "").replace(/^Module\s*\d+\s*[:.–-]\s*/i, "");
  }
  function getDone(){ try { return JSON.parse(localStorage.getItem(DONE_KEY)) || []; } catch (e){ return []; } }
  function setDone(list){ localStorage.setItem(DONE_KEY, JSON.stringify(list)); }
  function isDone(i){ return getDone().indexOf(i) >= 0; }
  function toggleDone(i){ var d = getDone(); var k = d.indexOf(i); if (k >= 0) d.splice(k,1); else d.push(i); setDone(d); }

  // Per-module metadata.
  var meta = modules.map(function (sec, i) {
    var h1 = sec.querySelector(":scope > h1");
    var chapters = sec.querySelectorAll(":scope > section.level2").length;
    var words = (sec.innerText || "").trim().split(/\s+/).length;
    var banner = sec.querySelector(".module-banner img");
    var firstP = sec.querySelector(":scope > blockquote, :scope > p");
    return { i:i, title: h1 ? cleanTitle(h1) : ("Module " + (i+1)), chapters:chapters, words:words,
             read: Math.max(1, Math.round(words/200)), thumb: banner ? banner.getAttribute("src") : "",
             blurb: firstP ? firstP.textContent.replace(/^[^:]*:\s*/, "") : "" };
  });

  // Hero stats.
  var totalWords = meta.reduce(function (a,m){ return a + m.words; }, 0);
  byId("s-mod").textContent = modules.length;
  byId("s-words").textContent = totalWords.toLocaleString();
  byId("s-read").textContent = Math.max(1, Math.round(totalWords/200));

  function pad(n){ return (n<10?"0":"") + n; }

  // Build overview cards.
  meta.forEach(function (m) {
    var card = document.createElement("div");
    card.className = "card"; card.style.animationDelay = (m.i*55) + "ms"; card.dataset.idx = m.i;
    card.innerHTML =
      '<div class="thumb"><span class="num">' + pad(m.i+1) + '</span>' +
      '<span class="check">✓</span>' + (m.thumb ? '<img alt="" src="' + m.thumb + '">' : '') + '</div>' +
      '<div class="body"><div class="meta">' + m.chapters + ' ' + UI.chapters + ' · ' + m.read + ' ' + UI.read + '</div>' +
      '<h3>' + m.title + '</h3><p class="blurb">' + m.blurb + '</p>' +
      '<div class="go">' + UI.open + ' →</div></div>';
    card.addEventListener("click", function(){ openModule(m.i); });
    grid.appendChild(card);
  });

  function refreshProgress(){
    var done = getDone().length;
    byId("overall-fill").style.width = (modules.length ? done/modules.length*100 : 0) + "%";
    byId("overall-lbl").textContent = done + " / " + modules.length + " " + UI.progress;
    meta.forEach(function (m){ grid.children[m.i].classList.toggle("done", isDone(m.i)); });
  }

  // Build chapter accordion for a module (once).
  function buildAccordion(sec){
    if (sec.dataset.acc) return;
    sec.dataset.acc = "1";
    sec.querySelectorAll(":scope > section.level2").forEach(function (ch) {
      var h2 = ch.querySelector(":scope > h2"); if (!h2) return;
      var body = document.createElement("div"); body.className = "chapter-body";
      while (h2.nextSibling) body.appendChild(h2.nextSibling);
      ch.appendChild(body);
      // All chapters start collapsed (CSS max-height:0). Animate open/close cleanly,
      // settling to 'none' when open so resizes/reflow never clip the content.
      h2.addEventListener("click", function(){
        if (ch.classList.contains("open")) {
          body.style.maxHeight = body.scrollHeight + "px";
          requestAnimationFrame(function(){ body.style.maxHeight = "0"; });
          ch.classList.remove("open");
        } else {
          ch.classList.add("open");
          body.style.maxHeight = body.scrollHeight + "px";
        }
      });
      body.addEventListener("transitionend", function(){
        if (ch.classList.contains("open")) body.style.maxHeight = "none";
      });
    });
  }

  function openModule(i){
    modules.forEach(function (s, k){ s.classList.toggle("active", k === i); });
    buildAccordion(modules[i]);
    overview.hidden = true; reader.hidden = false;
    byId("mod-idx").textContent = UI.module + " " + pad(i+1) + " " + UI.of + " " + pad(modules.length);
    var cb = byId("complete-btn");
    function syncComplete(){ var d = isDone(i); cb.textContent = (d ? "✓ " : "○ ") + (d ? UI.completed : UI.complete); cb.classList.toggle("solid", d); }
    cb.onclick = function(){ toggleDone(i); syncComplete(); refreshProgress(); }; syncComplete();
    buildModNav(i);
    location.hash = "m" + (i+1);
    window.scrollTo(0,0);
  }
  function showOverview(){ reader.hidden = true; overview.hidden = false; refreshProgress(); if (location.hash.indexOf("m") === 1) history.replaceState(null,"","#"); window.scrollTo(0,0); }

  function buildModNav(i){
    var nav = byId("modnav"); nav.innerHTML = "";
    function link(j, dir, label){
      var a = document.createElement("a"); a.className = dir + (j<0||j>=modules.length ? " disabled" : "");
      a.innerHTML = '<div class="dir">' + label + '</div>' + (meta[j] ? '<span class="ttl">' + meta[j].title + '</span>' : '');
      if (meta[j]) a.addEventListener("click", function(){ openModule(j); });
      return a;
    }
    nav.appendChild(link(i-1, "prev", "← $prev$"));
    nav.appendChild(link(i+1, "next", "$next$ →"));
  }

  byId("home-btn").addEventListener("click", showOverview);
  byId("back-btn").addEventListener("click", showOverview);
  byId("start-btn").addEventListener("click", function(){ openModule(0); });

  // Decorate content: callouts, tables, code copy buttons.
  var KINDS = { warning:["warning","avertissement","attention","danger"], note:["note","remarque","important"], tip:["pro tip","tip","astuce","conseil"] };
  document.querySelectorAll("#content blockquote").forEach(function (bq){
    var s = bq.querySelector("strong"); if (!s) return; var label = s.textContent.toLowerCase();
    for (var k in KINDS) if (KINDS[k].some(function (w){ return label.indexOf(w) === 0; })) { bq.classList.add("callout-"+k); break; }
  });
  document.querySelectorAll("#content table").forEach(function (t){ var w = document.createElement("div"); w.className="table-wrap"; t.parentNode.insertBefore(w,t); w.appendChild(t); });
  document.querySelectorAll("#content pre").forEach(function (pre){
    var w = document.createElement("div"); w.className="codeblock"; pre.parentNode.insertBefore(w,pre); w.appendChild(pre);
    var b = document.createElement("button"); b.className="btn copy-btn"; b.textContent="Copy";
    b.addEventListener("click", function(){ navigator.clipboard.writeText(pre.innerText).then(function(){ b.textContent="✓"; setTimeout(function(){ b.textContent="Copy"; },1200); }); });
    w.appendChild(b);
  });

  // Reading progress within the reader + back-to-top.
  function onScroll(){
    var h = root, max = h.scrollHeight - h.clientHeight;
    var pct = max>0 ? h.scrollTop/max*100 : 0;
    byId("progress-top").firstElementChild.style.width = pct + "%";
    if (!reader.hidden) byId("mod-progress").style.width = pct + "%";
    var tt = byId("totop"); if (h.scrollTop>500) tt.classList.add("show"); else tt.classList.remove("show");
  }
  document.addEventListener("scroll", onScroll, { passive:true });
  byId("totop").addEventListener("click", function(){ window.scrollTo({ top:0, behavior:"smooth" }); });

  // Search filters the module grid.
  byId("search").addEventListener("input", function (e){
    var q = e.target.value.trim().toLowerCase();
    meta.forEach(function (m){
      var hay = (m.title + " " + m.blurb).toLowerCase();
      grid.children[m.i].style.display = (!q || hay.indexOf(q) >= 0) ? "" : "none";
    });
  });

  refreshProgress();
  var m = location.hash.match(/^#m(\d+)/);
  if (m){ var idx = parseInt(m[1],10)-1; if (idx>=0 && idx<modules.length) openModule(idx); }
})();
</script>
</body>
</html>
"""


def data_uri(path: Path, mime: str) -> str:
    """Return a base64 data URI for *path* with the given MIME type."""
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def font_faces(fonts_dir: Path) -> str:
    """Return @font-face rules embedding each woff2 as base64."""
    rules = []
    for family, weight, filename in FONTS:
        uri = data_uri(fonts_dir / filename, "font/woff2")
        rules.append(
            f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"font-display:swap;src:url({uri}) format('woff2');}}")
    return "\n".join(rules)


def build(src: Path, out: Path, lang: str, assets_dir: Path, hero: Path, fonts_dir: Path,
          sibling_href: str, sibling_label: str, pdf_href: str,
          player_href: str = "", player_label: str = "") -> None:
    """Enrich, render, and write the self-contained module-centric web app for one language."""
    ui = UI[lang]
    enriched = enrich_markdown(src.read_text(encoding="utf-8"), lang, assets_dir)
    template = (TEMPLATE
                .replace("__FONTS__", font_faces(fonts_dir))
                .replace("__HERO_BG__", data_uri(hero, "image/jpeg")))

    work = Path(tempfile.mkdtemp(prefix="pf-html-"))
    try:
        (work / "course.md").write_text(enriched, encoding="utf-8")
        (work / "template.html").write_text(template, encoding="utf-8")

        cmd = [
            "pandoc", str(work / "course.md"), "-o", str(out),
            "--from=markdown-implicit_figures",
            "--standalone", "--embed-resources", "--section-divs", "--number-sections",
            "--shift-heading-level-by=-1",
            "--template", str(work / "template.html"),
            "--highlight-style", "pygments",
            "-V", f"lang={lang}",
        ]
        for key, value in ui.items():
            cmd += ["-V", f"{key}={value}"]
        if sibling_href:
            cmd += ["-V", f"sibling_href={sibling_href}", "-V", f"sibling_label={sibling_label}"]
        if pdf_href:
            cmd += ["-V", f"pdf_href={pdf_href}"]
        if player_href:
            cmd += ["-V", f"player_href={player_href}", "-V", f"player_label={player_label}"]

        subprocess.run(cmd, check=True, cwd=work)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--lang", required=True)
    parser.add_argument("--assets-dir", required=True, type=Path)
    parser.add_argument("--hero", required=True, type=Path)
    parser.add_argument("--fonts-dir", required=True, type=Path)
    parser.add_argument("--sibling-href", default="")
    parser.add_argument("--sibling-label", default="")
    parser.add_argument("--pdf-href", default="")
    parser.add_argument("--player-href", default="")
    parser.add_argument("--player-label", default="")
    args = parser.parse_args()
    build(args.src, args.out, args.lang, args.assets_dir, args.hero, args.fonts_dir,
          args.sibling_href, args.sibling_label, args.pdf_href, args.player_href, args.player_label)


if __name__ == "__main__":
    main()
