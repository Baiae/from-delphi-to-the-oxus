import argparse
import pathlib
import re
import subprocess
import time
from google import genai
from google.genai import types
from google.genai.errors import APIError

# --- CONFIGURATION ---
MODEL = "gemini-4-hydrogen"
BRANCH_NAME = "edited-v2"
CHAPTERS_DIR = pathlib.Path("Draft_Chapters")       # Folder containing your 24 .md files
OUTPUT_DIR = pathlib.Path("edited_chapters")  # Individual edited chapters land here
SYSTEM_PROMPT_FILE = pathlib.Path("system_instruction.md")
BATCH_SIZE = 2
PAUSE_SECONDS = 20                            # Safe buffer for Free-tier RPM/TPM
MAX_RETRIES = 3


def run_git(*args):
    subprocess.run(["git", *args], check=True)


def ensure_branch(branch: str):
    existing = subprocess.run(
        ["git", "rev-parse", "--verify", branch],
        capture_output=True,
    )
    if existing.returncode == 0:
        run_git("checkout", branch)
    else:
        run_git("checkout", "-b", branch)


def build_pair_prompt(batch: list[pathlib.Path]) -> str:
    names = ", ".join(p.name for p in batch)
    header = (
        f"You are editing {len(batch)} chapters in this single pass ({names}).\n"
        "Apply EVERY editorial rule, Word Count Differential, and [AUTHOR] Audit Log "
        "equally and in full to EACH chapter. Do NOT summarize, rush, or compress the "
        "second chapter.\n\n"
        "Wrap each completed chapter (Revised Chapter + Word Count Differential + "
        "Editorial & Audit Log) in these exact markers so my script can split them:\n"
        "=== BEGIN FILE: <exact_filename> ===\n"
        "...full output for that chapter...\n"
        "=== END FILE: <exact_filename> ===\n\n"
    )
    blocks = []
    for p in batch:
        text = p.read_text(encoding="utf-8")
        blocks.append(f'<chapter filename="{p.name}">\n{text}\n</chapter>')
    return header + "\n\n".join(blocks)


def split_outputs(response_text: str, batch: list[pathlib.Path]) -> dict[str, str]:
    pattern = re.compile(
        r"===\s*BEGIN FILE:\s*(.+?)\s*===\s*(.*?)\s*===\s*END FILE:\s*\1\s*===",
        re.DOTALL,
    )
    found = {m.group(1).strip(): m.group(2).strip() for m in pattern.finditer(response_text)}
    expected = {p.name for p in batch}
    return found if expected.issubset(found.keys()) else {}


def generate_with_retry(client, system_instruction: str, user_prompt: str):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return client.models.generate_content(
                model=MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    max_output_tokens=65536,
                    thinking_config=types.ThinkingConfig(thinking_level="high"),
                ),
            )
        except APIError as e:
            if e.code == 429 and attempt < MAX_RETRIES:
                wait = 30 * attempt
                print(f"  [429 rate limit] Waiting {wait}s before retry {attempt}/{MAX_RETRIES}...")
                time.sleep(wait)
            else:
                raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test-first-pair",
        action="store_true",
        help="Run only the first unfinished pair of chapters to check quality",
    )
    parser.add_argument("--no-git", action="store_true", help="Skip git branch/commit steps")
    args = parser.parse_args()

    system_instruction = SYSTEM_PROMPT_FILE.read_text(encoding="utf-8")
    client = genai.Client()  # Reads GEMINI_API_KEY from environment

    if not args.no_git:
        ensure_branch(BRANCH_NAME)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    all_files = sorted(CHAPTERS_DIR.glob("*.md"))
    pending = [f for f in all_files if not (OUTPUT_DIR / f.name).exists()]

    if not pending:
        print("All chapters already exist in", OUTPUT_DIR)
        return

    batches = [pending[i : i + BATCH_SIZE] for i in range(0, len(pending), BATCH_SIZE)]
    if args.test_first_pair:
        batches = batches[:1]

    for idx, batch in enumerate(batches, 1):
        label = " + ".join(p.name for p in batch)
        print(f"[RUN {idx}/{len(batches)}] Editing {label} with {MODEL}...")

        try:
            response = generate_with_retry(client, system_instruction, build_pair_prompt(batch))
        except APIError as e:
            if e.code == 429:
                print(f"\n[STOPPED] Hit 429 quota limit on {label}. Re-run later to resume.")
                break
            raise

        parsed = split_outputs(response.text, batch)
        written_paths = []

        if parsed:
            for p in batch:
                out_path = OUTPUT_DIR / p.name
                out_path.write_text(parsed[p.name], encoding="utf-8")
                written_paths.append(out_path)
        else:
            # Lossless fallback if the model alters a delimiter tag
            fallback_name = "_AND_".join(p.stem for p in batch) + ".md"
            fallback_path = OUTPUT_DIR / fallback_name
            fallback_path.write_text(response.text, encoding="utf-8")
            written_paths.append(fallback_path)
            print(f"  [WARN] Delimiters not matched cleanly; saved combined output to {fallback_path}")

        usage = response.usage_metadata
        cached = getattr(usage, "cached_content_token_count", 0) or 0
        print(
            f"[DONE] {label} | in: {usage.prompt_token_count} "
            f"(cached: {cached}) | out: {usage.candidates_token_count}"
        )

        if not args.no_git:
            for wp in written_paths:
                run_git("add", str(wp))
            run_git("commit", "-m", f"Edit {label} with {MODEL} (v2)")

        if idx < len(batches):
            time.sleep(PAUSE_SECONDS)

    print("\nFinished. Push your branch with: git push -u origin", BRANCH_NAME)


if __name__ == "__main__":
    main()
