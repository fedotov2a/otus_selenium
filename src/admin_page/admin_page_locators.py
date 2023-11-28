from selenium.webdriver.common.by import By


class AdminPageLocators:
    CATALOG_TAB = (By.XPATH, '//li[@id = "menu-catalog"]/a')
    PRODUCTS_TAB = (By.XPATH, '//li[@id = "menu-catalog"]//a[text() = "Products"]')
    ADD_PRODUCT_BUTTON = (By.XPATH, '//a[@data-original-title = "Add New"]')
    DELETE_PRODUCT_BUTTON = (By.XPATH, '//button[@data-original-title = "Delete"]')
    PRODUCT_NAME_INPUT = (By.XPATH, '//input[@id  = "input-name1"]')
    META_TAG_INPUT = (By.XPATH, '//input[@id  = "input-meta-title1"]')
    DATA_TAB = (By.XPATH, '//a[@data-toggle = "tab"][text() = "Data"]')
    MODEL_INPUT = (By.XPATH, '//input[@id = "input-model"]')
    PRICE_INPUT = (By.XPATH, '//input[@id = "input-price"]')
    SAVE_BUTTON = (By.XPATH, '//button[@data-original-title = "Save"]')
    PRODUCT_NAME_FILTER_INPUT = (By.XPATH, '//input[@id = "input-name"]')
    FILTER_BUTTON = (By.XPATH, '//button[@id = "button-filter"]')

    PRODUCT_LIST = (By.XPATH, '//table')
    NEW_PRODUCT = (By.XPATH, '//table/tbody/tr[1]')
    PRODUCT_CHECKBOX = (By.XPATH, './td[1]/input')
    PRODUCT_NAME = (By.XPATH, './td[3]')
    PRODUCT_MODEL = (By.XPATH, './td[4]')
    PRODUCT_PRICE = (By.XPATH, './td[5]')
