from test_data import data_for_living_form_to_catalog as data
from test_data import data_for_filing_order_form as order


def test_url_catalog_page(catalog_page):
    catalog_page.open_page()
    catalog_page.check_catalog_page("catalog")


def test_all_products_page(catalog_page):
    catalog_page.open_page()
    catalog_page.check_all_products_to_page(36)


def test_button_leave_request(catalog_page):
    catalog_page.open_page()
    catalog_page.check_button_leave_request('Оставьте заявку')

def test_form_leave_request(catalog_page):
    catalog_page.open_page()
    catalog_page.check_form_to_leave_request(data.full_name, data.phone, data.desc, data.link_address_to_sofa)

def test_order_form(catalog_page):
    catalog_page.open_page()
    catalog_page.link_to_soft()

def test_filing_form_order(catalog_page):
    catalog_page.open_page()
    catalog_page.check_form_to_order_soft(
        order.title_soft, order.quantity_soft, order.name, order.phone, order.desc, order.success)
