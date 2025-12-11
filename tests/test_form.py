# tests/test_form.py

from utils.driver import get_driver
from utils.report_generator import ReportGenerator
from pages.form_page import FormPage

def test_form_submission():

    driver = get_driver()
    form = FormPage(driver)

    try:
        form.open_form_page()
        form.enter_name("Jonty")
        form.enter_email("jonty@test.com")
        form.submit_form()

        assert "Form submitted" in form.get_success()
        ReportGenerator.write_csv("test_form_submission", "PASS")

    except Exception as e:
        ReportGenerator.write_csv("test_form_submission", "FAIL")
        raise e

    finally:
        driver.quit()
