# pages/form_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import LOCAL_FORM
from pathlib import Path

class FormPage(BasePage):

    NAME = (By.ID, "my-text-id")
    EMAIL = (By.ID, "my-email-id")
    SUBMIT = (By.ID, "submit")
    SUCCESS = (By.TAG_NAME, "h1")

    def open_form_page(self):
        # Convert local file path to file:// URI (works on Windows too)
        file_uri = Path(LOCAL_FORM).absolute().as_uri()
        self.open(file_uri)

    def enter_name(self, name):
        self.type(self.NAME, name)

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def submit_form(self):
        self.click(self.SUBMIT)

    def get_success(self):
        return self.get_text(self.SUCCESS)
