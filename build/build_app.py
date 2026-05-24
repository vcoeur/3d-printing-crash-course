#!/usr/bin/env python3
"""Build the unified, phone-first single-page web app (player/site/index.html).

One file, one URL, three views switched in place by a GET parameter:

    index.html?lang=<en|fr>&view=<watch|read|pdf>&at=<m.c.s>[&speed=<x>][&cc=0]

* watch — the animated, narrated player (reads course.json + diagrams.js + audio/ at runtime).
* read  — the course prose for the active language (rendered here at build time, both langs
          embedded; images load relatively from assets/images/ in the bundle).
* pdf   — opens course_<lang>.pdf.

This module is the single source of the online app: the unified dark template below carries
the full watch + read + router JS inline, so there is no separate player.html to drift. The
self-contained offline deliverables (dist/course_<lang>.{html,pdf}) are still built by
build_all.sh and are unaffected.

Pipeline per language: consolidate.py -> enrich_markdown (HTML diagrams + banners) -> pandoc
(body fragment, --section-divs / --number-sections) -> embed. Run from the repo root.
"""

import argparse
import base64
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from enrich import enrich_markdown  # noqa: E402

LANGS = ("en", "fr")

FONTS = [
    ("Bricolage Grotesque", 700, "bricolage-700.woff2"),
    ("Bricolage Grotesque", 800, "bricolage-800.woff2"),
    ("Spline Sans", 400, "spline-400.woff2"),
    ("Spline Sans", 600, "spline-600.woff2"),
    ("Spline Sans Mono", 400, "splinemono-400.woff2"),
    ("Spline Sans Mono", 600, "splinemono-600.woff2"),
]

# Pandoc emits only the rendered body when given this template.
BODY_TEMPLATE = "$body$"


def font_faces(fonts_dir: Path) -> str:
    """Return @font-face rules embedding each woff2 as a base64 data URI."""
    rules = []
    for family, weight, filename in FONTS:
        data = base64.b64encode((fonts_dir / filename).read_bytes()).decode("ascii")
        rules.append(
            f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"font-display:swap;src:url(data:font/woff2;base64,{data}) format('woff2');}}")
    return "\n".join(rules)


def render_body(modules_dir: Path, lang: str) -> str:
    """Consolidate + enrich + render one language's course markdown to an HTML body fragment.

    Image paths stay relative (assets/images/…); the bundle ships the images, so the fragment
    is light and the single file stays small.
    """
    work = Path(tempfile.mkdtemp(prefix="pf-app-"))
    try:
        consolidated = work / f"course_{lang}.md"
        subprocess.run(
            [sys.executable, str(Path(__file__).parent / "consolidate.py"),
             "--lang", lang, "--modules-dir", str(modules_dir), "--out", str(consolidated)],
            check=True)
        enriched = enrich_markdown(consolidated.read_text(encoding="utf-8"), lang, Path("assets/images"))
        (work / "enriched.md").write_text(enriched, encoding="utf-8")
        (work / "body.html").write_text(BODY_TEMPLATE, encoding="utf-8")
        out = subprocess.run(
            ["pandoc", str(work / "enriched.md"),
             "--from=markdown-implicit_figures", "--standalone", "--section-divs",
             "--number-sections", "--shift-heading-level-by=-1",
             "--template", str(work / "body.html"), "--highlight-style", "pygments",
             "-V", f"lang={lang}"],
            check=True, capture_output=True, text=True)
        return out.stdout
    finally:
        import shutil
        shutil.rmtree(work, ignore_errors=True)


def build(repo: Path, out: Path) -> None:
    """Assemble player/site-style index.html from the unified template and both prose bodies."""
    fonts = font_faces(repo / "assets" / "fonts")
    bodies = {lang: render_body(repo / "course_modules" / lang, lang) for lang in LANGS}
    html = (APP_TEMPLATE
            .replace("__FONTS__", fonts)
            .replace("__BODY_EN__", bodies["en"])
            .replace("__BODY_FR__", bodies["fr"]))
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size:,} bytes)")


# The unified template is assembled with str.replace (never fed to pandoc), so the inline JS
# is free to use template literals and $ — no pandoc-variable collisions to avoid.
APP_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0e1014">
<title>3D Printing Crash Course</title>
<style>
__FONTS__
:root{
  --bg:#0e1014; --panel:#15181f; --panel2:#1b1f28; --line:#272c38;
  --ink:#e8eaf0; --muted:#9aa3b6; --accent:#ff7a2f; --accent-soft:#ffb066;
  --good:#39d98a; --warn:#ffcf5c; --bad:#ff6b6b;
  --display:"Bricolage Grotesque",Georgia,serif;
  --body:"Spline Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
  --mono:"Spline Sans Mono",ui-monospace,Menlo,monospace;
  --nav-w:300px; --header-h:54px;
}
*{box-sizing:border-box}
html{height:100%}
body{margin:0;height:100%;background:var(--bg);color:var(--ink);
  font:15px/1.5 var(--body);display:flex;flex-direction:column;overflow:hidden;
  -webkit-text-size-adjust:100%}

/* ---- top reading-progress bar (read view) ---- */
#progress{position:fixed;top:0;left:0;height:3px;width:100%;z-index:80;pointer-events:none}
#progress>i{display:block;height:100%;width:0;background:var(--accent);transition:width .1s linear}
body[data-view="watch"] #progress{display:none}

