import time

import pytest

from new_pages.login_page1 import Login



class Test_Login:

    def test_01_login_with_valid_creds(self, setup):
        """
        Test to verify that a user can successfully log in using valid credentials.
        """
        login = Login(setup)
        login.do_login("piyushd+lwp+rm2@valuefy.com", "Piyush@123456")
        login.assertion(login.is_displayed(login.DASHBOARD_NEAME_XPATH), True)


    def test_02_login_with_invalid_creds(self, setup):
        """
        Test to verify the error message when login is attempted with invalid email and password.
        """
        login = Login(setup)
        login.do_login("piyushd+lwp@valuefy.com", "Piyush@123566")
        actual_result = login.get_text(login.INVALID_CREDS_MEESAGE)
        login.assertion(actual_result, "Incorrect username or password. Please try again!")

    def test_03_login_with_invalid_email_valid_password(self, setup):
        """
        Test to verify the error message when login is attempted with an invalid email and valid password.
        """
        login = Login(setup)
        login.do_login("piyushd+lwp@valuefy.com", "Piyush@123")
        actual_result = login.get_text(login.INVALID_CREDS_MEESAGE)
        login.assertion(actual_result, "Incorrect username or password. Please try again!")

    def test_04_login_with_invalid_email_invalid_password(self, setup):
        """
        Test to verify the error message when login is attempted with both invalid email and invalid password.
        """
        login = Login(setup)
        login.do_login("piyushd+lwp@valuefy.com", "Piyush@123566")
        actual_result = login.get_text(login.INVALID_CREDS_MEESAGE)
        login.assertion(actual_result, "Incorrect username or password. Please try again!")

    def test_05_login_with_valid_email_invalid_password(self, setup):
        """
        Test to verify the error message when login is attempted with a valid email and invalid password.
        """
        login = Login(setup)
        login.do_login("piyushd+lwp+rm2@valuefy.com", "Piyush@123566")
        actual_result = login.get_text(login.INVALID_CREDS_MEESAGE)
        login.assertion(actual_result, "Incorrect username or password. Please try again!")

    # def test_06_to_verify_2_FA_authentication(self,setup):
    #     """
    #     (Commented Out) Test to verify 2FA authentication using authenticator code.
    #     """
    #     login = Login(setup)
    #     key = "INKVKKC3LBXSI5K5EVBHIVTNGARUMSRWGUXEOILZFZKEQJS5JVNQ"
    #     totp = pyotp.TOTP(key)
    #     login.do_login("Omkarb+sys@valuefy.com", "Pass@1234")
    #     login.authentication_2fa_code(totp.now())

    @pytest.mark.testing
    def test_06_verify_after_click_sign_up_user_navigate_to_mfa_page(self, setup):
        """
        Test to verify that after login with valid credentials, user is redirected to the MFA page.
        """
        driver, username, password = setup
        login = Login(driver)
        login.do_login(username, password)




