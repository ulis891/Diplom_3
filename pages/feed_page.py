from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def click_order(self, index=0):
        orders = self.find_elements(FeedPageLocators.ORDER_ITEM)
        orders[index].click()

    def is_order_details_visible(self):
        try:
            self.wait_for_element_visible(FeedPageLocators.ORDER_DETAILS_MODAL)
            return True
        except:
            return False

    def get_total_orders_count(self):
        return int(self.get_text(FeedPageLocators.TOTAL_ORDERS))

    def get_today_orders_count(self):
        return int(self.get_text(FeedPageLocators.TODAY_ORDERS))

    def get_in_progress_orders(self):
        in_progress_section = self.find_element(FeedPageLocators.IN_PROGRESS_SECTION)
        order_numbers = in_progress_section.find_elements(*FeedPageLocators.ORDER_NUMBER)
        return [order.text for order in order_numbers]

    def is_order_in_progress(self, order_number):
        return order_number in self.get_in_progress_orders()