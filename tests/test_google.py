from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import WebDriverException
import time

# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, timeout=2)
# driver.get('https://www.google.com/ncr')
# driver.implicitly_wait(2)  # example  - variant of waiting
# driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene')
# driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys(Keys.ENTER)
# тождественно:
#driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene', Keys.ENTER)
#
# def find_element(driver):
#     return driver.find_element(By.CSS_SELECTOR, '[name=q]')
#
# wait.until(find_element).send_keys('selene', Keys.ENTER)

# on one line code and use lambda:
# wait.until(
#     lambda driver: driver.find_element(By.CSS_SELECTOR, '[name=q]')
# ).send_keys('selene', Keys.ENTER)

# EC.visibility_of_element_located()



driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException))
driver.get('https://www.ecosia.org/')


# wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, '[name=q]')).send_keys('selene yashaka', Keys.ENTER)

def element(by, selector):
    def find_element(driver):
        return driver.find_element(by, selector)
    return find_element

# the same variant
# def element(by, selector):
#     def find_element(driver):
#         return EC._element_if_visible(driver.find_element(by, selector))
#     return find_element

'''чтобы например по умолчанию искать только по селектору
def element(selector):
    selector_type = By.XPATH if (
        selector.startswith('/')
        or selector.startswith('//')
        or selector.startswith('./')
        or selector.startswith('(')
        or selector.startswith('..')
    ) else By.CSS_SELECTOR
    def find_element(driver):
        return driver.find_element(selector_type, selector)
    return find_element

wait.until(element('[name=q]')).send_keys('selene yashaka', Keys.ENTER)'''



wait.until(element(By.CSS_SELECTOR, '[name=q]')).send_keys('selene yashaka', Keys.ENTER)
wait.until(element(By.CSS_SELECTOR, '[data-test-id=mainline-result-web]:nth-of-type(1) a')).click()

time.sleep(3)

