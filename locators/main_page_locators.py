from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")

    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter')]")

    ORDER_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
