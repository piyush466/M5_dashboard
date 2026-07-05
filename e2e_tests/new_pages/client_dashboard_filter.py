import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from uihelper.helper_file import UI_Helper

class ClientDashboard_Filter(UI_Helper):
    # CLICK_ON_CLIENT_NAME = (By.XPATH, "//*[text()='piyush  piyush-30_06']")
    CLICK_ON_CLIENT_NAME = (By.XPATH, "//*[text()='piyush Dravyakar-999']")
    CLICK_ON_ASSET_FILTER_XPATH = (By.XPATH, "//*[contains(text(),'Asset/Subasset Filter')]")
    VERIFY_LENGH_OF_CHECK_BOX_XPATH = (By.XPATH, "//button[@role='checkbox']")
    ENTER_FILTER_NAME_IN_TEXTBOX_CSS = (By.CSS_SELECTOR, "input.flex.h-9.w-full.flex-1")
    CLICK_ON_SAVE_BUTTON_CSS = (By.CSS_SELECTOR, "button.inline-flex.self-start")
    VERIFY_SAVED_MESSAGE_DISPLAYED_XPATH = (By.XPATH, "//*[text()='Filter saved successfully']")
    CLICK_ON_SAVED_FILTER_XPATH = (By.CSS_SELECTOR, "button.inline-flex.items-center.flex-1:nth-of-type(2)")
    DELETE_CREATED_FILTER_XPATH = (By.XPATH, "//button[@aria-label='Delete']")
    VERIFY_FILTER_DELETE_XPATH = (By.XPATH, "//*[text()='Filter deleted successfully']")
    CLICK_ON_EDIT_BUTTON_XPAATH = (By.XPATH, "//button[@aria-label='Edit']")
    VERIFY_FILTER_UPDATE_XPATH = (By.XPATH, "//*[text()='Filter updated successfully']")
    WAIT_FOR_LOADER_DISAPPEAR_XPATH = (By.XPATH, "//*[@alt='Loading content']")
    CLICK_ON_MAKE_PRIMARY_BUTTON_XPATH = (By.XPATH, "//button[@aria-label='Set as Primary']")
    CLICK_ON_MAKE_PRIMARY_FOR_CLIENT_BUTTON_XPATH = (By.XPATH, "//button[@aria-label='Set as Primary for Client']")
    CLICK_ON_SET_PRIMARY_XPATH = (By.XPATH, "//button[text()='Set as Primary']")
    CLICK_ON_LOGOUT_ID = (By.ID, "logout-button")
    GET_PORTFOLI0_NET_VALUE_XPATH = (By.XPATH, "//*[contains(text(),'Portfolio Value (Net)')]//ancestor::div[3]/div[2]/button/h2")
    REMOVE_MULTI_ASSET_ALTERNATIVE_INVESTMENT_XPATH = (By.XPATH, "//*[contains(text(),'Multi-Asset & Alternative Investments')]//parent::label/button")
    CLICK_ON_APPLY_FILTER_BUTTON_XPATH = (By.XPATH, "//*[contains(text(),'Apply Filters')]")

    def __init__(self,driver):
        self.driver = driver

    def navigate_client_dashboard(self):
        self.scroll_down_toElement(self.CLICK_ON_CLIENT_NAME)
        self.js_click(self.CLICK_ON_CLIENT_NAME)

    def open_asset_filter(self):
        self.wait_until_loader_disappears(self.WAIT_FOR_LOADER_DISAPPEAR_XPATH)
        self.js_click(self.CLICK_ON_ASSET_FILTER_XPATH)

    def create_new_filter(self,filter_name):
        self.clear_text(self.ENTER_FILTER_NAME_IN_TEXTBOX_CSS)
        time.sleep(2)
        self.send_key(self.ENTER_FILTER_NAME_IN_TEXTBOX_CSS, filter_name)
        self.do_click(self.CLICK_ON_SAVE_BUTTON_CSS)


    def delete_create_filter(self, filter_name):
        self.is_displayed(self.CLICK_ON_SAVED_FILTER_XPATH)
        saved_filter_button = self.driver.find_element(By.CSS_SELECTOR, "button.inline-flex.items-center.flex-1:nth-of-type(2)")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", saved_filter_button)
        time.sleep(5)
        self.until_clickable(self.CLICK_ON_SAVED_FILTER_XPATH)
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,f"//*[text()='{filter_name}']")))
        element.click()
        self.scroll_down_toElement((By.XPATH,f"//*[text()='{filter_name}']"))
        self.do_click(self.DELETE_CREATED_FILTER_XPATH)

    def update_created_filter(self, createdfilter_name, filter_name):
        self.is_displayed(self.CLICK_ON_SAVED_FILTER_XPATH)
        saved_filter_button = self.driver.find_element(By.CSS_SELECTOR,
                                                       "button.inline-flex.items-center.flex-1:nth-of-type(2)")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", saved_filter_button)
        time.sleep(5)
        self.until_clickable(self.CLICK_ON_SAVED_FILTER_XPATH)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,f"//*[text()='{createdfilter_name}']"))).click()
        self.do_click(self.CLICK_ON_EDIT_BUTTON_XPAATH)
        self.create_new_filter(filter_name)

    def make_primary_filter(self, createdfilter_name):
        self.is_displayed(self.CLICK_ON_SAVED_FILTER_XPATH)
        saved_filter_button = self.driver.find_element(By.CSS_SELECTOR,
                                                       "button.inline-flex.items-center.flex-1:nth-of-type(2)")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", saved_filter_button)
        time.sleep(5)
        self.until_clickable(self.CLICK_ON_SAVED_FILTER_XPATH)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[text()='{createdfilter_name}']"))).click()
        self.do_click(self.CLICK_ON_MAKE_PRIMARY_BUTTON_XPATH)
        self.make_primary = self.is_displayed((By.XPATH, f"//*[text()='{createdfilter_name}']/parent::div/span[2]"))


    def make_primary_for_client(self,createdfilter_name):
        self.is_displayed(self.CLICK_ON_SAVED_FILTER_XPATH)
        saved_filter_button = self.driver.find_element(By.CSS_SELECTOR,
                                                       "button.inline-flex.items-center.flex-1:nth-of-type(2)")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", saved_filter_button)
        time.sleep(5)
        self.until_clickable(self.CLICK_ON_SAVED_FILTER_XPATH)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[text()='{createdfilter_name}']"))).click()
        self.do_click(self.CLICK_ON_MAKE_PRIMARY_FOR_CLIENT_BUTTON_XPATH)
        self.do_click(self.CLICK_ON_SET_PRIMARY_XPATH)
        self.js_click(self.CLICK_ON_LOGOUT_ID)
        time.sleep(5)

    def go_to_saved_filter(self,createdfilter_name):
        self.is_displayed(self.CLICK_ON_SAVED_FILTER_XPATH)
        saved_filter_button = self.driver.find_element(By.CSS_SELECTOR,
                                                       "button.inline-flex.items-center.flex-1:nth-of-type(2)")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", saved_filter_button)
        time.sleep(5)
        self.until_clickable(self.CLICK_ON_SAVED_FILTER_XPATH)
        self.element = self.is_displayed((By.XPATH, f"//*[text()='{createdfilter_name}']/parent::div/span[2]"))

    def apply_filter_without_multi_asset_investment(self):
        self.portfolio_value = self.get_text(self.GET_PORTFOLI0_NET_VALUE_XPATH)
        self.do_click(self.REMOVE_MULTI_ASSET_ALTERNATIVE_INVESTMENT_XPATH)
        self.do_click(self.CLICK_ON_APPLY_FILTER_BUTTON_XPATH)
        time.sleep(3)
        self.after_removed_multi_asset_checkbox = self.get_text(self.GET_PORTFOLI0_NET_VALUE_XPATH)







