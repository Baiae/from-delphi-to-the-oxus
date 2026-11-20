# Editing the book with Gemini

The input chapters are Draft_Chapters/Ch01.md through Ch24.md. The full user-supplied editing prompt and historical reference are in system_instruction.md.

## Local setup

Use Python 3.12 or newer in a virtual environment.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Set GEMINI_API_KEY in the shell, or place it in .env using the format shown in .env.example. The local .env file is ignored by Git.

## Check and run

From this repository, validate the inputs first.

```sh
.venv/bin/python edit_book.py --dry-run
.venv/bin/python edit_book.py --only Ch01.md
```

Inspect the Chapter 1 output before continuing through the remaining chapters.

```sh
.venv/bin/python edit_book.py
git push -u origin edited-v2
```

The default model is gemini-4-neon. Use --model gemini-4-carbon to select Carbon. Each API call contains one chapter and the same system prompt. Every chapter is sent to Google's API. Usage and charges depend on the API account and model.

Results contain the revised chapter, word-count differential and editorial audit in edited_chapters/ChNN.md. A matching ChNN.usage.json records input/output hashes, model and token usage. Git checkpoints each completed response on edited-v2. The source chapter files stay in Draft_Chapters.

Completed responses with matching inputs are skipped, including when --only is used. To deliberately rerun a chapter, first preserve its output elsewhere, then remove its output and usage record. If the source, prompt or model changes, existing results require review before rerunning. API errors, empty responses and unfinished generations stop the run.

Use --no-git to skip branch switching and commits. On a normal interruption the run releases its lock. After a machine crash, check that no edit process is running before removing edited_chapters/.editing.lock.

The audit compares the manuscript with the supplied historical reference. The script has no web-search tool and does not retrieve the 120 named sources. Historical flags and model-generated counts require review.
