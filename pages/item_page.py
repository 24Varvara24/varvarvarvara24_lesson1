from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        # Кнопка Add to Cart: Здесь будет локатор XPATH
        self.add_to_cart_btn = (By.XPATH, '//*[@id="add-to-cart"]')
        # Кнопка Back to products: Здесь будет локатор XPATH
        self.back_to_products = (By.XPATH, '//*[@id="back-to-products"]')

    @allure.step('клик по кнопке "Add to cart"')
    def add_to_cart_btn_click(self) -> None:
        self.find_element(*self.add_to_cart_btn).click()

    @allure.step('клик по кнопке "Back to products"')
    def back_to_products_click(self) -> None:
        self.find_element(*self.back_to_products).click()
