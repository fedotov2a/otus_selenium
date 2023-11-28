from src.login_admin_page.login_admin_page import LoginAdminPage
from test_data.user_admin import UserAdmin


def test_check_elements_on_login_admin_page(browser, url):
    login_admin_page = LoginAdminPage(browser, f'{url}/admin')
    login_admin_page.open()
    login_admin_page.check_elements()


def test_login_admin(browser, url):
    login_admin_page = LoginAdminPage(browser, f'{url}/admin')
    login_admin_page.open()
    login_admin_page.enter_name(UserAdmin.name)
    login_admin_page.enter_password(UserAdmin.password)
    login_admin_page.click_on_login_button()
    login_admin_page.check_logged_in()
    login_admin_page.click_on_logout_button()
    login_admin_page.check_logout()
