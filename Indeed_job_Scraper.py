# Raimal Raja
#this program will fatch data from 14 domains of indeed.com. Job name, company name, location, url, and save it into csv file
# cloudscraper = for bypassing bot protection
# beautiful soup = for parsing HTML
# pandas = for interacting with data, manuplating, organizing, using structure named DataFrame
# time =  for measuring elapsed time, sleep, delaying program so that it should not rush on server
# random = for randomizing number of attemp, and simulating random events or avoiding detection by websites.
# getpass = for authentication before excuting main body of code 
# sys = this working like os  module but it is defferent from it, sys module deals with python runtime environment and access to system-specific parameters and functions
# concurrent.futures = For multiprocessing and multi-Threading
# logging = for printing message like INFO, WARNING, Error, and also monitoring, and troubleshooting program.
# Request Exception = for all exceptions that can occur during HTTP requests. like ConnectionError, HTTPError,and Timeout

import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import getpass
import sys
import concurrent.futures
import logging
from requests.exceptions import RequestException

# Setting up logging to track my script's progress and catch issues, if any occurs during or in the middle of program execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# These variables control my retry mechanism for network errors
MAX_RETRIES = 3
RETRY_DELAY = 5

def login():
    #This function handles user authentication.
    attempts = 3
    while attempts > 0:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        
        # if condition for varifying credentials
        if username == "Professor" and password == "raja":
            logging.info("Login successful!")
            return True
        else:
            # it only give me three chance to enter password after that it will be terminated
            attempts -= 1
            logging.warning(f"Invalid username or password. {attempts} attempts remaining.")
    
    logging.error("Login failed. Exiting the program.")
    sys.exit(1)

def export(results):
    #This function exports program scraped data to a CSV file.
    df = pd.DataFrame(results)
    
    # by using Pandas's class DataFrame, opening file in append mode to append data
    df.to_csv("Multi_Country_Job_results.csv", mode="a", index=False, header=True)
    logging.info("Results exported to Multi_Country_Job_results.csv")

def scrape_job(base_url, job_search, country):
    #This function scrapes job listings for a specific job search term in a given country.
    url = f"{base_url}jobs?q={job_search.replace(' ', '+')}&l="
    scraper = cloudscraper.create_scraper()
    
    # This loop implements prgram retry mechanism for network errors
    for attempt in range(MAX_RETRIES):
        try:
            response = scraper.get(url)
            response.raise_for_status()
            break
        except RequestException as e:
            if attempt < MAX_RETRIES - 1:
                logging.warning(f"Request failed. Retrying in {RETRY_DELAY} seconds... ({attempt + 1}/{MAX_RETRIES})")
                time.sleep(RETRY_DELAY)
            else:
                logging.error(f"Failed to fetch {url} after {MAX_RETRIES} attempts. Error: {str(e)}")
                return []

    # I have used BeautifulSoup to parse the HTML and extract job listings
    bs = BeautifulSoup(response.text, "html.parser")
    job_list = bs.find('ul', {'class': 'css-zu9cdh'})
    
    if not job_list:
        logging.warning(f"No job listings found for {job_search} in {country}")
        return []

    jobs = job_list.find_all('div', {'class': 'job_seen_beacon'})
    info = []

    # extract data for each job listing
    for job in jobs:
        job_data = extract_job_data(job, base_url, scraper)
        if job_data:
            job_data['country'] = country
            job_data['search_term'] = job_search
            info.append(job_data)

    logging.info(f"Scraped {len(info)} jobs for {job_search} in {country}")
    return info

