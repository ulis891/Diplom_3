import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    @allure.step("Клик по заказу")
    def click_order(self, index=0):
        orders = self.find_elements(FeedPageLocators.ORDER_ITEM)
        orders[index].click()

    def is_order_details_visible(self):
        try:
            self.wait_for_element_visible(FeedPageLocators.ORDER_DETAILS_MODAL)
            return True
        except:
            return False

    @allure.step("Получить количество заказов")
    def get_total_orders_count(self):
        return int(self.get_text(FeedPageLocators.TOTAL_ORDERS))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_text(FeedPageLocators.TODAY_ORDERS))

    @allure.step("Получить список заказов в работе")
    def get_in_progress_orders(self):
        in_progress_section = self.find_element(FeedPageLocators.IN_PROGRESS_SECTION)
        order_numbers = in_progress_section.find_elements(*FeedPageLocators.ALL_ORDER_NUMBERS)
        return [order.text for order in order_numbers]

    def is_order_in_progress(self, order_number):
        orders = self.get_in_progress_orders()
        return "#0" + str(order_number) in orders
