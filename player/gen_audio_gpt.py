#!/usr/bin/env python3
"""Generate per-scene narration MP3s for course.json using OpenRouter GPT-4o Mini TTS.

Cheaper sibling of gen_audio_voxtral.py (~$0.60 vs ~$16 per 1M input characters): same
--course/--out contract and same <out>/<lang>/<scene_id>.mp3 layout, so build_site.sh is
unchanged. GPT-4o Mini TTS is multilingual — one voice (marin) reads both EN and FR;
language follows the input text. Idempotent: existing non-empty files are skipped unless
--force. Needs OPENROUTER_API_KEY or ~/.config/openrouter/api-key.

Run (from the repo root):
  python3 player/gen_audio_gpt.py --course player/course.json --out player/audio
"""
import argparse
import concurrent.futures
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API_URL = "https://openrouter.ai/api/v1/audio/speech"
MODEL = "openai/gpt-4o-mini-tts-2025-12-15"
VOICE = "marin"  # GPT-4o voices are multilingual — one voice covers EN + FR.


def load_api_key():
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        key_file = Path.home() / ".config" / "openrouter" / "api-key"
        if key_file.is_file():
            key = key_file.read_text().strip()
    if not key:
        sys.exit("gen_audio_gpt: no API key (set OPENROUTER_API_KEY or ~/.config/openrouter/api-key)")
    return key


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


def synth(lang, scene_id, text, out_dir, force, api_key):
    out = os.path.join(out_dir, lang, f"{scene_id}.mp3")
    if not force and os.path.exists(out) and os.path.getsize(out) > 0:
        return "skip"
    payload = json.dumps(
        {"model": MODEL, "input": text, "voice": VOICE, "response_format": "mp3"}
    ).encode()
    request = urllib.request.Request(
        API_URL,
        data=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        audio = response.read()
    os.makedirs(os.path.dirname(out), exist_ok=True)
    # Write via a temp file so an interrupted run never leaves a truncated mp3.
    tmp = out + ".part"
    with open(tmp, "wb") as handle:
        handle.write(audio)
    os.replace(tmp, out)
    return "ok"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", required=True)
    parser.add_argument("--out", required=True, help="audio output directory")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--conc", type=int, default=6, help="concurrent requests")
    args = parser.parse_args()

    api_key = load_api_key()
    with open(args.course, encoding="utf-8") as handle:
        course = json.load(handle)
    items = collect(course)
    n_en = sum(1 for it in items if it[0] == "en")
    print(f"{len(items)} clips ({n_en} en / {len(items) - n_en} fr)")

    done = 0
    results = []

    def work(item):
        lang, scene_id, text = item
        try:
            return synth(lang, scene_id, text, args.out, args.force, api_key)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode(errors="replace")[:200]
            return f"err:{lang}/{scene_id}:{exc.code}:{detail}"
        except Exception as exc:  # keep going; report at the end
            return f"err:{lang}/{scene_id}:{exc}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.conc) as pool:
        for result in pool.map(work, items):
            results.append(result)
            done += 1
            if done % 25 == 0:
                print(f"  {done}/{len(items)}")

    ok = results.count("ok")
    skip = results.count("skip")
    errs = [r for r in results if isinstance(r, str) and r.startswith("err:")]
    print(f"done: {ok} generated, {skip} skipped, {len(errs)} errors")
    for e in errs[:20]:
        print("  " + e)


if __name__ == "__main__":
    main()
