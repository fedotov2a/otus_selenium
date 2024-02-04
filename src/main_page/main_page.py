import random
import allure

from src.common.base_page import BasePage
from src.main_page.main_page_locators import MainPageLocators
from src.common.common_locators import MenuBarLocators


class MainPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step
    def check_elements(self):
        account_button = self.find_element(MenuBarLocators.ACCOUNT_BUTTON)
        account_button.click()

        self.find_element(MenuBarLocators.LOGIN_BUTTON)
        account_button.click()

        self.find_element(MenuBarLocators.WISH_LIST_BUTTON)
        self.find_element(MainPageLocators.SEARCH_INPUT)
        self.find_element(MainPageLocators.CART_BUTTON)

    @allure.step
    def click_on_main_cart_button(self):
        self.click(MainPageLocators.MAIN_CART_BUTTON)

    @allure.step
    def add_random_product_to_cart(self):
        product_cards = self.find_elements(MainPageLocators.PRODUCT_CARD)
        product_card = random.choice(product_cards)
        product_name = product_card.find_element(*MainPageLocators.PRODUCT_NAME).text
        product_price = product_card.find_element(*MainPageLocators.PRODUCT_PRICE).text.split('\n')[0]
        add_to_cart_button = product_card.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

        return product_name, product_price

    @allure.step
    def check_product_in_cart(self, product_name, product_price):
        product_name_in_cart = self.find_element(MainPageLocators.PRODUCT_NAME_IN_MAIN_CART).text
        product_price_in_cart = self.find_element(MainPageLocators.PRODUCT_PRICE_IN_MAIN_CART).text

        assert product_name_in_cart == product_name
        assert product_price_in_cart == product_price

    @allure.step
    def check_currency(self, currency):
        product_cards = self.find_elements(MainPageLocators.PRODUCT_CARD)

        for product_card in product_cards:
            product_price = product_card.find_element(*MainPageLocators.PRODUCT_PRICE).text
            assert currency in product_price
