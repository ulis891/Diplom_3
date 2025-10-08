from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
import allure

class ProfilePage(BasePage):
    @allure.step("Клик на кнопку 'История заказов'")
    def click_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Клик на кнопку 'Выйти'")
    def click_logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Проверка видимости истории заказов")
    def is_order_history_visible(self):
        self.wait_for_element_visible(ProfilePageLocators.ORDER_HISTORY_LIST)
        try:
            if "order-history" in self.driver.current_url:
                return True
        except:
                return False

    @allure.step("Проверка выхода из профиля")
    def is_logged_out(self):
        return "login" in self.driver.current_url

    @allure.step("Проверка перехода на странцу профиля")
    def is_profile_page(self):
        self.wait_for_element_visible(ProfilePageLocators.ORDER_HISTORY_LIST)
        if "profile" in self.driver.current_url:
            return True
        else:
            return False
