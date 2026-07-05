import time
from os import times

import driver
from selenium.webdriver.common.by import By

from locators.individual_onboarding_locators import IndividualOnboard
from locators.other_details_locators import OtherDetials, CynopsisDetails, CynopsisResult
from locators.regulatory_details_locators import RegulatoryDetails
from locators.related_members_locators import RelatedMembersLocators
from locators.risk_profile_locators import RiskProfile
from new_pages.dashboard_page1 import DashboardList
from uihelper.helper_file import UI_Helper


class Individual_Onboarding(UI_Helper):

    def __init__(self, driver):
        # Initialize the driver instance for this class
        self.driver = driver

    def go_to_the_client_onboarding(self):
        # Click on the hamburger menu on the dashboard
        # self.wait_until_loader_disappears(DashboardList.HUMBERGER_MENU_XPATH)
        self.is_displayed(DashboardList.HUMBERGER_MENU_XPATH)
        self.until_clickable(DashboardList.HUMBERGER_MENU_XPATH)
        time.sleep(2)
        # self.js_click(DashboardList.HUMBERGER_MENU_XPATH)
        # Click on the 'Client Onboarding' option
        self.js_click(IndividualOnboard.SELECT_CLIENT_ONBOARDING_XPATH)

        # Verify the 'Onboard New' button is displayed
        time.sleep(2)
        self.is_enable(IndividualOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        time.sleep(2)
        self.until_clickable(IndividualOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        # self.is_displayed(IndividualOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        # Click on the 'Onboard New' button
        # self.do_click(IndividualOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        # self.is_element_present(IndividualOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)
        # self.js_click(IndividualOnboard.CLICK_ON_ONBOARD_NEW_BUTTON)

        # self.driver.refresh()
        # Select 'Individual' option for onboarding
        self.until_clickable(IndividualOnboard.CLICK_ON_INDIVIDUAL_XPATH)
        # self.js_click(IndividualOnboard.CLICK_ON_INDIVIDUAL_XPATH)
        # Select the 'No' option in radio buttons
        # self.do_click(IndividualOnboard.SELECT_RADIO_BUTTON_NO_ID)
        # Click the 'Proceed' button
        # self.do_click(IndividualOnboard.CLICK_ON_PROCEED_BUTTON_XPATH)
        # Verify the 'Individual Basic Details' form is displayed
        self.is_displayed(IndividualOnboard.TEXT_INDIVIDUAL_BASIC_DETAILS_FORM_XPATH)

    def fill_basic_detail_form(self, fname, lname, issueDate, expiryDate, birthDate, contactNumber, emailId, enterBankDetails):
        # Select gender from dropdown
        self.do_click(IndividualOnboard.CLICK_ON_SELECT_GENDER_XPATH)
        self.do_click(IndividualOnboard.SELECT_MALE_FROM_DROPDOWN_XPATH)
        # Select title from dropdown
        self.do_click(IndividualOnboard.CLICK_ON_SELECT_TITLE_XPATH)
        self.do_click(IndividualOnboard.SELECT_MR_FROM_DROPDOWN_XPATH)
        # Enter first name
        self.send_key(IndividualOnboard.CLICK_ON_FIRST_NAME_XPATH, fname)
        # Enter last name
        self.send_key(IndividualOnboard.CLICK_ON_LAST_NAME_XPATH, lname)
        # Click to open National ID section
        self.do_click(IndividualOnboard.CLICK_ON_NATIONAL_ID_XPATH)
        # Click on 'Primary Date of Issue'
        self.do_click(IndividualOnboard.CLICK_ON_PRIMARY_DATE_OF_ISSUE_XPATH)
        # Enter 'Primary Date of Issue'
        self.send_key(IndividualOnboard.ENTER_PRIMARY_DATE_OF_ISSUE_XPATH, issueDate)
        # Scroll to 'Primary Date of Expiry'
        self.scroll_down_toElement(IndividualOnboard.CLICK_ON_PRIMARY_DATE_OF_EXPIRY_XPATH)
        # Click on 'Primary Date of Expiry'
        self.do_click(IndividualOnboard.CLICK_ON_PRIMARY_DATE_OF_EXPIRY_XPATH)
        # Wait until expiry date input is clickable
        time.sleep(3) # time
        # Enter expiry date
        self.send_key(IndividualOnboard.ENTER_PRIMARY_DATE_OF_EXPIRY_XPATH, expiryDate)
        # Verify 'Date of Birth' field is displayed
        time.sleep(2)# time
        # Click on 'Date of Birth'
        self.do_click(IndividualOnboard.CLICK_ON_PRIMARY_DATE_OF_BIRTH_XPATH)
        # Verify date of birth input is displayed
        time.sleep(2) # time
        # Enter date of birth
        self.send_key(IndividualOnboard.ENTER_PRIMARY_DATE_OF_BIRTH_XPATH, birthDate)
        # Verify nationality field is displayed
        self.is_displayed(IndividualOnboard.CLICK_ON_NATIONALITY_XPATH)  # time
        # Select nationality
        self.do_click(IndividualOnboard.CLICK_ON_NATIONALITY_XPATH)
        self.do_click(IndividualOnboard.SELECT_ITALY_CITY_NATIONALITY_XPATH)
        # Select contact number country code
        self.do_click(IndividualOnboard.CLICK_ON_CONTACT_NUMBER_XPATH)
        self.do_click(IndividualOnboard.SELECT_ITALY_CODE_XPATH)
        # Enter contact number
        self.send_key(IndividualOnboard.ENTER_CONTACT_NUMBER_XPATH, contactNumber)
        # Enter email address
        self.send_key(IndividualOnboard.ENTER_EMAIL_ADDRESS_XPATH, emailId)
        # Select Country of ID Issuance
        # Scroll to 'Cynopsis Screening' section
        self.scroll_down_toElement(IndividualOnboard.CLICK_ON_CYNOPSIS_SCREENING_ONBOARDING_XPATH)
        # Select Cynopsis Screening option
        self.do_click(IndividualOnboard.CLICK_ON_CYNOPSIS_SCREENING_ONBOARDING_XPATH)
        self.do_click(IndividualOnboard.SELECT_FACE_TO_FACE_XPATH)
        # Select payment mode
        self.do_click(IndividualOnboard.CLICK_ON_PAYMENT_MODE_XPATH)
        self.do_click(IndividualOnboard.SELECT_TELEGRAPHIC_TRANSFER_XPATH)
        # select Country of ID Issuance
        self.do_click(IndividualOnboard.CLICK_ON_COUNTRY_ID_INSURANCE_XPATH)
        self.js_click(IndividualOnboard.SELECT_ITALY_COUNTRY_XPATH)
        # Enter ID Number
        self.send_key(IndividualOnboard.ENTER_ID_NUMBER_XPATH, "123213")
        # Select product/service complexity
        self.do_click(IndividualOnboard.CLICK_ON_PRODUCT_SERVICE_COMPLEX_XPATH)
        self.do_click(IndividualOnboard.SELECT_SIMPLE_XPATH)
        # Select source of fund
        self.do_click(IndividualOnboard.CLICK_ON_SOURCE_OF_FUND_XPATH)
        self.do_click(IndividualOnboard.SELECT_LOAN_XPATH)
        # Select screening status
        self.do_click(IndividualOnboard.CLICK_ON_SCREENING_STATUS_XPATH)
        self.do_click(IndividualOnboard.SELECT_CURRENT_XPATH)
        # Select 'No' for PEP status or related field
        self.do_click(IndividualOnboard.SELECT_NO_RADIO_BUTTON_XPATH)
        # Enter bank account details
        self.send_key(IndividualOnboard.ENTER_BANK_ACCOUNT_DETAILS_XPATH, enterBankDetails)
        # Enter additional information
        self.send_key(IndividualOnboard.ENTER_ADDITIOANL_INFORMATION_XPATH, "details")
        # Enter business relationship details
        self.send_key(IndividualOnboard.ENTER_BUSSINESS_RELATIONSHIP_XPATH, "Business name")
        # Select booking centre
        self.scroll_down_toElement(IndividualOnboard.CLICK_ON_BOOKING_CENTRE_XPATH)
        self.do_click(IndividualOnboard.CLICK_ON_BOOKING_CENTRE_XPATH)
        time.sleep(2)
        self.do_click(IndividualOnboard.SELECT_LUGANO_VIA_XPATH)
        # Submit the form
        self.do_click(IndividualOnboard.CLICK_ON_SUBMIT_BUTTON_XPATH)


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
        self.do_click(IndividualOnboard.CLICK_ON_SUBMIT_BUTTON_XPATH)

        # Store success message for validation
        self.form_created = self.get_text(RiskProfile.VALIDATE_MESSAGE_SHOW_XPATH)

    def fill_other_details_page(self):
        """
        Fill out the 'Other Details' page in the onboarding process.
        This includes selecting country/region, entering personal details,
        and submitting the form.
        """

        # Navigate to the 'Other Details' section
        self.do_click(OtherDetials.CLICK_ON_OTHER_DETAILS_PAGE_XPATH)

        # ===== Country & Region of Birth =====
        self.do_click(OtherDetials.CLICK_ON_COUNTRY_DOB_XPATH)  # Open country of birth dropdown
        self.do_click(OtherDetials.SELECT_VALUE_COUNTRY_XPATH)  # Select a country
        self.do_click(OtherDetials.CLICK_ON_REGION_DOB_XPATH)  # Open region of birth dropdown
        self.do_click(OtherDetials.SELECT_VALUE_REGION_XPATH)  # Select a region

        # # ===== Personal Address Details =====
        # self.send_key(OtherDetials.ENTER_PLACE_OF_BIRTH_XPATH, "Amravati")  # Enter place of birth
        # self.send_key(OtherDetials.ENTER_PERMANENT_ADDRESS_XPATH, "Ravi nagar")  # Enter permanent address
        # self.send_key(OtherDetials.ENTER_POSTAL_CODE_XPATH, "444601")  # Enter postal code

        # ===== Permanent Address Country & Region =====
        self.do_click(OtherDetials.CLICK_ON_COUNTRY_ADDRESS_XPATH)  # Open permanent address country dropdown
        self.is_displayed(OtherDetials.SELECT_VALUE_COUNTRY_ADDRESS_XPATH)  # Verify country option is visible
        self.scroll_down_toElement(OtherDetials.SELECT_VALUE_COUNTRY_ADDRESS_XPATH)  # Scroll to country option
        self.js_click(OtherDetials.SELECT_VALUE_COUNTRY_ADDRESS_XPATH)  # Select country via JS click

        # Permanant Address
        self.send_key(OtherDetials.ENTER_PERMANANT_ADDRESS_NEW_XPATH, "Mumbai")

        # Select state/region for permanent address
        self.js_click(OtherDetials.CLICK_ON_PERMANANT_STATE_REGION_ADDRESS_XPATH)  # Open state/region dropdown
        self.js_click(OtherDetials.SELECT_VALUE_PERMANANT_STATE_REGION_ADDRESS_XPATH)  # Select state/region

        # Select city for permanent address
        self.do_click(OtherDetials.CLICK_ON_PERMANANT_CITY_REGION_ADDRESS_XPATH)  # Open city dropdown
        self.do_click(OtherDetials.SELECT_VALUE_PERMANANT_CITY_REGION_ADDRESS_XPATH)  # Select city

        # ===== Submit the Form =====
        self.do_click(IndividualOnboard.CLICK_ON_SUBMIT_BUTTON_XPATH)  # Submit the Other Details form


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

    def go_to_cynopsis_page(self):
        self.do_click(CynopsisDetails.CLICK_ON_CYNOPSIS_DETAILS_PAGE_XPATH)
        self.cynopsis_header = self.get_text(CynopsisDetails.GET_CYNOPSIS_DETAILS_TEXT_XPATH)
        self.get_cynposis_details_percent = self.get_text(CynopsisDetails.GET_CYNOPSIS_DETAILS_PERCENTAGE_XPATH)
        self.get_cynopsis_button = self.is_enable(CynopsisDetails.INITIATE_SCREENING_BUTTON_XPATH)
        self.scroll_down_toElement(CynopsisDetails.GET_CONTACT_NUMBER_XPATH)
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

    def fill_related_memebers_page(self,fname,lname,dob):
        self.do_click(RelatedMembersLocators.CLICK_ON_RELATED_MEMBER_PAGE_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_ADD_ANOTHER_BUTTON_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_NO_RADIO_BUTTON_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_SELECT_MEMEBER_TYPE_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.SELECT_INDIVIDUAL_FROM_MEMBER_TYPE_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_CONFOIM_BUTTOM_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_MARITAL_STATUS_DROPDOWN_XPATH)
        self.do_click((RelatedMembersLocators.SELECT_VALUE_FROM_MARITAL_STATUS_DROPDOWN_XPATH))
        self.do_click(RelatedMembersLocators.CLICK_ON_RELATION_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.SELECT_VALUE_FROM_RELATION_STATUS_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.CLICK_ON_TITLE_DROPDOWN_XPATH)
        self.do_click(RelatedMembersLocators.SELECT_VALUE_FROM_TITLE_STATUS_DROPDOWN_XPATH)
        self.send_key(RelatedMembersLocators.ENTER_FIRST_NAME_XPATH,fname)
        self.send_key(RelatedMembersLocators.ENTER_LAST_NAME_XPATH,lname)
        self.do_click(RelatedMembersLocators.CLICK_ON_DATE_OF_BIRTH_XPATH)
        self.send_key(RelatedMembersLocators.ENTER_DATE_OF_BIRTH_XPATH, dob)
        self.do_click(RelatedMembersLocators.CLICK_ON_NATIONAL_ID_RADIO_BUTTON_XPATH)
        time.sleep(4)

    # def go_to_crp_details_fields(self):



















