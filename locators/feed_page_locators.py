from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed_orderFeed')]")
    ORDER_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//p[contains(text(), 'идентификатор')]")

    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
