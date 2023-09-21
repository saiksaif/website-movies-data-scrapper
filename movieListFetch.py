# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium_stealth import stealth
# import time

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")

# # options.add_argument("--headless")

# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options, executable_path="./chromedriver_mac_arm64/chromedriver")

# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )

# url = "https://bflix.io/movie"
# driver.get(url)
# time.sleep(5)

# driver = stealth.Chrome()
# driver = webdriver.Chrome()
# driver = webdriver.Chrome('/Users/saifali/Desktop/untitled folder/chromedriver_mac_arm64')
# wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
# driver.get('https://bflix.io/')

# r = requests.get('http://www.hearthpwn.com/cards?filter-attack-val=1&filter-attack-op=1&display=1', allow_redirects=False)

# try:
#     # print("Finding search form elements...")
#     # first_field = wait.until(EC.presence_of_element_located((By.NAME, 'NDC1')))
#     # second_field = wait.until(EC.presence_of_element_located((By.NAME, 'txtmsisdn')))
#     # submit_button = wait.until(EC.presence_of_element_located((By.ID, 'btnSubmit')))

#     # print("Entering values into fields...")
#     # first_field.send_keys('310')
#     # second_field.send_keys('0671698')
#     # second_field.send_keys(Keys.RETURN)  # Press Enter to submit
#     # wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
#     print("Finding First Menu...")
#     wait.until(EC.presence_of_element_located((By.ID, 'menu')))
#     print("First Menu Found...")

#     driver.navigate().to("https://bflix.io/movie/")

#     print("Finding Second Menu...")
#     wait.until(EC.presence_of_element_located((By.ID, 'menu')))
#     print("Second Menu Found...")

#     page_source = driver.page_source
#     soup = BeautifulSoup(page_source, 'html.parser')

#     # error_div = soup.find('div', class_='error1')
#     # result_div = soup.find('div', id='searchedList')

#     # if error_div is None and result_div and result_div.findAll('div', class_='col-md-6 box'):
#     #     results = result_div.findAll('div', class_='col-md-6 box')
#     #     for result in results:
#     #         print(result.text)
#     # elif result_div:
#     #     print("No search results found.") 
#     # else:
#     #     print("Something went wrong.")

# except Exception as e:
#     print("An error occurred:", str(e))

# finally:
#     print("Script finished. The tab will remain open for your inspection.")
#     wait = WebDriverWait(driver, 10000)  # Adjust the timeout as needed
#     input("Press Enter to close the tab...")
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
import random

# create a new Service instance and specify path to Chromedriver executable
service = ChromeService(executable_path=ChromeDriverManager().install())


# Step 2: Change browser properties
# create a ChromeOptions object
options = webdriver.ChromeOptions()

#run in headless mode
options.add_argument("--headless")

# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')
 
# disable pop-up blocking
options.add_argument('--disable-popup-blocking')
 
# start the browser window in maximized mode
options.add_argument('--start-maximized')
 
# disable extensions
options.add_argument('--disable-extensions')
 
# disable sandbox mode
options.add_argument('--no-sandbox')
 
# disable shared memory usage
options.add_argument('--disable-dev-shm-usage')


# Set navigator.webdriver to undefined
# create a driver instance
driver = webdriver.Chrome(service=service, options=options)

# Change the property value of the navigator for webdriver to undefined
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")



# Step 3: Rotate user agents 
user_agents = [
    # Add your list of user agents here
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
]

# select random user agent
user_agent = random.choice(user_agents)

# pass in selected user agent as an argument
options.add_argument(f'user-agent={user_agent}')

# set user agent using execute_cpd_cmd
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})


# Step 4: Scrape using Stealth
#enable stealth mode
stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

# navigate to nowsecure
driver.get("https://bflix.io/movie/")
 
# Wait for page to load
while driver.execute_script("return document.readyState") != "complete":
    pass

# Take screenshot
driver.save_screenshot("bflix.png")

print(driver.page_source)
input("Press Enter to close the tab...")
 
# Close browser
driver.quit()
