from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
