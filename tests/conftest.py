import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from api import ApiClient
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators


# @pytest.fixture(scope="function")
# def driver():
#     options = FirefoxOptions()
#     options.add_argument('--window-size=1920,1080')
#     service = Service(GeckoDriverManager().install())
#     driver = webdriver.Firefox(service=service)
#     yield driver
#     driver.quit()

@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_account():
    client = ApiClient()
    user = client.user_data()
    token = client.create_account(user)
    yield user["email"], user["password"]
    client.delete_user(token)


@pytest.fixture(scope="function")
def login_user(driver, create_account):
    email, password = create_account
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.click_login_button()
    login_page = LoginPage(driver)
    login_page.login(email, password)
    return driver

