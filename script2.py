from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import random
import time

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

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False) 

print('Staring hits')
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent[0]})
driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})
driver.get('https://bflix.io/movie/the-quintessential-quintuplets-movie-20r64/1-1')
driver.implicitly_wait(5)
print('Hits ended')	

# element1 = wait.until(EC.presence_of_element_located((By.ID, 'servers')))
# element = wait.until(EC.visibility_of_element_located((By.XPATH, '//section[@id="servers"]')))
# element = wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="server"]')))
# element = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@data-id="45"]')))
# element = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@class="server"]')))
# section = wait.until(EC.presence_of_element_located((By.ID, 'servers')))

wait = WebDriverWait(driver, 20)
section = wait.until(EC.presence_of_element_located((By.ID, 'servers')))
print('Section found ' + section.text + ' end')
# Now, wait for the <ul> element within the <section> to have child <li> elements
# ul_element = wait.until(EC.presence_of_element_located((By.XPATH, '//section[@id="servers"]//ul[li]')))
ul_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.server[data-id*='45']")))

print('Section content found')
serverType = ul_element.text

driver.quit()
serverType = ul_element.text
print('\|/')
print(serverType)
print('/|\\')
driver.quit()
