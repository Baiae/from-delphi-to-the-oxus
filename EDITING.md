# Editing the book with Gemini Hydrogen

The input chapters are Draft_Chapters/Ch01.md through Ch24.md. The full supplied editing prompt and historical reference are in system_instruction.md. The editor is the user-supplied paired-chapter script, with CHAPTERS_DIR adjusted for this repository.

## Local setup

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Set GEMINI_API_KEY in the shell. If you use the ignored .env file created during setup, load it into this terminal session from the repository root.

```sh
set -a
source .env
set +a
```

## Test and run

Run the first unfinished pair and inspect the resulting chapter text and audits.

```sh
.venv/bin/python edit_book.py --test-first-pair
```

After reviewing that pair, process remaining chapters.

```sh
.venv/bin/python edit_book.py
git push -u origin edited-v2
```

The script uses gemini-4-hydrogen and sends two chapters plus the system instruction to Google's API per request. It waits 20 seconds between pairs and retries HTTP 429 twice, after 30 and 60 seconds. An API account quota or billing block may still require account changes.

Responses with the expected delimiters are saved in edited_chapters/ChNN.md, including the word-count differential and audit. If delimiters fail to match, a combined file is saved for manual review. Individual chapter filenames already present are skipped, including when source or prompt changes. Each batch is committed on edited-v2.

This supplied script does not validate generation finish reasons, lock concurrent runs, write separate usage records, or atomically write the two chapter outputs. Inspect completeness and quality before resuming after an interruption. A combined fallback file does not mark its individual chapters complete.

The historical audit uses the supplied reference block. The script does not retrieve the named sources or verify model-generated counts.
