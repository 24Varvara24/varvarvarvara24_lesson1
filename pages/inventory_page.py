from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        # Кнопка Add to Cart для Sauce Labs Bolt T-Shirt
        self.add_bolt_tshirt_to_cart_btn = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        self.shopping_cart_badge = (By.XPATH, '//*[@class="shopping_cart_badge"]')  # Цифра наличия товара
        self.item = (By.ID, 'item_1_title_link')  # Заголовок любого товара: Здесь будет локатор по ID

        # Кнопка Add to Cart для Sauce Labs Fleece Jacket: Здесь будет локатор XPATH
        self.add_jacket_to_cart_btn = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')

        self.cart_btn = (By.XPATH, '//*[@class="shopping_cart_link"]')  # Кнопка корзины: Здесь будет локатор XPATH
        self.item_bolt_tshirt_price = (By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')

    @allure.step('клик по кнопке Add to Cart для Sauce Labs Bolt T-Shirt')
    def add_tshirt_to_cart_btn_click(self) -> None:
        self.click(self.add_bolt_tshirt_to_cart_btn)

    @allure.step('Получить значение иконки рядом с корзиной(к-во товаров)')
    def number_in_red_circle(self) -> str:
        return self.get_text(self.shopping_cart_badge)

    @allure.step('клик по иконке корзины')
    def cart_btn_click(self) -> None:
        self.click(self.cart_btn)

    @allure.step('Получить цену Sauce Labs Bolt T-Shirt(в каталоге)')
    def get_bolt_tshirt_price_catalog(self) -> str:
        return self.get_text(self.item_bolt_tshirt_price)
