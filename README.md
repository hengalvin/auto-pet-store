# Auto-Pet-Store Automation

Automated test suite for the [Swagger Petstore API](https://petstore.swagger.io/), built using **Pytest**, with **schema validation** via **Pydantic**, and beautiful **Allure reports** reporting

https://github.com/user-attachments/assets/a5e80e4e-b3d7-49ba-8068-74b6d87c065b

---

## Features

- Clean, **modular test structure** using Pytest
- **Reusable and abstracted API client** for consistent and maintainable request handling
- **Schema validation** using Pydantic for accurate and contract-based API testing
- Integrated **Allure reporting** for detailed, visual test results
- **Custom logging** for request/response debugging
- Supports automatic **retries for flaky tests**
- Custom **run commands** to easily execute specific test suites
- Centralized **configuration file** to manage all test settings and constants in one place

---

## Test Coverage & Result
| Test Case ID | Description |
|--------------|-------------|
| TC01 | Add new pet with custom name success |
| TC02 | Find pet by status success |
| TC03 | Find pet by ID success |

**Note:** *The Petstore API used in this project is a publicly available mocked service, which may occasionally return intermittent errors or unstable responses. To improve test reliability, a retry mechanism has been implemented to automatically reattempt failed API requests where applicable.*

<img width="983" alt="image" src="https://github.com/user-attachments/assets/8ec5dd90-fa24-45d0-a92f-802893f807de" />

---

## Tech Stack

### Core Testing
- Python 3.9+
- [Pytest](https://docs.pytest.org/en/stable/): Python testing framework for writing simple to scalable test cases
- [Requests](https://requests.readthedocs.io/en/latest/): HTTP library for sending API requests
- [Pydantic](https://docs.pydantic.dev/): Data validation and schema enforcement using Python type hints
- [pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures): Plugin to automatically rerun flaky tests

### Reporting
- [Allure Pytest](https://allurereport.org/): Plugin to generate detailed and interactive test reports

---

## Setup Instructions
Pre-Requisite:
- Python 3.9+
- Homebrew

#### 1. Clone the repo

```bash
git clone https://github.com/hengalvin/auto-pet-store.git
cd auto-pet-store
```

#### 2. Create virtual environment and install requirements

```bash
python -m venv venv
pip install -r requirements.txt
```

#### 3. Install Allure-CLI (optional, but recommended: if want to open allure report on the web)

```bash
brew install allure
```

---

## How to Run Tests

This project uses `pytest` for automated testing and integrates with Allure for test reporting. You can run all tests or a specific test suite using the command-line interface.

### Basic Command

To execute the test suite, use the following command from the project root directory:

```bash
python run_test.py
```

### Command-Line Options
| Argument          | Description                                                                                     | Example Usage                  |
| ----------------- | ----------------------------------------------------------------------------------------------- | ------------------------------ |
| `--path={path}`   | Run a specific test suite located at the given path. If omitted, all test suites will run.      | `--path=tests/api/add_new_pet` |
| `--create-report` | Generate an Allure report at the end of the test execution.                                     | `--create-report`              |
| `--open`          | Automatically open the generated Allure HTML report in the browser. Requires `--create-report`. | `--create-report --open`       |

⚠️ Note: The --open option requires the Allure CLI to be installed on your system.

<img width="1452" alt="image" src="https://github.com/user-attachments/assets/d3d2b9d1-04cd-4cb6-a0ab-9f181e0ede62" />


### Example Commands
**1. Run all tests, generate and open test result report:**
```bash
python run_test.py --create-report --open
```

**2. Run only a specific test suite:**
```bash
python run_test.py --path=tests/api/add_new_pet
```

**3. Run a specific suite, generate report only (don't open)**
```bash
python run_test.py --path=tests/api/add_new_pet --create-report --open
```
---

## Snapshots

**Custom info & error logs**
<img width="1319" alt="image" src="https://github.com/user-attachments/assets/1ad32646-d17b-4ea7-8774-0666952ff559" />


** Allure report graphs**
<img width="983" alt="image" src="https://github.com/user-attachments/assets/8b1d6282-2bc3-4d66-8977-889b21055c53" />

## Future Roadmap
This section outlines planned improvements and next steps to enhance this automation project:

### Deployment & Scheduling
- **Deploy test automation to a cloud service**
- **Schedule recurring test runs** (e.g., daily, hourly) to monitor system health over time

### Notifications & Insights
- **Integrate email or webhook notifications** to alert stakeholders on test results
- **Track test history and trend analysis** to evaluate long-term system stability and performance
