#!/usr/bin/env python3
"""Consolidate per-module course markdown into one all-in-one source document.

Reads ``module_NN_*.md`` files from a language directory, cleans them, and
concatenates them under a single YAML front-matter block so the result feeds
both the PDF build (``md_to_pdf.sh``) and the HTML build (``build_html.py``).

Cleaning applied to every module:
  * strip orphan ``[^NN^]`` / ``[^NN]`` reference markers (no definitions exist),
  * turn emoji callouts (``💡 **Pro Tip:**`` etc.) into plain blockquotes so
    xelatex does not silently drop the glyph,
  * demote every ATX heading by one level so module titles sit just under the
    document title (``md_to_pdf.sh`` shifts headings up by one again).
"""

import argparse
import re
from pathlib import Path

# Per-language document metadata (front matter). Body content comes from the
# module files; only the wrapper strings live here.
META = {
    "en": {
        "title": "3D Printing Crash Course",
        "subtitle": "The fast-track FDM & CoreXY course — Bambu Lab focused",
        "abstract": (
            "A comprehensive, beginner-to-advanced guide to FDM 3D printing, "
            "with a focus on CoreXY kinematics and the Bambu Lab ecosystem. "
            "Across eight modules it covers the technology and history of additive "
            "manufacturing, printer hardware, materials, slicer software, profile "
            "configuration and calibration, multi-material printing with AMS, and "
            "troubleshooting, safety, and best practices. By the end you will "
            "understand the reasoning behind every setting and mechanical choice "
            "and be equipped to diagnose problems and dial in high-quality prints."
        ),
    },
    "fr": {
        "title": "Cours accéléré d'impression 3D",
        "subtitle": "Le cours accéléré FDM et CoreXY — axé sur l'écosystème Bambu Lab",
        "abstract": (
            "Un guide complet de l'impression 3D FDM, du débutant à l'avancé, axé "
            "sur la cinématique CoreXY et l'écosystème Bambu Lab. À travers huit "
            "modules, il couvre la technologie et l'histoire de la fabrication "
            "additive, le matériel des imprimantes, les matériaux, les logiciels "
            "de tranchage, la configuration et la calibration des profils, "
            "l'impression multi-matériaux avec l'AMS, ainsi que le dépannage, la "
            "sécurité et les bonnes pratiques. À la fin, vous comprendrez le "
            "raisonnement derrière chaque réglage et chaque choix mécanique, et "
            "vous serez en mesure de diagnostiquer les problèmes et d'obtenir des "
            "impressions de haute qualité."
        ),
    },
}

# Orphan reference markers: [^18^], [^161^], and the plain [^18] variant. A
# leading space is consumed so " text [^9^]." collapses to " text." cleanly.
RE_FOOTNOTE = re.compile(r"\s*\[\^\d+\^?\]")
# Pictographic emoji (incl. 💡 ⚠ 📝) plus the variation selector. Ranges are
# chosen to leave wanted symbols such as → (U+2192) and ≤ (U+2264) untouched.
RE_EMOJI = re.compile(r"[\U0001F300-\U0001FAFF\U00002600-\U000027BF️]")
RE_HEADING = re.compile(r"^(#{1,6})(\s)")
RE_FENCE = re.compile(r"^\s*```")
RE_SPACE_BEFORE_PUNCT = re.compile(r" +([.,;:!?])")

# Chars Latin Modern (xelatex default) lacks; mapped to LaTeX only for the PDF
# source. The canonical markdown keeps the real glyphs, which render fine in HTML.
SUPERSCRIPTS = "⁰¹²³⁴⁵⁶⁷⁸⁹"  # U+2070, U+00B9, U+00B2, U+00B3, U+2074..U+2079
SUBSCRIPTS = "₀₁₂₃₄₅₆₇₈₉"  # U+2080..U+2089 (e.g. chemical formulae like CaCO₃)
LATEX_CHAR_MAP = {"μ": r"$\mu$"}
LATEX_CHAR_MAP.update(
    {glyph: rf"\textsuperscript{{{digit}}}" for digit, glyph in enumerate(SUPERSCRIPTS)}
)
LATEX_CHAR_MAP.update(
    {glyph: rf"\textsubscript{{{digit}}}" for digit, glyph in enumerate(SUBSCRIPTS)}
)


