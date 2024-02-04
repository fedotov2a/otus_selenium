import random
import allure

from src.common.base_page import BasePage
from src.common.common_locators import MenuBarLocators


class MenuBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver, None)

    @allure.step
    def click_on_currency_button(self):
        self.click(MenuBarLocators.CURRENCY_BUTTON)

    @allure.step
    def click_on_currency_option(self, currency_name=None):
        currency_options = self.find_elements(MenuBarLocators.CURRENCY_OPTION_LIST)

        if currency_name is None:
            currency_option = random.choice(currency_options)
        else:
            currency_option = next(filter(lambda name: name in currency_option.text, currency_options))

        currency = currency_option.text.split()[0]
        currency_option.click()

        return currency
