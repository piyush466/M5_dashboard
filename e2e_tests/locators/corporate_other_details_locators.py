from selenium.webdriver.common.by import By


class CorporateOtherDetials:

    CLICK_ON_OTHER_DETAILS_PAGE_XPATH = (By.XPATH, "//*[text()='Other Details']")

    # select birthInformationCountryOfBirth
    CLICK_ON_COUNTRY_DOB_XPATH = (
        By.XPATH,
        "//div[@id='birthInformationCountryOfBirth']//button"
    )

    SELECT_VALUE_COUNTRY_XPATH = (
        By.XPATH,
        "//*[text()='Italy']"
    )

    # select birthInformationRegionOfBirth
    CLICK_ON_REGION_DOB_XPATH = (
        By.XPATH,
        "//div[@id='birthInformationRegionOfBirth']//button"
    )

    SELECT_VALUE_REGION_XPATH = (
        By.XPATH,
        "//*[text()='Veneto']"
    )

    ENTER_PLACE_OF_BIRTH_XPATH = (
        By.XPATH,
        "//input[@id='birthInformationPlaceOfBirth']"
    )

    ENTER_PERMANENT_ADDRESS_XPATH = (
        By.XPATH,
        "//input[@id='permanentAddress']"
    )

    ENTER_POSTAL_CODE_XPATH = (
        By.XPATH,
        "//input[@id='permanentAddressPostalCode']"
    )

    # select permanentAddressCountry
    CLICK_ON_COUNTRY_ADDRESS_XPATH = (
        By.XPATH,
        "//div[@id='permanentAddressCountry']//button"
    )

    SELECT_VALUE_COUNTRY_ADDRESS_XPATH = (
        By.XPATH,
        "//*[text()='Andorra']"
    )

    # select permanentAddressStateRegion
    CLICK_ON_PERMANANT_STATE_REGION_ADDRESS_XPATH = (
        By.XPATH,
        "//div[@id='permanentAddressStateRegion']//button"
    )

    SELECT_VALUE_PERMANANT_STATE_REGION_ADDRESS_XPATH = (
        By.XPATH,
        "//*[text()='Canillo']"
    )

    # select permanentAddressCity
    CLICK_ON_PERMANANT_CITY_REGION_ADDRESS_XPATH = (
        By.XPATH,
        "//div[@id='permanentAddressCity']//button"
    )

    SELECT_VALUE_PERMANANT_CITY_REGION_ADDRESS_XPATH = (
        By.XPATH,
        "//*[text()='Others']"
    )

    ENTER_PERMANANT_ADDRESS_NEW_XPATH = (
        By.XPATH,
        "//input[@id='permanentAddress']"
    )

    ENTER_CORPORATE_REGISTER_ADDRESS_XPATH = (
        By.XPATH, "//input[@id='registeredAddress']"
    )

    #ENTER THE Ownership Structure Layers

    CLICK_ON_OWNERSHIP_STRUCTURE_LAYER_XPATH = (
        By.XPATH, ""
    )

class CorporateCynopsisDetails:

    CLICK_ON_CYNOPSIS_DETAILS_PAGE_XPATH = (
        By.XPATH, "//span[text()='Cynopsis Details']"
    )

    GET_CYNOPSIS_DETAILS_TEXT_XPATH = (
        By.XPATH, "//*[text()='Corporate Cynopsis Details']"
    )

    GET_CYNOPSIS_DETAILS_PERCENTAGE_XPATH = (
        By.XPATH, "//*[text()='Cynopsis Details']/parent::div/parent::div/div[2]/div/span[text()='100']"
    )

    INITIATE_SCREENING_BUTTON_XPATH = (
        By.XPATH, "//*[contains(text(),'Initiate Screening')]"
    )

    GET_DATE_OF_ISSUE_XAPTH = (
        By.XPATH, "//*[text()='Date of Issue']//parent::div/div/button/button"
    )

    GET_USER_EMAIL_ID_XPATH = (
        By.XPATH, "//*[text()='Email ID']//parent::div/div/input[@id='emailId']"
    )

    GET_DATE_OF_EXPIRY_XPATH = (
        By.XPATH, "//*[text()='Date of Expiry']//parent::div/div/button/button"
    )

    GET_DATE_OF_BIRTH_XPATH = (
        By.XPATH, "//*[text()='Date of Birth']//parent::div/div/button/button"
    )

    GET_CONTACT_NUMBER_XPATH = (
        By.XPATH, "//*[text()='Contact Number']//parent::div/div/input"
    )

    GET_ENTITY_NAME_XPATH = (
        By.XPATH, "//input[@id='entityName']"
    )

    GET_REGISTRATION_NUMBER_XPATH = (
        By.XPATH, "//input[@id='registrationNumber']"
    )

    GET_CONTACT_NUMBER_CYNOPSIS_XPATH = (
        By.XPATH, "//input[@id='contactNumber']"
    )

    GET_EMAIL_ID_XPATH = (
        By.XPATH, "//input[@id='emailId']"
    )

    # CRP Details Sections

    GET_CRP_FIRST_NAME_XPATH = (
        By.XPATH, "//*[text()='First Name']//parent::div/div/div/input"
    )

    GET_CRP_LAST_NAME_XPATH = (
        By.XPATH, "//*[text()='Last Name']//parent::div/div/div/input"
    )

    GET_CRP_DATE_OF_BIRTH_XPATH = (
        By.XPATH, "//*[text()='Date of Birth']//parent::div/div/div/div/button/button"
    )


class CorporateCynopsisResult:

    CLICK_ON_CYNOPSIS_DETAILS_PAGE_XPATH = (
        By.XPATH, "//span[text()='Cynopsis Result']"
    )

    GET_CYNOPSIS_RESULT_TEXT_XPATH = (
        By.XPATH, "//div[text()='Cynopsis Result']"
    )

    GET_CYNOPSIS_RESULT_PAGE_TEXT_XPATH = (
        By.XPATH, "//p[text()='Initiate the Screening Process to see the Cynopsis Result']"
    )

    GET_USER_CLIENT_NAME_XPATH = (
        By.XPATH, "(//h2)[1]"
    )