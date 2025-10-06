import pytest
import requests
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


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
    return  requests.post(Urls.REGISTER, json=user_data)