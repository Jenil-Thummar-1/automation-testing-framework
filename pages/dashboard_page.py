# pages/dashboard_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    DROPDOWN = (By.LINK_TEXT, "Dropdown")
    CHECKBOXES = (By.LINK_TEXT, "Checkboxes")
    HEADER = (By.TAG_NAME, "h3")

    def open_dashboard(self):
        self.open("https://the-internet.herokuapp.com/")

    def go_to_dropdown(self):
        self.click(self.DROPDOWN)

    def go_to_checkboxes(self):
        self.click(self.CHECKBOXES)

    def get_header_text(self):
        return self.get_text(self.HEADER)
