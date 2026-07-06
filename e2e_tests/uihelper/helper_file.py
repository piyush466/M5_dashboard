from bs4 import element
from faker import Faker
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from datetime import datetime
from logger.logger_file import setup_logger


class UI_Helper:
    log = setup_logger()

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def random_text():
        try:
            value = random.randint(1, 9000000)
            UI_Helper.log.info(f"Generated random value: {value}")
            return value
        except Exception as e:
            UI_Helper.log.error(f"Error generating random value: {e}")

    def take_screenshot(self):
        date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshot_{date_str}.png"
        save_path = fr".//screenshots//{screenshot_name}"
        self.driver.save_screenshot(save_path)
        self.log.info(f"Screenshot saved to: {save_path}")

    def do_click(self, by_locator):
        try:
            self.log.info(f"Attempting to click on element: {by_locator}")
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).click()
            self.log.info(f"Clicked on element: {by_locator}")
        except Exception as e:
            self.log.error(f"Failed to click on element {by_locator}: {e}")
            raise  # Re-raise the exception so the test fails


    def send_key(self, by_locator, text):
        try:
            self.log.info(f"Sending keys '{text}' to element: {by_locator}")
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys(text)
            self.log.info(f"Keys sent to element: {by_locator}")
        except Exception as e:
            self.log.error(f"Failed to send keys to {by_locator}: {e}")
            raise  # Re-raise the exception so the test fails

    def get_title(self):
        try:
            title = self.driver.title
            self.log.info(f"Page title retrieved: {title}")
            return title
        except Exception as e:
            self.log.error(f"Error getting page title: {e}")

    def drop_down(self, by_locator, value):
        try:
            self.log.info(f"Selecting value '{value}' from dropdown: {by_locator}")
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
            select = Select(element)
            select.select_by_value(value)
            self.log.info(f"Selected value '{value}' from dropdown: {by_locator}")
        except Exception as e:
            self.log.error(f"Failed to select dropdown value '{value}' from {by_locator}: {e}")

    def get_text(self, by_locator):
        try:
            self.log.info(f"Getting text from element: {by_locator}")
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            text = element.text
            self.log.info(f"Retrieved text: '{text}' from element: {by_locator}")
            return text
        except Exception as e:
            self.log.error(f"Failed to get text from element {by_locator}: {e}")

    def is_selected(self, by_locator):
        try:
            self.log.info(f"Checking if element is selected: {by_locator}")
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).is_selected()
            self.log.info(f"Element is selected: {by_locator}")
            return element
        except Exception as e:
            self.log.error(f"Failed to check selected status: {by_locator}: {e}")
            raise

    def is_displayed(self, by_locator):
        try:
            self.log.info(f"Checking if element is displayed: {by_locator}")
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
            self.log.info(f"Element displayed status: {element}")
            return element
        except Exception as e:
            self.log.error(f"Failed to check display status of element {by_locator}: {e}")
            raise


    def is_enable(self, by_locator):
        try:
            self.log.info(f"Checking if element is enabled: {by_locator}")
            element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).is_enabled()
            self.log.info(f"Element enabled status: {element}")
            return element
        except Exception as e:
            self.log.error(f"Failed to check enable status of element {by_locator}: {e}")

    def assertion(self, actual_result, expected_result):
        try:
            self.log.info(f"Asserting values - Actual: {actual_result}, Expected: {expected_result}")
            assert actual_result == expected_result, f"Assertion failed: Actual '{actual_result}' does not match Expected '{expected_result}'"
            self.log.info("Assertion passed.")
            self.take_screenshot()
        except Exception as e:
            self.log.error(f"Assertion failed: {e}")
            self.take_screenshot()
            raise  # Re-raise the exception so the test fails

    def is_element_present(self, by_locator):
        try:
            self.log.info(f"Checking if element is present: {by_locator}")
            WebDriverWait(self.driver, 17).until(EC.presence_of_element_located(by_locator))
            self.log.info(f"Element is present: {by_locator}")
        except Exception as e:
            self.log.error(f"Element not present: {by_locator} - Error: {e}")
            raise  # Re-raise the exception so the test fails

    def js_click(self, by_locator):
        try:
            self.log.info(f"Performing JS click on element: {by_locator}")
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
            self.log.info(f"JS click executed on element: {by_locator}")
        except Exception as e:
            self.log.error(f"JS click failed on element {by_locator}: {e}")
            raise

    def scroll_down_toElement(self, by_locator):
        try:
            self.log.info(f"Scrolling to element: {by_locator}")
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.log.info(f"Scrolled to element: {by_locator}")
        except Exception as e:
            self.log.error(f"Failed to scroll to element {by_locator}: {e}")
            raise

    def hover_onElement(self, by_locator):
        action = ActionChains(self.driver)
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return action.move_to_element(element).perform()

    def assert_In(self, expected_result, actual_result):
        try:
            self.log.info(f"Asserting values - Actual: {actual_result}, Expected: {expected_result}")
            assert expected_result in actual_result, f"Assertion failed: Expected '{expected_result}' not found in Actual '{actual_result}'"
            self.log.info("Assertion passed.")
        except Exception as e:
            self.log.error(f"Assertion failed: {e}")
            raise  # Re-raise the exception so the test fails

    def assert_not_equal(self, expected_result, actual_result):
        try:
            self.log.info(f"Asserting values - Actual: {actual_result}, Expected: {expected_result}")
            assert expected_result != actual_result, f"Assertion failed: Expected '{expected_result}' not found in Actual '{actual_result}'"
            self.log.info("Assertion passed.")
        except Exception as e:
            self.log.error(f"Assertion failed: {e}")
            raise  # Re-raise the exception so the test fails


    def get_attribute(self,by_locator,attribute):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator)).get_attribute(attribute)
        return element

    def clear_text(self, by_locator):
        element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located(by_locator)).clear()
        return element

    @staticmethod
    def fake_name():
        faker = Faker()
        return faker.name()

    def get_length(self, by_locator):
        return len(WebDriverWait(self.driver,10,).until(EC.visibility_of_all_elements_located(by_locator)))

    def until_clickable(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()

    def wait_until_loader_disappears(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(by_locator))

    def wait_until_displayed(self,by_locator):
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(by_locator))

    def get_currnt_time(self):
        from datetime import datetime

        current_date = datetime.now().strftime("%d%m%Y")
        return current_date