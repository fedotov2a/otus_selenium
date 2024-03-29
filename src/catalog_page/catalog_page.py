from src.common.base_page import BasePage
from src.catalog_page.catalog_page_locators import CatalogPageLocators


class CatalogPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def check_elements(self):
        self.find_element(CatalogPageLocators.BREADCRUMB_LIST)
        self.find_element(CatalogPageLocators.CATALOG_NAME)
        self.find_element(CatalogPageLocators.LIST_VIEW_BUTTON)
        self.find_element(CatalogPageLocators.GRID_VIEW_BUTTON)
        self.find_element(CatalogPageLocators.SORT_SELECTBOX)
        self.find_element(CatalogPageLocators.LIMIT_SELECTBOX)

    def check_currency(self, currency):
        product_cards = self.find_elements(CatalogPageLocators.PRODUCT_CARDS)

        for product_card in product_cards:
            product_price = product_card.find_element(*CatalogPageLocators.PRODUCT_PRICE).text
            assert currency in product_price
