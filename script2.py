from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
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
# options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--lang=en_US') 
options.add_argument("--log-level=2")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('--ignore-ssl-errors')
options.add_argument('--no-sandbox')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False) 
options.page_load_strategy = 'none'

print('Staring hits')
service = ChromeService(executable_path=r"C:\Users\saifa\OneDrive\Desktop\BFLIX\webDrivers\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)

driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"})
# driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})
driver.get('https://bflix.io/movie/the-quintessential-quintuplets-movie-20r64/1-1')
# body_element = EC.presence_of_element_located(By.TAG_NAME, "body")
# driver.send_keys(Keys.ESCAPE)
# driver.execute_script('return window.stop')
driver.implicitly_wait(10)
print(driver.execute_script("return document.body.scrollHeight"))
# print(driver.execute_script("console.log = function() {};"))
print('Hits ended')

wait = WebDriverWait(driver, 20)
try:
    myElem = wait.until(EC.presence_of_element_located((By.ID, 'servers')))
    print("Servers found!")
    print(driver.execute_script("return document.body.scrollHeight"))
    driver.execute_script('return window.stop')
    # try:
    #     myElem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'server')))
    #     print("Server childs found!")
    #     print(driver.execute_script("return document.body.scrollHeight"))
        # driver.execute_script('return window.stop')
    driver.get_screenshot_as_file('screenshot.png')
    # except:
    #     print("Loading took too much time!")
    #     print(driver.execute_script("return document.body.scrollHeight"))
except:
    print("Loading took too much time!")
    print(driver.execute_script("return document.body.scrollHeight"))
    # driver.get_screenshot_as_file('screenshot.png')
    
print('Page length before all JS runs')
print(driver.execute_script("return document.body.scrollHeight"))

try:
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    print('Page length after all JS runs')
    print(driver.execute_script("return document.body.scrollHeight"))
except:
    print("All JS did not run, here is the page length!")
    print(driver.execute_script("return document.body.scrollHeight"))
# loginBtn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "signin")))
# ul_element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "server")))
# ul_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.server[data-id='45']")))

print('Final Page Length')
print(driver.execute_script("return document.body.scrollHeight"))

# JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
# network_requests = driver.execute_script(JS_get_network_requests)
# for n in network_requests:
#     if ".m3u8" in n["name"]: 
#         print(n["name"])

with open('sample2.html', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

# serverType = section.text
# print(serverType)
# input('Press ENTER to close the automated browser')
driver.quit()

# #####################################################################################################################
# ################################              FireFox Version            ############################################
# #####################################################################################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service as GeckoService
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
# import random
# import time

# user_agents = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/109.0.0.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/109.0.0.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/108.0.0.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/108.0.0.0',
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/108.0.0.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Firefox/16.1',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Firefox/16.1',
# ]
# user_agent = random.choice(user_agents)

# options = Options()
# options.headless = True
# options.add_argument('--width=1920')
# options.add_argument('--height=1080')
# # options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('--lang=en_US') 
# # options.add_argument('--no-sandbox')
# # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
# options.set_preference("intl.accept_languages", "en-US")
# options.set_preference("general.useragent.override", user_agent)
# # options.setProperty("webdriver.gecko.driver","path of geckodriver.exe")

# service = GeckoService(executable_path=GeckoDriverManager().install())

# with webdriver.Firefox(options=options, service=service) as driver:
#     print('Starting hits')
#     # driver.get('https://bflix.io/')
#     driver.get('https://bflix.io/movie/the-quintessential-quintuplets-movie-20r64/1-1')
#     print(driver.execute_script("return document.body.scrollHeight"))
#     print('Hits ended')

#     wait = WebDriverWait(driver, 20)
#     # section = wait.until(presence_of_element_located((By.ID, 'servers')))
#     wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

#     driver.save_screenshot('screenshot-f.png')
#     with open('sample2.html', 'w', encoding='utf-8') as file:
#         file.write(driver.page_source)

#     print(driver.execute_script("return document.body.scrollHeight"))

#     # serverType = section.text
#     # print(serverType)
#     driver.quit()
