from selenium.webdriver.common.by import By


class LoginAdminPageLocators:
    USERNAME_INPUT = (By.XPATH, '//input[@id = "input-username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id = "input-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type = "submit"]')
    FORGOTTEN_PASSWORD_BUTTON = (By.XPATH, '//a[text() = "Forgotten Password"]')
    TIP_LABEL = (By.XPATH, '//div[@class = "panel-heading"]')

    PROFILE_BUTTON = (By.XPATH, '//ul[contains(@class, "navbar-nav")]//a[@class = "dropdown-toggle"]')
    LOGOUT_BUTTON = (By.XPATH, '//a//span[text() = "Logout"]')
