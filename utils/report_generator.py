# utils/report_generator.py

import csv
from datetime import datetime
import os
from config.config import REPORT_CSV, HTML_REPORT
import logging


class ReportGenerator:

    @staticmethod
    def write_csv(test_name, status):
        """Write each test result to CSV file."""
        try:
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create file if not exists
            file_exists = os.path.isfile(REPORT_CSV)

            with open(REPORT_CSV, mode='a', newline='') as file:
                writer = csv.writer(file)

                # Add header only once
                if not file_exists:
                    writer.writerow(["Test Name", "Status", "Timestamp"])

                writer.writerow([test_name, status, time_now])

            logging.info(f"CSV updated → {test_name} : {status}")

        except Exception as e:
            logging.error(f"Failed to write CSV: {e}")

    @staticmethod
    def generate_html_report():
        """Generate a clean HTML report from CSV."""
        try:
            if not os.path.exists(REPORT_CSV):
                logging.warning("No CSV report found for HTML generation.")
                return

            rows = []

            with open(REPORT_CSV, "r") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)   # skip header
                for row in csv_reader:
                    rows.append(row)

            with open(HTML_REPORT, "w") as html:
                html.write("""
                <html>
                <head>
                    <style>
                        table {border-collapse: collapse; width: 100%;}
                        th, td {border: 1px solid #444; padding: 8px; text-align: left;}
                        th {background-color: #222; color: white;}
                    </style>
                </head>
                <body>
                <h2>Automation Test Report</h2>
                <table>
                <tr><th>Test Name</th><th>Status</th><th>Timestamp</th></tr>
                """)

                for r in rows:
                    color = "green" if r[1] == "PASS" else "red"
                    html.write(
                        f"<tr><td>{r[0]}</td><td style='color:{color}'>{r[1]}</td><td>{r[2]}</td></tr>"
                    )

                html.write("</table></body></html>")

            logging.info("HTML report generated successfully.")

        except Exception as e:
            logging.error(f"Failed to generate HTML report: {e}")
