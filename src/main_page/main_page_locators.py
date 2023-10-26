from selenium.webdriver.common.by import By


class MainPageLocators:
    CURRENCY_BUTTON = (By.XPATH, '//nav[@id = "top"]//div[contains(@class, "btn-group")]/button')
    PHONE_LABEL = (By.XPATH, '//nav[@id = "top"]//div[@id = "top-links"]//i[contains(@class, "fa-phone")]/../../span')
    ACCOUNT_BUTTON = (By.XPATH, '//a[@title = "My Account"]')
    REGISTER_BUTTON = (By.XPATH, '//ul[contains(@class, "dropdown-menu")]//a[text() = "Register"]')
    LOGIN_BUTTON = (By.XPATH, '//ul[contains(@class, "dropdown-menu")]//a[text() = "Login"]')
    WISH_LIST_BUTTON = (By.XPATH, '//a[@id = "wishlist-total"]')
    SHOPPING_CART_BUTTON = (By.XPATH, '//a[@title = "Shopping Cart"]')
    CHECKOUT_BUTTON = (By.XPATH, '//a[@title = "Checkout"]')

    MAIN_LOGO_IMG = (By.XPATH, '//header//img[@title = "Your Store"]')
    SEARCH_INPUT = (By.XPATH, '//header//div[@id = "search"]//input[@name = "search"]')
    SEARCH_BUTTON = (By.XPATH, '//header//div[@id = "search"]//button[contains(@class, "btn")]')
    CART_BUTTON = (By.XPATH, '//header//div[@id = "cart"]//button[contains(@class, "btn")]')
