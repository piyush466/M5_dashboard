import time

from selenium.webdriver.common.by import By

from locators.corporate_onboarding_locators import CorporateOnboard
from locators.corporate_other_details_locators import CorporateCynopsisDetails, CorporateOtherDetials
from locators.other_details_locators import OtherDetials, CynopsisDetails, CynopsisResult
from locators.regulatory_details_locators import RegulatoryDetails
from locators.related_members_locators import RelatedMembersLocators
from locators.risk_profile_locators import RiskProfile
from new_pages.dashboard_page1 import DashboardList
from uihelper.helper_file import UI_Helper


class Corporate_Onboarding(UI_Helper):

    def __init__(self, driver):
        # Initialize the driver instance for this class
        self.driver = driver

    def go_to_the_corp_client_onboarding(self):
        # Click on the hamburger menu on the dashboard
        # self.wait_until_loader_disappears(DashboardList.HUMBERGER_MENU_XPATH)
        self.is_displayed(DashboardList.HUMBERGER_MENU_XPATH)
        self.until_clickable(DashboardList.HUMBERGER_MENU_XPATH)
        time.sleep(2)
        # self.js_click(DashboardList.HUMBERGER_MENU_XPATH)
        # Click on the 'Client Onboarding' option
        self.js_click(CorporateOnboard.SELECT_CLIENT_ONBOARDING_XPATH)

        # Verify the 'Onboard New' button is displayed
        time.sleep(2)
        self.is_enable(CorporateOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        time.sleep(2)
        self.until_clickable(CorporateOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        # self.is_displayed(CorporateOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        # Click on the 'Onboard New' button
        # self.do_click(CorporateOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        # self.is_element_present(CorporateOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        # self.js_click(CorporateOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)

        # self.driver.refresh()
        # Select 'Corporate' option for onboarding
        self.until_clickable(CorporateOnboard.CLICK_ON_CORPORATE_XPATH)
        # self.js_click(CorporateOnboard.CLICK_ON_INDIVIDUAL_XPATH)
        # Select the 'No' option in radio buttons
        # self.do_click(CorporateOnboard.SELECT_RADIO_BUTTON_NO_ID)
        # Click the 'Proceed' button
        # self.do_click(CorporateOnboard.CLICK_ON_PROCEED_BUTTON_XPATH)
        # Verify the 'Corporate Basic Details' form is displayed
        self.is_displayed(CorporateOnboard.TEXT_CORPORATE_BASIC_DETAILS_FORM_XPATH)

    def fill_corporate_basic_detail_form(self, entityname, reg_number, mobile_number, emailid):

        # Enter first name
        self.send_key(CorporateOnboard.ENTER_ENTITY_NAME_XPATH,entityname)
        self.send_key(CorporateOnboard.ENTER_REGISTRATION_NUMBER_XPATH, reg_number)
        self.do_click(CorporateOnboard.CLICK_CORPORATE_ITALY_CODE_XPATH)
        self.do_click(CorporateOnboard.SELECT_CORPORATE_ITALY_CODE_XPATH)
        self.send_key(CorporateOnboard.ENTER_CORPORATE_CONTACT_NUMBER_XPATH, mobile_number)
        self.send_key(CorporateOnboard.ENTER_EMAIL_ID_XPATH, emailid)
        self.do_click(CorporateOnboard.CLICK_ON_ENTITY_TYPE_XPATH)
        time.sleep(2)
        self.is_displayed(CorporateOnboard.SELECT_ENTITY_TYPE_XPATH)
        self.do_click(CorporateOnboard.SELECT_ENTITY_TYPE_XPATH)
        self.do_click(CorporateOnboard.CLICK_ON_CORPORATE_SCREENING_STATUS_XPATH)
        self.do_click(CorporateOnboard.CLICK_ON_CORP_CURRENT_XPATH)
        # click on Ownership Structure Layers
        self.do_click(CorporateOnboard.CLICK_ON_OWNERSHIP_STRUCUTE_LAYER_XPATH)
        self.do_click(CorporateOnboard.SELECT_OWNERSHIP_STRUCUTE_LAYER_XPATH)
        # country of corporation
        self.do_click(CorporateOnboard.CLICK_ON_CORP_COUNTRY_OF_CORPRATION_XPATH)
        self.do_click(CorporateOnboard.SELECT_COUNTRY_OF_CORPORATION_XPATH)
        # CLICK ON INDUSTRY
        self.do_click(CorporateOnboard.CLICK_ON_CORP_INDUSTRY_XPATH)
        self.js_click(CorporateOnboard.SELECT_INDUSTRY_XPATH)
        # Cynopsis Screening - Onboarding Mode dropdown
        self.do_click(CorporateOnboard.CLICK_ON_CYNOPSIS_SCREENING_ONBOARDING_XPATH)
        self.do_click(CorporateOnboard.SELECT_FACE_TO_FACE_XPATH)
        # Cynopsis Screening - Payment Mode dropdown
        self.do_click(CorporateOnboard.CLICK_ON_PAYMENT_MODE_XPATH)
        self.do_click(CorporateOnboard.SELECT_TELEGRAPHIC_TRANSFER_XPATH)
        # Cynopsis Screening - Product/Service Complexity dropdown
        self.do_click(CorporateOnboard.CLICK_ON_PRODUCT_SERVICE_COMPLEX_XPATH)
        self.do_click(CorporateOnboard.SELECT_SIMPLE_XPATH)
        # Cynopsis Screening - Source of Funds dropdown
        self.do_click(CorporateOnboard.CLICK_ON_SOURCE_OF_FUND_XPATH)
        self.do_click(CorporateOnboard.SELECT_LOAN_XPATH)

        time.sleep(2)



    def fill_risk_profile_form(self):
        # Navigate to Risk Profile page
        self.do_click(RiskProfile.CLICK_ON_RISK_PROFILE_PAGE_XPATH)
        self.do_click(RiskProfile.CLICK_ON_KNOWLEDGE_AND_EXPERIENCE_XPATH)

        # Open Client Investment Profile section
        self.js_click(RiskProfile.CLICK_ON_CLIENT_INVESTMENT_PROFILE_XPATH)

        # Scroll to and open Client Details form
        self.scroll_down_toElement(RiskProfile.CLICK_ON_CLEINT_DETAILS_FORM_XPATH)
        self.js_click(RiskProfile.CLICK_ON_CLEINT_DETAILS_FORM_XPATH)

        # Scroll back to Knowledge & Experience section
        self.scroll_down_toElement(RiskProfile.CLICK_ON_KNOWLEDGE_AND_EXPERIENCE_XPATH)

        # List of all radio button XPaths to be clicked
        xpaths = [
            RiskProfile.CLICK_ON_YES_RADIO_BUTTONS_XPATH[1],
            RiskProfile.CLICK_ON_15_RADIO_BUTTONS_XPATH[1],
            RiskProfile.CLICK_ON_1_5_RADIO_BUTTONS_XPATH[1],
            RiskProfile.CLICK_ON_KNOWLEDGE_RADIO_BUTTONS_XPATH[1],
            RiskProfile.CLICK_ON_TRAINING_RADIO_BUTTONS_XPATH[1],
            RiskProfile.CLICK_ON_RISK_ACKNO_RADIO_BUTTONS_XPATH[1],
            RiskProfile.CLICK_ON_RADIO_BTN_CLIENT_INVESTMENT_PROFILE_XPATH[1],
            RiskProfile.CLICK_ON_CLIENT_DETAILS_RADIO_BTN_XAPTH[1]
        ]

        # Click all the radio buttons in sequence
        for xp in xpaths:
            [Btn.click() for Btn in self.driver.find_elements(By.XPATH, xp)]

        # Enter USD amount
        self.send_key(RiskProfile.ENTER_USD_AMOUNT_ID, "200000")

        # Select a risk level from dropdown
        self.scroll_down_toElement(RiskProfile.CLICK_ON_RISK_DROP_XPATH)
        self.do_click(RiskProfile.CLICK_ON_RISK_DROP_XPATH)
        self.do_click(RiskProfile.SELECT_VALUE_VIA_XPATH)

        # Click Evaluate button
        self.do_click(RiskProfile.CLICK_ON_EVALUATE_BUTTON_XPATH)

        # Scroll to and confirm with "Yes" button
        self.scroll_down_toElement(RiskProfile.CLICK_ON_YES_BUTTON_XPATH)
        self.js_click(RiskProfile.CLICK_ON_YES_BUTTON_XPATH)

        # Select a date from calendar

        self.is_displayed(RiskProfile.CLICK_ON_CALENDER_XPATH)
        time.sleep(3)
        self.js_click(RiskProfile.CLICK_ON_CALENDER_XPATH)
        self.do_click(RiskProfile.CLICK_ON_DATE_XPATH)

        # Save form and submit
        self.do_click(RiskProfile.CLICK_ON_SAVE_BUTTON)
        self.do_click(CorporateOnboard.CLICK_ON_SUBMIT_BUTTON_XPATH)

        # Store success message for validation
        self.form_created = self.get_text(RiskProfile.VALIDATE_MESSAGE_SHOW_XPATH)

    def fill_corp_other_details_page(self):
        """
        Fill out the 'Other Details' page in the onboarding process.
        This includes selecting country/region, entering personal details,
        and submitting the form.
        """

        # Navigate to the 'Other Details' section
        self.do_click(CorporateOtherDetials.CLICK_ON_OTHER_DETAILS_PAGE_XPATH)

        # Permanant Address
        self.send_key(CorporateOtherDetials.ENTER_CORPORATE_REGISTER_ADDRESS_XPATH, "Mumbai")


    def fill_regulatory_details_page(self):
        self.do_click(RegulatoryDetails.CLICK_ON_REGULATORY_DETAILS_PAGE_XPATH)
        allRadioBtns = self.driver.find_elements(By.XPATH, "//button[@role='radio']//parent::div/label[text()='No']")
        for radioBtn in allRadioBtns:
            radioBtn.click()
        self.do_click(RegulatoryDetails.CLICK_ON_PEP_DROP_DOWN_XPATH)
        self.do_click(RegulatoryDetails.SELECT_SENIOR_PUBLIC_FIGURE_XPATH)
        self.do_click(RegulatoryDetails.CLICK_ON_APPLICABLE_CLIENT_XPATH)
        self.do_click(RegulatoryDetails.SELECT_APPLICABLE_CLIENT_XPATH)
        self.send_key(RegulatoryDetails.ENTER_TEXTAREA_DETAILS_XPATH, "Details")
        self.do_click(RegulatoryDetails.CLICK_ON_CLIENT_CLASSIFICATION_XPATH)
        self.do_click(RegulatoryDetails.SELECT_CLIENT_CLASSIFICATION_XPATH)
        self.do_click(RegulatoryDetails.CLICK_ON_CLASSIFICATION2_XPATH)
        self.do_click(RegulatoryDetails.SELECT_PROFESSIONAL_CLIENT_XPATH)
        self.do_click(RegulatoryDetails.CLICK_ON_CHECKBOX_XPATH)
        self.do_click(RegulatoryDetails.CLICK_ON_APPLICABLE_EXPERIENCE_XPATH)
        self.do_click(RegulatoryDetails.SELECT_VALUE_FROM_APPLICABLE_DROP_DOWN)
        self.do_click(RegulatoryDetails.CLICK_ON_APPLICABLE_EXPERIENCE2_XPATH)
        self.do_click(RegulatoryDetails.SELECT_VALUE_FROM_APPLICABLE_DROP_DOWN2_XPATH)
        self.do_click(RegulatoryDetails.CLICK_ON_SELECT_APPLICABLE_DROP_DOWN_XPATH)
        self.do_click(RegulatoryDetails.SELECT_VALUE_FROM_APPLICABLE_DROP_DOWN_XPATH)
        self.send_key(RegulatoryDetails.SEND_FOREIGN_TAX_NUMBER_XPATH, "1321341")
        self.do_click(RegulatoryDetails.CLICK_ON_CHECKBOX_FTIN_XPATH)
        self.send_key(RegulatoryDetails.SEND_REF_NUMBER_XPATH, "414124")
        self.scroll_down_toElement(RegulatoryDetails.FILE_UPLOAD_XPATH)
        self.do_click(RegulatoryDetails.FILE_UPLOAD_XPATH)
        self.send_key(RegulatoryDetails.FILE_UPLOAD_XPATH, r".//image.png")

    def go_to_corp_cynopsis_page(self):
        self.do_click(CynopsisDetails.CLICK_ON_CYNOPSIS_DETAILS_PAGE_XPATH)
        self.cynopsis_header = self.get_text(CorporateCynopsisDetails.GET_CYNOPSIS_DETAILS_TEXT_XPATH)
        self.get_cynposis_details_percent = self.get_text(CorporateCynopsisDetails.GET_CYNOPSIS_DETAILS_PERCENTAGE_XPATH)
        self.get_cynopsis_button = self.is_enable(CorporateCynopsisDetails.INITIATE_SCREENING_BUTTON_XPATH)
        self.scroll_down_toElement(CorporateCynopsisDetails.GET_CONTACT_NUMBER_XPATH)
        time.sleep(2)
        # at = self.get_attribute(CynopsisDetails.GET_CONTACT_NUMBER_XPATH, "value")
        # print(at)
        # self.get_dateofissue = self.get_text(CynopsisDetails.GET_CONTACT_NUMBER_XPATH)
        # print(self.get_dateofissue)

    def go_to_cynopsis_result_page(self):
        self.do_click(CynopsisResult.CLICK_ON_CYNOPSIS_DETAILS_PAGE_XPATH)

    def cynopsis_result_initiate_screening(self):
        self.do_click(CynopsisResult.CLICK_ON_CYNOPSIS_DETAILS_PAGE_XPATH)
        self.do_click(CynopsisDetails.INITIATE_SCREENING_BUTTON_XPATH)
        self.user_name = self.get_text(CynopsisResult.GET_USER_CLIENT_NAME_XPATH)
        time.sleep(3)

    def fill_related_memebers_page(self,fname,lname):
        self.do_click(RelatedMembersLocators.CLICK_ON_RELATED_MEMBER_PAGE_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_ADD_ANOTHER_BUTTON_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_NO_RADIO_BUTTON_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_SELECT_MEMEBER_TYPE_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.SELECT_INDIVIDUAL_FROM_MEMBER_TYPE_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_CONFOIM_BUTTOM_XPATH)
        # self.do_click(RelatedMembersLocators.CLICK_ON_MARITAL_STATUS_DROPDOWN_XPATH)
        # self.do_click((RelatedMembersLocators.SELECT_VALUE_FROM_MARITAL_STATUS_DROPDOWN_XPATH))
        # self.do_click(RelatedMembersLocators.CLICK_ON_RELATION_DROPDOWN_XPATH)
        # self.do_click(RelatedMembersLocators.SELECT_VALUE_FROM_RELATION_STATUS_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_TITLE_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.SELECT_VALUE_FROM_TITLE_STATUS_DROPDOWN_XPATH)
        self.send_key(RelatedMembersLocators.ENTER_FIRST_NAME_XPATH,fname)
        self.send_key(RelatedMembersLocators.ENTER_LAST_NAME_XPATH,lname)
        # self.do_click(RelatedMembersLocators.CLICK_ON_DATE_OF_BIRTH_XPATH)
        # self.send_key(RelatedMembersLocators.ENTER_DATE_OF_BIRTH_XPATH, dob)
        self.do_click(RelatedMembersLocators.CLICK_ON_NATIONAL_ID_RADIO_BUTTON_XPATH)
        time.sleep(4)

    # def go_to_crp_details_fields(self):



















