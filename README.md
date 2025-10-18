This project automates the [FYC video platform](https://indeedemo-fyc.watch.indee.tv/) using **Python**, **Selenium**, and **Behave (BDD)**.  
It covers video selection, playback control, volume adjustment, resolution changes, and logout functionality.

---

## 📁 Project Structure
```
FYC_Automation/
│
├── features/
│   ├── video_playback.feature        # Feature file with Gherkin scenarios
│   ├── environment.py                # Behave hooks (setup & teardown)
│   ├── steps/
│   │   └── video_steps.py            # Step definitions
│   └── pages/
│       ├── base_page.py              # Common WebDriver utilities
│       ├── login_page.py             # Login Page actions
│       └── video_page.py             # Video Page actions
│
├── reports/                          # Allure report results (auto-generated)
├── run_tests.py                      # Behave runner with Allure integration
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

---

## ⚙️ Prerequisites

1. **Install Python 3.8+**
   ```bash
   python3 --version
   ```

2. **Install pip**
   ```bash
   python3 -m pip --version
   ```
   If missing:
   ```bash
   python3 -m ensurepip --upgrade
   ```

3. **Install Allure Command-Line Tool**
   - macOS:
     ```bash
     brew install allure
     ```
   - Windows:
     ```bash
     choco install allure-commandline
     ```

---

## 🧩 Installation Steps

1. Clone or download this repository:
   ```bash
   git clone https://github.com/KiranRegalla/pythoWithCucumber.git
   cd FYC_Automation
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```

3. Install required dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

   Or manually:
   ```bash
   python3 -m pip install selenium behave allure-behave webdriver-manager allure-pytest
   ```

---

## 🧠 Framework Highlights

✅ BDD Framework (Behave)  
✅ Page Object Model (POM)  
✅ Dynamic Waits with WebDriverWait  
✅ Error Handling & Logging  
✅ WebDriver Manager (no .exe needed)  
✅ Allure Reporting with Tags  
✅ Run tests on GitHub Actions (cloud/CI)  
✅ View latest Allure report online: [https://kiranregalla.github.io/pythoWithCucumber/](https://kiranregalla.github.io/pythoWithCucumber/) 

---

## 🚀 Running Tests

## On git hub actions

Click on the Actions tab in the top menu.
Select any one of the workflow.
Click Re-Run workflow to trigger the tests manually.
Wait for the workflow to complete. The logs will show test execution details, including passed and failed scenarios.
Get Allure reports as an artifact, download them from the Artifacts section to view the full report.

---
### Run All Tests
```bash
python run_tests.py
```

This executes all scenarios tagged as @video and generates Allure reports.

### Run with Specific Tags
```bash
behave --tags=@login
```
### Please find the live reports after every remote run on git hub actions
https://kiranregalla.github.io/pythoWithCucumber/ 

### Manually View Allure Report
```bash
allure serve reports/
```
---
---

## 🏗️ Tag Usage (Feature File Example)
```gherkin
@video @smoke
Feature: Automate Video Playback and Control

  @login
  Scenario: User logs in with valid PIN
    Given user launches the FYC platform
    When user enters the valid PIN
    Then user should be logged in successfully
```

Run with:
```bash
behave --tags=@login
```

---

## 🧾 Error Handling

- Try/Except for Selenium actions  
- Descriptive error logs  
- Safe teardown (`driver.quit()`)  

---

## 📊 Allure Reporting

Integrated Allure support via `allure-behave`:
```bash
-f allure_behave.formatter:AllureFormatter -o reports/
```
Generates and opens HTML report automatically via:
```bash
python run_tests.py
```

---
## 👨‍💻 Author
**Name:** Kiran Kumar  
**Role:** QA Automation Engineer  
**Tools Used:** Python, Selenium, Behave, WebDriver Manager, Allure Reports  
**Platform Tested:** [https://indeedemo-fyc.watch.indee.tv/](https://indeedemo-fyc.watch.indee.tv/)
