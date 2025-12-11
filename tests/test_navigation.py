# tests/test_navigation.py
from utils.driver import get_driver
from utils.report_generator import ReportGenerator
from pages.dashboard_page import DashboardPage

def test_navigation():

    driver = get_driver()
    dashboard = DashboardPage(driver)

    try:
        dashboard.open_dashboard()

        dashboard.go_to_dropdown()
        assert "Dropdown" in dashboard.get_header_text()

        dashboard.open_dashboard()
        dashboard.go_to_checkboxes()
        assert "Checkboxes" in dashboard.get_header_text()

        ReportGenerator.write_csv("test_navigation", "PASS")

    except Exception as e:
        ReportGenerator.write_csv("test_navigation", "FAIL")
        raise e

    finally:
        driver.quit()
