import csv
from bs4 import BeautifulSoup

# Bypassing cloudfare
import cloudscraper

# Timing
from timeit import Timer

# Retrieve csv file data and return as an array
def get_data_from_csv(csv_file, url):
    data = []
    with open(csv_file, mode='r', encoding='utf8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the headers
        url_index = headers.index('url')
        for row in reader:
            if row[url_index] == url:
                data.append(row)
    return data


def scrapeWithCache(url, csv_file, headers):

    # Check if url already scraped
    with open(csv_file, 'r', encoding='utf8') as data:
        
        s = data.read()
        
        if url not in s:
            scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
            content = scraper.get(url).content
            soup = BeautifulSoup(content, features='lxml')
            
            items = soup.find_all('div', class_ = 're__card-info')

            for item in items:
                # Get values for 1 row of data
                description = item.h3.text.strip()
                price = item.find('span', class_ = 're__card-config-price').text
                location = item.find('div', class_ = 're__card-location').select('span')[1].text
                
                # The availabilities of all fetched properties are not specified,
                # but since non-available properties are not displayed,
                # all fetched properties are assumed to be available
                row_data = [{'url' : url,'description' : description,'price' : price,'location' : location,'availability' : 'Available'}]
                
                # Append new row data to file
                with open(csv_file, mode='a', encoding='utf-8', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writerows(row_data)
                
            data = get_data_from_csv(csv_file, url)
            return data
        else:
            # Retrieve data if previously scraped
            data = get_data_from_csv(csv_file, url)
            return data
        
# CSV file path and headers
csv_file = 're_data.csv'
headers = ['url', 'description', 'price', 'location', 'availability']

# Scrape from this url
# To scrape from different paginations of this site, add 'p<page-number>'
# For example: 'https://batdongsan.com.vn/nha-dat-ban/p2'
url = 'https://batdongsan.com.vn/nha-dat-ban/'

# Time the code
t = Timer(lambda: scrapeWithCache(url, csv_file, headers))

#################################################

# # DE-COMMENT THIS SECTION TO PRINT THE RESULT

# # Magic happens here
# data = scrapeWithCache(url,headers,csv_file)
        
# # Print the retrieved data
# if data:
#     for row in data:
#         print('Description:', row[1])
#         print('Price:', row[2])
#         print('Location:', row[3])
#         print('Availability:', row[4])
#         print('')
# else:
#     print('URL not found in the CSV file.')

#################################################

# Runtime Result
print('Runtime:',t.timeit(number=1),'(s)')
print('')