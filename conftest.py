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
    parser.addoption('--executor')  # default='192.168.0.105'


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    maximize = request.config.getoption('--maximize')
    headless = request.config.getoption('--headless')
    executor = request.config.getoption('--executor')

    driver = None
    options = None

    if browser_name == 'chrome':
        options = ChromeOptions()

        if headless:
            options.add_argument('--headless=new')

        if executor is None:
            driver = webdriver.Chrome(options=options)  # ~/.cache/selenium
    elif browser_name == 'yandex':
        options = ChromeOptions()

        if headless:
            options.add_argument('--headless=new')

        if executor is None:
            ya_service = YaService(str(Path('~/Projects/Otus/webdrivers/yandexdriver').expanduser()))
            driver = webdriver.Chrome(service=ya_service, options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()

        if headless:
            options.add_argument('--headless')

        if executor is None:
            driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f'Браузер [{browser_name}] не поддерживается')

    if executor is not None:
        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            options=options
        )

    if maximize:
        driver.maximize_window()

    yield driver
    driver.quit()
