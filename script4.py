from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# driver = webdriver.PhantomJS(executable_path=r'C:\Users\saifa\AppData\Roaming\npm\node_modules\phantomjs-prebuilt\bin\phantomjs') # or add to your PATH

driver = webdriver.PhantomJS() # or add to your PATH
driver.set_window_size(1024, 768) # optional

driver.get('https://google.com/')
driver.save_screenshot('screen.png') # save a screenshot to disk

sbtn = driver.find_element_by_css_selector('button.gbqfba')
sbtn.click()