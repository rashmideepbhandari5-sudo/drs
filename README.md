# RASHMI Selenium Practice Project

This project is a small Selenium automation learning repository built in Python. It contains browser automation examples, page object model (POM) code, and login test cases for demo websites such as Demoblaze and Automation Testing.

## Overview

The repository is mainly used for learning and practicing:

- Selenium WebDriver basics
- Browser automation with Python
- Page Object Model structure
- Handling alerts and pop-ups
- Writing and running unit tests for frontend flows

## Project Structure

```text
RASHMI/
├── allclasscode/                 # Practice scripts and learning examples
│   ├── main.py
│   ├── AlertHandling.py
│   ├── prac.py
│   ├── Try_catch.py
│   ├── test_fail_or_pass.py
│   └── test_main.py             # Example unit test for a sample function
├── locator/                     # Locator constants
│   ├── __init__.py
│   └── Locater.py
├── pages/                       # Page objects
│   ├── __init__.py
│   └── LoginPage.py
├── testcases/                   # Automated test files
│   ├── __init__.py
│   └── test_login.py
├── .venv/                       # Virtual environment
├── README.md
└── .idea/                       # IDE settings
```

## Key Components

### `pages/LoginPage.py`
This file defines a `LoginPage` class that handles the login form actions on the demo login page.

It includes methods to:

- open the login modal
- enter username
- enter password
- click the login button
- perform the full login workflow

### `locator/Locater.py`
This file stores reusable UI element selectors such as:

- login button ID
- username field ID
- password field ID
- login button XPath

### `testcases/test_login.py`
This file contains Selenium-based login tests for a demo website.

It verifies:

- successful login with valid credentials
- failed login with invalid credentials

## Prerequisites

Before running the project, make sure you have:

- Python 3 installed
- Google Chrome installed
- ChromeDriver installed and available in PATH
- Selenium package installed

Install Selenium with:

```bash
pip install selenium
```

## Running the Tests

Run the test suite from the project root:

```bash
python -m unittest discover -s testcases
```

You can also run a specific test file directly:

```bash
python testcases/test_login.py
```

## Example Test Behavior

The login test opens the Demoblaze website, logs in with credentials, and verifies one of these:

- valid login shows a welcome message
- invalid login triggers an alert with the correct error text

## Notes

- This project is primarily for learning and practice.
- Some scripts in `allclasscode/` are examples rather than production-ready automation frameworks.
- The code uses direct Selenium calls and simple test structures, which are useful for understanding automation fundamentals.

## Suggested Next Improvements

- Add `requirements.txt`
- Use `pytest` instead of `unittest`
- Add WebDriver setup management
- Add better assertion messages and waits
- Create a more structured automation framework

## License

This repository is for educational and learning purposes.
