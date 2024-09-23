# Multi-Country Indeed Job Scraper

This Python script scrapes job listings from Indeed.com across 14 different country domains for multiple job professions. It extracts job details including title, company name, location, job URL, and company URL, then exports the results to a CSV file.

## Features

- Scrapes job listings from 14 Indeed.com country domains
- Searches for 14 different job professions
- Extracts comprehensive job details including company URLs
- Implements multi-threading for faster scraping
- Uses cloudscraper to bypass anti-bot measures
- Implements retry mechanism for handling network errors
- Exports results to a CSV file
- Includes user authentication for script execution

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/multi-country-indeed-scraper.git
   ```
2. Navigate to the project directory:
   ```
   cd multi-country-indeed-scraper
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python multi_country_indeed_scraper.py
   ```
2. Enter the username and password when prompted:
   - Username: Professor
   - Password: raja
3. The script will start scraping job listings from all specified countries and job professions.
4. Results will be saved in `Multi_Country_Job_results.csv` in the same directory.

## Customization

- To modify the list of countries or their Indeed URLs, edit the `domains` dictionary in the `main()` function.
- To change the job professions being searched, modify the `job_professions` list in the `main()` function.
- Adjust the `MAX_RETRIES` and `RETRY_DELAY` variables to fine-tune the retry mechanism.

## Dependencies

- [cloudscraper](https://github.com/VeNoMouS/cloudscraper): For bypassing Cloudflare's anti-bot page.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): For parsing HTML and extracting data.
- [pandas](https://pandas.pydata.org/): For creating and exporting data to CSV.
- [requests](https://docs.python-requests.org/en/latest/): For making HTTP requests.
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html): For implementing multi-threading.

## Additional Resources

1. [Python Documentation](https://docs.python.org/3/)
2. [Web Scraping Best Practices](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)
3. [Indeed.com Robot.txt](https://www.indeed.com/robots.txt)
4. [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
5. [Threading in Python](https://realpython.com/intro-to-python-threading/)
6. [Python Logging](https://docs.python.org/3/library/logging.html)

## Ethical Considerations

Web scraping may be against the terms of service of some websites. Always review and respect the target website's `robots.txt` file and terms of service. Use this script responsibly and ensure you have permission to scrape the target websites. The authors are not responsible for any misuse of this script.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/yourusername/multi-country-indeed-scraper/issues) if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
