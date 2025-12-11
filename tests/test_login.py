# tests/test_login.py

import time
from utils.driver import get_driver
from utils.report_generator import ReportGenerator
from pages.login_page import LoginPage

def test_login_valid():
    driver = get_driver()
    login = LoginPage(driver)

    try:
        login.open_login_page()
        login.enter_username("student")
        login.enter_password("Password123")
        login.click_login()

        assert "Logged In Successfully" in login.get_success_message()
        ReportGenerator.write_csv("test_login_valid", "PASS")

    except Exception as e:
        ReportGenerator.write_csv("test_login_valid", "FAIL")
        raise e

    finally:
        driver.quit()


def test_login_invalid():
    driver = get_driver()
    login = LoginPage(driver)

    try:
        login.open_login_page()
        login.enter_username("wrong")
        login.enter_password("incorrect")
        login.click_login()

        assert "Your username is invalid!" in login.get_error_message()
        ReportGenerator.write_csv("test_login_invalid", "PASS")

    except Exception as e:
        ReportGenerator.write_csv("test_login_invalid", "FAIL")
        raise e

    finally:
        driver.quit()
