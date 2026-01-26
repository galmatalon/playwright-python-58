# 🚀 Advanced Playwright-Python Automation Framework
### **Enterprise-Grade E2E Testing Solution**

[![Build & Test Status](https://github.com/galmatalon/playwright-python-58/actions/workflows/main.yml/badge.svg)](https://github.com/galmatalon/playwright-python-58/actions)
[![Playwright Version](https://img.shields.io/badge/Playwright-1.57.0-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/python/)
[![Python Version](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live-ff69b4?logo=allure&logoColor=white)](https://galmatalon.github.io/playwright-python-58/)

---

## 🌟 Overview
This repository showcases a high-performance, scalable, and robust automation framework designed for modern web applications. Utilizing the power of **Playwright** and **Python**, this project demonstrates industry best practices for E2E testing, including the Page Object Model (POM), CI/CD integration, and detailed visual reporting.

![Project Banner](https://img.freepik.com/free-vector/modern-desktop-with-data-visualization_23-2148281358.jpg?t=st=1715764000~exp=1715767600~hmac=a4b56c80b6f9f5b0f5b0f5b0f5b0f5b0f5b0f5b0f5b0f5b0f5b0f5b0f5b0f5b0)
*Note: A futuristic dashboard representing automation success, speed, and reliability.*

---

## 🎯 Project Goals
* **Reliability:** Minimize flakiness with Playwright's auto-wait and resilient selectors.
* **Speed:** Execute tests in parallel across multiple browser engines.
* **Transparency:** Provide stakeholders with crystal-clear Allure reports including screenshots and logs.
* **Continuous Integration:** Fully automated pipeline via GitHub Actions.

---

## 🛠️ Tech Stack
* **Language:** [Python 3.13+](https://www.python.org/)
* **Core Engine:** [Playwright](https://playwright.dev/python/) (Cross-browser: Chromium, Firefox, WebKit)
* **Test Runner:** [Pytest](https://docs.pytest.org/)
* **Reporting:** [Allure Report](https://docs.qameta.io/allure/)
* **CI/CD:** [GitHub Actions](https://github.com/features/actions)
* **Infrastructure:** Docker & XVFB (for headless Linux execution)

---

## 📊 Live Reports & Results
Every execution of our pipeline generates a comprehensive report. We use Allure to visualize test trends, durations, and failure points.

### **Latest Allure Dashboard**
[**🌐 View Live Allure Report**](https://galmatalon.github.io/playwright-python-58/)

> **Pro Tip:** You can see the full history of test runs under the **Actions** tab of this repository.

---

## 🏗️ Folder Structure
```bash
playwright-python-58/
├── .github/workflows/    # CI/CD Pipeline Definitions (GitHub Actions)
├── tests/                # Test Suite (Sanity, E2E, Regression)
│   └── test_sanity.py    # Core Sanity Tests
├── allure-results/       # Raw data for Allure reports
├── pytest.ini            # Pytest Configuration
├── requirements.txt      # Project Dependencies
└── README.md             # Project Documentation
