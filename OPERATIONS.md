# Operations & Troubleshooting

This file explains how the TLDR knowledge system works behind the scenes: local setup, GitHub Actions automation, daily topic lists, model configuration, recovery, and known limitations.

For the simple project purpose and public knowledge dashboard, see [README.md](README.md).

---

## 1. System overview

TLDR turns source URLs into short Markdown knowledge notes.

High-level flow:

```text
input/daily-machine-learning.md
input/daily-system-design.md
        ↓
scripts/daily_pick.py
        ↓
input/links-to-summarize.md
        ↓
scripts/process_links.py
        ↓
knowledge/<Category>/<generated-note>.md
        ↓
scripts/enforce_daily_categories.py
        ↓
scripts/update_readme_only.py
        ↓
README.md dashboard
        ↓
input/daily-processed.md
```

The automation currently processes one Machine Learning topic and one System Design topic per scheduled run.

---

## 2. Important files

| File | Purpose |
| --- | --- |
| `README.md` | Simple public-facing project description and generated knowledge dashboard. |
| `OPERATIONS.md` | Technical setup, automation details, and troubleshooting. |
| `.github/workflows/summarize.yml` | GitHub Actions workflow for scheduled processing. |
| `input/daily-machine-learning.md` | Source list for daily Machine Learning topics. |
| `input/daily-system-design.md` | Source list for daily System Design topics. |
| `input/links-to-summarize.md` | Temporary queue used by the processor. Should usually be empty after success. |
| `input/daily-processed.md` | Tracks daily URLs that were successfully processed. |
| `knowledge/` | Generated Markdown notes organized by category. |
| `scripts/daily_pick.py` | Picks the next unprocessed ML and System Design URLs. |
| `scripts/process_links.py` | Fetches page content, calls the model, writes Markdown files, and updates README. |
| `scripts/enforce_daily_categories.py` | Ensures daily ML/System Design URLs land in the intended category folders. |
| `scripts/reconcile_queue.py` | Compares selected URLs with generated knowledge files and preserves failures. |
| `scripts/update_readme_only.py` | Regenerates only the README dashboard. |

---

## 3. Local setup

Requires Python 3.11+.

```bash
python3.11 -m venv venv311
source venv311/bin/activate
pip install -r requirements.txt
```

On Windows:

```powershell
py -3.11 -m venv venv311
venv311\Scripts\activate
pip install -r requirements.txt
```

---

## 4. Environment variables

Create a `.env` file in the repository root for local runs.

Recommended GitHub Models setup:

```env
GITHUB_TOKEN=ghp_xxxxx
GITHUB_MODEL=openai/gpt-5
GITHUB_MAX_TOKENS=6000
GITHUB_RETRY_ATTEMPTS=4
GITHUB_RETRY_BASE_DELAY_SEC=1.5
GITHUB_RETRY_MAX_DELAY_SEC=20
```

Optional Gemini fallback/local alternative:

```env
GEMINI_API_KEY=xxxxx
GEMINI_RETRY_ATTEMPTS=4
GEMINI_RETRY_BASE_DELAY_SEC=1.5
GEMINI_RETRY_MAX_DELAY_SEC=20
```

Important behavior:

- If `GITHUB_TOKEN` is available, the adapter uses GitHub Models first.
- If `GITHUB_TOKEN` is missing and `GEMINI_API_KEY` exists, it uses Gemini.
- Current code does not automatically fall back to Gemini after a GitHub Models failure in the same run.

---

## 5. GitHub Actions configuration

The scheduled workflow lives at:

```text
.github/workflows/summarize.yml
```

Required workflow permissions:

```yaml
permissions:
  contents: write
  models: read
```

Why these are needed:

- `contents: write` lets the workflow commit generated notes and README updates.
- `models: read` lets the workflow call GitHub Models.

The workflow currently uses:

```yaml
GITHUB_MODEL: openai/gpt-5
GITHUB_MAX_TOKENS: '6000'
```

The workflow runs on:

- daily schedule
- manual `workflow_dispatch`
- push changes to `input/links-to-summarize.md`

---

## 6. Daily automation behavior

### Daily topic sources

Machine Learning topics are stored in:

```text
input/daily-machine-learning.md
```

System Design topics are stored in:

```text
input/daily-system-design.md
```

Each scheduled run picks the first URL from each list that is not already processed.

### Processed tracking

The system considers a URL processed if it appears in either:

```text
input/daily-processed.md
```

or as a `source_url:` inside a file under:

```text
knowledge/**/*.md
```

This prevents duplicate processing.

### Queue file

The selected daily URLs are written into:

```text
input/links-to-summarize.md
```

After a successful run, this file should be empty.

If a transient error happens, failed URLs are restored to this queue so they can be retried.

---

## 7. Adding more daily topics

Add new topics to the end of the correct list.

Machine Learning example:

```md
# 46 - Model Persistence
https://scikit-learn.org/stable/model_persistence.html
```

