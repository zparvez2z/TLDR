# Contributing to TLDR

Thank you for your interest in contributing! This guide will help you set up your development environment and run tests locally.

## Setup

### 1. Clone and navigate to the repository
```bash
git clone https://github.com/zparvez2z/TLDR.git
cd TLDR
```

### 2. Create a Python virtual environment
```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root and add your API keys:
```bash
GITHUB_TOKEN=<your-github-personal-access-token>
GITHUB_MODEL=openai/gpt-4.1-mini  # Optional; defaults to openai/gpt-4.1-mini
GEMINI_API_KEY=<your-gemini-api-key>  # Optional; fallback provider
```

See [OPERATIONS.md](OPERATIONS.md) for detailed configuration options.

## Running Tests

### Run all tests
```bash
pytest -q
```

### Run tests with verbose output
```bash
pytest -v
```

### Run a specific test file
```bash
pytest tests/test_arxiv_extractor.py -v
```

### Run tests with coverage
```bash
pytest --cov=scripts --cov=tests
```

## Running the Workflow Locally

### Add links to summarize
Edit `input/links-to-summarize.md`:
```markdown
https://example.com/article1
https://arxiv.org/html/2604.27351v1
```

### Run the summarization workflow
```bash
python scripts/process_links.py
```

This will:
1. Fetch and parse each URL
2. Call the language model (GitHub Models primary, Gemini fallback)
3. Save summaries to `knowledge/<Category>/<filename>.md`
4. Update `README.md` with the new entries

### Monitor the queue
If processing stops due to transient errors, check the queue status:
```bash
python scripts/monitor_queue.py
```

### Recover from failures
To retry failed links:
```bash
python scripts/recover.py
```

See [OPERATIONS.md](OPERATIONS.md) for more monitoring and recovery details.

## Code Quality

### Syntax check
```bash
python -m py_compile scripts/*.py
```

### Linting
```bash
ruff check scripts/ tests/
```

## Git Workflow

### Create a feature branch
```bash
git checkout -b feature/your-feature-name
```

### Make your changes, test, and commit
```bash
git add <files>
git commit -m "type: brief description"
```

Commit types: `feat`, `fix`, `ci`, `test`, `docs`, `refactor`, `chore`.

### Push and open a PR
```bash
git push origin feature/your-feature-name
```

Then open a pull request on GitHub. CI will automatically run tests, syntax check, and linting on your branch.

## Pull Request Checklist

- [ ] Tests pass locally (`pytest -q`)
- [ ] Syntax check passes (`python -m py_compile scripts/*.py`)
- [ ] Linting is clean (`ruff check scripts/ tests/`)
- [ ] Commit messages follow conventions (type: description)
- [ ] README or OPERATIONS.md updated if behavior changed
- [ ] Test fixtures added if appropriate

## Troubleshooting

### Import errors when running scripts directly
Ensure you're running from the project root:
```bash
cd /path/to/TLDR
python scripts/process_links.py
```

Or install the project in editable mode:
```bash
pip install -e .
```

### API rate limits
If you hit rate limits, see [GEMINI_USAGE.md](GEMINI_USAGE.md) for quota tracking and [OPERATIONS.md](OPERATIONS.md) for retry configuration.

### Test fixture issues
Fixtures are stored in `tests/fixtures/`. Check that HTML files are valid and use UTF-8 encoding.

## Questions?

Open an issue on GitHub or check [OPERATIONS.md](OPERATIONS.md) for detailed operational guidance.
