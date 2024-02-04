import allure

from src.common.base_page import BasePage
from src.register_page.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step
    def check_elements(self):
        self.logger.info(f'--- Проверка отображения эолементов на странице')

        self.find_element(RegisterPageLocators.PAGE_TITLE)
        self.find_element(RegisterPageLocators.FIRST_NAME_INPUT)
        self.find_element(RegisterPageLocators.LAST_NAME_INPUT)
        self.find_element(RegisterPageLocators.EMAIL_INPUT)
        self.find_element(RegisterPageLocators.PHONE_NUMBER_INPUT)
        self.find_element(RegisterPageLocators.PASSWORD_INPUT)
        self.find_element(RegisterPageLocators.CONFIRM_PASSWORD_INPUT)
        self.find_element(RegisterPageLocators.CONTINUE_BUTTON)

    @allure.step
    def enter_first_name(self, first_name):
        self.logger.info(f'--- Ввод имени [{first_name}]')

        self.set_text(RegisterPageLocators.FIRST_NAME_INPUT, first_name)

    @allure.step
    def enter_last_name(self, last_name):
        self.logger.info(f'--- Ввод фамилии [{last_name}]')

        self.set_text(RegisterPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step
    def enter_email(self, email):
        self.logger.info(f'--- Ввод email [{email}]')

        self.set_text(RegisterPageLocators.EMAIL_INPUT, email)

    @allure.step
    def enter_phone_number(self, phone_number):
        self.logger.info(f'--- Ввод номера телефона [{phone_number}]')

        self.set_text(RegisterPageLocators.PHONE_NUMBER_INPUT, phone_number)

    @allure.step
    def enter_password(self, password):
        self.logger.info(f'--- Ввод пароля [{password}]')

        self.set_text(RegisterPageLocators.PASSWORD_INPUT, password)

    @allure.step
    def enter_confirm_password(self, confirm_password):
        self.logger.info(f'--- Ввод пароля для подтверждения [{confirm_password}]')

        self.set_text(RegisterPageLocators.CONFIRM_PASSWORD_INPUT, confirm_password)

    @allure.step
    def select_privacy_policy_checkbox(self):
        self.logger.info(f'--- Нажатие на чекбокс Privacy Policy')

        self.click(RegisterPageLocators.PRIVACY_POLICY_CHECKBOX)

    @allure.step
    def click_on_continue_button(self):
        self.logger.info(f'--- Нажатие на кнопку продолжения регистрации')
        self.click(RegisterPageLocators.CONTINUE_BUTTON)

    @allure.step
    def check_success_account_created(self):
        self.logger.info(f'--- Проверка создания аккаунта')

        label = self.find_element(RegisterPageLocators.SUCCESS_ACCOUNT_CREATED_LABEL)
        assert 'Your Account Has Been Created!' == label.text
