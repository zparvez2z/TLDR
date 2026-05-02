# Operations & Troubleshooting

Complete guide to configuration, troubleshooting, and recovery procedures for the TLDR knowledge system.

## Setup Guide

### 1. Python Environment

Requires Python 3.11+

```bash
# Create virtual environment
python3.11 -m venv venv311
source venv311/bin/activate  # Linux/macOS
# or
venv311\Scripts\activate      # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create `.env` file in the repository root with at least one provider configured:

#### Provider Selection (pick one)
- `GITHUB_TOKEN` — Primary provider (GitHub Models)
- `GEMINI_API_KEY` — Fallback provider (Google Gemini)

#### GitHub Models Configuration
- `GITHUB_MODEL` (optional, default: `openai/gpt-4.1-mini`)
- `GITHUB_MAX_TOKENS` (optional, default: `1000`)
- `GITHUB_MODELS_ENDPOINT` (optional, overrides default endpoints)
- `GITHUB_RETRY_ATTEMPTS` (optional, default: `4`)
- `GITHUB_RETRY_BASE_DELAY_SEC` (optional, default: `1.5`)
- `GITHUB_RETRY_MAX_DELAY_SEC` (optional, default: `20`)

#### Gemini Configuration (Fallback)
- `GEMINI_RETRY_ATTEMPTS` (optional, default: `4`)
- `GEMINI_RETRY_BASE_DELAY_SEC` (optional, default: `1.5`)
- `GEMINI_RETRY_MAX_DELAY_SEC` (optional, default: `20`)

**Example `.env`:**
```
GITHUB_TOKEN=ghp_xxxxx
GITHUB_MODEL=openai/gpt-4.1-mini
GEMINI_API_KEY=sk-xxxxx
GITHUB_RETRY_ATTEMPTS=6
GITHUB_RETRY_MAX_DELAY_SEC=60
```

### 4. Run Ingestion

```bash
python scripts/process_links.py
```

---

## Monitoring & Status

### Check Queue and Knowledge Status

```bash
python scripts/monitor_queue.py
```

Output:
- Queue pending URLs (if any)
- Total summaries in knowledge base
- Recovery recommendations

---

## Troubleshooting

### Rate Limit Errors (429 / RESOURCE_EXHAUSTED)

**What happens:**
- GitHub Models returns HTTP 429 (too many requests)
- Gemini raises `RESOURCE_EXHAUSTED` quota error
- System automatically retries with exponential backoff
- If retries exhausted, processing stops and **remaining URLs are preserved** in `input/links-to-summarize.md`

**Recovery:**
1. Check remaining queue:
   ```bash
   python scripts/monitor_queue.py
   ```
2. Wait for rate limit window to reset:
   - GitHub Models: ~1 hour
   - Gemini: Varies by account quota
3. Re-run the script to process remaining URLs:
   ```bash
   python scripts/process_links.py
   ```

**Increase Resilience:**

If you want the system to wait longer before giving up, increase retry parameters in `.env`:

```
GITHUB_RETRY_ATTEMPTS=6
GITHUB_RETRY_MAX_DELAY_SEC=60
GEMINI_RETRY_ATTEMPTS=6
GEMINI_RETRY_MAX_DELAY_SEC=60
```

This will retry up to 6 times with maximum 60-second delays between attempts.

### Provider Fallback: Switch to Gemini

**If GitHub Models is down or rate-limited:**

1. Comment out `GITHUB_TOKEN` in `.env`:
   ```bash
   # GITHUB_TOKEN=ghp_xxxx
   GEMINI_API_KEY=sk-xxxxxx
   ```
2. Re-run:
   ```bash
   python scripts/process_links.py
   ```
   The system will now use Gemini as the primary provider.

**Restore GitHub Models:**
1. Uncomment `GITHUB_TOKEN`
2. Re-run the script

### Malformed Response from Model

**Symptom:** Error mentions "JSON decode" or "SummaryOutput validation"

**Cause:** Model returned incomplete or invalid JSON response

**Recovery:**
1. This is a transient error—retry automatically (queue is preserved)
2. Wait a moment and re-run:
   ```bash
   python scripts/process_links.py
   ```
3. If same URL consistently fails, it may be unsuitable for summarization:
   - Remove it from `input/links-to-summarize.md`
   - Or try with a different model: `GITHUB_MODEL=openai/gpt-4-turbo`

### Queue Stuck or Lost

**Recover from accidental queue deletion:**

```bash
# View recent commits to queue file
git log --oneline input/links-to-summarize.md | head -5

# Show queue content from specific commit
git show <commit-hash>:input/links-to-summarize.md

