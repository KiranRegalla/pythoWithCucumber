import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger
import os
import time
import tempfile

logger = get_logger()

def before_all(context):
    try:
        options = Options()
        options.add_argument("--start-maximized")

        # Headless mode (needed for GitHub Actions)
        options.add_argument("--headless=new")  # for Chrome 109+ use --headless=new
        options.add_argument("--no-sandbox")  # required for many CI environments
        options.add_argument("--disable-dev-shm-usage")  # avoid /dev/shm issues
        options.add_argument("--disable-gpu")  # for headless stability

        # Create a unique temporary directory for Chrome profile
        temp_profile_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={temp_profile_dir}")

        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        context.driver.implicitly_wait(10)
        logger.info("Browser launched successfully")

        # Clear all cookies
        with allure.step("Clearing all browser cookies"):
            context.driver.delete_all_cookies()
            logger.info("✅ All browser cookies cleared successfully")

        # Accept cookies if banner appears
        accept_cookies(context)

    except Exception as e:
        logger.error(f"Failed to start browser: {e}")
        raise
def accept_cookies(context, timeout=10):
    """
    Accept cookies by clicking the 'Accept All' button if it appears.
    """
    try:
        # Replace this XPATH with the actual button text/ID from your site
        accept_button = (By.XPATH, "//button[text()='Accept All']")

        logger.info("Waiting for 'Accept All Cookies' button...")
        button_element = WebDriverWait(context.driver, timeout).until(
            EC.element_to_be_clickable(accept_button)
        )
        button_element.click()
        logger.info("✅ 'Accept All Cookies' button clicked successfully.")
        return True
    except TimeoutException:
        logger.info("ℹ️ 'Accept All Cookies' button not found, skipping.")
        return False
    except Exception as e:
        logger.error(f"❌ Error clicking 'Accept All Cookies' button: {e}")
        return False

def after_step(context, step):
    """Capture screenshot if any step fails."""
    if step.status == "failed":
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        filename = f"{step.name}_{int(time.time())}.png"
        filepath = os.path.join(screenshots_dir, filename)
        context.driver.save_screenshot(filepath)
        allure.attach.file(filepath, name=step.name, attachment_type=allure.attachment_type.PNG)
        logger.error(f"Step failed: {step.name}, screenshot saved at {filepath}")

def after_all(context):
    try:
#        context.driver.quit()
        logger.info("Browser closed successfully")
    except Exception as e:
        logger.error(f"Error closing browser: {e}")
