from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.item_bolt_tshirt = (
            By.CSS_SELECTOR, '[data-test="inventory-item-name"]')  # название товара:локатор по селектору
        self.item_bolt_tshirt_price = (By.CSS_SELECTOR, '[class="inventory_item_price"]')  # цена:локатор по селектору
        self.payment_info_label = (
            By.CSS_SELECTOR, '[data-test="payment-info-label"]')  # Payment Information:локатор по селектору
        self.payment_info_value = (By.CSS_SELECTOR, '[data-test="payment-info-value"]')
        self.shipping_info_label = (
            By.CSS_SELECTOR, '[data-test="shipping-info-label"]')  # Shipping Information:локатор по селектору
        self.shipping_info_value = (By.CSS_SELECTOR, '[data-test="shipping-info-value"]')
        self.total_info_label = (By.CSS_SELECTOR, '[data-test="total-info-label"]')  # Price Total:локатор по селектору
        self.subtotal_label = (
            By.CSS_SELECTOR, '[data-test="subtotal-label"]')  # итоговая цена без учета налогов:локатор по селектору
        self.tax = (By.CSS_SELECTOR, '[data-test="tax-label"]')  # налоги:локатор по селектору
        self.total_label = (By.CSS_SELECTOR, '[data-test="total-label"]')  # итоговая цена:локатор по селектору

        self.finish_btn = (By.ID, 'finish')  # кнопка finish:локатор по Id

    @allure.step('Проверить название товара')
    def get_bolt_tshirt_name(self) -> str:
        return self.find_element(*self.item_bolt_tshirt).text

    @allure.step('Получить цену Sauce Labs Bolt T-Shirt(на странице заказа)')
    def get_bolt_tshirt_price(self) -> str:
        return self.find_element(*self.item_bolt_tshirt_price).text

    @allure.step('Получить цену Sauce Labs Bolt T-Shirt(на странице заказа)')
    def get_bolt_tshirt_price(self) -> str:
        return self.find_element(*self.item_bolt_tshirt_price).text

    @allure.step('Проверка наличия заголовка payment information и получить значение')
    def find_and_get_payment_information(self) -> str:
        assert self.find_element(*self.payment_info_label), ('[FAILED]:заголовок payment information отстуствует')
        return self.find_element(*self.payment_info_value).text

    @allure.step('Проверка наличия заголовка Shipping Information и получить значение')
    def find_and_get_shipping_info(self) -> str:
        assert self.find_element(*self.shipping_info_label), ('[FAILED]:заголовок shipping info отстуствует')
        return self.find_element(*self.shipping_info_value).text

    @allure.step('Проверка наличия заголовка Shipping Information')
    def find_total_info_label(self) -> str:
        assert self.find_element(*self.total_info_label), ('[FAILED]:заголовок Price Total: отстуствует')

    @allure.step('Получить цену товара без учета налогов(item_total)')
    def find_subtotal_value(self) -> str:
        return self.find_element(*self.subtotal_label).text

    @allure.step('Значение tax')
    def find_tax(self) -> str:
        return self.find_element(*self.tax).text

    @allure.step('Конечная цена с учетом налогов')
    def total_price(self) -> float:
        t = float(self.find_element(*self.subtotal_label).text[-5:]) + float(self.find_element(*self.tax).text[-4:])
        return t

    @allure.step('Клик по кнопке finish')
    def click_finish_btn(self) -> None:
        self.find_element(*self.finish_btn).click()
