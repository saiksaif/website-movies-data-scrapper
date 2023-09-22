from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_argument("--log-level=2")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
service = ChromeService(executable_path=r"C:\Users\saifa\OneDrive\Desktop\BFLIX\webDrivers\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url2 = "https://developer-tools.jwplayer.com/stream-tester"
driver.get(url2)

driver.get_screenshot_as_file('screenshot-sniffer.png')
    
JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
network_requests = driver.execute_script(JS_get_network_requests)
for n in network_requests:
    if ".m3u8" in n["name"]: 
        print(n["name"])

# Actual m3u8 link
# https://videos-cloudfront-usp.jwpsrv.com/650e0a77_ab6e2122a67d4627430adfbfa4d6a71139881567/site/LOPLPiDX/media/yp34SRmf/version/IFBsp7yL/manifest.ism/manifest-audio_eng=112000-video_eng=405144.m3u8
# Sniffed m3u8 link
# https://videos-cloudfront-usp.jwpsrv.com/650e0a77_ab6e2122a67d4627430adfbfa4d6a71139881567/site/LOPLPiDX/media/yp34SRmf/version/IFBsp7yL/manifest.ism/manifest-audio_eng=112000-video_eng=936240.m3u8

print('Final Page Length')
print(driver.execute_script("return document.body.scrollHeight"))
driver.quit()