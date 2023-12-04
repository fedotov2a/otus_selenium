from src.product_card_page.product_card_page import ProductCardPage


def test_check_elements_on_product_card_page(browser, url):
    product_card_page = ProductCardPage(browser, f'{url}/laptop-notebook/hp-lp3065')
    product_card_page.open()
    product_card_page.check_elements()
