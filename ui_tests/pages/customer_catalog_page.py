import re
import time

from pages.BaseClass import BaseClass
from pages.selectors import catalog_page_loc as cpl


class CustomerCatalogPage(BaseClass):
    page_url = "catalog"

    def check_catalog_page(self, text):
        url = self.get_current_url()
        word = re.search(r"\w+$", url)
        assert word.group() == text

    def check_all_products_to_page(self, number):
        all_products = self.all_find_visibility(cpl.loc_all_products)
        assert len(all_products) == number

    def click_button_leave_request(self):
        button = self.find_presence_element(cpl.loc_button_Leave_request)
        button.click()

    def check_button_leave_request(self, text):
        self.click_button_leave_request()
        text_next_frame = self.find_visibility(cpl.loc_text_next_page)
        assert text_next_frame.text == text

    def check_form_to_leave_request(self, name, phone, describe, link=None):
        self.click_button_leave_request()
        full_name = self.find_visibility(cpl.loc_input_name)
        self.send(full_name, name)
        telephone = self.find_presence_element(cpl.loc_input_phone_number)
        self.send(telephone, phone)
        desc = self.find_presence_element(cpl.loc_input_describe_task)
        self.send(desc, describe)
        button_link = self.find_presence_element(cpl.loc_button_select_file)
        button_link.click()
        link_to_file = self.find_visibility(cpl.loc_button_link_to_file)
        link_to_file.click()
        input_to_link = self.find_visibility(cpl.loc_provide_link)
        self.send(input_to_link, link)
        button_download = self.find_visibility(cpl.loc_download_link)
        button_download.click()

    def link_to_soft(self):
        self.scroll_to_offset(400)
        any_soft = self.find_visibility(cpl.loc_soft_pixar)
        any_soft.click()

    def check_form_to_order_soft(self, title_soft, quantity_soft, my_name, phone, describe, text):
        self.link_to_soft()
        button_order = self.find_visibility(cpl.loc_button_order)
        button_order.click()
        my_soft = self.find_visibility(cpl.loc_text_soft_pixar)
        count_soft = self.find_visibility(cpl.loc_quantity_soft_to_basket)
        if my_soft.text == title_soft and len(count_soft.text) == quantity_soft:
            name = self.find_visibility(cpl.loc_soft_form_name)
            self.send(name, my_name)
            tel = self.find_presence_element(cpl.loc_soft_form_phone)
            self.send(tel, phone)
            desc = self.find_presence_element(cpl.loc_soft_form_desc)
            self.send(desc, describe)
            checkbox = self.find_visibility(cpl.loc_soft_form_checkbox)
            checkbox.click()
            button = self.find_presence_element(cpl.loc_button_soft_form)
            button.click()
            text_success = self.find_visibility(cpl.loc_soft_order_success)
            assert text_success.text == text
            time.sleep(2)
        else:
            self.find_visibility(cpl.loc_delete_soft).click()
