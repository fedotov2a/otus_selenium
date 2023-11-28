from time import sleep
from src.main_page.main_page import MainPage
from src.common.menu_bar import MenuBar


def test_check_elements_on_main_page(browser, url):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.check_elements()


def test_add_product_to_cart(browser, url):
    main_page = MainPage(browser, url)
    main_page.open()
    product_name, product_price = main_page.add_random_product_to_cart()
    main_page.click_on_main_cart_button()
    main_page.check_product_in_cart(product_name, product_price)


def test_change_currency(browser, url):
    main_page = MainPage(browser, url)
    main_page.open()

    menu_bar = MenuBar(browser)
    menu_bar.click_on_currency_button()
    currency = menu_bar.click_on_currency_option()

    sleep(1)
    main_page.check_currency(currency)

