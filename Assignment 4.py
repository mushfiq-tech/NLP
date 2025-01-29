from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.daraz.com.bd/products/4g-wifi-i468701703-s2256167219.html')





product_info = {}

product_name = driver.find_element(By.XPATH, '//*[@id="module_product_title_1"]/div/div/h1').text
product_info['product_name'] = product_name



price = driver.find_element(By.XPATH, '//*[@id="module_product_price_1"]/div/div/span').text
product_info['price'] = price


product_details = driver.find_element(By.CSS_SELECTOR, '#module_product_detail > div > div > div.pdp-product-desc.height-limit > div.html-content.pdp-product-highlights > ul > li').text
product_info['product_details'] = product_details



print(product_info)

driver.quit()