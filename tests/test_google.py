from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/ncr')
# driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene')
# driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys(Keys.ENTER)
# тождественно:
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene', Keys.ENTER)



time.sleep(3)