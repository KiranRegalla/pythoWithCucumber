# automation_page.py
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from utils.logger import get_logger

logger = get_logger()

class AutomationPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the Automation project title
        self.automation_project_title = (By.XPATH, "//h5[text()='Test automation project']")
        # Locator for the Details section link
        self.details_section_link = (By.XPATH, "//a[@id='detailsSection']")
        # Locator for 'Accept All' button
        self.accept_all_button = (By.XPATH, "(//button[text()='Accept All'])[1]")
        self.iframe_xpath = (By.XPATH, "//iframe[@id='video_player']")
        self.settings_button = (By.XPATH, "(//div[@aria-label='Settings'])[2]")
        self.resolution_480_button = (By.XPATH, "//button[text()='480p']")
        self.resolution_720_button = (By.XPATH, "//button[text()='720p']")

    def click_accept_all_button(self, timeout=10):
        """
        Click on 'Accept All' button if it appears.
        """
        try:
            logger.info("Waiting for 'Accept All' button to be clickable...")
            button_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.accept_all_button)
            )
            button_element.click()
            logger.info("✅ 'Accept All' button clicked successfully.")
            return True
        except TimeoutException:
            logger.info("ℹ️ 'Accept All' button not found or already accepted, skipping.")
            return False
        except Exception as e:
            logger.error(f"❌ Error clicking 'Accept All' button: {e}")
            return False

    def click_automation_project_title(self, timeout=15):
        """
        Click 'Accept All' button first if it exists, then scroll to and click
        on 'Test automation project' title using Selenium click.
        """

        try:
            logger.info("Waiting for 'Test automation project' title to be clickable...")
            title_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.automation_project_title)
            )

            # Scroll the element into view
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", title_element
            )
            logger.info("Scrolled to 'Test automation project' title.")

            # Click the element
            title_element.click()
            logger.info("✅ 'Test automation project' title clicked successfully.")
            return True

        except TimeoutException:
            logger.error("❌ Timeout: 'Test automation project' title not clickable.")
            return False
        except NoSuchElementException:
            logger.error("❌ 'Test automation project' title not found on the page.")
            return False
        except WebDriverException as e:
            logger.error(f"❌ WebDriverException occurred while clicking title: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error clicking 'Test automation project' title: {e}")
            return False

    def click_details_section(self, timeout=15):
        """
        Scroll to and click on the 'Details' section link using Selenium click.
        Waits until the element is clickable, then pauses for 5 seconds.
        """
        try:
            logger.info("Waiting for 'Details' section link to be clickable...")
            details_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.details_section_link)
            )

            # Scroll the element into view
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", details_element
            )
            logger.info("Scrolled to 'Details' section link.")

            # Click the element
            details_element.click()
            logger.info("✅ 'Details' section link clicked successfully.")

            # Wait for 5 seconds
            time.sleep(5)
            logger.info("Waited 5 seconds after clicking 'Details' section link.")

            return True

        except TimeoutException:
            logger.error("❌ Timeout: 'Details' section link not clickable.")
            return False
        except NoSuchElementException:
            logger.error("❌ 'Details' section link not found on the page.")
            return False
        except WebDriverException as e:
            logger.error(f"❌ WebDriverException occurred while clicking 'Details' link: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error clicking 'Details' section link: {e}")
            return False

    def click_video_section(self, timeout=15):
        """
        Scroll to and click on the 'Video' section link using Selenium click.
        Waits until the element is clickable.
        """
        video_section_link = (By.XPATH, "//a[@id='videosSection']")

        try:
            logger.info("Waiting for 'Video' section link to be clickable...")
            video_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(video_section_link)
            )

            # Scroll the element into view
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", video_element
            )
            logger.info("Scrolled to 'Video' section link.")

            # Click the element
            video_element.click()
            logger.info("✅ 'Video' section link clicked successfully.")

            # Optional wait after clicking (if needed)
            time.sleep(5)
            logger.info("Waited 5 seconds after clicking 'Video' section link.")

            return True

        except TimeoutException:
            logger.error("❌ Timeout: 'Video' section link not clickable.")
            return False
        except NoSuchElementException:
            logger.error("❌ 'Video' section link not found on the page.")
            return False
        except WebDriverException as e:
            logger.error(f"❌ WebDriverException occurred while clicking 'Video' link: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error clicking 'Video' section link: {e}")
            return False

    def play_first_video(self, timeout=15):
        """
        Scroll to the 'Remaining Views' element and click on the first 'Play Video' button.
        """
        remaining_views = (By.XPATH, "//span[text()='Remaining Views: ']")
        play_button = (By.XPATH, "//button[@aria-label='Play Video']")

        try:
            # Wait for the remaining views element and scroll to it
            logger.info("Waiting for 'Remaining Views' element to be visible...")
            views_element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(remaining_views)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", views_element
            )
            logger.info("Scrolled to 'Remaining Views' element.")

            # Wait for the play button to be clickable and click it
            logger.info("Waiting for 'Play Video' button to be clickable...")
            play_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(play_button)
            )
            play_element.click()
            time.sleep(15)
            logger.info("✅ 'Play Video' button clicked successfully.")

            return True

        except TimeoutException:
            logger.error("❌ Timeout: 'Remaining Views' or 'Play Video' button not available.")
            return False
        except NoSuchElementException:
            logger.error("❌ 'Remaining Views' or 'Play Video' button not found on the page.")
            return False
        except WebDriverException as e:
            logger.error(f"❌ WebDriverException occurred while clicking 'Play Video': {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error in play_first_video: {e}")
            return False

    def pause_html5_video(self):
        """
        Switch to the video iframe and pause the HTML5 video inside it.
        Does NOT switch back to the default content.
        """
        try:
            # Declare iframe XPath inside the method


            logger.info("Waiting for and switching to the video iframe...")
            iframe_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.iframe_xpath)
            )
            self.driver.switch_to.frame(iframe_element)
            logger.info("✅ Switched to video iframe successfully.")

            # Locate the HTML5 video and pause it
            video_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )
            self.driver.execute_script("arguments[0].pause();", video_element)
            logger.info("✅ Video paused successfully inside the iframe.")
            time.sleep(10)
            return True

        except TimeoutException:
            logger.error("❌ Timeout: iframe or video element not found.")
            return False
        except NoSuchElementException:
            logger.error("❌ Video element not found inside the iframe.")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error while pausing video in iframe: {e}")
            return False

    def play_html5_video(self):
        """
        Resume (play) the HTML5 video inside the iframe.
        Assumes the driver is already switched to the iframe.
        """
        try:
            logger.info("Waiting for the HTML5 video element to be present...")
            # Locate the HTML5 video and play it
            video_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )
            self.driver.execute_script("arguments[0].play();", video_element)
            time.sleep(10)  # Optional: let the video play for 10 seconds
            logger.info("✅ Video resumed (playing) successfully inside the iframe.")
            return True

        except TimeoutException:
            logger.error("❌ Timeout: video element not found inside the iframe.")
            return False
        except NoSuchElementException:
            logger.error("❌ Video element not found inside the iframe.")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error while resuming video in iframe: {e}")
            return False

    def set_video_volume_to_50(self):
        """
        Set the volume of the HTML5 video to 50%.
        Assumes the driver is already switched to the iframe containing the video.
        """
        try:
            logger.info("Waiting for the HTML5 video element to be present for volume adjustment...")
            video_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )

            # Set volume to 50%
            self.driver.execute_script("arguments[0].volume = 0.5;", video_element)
            logger.info("✅ Video volume set to 50% successfully.")
            time.sleep(10)
            return True

        except TimeoutException:
            logger.error("❌ Timeout: video element not found for setting volume.")
            return False
        except NoSuchElementException:
            logger.error("❌ Video element not found for setting volume.")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error while setting video volume: {e}")
            return False

    def change_resolution_480_to_720_via_settings(self):
        """
        Change video resolution from 480p to 720p using the Settings button via JavaScript clicks.
        Assumes the driver is already inside the iframe containing the video.
        """
        try:
            # Hover element (video control bar)
            hover_element_xpath = "//div[@class='jw-controlbar jw-reset']"

            # ------------------ First Settings Click ------------------
            logger.info("Hovering over the video control bar before first Settings click...")
            hover_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, hover_element_xpath))
            )
            ActionChains(self.driver).move_to_element(hover_element).perform()
            logger.info("✅ Hover performed successfully.")

            # Click the Settings button normally
            logger.info("Clicking the 'Settings' button (first time)...")
            settings_elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.settings_button)
            )
            settings_elem.click()
            logger.info("✅ 'Settings' button clicked.")
            time.sleep(10)

            # Select 480p normally
            logger.info("Selecting 480p resolution...")
            button_480 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.resolution_480_button)
            )
            button_480.click()
            logger.info("✅ 480p selected. Waiting 10 seconds...")
            time.sleep(10)

            # ------------------ Second Settings Click ------------------
            logger.info("Hovering over the video control bar before second Settings click...")
            hover_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, hover_element_xpath))
            )
            ActionChains(self.driver).move_to_element(hover_element).perform()
            logger.info("✅ Hover performed successfully.")

            # Click Settings again normally
            logger.info("Clicking the 'Settings' button (second time)...")
            settings_elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.settings_button)
            )
            settings_elem.click()
            logger.info("✅ 'Settings' button clicked again.")
            time.sleep(10)

            # Select 720p normally
            logger.info("Selecting 720p resolution...")
            button_720 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.resolution_720_button)
            )
            button_720.click()
            logger.info("✅ 720p selected. Waiting 10 seconds...")
            time.sleep(10)

            self.driver.switch_to.default_content()
            logger.info("✅ Switched back to default content from iframe.")

            return True

        except TimeoutException:
            logger.error("❌ Timeout: Hover element, Settings, or resolution button not found/clickable.")
            return False
        except NoSuchElementException:
            logger.error("❌ Hover element, Settings, or resolution button not found on the page.")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error while changing video resolution: {e}")
            return False

    def navigate_back(self):
        """
        Navigate back to the previous page using Selenium's navigate.back() equivalent.
        """
        try:
            logger.info("Navigating back to the previous page...")
            self.driver.back()
            time.sleep(5)  # Optional: wait for 5 seconds to allow page to load
            logger.info("✅ Successfully navigated back to the previous page.")
            return True
        except WebDriverException as e:
            logger.error(f"❌ WebDriverException occurred while navigating back: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error while navigating back: {e}")
            return False

    def click_logout_button(self, timeout=10):
        """
        Hover over and click the 'Logout' button in the sidebar.
        """
        logout_button_xpath = "//a[@id='signOutSideBar']"

        try:
            logger.info("Waiting for the 'Logout' button to be visible and hoverable...")
            logout_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, logout_button_xpath))
            )

            # Hover over the logout button
            ActionChains(self.driver).move_to_element(logout_element).perform()
            logger.info("✅ Hovered over the 'Logout' button.")

            # Click the logout button
            logout_element.click()
            logger.info("✅ 'Logout' button clicked successfully.")
            return True

        except TimeoutException:
            logger.error("❌ Timeout: 'Logout' button not found or not clickable.")
            return False
        except NoSuchElementException:
            logger.error("❌ 'Logout' button not found on the page.")
            return False
        except WebDriverException as e:
            logger.error(f"❌ WebDriverException occurred while clicking 'Logout': {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Unexpected error while clicking 'Logout' button: {e}")
            return False
