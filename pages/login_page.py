from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.login = (By.ID, 'user-name')  # Локатор по ID для элемента строки ввода login
        self.password = (By.ID, 'password')  # Локатор по ID для элемента строки ввода password
        self.login_btn = (By.NAME, 'login-button')  # Локатор по Name для элемента кнопка Login

    @allure.step('аутентификация')
    def auth(self, login: str, password: str) -> None:
        self.input(self.login, login)
        self.input(self.password, password)
        self.click(self.login_btn)
