import pytest
from utils.report_generator import ReportGenerator

# 🔹 Clean old report
open("reports/test_report.csv", "w").close()
print("\nRunning all automation tests...\n")

# 🔹 Run all tests inside tests folder
pytest.main(["-q", "tests/"])

# 🔹 After test execution, generate HTML report
ReportGenerator.generate_html_report()

print("\n✔ All tests completed successfully!")
print("✔ HTML Report Generated: reports/report.html")
