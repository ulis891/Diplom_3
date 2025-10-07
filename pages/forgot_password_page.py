from pages.base_page import  BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    def input_email(self, email):
        self.input_text(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        self.click_element(ForgotPasswordLocators.RESTORE_BUTTON)

    def click_show_password_button(self):
        self.click_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):
        try:
            self.wait_for_element_visible(ForgotPasswordLocators.ACTIVE_PASSWORD_FIELD)
            return True
        except:
            return False

    def restore_password(self, email):
        self.input_email(email)
        self.click_restore_button()
