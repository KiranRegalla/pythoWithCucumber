import time
import allure
from behave import given, when, then
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.automation_page import AutomationPage
from utils.logger import get_logger

logger = get_logger()


@given("I launch the FYC application")
@allure.step("Launching the FYC application")
def step_launch_app(context):
    try:
        context.home_page = HomePage(context.driver)
        context.home_page.launch_url('https://indeedemo-fyc.watch.indee.tv/login', timeout=15)
    finally:
        screenshot_path = f"screenshots/launch_app_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="launch_app", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: launch application")


@when('I sign in using PIN "{pin}"')
@allure.step('Logging in with "{pin}"')
def step_login(context, pin):
    try:
        context.login_page = LoginPage(context.driver)
        context.login_page.login(pin, timeout=15)
    finally:
        screenshot_path = f"screenshots/login_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="login_step", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: login")


@then('I navigate to "{project_name}"')
@allure.step("Navigating to the project")
def step_open_project(context, project_name):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.click_automation_project_title()
    finally:
        screenshot_path = f"screenshots/open_project_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="open_project", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: open project")


@then("I switch to Details tab and wait for few seconds")
@allure.step("Switching to Details tab")
def step_details_tab(context):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.click_details_section(timeout=15)
    finally:
        screenshot_path = f"screenshots/details_tab_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="details_tab", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: details tab")


@then("I return to Videos tab")
@allure.step("Returning to Videos tab")
def step_videos_tab(context):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.click_video_section()
    finally:
        screenshot_path = f"screenshots/videos_tab_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="videos_tab", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: videos tab")


@then("I play the video for 10 seconds and pause")
@allure.step("Playing the video for 10 seconds")
def step_play_video(context):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.play_first_video()
        context.automation_page.pause_html5_video()
    finally:
        screenshot_path = f"screenshots/play_video_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="play_video", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: play video")


@then("I resume playback using Continue Watching button")
@allure.step("Resuming playback")
def step_resume_video(context):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.play_html5_video()
    finally:
        screenshot_path = f"screenshots/resume_video_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="resume_video", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: resume video")


@then("I set video volume to 50 percent")
@allure.step("Adjusting video volume")
def step_volume(context):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.set_video_volume_to_50()
    finally:
        screenshot_path = f"screenshots/volume_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="volume_adjust", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: volume adjustment")


@then("I change video resolution to 480p and then back to 720p")
@allure.step("Changing video resolution")
def step_resolution(context):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.change_resolution_480_to_720_via_settings()
    finally:
        screenshot_path = f"screenshots/resolution_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="change_resolution", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: change resolution")


@then("I pause video and exit project")
@allure.step("Pausing and exiting project")
def step_exit(context):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.pause_html5_video()
        context.automation_page.navigate_back()
    finally:
        screenshot_path = f"screenshots/exit_project_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="exit_project", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: exit project")


@then("I logout from the platform")
@allure.step("Logging out from the platform")
def step_logout(context):
    try:
        context.automation_page = AutomationPage(context.driver)
        context.automation_page.click_logout_button()
    finally:
        screenshot_path = f"screenshots/logout_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="logout_step", attachment_type=allure.attachment_type.PNG)
        logger.info("✅ Screenshot captured for step: logout")
