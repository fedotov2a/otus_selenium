from tests.common import assert_element
from src.register_page.register_page_locators import RegisterPageLocators


def test_check_elements_on_sign_up_page(browser, url):
    browser.get(f'{url}/index.php?route=account/register')

    assert_element(browser, RegisterPageLocators.PAGE_TITLE)
    assert_element(browser, RegisterPageLocators.FIRST_NAME_INPUT)
    assert_element(browser, RegisterPageLocators.LAST_NAME_INPUT)
    assert_element(browser, RegisterPageLocators.EMAIL_INPUT)
    assert_element(browser, RegisterPageLocators.PHONE_NUMBER_INPUT)
    assert_element(browser, RegisterPageLocators.PASSWORD_INPUT)
    assert_element(browser, RegisterPageLocators.CONFIRM_PASSWORD_INPUT)
    assert_element(browser, RegisterPageLocators.CONTINUE_BUTTON)
