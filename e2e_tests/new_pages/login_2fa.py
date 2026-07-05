import time
from os import times

import pyotp
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from uihelper.helper_file import UI_Helper


class Login_2fa(UI_Helper):
    VERIFY_AFTER_SIGN_IN_PAGE_XPATH = (By.XPATH, "//*[text()='Two - Factor Authentication']")
    CLICK_ENABLE_2FA_XPATH = (By.XPATH, "//*[text()='Enable 2FA']")
    CLICK_READTY_TO_SETUP_XPATH = (By.XPATH, "//*[text()='Ready to Setup']")
    VERIFY_DONE_BUTTON_DISABLE_ID = (By.ID, "done-button")
    VERIFY_QR_DISPLAYED_XPATH = (By.XPATH, "//*[@alt='QR Code']")
    CLICK_ON_RADIO_BUTTON_ID = (By.ID, "checkbox-authenticator")
    CLICK_ON_DONE_BUTTON_ID = (By.ID, "done-button")
    ENTER_EMAIL_OPT_XPATH = (By.XPATH, "(//*[@inputmode='numeric'])[1]")
    ENTER_AUTH_OTP_XPATH = (By.XPATH, "(//*[@inputmode='numeric'])[2]")
    CLICK_SUBMIT_AND_ENABLE_2FA_BUTTON_XPATH = (By.ID, "submit-enable-2fa-button")
    VERIFY_INVALID_EMAIL_OTP_XPATH = (By.XPATH, "//*[text()='Invalid Email OTP!']")
    VERIFY_INVALID_AUTH_OTP_XPATH = (By.XPATH, "//*[text()='Invalid Authenticator OTP!']")
    VERIFY_AFTER_SUCCESSFULL_AUTHENTICATED_XPATH = (By.ID, "dashboard-title")
    VERIFY_SUBMIT_BUTTON_DISABLE_XPATH = (By.ID, "submit-enable-2fa-button")
    CLICK_RESEND_BUTTON_CSS = (By.CSS_SELECTOR, "[class='ml-2 cursor-pointer']")
    VERIFY_AFTER_CLICK_RESEND_MESSAGE_XPATH = (By.XPATH, "//*[text()='OTP resent successfully.']")
    HOVER_ON_RESEND_XPATH = (By.CSS_SELECTOR, ".bg-primary.text-primary-foreground")



    def __init__(self, driver):
        self.driver = driver
        key = "INKVKKC3LBXSI5K5EVBHIVTNGARUMSRWGUXEOILZFZKEQJS5JVNQ"
        self.totp = pyotp.TOTP(key)

    def page_navigate_after_login(self):
        time.sleep(2)
        self.do_click(self.CLICK_ENABLE_2FA_XPATH)
        time.sleep(2)

    def click_ready_to_setup(self):
        self.do_click(self.CLICK_READTY_TO_SETUP_XPATH)
        self.is_enable(self.VERIFY_DONE_BUTTON_DISABLE_ID)

    def click_on_radio_button_and_verify_with_creds(self,email_otp, auth_otp):
        time.sleep(3)
        self.do_click(self.CLICK_ENABLE_2FA_XPATH)
        time.sleep(4)
        self.do_click(self.CLICK_READTY_TO_SETUP_XPATH)
        time.sleep(2)
        self.do_click(self.CLICK_ON_RADIO_BUTTON_ID)
        self.do_click(self.CLICK_ON_DONE_BUTTON_ID)
        time.sleep(2)
        self.send_key(self.ENTER_EMAIL_OPT_XPATH, email_otp)
        time.sleep(2)
        self.send_key(self.ENTER_AUTH_OTP_XPATH, auth_otp)
        time.sleep(2)
        self.do_click(self.CLICK_SUBMIT_AND_ENABLE_2FA_BUTTON_XPATH)

    def click_on_radio_button_and_verify_with_creds_wait_20_second(self, email_otp, auth_otp):
        time.sleep(2)
        self.do_click(self.CLICK_ENABLE_2FA_XPATH)
        time.sleep(3)
        self.do_click(self.CLICK_READTY_TO_SETUP_XPATH)
        time.sleep(2)
        self.do_click(self.CLICK_ON_RADIO_BUTTON_ID)
        self.do_click(self.CLICK_ON_DONE_BUTTON_ID)
        time.sleep(2)
        self.send_key(self.ENTER_EMAIL_OPT_XPATH, email_otp)
        self.send_key(self.ENTER_AUTH_OTP_XPATH, auth_otp)
        self.do_click(self.CLICK_SUBMIT_AND_ENABLE_2FA_BUTTON_XPATH)

    def click_on_resend_button(self):
        self.do_click(self.CLICK_RESEND_BUTTON_CSS)
        element = self.driver.find_element(By.CSS_SELECTOR, "[class='ml-2 cursor-not-allowed opacity-50']")
        action = ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(element).perform()










