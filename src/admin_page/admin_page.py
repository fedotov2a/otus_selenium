import allure

from src.common.base_page import BasePage
from src.admin_page.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step
    def click_on_catalog_tab(self):
        self.logger.info(f'--- Нажатие на таб каталога')
        self.click(AdminPageLocators.CATALOG_TAB)

    @allure.step
    def click_on_products_tab(self):
        self.logger.info(f'--- Нажатие на таб товаров')
        self.click(AdminPageLocators.PRODUCTS_TAB)

    @allure.step
    def click_on_add_product(self):
        self.logger.info(f'--- Добавление товара')
        self.click(AdminPageLocators.ADD_PRODUCT_BUTTON)

    @allure.step
    def enter_product_name(self, product_name):
        self.logger.info(f'--- Ввод названия товара [{product_name}]')
        self.set_text(AdminPageLocators.PRODUCT_NAME_INPUT, product_name)

    @allure.step
    def enter_meta_tag(self, meta_tag):
        self.logger.info(f'--- Ввод мета-тега [{meta_tag}]')
        self.set_text(AdminPageLocators.META_TAG_INPUT, meta_tag)

    @allure.step
    def click_on_data_tab(self):
        self.logger.info(f'--- Нажатие на таб данных')
        self.click(AdminPageLocators.DATA_TAB)

    @allure.step
    def enter_model(self, model):
        self.logger.info(f'--- Ввод названия модели [{model}]')
        self.set_text(AdminPageLocators.MODEL_INPUT, model)

    @allure.step
    def enter_price(self, price):
        self.logger.info(f'--- Ввод цены [{price}]')
        self.set_text(AdminPageLocators.PRICE_INPUT, price)

    @allure.step
    def click_on_save_button(self):
        self.logger.info(f'--- Нажатие на кнопку сохранения')
        self.click(AdminPageLocators.SAVE_BUTTON)

    @allure.step
    def check_new_product_in_table(
            self,
            product_name,
            product_model,
            price
    ):
        self.logger.info(f'--- Проверка нахождения нового товара в таблице')

        new_product = self.find_element(AdminPageLocators.NEW_PRODUCT)

        new_product_name = new_product.find_element(*AdminPageLocators.PRODUCT_NAME).text
        assert product_name == new_product_name

        new_product_model = new_product.find_element(*AdminPageLocators.PRODUCT_MODEL).text
        assert product_model == new_product_model

        new_product_price = new_product.find_element(*AdminPageLocators.PRODUCT_PRICE).text
        assert price in new_product_price

    @allure.step
    def select_new_product(self):
        self.logger.info(f'--- Выбор нового товара')

        new_product = self.find_element(AdminPageLocators.NEW_PRODUCT)
        new_product.find_element(*AdminPageLocators.PRODUCT_CHECKBOX).click()

    @allure.step
    def click_on_delete_button(self):
        self.logger.info(f'--- Нажатие на кнопку удаления товара')

        self.click(AdminPageLocators.DELETE_PRODUCT_BUTTON)

    @allure.step
    def enter_product_name_filter(self, product_name):
        self.logger.info(f'--- Ввод названия продукта [{product_name}]')

        self.set_text(AdminPageLocators.PRODUCT_NAME_FILTER_INPUT, product_name)

    @allure.step
    def click_on_filter_button(self):
        self.logger.info(f'--- Нажатие на кнопку фильтрации')

        self.click(AdminPageLocators.FILTER_BUTTON)
