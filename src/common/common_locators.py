from selenium.webdriver.common.by import By


class MenuBarLocators:
    CURRENCY_BUTTON = (By.XPATH, '//nav[@id = "top"]//div[contains(@class, "btn-group")]/button')
    CURRENCY_OPTION_LIST = (By.XPATH, '//button[contains(@class, "currency-select")]')
    PHONE_LABEL = (By.XPATH, '//nav[@id = "top"]//div[@id = "top-links"]//i[contains(@class, "fa-phone")]/../../span')
    ACCOUNT_BUTTON = (By.XPATH, '//a[@title = "My Account"]')
    REGISTER_BUTTON = (By.XPATH, '//ul[contains(@class, "dropdown-menu")]//a[text() = "Register"]')
    LOGIN_BUTTON = (By.XPATH, '//ul[contains(@class, "dropdown-menu")]//a[text() = "Login"]')
    WISH_LIST_BUTTON = (By.XPATH, '//a[@id = "wishlist-total"]')
    SHOPPING_CART_BUTTON = (By.XPATH, '//a[@title = "Shopping Cart"]')
    CHECKOUT_BUTTON = (By.XPATH, '//a[@title = "Checkout"]')
