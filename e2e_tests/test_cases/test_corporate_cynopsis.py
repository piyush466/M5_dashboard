import time

import pytest

from locators.corporate_other_details_locators import CorporateCynopsisDetails
from locators.other_details_locators import CynopsisDetails, CynopsisResult
from new_pages.Individual_onboarding_pages import Individual_Onboarding
from new_pages.corporate_onboarding_pages import Corporate_Onboarding
from new_pages.dashboard_page1 import DashboardList
from new_pages.login_page1 import Login
from utilities.configpar import ConfigReader
from utilities.json_reader import test_data, related_member_data, corporate_basic_details_data


class Test_Corp_Cynopsis:
    username = ConfigReader.read_config("tenant42", "username")
    password = ConfigReader.read_config("tenant42", "password")

    @pytest.mark.cynopsis
    def test_01_verify_user_can_navigate_to_corporate_cynopsis_details_page(self, setup):
        """
        Verify that the user can successfully navigate to the Corporate Cynopsis Details page.
        """
        login = Login(setup)
        corp_onboard = Corporate_Onboarding(setup)
        login.do_login(self.username, self.password)
        corp_onboard.go_to_the_corp_client_onboarding()
        corp_onboard.go_to_corp_cynopsis_page()
        corp_onboard.assertion(corp_onboard.cynopsis_header, "Corporate Cynopsis Details")

    @pytest.mark.cynopsis
    def test_02_verify_corporate_cynopsis_completion_is_100_percent_after_submitting_basic_and_other_details(self, setup):
        """
        Verify that the Corporate Cynopsis completion percentage is displayed as 100%
        after submitting the Corporate Basic Details and Other Details forms.
        """
        login = Login(setup)
        corp_onboard = Corporate_Onboarding(setup)
        login.do_login(self.username, self.password)
        corp_onboard.go_to_the_corp_client_onboarding()
        corp_onboard.fill_corporate_basic_detail_form(
            corporate_basic_details_data["entity_name"],
            corporate_basic_details_data["reg_number"],
            corporate_basic_details_data["mobile_number"],
            corporate_basic_details_data["emailid"]
        )
        corp_onboard.fill_corp_other_details_page()
        corp_onboard.go_to_corp_cynopsis_page()
        corp_onboard.assertion(corp_onboard.get_cynposis_details_percent, "100%")

    @pytest.mark.cynopsis
    def test_03_verify_initiate_screening_button_is_enabled_after_completing_required_information(self, setup):
        """
        Verify that the Initiate Screening button is enabled after all mandatory
        corporate information is successfully completed.
        """
        login = Login(setup)
        corp_onboard = Corporate_Onboarding(setup)
        login.do_login(self.username, self.password)
        corp_onboard.go_to_the_corp_client_onboarding()
        corp_onboard.fill_corporate_basic_detail_form(
            corporate_basic_details_data["entity_name"],
            corporate_basic_details_data["reg_number"],
            corporate_basic_details_data["mobile_number"],
            corporate_basic_details_data["emailid"]
        )
        corp_onboard.fill_corp_other_details_page()
        corp_onboard.go_to_corp_cynopsis_page()
        corp_onboard.assertion(corp_onboard.get_cynopsis_button, True)

    @pytest.mark.cynopsis
    def test_04_verify_user_can_navigate_to_cynopsis_result_page(self, setup):
        """
        Verify that the user can successfully navigate to the Corporate Cynopsis Result page.
        """
        login = Login(setup)
        corp_onboard = Corporate_Onboarding(setup)
        login.do_login(self.username, self.password)
        corp_onboard.go_to_the_corp_client_onboarding()
        corp_onboard.go_to_cynopsis_result_page()
        corp_onboard.assertion(
            corp_onboard.get_text(CynopsisResult.GET_CYNOPSIS_RESULT_TEXT_XPATH),
            "Cynopsis Result"
        )

    @pytest.mark.cynopsis
    def test_05_verify_cynopsis_result_page_displays_expected_instructional_message(self, setup):
        """
        Verify that the Cynopsis Result page displays the expected instructional
        message before initiating the screening process.
        """
        login = Login(setup)
        corp_onboard = Corporate_Onboarding(setup)
        login.do_login(self.username, self.password)
        corp_onboard.go_to_the_corp_client_onboarding()
        corp_onboard.go_to_cynopsis_result_page()
        corp_onboard.assertion(
            corp_onboard.get_text(CynopsisResult.GET_CYNOPSIS_RESULT_PAGE_TEXT_XPATH),
            "Initiate the Screening Process to see the Cynopsis Result"
        )

    @pytest.mark.cynopsis
    def test_06_verify_all_basic_information_details_are_displayed_on_the_corporate_cynopsis_page(self, setup):
        """
        Verify that all Corporate Basic Information details, including Entity Name,
        Registration Number, Contact Number, and Email ID, are correctly displayed
        on the Corporate Cynopsis Details page.
        """
        login = Login(setup)
        corp_onboard = Corporate_Onboarding(setup)
        login.do_login(self.username, self.password)
        corp_onboard.go_to_the_corp_client_onboarding()
        corp_onboard.fill_corporate_basic_detail_form(
            corporate_basic_details_data["entity_name"],
            corporate_basic_details_data["reg_number"],
            corporate_basic_details_data["mobile_number"],
            corporate_basic_details_data["emailid"]
        )
        corp_onboard.go_to_corp_cynopsis_page()
        corp_onboard.assertion(corporate_basic_details_data["entity_name"],
                               corp_onboard.get_attribute(CorporateCynopsisDetails.GET_ENTITY_NAME_XPATH, "value"))
        corp_onboard.assertion(corporate_basic_details_data["reg_number"],
                               corp_onboard.get_attribute(CorporateCynopsisDetails.GET_REGISTRATION_NUMBER_XPATH, "value"))
        corp_onboard.assertion(corporate_basic_details_data["mobile_number"],
                               corp_onboard.get_attribute(CorporateCynopsisDetails.GET_CONTACT_NUMBER_CYNOPSIS_XPATH, "value"))
        corp_onboard.assertion(corporate_basic_details_data["emailid"],
                               corp_onboard.get_attribute(CorporateCynopsisDetails.GET_EMAIL_ID_XPATH, "value"))

    @pytest.mark.cynopsis
    def test_07_verify_primary_entity_is_selected_by_default_after_initiating_screening(self, setup):
        """
        Verify that the primary corporate entity is displayed as the default selected
        value after initiating the screening process.
        """
        login = Login(setup)
        corp_onboard = Corporate_Onboarding(setup)
        login.do_login(self.username, self.password)
        corp_onboard.go_to_the_corp_client_onboarding()
        corp_onboard.fill_corporate_basic_detail_form(
            corporate_basic_details_data["entity_name"],
            corporate_basic_details_data["reg_number"],
            corporate_basic_details_data["mobile_number"],
            corporate_basic_details_data["emailid"]
        )
        corp_onboard.fill_corp_other_details_page()
        corp_onboard.go_to_cynopsis_result_page()
        corp_onboard.cynopsis_result_initiate_screening()
        corp_onboard.assertion(
            corporate_basic_details_data["entity_name"],
            corp_onboard.get_attribute(CynopsisResult.GET_USER_NAME_FROM_SCREENING_POPUP_XPATH, "value")
        )

    @pytest.mark.cynopsis
    def test_08_verify_related_member_details_are_displayed_on_the_corporate_cynopsis_page(self, setup):
        """
        Verify that the related member's First Name and Last Name are correctly
        displayed on the Corporate Cynopsis Details page.
        """
        login = Login(setup)
        corp_onboard = Corporate_Onboarding(setup)
        login.do_login(self.username, self.password)
        corp_onboard.go_to_the_corp_client_onboarding()
        corp_onboard.fill_related_memebers_page(
            related_member_data["first_name"],
            related_member_data["last_name"]
        )
        corp_onboard.go_to_corp_cynopsis_page()
        corp_onboard.assertion(
            related_member_data["first_name"],
            corp_onboard.get_attribute(CynopsisDetails.GET_CRP_FIRST_NAME_XPATH, "value")
        )
        corp_onboard.assertion(
            related_member_data["last_name"],
            corp_onboard.get_attribute(CynopsisDetails.GET_CRP_LAST_NAME_XPATH, "value")
        )

