import time
from utils.find_all_new_brawsers_windows import find_browsers_windows
from pages.BaseClass import BaseClass
from pages.selectors import main_page_loc as mp
import allure


class CustomerMainPage(BaseClass):
    page_url = None

    @allure.feature("Главная страница")
    @allure.description("Проверка главного текста на странице")
    def check_main_page(self, text):
        big_title_main_page = self.find_visibility(mp.name_main_page)
        assert big_title_main_page.text == text

    @allure.feature("Ссылка каталог")
    @allure.description("Проверка работает ли ссылка - catalog")
    def check_link_catalog_page(self, name):
        link_catalog_page = self.find_visibility(mp.catalog_loc)
        link_catalog_page.click()
        name_in_catalog_page = self.find_visibility(mp.catalog_page_name_loc)

        assert name_in_catalog_page.text == name

    @allure.feature("Ссылка проект")
    @allure.description("Проверка работает ли ссылка - project")
    def check_projects_page(self, name):
        link_projects_page = self.find_visibility(mp.projects_loc)
        link_projects_page.click()
        name_in_projects_page = self.find_visibility(mp.projects_page_name_loc)

        assert name in name_in_projects_page.text

    @allure.feature("Ссылка блог")
    @allure.description("Проверка работает ли ссылка - blog")
    def check_blog_page(self, name):
        link_blog_page = self.find_visibility(mp.blog_loc)
        link_blog_page.click()
        name_in_blog_page = self.find_visibility(mp.blog_name_page_loc)

        assert name in name_in_blog_page.text

    @allure.feature("Ссылка дизайнерам")
    @allure.description("Проверка работает ли ссылка - designers")
    def check_designers(self, name):
        blog = self.find_presence_element(mp.designers_loc)
        blog.click()
        element = self.find_presence_element(mp.element_designers_loc)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);", element
        )
        assert element.text == name

    @allure.feature("Ссылка контакты")
    @allure.description("Проверка работает ли ссылка - contacts")
    def check_contacts(self, name):
        link_contacts = self.find_presence_element(mp.contacts_loc)
        link_contacts.click()
        element = self.find_visibility(mp.loc_bel)
        assert element.text == name

    @allure.feature("Иконка WhatsApp")
    @allure.description("Проверка работает ли иконка - WhatsApp")
    def check_link_whatsapp(self, text):
        link_whatsapp = self.find_visibility(mp.loc_whatsapp)
        link_whatsapp.click()
        try:
            find_browsers_windows(self.driver)
            check_tel_whatsapp = self.find_visibility(mp.loc_text_whatsapp_2)
        except Exception:
            find_browsers_windows(self.driver)
            check_tel_whatsapp = self.find_visibility(mp.loc_text_whatsapp)

        assert check_tel_whatsapp.text == text

    @allure.feature("Иконка telegram")
    @allure.description("Проверка работает ли иконка - Telegram")
    def check_link_telegram(self, url):
        button_telegram = self.find_visibility(mp.loc_telegram)
        href = button_telegram.get_attribute("href")
        button_telegram.click()
        find_browsers_windows(self.driver)

        assert href == url
        assert "t.me" in href, "Ссылка не является Telegram ссылкой"

    @allure.feature("Иконка instagram")
    @allure.description("Проверка работает ли иконка - Instagram")
    def check_link_instagram(self):
        button_instagram = self.find_visibility(mp.loc_instagram)
        button_instagram.click()
        link = button_instagram.get_attribute("href")
        assert link == "https://www.instagram.com/artmas.by/"

    @allure.feature("Footer")
    @allure.description("Проверка футера на содержание")
    def check_text_main_footer(self, text):
        self.scroll_down()
        footer_text = self.find_presence_element(mp.loc_text_footer)

        assert footer_text.text == text

    @allure.feature("Прокрутка страницы")
    @allure.description("Проверка скроллинг до середины страницы")
    def check_text_in_middle_page(self, text, offset):
        self.scroll_to_offset(offset)
        element = self.find_visibility(mp.loc_lisbon)
        assert element.text == text

    @allure.feature("Оставить сообщение")
    @allure.description("Проверка работает ли сообщение по чату")
    def check_callback_button(self, text):
        self.find_presence_element(mp.loc_callback).click()
        self.find_visibility(mp.loc_open_line).click()
        time.sleep(1)
        input_message = self.find_presence_element(mp.loc_input_message)
        self.send(input_message, 'I need specialist help')
        button_message = self.find_visibility(mp.loc_button_message)
        button_message.click()
        text_massage = self.find_visibility(mp.loc_text_message).text
        assert text_massage == text
