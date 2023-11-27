from src.main_page.main_page import MainPage


def test_check_elements_on_main_page(browser, url):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.check_elements()
