from tests.common import assert_element
from src.login_admin_page.login_admin_page_locators import AdminPageLocators


def test_check_elements_on_login_admin_page(browser, url):
    browser.get(f'{url}/admin')

    assert_element(browser, AdminPageLocators.TIP_LABEL)
    assert_element(browser, AdminPageLocators.USERNAME_INPUT)
    assert_element(browser, AdminPageLocators.PASSWORD_INPUT)
    assert_element(browser, AdminPageLocators.FORGOTTEN_PASSWORD_BUTTON)
    assert_element(browser, AdminPageLocators.LOGIN_BUTTON)
