from src.catalog_page.catalog_page import CatalogPage


def test_check_elements_on_laptop_notebook_page(browser, url):
    catalog_page = CatalogPage(browser, f'{url}/laptop-notebook')
    catalog_page.open()
    catalog_page.check_elements()
