import pytest
import allure
import logging

from datetime import datetime
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
    parser.addoption('--executor')
    parser.addoption("--log_level", default="INFO")


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    item.status = 'passed' if rep.outcome == 'passed' else 'failed'


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    maximize = request.config.getoption('--maximize')
    headless = request.config.getoption('--headless')
    executor = request.config.getoption('--executor')
    log_level = request.config.getoption('--log_level')

    driver = None
    options = None

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'logs/{request.node.name}.log')
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info(f'--- Тест [{request.node.name}] запущен [{datetime.now()}]')

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

    caps = {
        "browserName": browser_name
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    if executor is not None:
        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            options=options
        )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info(f'--- Браузер [{browser_name}] запущен')

    if maximize:
        driver.maximize_window()

    yield driver

    if request.node.status == "failed":
        allure.attach(
            driver.get_screenshot_as_png(),
            name='failure_screenshot.png',
            attachment_type=allure.attachment_type.PNG
        )

    logger.info(f'--- Тест [{request.node.name}] завершился [{datetime.now()}]')
    driver.quit()
