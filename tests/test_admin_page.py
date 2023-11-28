from src.admin_page.admin_page import AdminPage
from src.login_admin_page.login_admin_page import LoginAdminPage
from test_data.user_admin import UserAdmin
from test_data.product import Product


def test_add_product(browser, url):
    login_admin_page = LoginAdminPage(browser, f'{url}/admin')
    login_admin_page.open()
    login_admin_page.enter_name(UserAdmin.name)
    login_admin_page.enter_password(UserAdmin.password)
    login_admin_page.click_on_login_button()

    admin_page = AdminPage(browser, login_admin_page.current_url())
    admin_page.click_on_catalog_tab()
    admin_page.click_on_products_tab()
    admin_page.click_on_add_product()
    admin_page.enter_product_name(Product.name)
    admin_page.enter_meta_tag(Product.meta_tag)
    admin_page.click_on_data_tab()
    admin_page.enter_model(Product.model)
    admin_page.enter_price(Product.price)
    admin_page.click_on_save_button()
    admin_page.enter_product_name_filter(Product.name)
    admin_page.click_on_filter_button()
    admin_page.check_new_product_in_table(
        Product.name,
        Product.model,
        Product.price
    )


def test_delete_product(browser, url):
    login_admin_page = LoginAdminPage(browser, f'{url}/admin')
    login_admin_page.open()
    login_admin_page.enter_name(UserAdmin.name)
    login_admin_page.enter_password(UserAdmin.password)
    login_admin_page.click_on_login_button()

    admin_page = AdminPage(browser, login_admin_page.current_url())
    admin_page.click_on_catalog_tab()
    admin_page.click_on_products_tab()
    admin_page.enter_product_name_filter(Product.name)
    admin_page.click_on_filter_button()
    admin_page.select_new_product()
    admin_page.click_on_delete_button()
    admin_page.accept_alert()
