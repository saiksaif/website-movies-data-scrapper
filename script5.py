import undetected_chromedriver as uc 
from fake_useragent import UserAgent
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ua = UserAgent() 
options = uc.ChromeOptions() 
options.add_argument("--user-data-dir=C:\\Users\\saifa\\AppData\\Local\\Google\\Chrome\\User Data")
 
driver = uc.Chrome(options=options)
driver.get('https://hlsjs.video-dev.org/demo/?src=https%3A%2F%2Ftest-streams.mux.dev%2Fx36xhzz%2Fx36xhzz.m3u8&demoConfig=eyJlbmFibGVTdHJlYW1pbmciOnRydWUsImF1dG9SZWNvdmVyRXJyb3IiOnRydWUsInN0b3BPblN0YWxsIjpmYWxzZSwiZHVtcGZNUDQiOmZhbHNlLCJsZXZlbENhcHBpbmciOi0xLCJsaW1pdE1ldHJpY3MiOi0xfQ==')


wait = WebDriverWait(driver, 20)
player = wait.until(EC.presence_of_element_located((By.NAME, 'config-apply')))
player.click()

# JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
# network_requests = driver.execute_script(JS_get_network_requests)
# for n in network_requests:
#     if ".m3u8" in n["name"]: 
#         print(n["name"])

urlPopup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Click or right click to open the m3u8 URL']")))
print(urlPopup.get_attribute("href"))
# title="Click or right click to open the m3u8 URL"

input('Close software...')
driver.close