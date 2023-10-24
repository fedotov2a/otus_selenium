from tests.common import assert_element
from src.catalog_page.catalog_page_locators import CatalogPageLocators


def test_check_elements_on_laptop_notebook_page(browser, url):
    browser.get(f'{url}/laptop-notebook')

    assert_element(browser, CatalogPageLocators.BREADCRUMB_LIST)
    assert_element(browser, CatalogPageLocators.CATALOG_NAME)
    assert_element(browser, CatalogPageLocators.LIST_VIEW_BUTTON)
    assert_element(browser, CatalogPageLocators.GRID_VIEW_BUTTON)
    assert_element(browser, CatalogPageLocators.SORT_SELECTBOX)
    assert_element(browser, CatalogPageLocators.LIMIT_SELECTBOX)
