# pages/login_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL


class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "h1.post-title")
    ERROR_MESSAGE = (By.ID, "error")

    def open_login_page(self):
        self.open(BASE_URL)

    def enter_username(self, username):
        self.type(self.USERNAME, username)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
