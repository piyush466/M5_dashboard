# M5 Dashboard Automation Framework

## Overview

This project is an end-to-end UI automation framework developed using **Python**, **Selenium WebDriver**, and **Pytest** for automating the M5 Dashboard application.

The framework follows the **Page Object Model (POM)** design pattern to improve code reusability, readability, and maintainability.

---

## Tech Stack

- Python 3.x
- Selenium WebDriver
- Pytest
- Faker
- OpenPyXL
- WebDriver Manager
- Page Object Model (POM)

---

## Project Structure

```
M5_dashboard/
│
├── new_pages/
│   ├── dashboard/
│   ├── login_page1.py
│   ├── dashboard_page1.py
│   └── ...
│
├── test_cases/
│   ├── test_dashboard/
│   └── ...
│
├── utilities/
│   ├── configpar.py
│   ├── logger.py
│   └── ...
│
├── uihelper/
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
├── pytest.ini
├── conftest.py
└── README.md
```

---

## Features

- Page Object Model (POM)
- Explicit Waits
- Reusable Utility Methods
- Logging Support
- Configuration File Support
- Cross Browser Support (if configured)
- Screenshot on Failure (if implemented)
- Excel File Validation
- Download Verification
- Dynamic XPath Handling

---

## Prerequisites

- Python 3.9 or above
- Google Chrome
- ChromeDriver (or WebDriver Manager)
- Git

---

## Installation

Clone the repository

```bash
git clone https://github.com/piyush466/M5_dashboard.git
```

Navigate to the project directory

```bash
cd M5_dashboard
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all test cases

```bash
pytest
```

Run a specific test file

```bash
pytest test_cases/test_dashboard/test_client_need_attention.py
```

Run with verbose output

```bash
pytest -v
```

Run a specific test case

```bash
pytest -k "test_01_verify_all_columns_are_displayed"
```

Generate HTML Report (if pytest-html is installed)

```bash
pytest --html=Reports/report.html --self-contained-html
```

---

## Framework Design

The framework follows the Page Object Model (POM).

- Test scripts contain only test logic.
- Page classes contain web element locators and actions.
- Utility classes contain reusable helper methods.
- Configuration values are managed using configuration files.
- Logging is implemented for easier debugging.

---

## Test Coverage

Current automation includes:

- Login
- Dashboard Validation
- Client Need Attention Widget
- Dropdown Validation
- Search Functionality
- Excel Download Validation
- Pagination Validation
- Take Action Navigation
- Status Validation Based on Expiry Date

---

## Best Practices

- Keep locators inside Page Classes.
- Use Explicit Waits instead of Sleep.
- Avoid hardcoded test data.
- Keep test cases independent.
- Follow naming conventions for test methods.

---

## Author

**Piyush Shdravyakar**

QA Automation Engineer

GitHub: https://github.com/piyush466

---

## License

This project is created for automation learning and demonstration purposes.