from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    base_url = "https://artmas.by/"
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        if self.page_url is None:
            self.driver.get(f"{self.base_url}")
        else:
            self.driver.get(f"{self.base_url}{self.page_url}")

    def find_headers_title(self, title: str):
        return self.wait.until(EC.title_is(title=title))

    def find_visibility(self, locator):
        """Нвхомин элемент с ожидание когда он будет виден"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def all_find_visibility(self, locator):
        """Поиск всех элементо на странице после их появления"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def find_presence_element(self, locator):
        """Поиск элемента по расположению"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def scroll_down(self):
        """Плавная прокрутка страницы в самый низ"""
        self.driver.execute_script(
            "window.scrollTo({top: document.body.scrollHeight," "behavior: 'smooth'});"
        )

    def scroll_to_offset(self, offset=0):
        """Прокрутка до определённого места по заданной координате"""
        if offset:
            self.driver.execute_script(f"window.scrollTo(0, {offset});")
        else:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

    def get_current_url(self):
        return self.driver.current_url

    def send(self, object, text):
        object.send_keys(text)
