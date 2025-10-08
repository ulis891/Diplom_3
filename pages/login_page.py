import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step("Ввод email")
    def input_email(self, email):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def input_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажатие кнопки логина")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Нажатие ссылки регистрации")
    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)

    @allure.step("Нажатие ссылки восстановления пароля")
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Вход в аккаунт")
    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()
