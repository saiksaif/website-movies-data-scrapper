# website-movies-data-scrapper

--------------------------------------------------------------------------------
----  This Project is was only made for learning and educational purposes.  ----
--------------------  It is not intended to be misused.  -----------------------
--------------------------------------------------------------------------------

# Project Description

It is a bot that will get list of all movies from a website using requests.
After that it will use undetected-chromedriver with selenium to scrape details
of the movies and get an m3u8 link of the streaming movie.

# Pre-Requisites

Install the following:

1- Beautiful Soup
```
pip install bs4
/..

../
from bs4 import BeautifulSoup
```

2- Selenium
```
pip install selenium
/..

../
from selenium import webdriver
```

3- Undetected Chromedriver
```
pip install undetected_chromedriver
/..

../
import undetected_chromedriver as uc
```

Other than these you must have the following on your system:

1- Google Chrome

2- Python (3.11 used in this project)

3- A user profile signed in on google chrome

# Running the Bot

Follow these steps to get the bot to run for the first time:

1- First you should understand the first 5 script files in any order and see what they are doing.

2- After understanding them, open the scriptF.py file.

3- Change the path for chrome user data at the end of the file.

4- Change the links and html scrappers according to the website you want to scrape on.

5- In terminal run: python scriptF.py OR python3 scriptF.py (For MacOS)

6- The bot will scrape the website movie list one page at a time. so how many pages the bot scrapes in one run can be adjusted by increasing iterations of the for loop at end of code.

7- All data scraped will finally be stored in a listF.txt file and a listF.csv file which can be viewed in excel.

8- To avoid detection, You can run multiple instances of this bot with different range of pages on different machines.

# Happy Data Scraping :)
