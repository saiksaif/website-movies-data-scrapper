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
import undetected_chromedriver as uc

def has_only_poster_class(tag):
    return tag.name == 'div' and tag.get('class') == ['poster'] and len(tag.attrs) == 1

def run_movies_getter(pageNum, driver):
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

    if response.status_code == 200:
        print("Response Content:")
        print(response.status_code)

        html_content = response.text

        with open('sample.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        soup = BeautifulSoup(response.text, 'html.parser')
        poster_links = soup.find_all(has_only_poster_class, recursive=True)

        extracted_data = []
        for div in poster_links:
            a_tags = div.find_all('a')
            for a_tag in a_tags:
                img_tags = a_tag.find_all('img')
                if img_tags:
                    extracted_tags = [str(tag) for tag in extracted_data]
                    img_alt = img_tags[0].get('alt', '') 
                    a_href = a_tag.get('href', '')
                    getMovie = run_movie_date_and_m3u8_getter('https://bflix.io' + a_href + '/1-1', driver)
                    extracted_data.append([img_alt, getMovie[0], 'https://bflix.io' + a_href + '/1-1', getMovie[1]])

        csv_filename = 'listF.csv'
        # Check if the CSV file is empty
        csv_exists = os.path.isfile(csv_filename)
        is_empty = not csv_exists or os.stat(csv_filename).st_size == 0

        with open(csv_filename, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            if is_empty:
                csvwriter.writerow(['Name', 'Release', 'URL', 'm3u8 URL'])
            
            # Write data rows
            csvwriter.writerows(extracted_data)

        with open('listF.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(extracted_tags))
    else:
        print("Request failed with status code:", response.status_code)

def run_movie_date_and_m3u8_getter(url, driver):
    driver.get(url)
    targetLink = 'No Link Found'
    date_created = 'No Date Found'

    wait = WebDriverWait(driver, 10)
    try:
        myElem = wait.until(EC.presence_of_element_located((By.ID, 'servers')))
        try:
            ul_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.server[data-id='45']")))       
            try:
                ul_element.click()
                try:
                    player = wait.until(EC.presence_of_element_located((By.ID, 'player')))
                    urlPopup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Click or right click to open the m3u8 URL']")))
                    targetLink = str(urlPopup.get_attribute("href"))
                except:
                    print('Unable to locate player')            
            except:
                print('Unable to click button')
        except:
            print("Loading 2 took too much time!")
    except:
        print("Loading took too much time!")
    try:
        date_element = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@itemprop="dateCreated"]')))
        date_created = str(date_element.text)
    except:
        print("Unable to find date")

    time.sleep(1)
    returnData = [date_created, targetLink]
    return returnData

    
options = uc.ChromeOptions() 
options.add_argument("--user-data-dir=C:\\Users\\saifa\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--disable-gpu")
driver = uc.Chrome(options=options) 

for n in range(2, 3):
    print('Starting')
    run_movies_getter(n, driver)
    print('Waiting for round ' + str(n+1))
    time.sleep(5)

driver.quit()

# run_movie_date_getter('https://bflix.io/movie/the-quintessential-quintuplets-movie-20r64/1-1')