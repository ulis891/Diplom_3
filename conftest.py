import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from api import ApiClient
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def create_account():
    client = ApiClient()
    user = client.user_data()
    token = client.create_account(user)
    yield user["email"], user["password"], token
    client.delete_user(token)


@pytest.fixture(scope="function")
def user_with_order_from_api(create_account):
    email, password, token = create_account
    client = ApiClient()
    order_number = client.create_order(token)
    return email, password, order_number

@pytest.fixture(scope="function")
def login_user_from_api(driver, user_with_order_from_api):
    email, password, order_number = user_with_order_from_api
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.click_login_button()
    login_page = LoginPage(driver)
    login_page.login(email, password)
    return driver, order_number




@pytest.fixture(scope="function")
def login_user(driver, create_account):
    email, password, _ = create_account
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.click_login_button()
    login_page = LoginPage(driver)
    login_page.login(email, password)
    return driver


@pytest.fixture(scope="function")
def user_with_order(login_user):
    driver = login_user
    main_page = MainPage(driver)
    main_page.drag_ingredient_to_basket(0)
    main_page.click_order_button()
    order_number = main_page.get_order_number()
    main_page.close_modal()
    return driver, order_number
