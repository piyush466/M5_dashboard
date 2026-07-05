import time
from selenium.webdriver.common.by import By
from uihelper.helper_file import UI_Helper


class Login(UI_Helper):
    CLICK_ON_I_AGRRE_XPATH = (By.XPATH, "//*[text()='I Agree']")
    ENTER_USEERNAME_XPATH = (By.XPATH, "//*[contains(@placeholder, 'Username')]")
    ENTER_PASSWORD_XPATH = (By.XPATH, "//*[contains(@placeholder, 'Password')]")
    CLICK_ON_I_SIGN_IN_XPATH = (By.XPATH, "//*[text()='Sign in']")
    DASHBOARD_NEAME_XPATH = (By.XPATH, "//button[text()='Apply']")
    INVALID_CREDS_MEESAGE = (By.XPATH, '//*[contains(text(), "Incorrect username or password. Please try again!")]')
    AUTH_CODE_XPATH = (By.XPATH, "//*[@placeholder='2FA Password']")
    VERIFY_AFTER_INVALID_2FA_LOGIN_XPATH = (By.XPATH, "//*[text()='Invalid Token']")

    def __init__(self, driver):
        self.driver = driver

    def do_login(self, username, password):
        time.sleep(2)
        try:
            self.do_click(self.CLICK_ON_I_AGRRE_XPATH)
        except:
            None
        self.send_key(self.ENTER_USEERNAME_XPATH, username)
        self.send_key(self.ENTER_PASSWORD_XPATH, password)
        self.do_click(self.CLICK_ON_I_SIGN_IN_XPATH)
        time.sleep(2)

    def authentication_2fa_code(self,otp):
        self.send_key(self.AUTH_CODE_XPATH, otp)
        self.do_click(self.CLICK_ON_I_SIGN_IN_XPATH)

    def expire_authentication_2fa_code(self,otp):
        self.send_key(self.AUTH_CODE_XPATH, otp)
        time.sleep(45)
        self.do_click(self.CLICK_ON_I_SIGN_IN_XPATH)