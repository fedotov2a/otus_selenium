from src.login_admin_page.login_admin_page import LoginAdminPage


def test_check_elements_on_login_admin_page(browser, url):
    login_admin_page = LoginAdminPage(browser, f'{url}/admin')
    login_admin_page.open()
    login_admin_page.check_elements()