# Inline-code span, so $ inside `$PATH` is preserved while $ in prose is escaped.
RE_CODE_SPAN = re.compile(r"`[^`]*`")
RE_DOLLAR = re.compile(r"(?<!\\)\$")


def escape_dollars(line: str) -> str:
    """Escape every literal $ in prose (currency "$200", cost tiers "$$$") but not inside inline code.

    The course contains no real LaTeX math, so bare $ would otherwise pair up as
    pandoc inline/display-math delimiters and corrupt the output.
    """
    parts = RE_CODE_SPAN.split(line)
    spans = RE_CODE_SPAN.findall(line)
    rebuilt = []
    for index, prose in enumerate(parts):
        rebuilt.append(RE_DOLLAR.sub(r"\\$", prose))
        if index < len(spans):
            rebuilt.append(spans[index])
    return "".join(rebuilt)


def clean_prose_line(line: str, pdf_safe: bool) -> str:
    """Clean one non-code line: drop emoji and tidy spacing/callouts/headings/currency (footnotes handled globally)."""
    line = escape_dollars(line)
    if RE_EMOJI.search(line):
        line = RE_EMOJI.sub("", line)
        line = re.sub(r"  +", " ", line)
        # Promote a bare bold-led callout to a blockquote for visual distinction,
        # but leave existing blockquotes and list items as-is (only emoji removed).
        stripped = line.lstrip()
        if stripped.startswith("**") and not line.lstrip().startswith(("-", ">")):
            line = "> " + stripped
        else:
            line = line.lstrip() if stripped.startswith(("**", ">")) else line
    line = RE_SPACE_BEFORE_PUNCT.sub(r"\1", line)
    if pdf_safe:
        for glyph, latex in LATEX_CHAR_MAP.items():
            if glyph in line:
                line = line.replace(glyph, latex)
    heading = RE_HEADING.match(line)
    if heading and len(heading.group(1)) < 6:
        line = "#" + line
    return line


def clean_module(text: str, pdf_safe: bool) -> str:
    """Return one module's markdown cleaned, leaving fenced code blocks untouched."""
    out_lines = []
    in_fence = False
    for line in text.split("\n"):
        # Orphan footnote markers are artifacts that never belong in code either.
        line = RE_FOOTNOTE.sub("", line)
        if RE_FENCE.match(line):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        out_lines.append(line if in_fence else clean_prose_line(line, pdf_safe))
    return "\n".join(out_lines).strip()


def build(lang: str, modules_dir: Path, out_path: Path, pdf_safe: bool) -> None:
    """Consolidate every module under *modules_dir* into *out_path* for *lang*."""
    meta = META[lang]
    modules = sorted(modules_dir.glob("module_*.md"))
    if not modules:
        raise SystemExit(f"no module_*.md found in {modules_dir}")

    parts = [
        "---",
        f"lang: {lang}",  # localises pandoc auto-strings (TOC title, Abstract) + hyphenation
        f'title: "{meta["title"]}"',
        f'subtitle: "{meta["subtitle"]}"',
        'date: "2026-05-20"',
        "abstract: |",
        *[f"  {sentence}" for sentence in [meta["abstract"]]],
        "---",
        "",
    ]
    for module in modules:
        parts.append("\\newpage")
        parts.append("")
        parts.append(clean_module(module.read_text(encoding="utf-8"), pdf_safe))
        parts.append("")

    out_path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    target = "PDF source" if pdf_safe else "canonical"
    print(f"wrote {out_path} ({target}) from {len(modules)} modules ({out_path.stat().st_size} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", required=True, choices=sorted(META))
    parser.add_argument("--modules-dir", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Map glyphs Latin Modern lacks (μ, superscripts) to LaTeX for the xelatex PDF source.",
    )
    args = parser.parse_args()
    build(args.lang, args.modules_dir, args.out, args.pdf)


if __name__ == "__main__":
    main()
