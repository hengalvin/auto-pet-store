import os
import subprocess
import argparse
import datetime

def main():
    parser = argparse.ArgumentParser(description="Run API Automation Tests")
    parser.add_argument('--create-report', action='store_true', help='Generate Allure report after test run')
    parser.add_argument('--open', action='store_true', help='Auto open Allure report after generate report')
    parser.add_argument("--path", default="tests/", help="Path to tests (default: tests/)")
    args = parser.parse_args()

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    results_dir = f"reports/allure-results/{timestamp}"
    report_dir = f"reports/allure-report/{timestamp}"

    os.makedirs(results_dir, exist_ok=True)

    pytest_cmd = [
        "pytest",
        "-v",
        args.path,  # configurable if want to test 
    ]

    if args.create_report:
        pytest_cmd.append(f"--alluredir={results_dir}")

    print("Running tests...")
    subprocess.run(pytest_cmd)

    if args.create_report:
        print("Generating Allure report...")
        subprocess.run(["allure", "generate", results_dir, "-o", report_dir, "--clean"])

        if args.open:
            print("Opening Allure report in browser...")
            subprocess.run(["allure", "open", report_dir])

if __name__ == "__main__":
    main()
