# Web Scraping with CSV Caching

This code scrapes data from a specified URL and stores it in a CSV file. It utilizes the `csv` library to read and write CSV files and the `BeautifulSoup` library to parse HTML content.

## Dependencies

The code requires the following dependencies:

- `csv`: This library is used for reading and writing CSV files.
- `BeautifulSoup`: This library is used for parsing HTML content.
- `cloudscraper`: This library is used to bypass Cloudflare protection.
- `timeit.Timer`: This library is used for timing the code execution.

Make sure to install these dependencies before running the code.

## Functionality

The code snippet includes the following functions:

1. `get_data_from_csv(csv_file, url)`: This function reads the data from a given CSV file and returns an array of rows that match the provided URL.

2. `scrapeWithCache(url, headers, csv_file)`: This function scrapes the specified URL and caches the data in a CSV file. It checks if the URL has already been scraped by searching for it in the CSV file. If the URL is not found, it uses `cloudscraper` to bypass Cloudflare protection, retrieves the HTML content, and parses it using `BeautifulSoup`. It then extracts the desired data from the HTML, creates a row of data, and appends it to the CSV file. Finally, it returns the scraped data.

## Usage

To use the code:

1. Set the CSV file path and headers in the variables `csv_file` and `headers`, respectively.

2. Specify the URL to scrape in the `url` variable.

3. Uncomment the section to print the result if desired. This section retrieves the data from the URL, prints the description, price, and location for each row, and checks if the URL is found in the CSV file.

4. Open Terminal.

5. If in another folder, move to the task3 folder using 'cd task3'.

6. Run the program using 'python web_scraping.py' or 'python3 web_scraping.py'.

## Runtime Result

The code includes a timer to measure the runtime of the `scrapeWithCache` function. The result is printed in seconds.