#!/usr/bin/env python3
"""Validate per-module scene JSON against the player schema.

Checks: required structure, element types in the allowed set, narration has
non-empty en+fr, and flags bilingual objects missing the 'fr' (or 'en') side.
Exits non-zero if any hard error is found.
"""
import argparse
import glob
import json
import os
import sys

ALLOWED = {"kicker", "title", "lead", "bullets", "compare", "cards",
           "timeline", "pipeline", "stages", "stat", "callout", "table", "diagram"}
DIAGRAM_KINDS = {"corexy", "bedslinger", "hotend", "fdm_layers", "extruder", "ams",
                 "first_layer", "overhang", "infill", "adhesion", "retraction", "anisotropy"}


def walk_bilingual(node, path, missing):
    """Flag dicts that look bilingual (have 'en') but lack 'fr', or vice-versa."""
    if isinstance(node, dict):
        if ("en" in node) ^ ("fr" in node):
            missing.append(path)
        for k, v in node.items():
            walk_bilingual(v, f"{path}.{k}", missing)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk_bilingual(v, f"{path}[{i}]", missing)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenes-dir", required=True)
    args = parser.parse_args()

    errors, warnings = [], []
    total_scenes = 0
    for path in sorted(glob.glob(os.path.join(args.scenes_dir, "module_*.json"))):
        name = os.path.basename(path)
        try:
            with open(path, encoding="utf-8") as handle:
                mod = json.load(handle)
        except Exception as exc:
            errors.append(f"{name}: invalid JSON: {exc}")
            continue
        for key in ("module", "module_title", "chapters"):
            if key not in mod:
                errors.append(f"{name}: missing top-level '{key}'")
        n_sc = 0
        for ch in mod.get("chapters", []):
            for sc in ch.get("scenes", []):
                n_sc += 1
                total_scenes += 1
                sid = sc.get("id", "?")
                nar = sc.get("narration") or {}
                if not nar.get("en", "").strip() or not nar.get("fr", "").strip():
                    errors.append(f"{name} {sid}: narration missing en or fr")
                els = sc.get("elements", [])
                if not els:
                    warnings.append(f"{name} {sid}: no elements")
                for e in els:
                    if e.get("type") not in ALLOWED:
                        errors.append(f"{name} {sid}: bad element type {e.get('type')!r}")
                    elif e.get("type") == "diagram" and e.get("kind") not in DIAGRAM_KINDS:
                        errors.append(f"{name} {sid}: unknown diagram kind {e.get('kind')!r}")
                miss = []
                walk_bilingual(sc, sid, miss)
                for m in miss:
                    warnings.append(f"{name}: one-sided bilingual at {m}")
        print(f"{name}: module {mod.get('module')}, {len(mod.get('chapters', []))} chapters, {n_sc} scenes")

    print(f"\nTOTAL scenes: {total_scenes}")
    if warnings:
        print(f"\n{len(warnings)} warnings:")
        for w in warnings[:40]:
            print("  ! " + w)
    if errors:
        print(f"\n{len(errors)} ERRORS:")
        for e in errors[:60]:
            print("  ✗ " + e)
        sys.exit(1)
    print("\nOK — no hard errors.")


if __name__ == "__main__":
    main()
