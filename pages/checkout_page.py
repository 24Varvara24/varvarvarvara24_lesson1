from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.firstname = (By.ID, 'first-name')  # Локатор по ID для элемента строки ввода firstname
        self.lastname = (By.ID, 'last-name')  # Локатор по ID для элемента строки ввода lastname
        self.postal_code = (By.ID, 'postal-code')  # Локатор по ID для элемента строки ввода Postal Code
        self.continue_btn = (By.ID, 'continue')  # кнопка continue:локатор по ID
        self.checkout_btn = (By.ID, 'checkout')  # кнопка checkout:локатор по ID
        self.item_bolt_tshirt = (
            By.CSS_SELECTOR, '[data-test="inventory-item-name"]')  # название товара:локатор по селектору
        self.item_bolt_tshirt_price = (By.CSS_SELECTOR, '[class="inventory_item_price"]')  # цена:локатор по селектору

    @allure.step('клик по кнопке "Checkout"')
    def click_btn_checkout(self) -> None:
        self.find_element(*self.checkout_btn).click()

    @allure.step('ввод данных')
    def input_data(self, firstname: str, lastname: str, postal_code: str) -> None:
        self.find_element(*self.firstname).send_keys(firstname)
        self.find_element(*self.lastname).send_keys(lastname)
        self.find_element(*self.postal_code).send_keys(postal_code)

    @allure.step('клик по кнопке Continue')
    def click_continue_btn(self) -> None:
        self.find_element(*self.continue_btn).click()
