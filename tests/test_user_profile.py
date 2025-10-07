import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestUserProfile:
    @allure.feature('Личный кабинет')
    @allure.story('Переход в личный кабинет')
    def test_go_to_personal_account(self, login_user):
        driver = login_user
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        assert "account" in driver.current_url
        assert "profile" in driver.current_url

    @allure.feature('Личный кабинет')
    @allure.story('Переход в историю заказов')
    def test_go_to_order_history(self, user_with_order):
        driver = user_with_order
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        assert "order-history" in driver.current_url

    @allure.feature('Личный кабинет')
    @allure.story('Выход из аккаунта')
    def test_logout(self, login_user):
        driver = login_user
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_logout()
        profile_page.wait_for_url_to_contain("login")
        assert "login" in driver.current_url
