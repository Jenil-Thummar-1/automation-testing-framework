import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

    def click(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except Exception as e:
            logging.error(f"Failed to click {locator} | {e}")
            raise e

    def type(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
        except Exception as e:
            logging.error(f"Failed to TYPE in {locator} | {e}")
            raise e

    def get_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except Exception as e:
            logging.error(f"Failed to get TEXT from {locator} | {e}")
            raise e
