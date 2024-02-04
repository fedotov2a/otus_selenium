import allure

from src.common.base_page import BasePage
from src.product_card_page.product_card_page_locators import ProductCardPageLocators


class ProductCardPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step
    def check_elements(self):
        product_name_elem = self.find_element(ProductCardPageLocators.PRODUCT_NAME_LABEL)
        assert product_name_elem.text == 'HP LP3065'

        price_elem = self.find_element(ProductCardPageLocators.PRICE_LABEL)
        assert price_elem.text == '$122.00'

        self.find_element(ProductCardPageLocators.ADD_TO_WISH_LIST_BUTTON)
        self.find_element(ProductCardPageLocators.COMPARE_WITH_BUTTON)
        self.find_element(ProductCardPageLocators.ADD_TO_CART_BUTTON)
