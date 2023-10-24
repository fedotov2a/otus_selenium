import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as YaService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--maximize', action='store_true')
    parser.addoption('--headless', action='store_true')
    parser.addoption('--url', help='base app url')


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    maximize = request.config.getoption('--maximize')
    headless = request.config.getoption('--headless')

    if browser_name == 'chrome':
        chrome_options = ChromeOptions()

        if headless:
            chrome_options.add_argument('--headless=new')

        driver = webdriver.Chrome(options=chrome_options)  # ~/.cache/selenium
    elif browser_name == 'firefox':
        ff_options = FirefoxOptions()

        if headless:
            ff_options.add_argument('--headless')

        driver = webdriver.Firefox(options=ff_options)
    elif browser_name == 'yandex':
        chrome_options = ChromeOptions()

        if headless:
            chrome_options.add_argument('--headless=new')

        ya_service = YaService(str(Path('~/Projects/Otus/webdrivers/yandexdriver').expanduser()))
        driver = webdriver.Chrome(service=ya_service, options=chrome_options)
    else:
        raise ValueError(f'Браузер [{browser_name}] не поддерживается')

    if maximize:
        driver.maximize_window()

    yield driver
    driver.quit()
