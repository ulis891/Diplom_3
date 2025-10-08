from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
import allure


class MainPage(BasePage):
    @allure.step("Клик на кнопку входа")
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Клик на кнопку личного кабинета")
    def click_personal_account_button(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик на кнопку конструктора")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на кнопку заказов")
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_ingredient(self, index=0):
        self.wait_for_element_visible(
            (MainPageLocators.INGREDIENT_ITEM[0], f"{MainPageLocators.INGREDIENT_ITEM[1]}[{index + 1}]"))
        ingredient_locator = (
        MainPageLocators.INGREDIENT_ITEM[0], f"{MainPageLocators.INGREDIENT_ITEM[1]}[{index + 1}]")
        self.click_element(ingredient_locator)
        # sleep(2)
        # ingredients[index].click()

    def is_modal_visible(self):
        try:
            self.wait_for_element_visible(MainPageLocators.MODAL)
            return True
        except:
            return False

    @allure.step("Клик на кнопку закрытия модального окна")
    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_not_visible(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверка видимости деталей ингредиента")
    def is_ingredient_details_visible(self):
        try:
            self.wait_for_element_visible(MainPageLocators.INGREDIENT_DETAILS)
            return True
        except:
            return False

    @allure.step("Получение количества ингредиентов в корзине")
    def get_ingredient_counter(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        counters = ingredients[index].find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if counters:
            return int(counters[0].text)
        return 0

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_ingredient_to_basket(self, index=6):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        basket = self.find_element(MainPageLocators.ORDER_BASKET)
        action = ActionChains(self.driver)
        action.drag_and_drop(ingredients[index], basket).perform()

    @allure.step("Клик на кнопку оформления заказа")
    def click_order_button(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    # def get_order_number(self):
    #     if self.is_modal_visible():
    #         number = self.find_element(MainPageLocators.ORDER_NUMBER).text
    #         if number == "9999":
    #             sleep(5)
    #             number = self.find_element(MainPageLocators.ORDER_NUMBER).text
    #         return number
    #     else:
    #         return None

    def get_order_number(self):
        if self.is_modal_visible():
            # # Начальное значение
            # number = self.find_element(MainPageLocators.ORDER_NUMBER).text
            #
            # # Если значение "9999", ждём, пока оно изменится
            # if number == "9999":
            WebDriverWait(self.driver, self.time).until(
                lambda d: self.find_element(MainPageLocators.ORDER_NUMBER).text != "9999"
            )
            number = self.find_element(MainPageLocators.ORDER_NUMBER).text

            return number
        else:
            return None

    @allure.step("Отображение конструктора")
    def is_constructor(self):
        return self.driver.current_url == self.base_url + "/"

    @allure.step("Отображение ленты заказов")
    def is_order_feed(self):
        if self.driver.current_url == self.base_url + "/feed":
            return True
        else:
            return False
