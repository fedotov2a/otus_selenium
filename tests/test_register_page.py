import allure

from src.register_page.register_page import RegisterPage
from test_data.user import User


@allure.feature('Страница регистрации пользователя')
@allure.title('Отображение элементов на странице регистрации пользователя')
def test_check_elements_on_register_page(browser, url):
    register_page = RegisterPage(browser, f'{url}/index.php?route=account/register')
    register_page.open()
    register_page.check_elements()


@allure.feature('Страница регистрации пользователя')
@allure.title('Регистрация пользователя')
def test_register_user(browser, url):
    register_page = RegisterPage(browser, f'{url}/index.php?route=account/register')
    register_page.open()

    register_page.enter_first_name(User.first_name)
    register_page.enter_last_name(User.last_name)
    register_page.enter_email(User.email)
    register_page.enter_phone_number(User.phone_number)
    register_page.enter_password(User.password)
    register_page.enter_confirm_password(User.confirm_password)
    register_page.select_privacy_policy_checkbox()
    register_page.click_on_continue_button()
    register_page.check_success_account_created()
