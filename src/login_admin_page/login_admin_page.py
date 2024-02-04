import allure

from src.common.base_page import BasePage
from src.login_admin_page.login_admin_page_locators import LoginAdminPageLocators


class LoginAdminPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step
    def check_elements(self):
        self.logger.info(f'--- Проверка отображения элементов')

        self.find_element(LoginAdminPageLocators.TIP_LABEL)
        self.find_element(LoginAdminPageLocators.USERNAME_INPUT)
        self.find_element(LoginAdminPageLocators.PASSWORD_INPUT)
        self.find_element(LoginAdminPageLocators.FORGOTTEN_PASSWORD_BUTTON)
        self.find_element(LoginAdminPageLocators.LOGIN_BUTTON)

    @allure.step
    def enter_name(self, text):
        self.logger.info(f'--- Ввод username [{text}]')

        self.set_text(LoginAdminPageLocators.USERNAME_INPUT, text)

    @allure.step
    def enter_password(self, text):
        self.logger.info(f'--- Ввод пароля [{text}]')

        self.set_text(LoginAdminPageLocators.PASSWORD_INPUT, text)

    @allure.step
    def click_on_login_button(self):
        self.logger.info(f'--- Нажатие на кнопку логина')

        self.click(LoginAdminPageLocators.LOGIN_BUTTON)

    @allure.step
    def click_on_logout_button(self):
        self.logger.info(f'--- Нажатие на кнопку разлогина')

        self.click(LoginAdminPageLocators.LOGOUT_BUTTON)

    @allure.step
    def check_logged_in(self):
        self.logger.info(f'--- Проверка профиля')

        element = self.find_element(LoginAdminPageLocators.PROFILE_BUTTON)
        assert 'John Doe' == element.text

    @allure.step
    def check_logout(self):
        self.logger.info(f'--- Проверка разлогина')

        self.check_elements()
