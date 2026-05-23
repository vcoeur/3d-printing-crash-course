#!/usr/bin/env python3
"""Combine the per-chapter Module 5 part files (_m5_c1..4.json) into module_05.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SCENES = os.path.join(HERE, "scenes")
TITLE = {"en": "Slicer Software Mastery", "fr": "Maîtriser les logiciels de tranchage"}

chapters = []
for n in (1, 2, 3, 4):
    with open(os.path.join(SCENES, f"_m5_c{n}.json"), encoding="utf-8") as handle:
        chapters.append(json.load(handle))
chapters.sort(key=lambda c: c["chapter"])

out = os.path.join(SCENES, "module_05.json")
with open(out, "w", encoding="utf-8") as handle:
    json.dump({"module": 5, "module_title": TITLE, "chapters": chapters}, handle,
              ensure_ascii=False, indent=1)
total = sum(len(c["scenes"]) for c in chapters)
print(f"module_05.json: {len(chapters)} chapters, {total} scenes")
