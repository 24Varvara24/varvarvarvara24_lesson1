from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By
from requests import get


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        # Локатор XPATH элемента продукта. Локатор должен находить
        # ровно 2 элемента на странице: первый и второй товар
        # то есть в DevTools вы должны видеть "1 of 2" при поиске данного локатора
        self.item_list = (By.CSS_SELECTOR, '[class="cart_item"]')
        self.item_bolt_tshirt = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        self.item_bolt_tshirt_price = (
            By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')

    @allure.step('подсчет количества элемента inventory_item_desc на странице')
    def number_of_products(self) -> int:
        return len(self.find_elements(*self.item_list))

    @allure.step('Проверить название товара')
    def get_bolt_tshirt_name(self) -> str:
        return self.find_element(*self.item_bolt_tshirt).text

    @allure.step('Получить цену Sauce Labs Bolt T-Shirt(на странице корзины)')
    def get_bolt_tshirt_price(self) -> str:
        return self.find_element(*self.item_bolt_tshirt_price).text
