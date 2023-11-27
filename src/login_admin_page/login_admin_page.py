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
