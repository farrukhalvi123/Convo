# Selenium BDD POM Automation Framework for Convo

## 🚀 Overview

This project implements a **Selenium-based automation framework** using the **Page Object Model (POM)** and **Behavior-Driven Development (BDD)** with `Behave`. It supports parallel execution, CI/CD integration with **GitHub Actions**, and **Allure Reports** for test reporting.

---

## 📌 Features

✅ **Selenium with Python** for browser automation\
✅ **Behave** for BDD-style test execution\
✅ **Page Object Model (POM)** for maintainable test scripts\
✅ **Allure Reports** for detailed test insights\
✅ **Parallel execution support**\
✅ **Headless mode in CI/CD** for smooth test runs

---

## 🛠️ Installation

### **1️⃣ Clone the Repository**

```sh
$ git clone https://github.com/farrukhalvi123/Convo
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**

```sh
$ python -m venv venv
$ source venv/bin/activate  # On macOS/Linux
$ venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**

```sh
$ pip install -r requirements.txt
```
```CICD
$ pip install -r requirements-ci.txt


---

## 🏃 Running Tests

### **Run All Tests**

```sh
$ behave
```

### **Run Specific Tagged Tests**

```sh
$ behave --tags=@Regression
```

### **Run Tests in Headless Mode (CI/CD)**

```sh
$ CI=true behave --tags=@Regression
```

---

## 🖥️ Project Structure

```
C│── features/
│   ├── steps/          # Step definitions
│   ├── pages/          # Page Object Model (POM) classes
│   ├── commons/        # Shared utilities
│   ├── config/         # Configuration files (YAML)
│   ├── reports/        # Test results & Allure reports
│   ├── environment.py  # Hooks (before/after scenario)
│   ├── example.feature # Sample BDD feature file
│
│── .github/workflows/  # CI/CD pipelines (GitHub Actions)
│── requirements.txt    # Python dependencies
│── README.md           # Documentation
```

---

## 🌍 CI/CD Integration (GitHub Actions)

This project is integrated with **GitHub Actions** to run tests automatically.

### **📜  GitHub Actions Workflow** (`.github/workflows/selenium-test.yml`)

```yaml
name: Selenium Tests

on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-ci.txt

      - name: Run Selenium tests and generate Allure report
        env:
          ENVIRONMENT: dev
        run: |
          behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results --tags=@Regression -D headless=true


      

      - name: Upload Allure Results
        uses: actions/upload-artifact@v4
        with:
          name: Allure-Results
          path: reports/allure-results

      - name: Upload Allure Report
        uses: actions/upload-artifact@v4
        with:
          name: Allure-Report
          path: reports/allure-report

```

---

## 📊 Generating Reports

### **Allure Reports (Recommended)**

```sh
$ behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
$ allure serve reports/allure-results
```



## 🏗️ Configurations

### **Modify Browser and Environment Settings** (`config/config_dev.yaml`)

```yaml
base_url: "https://the-internet.herokuapp.com"
browsers:
  - name: "chrome"
    headless: False




---

## 🎯 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b master`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push the branch (`git push origin feature-branch`)
5. Create a Pull Request

---

## 🛠️ Troubleshooting

### **Chrome WebDriver Errors**

```

### **Headless Mode Not Working?**

Try using `--headless=new` for newer Chrome versions.

```sh
$ behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results --tags=@Regression --headless
```


