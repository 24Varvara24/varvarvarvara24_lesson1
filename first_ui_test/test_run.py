import allure
from pages import BasePage, LoginPage, InventoryPage, ItemPage, CartPage


@allure.suite('Тесты лабы')
class Tests:

    @allure.title('Вход в аккаунт')
    def test_login(self, driver) -> None:
        auth_page = LoginPage(driver)
        with allure.step('Войти в аккаунт '):
            auth_page.auth('standard_user', 'secret_sauce')

        InventoryPage(driver).check_inventory_page_open()

    @allure.title('Вход в аккаунт с неправильным паролем')
    def test_error_password(self, driver) -> None:
        auth_page = LoginPage(driver)
        with allure.step('Войти в аккаунт '):
            auth_page.auth('standard_user', '123')

        InventoryPage(driver).check_inventory_page_not_open()

    @allure.title('Проверка добавления товара')
    def test_add_prod(self, driver) -> None:
        auth_page = LoginPage(driver)
        with allure.step('Войти в аккаунт '):
            auth_page.auth('standard_user', 'secret_sauce')
        inventory_page = InventoryPage(driver)
        with allure.step('Перейти на карту товара'):
            inventory_page.choose_item()

        item_page = ItemPage(driver)
        with allure.step('Добавить товар в корзину(клик по кнопке add_to_cart)'):
            item_page.add_to_cart_btn_click()
        with allure.step('Перейти обратно к каталогу товаров'):
            item_page.back_to_products_click()

        with allure.step('Добавить в корзину товар с названием Sauce Labs Fleece Jacket'):
            inventory_page.add_jacket_to_cart_btn_click()
        with allure.step('Перейти на страницу корзины'):
            inventory_page.cart_btn_click()

        cart_page = CartPage(driver)
        with allure.step('проверить что количество предметов в корзине равно двум'):
            assert cart_page.number_of_products() == 2
