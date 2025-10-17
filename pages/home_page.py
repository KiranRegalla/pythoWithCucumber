from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from utils.logger import get_logger

logger = get_logger()


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def launch_url(self, url, timeout=15):
        """
        Launches the given URL and waits until the page is fully loaded.

        :param url: URL of the page to open
        :param timeout: Max time (in seconds) to wait for page load
        :return: True if successful, False otherwise
        """
        try:
            logger.info(f"Launching URL: {url}")
            self.driver.get(url)

            # Wait until document.readyState == 'complete'
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            logger.info(f"✅ Successfully loaded the URL: {url}")
            return True

        except TimeoutException:
            logger.error(f"❌ Page did not load within {timeout} seconds: {url}")
            return False

        except WebDriverException as e:
            logger.error(f"❌ WebDriverException occurred while loading URL: {e}")
            return False

        except Exception as e:
            logger.error(f"❌ Unexpected error occurred while launching URL: {e}")
            return False
