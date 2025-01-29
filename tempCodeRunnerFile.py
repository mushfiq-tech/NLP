price = driver.find_element(By.XPATH, '//*[@id="module_product_price_1"]/div/div/span').text
product_info['price'] = price