System Design example:

```md
# 46 - Database Indexing
https://example.com/database-indexing-guide
```

Guidelines:

- Add one URL per topic.
- Prefer stable documentation pages over temporary blog posts.
- Avoid duplicates.
- Avoid direct PDF URLs for now; PDF support is not fully implemented yet.
- Keep Machine Learning topics in `daily-machine-learning.md`.
- Keep System Design topics in `daily-system-design.md`.

When the lists are empty, the workflow does not fail. It prints:

```text
No new daily topics available.
```

and leaves the queue empty.

---

## 8. Manual commands

Process whatever is currently in the queue:

```bash
python scripts/process_links.py
```

Pick the next daily ML/System Design pair:

```bash
python scripts/daily_pick.py
```

Enforce daily categories:

```bash
python scripts/enforce_daily_categories.py
```

Regenerate README dashboard only:

```bash
python scripts/update_readme_only.py
```

Run queue reconciliation:

```bash
python scripts/reconcile_queue.py
```

Check queue and knowledge status:

```bash
python scripts/monitor_queue.py
```

---

## 9. README behavior

The README is intentionally simple. It should explain the purpose of the repository, not the technical implementation.

The generated dashboard is kept between these markers:

```md
<!-- TLDR-AUTO-START -->
<!-- TLDR-AUTO-END -->
```

Do not manually edit content inside those markers unless you are repairing the generated dashboard. It will be overwritten by the README generation script.

The dashboard sorts entries using the date stored in each generated note. This means “Latest” may refer to the source/article date, not necessarily the date the automation processed the URL.

---

## 10. Category enforcement

Daily ML and System Design topics should land in predictable folders:

```text
knowledge/Machine-Learning/
knowledge/System-Design/
```

Because the model can sometimes choose a different category, the workflow runs:

```bash
python scripts/enforce_daily_categories.py
```

after processing.

This script moves generated daily-topic files into their intended category based on whether the source URL came from:

```text
input/daily-machine-learning.md
input/daily-system-design.md
```

---

## 11. Troubleshooting

### Queue is not empty after a run

This usually means at least one URL failed.

Check:

```bash
cat input/links-to-summarize.md
```

Then either wait and rerun, or remove the problematic URL.

### GitHub Models 403

Common causes:

- Missing `models: read` workflow permission.
- Model not available to the repository/account.
- Invalid or limited token.

Check that the workflow includes:

```yaml
permissions:
  contents: write
  models: read
```

### GitHub Models 400 with token parameter errors

For GPT-5, the adapter must use:

```python
max_completion_tokens
```

not:

```python
max_tokens
```

### Rate limit errors: 429

What happens:

- GitHub Models may return HTTP 429.
- The script retries with exponential backoff.
- If retries are exhausted, remaining URLs are preserved in `input/links-to-summarize.md`.

Recovery:

```bash
python scripts/monitor_queue.py
# wait for rate limit reset
python scripts/process_links.py
```

You can increase retry tolerance:

```env
GITHUB_RETRY_ATTEMPTS=6
GITHUB_RETRY_MAX_DELAY_SEC=60
```

### Empty or low-quality summaries

Possible causes:

- Paywalled content
- JavaScript-heavy pages
- PDF URLs
- Very short pages
- Model returned weak output

Inspect the generated note manually under `knowledge/`.

If it is bad:

1. Delete the bad Markdown file.
2. Re-add the URL to `input/links-to-summarize.md`.
3. Rerun the processor.

---

## 12. Current limitations

### PDF URLs

Direct PDF URLs are not properly supported yet.

The current processor is designed around HTML extraction. It fetches a URL and parses visible HTML text. A direct PDF URL may run, but the extracted context can be empty or unreliable.

Recommended future improvement:

```text
PDF URL
→ download PDF
→ extract text with pypdf/pdfplumber/PyMuPDF
→ pass extracted text to GitHub Models
→ generate Markdown summary
```

### JavaScript-heavy pages

Pages that rely heavily on client-side rendering may produce weak summaries because the script uses `requests`, not a browser.

### Model fallback

The system can use Gemini if GitHub Models is not configured, but it does not currently fall back from GitHub Models to Gemini after a GitHub Models runtime failure.

---

## 13. Maintenance checklist

Weekly or occasional checks:

- Confirm recent `docs: Auto-generate knowledge base` commits are being created.
- Confirm `input/links-to-summarize.md` is empty after successful runs.
- Confirm `daily-processed.md` is growing by expected URLs.
- Review recent generated notes for quality.
- Add more URLs before the daily topic lists run out.
- Keep README simple and move technical details here.

---

## 14. Roadmap ideas

Potential improvements:

- Add real PDF URL support.
- Add warning when daily topic lists are almost empty.
- Improve fallback from GitHub Models to Gemini.
- Add summary quality checks.
- Add a processed date field separate from source publication date.
- Improve README sorting to optionally show processing date.
