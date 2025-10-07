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
        try:
            self.wait_for_element_visible(ProfilePageLocators.ORDER_HISTORY_LIST)
            return True
        except:
            return False

    @allure.step("Проверка выхода из профиля")
    def is_logged_out(self):
        return "login" in self.driver.current_url
