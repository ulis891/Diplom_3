from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Отмена']")
    ORDER_HISTORY_LIST = (By.XPATH, "//ul[contains(@class, 'OrderHistory_list')")
