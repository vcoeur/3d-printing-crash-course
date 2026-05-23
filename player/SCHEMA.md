# Scene authoring schema — animated course player

Each module is authored as one JSON file shaped exactly like
[`_example_module.json`](scenes/_example_module.json) (read it — it shows every element
type in both languages). This file is the rulebook.

## Structure

```
{ "module": N, "module_title": {en,fr},
  "chapters": [ { "chapter": C, "title": {en,fr},
      "scenes": [ { "id": "N.C.i", "narration": {en,fr}, "elements": [ … ] } ] } ] }
```

- **Every text field is bilingual:** `{"en": "...", "fr": "..."}`. Language-neutral tokens
  (years, "FDM/FFF", "STL", "0.2 mm") may be a plain string.
- **Scene `id`** = `"<module>.<chapter>.<index>"`, index from 0 (e.g. `"3.2.0"`).

## Allowed element types (use ONLY these)

| type | shape | use for |
|------|-------|---------|
| `kicker` | `{type, text}` | small label, e.g. "Module 3 · Chapter 2" |
| `title` | `{type, text}` | the scene heading (one per scene) |
| `lead` | `{type, text}` | one larger intro sentence |
| `bullets` | `{type, items:[text,…]}` | 2–6 points; `<b>…</b>` allowed for the lead-in word |
| `compare` | `{type, left:{title,note}, right:{title,note,highlight?}}` | two things side by side |
| `cards` | `{type, items:[{title, desc, highlight?}]}` | 3–6 small labelled cards |
| `timeline` | `{type, nodes:[{label, text}]}` | 3–5 dated/sequential nodes |
| `pipeline` | `{type, steps:[{name, sub}]}` | 3–6 stages flowing left→right |
| `stages` | `{type, items:[{label, sub}]}` | 3–5 segments of one thing (e.g. hotend zones) |
| `stat` | `{type, value, caption}` | one big number/figure + caption |
| `callout` | `{type, variant:"tip"|"note"|"warning", text}` | one highlighted note |
| `table` | `{type, headers:[…], rows:[[…],…]}` | small table, ≤4 cols ≤5 rows |

`title`/`lead`/`text`/`note`/`caption`/`sub`/`desc` and each `bullets`/`items` entry are
bilingual objects. `value`, `label`, `name`, `card title` may be plain strings when
language-neutral.

## Authoring rules

1. **COVER THE WHOLE CHAPTER — this is a comprehensive course, not a summary.** Walk
   through every section and subsection of the chapter in order and turn its important
   content into scenes: every key fact, number, date, price, comparison, step, table, and
   warning must appear somewhere in the slides. You may drop only minor asides or redundant
   phrasing that does not suit a slide — **when in doubt, add another scene.** Expect
   roughly one scene per subsection or distinct idea: often **8–16+ scenes per chapter**,
   more for long chapters. Do not compress a dense chapter into a handful of slides.
2. **Title + recap.** First scene is the title scene: `kicker` ("Module N · Chapter C") +
   `title` + `lead`. End the chapter with a short recap scene (`bullets`) of its key points.
3. **One idea per scene.** 1–3 elements per scene (a `title` + one visual, optional
   `callout`). Don't cram a scene; split into more scenes instead.
4. **On-screen text is slide-terse** — phrases, not paragraphs (the full detail is carried
   by the narration + the set of scenes, not crammed onto one slide).
5. **Narration** = 1–3 spoken sentences (~15–40 words), warm, clear teacher tone. Write it
   to be *spoken*: expand symbols ("to", "then", "degrees"), no citation markers, no "→".
   The narration carries the detail; together the scenes must convey the chapter's full
   substance.
6. **Bilingual & faithful.** Pull the French from the French module source (correct accents
   — "é, è, à, ç, °, µ"), not a rough re-translation. The source course is already
   fact-checked: **reuse its numbers, dates, names, prices exactly; invent nothing.** Drop
   the `^[N]^` citation markers.
7. **Pick varied visuals** — lean on `compare`, `cards`, `timeline`, `pipeline`, `stages`,
   `stat` so chapters don't all look like bullet lists.
8. Output exactly one file: `local/player/scenes/module_<NN>.json` (zero-padded).