# Restore queue from commit
git checkout <commit-hash> input/links-to-summarize.md
```

**Prevention:** The system preserves the queue automatically on any transient error. Only on **full success** is the queue cleared.

### Empty or Low-Quality Summaries

**Cause:** Model struggled with URL content (paywalled, PDF, complex media, etc.)

**Inspect and Recover:**

1. View recent summaries in a category:
   ```bash
   python scripts/recover.py --inspect Software-Engineering
   ```

2. Review generated file manually:
   ```bash
   cat knowledge/Software-Engineering/article-name.md
   ```

3. Delete if unsuitable:
   ```bash
   rm knowledge/Software-Engineering/bad-summary.md
   ```

4. Re-queue the URL:
   ```bash
   python scripts/recover.py --requeue "https://example.com/article"
   ```

5. Re-run processor:
   ```bash
   python scripts/process_links.py
   ```

---

## Debugging

### Enable Detailed Logs

Add to `.env`:
```
PYTHONVERBOSE=1
```

Run with verbose output:
```bash
python -u scripts/process_links.py 2>&1 | tee process.log
```

Look for:
- **Provider selection:** "Using GitHub Models" or "Using Gemini"
- **Retry attempts:** "Retry attempt X of Y"
- **Rate-limit headers:** "Retry-After: NNN"
- **Parsed output:** "Parsed SummaryOutput: title=..."

### Inspect Processing Queue

View current queue:
```bash
cat input/links-to-summarize.md
```

Add a URL to queue:
```bash
echo "https://example.com/article" >> input/links-to-summarize.md
```

Clear queue (use with caution):
```bash
python scripts/monitor_queue.py --clear
```

---

## Helper Scripts Reference

| Script | Command | Purpose |
| --- | --- | --- |
| Monitor | `python scripts/monitor_queue.py` | Show queue status and summary count |
| Monitor | `python scripts/monitor_queue.py --clear` | Clear queue (with confirmation) |
| Recover | `python scripts/recover.py --requeue <url>` | Re-queue URL for reprocessing |
| Recover | `python scripts/recover.py --requeue-file <file>` | Re-queue multiple URLs from file |
| Recover | `python scripts/recover.py --inspect <category>` | List recent summaries in category |
| Update | `python scripts/update_readme_only.py` | Regenerate README index (no processing) |

---

## GitHub Actions Workflow

The workflow (`.github/workflows/summarize.yml`) runs automatically when `input/links-to-summarize.md` is updated:

1. **Checkout** repository
2. **Setup** Python 3.11 environment
3. **Install** dependencies from `requirements.txt`
4. **Validate** environment (logs active provider)
5. **Process** links using `process_links.py`
6. **Commit & push** generated files

The workflow uses GitHub Actions secrets:
- `GITHUB_TOKEN` (auto-provided, enables GitHub Models)
- `GEMINI_API_KEY` (optional fallback, must be configured in repo settings)

### Monitoring Workflow Runs

View workflow status:
```
https://github.com/YOUR_USER/TLDR/actions
```

---

## Provider Architecture

### GitHub Models (Primary)
- **API:** REST (`https://models.github.ai/inference/chat/completions`)
- **Auth:** Bearer token (GITHUB_TOKEN)
- **Default model:** `openai/gpt-4.1-mini`
- **Transient errors:** HTTP 429, 5xx, network timeouts
- **Retry:** Exponential backoff respecting Retry-After header

### Gemini API (Fallback)
- **SDK:** google-generativeai
- **Auth:** API key (GEMINI_API_KEY)
- **Model:** `gemini-3.1-pro-preview`
- **Transient errors:** RESOURCE_EXHAUSTED, quota, 429, 5xx, timeouts
- **Retry:** Exponential backoff with keyword-based error classification

**Provider Selection Logic:**
1. If `GITHUB_TOKEN` is set → use GitHub Models
2. Else if `GEMINI_API_KEY` is set → use Gemini
3. Else → raise `NotImplementedError` (no provider configured)

---

## FAQ

**Q: How long does processing take?**
A: Depends on model and internet connection. Typically 2-5 seconds per URL.

**Q: Why is the queue preserved on failure?**
A: To prevent data loss. If processing fails midway, the next run continues from where it left off.

**Q: Can I use both providers in one run?**
A: No, one provider per run. The system selects the active provider at startup based on env var priority.

**Q: What happens if the model returns invalid JSON?**
A: The system treats it as a transient error, retries automatically, and preserves the queue.

**Q: How do I delete a generated summary?**
A: Delete the `.md` file from `knowledge/<category>/` and optionally re-queue the URL if you want to retry.

**Q: Can I manually add URLs to the queue?**
A: Yes, append to `input/links-to-summarize.md` or use `python scripts/recover.py --requeue <url>`

---

## Support

For issues not covered above:

1. Check the logs: `python -u scripts/process_links.py 2>&1 | tee debug.log`
2. View the queue: `cat input/links-to-summarize.md`
3. Check provider credentials in `.env`
4. Review GitHub Actions workflow runs (if using CI): GitHub repo → Actions tab

---

## Usage & Cost History

See [GEMINI_USAGE.md](GEMINI_USAGE.md) for detailed analysis of Gemini API consumption, cost breakdown, and rate-limit patterns from the initial 6-month evaluation period (Jun–Nov 2025).
