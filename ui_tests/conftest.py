from selenium import webdriver
import pytest
from pages.customer_main_page import CustomerMainPage
from pages.customer_catalog_page import CustomerCatalogPage
from pages.customer_designer_page import CustomerDesignerPage


@pytest.fixture
def driver(request):
    # switching_to_desktop_telegram(Options())
    driver_chrome = webdriver.Chrome()
    driver_chrome.maximize_window()
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture
def main_page(driver):
    return CustomerMainPage(driver)


@pytest.fixture
def catalog_page(driver):
    return CustomerCatalogPage(driver)

@pytest.fixture
def designer_page(driver):
    return CustomerDesignerPage(driver)