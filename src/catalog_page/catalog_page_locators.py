from selenium.webdriver.common.by import By


class CatalogPageLocators:
    BREADCRUMB_LIST = (By.XPATH, '//ul[@class = "breadcrumb"]')
    CATALOG_NAME = (By.XPATH, '//h2[text() = "Laptops & Notebooks"]')
    LIST_VIEW_BUTTON = (By.XPATH, '//div[contains(@class, "btn-group-sm")]/button[@id = "list-view"]')
    GRID_VIEW_BUTTON = (By.XPATH, '//div[contains(@class, "btn-group-sm")]/button[@id = "grid-view"]')
    SORT_SELECTBOX = (By.XPATH, '//select[@id = "input-sort"]')
    LIMIT_SELECTBOX = (By.XPATH, '//select[@id = "input-limit"]')

    PRODUCT_CARDS = (By.XPATH, '//div[contains(@class, "product-thumb")]')
    PRODUCT_NAME = (By.XPATH, './div/div[contains(@class, "caption")]//a')
    PRODUCT_PRICE = (By.XPATH, './div/div[contains(@class, "caption")]//p[@class = "price"]')
