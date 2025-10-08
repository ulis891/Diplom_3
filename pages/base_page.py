from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"
        self.time = 10
        self.login_url = f'{self.base_url}/login'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.time).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        self.wait_for_page_load()
        self.wait_for_element_visible(locator)
        if self.is_element_blocked(locator):
            raise Exception(f"Элемнт {locator} заблокирован или недоступен")
        else:
            element = WebDriverWait(self.driver, self.time).until(EC.element_to_be_clickable(locator))
            ActionChains(self.driver).move_to_element(element).click().perform()
            if self.driver.current_url == self.base_url + '/' and locator != MainPageLocators.PLACE_ORDER_BUTTON:
                element.click()


    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))

    def wait_for_element_not_visible(self, locator):
        return WebDriverWait(self.driver, self.time).until(EC.invisibility_of_element_located(locator))

    def wait_for_url_to_contain(self, expected_url_part):
        WebDriverWait(self.driver, self.time).until(lambda d: expected_url_part in d.current_url)

    def is_element_blocked(self, locator):
        try:
            element = self.find_element(locator)
            return not element.is_displayed() or not element.is_enabled()
        except:
            return True

    def wait_for_page_load(self):
        WebDriverWait(self.driver, self.time).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
