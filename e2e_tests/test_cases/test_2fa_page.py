import time
import pyotp
import pytest
import allure
from new_pages.login_2fa import Login_2fa
from new_pages.login_page1 import Login
from utilities.configpar import ConfigReader


class Test_2FA:
    username = ConfigReader.read_config("tenant3", "username")
    password = ConfigReader.read_config("tenant3", "password")

    key = "INKVKKC3LBXSI5K5EVBHIVTNGARUMSRWGUXEOILZFZKEQJS5JVNQ"
    totp = pyotp.TOTP(key)

    @pytest.mark.run_this
    @allure.title("Verify navigation to 2FA page after clicking Sign In")
    def test_01_after_click_sign_in_user_navigate_to_2fa_page(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login.assertion(login_2fa.get_text(login_2fa.VERIFY_AFTER_SIGN_IN_PAGE_XPATH), "Two - Factor Authentication")

    @pytest.mark.run_this
    @allure.title("Verify QR code is displayed after enabling 2FA setup")
    def test_02_after_click_enable_2fa_QR_displayed(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login_2fa.page_navigate_after_login()
        login.assertion(login_2fa.is_displayed(login_2fa.VERIFY_QR_DISPLAYED_XPATH), True)

    @allure.title("Verify Done button is disabled if radio button is not selected")
    def test_03_without_select_radio_button_done_button_disable(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login_2fa.page_navigate_after_login()
        login_2fa.click_ready_to_setup()
        login_2fa.assertion(login_2fa.is_enable(login_2fa.VERIFY_DONE_BUTTON_DISABLE_ID), "False")

    @pytest.mark.run_this
    @allure.title("Verify validation with invalid OTPs in both email and authenticator fields")
    def test_04_check_with_invalid_otp_on_both_fields(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login_2fa.click_on_radio_button_and_verify_with_creds("123132", "312312")
        login_2fa.assertion(login_2fa.get_text(login_2fa.VERIFY_INVALID_EMAIL_OTP_XPATH), "Invalid Email OTP!")

    @allure.title("Verify form cannot be submitted without entering any OTPs")
    def test_05_check_without_otp_user_can_submit(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login_2fa.click_on_radio_button_and_verify_with_creds("  ", "    ")
        login_2fa.assertion(login_2fa.is_enable(login_2fa.VERIFY_SUBMIT_BUTTON_DISABLE_XPATH), False)

    @allure.title("Verify user can resend OTP successfully")
    def test_06_check_user_can_resend_the_opt(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login_2fa.click_on_radio_button_and_verify_with_creds("123456", "312312")
        login_2fa.click_on_resend_button()
        login_2fa.assertion(login_2fa.get_text(login_2fa.VERIFY_AFTER_CLICK_RESEND_MESSAGE_XPATH), "OTP resent successfully.")

    @allure.title("Verify message is displayed when user hovers after clicking resend OTP")
    def test_07_check_when_user_hover_on_after_resend_message_displayed(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login_2fa.click_on_radio_button_and_verify_with_creds("123456", "312312")
        login_2fa.click_on_resend_button()
        actual_result = login_2fa.get_text(login_2fa.HOVER_ON_RESEND_XPATH)
        login_2fa.assert_In("You can resend OTP after 2 minutes", actual_result)

    @pytest.mark.run_this
    @allure.title("Verify validation when email OTP is valid and authenticator OTP is invalid")
    def test_08_check_email_valid_auth_invalid(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login_2fa.click_on_radio_button_and_verify_with_creds_wait_20_second("123456", "312312")
        login_2fa.assertion(login_2fa.get_text(login_2fa.VERIFY_INVALID_AUTH_OTP_XPATH), "Invalid Authenticator OTP!")

    @allure.title("Verify successful authentication with valid email and authenticator OTPs")
    def test_09_check_with_when_both_otp_valid_entered(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login_2fa.click_on_radio_button_and_verify_with_creds_wait_20_second("123456", self.totp.now())
        login_2fa.assertion(login_2fa.is_displayed(login_2fa.VERIFY_AFTER_SUCCESSFULL_AUTHENTICATED_XPATH), True)

    @allure.title("Verify user lands on dashboard after successful 2FA authentication")
    def test_010_check_after_succesfully_authenticate_2fa_field_open(self, setup):
        login = Login(setup)
        login_2fa = Login_2fa(setup)
        login.do_login(self.username, self.password)
        login.authentication_2fa_code(self.totp.now())
        login_2fa.assertion(login_2fa.is_displayed(login_2fa.VERIFY_AFTER_SUCCESSFULL_AUTHENTICATED_XPATH), True)

    @allure.title("Verify error message displayed after entering invalid 2FA code")
    def test_011_check_with_invalid_2fa_login_screen(self, setup):
        login = Login(setup)
        login.do_login(self.username, self.password)
        login.authentication_2fa_code("111222")
        login.assertion(login.get_text(login.VERIFY_AFTER_INVALID_2FA_LOGIN_XPATH), "Invalid Token")

    @allure.title("Verify expired 2FA token is not accepted")
    def test_012_check_expire_2fa_used(self, setup):
        login = Login(setup)
        login.do_login(self.username, self.password)
        login.expire_authentication_2fa_code(self.totp.now())
        login.assertion(login.get_text(login.VERIFY_AFTER_INVALID_2FA_LOGIN_XPATH), "Invalid Token")
