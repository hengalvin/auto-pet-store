# 🐾 Auto-Pet-Store API Test Automation

Automated test suite for the [Swagger Petstore API](https://petstore.swagger.io/), built using **Pytest**, with **schema validation** via **Pydantic**, and beautiful **Allure reports**.

---

## 📌 Features

- ✅ Modular test structure using **Pytest**
- ✅ Reusable, abstracted **API client**
- ✅ **Schema validation** with Pydantic
- ✅ Integrated **Allure reporting**
- ✅ Environment variable support for flexible test configs
- ✅ Custom logging for request/response debugging

---

## 🧪 Test Coverage

| Test Case ID | Description |
|--------------|-------------|
| TC01 | Create a new pet named `Cat1` and verify it was created |
| TC02 | Create a new pet named `Cat2` and verify it was created |
| TC03 | Retrieve pets with status `available` and validate all match |
| TC04 | Retrieve pets with status `pending` and validate all match |
| TC05 | Get pet by ID (e.g. `2`) and validate schema compliance |

---

## 🧰 Tech Stack

- Python 3.9+
- [Pytest](https://docs.pytest.org/)
- [Requests](https://docs.python-requests.org/)
- [Pydantic](https://docs.pydantic.dev/) (v2) – for response schema validation
- [Allure-Pytest](https://docs.qameta.io/allure/) – for test reporting

---

## ⚙️ Setup Instructions

### 1. 📦 Clone the repo

```bash
git clone https://github.com/your-username/auto-pet-store.git
cd auto-pet-store
pip install -r requirements.txt