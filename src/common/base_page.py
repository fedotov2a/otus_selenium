from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(
            self,
            locator,
            expected_condition=ec.visibility_of_element_located,
            timeout=5
    ):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_condition(locator))
        except TimeoutException:
            self.driver.save_screenshot(f'{self.driver.session_id}.png')
            raise AssertionError(f'Не найден элемент [{locator}]')
