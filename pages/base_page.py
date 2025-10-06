from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"
        self.time = 10

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.time).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = WebDriverWait(self.driver, self.time).until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))
