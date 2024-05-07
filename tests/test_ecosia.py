from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import WebDriverException
import time

from seleyasha.conditions import type_to_element, click_on_element, number_of_elements

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException))
driver.get('https://www.ecosia.org/')
query = '[name=q]'

# wait.until(type_to_element('[name=q]', value='selene yashaka' + Keys.ENTER))
#
# wait.until(click_on_element('[data-test-id=mainline-result-web]:nth-of-type(1) a'))


# insert wait.until to type_to_element
wait.until(type_to_element(query, value='https://github.com/yashaka/selene/' + Keys.ENTER))
driver.back()
wait.until(type_to_element(query, value='pulls' + Keys.ENTER))

# insert wait.until(...) to click_on_element
wait.until(click_on_element('[data-test-id=mainline-result-web]:nth-of-type(1) a'))


# assert_that(...)
wait.until(number_of_elements('[id^=issue_]:not[id$=_link]', value=11))


# numbers_of_pulls = len(driver.find_element(By.CSS_SELECTOR, '[id^=issue_]:not[id$=_link]'))
# assert numbers_of_pulls == 11

time.sleep(2)