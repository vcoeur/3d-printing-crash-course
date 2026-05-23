#!/usr/bin/env python3
"""Merge per-module scene JSON files (module_*.json) into one course.json."""
import argparse
import glob
import json
import os

TITLE = {"en": "3D Printing Crash Course", "fr": "Cours accéléré d'impression 3D"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenes-dir", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    files = sorted(glob.glob(os.path.join(args.scenes_dir, "module_*.json")))
    modules, n_ch, n_sc = [], 0, 0
    for path in files:
        with open(path, encoding="utf-8") as handle:
            mod = json.load(handle)
        modules.append(mod)
        for chapter in mod["chapters"]:
            n_ch += 1
            n_sc += len(chapter["scenes"])
    modules.sort(key=lambda m: m["module"])

    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump({"title": TITLE, "modules": modules}, handle, ensure_ascii=False, indent=1)
    print(f"{len(modules)} modules, {n_ch} chapters, {n_sc} scenes -> {args.out}")


if __name__ == "__main__":
    main()
