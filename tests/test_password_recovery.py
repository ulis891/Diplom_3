import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.epic('stellarburgers')
class TestPasswordRecovery:
    @allure.feature('Восстановление пароля')
    @allure.story('Переход на страницу восстановления пароля')
    def test_go_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        assert "forgot-password" in driver.current_url

    @allure.feature('Восстановление пароля')
    @allure.story('Восстановление пароля с валидным email')
    def test_password_recovery_with_valid_email(self, driver, create_account):
        email, _, _ = create_account
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.input_email(email)
        forgot_password_page.click_restore_button()
        forgot_password_page.wait_for_url_to_contain("reset-password")
        assert "reset-password" in driver.current_url

    @allure.feature('Восстановление пароля')
    @allure.story('Показать/скрыть пароль')
    def test_show_hide_password(self, driver, create_account):
        email, _, _ = create_account
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.input_email(email)
        forgot_password_page.click_restore_button()
        forgot_password_page.click_show_password_button()
        assert forgot_password_page.is_password_field_active()
