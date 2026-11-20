"""Edit independent chapters with Gemini and checkpoint each completed response."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time

from google import genai
from google.genai import types, errors
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
MODEL = "gemini-4-neon"
BRANCH_NAME = "edited-v2"
CHAPTERS_DIR = ROOT / "Draft_Chapters"
OUTPUT_DIR = ROOT / "edited_chapters"
SYSTEM_PROMPT_FILE = ROOT / "system_instruction.md"


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
        stream.write(text)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", help="One chapter filename, such as Ch01.md")
    parser.add_argument("--no-git", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Validate inputs without API calls")
    parser.add_argument("--model", default=MODEL)
    args = parser.parse_args()
    files = sorted(CHAPTERS_DIR.glob("Ch[0-9][0-9].md"))
    if args.only:
        files = [path for path in files if path.name == args.only]
    if not files:
        raise SystemExit("No matching chapter files found in Draft_Chapters.")
    instruction = SYSTEM_PROMPT_FILE.read_text(encoding="utf-8").strip()
    if not instruction or "<historical_reference>" not in instruction or "</historical_reference>" not in instruction:
        raise SystemExit("system_instruction.md requires the prompt and complete historical reference.")
    if args.dry_run:
        for path in files:
            print(f"[READY] {path.name}: {len(path.read_text(encoding='utf-8').split())} words")
        print(f"Model: {args.model}; output: {OUTPUT_DIR}")
        return
    load_dotenv(ROOT / ".env", override=False)
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Set GEMINI_API_KEY or add it to the ignored .env file.")
    if not args.no_git:
        if git("diff", "--cached", "--name-only"):
            raise SystemExit("Commit or unstage existing staged changes before running.")
        changed = git("diff", "--name-only").splitlines()
        changed += git("ls-files", "--others", "--exclude-standard").splitlines()
        if any(not name.startswith("edited_chapters/") for name in changed):
            raise SystemExit("Commit or stash changes outside edited_chapters before running.")
        if git("branch", "--show-current") != BRANCH_NAME:
            branches = git("branch", "--list", BRANCH_NAME)
            git("switch", BRANCH_NAME) if branches else git("switch", "-c", BRANCH_NAME)
    OUTPUT_DIR.mkdir(exist_ok=True)
    # A second process must not edit the same chapter concurrently.
    lock = OUTPUT_DIR / ".editing.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise SystemExit("An edit run holds .editing.lock. If it stopped, remove the stale lock before resuming.")
    os.close(descriptor)
    try:
        with genai.Client(api_key=api_key) as client:
            for path in files:
                out_path = OUTPUT_DIR / path.name
                audit_path = OUTPUT_DIR / f"{path.stem}.usage.json"
                chapter_text = path.read_text(encoding="utf-8")
                fingerprint = {
                    "source_sha256": digest(chapter_text),
                    "system_sha256": digest(instruction),
                    "model": args.model,
                }
                if out_path.exists():
                    if not audit_path.exists():
                        raise SystemExit(f"{out_path.name} exists without its usage record. Review it before resuming.")
                    previous = json.loads(audit_path.read_text(encoding="utf-8"))
                    if any(previous.get(key) != value for key, value in fingerprint.items()):
                        raise SystemExit(f"{path.name} inputs changed. Preserve or remove its existing output before rerunning.")
                    if previous.get("output_sha256") != digest(out_path.read_text(encoding="utf-8")):
                        raise SystemExit(f"{out_path.name} was edited locally. Preserve it before rerunning.")
                    print(f"[SKIP] {path.name}: completed with the same inputs")
                else:
                    print(f"[EDITING] {path.name}", flush=True)
                    response = client.models.generate_content(
                        model=args.model,
                        contents=chapter_text,
                        config=types.GenerateContentConfig(
                            system_instruction=instruction,
                            temperature=0.4,
                            max_output_tokens=65536,
                            thinking_config=types.ThinkingConfig(thinking_level="high"),
                        ),
                    )
                    candidates = response.candidates or []
                    if not candidates or candidates[0].finish_reason != types.FinishReason.STOP:
                        raise SystemExit(f"{path.name}: incomplete or blocked response. No completed output saved.")
                    result = response.text
                    if not result or not result.strip():
                        raise SystemExit(f"{path.name}: empty response. No completed output saved.")
                    if "# Chapter" not in result or "Word Count" not in result or "Audit" not in result:
                        raise SystemExit(f"{path.name}: missing requested chapter or audit sections. No completed output saved.")
                    usage = response.usage_metadata
                    record = {
                        **fingerprint,
                        "output_sha256": digest(result),
                        "usage": usage.model_dump(mode="json") if usage else None,
                    }
                    # Write metadata first. A lone metadata file can safely be replaced on retry.
                    atomic_write(audit_path, json.dumps(record, indent=2) + "\n")
                    atomic_write(out_path, result)
                    print(f"[DONE] {path.name}", flush=True)
                    time.sleep(2)
                if not args.no_git:
                    git("add", "--", str(out_path.relative_to(ROOT)), str(audit_path.relative_to(ROOT)))
                    if git("diff", "--cached", "--name-only"):
                        git("commit", "-m", f"Edit {path.name} with {args.model} (v2)")
        print("Requested chapters complete.")
        if not args.no_git:
            print(f"Push with: git push -u origin {BRANCH_NAME}")
    finally:
        lock.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        main()
    except errors.APIError as error:
        key = os.environ.get("GEMINI_API_KEY", "")
        detail = str(error.message or "Check model access, quota and billing.")
        if key:
            detail = detail.replace(key, "[REDACTED]")
        raise SystemExit(f"Gemini API request failed (HTTP {error.code}): {detail}")
