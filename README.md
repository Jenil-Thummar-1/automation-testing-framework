🧪 Automation Testing Framework (Python + Selenium)

# End-to-End Automation Testing Framework  

A complete end-to-end automation testing framework built using Python, Selenium, and PyTest, featuring Page Object Model (POM), HTML/CSV reporting, structured logs, reusable utilities, and modular test scripts.

This framework automates real-world workflows such as:
✔ Login Testing
✔ Form Submission
✔ Website Navigation
✔ Reporting + Logging

🚀 Features
Page Object Model (POM)

Improves readability, reusability, and scalability.
Custom HTML + CSV Reporting

Generates:
reports/report.html
reports/test_report.csv

Logging System
Stores execution logs in:
logs/app.log

Selenium WebDriver Utility
Centralized driver configuration using Chrome with custom options.

PyTest Integration
Single test or entire suite run ho sakta hai:

python run_all.py

📁 Project Structure
automation_framework/
│
├── config/
│   └── config.py
│
├── logs/
│   └── app.log
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── form_page.py
│   └── dashboard_page.py
│
├── reports/
│   ├── report.html
│   └── test_report.csv
│
├── tests/
│   ├── test_login.py
│   ├── test_form.py
│   └── test_navigation.py
│
├── utils/
│   ├── driver.py
│   └── report_generator.py
│
└── run_all.py

⚙️ Technologies Used
Technology	Purpose
Python	Core scripting
Selenium WebDriver	Browser automation
PyTest	Test execution
HTML/CSS	Report generation
ChromeDriver	Browser driver
Logging Module	Execution logs
Page Object Model	Test structure

▶️ How to Run Tests
Step 1 — Install required libraries
pip install selenium
pip install pytest

Step 2 — Run all tests
python run_all.py

Step 3 — Check reports
HTML Report: reports/report.html
CSV Report: reports/test_report.csv

Logs: logs/app.log
📝 Test Scenarios Covered
✔ Login Tests

Valid login
Invalid login

✔ Form Submission Test
Fills fields and validates success message

✔ Navigation Test
Automates switching between pages and verifies UI text

->Why This Framework Is Professional
Modular, reusable Page Object Model
Custom reporting system
Error logging + screenshots (optional extension)
Clean folder structure
Industry-grade coding practices
Easy to scale & maintain
Ready for CI/CD integration (GitHub Actions, Jenkins etc.)

🎯 Future Enhancements
Add screenshot capture on test failure
Add Allure Reporting
Integrate CI/CD with GitHub Actions
Add API Testing module
Add parallel execution support

👨‍💻 Author
Jenil Thummar
Python Automation Engineer (Beginner → Pro Journey 🚀)
GitHub: https://github.com/Jenil-Thummar-1
# Updated README
