#!/usr/bin/env python3
"""Generate per-scene narration MP3s for course.json using Edge TTS.

Voices: en -> en-US-AriaNeural, fr -> fr-FR-DeniseNeural. Output:
<out>/<lang>/<scene_id>.mp3. Idempotent: existing non-empty files are skipped
unless --force. Edge TTS is a free Microsoft cloud call (text is sent to MS).

Run: uv run --with edge-tts python gen_audio_edge.py --course course.json --out audio
"""
import argparse
import asyncio
import json
import os

import edge_tts

VOICES = {"en": "en-US-AriaNeural", "fr": "fr-FR-DeniseNeural"}


def collect(course):
    items = []
    for module in course["modules"]:
        for chapter in module["chapters"]:
            for scene in chapter["scenes"]:
                for lang in ("en", "fr"):
                    text = (scene.get("narration") or {}).get(lang, "").strip()
                    if text:
                        items.append((lang, scene["id"], text))
    return items


async def synth(sem, lang, scene_id, text, out_dir, force):
    out = os.path.join(out_dir, lang, f"{scene_id}.mp3")
    if not force and os.path.exists(out) and os.path.getsize(out) > 0:
        return "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    async with sem:
        await edge_tts.Communicate(text, VOICES[lang]).save(out)
    return "ok"


async def run(items, out_dir, force, concurrency):
    sem = asyncio.Semaphore(concurrency)
    done = 0

    async def wrap(item):
        nonlocal done
        try:
            result = await synth(sem, *item, out_dir, force)
        except Exception as exc:  # keep going; report at the end
            result = f"err:{item[0]}/{item[1]}:{exc}"
        done += 1
        if done % 25 == 0:
            print(f"  {done}/{len(items)}")
        return result

    return await asyncio.gather(*(wrap(it) for it in items))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", required=True)
    parser.add_argument("--out", required=True, help="audio output directory")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--conc", type=int, default=6, help="concurrent requests")
    args = parser.parse_args()

    with open(args.course, encoding="utf-8") as handle:
        course = json.load(handle)
    items = collect(course)
    n_en = sum(1 for it in items if it[0] == "en")
    print(f"{len(items)} clips ({n_en} en / {len(items) - n_en} fr)")

    results = asyncio.run(run(items, args.out, args.force, args.conc))
    ok = results.count("ok")
    skip = results.count("skip")
    errs = [r for r in results if isinstance(r, str) and r.startswith("err:")]
    print(f"done: {ok} generated, {skip} skipped, {len(errs)} errors")
    for e in errs[:20]:
        print("  " + e)


if __name__ == "__main__":
    main()