def extract_job_data(job, base_url, scraper):
    
    # This function extracts relevant data from a single job listing, including the company URL.
    TITLE = job.find('h2', {'class': 'jobTitle'})
    if not TITLE:
        return None
    
    title = TITLE.text.strip()
    link = TITLE.find('a')
    if not link or 'data-jk' not in link.attrs:
        return None
    
    job_key = link.attrs['data-jk']
    job_url = f"{base_url}viewjob?jk={job_key}"
    
    company_name_element = job.find('span', {'class': 'css-63koeb'})
    company_name = company_name_element.text.strip() if company_name_element else "N/A"
    
    company_location_element = job.find('div', {'class': "company_location"})
    company_location = company_location_element.text.strip() if company_location_element else "N/A"
    
    # Here's where i extract the company URL
    company_url = extract_company_url(job_url, scraper)
    
    return {
        'title': title,
        'company name': company_name,
        'company location': company_location,
        'job url': job_url,
        'company url': company_url
    }

def extract_company_url(job_url, scraper):
    
    # This new function extracts the company URL from the job detail page.
    for attempt in range(MAX_RETRIES):
        try:
            response = scraper.get(job_url)
            response.raise_for_status()
            break
        except RequestException as e:
            if attempt < MAX_RETRIES - 1:
                logging.warning(f"Failed to fetch job details. Retrying in {RETRY_DELAY} seconds... ({attempt + 1}/{MAX_RETRIES})")
                time.sleep(RETRY_DELAY)
            else:
                logging.error(f"Failed to fetch job details after {MAX_RETRIES} attempts. Error: {str(e)}")
                return "N/A"

    soup = BeautifulSoup(response.text, 'html.parser')
    company_link = soup.find('a', {'data-tn-element': 'companyName'})
    
    if company_link and 'href' in company_link.attrs:
        return company_link['href']
    else:
        return "N/A"

def scrape_country(country, base_url, job_professions):
    
    #This function scrapes all job professions for a given country.
    country_results = []
    scraper = cloudscraper.create_scraper()
    for job in job_professions:
        country_results.extend(scrape_job(base_url, job, country))
        
        # I add a small delay between requests to be polite to the server, and not rush
        time.sleep(random.uniform(3, 10))
    return country_results

def main():
    # This the list of domain given to me, i have saved in a dictionary maps countries to their Indeed URLs
    domains = {
        "United States": "https://www.indeed.com/",
        "Japan": "https://jp.indeed.com/",
        "Germany": "https://de.indeed.com/",
        "India": "https://in.indeed.com/",
        "United Kingdom": "https://www.indeed.co.uk/",
        "France": "https://www.indeed.fr/",
        "Italy": "https://it.indeed.com/",
        "Brazil": "https://www.indeed.com.br/",
        "Canada": "https://ca.indeed.com/",
        "Russia": "https://ru.indeed.com/",
        "South Korea": "https://kr.indeed.com/",
        "Australia": "https://au.indeed.com/",
        "Spain": "https://www.indeed.es/",
        "Mexico": "https://www.indeed.com.mx/"
    }

    # This list contains all the job professions for which i need to write scraper
    job_professions = [
        "DevOps engineer",
        "Lens Coater",
        "Plumbing Designer",
        "Financial Assistance Advisor",
        "Locker Room, Coatroom, and Dressing Room Attendants",
        "Visual Merchandiser (VM)",
        "Wood Stainer",
        "Size Mixer",
        "Marine Diesel Mechanic",
        "Soaking Pits Supervisor",
        "Plasma Processing Centrifuge Operator",
        "Certified Income Tax Preparer (CTP)",
        "Public Relations Coordinator (PR Coordinator)",
        "Paper Machine Tender"
    ]

    all_results = []

    # i used a ThreadPoolExecutor to scrape multiple countries concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_country = {executor.submit(scrape_country, country, base_url, job_professions): country 
                             for country, base_url in domains.items()}
        
        # this will collect results as they complete and handle any exceptions
        for future in concurrent.futures.as_completed(future_to_country):
            country = future_to_country[future]
            try:
                results = future.result()
                all_results.extend(results)
                logging.info(f"Completed scraping for {country}")
            except Exception as exc:
                logging.error(f"{country} generated an exception: {exc}")

    # Finally, i have exported all the collected results
    export(all_results)
    logging.info("Scraping completed. Results saved to Multi_Country_Job_results.csv")

if __name__ == "__main__":
    # We only proceed with scraping if the login is successful
    if login():
        main()
