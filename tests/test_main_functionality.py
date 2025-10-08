import allure
from pages.main_page import MainPage


@allure.epic('stellarburgers')
class TestMainFunctionality:
    @allure.feature('Основной функционал')
    @allure.story('Переход в конструктор')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_constructor_button()
        assert main_page.is_constructor()

    @allure.feature('Основной функционал')
    @allure.story('Переход в ленту заказов')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed_button()
        assert main_page.is_order_feed()

    @allure.feature('Основной функционал')
    @allure.story('Открытие деталей ингредиента')
    def test_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_ingredient(0)
        assert main_page.is_modal_visible()
        assert main_page.is_ingredient_details_visible()

    @allure.feature('Основной функционал')
    @allure.story('Закрытие деталей ингредиента')
    def test_close_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_ingredient(0)
        main_page.close_modal()
        assert not main_page.is_modal_visible()

    @allure.feature('Основной функционал')
    @allure.story('Увеличение счетчика ингредиента')
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        initial_count = main_page.get_ingredient_counter(0)
        main_page.drag_ingredient_to_basket(0)
        new_count = main_page.get_ingredient_counter(0)
        assert new_count > initial_count

    @allure.feature('Основной функционал')
    @allure.story('Оформление заказа авторизованным пользователем')
    def test_place_order_authenticated_user(self, login_user):
        main_page = MainPage(login_user)
        main_page.drag_ingredient_to_basket(0)
        main_page.click_order_button()
        assert main_page.is_modal_visible()
