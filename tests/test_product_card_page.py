from tests.common import assert_element
from src.product_card_page.product_card_page_locators import ProductCardPageLocators


def test_check_elements_on_product_card_page(browser, url):
    browser.get(f'{url}/laptop-notebook/hp-lp3065')

    product_name_elem = assert_element(browser, ProductCardPageLocators.PRODUCT_NAME_LABEL)
    assert product_name_elem.text == 'HP LP3065'

    price_elem = assert_element(browser, ProductCardPageLocators.PRICE_LABEL)
    assert price_elem.text == '$122.00'

    assert_element(browser, ProductCardPageLocators.ADD_TO_WISH_LIST_BUTTON)
    assert_element(browser, ProductCardPageLocators.COMPARE_WITH_BUTTON)
    assert_element(browser, ProductCardPageLocators.ADD_TO_CART_BUTTON)
