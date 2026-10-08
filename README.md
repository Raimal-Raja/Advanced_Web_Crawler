# Advanced Web Crawler

Python Indeed scraping prototype for collecting job listings across country domains and saving CSV results.

## Repository guide

### Contents

- [Indeed_job_Scraper.py](Indeed_job_Scraper.py)
- [Multi_Country_Job_results.csv](Multi_Country_Job_results.csv)
- [README.md](README.md)
- [requirements.txt](requirements.txt)

### Getting started

```bash
git clone https://github.com/Raimal-Raja/Advanced_Web_Crawler.git
cd Advanced_Web_Crawler
```

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r "requirements.txt"
```

Application entry point:

```bash
python Indeed_job_Scraper.py
```

### Configuration and limitations

Live scraping depends on site permissions, browser availability, current page markup, and anti-bot responses. Passing syntax checks does not verify live collection. Browser-handling code does not guarantee access.

### Validation

Reviewed on 2026-10-08. Python syntax checks passed for 1 source files. Syntax validation does not establish runtime correctness or dependency compatibility.

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

No top-level license file was found during this review.
