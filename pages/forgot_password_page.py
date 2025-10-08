import allure
from pages.base_page import  BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Ввод email")
    def input_email(self, email):
        self.input_text(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Нажать кнопку восстановления пароля")
    def click_restore_button(self):
        self.click_element(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Нажать кнопку показать пароль")
    def click_show_password_button(self):
        self.click_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверка активности поля ввода пароля")
    def is_password_field_active(self):
        try:
            self.wait_for_element_visible(ForgotPasswordLocators.ACTIVE_PASSWORD_FIELD)
            return True
        except:
            return False

    @allure.step("Проверка сброса пароля")
    def restore_password(self, email):
        self.input_email(email)
        self.click_restore_button()

    @allure.step("Проверка перехода на страницу востановления пароля")
    def check_forgot_password_page(self):
        if "forgot-password" in self.driver.current_url:
            return True
        else:
            return False


    @allure.step("Проверка перехода на страницу ввода нового пароля")
    def check_reset_password_page(self):
        if "reset-password" in self.driver.current_url:
            return True
        else:
            return False
