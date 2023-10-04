import undetected_chromedriver as uc 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = uc.ChromeOptions() 
options.add_argument("--user-data-dir=C:\\Users\\saifa\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
 
driver = uc.Chrome(options=options)
# driver.execute_cdp_cmd("Emulation.setCPUThrottlingRate", {'rate': 10})
driver.get('https://bflix.to/movie/free-from-the-shadows-hd-ww98l/1-1')

targetLink = '--empty--'
wait = WebDriverWait(driver, 20)
try:
    myElem = wait.until(EC.visibility_of_element_located((By.ID, 'film-servers')))
    try:
        ul_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.film-server[data-id='45']")))  
        try:
            ul_element.click()
            try:
                player = wait.until(EC.presence_of_element_located((By.ID, 'player')))
                urlPopup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Click or right click to open the m3u8 URL']")))
                targetLink = urlPopup.get_attribute("href")
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
    date_created = date_element.text
except:
    print("Unable to find date")

print(date_created)
print(targetLink)
driver.get_screenshot_as_file('screenshot-uc.png')
driver.close