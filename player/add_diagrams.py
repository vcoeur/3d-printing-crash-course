#!/usr/bin/env python3
"""Place schematic `diagram` elements on the scenes that actually teach each concept.

Earlier this matched scenes by keyword, which misfired badly (the AMS diagram landed
on Bambu *history* scenes, `retraction` on a temperature scene, etc.). Placement is now
an explicit, hand-verified map of (module, chapter, scene_index) -> diagram kind: each
diagram appears only where its subject is the point of the scene.

Idempotent: strips every existing diagram element first, then inserts from PLACEMENTS,
so re-running always reproduces exactly this set. A diagram is inserted right after the
scene's title element. Scene indices are stable (we add an element to a scene, never a
scene to a chapter), so they match `dump_titles.py` / the player's `?at=M.C.S`.
"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SCENES = os.path.join(HERE, "scenes")

# (module, chapter, scene_index, kind) — verified against dump_titles.py.
PLACEMENTS = [
    # CoreXY kinematics (Module 1, Ch 3)
    (1, 3, 0, "corexy"),     # CoreXY — The High-Performance Kinematic System
    (1, 3, 2, "corexy"),     # How CoreXY Solves It
    (1, 3, 3, "corexy"),     # The CoreXY Math
    # Bed-slinger / Cartesian motion
    (1, 3, 1, "bedslinger"), # The Problem with Bedslingers
    (1, 3, 5, "bedslinger"), # CoreXY vs. Bedslinger: By the Numbers
    (1, 3, 9, "bedslinger"), # CoreXY vs. Cartesian vs. Delta
    (3, 2, 1, "bedslinger"), # CoreXY vs. Bed-Slinger
    # Hotend cross-section / heat zones
    (1, 2, 3, "hotend"),     # Hotend Anatomy
    (2, 1, 0, "hotend"),     # The Hotend and Nozzle
    (2, 1, 1, "hotend"),     # Hotend Anatomy: Five Components
    (2, 1, 2, "hotend"),     # Heat Sink and Heat Creep
    # Layer-by-layer deposition / how FDM works
    (1, 2, 0, "fdm_layers"), # FDM Technology Deep Dive
    (1, 2, 1, "fdm_layers"), # How FDM Works: Step by Step
    # Direct drive vs Bowden
    (1, 2, 22, "extruder"),  # Direct Drive vs. Bowden
    (2, 2, 1, "extruder"),   # Direct Drive vs. Bowden
    (2, 2, 2, "extruder"),   # The Compliance Problem in Bowden Systems
    # AMS filament path (Module 7, Ch 1)
    (7, 1, 1, "ams"),        # The AMS Ecosystem
    (7, 1, 9, "ams"),        # The Filament Path — 6 Stages
    (7, 1, 11, "ams"),       # Stage 3–5: Hub, Tube, and Buffer
    (7, 1, 12, "ams"),       # The Filament Change Sequence
    # First-layer / Z-offset
    (8, 1, 1, "first_layer"),# Why the First Layer Matters
    (8, 1, 2, "first_layer"),# Signs of a Good First Layer
    (8, 1, 3, "first_layer"),# Z-Offset: The Critical Distance
    (6, 2, 11, "first_layer"),# First Layer Settings
    # 45-degree overhang rule / bridging / supports
    (1, 2, 20, "overhang"),  # Supports and Bridging
    (5, 2, 14, "overhang"),  # Slow Down for Overhangs
    (4, 3, 9, "overhang"),   # PVA — Water-Soluble Supports
    # Infill density and patterns
    (1, 2, 18, "infill"),    # Layer Height, Walls, and Infill
    (1, 2, 19, "infill"),    # Infill Patterns
    (5, 1, 8, "infill"),     # Infill: Density and Pattern
    (5, 1, 9, "infill"),     # Why Gyroid Wins for Multi-Directional Loads
    # Retraction / stringing
    (4, 1, 8, "retraction"), # Taming PETG Stringing
    (8, 2, 8, "retraction"), # Stringing: Causes and Fixes
    (8, 2, 9, "retraction"), # Retraction Guidelines
    (6, 4, 14, "retraction"),# Step 4: Retraction Calibration
    # Z-anisotropy / orientation
    (5, 1, 4, "anisotropy"), # Why Orientation Matters
    (8, 4, 5, "anisotropy"), # Orientation Trade-offs
    (8, 4, 12, "anisotropy"),# FDM Design Rules
    # Skirt / brim / raft adhesion aids
    (5, 1, 11, "adhesion"),  # Bed Adhesion: Skirt · Brim · Raft
    (8, 1, 10, "adhesion"),  # Adhesion Aids: Skirt, Brim, Raft
]


def strip_diagrams(scene):
    before = len(scene.get("elements", []))
    scene["elements"] = [e for e in scene.get("elements", []) if e.get("type") != "diagram"]
    return before - len(scene["elements"])


def insert_after_title(scene, kind):
    els = scene["elements"]
    idx = next((i for i, e in enumerate(els) if e.get("type") == "title"), -1)
    els.insert(idx + 1, {"type": "diagram", "kind": kind})


def main():
    # index placements by module for a single pass per file
    by_module = {}
    for mod_num, ch_num, sc_idx, kind in PLACEMENTS:
        by_module.setdefault(mod_num, []).append((ch_num, sc_idx, kind))

    removed = inserted = 0
    log = []
    for path in sorted(glob.glob(os.path.join(SCENES, "module_*.json"))):
        with open(path, encoding="utf-8") as handle:
            mod = json.load(handle)
        mod_num = mod["module"]
        # 1. strip every existing diagram
        for ch in mod["chapters"]:
            for sc in ch["scenes"]:
                removed += strip_diagrams(sc)
        # 2. place from the curated map
        chap_by_num = {ch["chapter"]: ch for ch in mod["chapters"]}
        for ch_num, sc_idx, kind in by_module.get(mod_num, []):
            ch = chap_by_num.get(ch_num)
            if ch is None or sc_idx >= len(ch["scenes"]):
                log.append("  ! SKIP {}.{}.{} ({}) — out of range".format(mod_num, ch_num, sc_idx, kind))
                continue
            insert_after_title(ch["scenes"][sc_idx], kind)
            inserted += 1
            log.append("  {}.{}.{}  +{}".format(mod_num, ch_num, sc_idx, kind))
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(mod, handle, ensure_ascii=False, indent=1)

    for line in sorted(log):
        print(line)
    print("\nremoved {} old diagrams; placed {} curated diagrams".format(removed, inserted))


if __name__ == "__main__":
    main()
