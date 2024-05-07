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


def type_to_element(selector, value):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        # is_element_covered = driver.execute_script('element = arguments[0]; element.click; return is_element_covered', webelement) == 'true'
        # if is_element_cover:
        #     raise WebDriverException('covered element')
        webelement.send_keys(value)
        return webelement

    return command


def click_on_element(selector):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        webelement.click()
        return webelement

    return command


def number_of_elements(selector, value: int):
    def predicate(driver: WebDriver) -> bool:
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return predicate
