import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.logger = driver.logger

    def open(self):
        self.logger.debug(f'--- Открытие страницы [{self.url}]')
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
            self.logger.debug(f'--- Локатор [{locator}] не найден')
            allure.attach(self.driver.get_screenshot_as_png(), name=f'{self.driver.session_id}.png', attachment_type=AttachmentType.PNG)
            raise AssertionError(f'Не найден элемент [{locator}]')

    def find_elements(
            self,
            locator,
            expected_condition=ec.visibility_of_all_elements_located,
            timeout=5
    ):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_condition(locator))
        except TimeoutException:
            self.logger.debug(f'--- Локатор [{locator}] не найден')
            allure.attach(self.driver.get_screenshot_as_png(), name=f'{self.driver.session_id}.png', attachment_type=AttachmentType.PNG)
            raise AssertionError(f'Не найдены элементы [{locator}]')

    def set_text(
            self,
            locator,
            text,
            click=True,
            clear=True,
            press_enter=False
    ):
        self.logger.debug(f'--- Ввод [{text}] в [{locator}]')

        element = self.find_element(locator, expected_condition=ec.element_to_be_clickable)

        if clear:
            element.clear()

        if click:
            element.click()

        element.send_keys(text)

        if press_enter:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()

    def click(self, locator, **kwargs):
        self.logger.debug(f'--- Нажатие на [{locator}]')

        element = self.find_element(locator, **kwargs)
        element.click()

    def accept_alert(self):
        self.logger.debug(f'--- Нажатие на allert')
        Alert(self.driver).accept()

    def current_url(self):
        return self.driver.current_url
