from src.common.base_page import BasePage
from src.admin_page.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def click_on_catalog_tab(self):
        self.click(AdminPageLocators.CATALOG_TAB)

    def click_on_products_tab(self):
        self.click(AdminPageLocators.PRODUCTS_TAB)

    def click_on_add_product(self):
        self.click(AdminPageLocators.ADD_PRODUCT_BUTTON)

    def enter_product_name(self, product_name):
        self.set_text(AdminPageLocators.PRODUCT_NAME_INPUT, product_name)

    def enter_meta_tag(self, meta_tag):
        self.set_text(AdminPageLocators.META_TAG_INPUT, meta_tag)

    def click_on_data_tab(self):
        self.click(AdminPageLocators.DATA_TAB)

    def enter_model(self, model):
        self.set_text(AdminPageLocators.MODEL_INPUT, model)

    def enter_price(self, price):
        self.set_text(AdminPageLocators.PRICE_INPUT, price)

    def click_on_save_button(self):
        self.click(AdminPageLocators.SAVE_BUTTON)

    def check_new_product_in_table(
            self,
            product_name,
            product_model,
            price
    ):
        new_product = self.find_element(AdminPageLocators.NEW_PRODUCT)

        new_product_name = new_product.find_element(*AdminPageLocators.PRODUCT_NAME).text
        assert product_name == new_product_name

        new_product_model = new_product.find_element(*AdminPageLocators.PRODUCT_MODEL).text
        assert product_model == new_product_model

        new_product_price = new_product.find_element(*AdminPageLocators.PRODUCT_PRICE).text
        assert price in new_product_price

    def select_new_product(self):
        new_product = self.find_element(AdminPageLocators.NEW_PRODUCT)
        new_product.find_element(*AdminPageLocators.PRODUCT_CHECKBOX).click()

    def click_on_delete_button(self):
        self.click(AdminPageLocators.DELETE_PRODUCT_BUTTON)

    def enter_product_name_filter(self, product_name):
        self.set_text(AdminPageLocators.PRODUCT_NAME_FILTER_INPUT, product_name)

    def click_on_filter_button(self):
        self.click(AdminPageLocators.FILTER_BUTTON)
