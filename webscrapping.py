from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)


driver.get('https://www.daraz.com.bd/routers/')  


time.sleep(10)  
element = driver.find_element(By.CSS_SELECTOR, '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(1) > div > div > div.buTCk > div.RfADt > a')  

print(element.text)
driver.quit()

