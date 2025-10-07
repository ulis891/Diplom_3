from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)

    def click_personal_account_button(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        ingredients[index].click()

    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_not_visible(MainPageLocators.MODAL_CLOSE_BUTTON)

    def is_modal_visible(self):
        try:
            self.wait_for_element_visible(MainPageLocators.MODAL)
            return True
        except:
            return False

    def is_ingredient_details_visible(self):
        try:
            self.wait_for_element_visible(MainPageLocators.INGREDIENT_DETAILS)
            return True
        except:
            return False

    def get_ingredient_counter(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        counters = ingredients[index].find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if counters:
            return int(counters[0].text)
        return 0

    def drag_ingredient_to_basket(self, index=6):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        basket = self.find_element(MainPageLocators.ORDER_BASKET)
        action = ActionChains(self.driver)
        # action.click_and_hold(ingredients[index]).move_to_element(basket).release().perform()
        action.drag_and_drop(ingredients[index], basket).perform()

    def click_order_button(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

