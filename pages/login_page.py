from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from utils.logger import get_logger

logger = get_logger()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.pin_input = (By.XPATH, "//input[@id='pin']")
        self.sign_in_button = (By.XPATH, "//button[@id='sign-in-button']")
        self.all_titles_button = (By.XPATH, "//button[@aria-label='All Titles']")  # Button to click
        self.all_titles_text = (By.XPATH, "//p[text()=' All Titles ']")  # Text to verify

    def enter_pin(self, pin, timeout=15):
        try:
            logger.info("Waiting for PIN input field to be visible...")
            pin_element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.pin_input)
            )
            pin_element.clear()
            pin_element.send_keys(pin)
            logger.info("✅ PIN entered successfully.")
            return True
        except Exception as e:
            logger.error(f"❌ Error entering PIN: {e}")
            return False

    def click_sign_in(self, timeout=15):
        try:
            logger.info("Waiting for Sign In button to be clickable...")
            button_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.sign_in_button)
            )
            button_element.click()
            logger.info("✅ Sign In button clicked successfully.")
            return True
        except Exception as e:
            logger.error(f"❌ Error clicking Sign In: {e}")
            return False

    def click_all_titles_button(self, timeout=15):
        """Click the 'All Titles' button."""
        try:
            logger.info("Waiting for 'All Titles' button to be clickable...")
            button_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.all_titles_button)
            )
            button_element.click()
            logger.info("✅ 'All Titles' button clicked successfully.")
            return True
        except Exception as e:
            logger.error(f"❌ Error clicking 'All Titles' button: {e}")
            return False

    def verify_all_titles_text(self, timeout=15):
        """Verify the 'All Titles' text appears."""
        try:
            logger.info("Waiting for 'All Titles' text to appear...")
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.all_titles_text)
            )
            logger.info("✅ 'All Titles' text is visible. Verification successful.")
            return True
        except Exception as e:
            logger.error(f"❌ 'All Titles' text not found: {e}")
            return False

    def login(self, pin, timeout=15):
        """
        Complete login flow:
        1. Enter PIN
        2. Click Sign In
        3. Click 'All Titles' button
        4. Verify 'All Titles' text
        """
        if self.enter_pin(pin, timeout) and self.click_sign_in(timeout):
            if self.click_all_titles_button(timeout):
                return self.verify_all_titles_text(timeout)
            else:
                logger.error("❌ Failed to click 'All Titles' button.")
                return False
        else:
            logger.error("❌ Login failed: PIN entry or Sign In failed.")
            return False
