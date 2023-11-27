from src.common.base_page import BasePage
from src.register_page.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def check_elements(self):
        self.find_element(RegisterPageLocators.PAGE_TITLE)
        self.find_element(RegisterPageLocators.FIRST_NAME_INPUT)
        self.find_element(RegisterPageLocators.LAST_NAME_INPUT)
        self.find_element(RegisterPageLocators.EMAIL_INPUT)
        self.find_element(RegisterPageLocators.PHONE_NUMBER_INPUT)
        self.find_element(RegisterPageLocators.PASSWORD_INPUT)
        self.find_element(RegisterPageLocators.CONFIRM_PASSWORD_INPUT)
        self.find_element(RegisterPageLocators.CONTINUE_BUTTON)
