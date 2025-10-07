from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    def click_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    def click_logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    def is_order_history_visible(self):
        try:
            self.wait_for_element_visible(ProfilePageLocators.ORDER_HISTORY_LIST)
            return True
        except:
            return False

    def is_logged_out(self):
        return "login" in self.driver.current_url
