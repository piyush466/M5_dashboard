import time

import pytest

from locators.other_details_locators import CynopsisDetails, CynopsisResult
from new_pages.Individual_onboarding_pages import Individual_Onboarding
from new_pages.dashboard_page1 import DashboardList
from new_pages.login_page1 import Login
from utilities.configpar import ConfigReader
from utilities.json_reader import test_data, related_member_data


class Test_Cynopsis:
    username = ConfigReader.read_config("tenant42", "username")
    password = ConfigReader.read_config("tenant42", "password")

    @pytest.mark.cynopsis
    def test_01_verify_user_can_navigate_to_cynopsis_details_page(self, setup):
        """
        Verify that the user can successfully navigate to the Individual Cynopsis Details page.
        """
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.go_to_cynopsis_page()
        ind_onboard.assertion(ind_onboard.cynopsis_header, "Individual Cynopsis Details")

    @pytest.mark.cynopsis
    def test_02_verify_cynopsis_completion_is_100_percent_after_submitting_basic_and_other_details(self, setup):
        """
        Verify that the Cynopsis completion percentage is displayed as 100% after submitting
        the Basic Details and Other Details forms.
        """
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_basic_detail_form(
            test_data["first_name"],
            test_data["last_name"],
            test_data["date_of_issue"],
            test_data["date_of_expiry"],
            test_data["dob"],
            test_data["mobile"],
            test_data["email"],
            test_data["bank_name"],
        )
        ind_onboard.fill_other_details_page()
        ind_onboard.go_to_cynopsis_page()
        ind_onboard.assertion(ind_onboard.get_cynposis_details_percent, "100%")

    @pytest.mark.cynopsis
    def test_03_verify_initiate_screening_button_is_enabled_after_completing_required_information(self, setup):
        """
        Verify that the Initiate Screening button is enabled after all mandatory
        information is successfully completed.
        """
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_basic_detail_form(
            test_data["first_name"],
            test_data["last_name"],
            test_data["date_of_issue"],
            test_data["date_of_expiry"],
            test_data["dob"],
            test_data["mobile"],
            test_data["email"],
            test_data["bank_name"],
        )
        ind_onboard.fill_other_details_page()
        ind_onboard.go_to_cynopsis_page()
        ind_onboard.assertion(ind_onboard.get_cynopsis_button, True)

    @pytest.mark.cynopsis
    def test_04_verify_user_can_navigate_to_cynopsis_result_page(self, setup):
        """
        Verify that the user can successfully navigate to the Cynopsis Result page.
        """
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.go_to_cynopsis_result_page()
        ind_onboard.assertion(
            ind_onboard.get_text(CynopsisResult.GET_CYNOPSIS_RESULT_TEXT_XPATH),
            "Cynopsis Result"
        )

    @pytest.mark.cynopsis
    def test_05_verify_cynopsis_result_page_displays_expected_instructional_message(self, setup):
        """
        Verify that the Cynopsis Result page displays the expected instructional
        message before initiating the screening process.
        """
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.go_to_cynopsis_result_page()
        ind_onboard.assertion(
            ind_onboard.get_text(CynopsisResult.GET_CYNOPSIS_RESULT_PAGE_TEXT_XPATH),
            "Initiate the Screening Process to see the Cynopsis Result"
        )

    @pytest.mark.cynopsis
    def test_06_verify_all_basic_information_details_are_displayed_on_the_cynopsis_page(self, setup):
        """
        Verify that all Basic Information details entered during onboarding
        are correctly displayed on the Cynopsis Details page.
        """
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_basic_detail_form(
            test_data["first_name"],
            test_data["last_name"],
            test_data["date_of_issue"],
            test_data["date_of_expiry"],
            test_data["dob"],
            test_data["mobile"],
            test_data["email"],
            test_data["bank_name"],
        )
        ind_onboard.go_to_cynopsis_page()
        time.sleep(2)
        ind_onboard.assertion(test_data["date_of_issue"], ind_onboard.get_text(CynopsisDetails.GET_DATE_OF_ISSUE_XAPTH))
        ind_onboard.assertion(test_data["email"], ind_onboard.get_attribute(CynopsisDetails.GET_USER_EMAIL_ID_XPATH, "value"))
        ind_onboard.assertion(test_data["date_of_expiry"], ind_onboard.get_text(CynopsisDetails.GET_DATE_OF_EXPIRY_XPATH))
        ind_onboard.assertion(test_data["dob"], ind_onboard.get_text(CynopsisDetails.GET_DATE_OF_BIRTH_XPATH))
        ind_onboard.assertion(test_data["mobile"], ind_onboard.get_attribute(CynopsisDetails.GET_CONTACT_NUMBER_XPATH, "value"))

    @pytest.mark.cynopsis
    def test_07_verify_primary_user_is_selected_by_default_after_initiating_screening(self, setup):
        """
        Verify that the primary user is displayed as the default selected user
        after initiating the screening process.
        """
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_basic_detail_form(
            test_data["first_name"],
            test_data["last_name"],
            test_data["date_of_issue"],
            test_data["date_of_expiry"],
            test_data["dob"],
            test_data["mobile"],
            test_data["email"],
            test_data["bank_name"],
        )
        ind_onboard.fill_other_details_page()
        ind_onboard.go_to_cynopsis_result_page()
        ind_onboard.cynopsis_result_initiate_screening()
        ind_onboard.assertion(
            ind_onboard.user_name.replace("Mr. ", "").lower(),
            f"{test_data['first_name']} {test_data['last_name']}".lower()
        )

    @pytest.mark.cynopsis
    def test_08_verify_related_member_details_are_displayed_on_the_cynopsis_page(self, setup):
        """
        Verify that the related member's First Name, Last Name, and Date of Birth
        are correctly displayed on the Cynopsis Details page.
        """
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_related_memebers_page(
            related_member_data["first_name"],
            related_member_data["last_name"],
            related_member_data["date_of_birth"]
        )
        ind_onboard.go_to_cynopsis_page()
        ind_onboard.assertion(related_member_data["first_name"], ind_onboard.get_attribute(CynopsisDetails.GET_CRP_FIRST_NAME_XPATH, "value"))
        ind_onboard.assertion(related_member_data["last_name"], ind_onboard.get_attribute(CynopsisDetails.GET_CRP_LAST_NAME_XPATH, "value"))
        ind_onboard.assertion(related_member_data["date_of_birth"], ind_onboard.get_text(CynopsisDetails.GET_CRP_DATE_OF_BIRTH_XPATH))