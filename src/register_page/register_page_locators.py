from selenium.webdriver.common.by import By


class RegisterPageLocators:
    PAGE_TITLE = (By.XPATH, '//h1[text() = "Register Account"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id = "input-firstname"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id = "input-lastname"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id = "input-email"]')
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@id = "input-telephone"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id = "input-password"]')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//input[@id = "input-confirm"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@type = "submit"]')
