import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.epic('stellarburgers')
class TestUserProfile:
    @allure.feature('Личный кабинет')
    @allure.story('Переход в личный кабинет')
    def test_go_to_personal_account(self, login_user):
        driver = login_user
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        prfile_page = ProfilePage(driver)
        assert prfile_page.is_profile_page()

    @allure.feature('Личный кабинет')
    @allure.story('Переход в историю заказов')
    def test_go_to_order_history(self, login_user_from_api):
        driver, _ = login_user_from_api
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        assert profile_page.is_order_history_visible()

    @allure.feature('Личный кабинет')
    @allure.story('Выход из аккаунта')
    def test_logout(self, login_user):
        driver = login_user
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_logout()
        profile_page.wait_for_url_to_contain("login")
        assert profile_page.is_logged_out()

