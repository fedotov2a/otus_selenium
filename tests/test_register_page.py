from src.register_page.register_page import RegisterPage


def test_check_elements_on_register_page(browser, url):
    register_page = RegisterPage(browser, f'{url}/index.php?route=account/register')
    register_page.open()
    register_page.check_elements()
