import allure
import pytest
import requests
from bs4 import BeautifulSoup
from allure_commons.types import Severity, LabelType
import time


URL = 'https://artmas.by'

@allure.title("Фикстура для начала сессии")
@pytest.fixture()
def session():
    with allure.step("Именуем сессию"):
        session = requests.Session()
    with allure.step("Определяем юзер агента как версию браузера и ОС"):
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    return session

@allure.title("Фикстура получения ответа от сервера")
@pytest.fixture()
def main_page():
    with allure.step("Получения ответа по url-адресу https://artmas.by"):
        response = requests.get(url=URL)
    return response

@allure.title("Тест на получения статуса 200")
@allure.description("Тестируем что основные страницы сайта https://artmas.by работают")
@allure.label(LabelType.FRAMEWORK, 'pytest')
@allure.label(LabelType.LANGUAGE, 'python')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('page',
                         ["",
                         "catalog",
                         "projects",
                         "designers",
                         "blog"]
                         )
def test_all_pages_status_code_200(session, page):
    with allure.step("Получение имя странички сайта и подготовка url-адреса"):
        url = f'{URL}/{page}'.strip('/')
    with allure.step("Получаем ответ от выбранной странички сайта"):
        response = session.get(url)
    with allure.step("Проверка на статус кода каждой страницы"):
        assert response.status_code == 200, f'Страница {page} не активна. Статус кода: {response.status_code}'

@allure.title("Функция для проверки Content_type")
def check_headers_content_type(response):
    assert response == 'text/html; charset=UTF-8'

@allure.title("Функция для проверки названия страниц сайта")
def check_title_page(response, name_page):
    assert response == name_page

@allure.title("Параметризованный тест для headers")
@allure.description("Тестируем headers на то какой мы получаем"
                    " Content_type https://artmas.by работают")
@allure.label(LabelType.FRAMEWORK, 'pytest')
@allure.label(LabelType.LANGUAGE, 'python')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('page',
                         ["",
                         "catalog",
                         "projects",
                         "designers",
                         "blog"]
                         )
def test_headers_text_html_all_pages(session, page):
    with allure.step("Получение имя странички сайта и подготовка url-адреса"):
        response = session.get(url=f'{URL}/{page}')
    with allure.step("Получаем ответ для получения нужного headers - content-type"):
        content_type = response.headers["content-type"]
    with allure.step("Проверка нужного headers: ожидаемый ответ text/html; charset=UTF-8"):
        check_headers_content_type(content_type)


@allure.title("Параметризованный тест для проверки названия страниц")
@allure.description("Находим соответствие названий страниц")
@allure.label(LabelType.FRAMEWORK, 'pytest', 'BeautifulSoup4')
@allure.label(LabelType.LANGUAGE, 'python')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('page, page_title',
                         [
                         ("", "Дизайнерская мягкая мебель ARTMAS - Минск, Москва, Санкт-Петербург"),
                         ("catalog", "Каталог товаров"),
                         ("projects", "Проекты"),
                         ("designers", "Дизайнерам"),
                         ("blog", "Блог"),
                         ])
def test_all_pages_title(session, page, page_title):
    with allure.step("Проверка для главной страницы"):
        if page == "":
            url = f'{URL}'
            response = session.get(url=url)
            with allure.step("Использование вспомогательный библиотеки для парсера страницы"):
                soup = BeautifulSoup(response.text, 'html.parser').title.string
                assert 'Дизайнерская мягкая мебель ARTMAS' in soup
        else:
            with allure.step("Получение имя странички сайта и подготовка url-адреса"):
                url = f'{URL}/{page}'.strip('/')
                response = session.get(url)
                with allure.step("Нахождение название страницы через парсер"):
                    soup = BeautifulSoup(response.text, 'html.parser').title.string
                with allure.step("Проверка оглавления страницы"):
                    check_title_page(soup, page_title)

@allure.title("Тест на скорость ответа страницы")
@allure.description("Скорость ожидания ответа, очень важна для удобства клиента")
@allure.label(LabelType.FRAMEWORK, 'pytest', 'time')
@allure.label(LabelType.LANGUAGE, 'python')
@allure.severity(allure.severity_level.CRITICAL)
def test_speed_time_open_site(session):
    with allure.step("Список страниц"):
        names_pages = ["", "catalog", "projects", "designers", "blog"]
    with allure.step("Итерация по страницам"):
        for name in names_pages:
            url = f'{URL}/{name}'.strip('/')
            with allure.step("Замеряем стартовое время открытия страницы"):
                start_time = time.time()
                response = session.get(url=url)
            with allure.step("получения результата в секундах"):
                end_time = time.time() - start_time
            with allure.step("Проверка скорости на ответ"):
                if end_time < 2:
                    print(f'{name} - {end_time:.1f} sec - speed page')
                else:
                    assert False, f'{name} - {end_time:.1f} sec - slow page'
