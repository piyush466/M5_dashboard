from selenium.webdriver.common.by import By


class CorporateOnboard:

    # ------- Basic Details Form locators -------

    # Menu option to go to Client Onboarding
    SELECT_CLIENT_ONBOARDING_XPATH = (By.XPATH, "//*[contains(text(),'Client Onboarding')]")

    # Button to start new onboarding
    CLICK_ON_ONBOARD_NEW_BUTTON = (By.XPATH, "//button//span[normalize-space()='Onboard New']")

    # Option to select 'Corporate' onboarding type
    CLICK_ON_CORPORATE_XPATH = (By.XPATH, "//span[text()='Corporate']")

    # Radio button to select 'No' option
    SELECT_RADIO_BUTTON_NO_ID = (By.ID, "no")

    # Proceed button in onboarding flow
    CLICK_ON_PROCEED_BUTTON_XPATH = (By.XPATH, "//*[contains(text(),'Proceed')]")

    # Text label to verify the 'Corporate Basic Details' form is opened
    TEXT_CORPORATE_BASIC_DETAILS_FORM_XPATH = (
        By.XPATH,
        "//*[contains(text(),'Corporate Basic Details')]"
    )

    # ------- Basic Details Form fields -------

    # Gender dropdown button
    CLICK_ON_SELECT_GENDER_XPATH = (By.XPATH, "//div[@id='gender']//button")

    # Option 'Male' in gender dropdown
    SELECT_MALE_FROM_DROPDOWN_XPATH = (By.XPATH, "//*[text()='Male']")

    # Title dropdown button
    CLICK_ON_SELECT_TITLE_XPATH = (By.XPATH, "//div[@id='title']//button")

    # Option 'Mr' in title dropdown
    SELECT_MR_FROM_DROPDOWN_XPATH = (By.XPATH, "//*[text()='Mr']")

    # First name input field
    CLICK_ON_FIRST_NAME_XPATH = (By.XPATH, "//div[@id='firstName']//input")

    # Last name input field
    CLICK_ON_LAST_NAME_XPATH = (By.XPATH, "//div[@id='lastName']//input")

    # 'National ID' section
    CLICK_ON_NATIONAL_ID_XPATH = (By.XPATH, "//*[contains(text(),'National ID')]")

    # Primary ID - Date of Issue
    CLICK_ON_PRIMARY_DATE_OF_ISSUE_XPATH = (
        By.XPATH,
        "//div[@id='primaryIdDateOfIssue']//button"
    )
    ENTER_PRIMARY_DATE_OF_ISSUE_XPATH = (
        By.XPATH,
        "//input[@placeholder='Select date']"
    )

    # Primary ID - Date of Expiry
    CLICK_ON_PRIMARY_DATE_OF_EXPIRY_XPATH = (
        By.XPATH,
        "//div[@id='primaryIdDateOfExpiry']//button"
    )
    ENTER_PRIMARY_DATE_OF_EXPIRY_XPATH = (
        By.XPATH,
        "//input[@placeholder='Select date']"
    )

    # Primary ID - Date of Birth
    CLICK_ON_PRIMARY_DATE_OF_BIRTH_XPATH = (
        By.XPATH,
        "//div[@id='primaryIdDateOfBirth']//button"
    )
    ENTER_PRIMARY_DATE_OF_BIRTH_XPATH = (
        By.XPATH,
        "//input[@placeholder='Select date']"
    )

    # Nationality dropdown
    CLICK_ON_NATIONALITY_XPATH = (
        By.XPATH,
        "//div[@id='primaryIdNationality']//button"
    )
    SELECT_ITALY_CITY_NATIONALITY_XPATH = (
        By.XPATH,
        "//*[text()='Italy']"
    )

    # Contact number country code dropdown
    CLICK_ON_CONTACT_NUMBER_XPATH = (
        By.XPATH,
        "//div[@id='contactNumber']//button"
    )
    SELECT_ITALY_CODE_XPATH = (
        By.XPATH,
        "//*[text()='+39 (Italy)']"
    )

    # Contact number input field
    ENTER_CONTACT_NUMBER_XPATH = (
        By.XPATH,
        "(//*[@id='contactNumber'])[2]"
    )

    # Email address input field
    ENTER_EMAIL_ADDRESS_XPATH = (
        By.XPATH,
        "//input[@id='emailId']"
    )

    # Country of ID Issuance
    CLICK_ON_COUNTRY_ID_INSURANCE_XPATH = (
        By.XPATH,
        "//div[@id='primaryIdCountryOfIssuance']//button"
    )
    SELECT_ITALY_COUNTRY_XPATH = (
        By.XPATH,
        "(//*[text()='Italy'])[2]"
    )

    # Enter ID Number
    ENTER_ID_NUMBER_XPATH = (
        By.XPATH,
        "//input[@id='primaryIdIdNumber']"
    )

    # Cynopsis Screening - Onboarding Mode dropdown
    CLICK_ON_CYNOPSIS_SCREENING_ONBOARDING_XPATH = (
        By.XPATH,
        "//div[@id='cynopsisScreeningOnboardingMode']//button"
    )
    SELECT_FACE_TO_FACE_XPATH = (
        By.XPATH,
        "//*[text()='Face to Face']"
    )

    # Cynopsis Screening - Payment Mode dropdown
    CLICK_ON_PAYMENT_MODE_XPATH = (
        By.XPATH,
        "//div[@id='cynopsisScreeningPaymentMode']//button"
    )
    SELECT_TELEGRAPHIC_TRANSFER_XPATH = (
        By.XPATH,
        "//*[text()='Telegraphic Transfer']"
    )

    # Cynopsis Screening - Product/Service Complexity dropdown
    CLICK_ON_PRODUCT_SERVICE_COMPLEX_XPATH = (
        By.XPATH,
        "//div[@id='cynopsisScreeningProductServiceComplexity']//button"
    )
    SELECT_SIMPLE_XPATH = (
        By.XPATH,
        "//*[text()='Simple']"
    )

    # Cynopsis Screening - Source of Funds dropdown
    CLICK_ON_SOURCE_OF_FUND_XPATH = (
        By.XPATH,
        "//div[@id='cynopsisScreeningSourceOfFunds']//button"
    )
    SELECT_LOAN_XPATH = (
        By.XPATH,
        "//*[text()='Loan']"
    )

    # Cynopsis Screening - Status dropdown
    CLICK_ON_SCREENING_STATUS_XPATH = (
        By.XPATH,
        "//div[@id='cynopsisScreeningStatus']//button"
    )
    SELECT_CURRENT_XPATH = (
        By.XPATH,
        "//*[text()='Current']"
    )

    # Cynopsis Screening - 'Undischarged Bankrupt' No option
    SELECT_NO_RADIO_BUTTON_XPATH = (
        By.XPATH,
        "//*[@for='cynopsisScreeningUndischargedBankrupt-no']"
    )

    # Bank account details textarea
    ENTER_BANK_ACCOUNT_DETAILS_XPATH = (
        By.XPATH,
        "//textarea[@id='cynopsisScreeningBankAccount']"
    )

    # Additional information textarea
    ENTER_ADDITIOANL_INFORMATION_XPATH = (
        By.XPATH,
        "//textarea[@id='cynopsisScreeningAdditionalInformation']"
    )

    # Nature of business relationship textarea
    ENTER_BUSSINESS_RELATIONSHIP_XPATH = (
        By.XPATH,
        "//textarea[@id='cynopsisScreeningNatureOfBusinessRelationship']"
    )

    # Booking centre dropdown
    CLICK_ON_BOOKING_CENTRE_XPATH = (
        By.XPATH,
        "//div[@id='bookingCentre']//button"
    )
    SELECT_LUGANO_VIA_XPATH = (
        By.XPATH,
        "//*[text()='Lugano - Via Giuseppe Cattori 126900']"
    )

    # ------- End of Basic Details Form -------

    # Submit button at the end of form
    CLICK_ON_SUBMIT_BUTTON_XPATH = (
        By.XPATH,
        "//*[text()='Submit']"
    )

    # Basic details form corporate

    # enter the entity name
    ENTER_ENTITY_NAME_XPATH = (
        By.XPATH, "//input[@id='entityName']"
    )
    # enter the registtration number
    ENTER_REGISTRATION_NUMBER_XPATH = (
        By.XPATH, "//input[@id='registrationNumber']"
    )
    # enter the contact number
    CLICK_CORPORATE_ITALY_CODE_XPATH = (By.XPATH, "//div[@id='contactNumber']//button")

    SELECT_CORPORATE_ITALY_CODE_XPATH = (By.XPATH, "//*[text()='+39 (Italy)']")

    ENTER_CORPORATE_CONTACT_NUMBER_XPATH = (
        By.XPATH, "//input[@id='contactNumber']"
    )

    # enter email id
    ENTER_EMAIL_ID_XPATH = (
        By.XPATH, "//input[@id='emailId']"
    )

    #select entity type
    CLICK_ON_ENTITY_TYPE_XPATH = (
        By.XPATH, "//div[@id='entityType']/button"
    )
     #select charity from dropdown
    SELECT_ENTITY_TYPE_XPATH = (
        By.XPATH, "//*[text()='Club']"
    )

    # click on cynopsis screenin status field
    CLICK_ON_CORPORATE_SCREENING_STATUS_XPATH = (
        By.XPATH, "//div[@id='cynopsisScreeningStatus']/button"
    )

    CLICK_ON_CORP_CURRENT_XPATH = (
        By.XPATH, "//*[text()='Current']"
    )

    #click on country of corporation

    CLICK_ON_CORP_COUNTRY_OF_CORPRATION_XPATH =(
        By.XPATH, "//div[@id='cynopsisScreeningCountryOfOperation']/button"
    )

    SELECT_COUNTRY_OF_CORPORATION_XPATH = (
        By.XPATH, "//*[text()='Italy']"
    )

    # click on Ownership Structure Layers
    CLICK_ON_OWNERSHIP_STRUCUTE_LAYER_XPATH = (
        By.XPATH, "//div[@id='cynopsisScreeningOwnershipStructureLayers']/button"
    )

    SELECT_OWNERSHIP_STRUCUTE_LAYER_XPATH = (
        By.XPATH, "//*[text()='1']"
    )

    # CLICK ON Industry
    CLICK_ON_CORP_INDUSTRY_XPATH = (
        By.XPATH, "//div[@id='cynopsisIndustryInternational']/button"
    )

    SELECT_INDUSTRY_XPATH = (
        By.XPATH, "//*[text()='ANTIQUES & ARTPIECE']"
    )


