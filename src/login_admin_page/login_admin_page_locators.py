from selenium.webdriver.common.by import By


class AdminPageLocators:
    USERNAME_INPUT = (By.XPATH, '//input[@id = "input-username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id = "input-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type = "submit"]')
    FORGOTTEN_PASSWORD_BUTTON = (By.XPATH, '//a[text() = "Forgotten Password"]')
    TIP_LABEL = (By.XPATH, '//div[@class = "panel-heading"]')