/* ---- shared header ---- */
header.topbar{display:flex;align-items:center;gap:10px;flex:none;height:var(--header-h);
  padding:0 14px;background:linear-gradient(90deg,#12151c,#171b24);border-bottom:1px solid var(--line);
  padding-top:env(safe-area-inset-top)}
.topbar .ic{display:none;background:var(--panel2);border:1px solid var(--line);color:var(--ink);
  width:38px;height:38px;border-radius:10px;font-size:17px;cursor:pointer;flex:none}
.brand{font-family:var(--display);font-weight:800;font-size:16px;white-space:nowrap}
.brand .a{color:var(--accent)}
.brand .full{display:inline}.brand .short{display:none}
.grow{flex:1}
.modes{display:flex;background:var(--panel2);border:1px solid var(--line);border-radius:999px;padding:3px;gap:2px}
.modes a{display:flex;align-items:center;gap:5px;color:var(--muted);text-decoration:none;
  padding:6px 13px;border-radius:999px;font-weight:700;font-size:13px;cursor:pointer;white-space:nowrap}
.modes a:hover{color:var(--ink)}
.modes a.active{background:var(--accent);color:#1a1205}
.seg{display:flex;background:var(--panel2);border:1px solid var(--line);border-radius:8px;overflow:hidden}
.seg button{border:0;background:transparent;color:var(--muted);padding:6px 11px;cursor:pointer;font-size:12.5px;font-weight:600}
.seg button:hover{color:var(--ink)}
.seg button.active{background:var(--accent);color:#1a1205}

/* ---- layout: nav + main ---- */
.body{display:flex;flex:1;min-height:0;position:relative}
aside#nav{width:var(--nav-w);flex:none;background:var(--panel);border-right:1px solid var(--line);
  overflow-y:auto;padding:8px 0;-webkit-overflow-scrolling:touch}
#scrim{display:none;position:absolute;inset:0;background:rgba(0,0,0,.55);z-index:40}
main{flex:1;display:flex;flex-direction:column;min-width:0;
  background:radial-gradient(1200px 600px at 70% -10%,#171c27,#0e1014)}

/* nav items */
.mod{border-bottom:1px solid var(--line)}
.mod>.modhead{display:flex;align-items:center;gap:8px;padding:11px 14px;cursor:pointer;user-select:none;font-weight:700;font-size:13.5px}
.mod>.modhead .num{width:22px;height:22px;flex:none;border-radius:6px;background:var(--panel2);border:1px solid var(--line);display:grid;place-items:center;font-size:12px;color:var(--accent-soft);font-weight:800}
.mod>.modhead .chev{margin-left:auto;color:var(--muted);transition:transform .2s}
.mod.open>.modhead .chev{transform:rotate(90deg)}
.chapters{display:none;padding:2px 0 8px}
.mod.open .chapters{display:block}
.chapters a{display:flex;gap:9px;align-items:center;padding:8px 14px 8px 22px;color:var(--muted);text-decoration:none;font-size:13px;border-left:3px solid transparent;cursor:pointer}
.chapters a .cnum{color:#5b6478;font-variant-numeric:tabular-nums;font-size:12px}
.chapters a:hover{color:var(--ink);background:#191d26}
.chapters a.active{color:var(--ink);background:#1d2230;border-left-color:var(--accent)}

/* ---- views ---- */
#watch,#read{flex:1;min-height:0}
body[data-view="watch"] #read{display:none}
body[data-view="read"] #watch{display:none}

/* ===== WATCH ===== */
#watch{display:flex;flex-direction:column}
.crumb{padding:9px 18px;color:var(--muted);font-size:12.5px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:10px}
.crumb b{color:var(--ink)}
.crumb .pos{margin-left:auto;font-variant-numeric:tabular-nums}
.stagewrap{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:14px 16px;min-height:0;overflow:hidden}
.stage{flex:0 1 auto;min-height:0;max-height:100%;width:min(100%,960px);aspect-ratio:16/9;
  background:linear-gradient(160deg,#161a23,#10131a);border:1px solid var(--line);border-radius:16px;
  box-shadow:0 24px 60px rgba(0,0,0,.45),0 0 0 1px rgba(255,122,47,.06);
  position:relative;overflow:hidden;padding:38px 44px;display:flex;flex-direction:column;justify-content:center}
.stage::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(120% 120% at 50% 0%,transparent 60%,rgba(0,0,0,.30))}
.content{position:relative;overflow:hidden}
.content-inner{transform-origin:center center}
.kicker{color:var(--accent);font-weight:800;letter-spacing:1.5px;text-transform:uppercase;font-size:12px;margin:0 0 10px}
.s-title{font-family:var(--display);font-size:32px;line-height:1.12;margin:0 0 12px;font-weight:800}
.lead{font-size:18px;color:#cfd5e2;max-width:48ch;margin:0 0 6px}
ul.points{list-style:none;margin:8px 0 0;padding:0;max-width:62ch}
ul.points li{position:relative;padding:5px 0 5px 26px;font-size:15px;color:#d7dce8}
ul.points li::before{content:"";position:absolute;left:3px;top:12px;width:9px;height:9px;border-radius:3px;background:var(--accent)}
ul.points li b{color:#fff}
.compare{display:flex;gap:18px;margin-top:12px}
.compare .card{flex:1;background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:15px}
.compare .card.hi{border-color:#3a2a17;box-shadow:inset 0 0 0 1px rgba(255,122,47,.30)}
.compare .card h3{margin:0 0 8px;font-size:15px}
.compare .note{color:var(--muted);font-size:13px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-top:12px}
.cards .c{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:12px}
.cards .c .t{font-weight:800;color:var(--accent-soft);font-size:14px}
.cards .c .d{color:var(--muted);font-size:12.5px;margin-top:5px;line-height:1.4}
.cards .c.hi{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
.timeline{margin-top:18px;position:relative}
.timeline .rail{position:absolute;left:0;right:0;top:9px;height:3px;background:var(--line)}
.timeline .nodes{display:flex;justify-content:space-between;gap:10px;position:relative}
.timeline .node{flex:1;text-align:center}
.timeline .node .dot{width:16px;height:16px;border-radius:50%;background:var(--accent);margin:0 auto 10px;box-shadow:0 0 0 4px rgba(255,122,47,.18)}
.timeline .node .yr{font-weight:800;font-size:16px}
.timeline .node .lb{color:var(--muted);font-size:11.5px;margin-top:3px;line-height:1.35}
.pipe{display:flex;align-items:stretch;gap:6px;margin-top:16px;flex-wrap:wrap}
.pipe .step{flex:1;min-width:104px;background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:11px 10px;text-align:center}
.pipe .step .s{font-weight:800;font-size:14px}
.pipe .step .f{color:var(--muted);font-size:11px;margin-top:4px}
.pipe .arrow{color:var(--accent);font-size:20px;align-self:center;flex:none}
.stages{display:flex;gap:0;margin-top:16px;align-items:stretch}
.stages .zone{flex:1;padding:12px 10px;text-align:center;border:1px solid var(--line);border-left:0}
.stages .zone:first-child{border-left:1px solid var(--line);border-radius:10px 0 0 10px}
.stages .zone:last-child{border-radius:0 10px 10px 0}
.stages .zone:nth-child(1){background:#16202b}.stages .zone:nth-child(2){background:#1c2433}
.stages .zone:nth-child(3){background:#241d2b}.stages .zone:nth-child(4){background:#2a1d16}
.stages .zone:nth-child(5){background:#2b2516}
.stages .zone .z{font-weight:800;font-size:13px}
.stages .zone .t{font-size:11px;color:var(--muted);margin-top:4px}
.stat{display:flex;align-items:baseline;gap:16px;margin-top:12px}
.stat .v{font-size:50px;font-weight:800;color:var(--accent);line-height:1}
.stat .cap{color:#cfd5e2;font-size:16px;max-width:34ch}
.callout{margin-top:12px;border-left:4px solid var(--accent);background:var(--panel2);border-radius:0 10px 10px 0;padding:10px 14px;font-size:14px;color:#dbe0ec}
.callout.tip{border-left-color:var(--good)} .callout.warning{border-left-color:var(--warn)} .callout.note{border-left-color:var(--accent)}
.callout .lbl{font-weight:800;text-transform:uppercase;font-size:11px;letter-spacing:1px;margin-right:8px}
.callout.tip .lbl{color:var(--good)} .callout.warning .lbl{color:var(--warn)} .callout.note .lbl{color:var(--accent-soft)}
table.t{border-collapse:collapse;margin-top:12px;font-size:13px;width:100%}
table.t th,table.t td{border:1px solid var(--line);padding:6px 10px;text-align:left}
table.t th{background:var(--panel2);color:var(--accent-soft);font-weight:700}
.diagram{margin-top:14px;display:flex;justify-content:center}
.diagram svg{max-width:100%;height:auto;max-height:46vh}
.diagram .d-label{font:600 12px var(--mono);fill:var(--ink)}
.diagram .d-sub{font:11px sans-serif;fill:var(--muted)}
.diagram .d-accent{fill:var(--accent)} .diagram .d-stroke{stroke:var(--ink)} .diagram .d-line{stroke:var(--line)}
.reveal{opacity:0;transform:translateY(12px);transition:opacity .5s ease,transform .5s ease}
.reveal.on{opacity:1;transform:none}
.captions{position:absolute;left:0;right:0;bottom:14px;display:flex;justify-content:center;pointer-events:none}
.captions span{background:rgba(8,10,14,.82);color:#eef1f7;padding:7px 14px;border-radius:8px;font-size:14px;max-width:82%;text-align:center}
body.nocap .captions{display:none}
.dock{flex:none;width:min(100%,960px);background:#12151c;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.controls{display:flex;align-items:center;gap:12px;padding:10px 18px 4px}
.controls button.ic2{background:var(--panel2);border:1px solid var(--line);color:var(--ink);width:38px;height:38px;border-radius:10px;cursor:pointer;font-size:14px;flex:none}
.controls button.play{width:46px;height:46px;background:var(--accent);border-color:var(--accent);color:#1a1205;font-size:18px;flex:none}
.controls button.ic2:hover{border-color:var(--accent)}
.scrub{flex:1;display:flex;align-items:center;gap:10px;min-width:0}
.track{flex:1;height:8px;background:var(--panel2);border:1px solid var(--line);border-radius:999px;position:relative;cursor:pointer}
.track .fill{position:absolute;left:0;top:0;bottom:0;background:linear-gradient(90deg,var(--accent-soft),var(--accent));border-radius:999px;width:0}
.track .head{position:absolute;top:50%;width:14px;height:14px;border-radius:50%;background:#fff;transform:translate(-50%,-50%);box-shadow:0 1px 4px rgba(0,0,0,.5);left:0}
.dots{display:flex;gap:3px;align-items:center;flex-wrap:wrap;max-width:32%}
.dots i{width:9px;height:9px;border-radius:50%;background:var(--panel2);border:1px solid var(--line);cursor:pointer;display:block}
.dots i.done{background:var(--accent)} .dots i.cur{background:var(--accent-soft);box-shadow:0 0 0 2px rgba(255,122,47,.35)}
.time{color:var(--muted);font-variant-numeric:tabular-nums;font-size:12.5px;min-width:84px;text-align:right}
.settings{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:8px 18px 12px;border-top:1px solid var(--line)}
.settings .slab{color:var(--muted);font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.settings .sep{width:1px;height:20px;background:var(--line);margin:0 4px}
.loading{display:grid;place-items:center;height:100%;color:var(--muted);padding:24px;text-align:center}

/* ===== READ ===== */
#read{overflow-y:auto;-webkit-overflow-scrolling:touch}
.readwrap{max-width:880px;margin:0 auto;padding:2rem 1.3rem 5rem}
.readbody{display:none}.readbody.on{display:block}
.readbody section.level1{display:none}
.readbody section.level1.active{display:block;animation:fade .35s ease}
@keyframes fade{from{opacity:0;transform:translateY(8px)}to{opacity:1}}
.readbody section.level1>h1{font-family:var(--display);font-weight:800;font-size:clamp(1.7rem,5vw,2.6rem);
  line-height:1.05;letter-spacing:-.02em;margin:.2rem 0 1rem}
.readbody h1 .header-section-number{display:none}
.readbody{font-size:17px;line-height:1.7;color:var(--ink)}
.readbody a{color:var(--accent-soft);text-decoration:none}.readbody a:hover{text-decoration:underline}
.module-banner{margin:0 0 1.4rem}
.module-banner img{width:100%;max-height:420px;object-fit:contain;border-radius:14px;background:var(--panel2);display:block}
.module-banner p{margin:.5rem 0 0;font-family:var(--mono);font-size:.74rem;color:var(--muted);text-align:center;letter-spacing:.04em}
.readbody .diagram{display:block;position:relative;margin:1.6rem 0;background:var(--panel2);border:1px solid var(--line);border-radius:16px;padding:2rem 1.1rem 1rem}
.readbody .diagram::before{content:"SCHEMATIC";position:absolute;top:.7rem;left:1.1rem;font-family:var(--mono);font-size:.62rem;letter-spacing:.2em;color:var(--muted)}
html[lang="fr"] .readbody .diagram::before{content:"SCHÉMA"}
.readbody .diagram>p{margin:1rem 0 0;text-align:center;font-family:var(--mono);font-size:.74rem;color:var(--muted)}
.schema-flow{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:.35rem .1rem}
.sunit{display:inline-flex;align-items:center}
.snode{display:inline-block;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.55rem .8rem;font-weight:600;font-size:.9rem;text-align:center;max-width:170px}
.snode.accent{background:linear-gradient(135deg,var(--accent),#ffae6b);color:#1a1205;border-color:transparent}
.sarrow{width:24px;height:2px;background:var(--accent);margin:0 .3rem;position:relative;flex:0 0 auto}
.sarrow::after{content:"";position:absolute;right:-1px;top:-3px;border-left:7px solid var(--accent);border-top:4px solid transparent;border-bottom:4px solid transparent}
.schema-tree{display:flex;flex-direction:column;align-items:center;gap:1rem}
.sroot{background:linear-gradient(135deg,var(--accent),#ffae6b);color:#1a1205;font-family:var(--display);font-weight:700;padding:.55rem 1.1rem;border-radius:10px;font-size:1.05rem;position:relative}
.sroot::after{content:"";position:absolute;bottom:-11px;left:50%;transform:translateX(-50%);border-top:7px solid var(--accent);border-left:5px solid transparent;border-right:5px solid transparent}
.sfan{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;width:100%}
.sgroup{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:.7rem .9rem}
.sgroup-h{font-family:var(--mono);font-size:.74rem;letter-spacing:.05em;text-transform:uppercase;color:var(--accent-soft);font-weight:600;margin-bottom:.4rem}
.sgroup ul{margin:0;padding-left:1.05rem}.sgroup li{font-size:.88rem;margin:.15rem 0}
.schema-dec{display:flex;flex-direction:column;align-items:center;gap:.3rem}
.drow{display:flex;align-items:center;gap:.55rem;flex-wrap:wrap;justify-content:center;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.5rem .9rem}
.drow .dq{font-weight:600}.drow .darr,.drow .dlbl{font-family:var(--mono);font-size:.76rem;color:var(--muted)}
.drow .dout{font-weight:700}.drow .dout.accent{color:var(--accent)}
.drow.dfin{border-color:var(--accent)}.dno{font-family:var(--mono);font-size:.72rem;color:var(--muted)}
section.level2{border:1px solid var(--line);border-radius:14px;margin:.8rem 0;overflow:hidden;background:var(--panel)}
section.level2>h2{cursor:pointer;margin:0;padding:1rem 1.1rem;font-family:var(--display);font-weight:700;font-size:1.12rem;display:flex;align-items:center;gap:.7rem;user-select:none}
section.level2>h2 .header-section-number{font-family:var(--mono);font-weight:600;font-size:.85rem;color:var(--accent);background:rgba(255,122,47,.14);border-radius:7px;padding:.15rem .5rem}
section.level2>h2::after{content:"+";margin-left:auto;font-family:var(--mono);color:var(--muted);font-size:1.2rem}
section.level2.open>h2::after{content:"\2212";color:var(--accent)}
.chapter-body{padding:0 1.1rem;max-height:0;overflow:hidden;transition:max-height .35s ease}
section.level2.open .chapter-body{padding:.2rem 1.1rem 1.1rem}
.readbody h3{font-family:var(--display);font-weight:700;font-size:1.16rem;margin-top:1.5rem}
.readbody h4{font-size:1.02rem;margin-top:1.2rem}
.readbody h5{font-family:var(--mono);font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.readbody hr{display:none}
.readbody p,.readbody li{overflow-wrap:break-word}
.readbody blockquote{margin:1.2rem 0;padding:.7rem 1.05rem;border-left:3px solid var(--line);background:var(--panel2);border-radius:0 10px 10px 0}
.readbody blockquote p{margin:.3rem 0}
.readbody blockquote.callout-warning{border-left-color:var(--warn);background:#241a0c}
.readbody blockquote.callout-note{border-left-color:#5fb0ff;background:#0e1d2b}
.readbody blockquote.callout-tip{border-left-color:var(--good);background:#0e2018}
.table-wrap{overflow-x:auto;margin:1.3rem 0;border:1px solid var(--line);border-radius:12px}
.readbody table{border-collapse:collapse;width:100%;font-size:.9rem}
.readbody th,.readbody td{border-bottom:1px solid var(--line);padding:.55rem .8rem;text-align:left;vertical-align:top}
.readbody thead th{background:var(--panel2);font-family:var(--mono);font-size:.78rem;letter-spacing:.04em}
.readbody code{font-family:var(--mono);background:var(--panel2);padding:.1rem .35rem;border-radius:5px;font-size:.85em}
.readbody pre{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:1rem 1.1rem;overflow-x:auto;font-family:var(--mono)}
.readbody pre code{background:none;padding:0}
.modnav{display:flex;justify-content:space-between;gap:1rem;margin-top:2.5rem}
.modnav a{flex:1;border:1px solid var(--line);border-radius:12px;padding:.9rem 1.1rem;background:var(--panel);cursor:pointer;color:var(--ink);text-decoration:none}
.modnav a:hover{border-color:var(--accent)}
.modnav .dir{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.modnav .ttl{font-family:var(--display);font-weight:700;display:block;margin-top:.2rem}
.modnav .next{text-align:right}
.modnav .disabled{opacity:.35;pointer-events:none}

/* ===== phone-first responsive ===== */
@media (max-width:900px){
  .topbar .ic{display:block}
  aside#nav{position:absolute;top:0;bottom:0;left:0;z-index:50;width:min(86vw,320px);
    transform:translateX(-100%);transition:transform .25s ease;box-shadow:0 0 40px rgba(0,0,0,.6)}
  body.nav-open aside#nav{transform:none}
  body.nav-open #scrim{display:block}
  .brand .full{display:none}.brand .short{display:inline}
  .modes a span{display:none}              /* icon-only mode toggle on narrow screens */
  .modes a{padding:6px 10px}
  .stagewrap{padding:10px 10px 12px;justify-content:flex-start;gap:10px}
  .stage{padding:18px 18px;border-radius:12px;width:100%;aspect-ratio:auto;flex:1 1 auto}
  .crumb{flex-wrap:wrap;padding:8px 12px}
  .s-title{font-size:22px}.lead{font-size:15px}
  .controls{gap:8px;padding:10px 12px 4px}
  .dots{display:none}                      /* per-scene dots too dense on a phone */
  .time{min-width:0}
  .settings{padding:8px 12px 12px;gap:8px}
  .readwrap{padding:1.2rem 1rem 4rem}
  .compare{flex-direction:column;gap:10px}
}
@media (max-width:420px){
  .modes a{padding:6px 9px;font-size:12px}
  .seg button{padding:6px 9px}
}
</style>
</head>
<body data-view="watch">
<div id="progress"><i></i></div>
<header class="topbar">
  <button class="ic" id="navToggle" title="Modules" aria-label="Modules">☰</button>
  <div class="brand"><span class="full">3D Printing <span class="a">Crash Course</span></span><span class="short">3D <span class="a">Course</span></span></div>
  <div class="grow"></div>
  <nav class="modes">
    <a class="mode" data-view="watch" title="Watch the animated course">▶ <span class="lbl-watch">Watch</span></a>
    <a class="mode" data-view="read" title="Read the course">📖 <span class="lbl-read">Read</span></a>
    <a class="mode" id="pdfLink" data-view="pdf" title="Download PDF">⬇ <span>PDF</span></a>
  </nav>
  <div class="seg" id="langSeg"><button data-lang="en" class="active">EN</button><button data-lang="fr">FR</button></div>
</header>
<div class="body">
  <aside id="nav"></aside>
  <div id="scrim"></div>
  <main>
    <section id="watch">
      <div class="crumb" id="crumb"></div>
      <div class="stagewrap">
        <div class="stage" id="stage">
          <div class="content"><div class="content-inner" id="stage-content"></div></div>
          <div class="captions"><span id="caption"></span></div>
        </div>
        <div class="dock">
          <div class="controls">
            <button class="ic2" id="prev" title="Previous scene">⏮</button>
            <button class="play" id="play" title="Play / Pause">▶</button>
            <button class="ic2" id="next" title="Next scene">⏭</button>
            <div class="scrub">
              <div class="dots" id="dots"></div>
              <div class="track" id="track"><div class="fill" id="fill"></div><div class="head" id="head"></div></div>
              <div class="time" id="time">0:00 / 0:00</div>
            </div>
          </div>
          <div class="settings">
            <span class="slab" id="lab-speed">Speed</span>
            <div class="seg" id="speedSeg">
              <button data-s="0.75">0.75×</button><button data-s="1" class="active">1×</button>
              <button data-s="1.25">1.25×</button><button data-s="1.5">1.5×</button><button data-s="2">2×</button>
            </div>
            <span class="sep"></span>
            <span class="slab" id="lab-cc">Captions</span>
            <div class="seg" id="capSeg"><button data-cc="1" class="active" id="cc-on">On</button><button data-cc="0" id="cc-off">Off</button></div>
          </div>
        </div>
      </div>
    </section>
    <section id="read">
      <div class="readwrap">
        <div class="readbody" data-lang="en">__BODY_EN__</div>
        <div class="readbody" data-lang="fr">__BODY_FR__</div>
      </div>
    </section>
  </main>
</div>
<audio id="narration" preload="auto"></audio>
<script src="diagrams.js"></script>
<script>
const $=s=>document.querySelector(s);
const STR={
  en:{watch:"Watch",read:"Read",module:"Module",chapter:"Chapter",speed:"Speed",captions:"Captions",on:"On",off:"Off",prev:"Previous",next:"Next"},
  fr:{watch:"Voir",read:"Lire",module:"Module",chapter:"Chapitre",speed:"Vitesse",captions:"Sous-titres",on:"Activés",off:"Coupés",prev:"Précédent",next:"Suivant"}
};
const DIAGRAMS=window.DIAGRAMS||{};
let COURSE=null,lang="en",view="watch",speed=1,cc=true;
let mi=0,ci=0,si=0,playing=false,FLAT=[];
const audio=$("#narration");

const tr=v=>v==null?"":(typeof v==="string"?v:(v[lang]??v.en??""));
const curMod=()=>COURSE.modules[mi];
const curChap=()=>curMod().chapters[ci];
const curScenes=()=>curChap().scenes;
const curScene=()=>curScenes()[si];
function buildFlat(){FLAT=[];COURSE.modules.forEach((m,a)=>m.chapters.forEach((c,b)=>FLAT.push([a,b])));}
function flatIndex(){return FLAT.findIndex(([a,b])=>a===mi&&b===ci);}

/* ---- shared nav (drives both views) ---- */
function buildNav(){
  const nav=$("#nav");nav.innerHTML="";
  COURSE.modules.forEach((m,a)=>{
    const mod=document.createElement("div");mod.className="mod"+(a===mi?" open":"");
    const head=document.createElement("div");head.className="modhead";
    head.innerHTML=`<span class="num">${m.module}</span><span>${tr(m.module_title)}</span><span class="chev">›</span>`;
    head.onclick=()=>mod.classList.toggle("open");
    const ch=document.createElement("div");ch.className="chapters";
    m.chapters.forEach((c,b)=>{
      const link=document.createElement("a");
      link.className=(a===mi&&b===ci)?"active":"";link.dataset.a=a;link.dataset.b=b;
      link.innerHTML=`<span class="cnum">${m.module}.${c.chapter}</span><span>${tr(c.title)}</span>`;
      link.onclick=()=>{goto(a,b,0);closeNav();};
      ch.appendChild(link);
    });
    mod.appendChild(head);mod.appendChild(ch);nav.appendChild(mod);
  });
}
function markNav(){
  document.querySelectorAll(".chapters a").forEach(x=>x.classList.toggle("active",+x.dataset.a===mi&&+x.dataset.b===ci));
  const openMod=document.querySelectorAll(".mod")[mi];
  if(openMod&&!openMod.classList.contains("open"))openMod.classList.add("open");
}
function openNav(){document.body.classList.add("nav-open");}
function closeNav(){document.body.classList.remove("nav-open");}
$("#navToggle").onclick=()=>document.body.classList.toggle("nav-open");
$("#scrim").onclick=closeNav;

/* navigate to module a / chapter b / scene s, honouring the current view */
function goto(a,b,s){
  mi=a;ci=b;si=s||0;
  if(view==="watch"){renderScene();play(true);}
  else{showRead(true);}
  markNav();syncURL();
}

/* ===== WATCH ===== */
function el(e){
  switch(e.type){
    case"kicker":return `<p class="kicker reveal">${tr(e.text)}</p>`;
    case"title":return `<h1 class="s-title reveal">${tr(e.text)}</h1>`;
    case"lead":return `<p class="lead reveal">${tr(e.text)}</p>`;
    case"bullets":return `<ul class="points">${(e.items||[]).map(p=>`<li class="reveal">${tr(p)}</li>`).join("")}</ul>`;
    case"compare":{const c=s=>`<div class="card${s.highlight?' hi':''}"><h3>${tr(s.title)}</h3><div class="note">${tr(s.note)}</div></div>`;
      return `<div class="compare reveal">${c(e.left||{})}${c(e.right||{})}</div>`;}
    case"cards":return `<div class="cards">${(e.items||[]).map(c=>`<div class="c${c.highlight?' hi':''} reveal"><div class="t">${tr(c.title)}</div><div class="d">${tr(c.desc)}</div></div>`).join("")}</div>`;
    case"timeline":return `<div class="timeline reveal"><div class="rail"></div><div class="nodes">${(e.nodes||[]).map(n=>`<div class="node reveal"><div class="dot"></div><div class="yr">${tr(n.label)}</div><div class="lb">${tr(n.text)}</div></div>`).join("")}</div></div>`;
    case"pipeline":{const steps=(e.steps||[]).map(s=>`<div class="step reveal"><div class="s">${tr(s.name)}</div><div class="f">${tr(s.sub)}</div></div>`);
      return `<div class="pipe">${steps.join('<span class="arrow">→</span>')}</div>`;}
    case"stages":return `<div class="stages reveal">${(e.items||[]).map(z=>`<div class="zone reveal"><div class="z">${tr(z.label)}</div><div class="t">${tr(z.sub)}</div></div>`).join("")}</div>`;
    case"stat":return `<div class="stat reveal"><div class="v">${tr(e.value)}</div><div class="cap">${tr(e.caption)}</div></div>`;
    case"callout":{const v=e.variant||"note";
      const L=(lang==="fr"?{tip:"Astuce",note:"Note",warning:"Attention"}:{tip:"Tip",note:"Note",warning:"Warning"})[v];
      return `<div class="callout ${v} reveal"><span class="lbl">${L}</span>${tr(e.text)}</div>`;}
    case"table":{const h=(e.headers||[]).map(x=>`<th>${tr(x)}</th>`).join("");
      const rows=(e.rows||[]).map(r=>`<tr>${r.map(x=>`<td>${tr(x)}</td>`).join("")}</tr>`).join("");
      return `<table class="t reveal"><thead><tr>${h}</tr></thead><tbody>${rows}</tbody></table>`;}
    case"diagram":return DIAGRAMS[e.kind]?`<div class="diagram reveal">${DIAGRAMS[e.kind](lang,e)}</div>`:"";
    default:return "";
  }
}
let revealEls=[];
function renderScene(){
  const sc=curScene();
  $("#crumb").innerHTML=`${STR[lang].module} ${curMod().module} · <b>${tr(curMod().module_title)}</b> &nbsp;›&nbsp; ${STR[lang].chapter} ${curChap().chapter}: <b>${tr(curChap().title)}</b><span class="pos">${si+1} / ${curScenes().length}</span>`;
  const inner=$("#stage-content");
  inner.innerHTML=(sc.elements||[]).map(el).join("");
  fitContent();
  $("#caption").textContent=tr(sc.narration);
  revealEls=[...inner.querySelectorAll(".reveal")];
  audio.src=`audio/${lang}/${sc.id}.mp3`;audio.load();audio.playbackRate=speed;
  markNav();buildDots();updateScrub(0);applyReveal(0);
}
function applyReveal(frac){
  const n=revealEls.length||1;
  revealEls.forEach((node,i)=>{const th=(i/n)*0.66;node.classList.toggle("on",(!playing)||frac>=th);});
}
function fitContent(){
  const stage=$("#stage"),inner=$("#stage-content");if(!stage||!inner)return;
  inner.style.transform="none";
  const cs=getComputedStyle(stage);
  const avH=stage.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom);
  const avW=stage.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight);
  const need=inner.getBoundingClientRect();
  const k=Math.min(1,avH/need.height,avW/need.width);
  inner.style.transform=k<0.998?`scale(${k.toFixed(4)})`:"";
}
window.addEventListener("resize",()=>{if(COURSE&&view==="watch")fitContent();});
function buildDots(){
  const d=$("#dots");d.innerHTML="";const n=curScenes().length;
  for(let i=0;i<n;i++){const b=document.createElement("i");
    b.className=i<si?"done":i===si?"cur":"";b.onclick=()=>{si=i;renderScene();play(playing);};d.appendChild(b);}
}
function fmt(s){if(!isFinite(s))s=0;s=Math.max(0,Math.round(s));return `${Math.floor(s/60)}:${String(s%60).padStart(2,"0")}`;}
function updateScrub(frac){
  const dur=isFinite(audio.duration)?audio.duration:0;
  $("#fill").style.width=(frac*100)+"%";$("#head").style.left=(frac*100)+"%";
  $("#time").textContent=`${fmt(audio.currentTime||0)} / ${fmt(dur)}`;
}
function play(on){
  playing=on;$("#play").textContent=on?"❚❚":"▶";
  if(on){audio.playbackRate=speed;audio.play().catch(()=>{});}else audio.pause();
}
function toggle(){play(!playing);}
audio.addEventListener("timeupdate",()=>{const dur=audio.duration;const frac=isFinite(dur)&&dur>0?audio.currentTime/dur:0;applyReveal(frac);updateScrub(frac);});
audio.addEventListener("loadedmetadata",()=>{audio.playbackRate=speed;});
audio.addEventListener("ended",()=>nextScene(true));
audio.addEventListener("error",()=>{if(playing&&view==="watch")setTimeout(()=>nextScene(true),3500);});
function nextScene(auto){
  if(si<curScenes().length-1){si++;renderScene();if(playing||auto)play(true);syncURL();return;}
  const idx=flatIndex();
  if(idx<FLAT.length-1){[mi,ci]=FLAT[idx+1];si=0;renderScene();if(playing||auto)play(true);syncURL();}
  else{play(false);}
}
function prevScene(){
  if(si>0){si--;renderScene();play(playing);syncURL();return;}
  const idx=flatIndex();
  if(idx>0){[mi,ci]=FLAT[idx-1];si=COURSE.modules[mi].chapters[ci].scenes.length-1;renderScene();play(playing);syncURL();}
}
$("#play").onclick=toggle;$("#next").onclick=()=>nextScene(false);$("#prev").onclick=prevScene;
$("#track").addEventListener("click",ev=>{
  const dur=audio.duration;if(!isFinite(dur)||dur<=0)return;
  const r=ev.currentTarget.getBoundingClientRect();
  audio.currentTime=Math.min(1,Math.max(0,(ev.clientX-r.left)/r.width))*dur;
});
document.addEventListener("keydown",e=>{
  if(e.target.tagName==="INPUT")return;
  if(view!=="watch")return;
  if(e.code==="Space"){e.preventDefault();toggle();}
  if(e.code==="ArrowRight")nextScene(false);
  if(e.code==="ArrowLeft")prevScene();
});
$("#speedSeg").addEventListener("click",ev=>{const b=ev.target.closest("button");if(!b)return;setSpeed(parseFloat(b.dataset.s));});
function setSpeed(s){speed=s;audio.playbackRate=s;document.querySelectorAll("#speedSeg button").forEach(b=>b.classList.toggle("active",parseFloat(b.dataset.s)===s));syncURL();}
$("#capSeg").addEventListener("click",ev=>{const b=ev.target.closest("button");if(!b)return;setCC(b.dataset.cc==="1");});
function setCC(on){cc=on;document.body.classList.toggle("nocap",!on);document.querySelectorAll("#capSeg button").forEach(b=>b.classList.toggle("active",(b.dataset.cc==="1")===on));syncURL();}

/* ===== READ ===== */
let readModules=[];          // .level1 sections of the active-lang body
function activeReadBody(){return document.querySelector(`.readbody[data-lang="${lang}"]`);}
function wireRead(body){
  if(body.dataset.wired)return;body.dataset.wired="1";
  body.querySelectorAll(":scope > section.level1 > section.level2").forEach(ch=>{
    const h2=ch.querySelector(":scope > h2");if(!h2)return;
    const inner=document.createElement("div");inner.className="chapter-body";
    while(h2.nextSibling)inner.appendChild(h2.nextSibling);
    ch.appendChild(inner);
    h2.addEventListener("click",()=>{
      if(ch.classList.contains("open")){inner.style.maxHeight=inner.scrollHeight+"px";requestAnimationFrame(()=>inner.style.maxHeight="0");ch.classList.remove("open");}
      else{ch.classList.add("open");inner.style.maxHeight=inner.scrollHeight+"px";}
    });
    inner.addEventListener("transitionend",()=>{if(ch.classList.contains("open"))inner.style.maxHeight="none";});
  });
  body.querySelectorAll("blockquote").forEach(bq=>{
    const s=bq.querySelector("strong");if(!s)return;const t=s.textContent.toLowerCase();
    const K={warning:["warning","avertissement","attention","danger"],note:["note","remarque","important"],tip:["pro tip","tip","astuce","conseil"]};
    for(const k in K)if(K[k].some(w=>t.indexOf(w)===0)){bq.classList.add("callout-"+k);break;}
  });
  body.querySelectorAll("table").forEach(t=>{const w=document.createElement("div");w.className="table-wrap";t.parentNode.insertBefore(w,t);w.appendChild(t);});
  body.querySelectorAll(".modnav").forEach(n=>n.remove());
}
function showRead(scroll){
  document.querySelectorAll(".readbody").forEach(b=>b.classList.toggle("on",b.dataset.lang===lang));
  const body=activeReadBody();wireRead(body);
  readModules=[...body.querySelectorAll(":scope > section.level1")];
  readModules.forEach((s,k)=>s.classList.toggle("active",k===mi));
  buildModNav();
  // open + scroll to the active chapter
  const sec=readModules[mi];
  const target=sec&&sec.querySelector(`section.level2[data-number="${curMod().module}.${curChap().chapter}"]`);
  if(target){const inner=target.querySelector(".chapter-body");
    if(inner&&!target.classList.contains("open")){target.classList.add("open");inner.style.maxHeight="none";}}
  if(scroll){const rd=$("#read");
    if(target){rd.scrollTop=0;requestAnimationFrame(()=>{rd.scrollTop=target.offsetTop-12;});}
    else rd.scrollTop=0;}
  updateReadProgress();markNav();
}
function buildModNav(){
  const sec=readModules[mi];if(!sec)return;
  sec.querySelectorAll(":scope > .modnav").forEach(n=>n.remove());
  const nav=document.createElement("nav");nav.className="modnav";
  const mk=(j,dir,label)=>{
    const a=document.createElement("a");a.className=dir+((j<0||j>=COURSE.modules.length)?" disabled":"");
    const t=COURSE.modules[j]?tr(COURSE.modules[j].module_title):"";
    a.innerHTML=`<div class="dir">${label}</div><span class="ttl">${t}</span>`;
    if(COURSE.modules[j])a.onclick=()=>goto(j,0,0);
    return a;
  };
  nav.appendChild(mk(mi-1,"prev","← "+STR[lang].prev));
  nav.appendChild(mk(mi+1,"next",STR[lang].next+" →"));
  sec.appendChild(nav);
}
function updateReadProgress(){
  const rd=$("#read");const max=rd.scrollHeight-rd.clientHeight;
  const pct=max>0?rd.scrollTop/max*100:0;$("#progress").firstElementChild.style.width=pct+"%";
}
let scrollT=null;
$("#read").addEventListener("scroll",()=>{
  updateReadProgress();
  if(scrollT)return;scrollT=setTimeout(()=>{scrollT=null;syncReadPos();},220);
},{passive:true});
function syncReadPos(){
  // find the chapter heading nearest the top of the read pane → reflect into mi/ci/at.
  // Bail if read isn't the visible view: a debounced scroll tick can land after a switch
  // to watch, when #read is display:none and every rect reads 0 (would wrongly reset ci).
  if(view!=="read")return;
  const sec=readModules[mi];if(!sec)return;const rd=$("#read");
  const chaps=[...sec.querySelectorAll(":scope > section.level2")];
  let best=ci,bestTop=-1e9;
  chaps.forEach(ch=>{const top=ch.getBoundingClientRect().top-rd.getBoundingClientRect().top;
    if(top<=80&&top>bestTop){bestTop=top;best=chaps.indexOf(ch);}});
  const dn=chaps[best]&&chaps[best].dataset.number;       // "M.C"
  if(dn){const c=parseInt(dn.split(".")[1],10)-1;if(c>=0&&c!==ci){ci=c;si=0;markNav();syncURL();}}
}

/* ===== view + language switching ===== */
function setView(v){
  if(v==="pdf"){window.open(`course_${lang}.pdf`,"_blank");return;}
  view=v;document.body.dataset.view=v;
  document.querySelectorAll(".modes a").forEach(a=>a.classList.toggle("active",a.dataset.view===v));
  if(v==="watch"){if(playing)play(false);renderScene();fitContent();}
  else{showRead(true);}
  syncURL();
}
document.querySelectorAll(".modes a").forEach(a=>a.addEventListener("click",e=>{e.preventDefault();setView(a.dataset.view);}));
$("#langSeg").addEventListener("click",ev=>{const b=ev.target.closest("button");if(!b)return;setLang(b.dataset.lang);});
function setLang(l){
  lang=l;document.documentElement.lang=l;
  document.querySelectorAll("#langSeg button").forEach(b=>b.classList.toggle("active",b.dataset.lang===l));
  document.querySelector(".lbl-watch").textContent=STR[l].watch;
  document.querySelector(".lbl-read").textContent=STR[l].read;
  $("#lab-speed").textContent=STR[l].speed;$("#lab-cc").textContent=STR[l].captions;
  $("#cc-on").textContent=STR[l].on;$("#cc-off").textContent=STR[l].off;
  $("#pdfLink").title=`course_${l}.pdf`;
  buildNav();
  if(view==="watch"){const t=audio.currentTime;renderScene();
    if(t&&isFinite(t)){audio.addEventListener("loadedmetadata",function once(){audio.currentTime=Math.min(t,audio.duration||t);audio.removeEventListener("loadedmetadata",once);},{once:true});}
    play(playing);
  }else showRead(false);
  syncURL();
}

/* ===== bookmarkable URL ===== */
function syncURL(){
  if(!COURSE)return;
  const p=new URLSearchParams();
  p.set("lang",lang);p.set("view",view);
  p.set("at",`${curMod().module}.${curChap().chapter}.${si}`);
  if(speed!==1)p.set("speed",String(speed));
  if(!cc)p.set("cc","0");
  history.replaceState(null,"",`?${p.toString()}`);
}

fetch("course.json").then(r=>r.json()).then(data=>{
  COURSE=data;buildFlat();
  const q=new URLSearchParams(location.search);
  lang=q.get("lang")==="fr"?"fr":"en";
  view=["watch","read","pdf"].includes(q.get("view"))?q.get("view"):"watch";
  speed=parseFloat(q.get("speed"))||1;cc=q.get("cc")!=="0";
  if(q.get("at")){const[a,b,c]=q.get("at").split(".").map(Number);
    const mIx=COURSE.modules.findIndex(m=>m.module===a);
    if(mIx>=0){mi=mIx;const cIx=COURSE.modules[mIx].chapters.findIndex(ch=>ch.chapter===b);if(cIx>=0)ci=cIx;si=c||0;}}
  document.body.classList.toggle("nocap",!cc);
  document.querySelectorAll("#speedSeg button").forEach(b=>b.classList.toggle("active",parseFloat(b.dataset.s)===speed));
  document.querySelectorAll("#capSeg button").forEach(b=>b.classList.toggle("active",(b.dataset.cc==="1")===cc));
  // pdf as a landing view: open the pdf, but show watch underneath
  const landingPdf=view==="pdf";if(landingPdf)view="watch";
  setLang(lang);
  setView(view);
  if(landingPdf)window.open(`course_${lang}.pdf`,"_blank");
}).catch(()=>{$("#stage-content").innerHTML=`<div class="loading">Could not load course.json — serve this folder over HTTP (not file://).</div>`;});
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="repo root (defaults to the parent of build/)")
    parser.add_argument("--out", type=Path, required=True, help="output index.html path")
    args = parser.parse_args()
    build(args.repo, args.out)


if __name__ == "__main__":
    main()
