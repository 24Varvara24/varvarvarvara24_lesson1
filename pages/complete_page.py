from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class CompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.checkout_complete = (By.CSS_SELECTOR, '[data-test="title"]')
        self.order_title = (By.CSS_SELECTOR, '[data-test="complete-header"]')
        self.order_text = (By.CSS_SELECTOR, '[data-test="complete-text"]')
        self.back_home_btn = (By.CSS_SELECTOR, '[data-test="back-to-products"]')

    @allure.step('Проверка наличия надписи Checkout: Complete!')
    def find_checkout_complete(self) -> None:
        assert self.find_element(*self.checkout_complete)

    @allure.step('Проверка наличия надписи Thank you for your order!')
    def find_order_title(self) -> None:
        assert self.find_element(*self.order_title)

    @allure.step('Проверка наличия текста заказа')
    def find_order_text(self) -> None:
        assert self.find_element(*self.order_text)

    @allure.step('Проверка наличия кнопки Back Home')
    def find_back_home_btn(self) -> None:
        assert self.find_element(*self.back_home_btn)

    @allure.step('Клик по кнопке Back Home')
    def find_back_home_btn(self) -> None:
        self.find_element(*self.back_home_btn).click()
