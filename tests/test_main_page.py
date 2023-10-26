from tests.common import assert_element
from src.main_page.main_page_locators import MainPageLocators


def test_check_elements_on_main_page(browser, url):
    browser.get(url)

    account_button = assert_element(browser, MainPageLocators.ACCOUNT_BUTTON)
    account_button.click()

    assert_element(browser, MainPageLocators.LOGIN_BUTTON)
    account_button.click()

    assert_element(browser, MainPageLocators.WISH_LIST_BUTTON)
    assert_element(browser, MainPageLocators.SEARCH_INPUT)
    assert_element(browser, MainPageLocators.CART_BUTTON)
