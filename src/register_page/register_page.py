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

    def enter_first_name(self, first_name):
        self.set_text(RegisterPageLocators.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.set_text(RegisterPageLocators.LAST_NAME_INPUT, last_name)

    def enter_email(self, email):
        self.set_text(RegisterPageLocators.EMAIL_INPUT, email)

    def enter_phone_number(self, phone_number):
        self.set_text(RegisterPageLocators.PHONE_NUMBER_INPUT, phone_number)

    def enter_password(self, password):
        self.set_text(RegisterPageLocators.PASSWORD_INPUT, password)

    def enter_confirm_password(self, confirm_password):
        self.set_text(RegisterPageLocators.CONFIRM_PASSWORD_INPUT, confirm_password)

    def select_privacy_policy_checkbox(self):
        self.click(RegisterPageLocators.PRIVACY_POLICY_CHECKBOX)

    def click_on_continue_button(self):
        self.click(RegisterPageLocators.CONTINUE_BUTTON)

    def check_success_account_created(self):
        label = self.find_element(RegisterPageLocators.SUCCESS_ACCOUNT_CREATED_LABEL)
        assert 'Your Account Has Been Created!' == label.text
