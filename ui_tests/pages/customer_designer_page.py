import time
from test_data import data_filing_form_become_partner as d
import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.BaseClass import BaseClass
from pages.selectors import designer_loc as dl


class CustomerDesignerPage(BaseClass):
    page_url = 'designers'

    def check_title_designer_page(self, text):
        assert self.find_headers_title(text) == True, "Не правильный переход страницы или название!"

    def check_positive_form_become_partner(self,name, phone, city, email, comment, text):
        self.scroll_to_offset(700)
        self.find_visibility(dl.loc_button_become_partner).click()
        name_designer = self.find_presence_element(dl.loc_input_name)
        self.send(name_designer, name )
        telephone = self.find_presence_element(dl.loc_input_phone)
        self.send(telephone, phone)
        city_designer = self.find_presence_element(dl.loc_input_city)
        self.send(city_designer, city)
        email_designer = self.find_presence_element(dl.loc_input_email)
        self.send(email_designer, email)
        comment_text = self.find_presence_element(dl.loc_input_comment)
        self.send(comment_text, comment)
        agreement = self.find_presence_element(dl.loc_checkbox)
        agreement.click()
        self.find_visibility(dl.loc_button_send).click()
        success = self.find_visibility(dl.loc_successe)
        print(success.text)
        assert text in success.text

