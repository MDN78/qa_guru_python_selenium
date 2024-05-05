from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2)
driver.get('https://www.google.com/ncr')
# driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene')
# driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys(Keys.ENTER)
# тождественно:
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene', Keys.ENTER)
wait.until()


time.sleep(3)