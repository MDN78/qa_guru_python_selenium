from seleyasha import helper
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def to_locator(selector: str) -> tuple[str, str]:
    return (By.XPATH, selector) if (
            selector.startswith('/')
            or selector.startswith('//')
            or selector.startswith('./')
            or selector.startswith('(')
            or selector.startswith('..')
    ) else (By.CSS_SELECTOR, selector)


def type(selector, value):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        webelement.send_keys(value)
        return webelement

    return helper.wait.until(command)


def click(selector):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        webelement.click()
        return webelement

    return helper.wait.until(command)


def assert_that(selector, value: int):
    def predicate(driver: WebDriver) -> bool:
        webelements = driver.find_elements(*to_locator(selector))
        actual_value = len(webelements)
        if actual_value != value:
            raise AssertionError(f'number of elements is not {value}\nactual value: {actual_value}')
        return webelements

    return predicate
