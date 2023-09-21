import requests
import random
from bs4 import BeautifulSoup
import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def has_only_poster_class(tag):
    return tag.name == 'div' and tag.get('class') == ['poster'] and len(tag.attrs) == 1

def run_movies_getter(pageNum):
    url = "https://bflix.io/movie?page=" + str(pageNum)
    print(url)

    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    ]
    user_agent = random.choice(user_agents)

    # Define the headers based on what you see in Postman
    # GET /movie HTTP/1.1
    # "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    headers = {
        "User-Agent" : user_agent,
        # "User-Agent" : "Site24x7",
        "Cache-Control" : "no-cache",
        "Accept" : "*/*",
        "Connection" : "Keep-Alive",
        "Accept-Encoding" : "gzip",
        "X-Site24x7-Id" : "1420e1c1b70c",
        "Host" : "bflix.io"
    }

    response = requests.get(url, headers=headers)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False) 

    if response.status_code == 200:
        print("Response Content:")
        print(response.status_code)

        html_content = response.text

        with open('sample.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        soup = BeautifulSoup(response.text, 'html.parser')
        poster_links = soup.find_all(has_only_poster_class, recursive=True)
        
        driver = webdriver.Chrome(options=options)
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent[0]})
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})

        extracted_data = []
        for div in poster_links:
            a_tags = div.find_all('a')
            for a_tag in a_tags:
                img_tags = a_tag.find_all('img')
                if img_tags:
                    extracted_tags = [str(tag) for tag in extracted_data]
                    img_alt = img_tags[0].get('alt', '') 
                    a_href = a_tag.get('href', '')
                    extracted_data.append([img_alt, run_movie_date_getter('https://bflix.io' + a_href + '/1-1', driver), 'https://bflix.io' + a_href + '/1-1'])


        driver.quit()
        csv_filename = 'list.csv'

        # Check if the CSV file is empty
        csv_exists = os.path.isfile(csv_filename)
        is_empty = not csv_exists or os.stat(csv_filename).st_size == 0

        with open(csv_filename, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            if is_empty:
                csvwriter.writerow(['Name', 'Release', 'URL'])
            
            # Write data rows
            csvwriter.writerows(extracted_data)

        with open('list.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(extracted_tags))
    else:
        print("Request failed with status code:", response.status_code)

def run_movie_date_getter(url, driver):
    driver.get(url)

    # time.sleep(2)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@itemprop="dateCreated"]')))

    date_created = element.text
    # print(date_created)
    return date_created

for n in range(1, 2):
    print('Starting')
    run_movies_getter(n)
    print('Waiting for round ' + str(n+1))
    time.sleep(5)

# run_movie_date_getter('https://bflix.io/movie/the-quintessential-quintuplets-movie-20r64/1-1')