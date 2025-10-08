import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
import helper


@allure.epic('stellarburgers')
class TestOrderFeed:
    @allure.feature('Лента заказов')
    @allure.story('Детали заказа в модальном окне')
    def test_order_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed_button()
        feed_page = FeedPage(driver)
        feed_page.click_order(0)
        assert feed_page.is_order_details_visible()

    @allure.feature('Лента заказов')
    @allure.story('Отображение заказов пользователя в ленте')
    def test_user_orders_in_feed(self, driver, user_with_order_from_api):
        email, password, order_number = user_with_order_from_api
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.login(email, password)
        main_page.click_order_feed_button()
        feed_page = FeedPage(driver)
        assert feed_page.is_order_in_progress(order_number)

    @allure.feature('Лента заказов')
    @allure.story('Увеличение счетчика всех заказов')
    def test_total_orders_counter_increase(self, driver, create_account):
        email, password, token = create_account
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed_button()
        feed_page = FeedPage(driver)
        initial_total = feed_page.get_total_orders_count()
        helper.add_order(token)
        new_total = feed_page.get_total_orders_count()
        assert new_total > initial_total

    @allure.feature('Лента заказов')
    @allure.story('Увеличение счетчика заказов за сегодня')
    def test_today_orders_counter_increase(self, driver, create_account):
        email, password, token = create_account
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed_button()
        feed_page = FeedPage(driver)
        initial_total = feed_page.get_today_orders_count()
        helper.add_order(token)
        new_total = feed_page.get_today_orders_count()
        assert new_total > initial_total

    @allure.feature('Лента заказов')
    @allure.story('Отображение заказа в работе')
    def test_order_in_progress(self, driver, create_account):
        email, password, token = create_account
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed_button()
        feed_page = FeedPage(driver)
        order_number = helper.add_order(token)
        assert feed_page.is_order_in_progress(order_number)
