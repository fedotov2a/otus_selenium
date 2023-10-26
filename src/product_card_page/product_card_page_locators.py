from selenium.webdriver.common.by import By


class ProductCardPageLocators:
    ADD_TO_WISH_LIST_BUTTON = (By.XPATH, '//button[@data-original-title = "Add to Wish List"]')
    COMPARE_WITH_BUTTON = (By.XPATH, '//button[@data-original-title = "Compare this Product"]')
    PRODUCT_NAME_LABEL = (By.XPATH, '//div[@class = "col-sm-4"]/h1')
    PRICE_LABEL = (By.XPATH, '//div[@class = "col-sm-4"]//h2')
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@id = "button-cart"]')
