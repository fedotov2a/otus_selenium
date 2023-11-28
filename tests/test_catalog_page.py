from time import sleep

from src.catalog_page.catalog_page import CatalogPage
from src.common.menu_bar import MenuBar


def test_check_elements_on_laptop_notebook_page(browser, url):
    catalog_page = CatalogPage(browser, f'{url}/laptop-notebook')
    catalog_page.open()
    catalog_page.check_elements()


def test_change_currency(browser, url):
    catalog_page = CatalogPage(browser, f'{url}/laptop-notebook')
    catalog_page.open()

    menu_bar = MenuBar(browser)
    menu_bar.click_on_currency_button()
    currency = menu_bar.click_on_currency_option()

    sleep(1)
    catalog_page.check_currency(currency)
