# config/config.py
from pathlib import Path
import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------
# Logs
# ---------------------------
LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")
# Local test pages
LOCAL_FORM = str(Path(BASE_DIR).joinpath("test_pages", "local_form.html").absolute())
# ---------------------------
# Reports
# ---------------------------
REPORT_CSV = os.path.join(BASE_DIR, "reports", "test_report.csv")
HTML_REPORT = os.path.join(BASE_DIR, "reports", "report.html")

# ---------------------------
# URLs
# ---------------------------
BASE_URL = "https://practicetestautomation.com/practice-test-login/"
FORM_URL = "https://practicetestautomation.com/contact-form/"
DASHBOARD_URL = "https://the-internet.herokuapp.com/"

# ---------------------------
# Login Credentials
# ---------------------------
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"

INVALID_USERNAME = "wrong"
INVALID_PASSWORD = "incorrect"
