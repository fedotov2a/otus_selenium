from src.common.base_page import BasePage
from src.login_admin_page.login_admin_page_locators import LoginAdminPageLocators


class LoginAdminPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def check_elements(self):
        self.find_element(LoginAdminPageLocators.TIP_LABEL)
        self.find_element(LoginAdminPageLocators.USERNAME_INPUT)
        self.find_element(LoginAdminPageLocators.PASSWORD_INPUT)
        self.find_element(LoginAdminPageLocators.FORGOTTEN_PASSWORD_BUTTON)
        self.find_element(LoginAdminPageLocators.LOGIN_BUTTON)

    def enter_name(self, text):
        self.set_text(LoginAdminPageLocators.USERNAME_INPUT, text)

    def enter_password(self, text):
        self.set_text(LoginAdminPageLocators.PASSWORD_INPUT, text)

    def click_on_login_button(self):
        self.click(LoginAdminPageLocators.LOGIN_BUTTON)

    def click_on_logout_button(self):
        self.click(LoginAdminPageLocators.LOGOUT_BUTTON)

    def check_logged_in(self):
        element = self.find_element(LoginAdminPageLocators.PROFILE_BUTTON)
        assert 'John Doe' == element.text

    def check_logout(self):
        self.check_elements()
