import pytest
from test_data import data_filing_form_become_partner as d


def test_title_designer_page(designer_page):
    designer_page.open_page()
    designer_page.check_title_designer_page('Дизайнерам')


def test_positive_form_become_partner(designer_page):
    designer_page.open_page()
    designer_page.check_positive_form_become_partner(d.name, d.phone, d.city, d.email, d.comment, 'Отлично')