from src.common.base_page import BasePage
from src.main_page.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def check_elements(self):
        account_button = self.find_element(MainPageLocators.ACCOUNT_BUTTON)
        account_button.click()

        self.find_element(MainPageLocators.LOGIN_BUTTON)
        account_button.click()

        self.find_element(MainPageLocators.WISH_LIST_BUTTON)
        self.find_element(MainPageLocators.SEARCH_INPUT)
        self.find_element(MainPageLocators.CART_BUTTON)
