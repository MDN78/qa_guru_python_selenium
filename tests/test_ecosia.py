from seleyasha import helper
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import WebDriverException

from seleyasha.conditions import type, click, assert_that

helper.driver = webdriver.Chrome()
helper.wait = WebDriverWait(helper.driver, timeout=2, ignored_exceptions=(WebDriverException,))
helper.driver.get('https://www.ecosia.org/')
query = '[name=q]'

type(query, value='https://github.com/yashaka/selene/' + Keys.ENTER)

helper.driver.back()

type(query, value='pulls' + Keys.ENTER)

click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

assert_that('[id^=issue_]:not[id$=_link]', value=11)

helper.driver.quit()
