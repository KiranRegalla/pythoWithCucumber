import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from utils.logger import get_logger

logger = get_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            logger.info(f"Clicked element {locator}")
            allure.step(f"Clicked element {locator}")
        except (TimeoutException, ElementClickInterceptedException) as e:
            logger.error(f"Failed to click {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            elem = self.wait.until(EC.visibility_of_element_located(locator))
            elem.clear()
            elem.send_keys(text)
            logger.info(f"Entered text in {locator}")
            allure.step(f"Entered text in {locator}")
        except TimeoutException as e:
            logger.error(f"Failed to send keys to {locator}: {e}")
            raise

    def get_element(self, locator):
        try:
            elem = self.wait.until(EC.presence_of_element_located(locator))
            return elem
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Element not found: {locator} - {e}")
            raise
