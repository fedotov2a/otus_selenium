from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_LOGO_IMG = (By.XPATH, '//header//img[@title = "Your Store"]')
    SEARCH_INPUT = (By.XPATH, '//header//div[@id = "search"]//input[@name = "search"]')
    SEARCH_BUTTON = (By.XPATH, '//header//div[@id = "search"]//button[contains(@class, "btn")]')
    CART_BUTTON = (By.XPATH, '//header//div[@id = "cart"]//button[contains(@class, "btn")]')

    PRODUCT_CARD = (By.XPATH, '//div[contains(@class, "product-thumb")]')
    ADD_TO_CART_BUTTON = (By.XPATH, './div[contains(@class, "button-group")]/button//span[text() = "Add to Cart"]')
    PRODUCT_NAME = (By.XPATH, './div[contains(@class, "caption")]//a')
    PRODUCT_PRICE = (By.XPATH, './div[contains(@class, "caption")]//p[@class = "price"]')

    MAIN_CART_BUTTON = (By.XPATH, '//div[@id = "cart"]/button')
    PRODUCT_NAME_IN_MAIN_CART = (By.XPATH, '//div[@id = "cart"]//li[1]/table//td[2]/a')
    PRODUCT_PRICE_IN_MAIN_CART = (By.XPATH, '//div[@id = "cart"]//li[1]/table//td[4]')
